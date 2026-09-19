# -*- coding: utf-8 -*-
"""صفحة الريلز المتحركة — نسخة موسّعة. الاستخدام: python3 reel_scene.py <المدة بالثواني> <ملف الخرج>"""
import io, os, sys, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORNER = io.open(os.path.join(ROOT, 'tools', 'corner.svg'), encoding='utf-8').read()
ORN = CORNER[CORNER.index('>')+1: CORNER.rindex('</svg>')]

DUR  = float(sys.argv[1]) if len(sys.argv) > 1 else 30.0
OUT  = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'share', 'reel.html')
R    = random.Random(9)

# ── جدول المشاهد (بداية، نهاية) بالثواني ──
if DUR <= 35:
    P = {'a': (0.0, 5.6), 'b': (5.3, 10.8), 'c': (10.5, 18.0),
         'd': (17.7, 22.8), 'e': (22.5, 26.6), 'f': (26.3, DUR)}
else:
    P = {'a': (0.0, 9.0), 'b': (8.6, 17.5), 'c': (17.1, 30.0),
         'd': (29.6, 39.0), 'e': (38.6, 47.0), 'f': (46.6, DUR)}

def pct(t):
    return round(t / DUR * 100.0, 3)

def vis(key, fade=0.55):
    """كيفريمز ظهور/اختفاء المشهد على تايم‌لاين واحد"""
    s, e = P[key]
    a, b = pct(s), pct(min(s + fade, e))
    c, d = pct(max(e - fade, s)), pct(e)
    if s <= 0.001:
        return '0%%,%s%%{opacity:1}%s%%,100%%{opacity:0}' % (c, d)
    if abs(e - DUR) < 0.01:
        return '0%%,%s%%{opacity:0}%s%%,100%%{opacity:1}' % (a, b)
    return '0%%,%s%%{opacity:0}%s%%,%s%%{opacity:1}%s%%,100%%{opacity:0}' % (a, b, c, d)

def at(key, off):
    """توقيت مطلق داخل المشهد"""
    return '%.2fs' % (P[key][0] + off)

# ── الورد المتساقط بطبقتين ──
def petals(n, blur, smin, smax, dmin, dmax, op):
    cols = ['rgba(190,154,96,%.2f)', 'rgba(217,188,133,%.2f)', 'rgba(149,115,62,%.2f)', 'rgba(242,228,200,%.2f)']
    out = []
    for _ in range(n):
        sz = R.uniform(smin, smax)
        out.append('<span class="pt" style="left:%.1f%%;width:%.1fpx;height:%.1fpx;background:%s;'
                   'animation-duration:%.1fs;animation-delay:-%.1fs;--dx:%.0fpx"></span>'
                   % (R.uniform(-5, 103), sz, sz*0.72, (R.choice(cols) % op),
                      R.uniform(dmin, dmax), R.uniform(0, dmax), R.uniform(-160, 160)))
    return '<div class="petals" style="filter:blur(%.1fpx)">%s</div>' % (blur, ''.join(out))

MONO = u'''<svg class="mono" viewBox="0 0 220 220">
  <circle class="r1" cx="110" cy="110" r="99" fill="none" stroke="currentColor" stroke-width="1.1" opacity=".5"/>
  <circle class="r2" cx="110" cy="110" r="90" fill="none" stroke="currentColor" stroke-width=".7" opacity=".3"/>
  <g class="dia" fill="currentColor" opacity=".55">
    <path d="M110 5.4 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/><path d="M110 205.8 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/>
    <path d="M10 105.6 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/><path d="M210.2 105.6 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/>
  </g>
  <g class="gly" fill="currentColor" font-family="Aref Ruqaa, Amiri, serif" font-weight="700" text-anchor="middle">
    <text x="128" y="146" font-size="123">&#1593;</text><text x="92" y="160" font-size="123">&#1582;</text>
  </g>
</svg>'''
MONO_S = MONO.replace('class="r1"', 'class="r1 st"').replace('class="r2"', 'class="r2 st"') \
             .replace('class="dia"', 'class="dia st"').replace('class="gly"', 'class="gly st"')

def orns(keys, key, base=0.0, step=0.13, cls=''):
    return ''.join('<svg class="orn %s %s" viewBox="0 0 300 300" style="animation-delay:%s">%s</svg>'
                   % (c, cls, at(key, base + i*step), ORN) for i, c in enumerate(keys))

CSS = u'''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#FDF9F1}
body{font-family:'IBM Plex Sans Arabic',sans-serif;font-weight:300;color:#333E42;direction:rtl;text-align:center;position:relative}
.scene{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0}
.sa{animation:ka __D__s linear both}.sb{animation:kb __D__s linear both}.sc{animation:kc __D__s linear both}
.sd{animation:kd __D__s linear both}.se{animation:ke __D__s linear both}.sf{animation:kf __D__s linear both}
@keyframes ka{__KA__}@keyframes kb{__KB__}@keyframes kc{__KC__}
@keyframes kd{__KD__}@keyframes ke{__KE__}@keyframes kf{__KF__}

/* توهّج ذهبي بيتنفّس */
.glow{position:absolute;width:1500px;height:1500px;border-radius:50%;pointer-events:none;
  background:radial-gradient(circle,rgba(217,188,133,.22),transparent 62%);
  animation:breathe __D__s ease-in-out infinite}
@keyframes breathe{0%,100%{transform:scale(.9);opacity:.55}50%{transform:scale(1.06);opacity:.9}}

/* الورد في الأركان */
.orn{position:absolute;width:440px;height:auto;opacity:0}
.orn.a{top:0;left:0;animation:oa 1.5s cubic-bezier(.2,.85,.3,1) both}
.orn.b{top:0;right:0;animation:ob 1.5s cubic-bezier(.2,.85,.3,1) both}
.orn.c{bottom:0;left:0;animation:oc 1.5s cubic-bezier(.2,.85,.3,1) both}
.orn.d{bottom:0;right:0;animation:od 1.5s cubic-bezier(.2,.85,.3,1) both}
@keyframes oa{from{opacity:0;transform:scale(.8) rotate(-7deg) translate(-30px,-30px)}to{opacity:.62;transform:none}}
@keyframes ob{from{opacity:0;transform:scaleX(-1) scale(.8) rotate(7deg) translate(-30px,-30px)}to{opacity:.62;transform:scaleX(-1)}}
@keyframes oc{from{opacity:0;transform:scaleY(-1) scale(.8) rotate(7deg) translate(-30px,-30px)}to{opacity:.62;transform:scaleY(-1)}}
@keyframes od{from{opacity:0;transform:scale(-.8,-.8) rotate(-7deg) translate(30px,30px)}to{opacity:.62;transform:scale(-1,-1)}}
.orn.sm{width:330px}

/* المونوجرام */
.mono{width:300px;height:auto;color:#95733E}
.mono .r1{stroke-dasharray:622;stroke-dashoffset:622;animation:draw 1.7s ease __M1__ both}
.mono .r2{stroke-dasharray:566;stroke-dashoffset:566;animation:draw 1.7s ease __M2__ both}
.mono .dia{opacity:0;animation:fdi 1s ease __M3__ both}
.mono .gly{opacity:0;transform-origin:110px 130px;animation:gly 1.1s cubic-bezier(.2,.9,.3,1.25) __M4__ both}
.mono .st{animation:none!important;stroke-dashoffset:0;opacity:1;transform:none}
.mono .dia.st{opacity:.55}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes gly{from{opacity:0;transform:scale(.84)}to{opacity:1;transform:none}}
@keyframes fdi{from{opacity:0}to{opacity:.55}}

/* نبضة الختم */
.ring{position:absolute;width:300px;height:300px;border-radius:50%;border:2px solid rgba(190,154,96,.75);
  opacity:0;transform:scale(.8);pointer-events:none}
@keyframes ripple{0%{opacity:.8;transform:scale(.82)}100%{opacity:0;transform:scale(1.75)}}

/* حركات عامة */
.up{opacity:0;animation:up 1.05s cubic-bezier(.2,.85,.3,1) both}
@keyframes up{from{opacity:0;transform:translateY(42px)}to{opacity:1;transform:none}}
.fi{opacity:0;animation:fi 1.15s ease both}
@keyframes fi{from{opacity:0}to{opacity:1}}
.rx{opacity:0;animation:rx 1.1s cubic-bezier(.2,.85,.3,1) both}
@keyframes rx{from{opacity:0;transform:translateX(-64px)}to{opacity:1;transform:none}}
.lx{opacity:0;animation:lx 1.1s cubic-bezier(.2,.85,.3,1) both}
@keyframes lx{from{opacity:0;transform:translateX(64px)}to{opacity:1;transform:none}}
.pop{opacity:0;animation:pop .95s cubic-bezier(.2,.9,.3,1.5) both}
@keyframes pop{from{opacity:0;transform:scale(.72)}to{opacity:1;transform:none}}

/* كشف سطر بقناع (يمين ← شمال) */
.wipe{clip-path:inset(0 0 0 100%);animation:wp 1.15s cubic-bezier(.55,0,.2,1) both}
@keyframes wp{to{clip-path:inset(0 0 0 0)}}

/* لمعة ذهبية على النص */
.shine{background:linear-gradient(100deg,#1E2A2E 0 40%,#E0C48A 50%,#1E2A2E 60% 100%);
  background-size:260% 100%;background-position:-70% 0;
  -webkit-background-clip:text;background-clip:text;color:transparent;
  opacity:0;animation:shn 2.1s ease both}
@keyframes shn{
  0%{background-position:190% 0;opacity:0;transform:translateY(34px)}
  22%{opacity:1;transform:none}
  100%{background-position:-70% 0;opacity:1;transform:none}}

/* الخط الذهبي */
.rule{display:flex;align-items:center;gap:26px;width:520px;margin:44px auto}
.rule i{flex:1;height:1px;background:linear-gradient(90deg,transparent,#BE9A60,transparent);transform:scaleX(0);animation:gw 1.05s cubic-bezier(.2,.85,.3,1) both}
.rule b{width:15px;height:15px;background:#BE9A60;transform:rotate(45deg) scale(0);animation:db .75s cubic-bezier(.2,.9,.3,1.5) both}
@keyframes gw{to{transform:scaleX(1)}}
@keyframes db{to{transform:rotate(45deg) scale(1)}}

.kick{font-size:31px;color:#6D787C;word-spacing:.55em;margin-top:46px}
.ayah{font-family:'Amiri',serif;font-size:50px;line-height:2.15;max-width:880px}
.src{font-size:27px;color:#95733E;word-spacing:.3em;margin-top:26px}
.names{font-family:'Aref Ruqaa',serif;font-weight:700;font-size:122px;line-height:1.55;color:#1E2A2E;display:flex;align-items:center;justify-content:center;gap:34px}
.names em{font-family:'Amiri',serif;font-style:normal;color:#BE9A60;font-size:.46em}
.big{font-family:'Amiri',serif;font-weight:700;font-size:225px;color:#95733E;line-height:1.05}
.lbl{font-size:35px;color:#6D787C;word-spacing:.4em}
.val{font-family:'Amiri',serif;font-weight:700;font-size:68px;color:#1E2A2E;line-height:1.7}
.sub{font-size:35px;color:#6D787C;line-height:2}

/* الصورة داخل قوس */
.archwrap{position:absolute;top:0;left:0;width:1080px;height:1360px;display:grid;place-items:center}
.arch{width:940px;height:1250px;overflow:hidden;position:relative;
  border-radius:470px 470px 26px 26px;
  clip-path:inset(50% 0 50% 0 round 470px 470px 26px 26px);
  animation:arch 1.4s cubic-bezier(.6,0,.2,1) __CA__ both}
@keyframes arch{to{clip-path:inset(0 0 0 0 round 470px 470px 26px 26px)}}
.arch img{width:100%;height:100%;object-fit:cover;object-position:center 15%;display:block;
  animation:kb2 __CK__s ease-out __CA__ both}
@keyframes kb2{from{transform:scale(1.1)}to{transform:scale(1)}}
.archline{position:absolute;top:0;left:0;width:1080px;height:1360px;display:grid;place-items:center;pointer-events:none}
.archline span{width:972px;height:1282px;border:1.5px solid rgba(190,154,96,.55);border-radius:486px 486px 32px 32px;
  opacity:0;transform:scale(.97);animation:al 1.3s cubic-bezier(.2,.85,.3,1) __CL__ both}
@keyframes al{to{opacity:1;transform:none}}
.below{position:absolute;left:0;right:0;top:1360px;bottom:0;background:#FDF9F1;display:flex;flex-direction:column;align-items:center;justify-content:center}
.medal{width:236px;height:236px;border-radius:50%;background:#FDF9F1;display:grid;place-items:center;
  margin:-118px auto -40px;position:relative;z-index:3;box-shadow:0 12px 40px rgba(30,42,46,.14)}
.medal .mono{width:198px}

/* الورد المتساقط */
.petals{position:absolute;inset:0;pointer-events:none;z-index:6;overflow:hidden}
.pt{position:absolute;top:-9%;border-radius:60% 6% 60% 6%;opacity:0;animation-name:fall;animation-timing-function:linear;animation-iteration-count:infinite}
@keyframes fall{0%{transform:translate3d(0,-9vh,0) rotate(0);opacity:0}9%{opacity:1}90%{opacity:.85}100%{transform:translate3d(var(--dx),118vh,0) rotate(600deg);opacity:0}}

.prog{position:absolute;left:0;bottom:0;height:5px;width:100%;transform-origin:right;transform:scaleX(0);
  background:linear-gradient(90deg,#95733E,#D9BC85);z-index:9;animation:pg __D__s linear both}
@keyframes pg{to{transform:scaleX(1)}}
.vig{position:absolute;inset:0;pointer-events:none;z-index:5;
  background:radial-gradient(132% 92% at 50% 45%, transparent 55%, rgba(120,95,60,.11) 100%)}
'''

BODY = u'''
<div class="glow" style="top:-260px;right:-320px"></div>
<div class="glow" style="bottom:-300px;left:-340px"></div>

<!-- ═══ أ · الافتتاح ═══ -->
<section class="scene sa">
  __ORN_A__
  <div style="position:relative;display:grid;place-items:center">
    <span class="ring" style="animation:ripple 1.9s ease __RA__ both"></span>
    __MONO__
  </div>
  <p class="kick up" style="animation-delay:__A1__">دعوة&nbsp; زفاف</p>
  <div class="rule"><i style="animation-delay:__A2__"></i><b style="animation-delay:__A3__"></b><i style="animation-delay:__A2__"></i></div>
  <p class="names shine" style="font-size:104px;animation-delay:__A4__">عبدالله <em>&amp;</em> خلود</p>
</section>

<!-- ═══ ب · الآية ═══ -->
<section class="scene sb">
  __ORN_B__
  <p class="ayah"><span class="wipe" style="display:inline-block;animation-delay:__B1__">﴿ وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا</span><br>
  <span class="wipe" style="display:inline-block;animation-delay:__B2__">لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ﴾</span></p>
  <div class="rule"><i style="animation-delay:__B3__"></i><b style="animation-delay:__B4__"></b><i style="animation-delay:__B3__"></i></div>
  <p class="src fi" style="animation-delay:__B5__">سورة&nbsp; الروم</p>
</section>

<!-- ═══ ج · الصورة والأسماء ═══ -->
<section class="scene sc">
  <div class="archwrap"><div class="arch"><img src="../images/couple.jpg"></div></div>
  <div class="archline"><span></span></div>
  <div class="below">
    <svg class="orn c sm" viewBox="0 0 300 300" style="animation-delay:__C4__">__ORN__</svg>
    <svg class="orn d sm" viewBox="0 0 300 300" style="animation-delay:__C5__">__ORN__</svg>
    <div class="medal pop" style="animation-delay:__C2__">__MONO_S__</div>
    <h1 class="names">
      <span class="up" style="animation-delay:__C3__">عبدالله</span>
      <em class="fi" style="animation-delay:__C6__">&amp;</em>
      <span class="up" style="animation-delay:__C7__">خلود</span>
    </h1>
  </div>
</section>

<!-- ═══ د · التاريخ ═══ -->
<section class="scene sd">
  __ORN_D__
  <p class="lbl fi" style="animation-delay:__D1__">بكل الحب ندعوكم يوم</p>
  <p class="val rx" style="font-size:82px;margin-top:16px;animation-delay:__D2__">السبت</p>
  <p class="big pop" style="animation-delay:__D3__">10</p>
  <p class="val lx" style="animation-delay:__D4__">أكتوبر &nbsp;2026</p>
  <div class="rule"><i style="animation-delay:__D5__"></i><b style="animation-delay:__D6__"></b><i style="animation-delay:__D5__"></i></div>
  <p class="sub fi" style="animation-delay:__D7__">من الثالثة عصرًا حتى السابعة مساءً</p>
</section>

<!-- ═══ هـ · المكان ═══ -->
<section class="scene se">
  __ORN_E__
  <p class="lbl fi" style="animation-delay:__E1__">المكان</p>
  <p class="val up" style="font-size:78px;margin-top:18px;animation-delay:__E2__">قاعة سندريلا<br>قصر الأميرات</p>
  <div class="rule"><i style="animation-delay:__E3__"></i><b style="animation-delay:__E4__"></b><i style="animation-delay:__E3__"></i></div>
  <p class="sub fi" style="animation-delay:__E5__">حديقة العاشر من رمضان، شارع الطيران<br>الحي السابع، مدينة نصر، القاهرة</p>
</section>

<!-- ═══ و · الختام ═══ -->
<section class="scene sf">
  __ORN_F__
  <div style="position:relative;display:grid;place-items:center">
    <span class="ring" style="animation:ripple 2.1s ease __RF__ both"></span>
    <span class="ring" style="animation:ripple 2.1s ease __RF2__ both"></span>
    <div class="pop" style="animation-delay:__F1__">__MONO_S2__</div>
  </div>
  <h1 class="names shine" style="font-size:100px;margin-top:46px;animation-delay:__F2__">عبدالله <em>&amp;</em> خلود</h1>
  <div class="rule"><i style="animation-delay:__F3__"></i><b style="animation-delay:__F4__"></b><i style="animation-delay:__F3__"></i></div>
  <p class="sub fi" style="font-size:43px;animation-delay:__F5__">في انتظاركم لمشاركتنا فرحتنا</p>
  <p class="sub fi" style="font-size:27px;color:#95733E;margin-top:46px;direction:ltr;animation-delay:__F6__">abdallahghorap1212.github.io/wedding-abdallah-kholoud</p>
</section>

<div class="vig"></div>
__PETALS_BACK__
__PETALS_FRONT__
<i class="prog"></i>
'''

css = (CSS.replace('__D__', '%g' % DUR)
          .replace('__KA__', vis('a')).replace('__KB__', vis('b')).replace('__KC__', vis('c'))
          .replace('__KD__', vis('d')).replace('__KE__', vis('e')).replace('__KF__', vis('f'))
          .replace('__M1__', at('a', 0.5)).replace('__M2__', at('a', 0.75))
          .replace('__M3__', at('a', 1.6)).replace('__M4__', at('a', 1.65))
          .replace('__CA__', at('c', 0.15)).replace('__CK__', '%g' % (P['c'][1]-P['c'][0]))
          .replace('__CL__', at('c', 1.1)))

body = (BODY.replace('__ORN_A__', orns('abcd', 'a', 0.15))
            .replace('__ORN_B__', orns('abcd', 'b', 0.05, 0.1))
            .replace('__ORN_D__', orns('abcd', 'd', 0.05, 0.1))
            .replace('__ORN_E__', orns('abcd', 'e', 0.05, 0.1))
            .replace('__ORN_F__', orns('abcd', 'f', 0.05, 0.1))
            .replace('__RA__', at('a', 1.6)).replace('__RF__', at('f', 0.5)).replace('__RF2__', at('f', 1.0))
            .replace('__A1__', at('a', 2.35)).replace('__A2__', at('a', 2.75)).replace('__A3__', at('a', 3.0))
            .replace('__A4__', at('a', 3.1))
            .replace('__B1__', at('b', 0.35)).replace('__B2__', at('b', 0.75))
            .replace('__B3__', at('b', 1.7)).replace('__B4__', at('b', 1.95)).replace('__B5__', at('b', 2.1))
            .replace('__C2__', at('c', 1.5)).replace('__C3__', at('c', 2.0))
            .replace('__C4__', at('c', 1.7)).replace('__C5__', at('c', 1.85))
            .replace('__C6__', at('c', 2.35)).replace('__C7__', at('c', 2.55))
            .replace('__D1__', at('d', 0.15)).replace('__D2__', at('d', 0.5)).replace('__D3__', at('d', 0.95))
            .replace('__D4__', at('d', 1.55)).replace('__D5__', at('d', 2.15)).replace('__D6__', at('d', 2.4))
            .replace('__D7__', at('d', 2.55))
            .replace('__E1__', at('e', 0.15)).replace('__E2__', at('e', 0.5)).replace('__E3__', at('e', 1.3))
            .replace('__E4__', at('e', 1.55)).replace('__E5__', at('e', 1.7))
            .replace('__F1__', at('f', 0.35)).replace('__F2__', at('f', 0.95)).replace('__F3__', at('f', 1.55))
            .replace('__F4__', at('f', 1.8)).replace('__F5__', at('f', 1.95)).replace('__F6__', at('f', 2.45))
            .replace('__MONO_S2__', MONO_S.replace('class="mono"', 'class="mono" style="width:250px"'))
            .replace('__MONO_S__', MONO_S)
            .replace('__MONO__', MONO)
            .replace('__ORN__', ORN)
            .replace('__PETALS_BACK__',  petals(16, 0.0, 6, 12, 11, 20, 0.55))
            .replace('__PETALS_FRONT__', petals(9, 2.6, 16, 30, 7, 13, 0.45)))

html = (u'<!DOCTYPE html><html dir="rtl"><head><meta charset="utf-8">'
        u'<link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=Amiri:wght@400;700'
        u'&family=IBM+Plex+Sans+Arabic:wght@200;300;400;500;600&display=swap" rel="stylesheet">'
        u'<style>%s</style></head><body>%s</body></html>' % (css, body))
io.open(OUT, 'w', encoding='utf-8').write(html)
print('كتبت %s · %ds · %d حرف' % (OUT, DUR, len(html)))

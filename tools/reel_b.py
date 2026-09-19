# -*- coding: utf-8 -*-
"""الريلز التاني — رحلة رأسية داخل إطار ذهبي ثابت. python3 reel_b.py <المدة> <الخرج>"""
import io, os, sys, random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORNER = io.open(os.path.join(ROOT, 'tools', 'corner.svg'), encoding='utf-8').read()
ORN = CORNER[CORNER.index('>')+1: CORNER.rindex('</svg>')]
DUR = float(sys.argv[1]) if len(sys.argv) > 1 else 30.0
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'share', 'reelB.html')
R = random.Random(33)

H = 1920
N = 6
# لحظات وصول كل لوحة (ثانية) — وقفة ثم انزلاق
HOLD, SLIDE = (DUR - 5 * 0.95) / N, 0.95
STOPS = [i * (HOLD + SLIDE) for i in range(N)]

def pct(t): return round(max(0.0, min(100.0, t / DUR * 100.0)), 3)
def at(i, off): return '%.2fs' % (STOPS[i] + off)

# كيفريمز الرحلة
kf = []
for i in range(N):
    a, b = pct(STOPS[i]), pct(STOPS[i] + HOLD)
    ease = ';animation-timing-function:cubic-bezier(.62,0,.24,1)' if i < N - 1 else ''
    kf.append('%s%%,%s%%{transform:translateY(-%dpx)%s}' % (a, b, i * H, ease))
TRAVEL = ''.join(kf)

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
MONO_S = (MONO.replace('class="r1"', 'class="r1 st"').replace('class="r2"', 'class="r2 st"')
              .replace('class="dia"', 'class="dia st"').replace('class="gly"', 'class="gly st"'))

petals = ''.join(
    '<span class="pt" style="left:%.1f%%;width:%.1fpx;height:%.1fpx;background:rgba(%s);'
    'animation-duration:%.1fs;animation-delay:-%.1fs;--dx:%.0fpx"></span>'
    % (R.uniform(-4, 103), s := R.uniform(7, 15), s * .72,
       R.choice(['190,154,96,.5', '217,188,133,.45', '242,228,200,.6']),
       R.uniform(10, 18), R.uniform(0, 18), R.uniform(-130, 130))
    for _ in range(15))

CSS = u'''
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#FDF9F1}
body{font-family:'IBM Plex Sans Arabic',sans-serif;font-weight:300;color:#333E42;direction:rtl;text-align:center;position:relative}

/* الشريط المتحرك */
.reel{position:absolute;top:0;left:0;width:1080px;animation:travel __D__s linear both}
@keyframes travel{__TRAVEL__}
.pane{width:1080px;height:1920px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 96px;position:relative}

/* الإطار الذهبي الثابت */
.frame{position:absolute;inset:38px;border:1px solid rgba(190,154,96,.55);pointer-events:none;z-index:8}
.frame::before{content:"";position:absolute;inset:11px;border:1px solid rgba(190,154,96,.26)}
.fx{position:absolute;width:360px;height:auto;color:#BE9A60;opacity:.55;z-index:7;pointer-events:none}
.fx.tl{top:0;left:0}
.fx.br{bottom:0;right:0;transform:scale(-1,-1)}

/* المونوجرام */
.mono{width:290px;height:auto;color:#95733E}
.mono .r1{stroke-dasharray:622;stroke-dashoffset:622;animation:draw 1.6s ease __M1__ both}
.mono .r2{stroke-dasharray:566;stroke-dashoffset:566;animation:draw 1.6s ease __M2__ both}
.mono .dia{opacity:0;animation:fdi .9s ease __M3__ both}
.mono .gly{opacity:0;transform-origin:110px 130px;animation:gly 1s cubic-bezier(.2,.9,.3,1.25) __M4__ both}
.mono .st{animation:none!important;stroke-dashoffset:0;opacity:1;transform:none}
.mono .dia.st{opacity:.55}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes gly{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:none}}
@keyframes fdi{from{opacity:0}to{opacity:.55}}

/* حركات */
.u{opacity:0;animation:u 1.05s cubic-bezier(.2,.85,.3,1) both}
@keyframes u{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:none}}
.f{opacity:0;animation:f 1.15s ease both}
@keyframes f{from{opacity:0}to{opacity:1}}
.p{opacity:0;animation:p .95s cubic-bezier(.2,.9,.3,1.5) both}
@keyframes p{from{opacity:0;transform:scale(.75)}to{opacity:1;transform:none}}
.w{clip-path:inset(0 0 0 100%);animation:w 1.2s cubic-bezier(.55,0,.2,1) both}
@keyframes w{to{clip-path:inset(0 0 0 0)}}

.rule{display:flex;align-items:center;gap:26px;width:520px;margin:40px auto}
.rule i{flex:1;height:1px;background:linear-gradient(90deg,transparent,#BE9A60,transparent);transform:scaleX(0);animation:gw 1.05s cubic-bezier(.2,.85,.3,1) both}
.rule b{width:15px;height:15px;background:#BE9A60;transform:rotate(45deg) scale(0);animation:db .75s cubic-bezier(.2,.9,.3,1.5) both}
@keyframes gw{to{transform:scaleX(1)}}
@keyframes db{to{transform:rotate(45deg) scale(1)}}

.kick{font-size:31px;color:#6D787C;word-spacing:.55em;margin-top:44px}
.names{font-family:'Aref Ruqaa',serif;font-weight:700;font-size:118px;line-height:1.55;color:#1E2A2E;display:flex;align-items:center;justify-content:center;gap:32px}
.names em{font-family:'Amiri',serif;font-style:normal;color:#BE9A60;font-size:.46em}
.date{font-family:'Amiri',serif;font-size:44px;color:#4A555A;line-height:1.9}
.ayah{font-family:'Amiri',serif;font-size:50px;line-height:2.15;color:#3A4549}
.src{font-size:27px;color:#95733E;word-spacing:.3em;margin-top:26px}
.big{font-family:'Amiri',serif;font-weight:700;font-size:250px;color:#95733E;line-height:1}
.lbl{font-size:35px;color:#7C878B;word-spacing:.45em}
.val{font-family:'Amiri',serif;font-weight:700;font-size:74px;color:#1E2A2E;line-height:1.65}
.sub{font-size:35px;color:#6D787C;line-height:2}

/* الصورة في قوس */
.arch{width:820px;height:1090px;overflow:hidden;position:relative;
  border-radius:410px 410px 24px 24px;
  clip-path:inset(100% 0 0 0 round 410px 410px 24px 24px);
  animation:arch 1.35s cubic-bezier(.6,0,.22,1) __AR__ both;
  box-shadow:0 26px 70px rgba(120,95,60,.18)}
@keyframes arch{to{clip-path:inset(0 0 0 0 round 410px 410px 24px 24px)}}
.arch img{width:100%;height:100%;object-fit:cover;object-position:center 14%;display:block;
  animation:kb 6s ease-out __AR__ both}
@keyframes kb{from{transform:scale(1.1)}to{transform:scale(1)}}
.archline{position:absolute;width:868px;height:1138px;border:1.5px solid rgba(190,154,96,.5);
  border-radius:434px 434px 30px 30px;opacity:0;transform:scale(.97);
  animation:al 1.2s cubic-bezier(.2,.85,.3,1) __AL__ both}
@keyframes al{to{opacity:1;transform:none}}

/* ورد متساقط */
.petals{position:absolute;inset:0;pointer-events:none;z-index:6;overflow:hidden}
.pt{position:absolute;top:-9%;border-radius:60% 6% 60% 6%;opacity:0;animation-name:fall;animation-timing-function:linear;animation-iteration-count:infinite}
@keyframes fall{0%{transform:translate3d(0,-9vh,0) rotate(0);opacity:0}9%{opacity:1}90%{opacity:.85}100%{transform:translate3d(var(--dx),118vh,0) rotate(560deg);opacity:0}}

.prog{position:absolute;left:0;bottom:0;height:5px;width:100%;transform-origin:right;transform:scaleX(0);
  background:linear-gradient(90deg,#95733E,#D9BC85);z-index:9;animation:pg __D__s linear both}
@keyframes pg{to{transform:scaleX(1)}}
'''

BODY = u'''
<div class="reel">

  <!-- ١ · الغلاف -->
  <section class="pane">
    __MONO__
    <p class="kick u" style="animation-delay:__P1A__">دعوة&nbsp; زفاف</p>
    <h1 class="names" style="margin-top:14px">
      <span class="u" style="animation-delay:__P1B__">عبدالله</span>
      <em class="f" style="animation-delay:__P1C__">&amp;</em>
      <span class="u" style="animation-delay:__P1D__">خلود</span></h1>
    <div class="rule"><i style="animation-delay:__P1E__"></i><b style="animation-delay:__P1F__"></b><i style="animation-delay:__P1E__"></i></div>
    <p class="date f" style="animation-delay:__P1G__">السبت &nbsp;١٠ أكتوبر &nbsp;٢٠٢٦</p>
  </section>

  <!-- ٢ · الصورة -->
  <section class="pane">
    <div class="archline"></div>
    <div class="arch"><img src="../images/couple.jpg"></div>
  </section>

  <!-- ٣ · الآية -->
  <section class="pane">
    <p class="ayah"><span class="w" style="display:inline-block;animation-delay:__P3A__">﴿ وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا</span><br>
    <span class="w" style="display:inline-block;animation-delay:__P3B__">لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ﴾</span></p>
    <div class="rule"><i style="animation-delay:__P3C__"></i><b style="animation-delay:__P3D__"></b><i style="animation-delay:__P3C__"></i></div>
    <p class="src f" style="animation-delay:__P3E__">سورة&nbsp; الروم</p>
  </section>

  <!-- ٤ · التاريخ -->
  <section class="pane">
    <p class="lbl f" style="animation-delay:__P4A__">بكل الحب ندعوكم يوم</p>
    <p class="val u" style="font-size:84px;margin-top:14px;animation-delay:__P4B__">السبت</p>
    <p class="big p" style="animation-delay:__P4C__">10</p>
    <p class="val u" style="animation-delay:__P4D__">أكتوبر &nbsp;2026</p>
    <div class="rule"><i style="animation-delay:__P4E__"></i><b style="animation-delay:__P4F__"></b><i style="animation-delay:__P4E__"></i></div>
    <p class="sub f" style="animation-delay:__P4G__">من الثالثة عصرًا حتى السابعة مساءً</p>
  </section>

  <!-- ٥ · المكان -->
  <section class="pane">
    <p class="lbl f" style="animation-delay:__P5A__">المكان</p>
    <p class="val u" style="font-size:80px;margin-top:18px;animation-delay:__P5B__">قاعة سندريلا<br>قصر الأميرات</p>
    <div class="rule"><i style="animation-delay:__P5C__"></i><b style="animation-delay:__P5D__"></b><i style="animation-delay:__P5C__"></i></div>
    <p class="sub f" style="animation-delay:__P5E__">حديقة العاشر من رمضان، شارع الطيران<br>الحي السابع، مدينة نصر، القاهرة</p>
  </section>

  <!-- ٦ · الختام -->
  <section class="pane">
    <div class="p" style="animation-delay:__P6A__">__MONO_S__</div>
    <h1 class="names u" style="font-size:100px;margin-top:44px;animation-delay:__P6B__">عبدالله <em>&amp;</em> خلود</h1>
    <div class="rule"><i style="animation-delay:__P6C__"></i><b style="animation-delay:__P6D__"></b><i style="animation-delay:__P6C__"></i></div>
    <p class="sub f" style="font-size:42px;animation-delay:__P6E__">في انتظاركم لمشاركتنا فرحتنا</p>
    <p class="sub f" style="font-size:27px;color:#95733E;margin-top:44px;direction:ltr;animation-delay:__P6F__">abdallahghorap1212.github.io/wedding-abdallah-kholoud</p>
  </section>

</div>

<svg class="fx tl" viewBox="0 0 300 300">__ORN__</svg>
<svg class="fx br" viewBox="0 0 300 300">__ORN__</svg>
<div class="frame"></div>
<div class="petals">__PETALS__</div>
<i class="prog"></i>
'''

css = (CSS.replace('__D__', '%g' % DUR).replace('__TRAVEL__', TRAVEL)
          .replace('__M1__', at(0, .45)).replace('__M2__', at(0, .7))
          .replace('__M3__', at(0, 1.5)).replace('__M4__', at(0, 1.55))
          .replace('__AR__', at(1, .2)).replace('__AL__', at(1, .95)))

body = (BODY
    .replace('__P1A__', at(0, 2.1)).replace('__P1B__', at(0, 2.4)).replace('__P1C__', at(0, 2.75))
    .replace('__P1D__', at(0, 2.95)).replace('__P1E__', at(0, 3.35)).replace('__P1F__', at(0, 3.6))
    .replace('__P1G__', at(0, 3.7))
    .replace('__P3A__', at(2, .25)).replace('__P3B__', at(2, .65)).replace('__P3C__', at(2, 1.6))
    .replace('__P3D__', at(2, 1.85)).replace('__P3E__', at(2, 2.0))
    .replace('__P4A__', at(3, .2)).replace('__P4B__', at(3, .5)).replace('__P4C__', at(3, .9))
    .replace('__P4D__', at(3, 1.5)).replace('__P4E__', at(3, 2.0)).replace('__P4F__', at(3, 2.25))
    .replace('__P4G__', at(3, 2.4))
    .replace('__P5A__', at(4, .2)).replace('__P5B__', at(4, .5)).replace('__P5C__', at(4, 1.3))
    .replace('__P5D__', at(4, 1.55)).replace('__P5E__', at(4, 1.7))
    .replace('__P6A__', at(5, .3)).replace('__P6B__', at(5, .85)).replace('__P6C__', at(5, 1.4))
    .replace('__P6D__', at(5, 1.65)).replace('__P6E__', at(5, 1.8)).replace('__P6F__', at(5, 2.3))
    .replace('__MONO_S__', MONO_S).replace('__MONO__', MONO)
    .replace('__ORN__', ORN).replace('__PETALS__', petals))

html = (u'<!DOCTYPE html><html dir="rtl"><head><meta charset="utf-8">'
        u'<link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=Amiri:wght@400;700'
        u'&family=IBM+Plex+Sans+Arabic:wght@200;300;400;500;600&display=swap" rel="stylesheet">'
        u'<style>%s</style></head><body>%s</body></html>' % (css, body))
io.open(OUT, 'w', encoding='utf-8').write(html)
print('كتبت %s · %gs · وقفة %.2fs' % (OUT, DUR, HOLD))

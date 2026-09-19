# -*- coding: utf-8 -*-
"""يولّد مشاهد ريلز الدعوة (1080x1920) كـ HTML جاهزة للتصوير."""
import io, os, sys

ROOT  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT   = os.path.join(ROOT, 'share', 'scenes')
CORNER = io.open(os.path.join(ROOT, 'tools', 'corner.svg'), encoding='utf-8').read()
CORNER_INNER = CORNER[CORNER.index('>')+1 : CORNER.rindex('</svg>')]

HEAD = u'''<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=Amiri:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@200;300;400;500;600&display=swap" rel="stylesheet">
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{width:1080px;height:1920px;overflow:hidden}
  body{
    background:#FDF9F1;color:#333E42;
    font-family:'IBM Plex Sans Arabic',sans-serif;font-weight:300;
    direction:rtl;text-align:center;
    display:flex;flex-direction:column;align-items:center;justify-content:center;
    position:relative;
  }
  .orn{position:absolute;width:430px;height:auto;opacity:.62}
  .orn.a{top:0;left:0}
  .orn.b{top:0;right:0;transform:scaleX(-1)}
  .orn.c{bottom:0;left:0;transform:scaleY(-1)}
  .orn.d{bottom:0;right:0;transform:scale(-1,-1)}
  .mono{width:300px;height:auto;color:#95733E}
  .mono.sm{width:210px}
  .kick{font-size:30px;color:#6D787C;word-spacing:.55em;margin-top:44px}
  .names{font-family:'Aref Ruqaa',serif;font-weight:700;font-size:118px;line-height:1.55;color:#1E2A2E}
  .names span{font-family:'Amiri',serif;color:#BE9A60;font-size:.46em;margin:0 22px}
  .rule{display:flex;align-items:center;gap:26px;width:520px;margin:44px auto}
  .rule i{flex:1;height:1px;background:linear-gradient(90deg,transparent,#BE9A60,transparent)}
  .rule b{width:15px;height:15px;background:#BE9A60;transform:rotate(45deg)}
  .ayah{font-family:'Amiri',serif;font-size:46px;line-height:2.1;max-width:840px;margin:0 auto}
  .src{font-size:26px;color:#95733E;word-spacing:.3em;margin-top:22px}
  .big{font-family:'Amiri',serif;font-weight:700;font-size:210px;color:#95733E;line-height:1.05}
  .lbl{font-size:34px;color:#6D787C;word-spacing:.4em}
  .val{font-family:'Amiri',serif;font-weight:700;font-size:64px;color:#1E2A2E;line-height:1.7}
  .sub{font-size:34px;color:#6D787C;line-height:2;margin-top:18px}
  .stack{display:flex;flex-direction:column;align-items:center;gap:18px}
  .pad{padding:0 90px}
  /* مشهد الصورة */
  .photo{position:absolute;inset:0;display:flex;flex-direction:column}
  .photo img{width:1080px;height:1350px;object-fit:cover;object-position:center 16%;display:block}
  .photo .below{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#FDF9F1}
  .medal{
    width:230px;height:230px;border-radius:50%;background:#FDF9F1;
    display:grid;place-items:center;margin:-115px auto -40px;position:relative;z-index:2;
    box-shadow:0 10px 34px rgba(30,42,46,.12);
  }
  .medal svg{width:196px;height:196px;color:#95733E}
</style>'''

MONO = u'''<svg class="mono %s" viewBox="0 0 220 220">
  <circle cx="110" cy="110" r="99" fill="none" stroke="currentColor" stroke-width="1.1" opacity=".45"/>
  <circle cx="110" cy="110" r="90" fill="none" stroke="currentColor" stroke-width=".7" opacity=".25"/>
  <g fill="currentColor" opacity=".55">
    <path d="M110 5.4 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/><path d="M110 205.8 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/>
    <path d="M10 105.6 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/><path d="M210.2 105.6 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/>
  </g>
  <g fill="currentColor" font-family="Aref Ruqaa, Amiri, serif" font-weight="700" text-anchor="middle">
    <text x="128" y="146" font-size="123">&#1593;</text><text x="92" y="160" font-size="123">&#1582;</text>
  </g>
</svg>'''

def orns(which='abcd'):
    return u''.join(u'<svg class="orn %s" viewBox="0 0 300 300">%s</svg>' % (c, CORNER_INNER) for c in which)

SCENES = [
  # 1 — الافتتاح
  orns('abcd') + MONO % '' + u'''
  <p class="kick">دعوة&nbsp; زفاف</p>
  <div class="rule"><i></i><b></b><i></i></div>
  <p class="ayah">﴿ وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا<br>لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ﴾</p>
  <p class="src">سورة&nbsp; الروم</p>''',

  # 2 — الصورة والأسماء
  u'''<div class="photo">
    <img src="../../images/couple.jpg">
    <div class="below">
      <div class="medal">''' + (MONO % '') + u'''</div>
      <h1 class="names">عبدالله <span>&amp;</span> خلود</h1>
    </div>
  </div>''',

  # 3 — التاريخ
  orns('ab') + u'''
  <p class="lbl">بكل الحب ندعوكم يوم</p>
  <p class="val" style="font-size:78px;margin-top:14px">السبت</p>
  <p class="big">10</p>
  <p class="val">أكتوبر &nbsp;2026</p>
  <div class="rule"><i></i><b></b><i></i></div>
  <p class="sub">من الثالثة عصرًا حتى السابعة مساءً</p>''',

  # 4 — المكان
  orns('cd') + u'''
  <div class="pad stack">
    <p class="lbl">المكان</p>
    <p class="val" style="font-size:74px">قاعة سندريلا<br>قصر الأميرات</p>
    <div class="rule"><i></i><b></b><i></i></div>
    <p class="sub">حديقة العاشر من رمضان، شارع الطيران<br>الحي السابع، مدينة نصر، القاهرة</p>
  </div>''',

  # 5 — الختام
  orns('abcd') + MONO % 'sm' + u'''
  <h1 class="names" style="font-size:96px;margin-top:40px">عبدالله <span>&amp;</span> خلود</h1>
  <div class="rule"><i></i><b></b><i></i></div>
  <p class="sub" style="font-size:40px">في انتظاركم لمشاركتنا فرحتنا</p>
  <p class="sub" style="font-size:26px;color:#95733E;margin-top:44px;direction:ltr;letter-spacing:.02em">abdallahghorap1212.github.io/wedding-abdallah-kholoud</p>''',
]

os.makedirs(OUT, exist_ok=True)
for i, body in enumerate(SCENES, 1):
    io.open(os.path.join(OUT, 'scene%d.html' % i), 'w', encoding='utf-8').write(
        u'<!DOCTYPE html><html dir="rtl"><head>%s</head><body>%s</body></html>' % (HEAD, body))
print('كتبت %d مشهد في %s' % (len(SCENES), OUT))

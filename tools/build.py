# -*- coding: utf-8 -*-
import io, sys
qr  = io.open(sys.argv[1], encoding='utf-8').read()
out = sys.argv[2]

HTML = u'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>دعوة زفاف عبدالله وخلود</title>
<meta name="description" content="يسعدنا دعوتكم لحضور حفل زفاف عبدالله وخلود — السبت ١٠ أكتوبر ٢٠٢٦، قاعة سندريلا بقصر الأميرات، حديقة العاشر من رمضان.">
<meta name="theme-color" content="#FDF8EF">
<meta property="og:title" content="دعوة زفاف عبدالله وخلود">
<meta property="og:description" content="السبت ١٠ أكتوبر ٢٠٢٦ — من ٣ عصرًا حتى ٧ مساءً — قاعة سندريلا، قصر الأميرات.">
<meta property="og:image" content="images/couple.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='18' fill='%23FDF8EF'/><text y='.86em' x='50' text-anchor='middle' font-size='74' fill='%2396733F'>&#1593;</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=Amiri:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Sans+Arabic:wght@200;300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="mono" viewBox="0 0 220 220">
    <circle cx="110" cy="110" r="99" fill="none" stroke="currentColor" stroke-width="1.1" opacity=".45"/>
    <circle cx="110" cy="110" r="90" fill="none" stroke="currentColor" stroke-width=".7" opacity=".25"/>
    <g fill="currentColor" opacity=".55">
      <path d="M110 5.4 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/>
      <path d="M110 205.8 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z"/>
      <path d="M5.4 110 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z" transform="translate(4.4 -4.4)"/>
      <path d="M205.8 110 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z" transform="translate(4.4 -4.4)"/>
    </g>
    <g fill="currentColor" font-family="Aref Ruqaa, Amiri, serif" font-weight="700" text-anchor="middle">
      <text x="128" y="146" font-size="123">&#1593;</text>
      <text x="92" y="160" font-size="123">&#1582;</text>
    </g>
  </symbol>

  <symbol id="deco" viewBox="0 0 120 120">
    <path d="M1 44 V1 H44" fill="none" stroke="currentColor" stroke-width="1.1"/>
    <path d="M11 52 V11 H52" fill="none" stroke="currentColor" stroke-width=".7" opacity=".55"/>
    <path d="M22 22 l7 7" stroke="currentColor" stroke-width=".8" opacity=".5"/>
    <path d="M33 22 l4.4 4.4 -4.4 4.4 -4.4 -4.4 z" fill="currentColor" opacity=".7"/>
  </symbol>
</svg>

<i class="progress" id="progress" aria-hidden="true"></i>

<!-- ═════════════ شاشة الافتتاح ═════════════ -->
<div class="opener" id="opener" role="dialog" aria-label="افتح الدعوة">
  <span class="op-panel op-top" aria-hidden="true"></span>
  <span class="op-panel op-bot" aria-hidden="true"></span>
  <div class="op-inner">
    <svg class="op-mono" viewBox="0 0 220 220" aria-hidden="true">
      <circle class="op-ring-a" cx="110" cy="110" r="99" fill="none" stroke="#C6A465" stroke-width="1.1" opacity=".6"/>
      <circle class="op-ring-b" cx="110" cy="110" r="90" fill="none" stroke="#C6A465" stroke-width=".7" opacity=".35"/>
      <g class="op-glyph" fill="#D8B87A" font-family="Aref Ruqaa, Amiri, serif" font-weight="700" text-anchor="middle">
        <text x="128" y="146" font-size="123">&#1593;</text>
        <text x="92" y="160" font-size="123">&#1582;</text>
      </g>
    </svg>
    <p class="op-to" id="opTo" hidden></p>
    <p class="op-kicker">دعوة زفاف</p>
    <p class="op-names">عبدالله <span>&amp;</span> خلود</p>
    <p class="op-date">السبت ١٠ أكتوبر ٢٠٢٦</p>
    <button class="op-btn" id="openerBtn" type="button">
      <span>افتح الدعوة</span>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 6.5h16v11H4z"/><path d="M4 7l8 6 8-6"/></svg>
    </button>
    <p class="op-hint">مع الموسيقى &#9834;</p>
  </div>
</div>

<!-- ═════════════ الغلاف ═════════════ -->
<header class="hero">
  <div class="hero-text">
    <div class="hero-in">
      <p class="hero-ayah reveal">﴿ وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ﴾</p>
      <p class="hero-ayah-src reveal">سورة الروم</p>

      <svg class="crest reveal" viewBox="0 0 220 220" role="img" aria-label="مونوجرام عبدالله وخلود"><use href="#mono"/></svg>
      <p class="guest reveal" id="guestLine" hidden></p>
      <p class="kicker reveal">دعوة زفاف</p>
      <h1 class="names reveal"><span class="nm">عبدالله</span><span class="amp">&amp;</span><span class="nm">خلود</span></h1>
      <div class="rule reveal" aria-hidden="true"><span></span><i></i><span></span></div>
      <p class="lede reveal">مع عائلتيهما يتشرفان بدعوتكم<br>لمشاركتهما أجمل أيام العمر</p>

      <div class="datebar reveal">
        <div class="db-side"><span class="db-lbl">اليوم</span><b>السبت</b></div>
        <div class="db-mid"><span class="db-mon">أكتوبر</span><b class="db-day">10</b><span class="db-year">2026</span></div>
        <div class="db-side"><span class="db-lbl">الساعة</span><b>٣ عصرًا</b></div>
      </div>

      <p class="hero-place reveal">قاعة سندريلا &mdash; قصر الأميرات<br>حديقة العاشر من رمضان، مدينة نصر</p>
    </div>
    <span class="vlabel" aria-hidden="true">10 &middot; 10 &middot; 2026</span>
    <a class="cue" href="#countdown" aria-label="انزل للأسفل"><span></span></a>
  </div>
  <div class="hero-img">
    <img src="images/couple.jpg" width="1024" height="1280" alt="العريس عبدالله والعروسة خلود" id="heroImg">
    <span class="img-frame" aria-hidden="true"></span>
  </div>
</header>

<!-- ═════════════ العد التنازلي ═════════════ -->
<section class="panel sand tight" id="countdown">
  <div class="wrap">
    <h2 class="stitle reveal">باقٍ على الفرح</h2>
    <div class="timer reveal" id="timer">
      <div class="unit"><b id="cd-days">--</b><span>يوم</span></div>
      <div class="unit"><b id="cd-hours">--</b><span>ساعة</span></div>
      <div class="unit"><b id="cd-mins">--</b><span>دقيقة</span></div>
      <div class="unit"><b id="cd-secs">--</b><span>ثانية</span></div>
    </div>
    <p class="timer-done" id="timerDone" hidden></p>
  </div>
</section>

<!-- ═════════════ التفاصيل ═════════════ -->
<section class="panel light">
  <div class="wrap">
    <h2 class="stitle reveal">تفاصيل الحفل</h2>

    <div class="spec reveal">
      <svg class="deco d-tl" viewBox="0 0 120 120" aria-hidden="true"><use href="#deco"/></svg>
      <svg class="deco d-tr" viewBox="0 0 120 120" aria-hidden="true"><use href="#deco"/></svg>
      <svg class="deco d-bl" viewBox="0 0 120 120" aria-hidden="true"><use href="#deco"/></svg>
      <svg class="deco d-br" viewBox="0 0 120 120" aria-hidden="true"><use href="#deco"/></svg>

      <div class="spec-grid">
        <div class="sc">
          <svg class="sc-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="1.5"/><path d="M8 3v4M16 3v4M3 10h18"/><circle cx="12" cy="15.5" r="1.4" fill="currentColor" stroke="none"/></svg>
          <h3 class="sc-lbl">التاريخ</h3>
          <p class="sc-val">السبت ١٠ أكتوبر ٢٠٢٦</p>
          <p class="sc-sub">٢٩ ربيع الآخر ١٤٤٨ هـ</p>
        </div>
        <div class="sc">
          <svg class="sc-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5.4l3.4 2"/></svg>
          <h3 class="sc-lbl">الموعد</h3>
          <p class="sc-val">٣:٠٠ عصرًا &mdash; ٧:٠٠ مساءً</p>
          <p class="sc-sub">فرح نهاري</p>
        </div>
        <div class="sc">
          <svg class="sc-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11z"/><circle cx="12" cy="10" r="2.4"/></svg>
          <h3 class="sc-lbl">المكان</h3>
          <p class="sc-val">قاعة سندريلا</p>
          <p class="sc-sub">قصر الأميرات &mdash; مدينة نصر</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═════════════ الوصول ═════════════ -->
<section class="panel sand">
  <div class="wrap">
    <h2 class="stitle reveal">الوصول للقاعة</h2>
    <div class="venue reveal">
      <p class="v-name">قاعة سندريلا &mdash; قصر الأميرات</p>
      <p class="v-addr">حديقة العاشر من رمضان، شارع الطيران، الحي السابع، مدينة نصر، القاهرة</p>
      <div class="v-grid">
        <div class="v-qr">__QR__</div>
        <div class="v-act">
          <p class="v-hint">امسح الكود بكاميرا موبايلك<br>وهيفتحلك مكان القاعة على الخريطة</p>
          <div class="btn-row">
            <a class="btn btn-fill" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&amp;query=%D9%82%D8%B5%D8%B1%20%D8%A7%D9%84%D8%A3%D9%85%D9%8A%D8%B1%D8%A7%D8%AA%20%D8%AD%D8%AF%D9%8A%D9%82%D8%A9%20%D8%A7%D9%84%D8%B9%D8%A7%D8%B4%D8%B1%20%D9%85%D9%86%20%D8%B1%D9%85%D8%B6%D8%A7%D9%86%20%D9%85%D8%AF%D9%8A%D9%86%D8%A9%20%D9%86%D8%B5%D8%B1">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11z"/><circle cx="12" cy="10" r="2.4"/></svg>
              خرائط جوجل
            </a>
            <a class="btn btn-line" target="_blank" rel="noopener" href="https://www.bing.com/maps/sharing?v=2&amp;pc=FACEBK&amp;mid=8100&amp;mkt=en-US&amp;FORM=FBKPL1&amp;q=%D8%AD%D8%AF%D9%8A%D9%82%D8%A9+%D8%A7%D9%84%D8%B9%D8%A7%D8%B4%D8%B1+%D9%85%D9%86+%D8%B1%D9%85%D8%B6%D8%A7%D9%86+-+%D9%85%D8%AF%D9%8A%D9%86%D8%A9+%D9%86%D8%B5%D8%B1+-+%D8%A7%D9%84%D8%AD%D9%8A+%D8%A7%D9%84%D8%B3%D8%A7%D8%A8%D8%B9+-+%D8%B4%D8%A7%D8%B1%D8%B9+%D8%A7%D9%84%D8%B7%D9%8A%D8%B1%D8%A7%D9%86+Nasr+City%2C+Cairo+Governorate%2C+Egypt+11765%2C+Cairo%2C+Egypt%2C+11735&amp;webglerror=a">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M9 3 3 5.5v15L9 18l6 3 6-2.5v-15L15 6 9 3z"/><path d="M9 3v15M15 6v15"/></svg>
              خرائط Bing
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═════════════ مستنيينكم ═════════════ -->
<section class="panel light">
  <div class="wrap narrow">
    <h2 class="stitle reveal">مستنيينكم</h2>
    <p class="lede reveal">حضوركم أجمل هدية</p>
    <div class="btn-row reveal">
      <a class="btn btn-fill" id="btnCal" href="event.ics">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M8 3v4M16 3v4M3 10h18M12 13v5M9.5 15.5h5"/></svg>
        أضف الموعد لتقويمك
      </a>
      <a class="btn btn-line" id="btnShare" target="_blank" rel="noopener" href="#">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.6 14.2c-.2.6-1.2 1.2-1.7 1.2-.5.1-1 .1-1.6-.1-.4-.1-.9-.3-1.5-.6-2.6-1.1-4.3-3.8-4.5-4-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.6-.3h.5c.1 0 .3 0 .5.4l.7 1.7c.1.1.1.3 0 .5l-.3.4-.3.3c-.1.1-.2.3 0 .5.1.2.6 1 1.3 1.6.9.8 1.6 1 1.9 1.2.2.1.4.1.5-.1l.7-.8c.2-.2.3-.2.5-.1l1.6.8c.2.1.4.2.4.3.1.2.1.7-.1 1.3z"/></svg>
        شارك الدعوة
      </a>
      <button class="btn btn-line" id="btnCopy" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M15 5.5A2.5 2.5 0 0 0 12.5 3h-7A2.5 2.5 0 0 0 3 5.5v7A2.5 2.5 0 0 0 5.5 15"/></svg>
        نسخ الرابط
      </button>
    </div>
  </div>
</section>

<footer class="panel sand foot">
  <svg class="deco d-bl" viewBox="0 0 120 120" aria-hidden="true"><use href="#deco"/></svg>
  <svg class="deco d-br" viewBox="0 0 120 120" aria-hidden="true"><use href="#deco"/></svg>
  <svg class="seal reveal" viewBox="0 0 220 220" aria-hidden="true"><use href="#mono"/></svg>
  <p class="foot-names">عبدالله &amp; خلود</p>
  <p class="foot-dua">اللهم بارك لهما وبارك عليهما واجمع بينهما في خير</p>
</footer>

<button class="music-btn" id="musicBtn" type="button" aria-pressed="false" aria-label="تشغيل موسيقى الخلفية" title="موسيقى الخلفية">
  <span class="eq" aria-hidden="true"><i></i><i></i><i></i></span>
  <svg class="mi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
    <path d="M9 18V5l11-2v13"/><circle cx="6.5" cy="18" r="2.8"/><circle cx="17.5" cy="16" r="2.8"/>
  </svg>
</button>

<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="script.js"></script>
</body>
</html>
'''
io.open(out, 'w', encoding='utf-8').write(HTML.replace('__QR__', qr))
print('index.html', len(HTML.encode('utf-8')), 'bytes')

# -*- coding: utf-8 -*-
import io, sys, re
couple = io.open(sys.argv[1], encoding='utf-8').read()
corner = io.open(sys.argv[2], encoding='utf-8').read()
qr     = io.open(sys.argv[3], encoding='utf-8').read()
out    = sys.argv[4]

# corner -> reusable symbol
corner_inner = corner[corner.index('>')+1 : corner.rindex('</svg>')]

couple = couple.replace('<svg viewBox', '<svg class="art-svg" viewBox', 1)

HTML = u'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>دعوة زفاف عبدالله وخلود</title>
<meta name="description" content="يسعدنا دعوتكم لحضور حفل زفاف عبدالله وخلود — السبت ١٠ أكتوبر ٢٠٢٦، قاعة سندريلا بقصر الأميرات، حديقة العاشر من رمضان.">
<meta name="theme-color" content="#FBF3EE">
<meta property="og:title" content="دعوة زفاف عبدالله وخلود">
<meta property="og:description" content="السبت ١٠ أكتوبر ٢٠٢٦ — من ٣ عصرًا حتى ٧ مساءً — قاعة سندريلا، قصر الأميرات.">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#128141;</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@400;700&family=Amiri:wght@400;700&family=Tajawal:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="orn" viewBox="0 0 300 300">__CORNER__</symbol></svg>

<div class="petals" id="petals" aria-hidden="true"></div>

<main class="sheet">

  <!-- ═══════════ الآية ═══════════ -->
  <section class="verse-top">
    <p class="ayah reveal">﴿ وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ﴾</p>
    <p class="ayah-src reveal">صدق الله العظيم &mdash; سورة الروم</p>
  </section>

  <!-- ═══════════ بطاقة الدعوة ═══════════ -->
  <section class="card">
    <svg class="corner corner-a" viewBox="0 0 300 300" aria-hidden="true"><use href="#orn"/></svg>
    <svg class="corner corner-b" viewBox="0 0 300 300" aria-hidden="true"><use href="#orn"/></svg>

    <div class="card-text">
      <p class="eyebrow reveal">دعوة زفاف</p>

      <h1 class="names reveal">
        <span class="nm">عبدالله</span><span class="amp">&amp;</span><span class="nm">خلود</span>
      </h1>

      <p class="families reveal">مع عائلتيهما يتشرفان بدعوتكم<br>لمشاركتهما أجمل أيام العمر</p>

      <div class="datebar reveal">
        <div class="db-side"><span>السبت</span></div>
        <div class="db-mid">
          <span class="db-mon">أكتوبر</span>
          <b class="db-day">10</b>
          <span class="db-year">2026</span>
        </div>
        <div class="db-side"><span>٣ عصرًا</span></div>
      </div>

      <p class="addr reveal">قاعة سندريلا &mdash; قصر الأميرات</p>
      <p class="addr addr-2 reveal">حديقة العاشر من رمضان، شارع الطيران، الحي السابع، مدينة نصر، القاهرة</p>
    </div>

    <div class="card-art" id="coupleFrame">
      <img id="couplePhoto" class="art-photo" src="images/couple.jpg" alt="العريس عبدالله والعروسة خلود">
      __COUPLE__
    </div>
  </section>

  <!-- ═══════════ العد التنازلي ═══════════ -->
  <section class="block" id="countdown">
    <h2 class="stitle reveal">باقي على الفرح</h2>
    <div class="timer reveal" id="timer">
      <div class="unit"><b id="cd-days">--</b><span>يوم</span></div>
      <div class="unit"><b id="cd-hours">--</b><span>ساعة</span></div>
      <div class="unit"><b id="cd-mins">--</b><span>دقيقة</span></div>
      <div class="unit"><b id="cd-secs">--</b><span>ثانية</span></div>
    </div>
    <p class="timer-done" id="timerDone" hidden></p>
  </section>

  <div class="divider" aria-hidden="true"><span></span><i>&#10052;</i><span></span></div>

  <!-- ═══════════ التفاصيل ═══════════ -->
  <section class="block">
    <h2 class="stitle reveal">تفاصيل الحفل</h2>
    <div class="cards">
      <article class="card-i reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18"/><circle cx="12" cy="15.5" r="1.5" fill="currentColor" stroke="none"/></svg></div>
        <h3>التاريخ</h3>
        <p class="big">السبت ١٠ / ١٠ / ٢٠٢٦</p>
        <p class="sub">يوافق ٢٩ ربيع الآخر ١٤٤٨ هـ</p>
      </article>
      <article class="card-i reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="12" cy="12" r="9"/><path d="M12 7v5.5l3.5 2"/></svg></div>
        <h3>الموعد</h3>
        <p class="big">٣:٠٠ عصرًا — ٧:٠٠ مساءً</p>
        <p class="sub">فرح نهاري</p>
      </article>
      <article class="card-i reveal">
        <div class="ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg></div>
        <h3>المكان</h3>
        <p class="big">قاعة سندريلا</p>
        <p class="sub">قصر الأميرات — حديقة العاشر من رمضان</p>
      </article>
    </div>
  </section>

  <div class="divider" aria-hidden="true"><span></span><i>&#10052;</i><span></span></div>

  <!-- ═══════════ المكان ═══════════ -->
  <section class="block">
    <h2 class="stitle reveal">مكان الحفل</h2>
    <p class="venue-name reveal">قاعة سندريلا — قصر الأميرات</p>
    <p class="venue-addr reveal">حديقة العاشر من رمضان، شارع الطيران، الحي السابع، مدينة نصر، القاهرة</p>
    <div class="btn-row reveal">
      <a class="btn btn-fill" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&amp;query=%D9%82%D8%B5%D8%B1%20%D8%A7%D9%84%D8%A3%D9%85%D9%8A%D8%B1%D8%A7%D8%AA%20%D8%AD%D8%AF%D9%8A%D9%82%D8%A9%20%D8%A7%D9%84%D8%B9%D8%A7%D8%B4%D8%B1%20%D9%85%D9%86%20%D8%B1%D9%85%D8%B6%D8%A7%D9%86%20%D9%85%D8%AF%D9%8A%D9%86%D8%A9%20%D9%86%D8%B5%D8%B1">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11z"/><circle cx="12" cy="10" r="2.4"/></svg>
        خرائط جوجل
      </a>
      <a class="btn btn-line" target="_blank" rel="noopener" href="https://www.bing.com/maps/sharing?v=2&amp;pc=FACEBK&amp;mid=8100&amp;mkt=en-US&amp;FORM=FBKPL1&amp;q=%D8%AD%D8%AF%D9%8A%D9%82%D8%A9+%D8%A7%D9%84%D8%B9%D8%A7%D8%B4%D8%B1+%D9%85%D9%86+%D8%B1%D9%85%D8%B6%D8%A7%D9%86+-+%D9%85%D8%AF%D9%8A%D9%86%D8%A9+%D9%86%D8%B5%D8%B1+-+%D8%A7%D9%84%D8%AD%D9%8A+%D8%A7%D9%84%D8%B3%D8%A7%D8%A8%D8%B9+-+%D8%B4%D8%A7%D8%B1%D8%B9+%D8%A7%D9%84%D8%B7%D9%8A%D8%B1%D8%A7%D9%86+Nasr+City%2C+Cairo+Governorate%2C+Egypt+11765%2C+Cairo%2C+Egypt%2C+11735&amp;webglerror=a">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M9 3 3 5.5v15L9 18l6 3 6-2.5v-15L15 6 9 3z"/><path d="M9 3v15M15 6v15"/></svg>
        خرائط Bing
      </a>
    </div>

    <div class="qr-box reveal">
      <div class="qr">__QR__</div>
      <p class="qr-cap">امسح الكود بكاميرا موبايلك عشان تفتح مكان القاعة على الخريطة</p>
    </div>
  </section>

  <div class="divider" aria-hidden="true"><span></span><i>&#10052;</i><span></span></div>

  <!-- ═══════════ أزرار ═══════════ -->
  <section class="block">
    <h2 class="stitle reveal">مستنيينكم</h2>
    <p class="note reveal">حضوركم أجمل هدية</p>
    <div class="btn-row reveal">
      <button class="btn btn-fill" id="btnCal" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18M12 13v5M9.5 15.5h5"/></svg>
        أضف الموعد للتقويم
      </button>
      <a class="btn btn-line" id="btnShare" target="_blank" rel="noopener" href="#">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm5.6 14.2c-.2.6-1.2 1.2-1.7 1.2-.5.1-1 .1-1.6-.1-.4-.1-.9-.3-1.5-.6-2.6-1.1-4.3-3.8-4.5-4-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.6-.3h.5c.1 0 .3 0 .5.4l.7 1.7c.1.1.1.3 0 .5l-.3.4-.3.3c-.1.1-.2.3 0 .5.1.2.6 1 1.3 1.6.9.8 1.6 1 1.9 1.2.2.1.4.1.5-.1l.7-.8c.2-.2.3-.2.5-.1l1.6.8c.2.1.4.2.4.3.1.2.1.7-.1 1.3z"/></svg>
        شارك الدعوة
      </a>
      <button class="btn btn-line" id="btnCopy" type="button">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2.5"/><path d="M15 5.5A2.5 2.5 0 0 0 12.5 3h-7A2.5 2.5 0 0 0 3 5.5v7A2.5 2.5 0 0 0 5.5 15"/></svg>
        نسخ الرابط
      </button>
    </div>
  </section>

  <footer class="foot">
    <div class="divider light" aria-hidden="true"><span></span><i>&#10052;</i><span></span></div>
    <p class="foot-names">عبدالله &amp; خلود</p>
    <p class="foot-dua">اللهم بارك لهما وبارك عليهما واجمع بينهما في خير</p>
  </footer>

</main>

<button class="music-btn" id="musicBtn" type="button" aria-pressed="false" aria-label="تشغيل موسيقى الخلفية" title="موسيقى الخلفية">
  <span class="eq" aria-hidden="true"><i></i><i></i><i></i></span>
  <svg class="mi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
    <path d="M9 18V5l11-2v13"/><circle cx="6.5" cy="18" r="2.8"/><circle cx="17.5" cy="16" r="2.8"/>
  </svg>
</button>

<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="script.js"></script>
</body>
</html>
'''
HTML = HTML.replace('__CORNER__', corner_inner).replace('__COUPLE__', couple).replace('__QR__', qr)
io.open(out, 'w', encoding='utf-8').write(HTML)
print('index.html', len(HTML.encode('utf-8')), 'bytes')

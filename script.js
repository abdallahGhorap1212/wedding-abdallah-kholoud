/* ═══════ دعوة زفاف عبدالله وخلود ═══════ */
(function () {
  'use strict';

  // موعد الفرح: السبت ١٠ أكتوبر ٢٠٢٦ — ٣:٠٠ عصرًا (بتوقيت الجهاز)
  var WEDDING = new Date(2026, 9, 10, 15, 0, 0);
  var WEDDING_END = new Date(2026, 9, 10, 19, 0, 0);

  /* ── صورة العريس والعروسة (لو موجودة تحلّ محل الرسمة) ── */
  var photo = document.getElementById('couplePhoto');
  var frame = document.getElementById('coupleFrame');
  if (photo && frame) {
    var showPhoto = function () {
      if (photo.naturalWidth > 0) frame.classList.add('has-photo');
    };
    if (photo.complete) showPhoto();
    photo.addEventListener('load', showPhoto);
    photo.addEventListener('error', function () { frame.classList.remove('has-photo'); });
  }

  /* ── العد التنازلي ── */
  var els = {
    days: document.getElementById('cd-days'),
    hours: document.getElementById('cd-hours'),
    mins: document.getElementById('cd-mins'),
    secs: document.getElementById('cd-secs'),
    timer: document.getElementById('timer'),
    done: document.getElementById('timerDone')
  };
  function pad(n) { return n < 10 ? '0' + n : '' + n; }
  function set(el, val) {
    if (!el || el.textContent === val) return;
    el.textContent = val;
    el.classList.add('tick');
    setTimeout(function () { el.classList.remove('tick'); }, 280);
  }

  function tick() {
    var diff = WEDDING.getTime() - Date.now();
    if (diff <= 0) {
      if (els.timer) els.timer.style.display = 'none';
      if (els.done) {
        els.done.hidden = false;
        els.done.textContent = Date.now() > WEDDING_END.getTime()
          ? 'ألف مبروك 🤍 شكرًا لمشاركتكم فرحتنا'
          : 'النهارده يوم الفرح — في انتظاركم! 🎉';
      }
      return;
    }
    var s = Math.floor(diff / 1000);
    set(els.days, String(Math.floor(s / 86400)));
    set(els.hours, pad(Math.floor(s / 3600) % 24));
    set(els.mins, pad(Math.floor(s / 60) % 60));
    set(els.secs, pad(s % 60));
  }
  if (els.days) { tick(); setInterval(tick, 1000); }

  /* ── ظهور العناصر عند التمرير ── */
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e, i) {
        if (e.isIntersecting) {
          setTimeout(function () { e.target.classList.add('in'); }, i * 90);
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  /* ── ورود متساقطة ── */
  var box = document.getElementById('petals');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (box && !reduce) {
    var colors = ['rgba(216,167,160,.75)', 'rgba(198,161,91,.65)', 'rgba(231,206,150,.7)', 'rgba(46,74,61,.28)'];
    var count = window.innerWidth < 600 ? 12 : 20;
    for (var i = 0; i < count; i++) {
      var p = document.createElement('span');
      var size = 6 + Math.random() * 10;
      p.className = 'petal';
      p.style.insetInlineStart = (Math.random() * 100) + 'vw';
      p.style.width = size + 'px';
      p.style.height = size * 0.75 + 'px';
      p.style.background = colors[i % colors.length];
      p.style.animationDuration = (11 + Math.random() * 12) + 's';
      p.style.animationDelay = (-Math.random() * 18) + 's';
      p.style.setProperty('--dx', (Math.random() * 120 - 60) + 'px');
      box.appendChild(p);
    }
  }

  /* ── رسالة سريعة ── */
  var toast = document.getElementById('toast');
  var toastTimer;
  function say(msg) {
    if (!toast) return;
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove('show'); }, 2800);
  }

  /* ── إضافة للتقويم — يفتح التقويم على طول ── */
  var btnCal = document.getElementById('btnCal');
  if (btnCal) {
    // أجهزة آبل بتفتح تطبيق التقويم فورًا من ملف ics، والباقي بنوديه على جوجل كاليندر
    var isApple = /iPad|iPhone|iPod|Macintosh/.test(navigator.userAgent) ||
                  (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);

    if (!isApple) {
      btnCal.href = 'https://calendar.google.com/calendar/render?action=TEMPLATE' +
        '&text='     + encodeURIComponent('حفل زفاف عبدالله وخلود') +
        '&dates=20261010T120000Z/20261010T160000Z' +
        '&details='  + encodeURIComponent('من ٣ عصرًا حتى ٧ مساءً — يسعدنا حضوركم 🤍') +
        '&location=' + encodeURIComponent('قاعة سندريلا - قصر الأميرات، حديقة العاشر من رمضان، شارع الطيران، مدينة نصر، القاهرة');
      btnCal.target = '_blank';
      btnCal.rel = 'noopener';
    }

    btnCal.addEventListener('click', function () {
      say(isApple ? 'هيفتحلك التقويم — اضغط «إضافة»' : 'هيفتح جوجل كاليندر في تبويب جديد');
    });
  }

  /* ── مشاركة واتساب ── */
  var btnShare = document.getElementById('btnShare');
  if (btnShare) {
    var text = 'دعوة زفاف عبدالله وخلود 🤍\n' +
      'السبت ١٠ أكتوبر ٢٠٢٦ — من ٣ عصرًا حتى ٧ مساءً\n' +
      'قاعة سندريلا — قصر الأميرات، حديقة العاشر من رمضان\n' +
      location.href;
    btnShare.href = 'https://wa.me/?text=' + encodeURIComponent(text);
    btnShare.addEventListener('click', function (e) {
      if (navigator.share) {
        e.preventDefault();
        navigator.share({ title: 'دعوة زفاف عبدالله وخلود', text: text }).catch(function () {
          window.open(btnShare.href, '_blank', 'noopener');
        });
      }
    });
  }

  /* ── نسخ الرابط ── */
  var btnCopy = document.getElementById('btnCopy');
  if (btnCopy) {
    btnCopy.addEventListener('click', function () {
      var url = location.href;
      if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(url).then(function () { say('تم نسخ الرابط ✓'); },
          function () { say(url); });
      } else {
        var t = document.createElement('textarea');
        t.value = url; t.setAttribute('readonly', '');
        t.style.position = 'fixed'; t.style.opacity = '0';
        document.body.appendChild(t); t.select();
        try { document.execCommand('copy'); say('تم نسخ الرابط ✓'); }
        catch (err) { say(url); }
        document.body.removeChild(t);
      }
    });
  }
})();

/* ═══════════ موسيقى الخلفية — أغنيتين ورا بعض بالتكرار ═══════════ */
(function () {
  'use strict';
  var btn = document.getElementById('musicBtn');
  if (!btn) return;

  var probe = document.createElement('audio');
  var ext = probe.canPlayType && probe.canPlayType('audio/webm; codecs="opus"') !== '' ? 'webm' : 'm4a';
  var N = 4;                    // عدد الأغاني
  function list(x) {
    var out = [];
    for (var i = 1; i <= N; i++) out.push('audio/track-' + i + '.' + x);
    return out;
  }
  var TRACKS = list(ext);
  var TARGET_VOL = 0.55;
  var GAP_MS = 4000;            // فاصل بين الأغاني (ملّي ثانية)
  var KEY = 'wedding-music';

  var audio = new Audio();
  audio.preload = 'auto';
  audio.volume = 0;
  audio.src = TRACKS[0];

  var idx = 0, userToggled = false, fadeTimer = null;
  var altTried = false, shouldPlay = false;

  // لما الأغنية تخلص، شغّل اللي بعدها — وبعد التانية ارجع للأولى
  var gapTimer = null;
  audio.addEventListener('ended', function () {
    idx = (idx + 1) % TRACKS.length;   // يبدّل بين الأغنيتين ويكرّر
    audio.src = TRACKS[idx];
    clearTimeout(gapTimer);
    gapTimer = setTimeout(function () {
      if (!shouldPlay) return;
      audio.volume = 0;
      audio.play().then(function () { fadeTo(TARGET_VOL); }).catch(function () {});
    }, GAP_MS);
  });
  // لو الصيغة مش مدعومة، جرّب الصيغة التانية مرة واحدة
  audio.addEventListener('error', function () {
    if (altTried) return;
    altTried = true;
    ext = (ext === 'webm' ? 'm4a' : 'webm');
    TRACKS = list(ext);
    audio.src = TRACKS[idx];
    audio.load();
    if (shouldPlay) audio.play().catch(function () {});
  });
  audio.addEventListener('play',  function () { setUI(true); });
  audio.addEventListener('pause', function () { setUI(false); });

  function setUI(on) {
    btn.classList.toggle('playing', on);
    btn.classList.toggle('hint', !on && !userToggled);
    btn.setAttribute('aria-pressed', on ? 'true' : 'false');
    btn.setAttribute('aria-label', on ? 'إيقاف موسيقى الخلفية' : 'تشغيل موسيقى الخلفية');
  }

  function fadeTo(target, done) {
    clearInterval(fadeTimer);
    fadeTimer = setInterval(function () {
      var d = target - audio.volume;
      if (Math.abs(d) < 0.03) {
        audio.volume = target;
        clearInterval(fadeTimer);
        if (done) done();
        return;
      }
      audio.volume = Math.min(1, Math.max(0, audio.volume + d * 0.18));
    }, 60);
  }

  function play() {
    shouldPlay = true;
    var p = audio.play();
    if (p && p.catch) p.catch(function () { setUI(false); });
    fadeTo(TARGET_VOL);
  }

  function stop() {
    shouldPlay = false;
    clearTimeout(gapTimer);
    fadeTo(0, function () { audio.pause(); });
  }

  btn.addEventListener('click', function () {
    userToggled = true;
    btn.classList.remove('hint');
    if (audio.paused) { play(); try { localStorage.setItem(KEY, 'on'); } catch (e) {} }
    else { stop(); try { localStorage.setItem(KEY, 'off'); } catch (e) {} }
  });

  function wanted() {
    try { return localStorage.getItem(KEY) !== 'off'; } catch (e) { return true; }
  }

  // ── التشغيل التلقائي ──
  // المتصفحات بتمنع الصوت من غير تفاعل، فبنحاول على طول — ولو اتمنع
  // بنفضل مستنيين أول أي تفاعل من الزائر ونشغّل ساعتها (لمسة، كليك، سكرول، زرار).
  var EVS = ['pointerdown', 'mousedown', 'touchstart', 'touchend', 'keydown', 'click', 'wheel', 'scroll'];

  function disarm() {
    EVS.forEach(function (e) { window.removeEventListener(e, tryStart); });
    document.removeEventListener('visibilitychange', onVisible);
  }

  function tryStart() {
    if (userToggled || !wanted()) { disarm(); return; }
    if (!audio.paused) { disarm(); return; }
    var p = audio.play();
    if (p && p.then) {
      p.then(function () { fadeTo(TARGET_VOL); disarm(); }).catch(function () { /* لسه متمنوع — نستنى تفاعل تاني */ });
    } else {
      fadeTo(TARGET_VOL);
      disarm();
    }
  }

  function onVisible() { if (!document.hidden) tryStart(); }

  EVS.forEach(function (e) { window.addEventListener(e, tryStart, { passive: true }); });
  document.addEventListener('visibilitychange', onVisible);

  // شاشة الافتتاح بتنادي دي — الضغطة بتدي إذن التشغيل
  window.__weddingPlay = function () { userToggled = true; btn.classList.remove('hint'); play(); };

  setUI(false);
  tryStart();                       // محاولة فورية أول ما الصفحة تفتح
  window.addEventListener('load', tryStart);
})();
/* ═══════════ شاشة الافتتاح + اسم الضيف ═══════════ */
(function () {
  'use strict';

  /* ── اسم الضيف من الرابط: ‎...?to=أحمد‎ ── */
  var to = '';
  try {
    var m = /[?&]to=([^&#]*)/.exec(location.search);
    if (m) to = decodeURIComponent(m[1].replace(/\+/g, ' ')).trim().slice(0, 48);
  } catch (e) { to = ''; }

  if (to) {
    var opTo = document.getElementById('opTo');
    if (opTo) { opTo.textContent = 'إلى / ' + to; opTo.hidden = false; }
    var line = document.getElementById('guestLine');
    if (line) {
      line.innerHTML = 'دعوة خاصة إلى ';
      var b = document.createElement('b');
      b.textContent = to;
      line.appendChild(b);
      line.hidden = false;
    }
  }

  /* ── الستارة ── */
  var opener = document.getElementById('opener');
  var btn = document.getElementById('openerBtn');
  if (!opener || !btn) return;

  document.body.classList.add('locked');
  opener.classList.add('ready');

  function enter() {
    btn.removeEventListener('click', enter);
    // الضغطة دي بتدي المتصفح إذن تشغيل الصوت
    if (typeof window.__weddingPlay === 'function') window.__weddingPlay();
    opener.classList.add('is-open');
    document.body.classList.remove('locked');
    setTimeout(function () {
      opener.style.display = 'none';
      window.dispatchEvent(new Event('resize'));   // عشان الـ reveal يتحسب من جديد
    }, 1350);
  }
  btn.addEventListener('click', enter);

  // لو الجافاسكريبت اتعطل لأي سبب، الستارة متفضلش قافلة الصفحة
  setTimeout(function () {
    if (!opener.classList.contains('is-open') && !opener.classList.contains('ready')) {
      document.body.classList.remove('locked');
    }
  }, 6000);
})();

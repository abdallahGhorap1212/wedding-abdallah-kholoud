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
    els.days.textContent = Math.floor(s / 86400);
    els.hours.textContent = pad(Math.floor(s / 3600) % 24);
    els.mins.textContent = pad(Math.floor(s / 60) % 60);
    els.secs.textContent = pad(s % 60);
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

  /* ── إضافة للتقويم (ملف ics) ── */
  function stamp(d) {
    return d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()) +
      'T' + pad(d.getHours()) + pad(d.getMinutes()) + '00';
  }
  var btnCal = document.getElementById('btnCal');
  if (btnCal) {
    btnCal.addEventListener('click', function () {
      var ics = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'PRODID:-//Abdallah & Kholoud//Wedding//AR',
        'CALSCALE:GREGORIAN',
        'BEGIN:VEVENT',
        'UID:wedding-abdallah-kholoud-20261010',
        'DTSTAMP:' + stamp(WEDDING),
        'DTSTART:' + stamp(WEDDING),
        'DTEND:' + stamp(WEDDING_END),
        'SUMMARY:حفل زفاف عبدالله وخلود',
        'DESCRIPTION:من 3 عصرًا حتى 7 مساءً — يسعدنا حضوركم',
        'LOCATION:قاعة سندريلا - قصر الأميرات، حديقة العاشر من رمضان، مدينة نصر، القاهرة',
        'BEGIN:VALARM',
        'TRIGGER:-P1D',
        'ACTION:DISPLAY',
        'DESCRIPTION:فاضل يوم على فرح عبدالله وخلود',
        'END:VALARM',
        'END:VEVENT',
        'END:VCALENDAR'
      ].join('\r\n');

      var blob = new Blob(['﻿' + ics], { type: 'text/calendar;charset=utf-8' });
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'wedding-abdallah-kholoud.ics';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(function () { URL.revokeObjectURL(url); }, 1500);
      say('تم تنزيل الموعد ✓ افتح الملف عشان يتضاف للتقويم');
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

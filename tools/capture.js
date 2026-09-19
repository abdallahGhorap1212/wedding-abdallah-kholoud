// يصوّر صفحة الريلز فريم بفريم بضبط زمن الأنيميشن بدقة
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const ROOT = path.dirname(__dirname);
const FPS = 30;
const DUR = Number(process.env.DUR || 25);
const OUT = process.argv[2] || path.join(ROOT, 'share', 'frames');
const SAMPLES = process.argv[3] ? process.argv[3].split(',').map(Number) : null;

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await puppeteer.launch({
    executablePath: '/usr/bin/google-chrome',
    headless: 'new',
    args: ['--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1920, deviceScaleFactor: 1 });
  await page.goto('file://' + (process.env.REEL || path.join(ROOT, 'share', 'reel.html')), { waitUntil: 'networkidle0' });
  await page.evaluate(() => document.fonts.ready);
  await new Promise(r => setTimeout(r, 1200));          // اطمن إن الخطوط والصورة اتحمّلوا

  const n = await page.evaluate(() => {
    document.getAnimations().forEach(a => a.pause());
    return document.getAnimations().length;
  });
  console.log('أنيميشن متتبّع:', n);

  const frames = SAMPLES
    ? SAMPLES.map(t => Math.round(t * FPS))
    : Array.from({ length: DUR * FPS }, (_, i) => i);

  let done = 0;
  for (const f of frames) {
    await page.evaluate(t => {
      document.getAnimations().forEach(a => { try { a.currentTime = t; } catch (e) {} });
    }, (f * 1000) / FPS);
    const name = SAMPLES ? `s_${(f / FPS).toFixed(1)}.jpg` : `f${String(f).padStart(5, '0')}.jpg`;
    await page.screenshot({ path: path.join(OUT, name), type: 'jpeg', quality: 93 });
    if (++done % 100 === 0) console.log('  ', done, '/', frames.length);
  }
  console.log('خلص:', done, 'فريم →', OUT);
  await browser.close();
})();

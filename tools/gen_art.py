# -*- coding: utf-8 -*-
"""رسمة كارتون للعروسين من الخلف على شاطئ المياه."""
import math, random, sys

W, H = 720, 470
R = random.Random(77)
P = []
def a(s): P.append(s)

SKIN="#EFC6A9"; SKIN_SH="#D8A183"
HAIR="#23242C"; HAIR2="#3D404C"
LINE="#DFD4C6"; WHITE_SH="#F1EAE0"
SHORE="#BFC8BD"
BUSH=["#8FA687","#7B9173","#A6BA9C","#96AD8C"]
BLOSS=["#F3D6C7","#FAE8DE","#FFFFFF","#EFC6B3"]

a('<defs>'
  '<linearGradient id="gSky" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0" stop-color="#FFFDFC"/><stop offset=".6" stop-color="#FCF5F0"/><stop offset="1" stop-color="#F4EEE7"/></linearGradient>'
  '<linearGradient id="gWater" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0" stop-color="#E5EBE7"/><stop offset="1" stop-color="#D5DDD8"/></linearGradient>'
  '<linearGradient id="gDress" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#FCF8F4"/><stop offset="1" stop-color="#EDE5DA"/></linearGradient>'
  '<linearGradient id="gScarf" x1="0" y1="0" x2="1" y2="0">'
  '<stop offset="0" stop-color="#FFFFFF"/><stop offset=".52" stop-color="#FDFAF6"/><stop offset="1" stop-color="#E8DFD3"/></linearGradient>'
  '<linearGradient id="gSuit" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0" stop-color="#353843"/><stop offset=".5" stop-color="#272932"/><stop offset="1" stop-color="#1A1C23"/></linearGradient>'
  '<linearGradient id="gSleeve" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0" stop-color="#32343E"/><stop offset="1" stop-color="#1F212A"/></linearGradient>'
  '<radialGradient id="gGlow"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>'
  '<radialGradient id="gWarm"><stop offset="0" stop-color="#F6DCCF" stop-opacity=".5"/><stop offset="1" stop-color="#F6DCCF" stop-opacity="0"/></radialGradient>'
  '</defs>')

def lace(x, y, r, op=.8):
    for k in range(4):
        aa = k*90 + R.uniform(-12, 12)
        a('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="none" stroke="%s" stroke-width=".85" opacity="%.2f"/>'
          % (x+math.cos(math.radians(aa))*r*.52, y+math.sin(math.radians(aa))*r*.52, r*.52, r*.37, LINE, op))
    a('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity="%.2f"/>' % (x, y, r*.17, LINE, op))

# ═════════ خلفية ═════════
a('<rect width="%d" height="%d" fill="url(#gSky)"/>' % (W, H))
a('<ellipse cx="360" cy="52" rx="340" ry="180" fill="url(#gGlow)"/>')
a('<ellipse cx="105" cy="230" rx="215" ry="150" fill="url(#gWarm)"/>')
a('<ellipse cx="630" cy="238" rx="215" ry="150" fill="url(#gWarm)"/>')

shore = ["M0,272"]; x = 0
while x < W:
    x += R.uniform(15, 44)
    shore.append("Q%.0f,%.0f %.0f,%.0f" % (x-11, 272 - R.uniform(3, 14), min(x, W), 272 - R.uniform(0, 4)))
shore.append("L%d,290 L0,290 Z" % W)
a('<path d="%s" fill="%s" opacity=".5"/>' % (" ".join(shore), SHORE))
a('<path d="M0,280 H720" stroke="%s" stroke-width="1.3" opacity=".45"/>' % SHORE)
a('<rect y="282" width="%d" height="150" fill="url(#gWater)"/>' % W)
for _ in range(30):
    a('<rect x="%.0f" y="%.0f" width="%.0f" height="%.1f" rx="1.6" fill="%s" opacity="%.2f"/>'
      % (R.uniform(-20, W), R.uniform(290, 428), R.uniform(40, 200), R.uniform(2, 3.6),
         R.choice(["#F3F7F4", "#FFFFFF", "#C9D3CC"]), R.uniform(.3, .7)))

# ═════════ العروسة ═════════
a('<g id="bride">')
# الفستان
a('<path d="M256,272 C230,288 214,322 208,364 L200,470 L400,470 L394,362 C388,320 372,288 346,274 Z" '
  'fill="url(#gDress)" stroke="%s" stroke-width="1.8"/>' % LINE)
a('<path d="M301,282 C298,340 298,410 300,470" fill="none" stroke="%s" stroke-width="1.6" opacity=".9"/>' % LINE)
a('<path d="M256,272 C238,296 226,334 222,378 L217,470" fill="none" stroke="%s" stroke-width="1.4" opacity=".65"/>' % LINE)
a('<path d="M346,274 C364,298 376,336 380,380 L385,470" fill="none" stroke="%s" stroke-width="1.4" opacity=".65"/>' % LINE)
for _ in range(120):
    x = R.uniform(212, 392); y = R.uniform(280, 468)
    if abs(x-301) < 6: continue
    lace(x, y, R.uniform(5, 11), R.uniform(.5, .95))
a('<path d="M346,274 C366,300 378,340 382,384 L387,470 L400,470 L394,362 C388,320 372,288 346,274 Z" fill="%s" opacity=".75"/>' % WHITE_SH)
# كتف
a('<path d="M256,272 C280,262 322,262 346,274" fill="none" stroke="%s" stroke-width="1.6" opacity=".8"/>' % LINE)

# الحجاب — أعرض وينزل على الكتف
a('<path d="M302,96 C262,96 236,124 230,166 C224,208 230,246 240,272 '
  'C246,286 250,296 252,306 L360,306 C362,294 366,278 372,258 C382,222 384,172 372,140 '
  'C360,110 336,96 302,96 Z" fill="url(#gScarf)" stroke="%s" stroke-width="1.9" stroke-linejoin="round"/>' % LINE)
a('<path d="M372,140 C384,172 382,222 372,258 C366,278 362,294 360,306 L338,306 C348,272 356,222 352,180 C349,152 344,130 337,116 Z" fill="%s" opacity=".7"/>' % WHITE_SH)
a('<path d="M247,166 C242,208 248,252 260,282" fill="none" stroke="%s" stroke-width="1.5" opacity=".8"/>' % LINE)
a('<path d="M263,120 C250,142 245,178 248,214" fill="none" stroke="%s" stroke-width="1.3" opacity=".6"/>' % LINE)
a('<path d="M252,306 C276,294 302,290 328,294 L360,306 Z" fill="%s" opacity=".6"/>' % WHITE_SH)
a('<path d="M252,300 C278,288 306,285 332,290 C344,292 354,298 360,304" fill="none" stroke="%s" stroke-width="1.6" opacity=".85"/>' % LINE)

# طرحة شبكية بلؤلؤ عند جهته
a('<g opacity=".8" transform="translate(344 148) scale(.62) translate(-344 -148)">')
a('<path d="M340,116 C368,126 384,154 386,190 C387,210 382,226 373,238 L350,228 C362,210 364,184 358,160 C353,142 348,126 338,118 Z" fill="#FFFFFF" opacity=".78" stroke="%s" stroke-width="1.2"/>' % LINE)
for i in range(7):
    a('<path d="M%d,120 C%d,152 %d,192 %d,232" fill="none" stroke="%s" stroke-width=".7" opacity=".85"/>'
      % (340+i*6, 350+i*5, 356+i*4, 353+i*3, LINE))
for i in range(6):
    a('<path d="M338,%d C354,%d 372,%d 384,%d" fill="none" stroke="%s" stroke-width=".7" opacity=".85"/>'
      % (124+i*19, 122+i*19, 126+i*18, 132+i*17, LINE))
for (px,py) in ((344,120),(357,127),(370,140),(379,160),(384,186),(378,212),(365,232),(352,226)):
    a('<circle cx="%d" cy="%d" r="3.4" fill="#FFFFFF" stroke="%s" stroke-width=".9"/>' % (px, py, LINE))
    a('<circle cx="%.1f" cy="%.1f" r="1.1" fill="#FFFFFF"/>' % (px-1.1, py-1.1))
a('</g>')
a('</g>')

# ═════════ العريس ═════════
a('<g id="groom">')
a('<path d="M462,232 C420,236 392,252 384,280 L366,470 L560,470 L542,280 C534,252 504,236 462,232 Z" fill="url(#gSuit)"/>')
a('<path d="M465,272 C463,336 462,406 463,470" fill="none" stroke="#41444F" stroke-width="1.5" opacity=".8"/>')
a('<path d="M542,280 L560,470 L508,470 C516,394 518,320 512,262 Z" fill="#15171E" opacity=".45"/>')
a('<path d="M384,280 L366,470 L406,470 C401,394 399,322 406,266 Z" fill="#3E414D" opacity=".32"/>')
# رقبة (خلف الياقة)
a('<path d="M442,224 h40 v42 h-40 z" fill="%s"/>' % SKIN)
a('<path d="M442,224 h40 v16 c-13,10 -27,10 -40,0 z" fill="%s" opacity=".45"/>' % SKIN_SH)
# ياقة القميص + ياقة الجاكيت
a('<path d="M428,236 C440,254 450,264 462,264 C474,264 484,254 496,236 L490,230 C479,246 470,254 462,254 C454,254 445,246 434,230 Z" fill="#FFFFFF" opacity=".95"/>')
a('<path d="M421,238 C436,262 447,277 462,277 C477,277 488,262 503,238 L496,232 C483,254 472,266 462,266 C452,266 441,254 428,232 Z" fill="#34373F"/>')

a('<g transform="translate(-15 3) rotate(-13 458 196)">')
# ودن
a('<ellipse cx="506" cy="196" rx="11.5" ry="16" fill="%s"/>' % SKIN)
a('<path d="M506,189 q7,5 1,13" fill="none" stroke="%s" stroke-width="1.7" opacity=".6"/>' % SKIN_SH)
# الوش (بروفايل) — يترسم قبل الشعر عشان الشعر يقصّه طبيعي
a('<path d="M436,142 C416,158 404,184 403,206 C402,230 412,248 430,256 L466,246 C444,236 432,218 431,194 C430,172 436,154 446,142 Z" fill="%s"/>' % SKIN)
a('<path d="M404,196 C394,201 392,213 401,218 C405,220 408,217 409,212 Z" fill="%s"/>' % SKIN)
a('<path d="M405,214 C408,236 417,250 432,257 L466,246 C446,238 433,224 427,204 Z" fill="%s" opacity=".45"/>' % HAIR)
a('<path d="M406,218 C411,238 420,250 433,256" fill="none" stroke="%s" stroke-width="1.6" opacity=".45"/>' % SKIN_SH)
# كتلة الشعر فوق الوش
a('<ellipse cx="470" cy="188" rx="53" ry="58" fill="%s"/>' % HAIR)
a('<path d="M470,240 C452,242 440,250 436,262 L494,266 C498,252 488,241 470,240 Z" fill="%s"/>' % HAIR)
a('<path d="M424,158 C434,142 452,133 472,133 C500,133 518,152 520,180 C512,158 494,146 470,147 C450,148 434,152 424,158 Z" fill="%s" opacity=".6"/>' % HAIR2)
a('<path d="M430,150 C444,138 466,134 484,140" fill="none" stroke="%s" stroke-width="3.2" stroke-linecap="round" opacity=".45"/>' % HAIR2)
a('<path d="M452,248 C464,256 482,256 496,248" fill="none" stroke="%s" stroke-width="2.2" opacity=".38"/>' % HAIR2)
for _ in range(9):
    t = R.uniform(-2.5, -0.8)
    ex = 470 + math.cos(t)*53; ey = 188 + math.sin(t)*58
    a('<path d="M%.1f,%.1f q%.1f,%.1f %.1f,%.1f" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round" opacity=".45"/>'
      % (ex, ey, R.uniform(-3,3), R.uniform(-5,-2), R.uniform(-6,6), R.uniform(-8,-4), HAIR2))
a('</g></g>')

# ═════════ ذراعه حوالين ضهرها ═════════
a('<g id="hug">')
a('<path d="M406,288 C368,304 328,350 296,392 C286,404 276,414 268,422" fill="none" stroke="url(#gSleeve)" stroke-width="52" stroke-linecap="round"/>')
a('<path d="M406,294 C372,310 334,354 304,394" fill="none" stroke="#43464F" stroke-width="2.2" opacity=".32"/>')
a('<path d="M272,396 l26,21 -13,16 -26,-21 z" fill="#34373F"/>')
for i in range(3):
    a('<circle cx="%.1f" cy="%.1f" r="2.2" fill="#5E6373"/>' % (274+i*7.4, 406+i*5.9))
a('<g transform="rotate(26 248 436)">')
a('<path d="M218,430 C218,414 233,405 253,405 L278,408 C287,412 287,430 278,439 C267,450 242,456 229,449 C220,445 218,438 218,430 Z" fill="%s"/>' % SKIN)
for i in range(4):
    a('<path d="M%.0f,411 C%.0f,424 %.0f,437 %.0f,447" fill="none" stroke="%s" stroke-width="1.6" opacity=".5"/>'
      % (238+i*12, 236+i*12, 235+i*12, 238+i*12, SKIN_SH))
a('<path d="M218,430 C223,443 238,451 255,451" fill="none" stroke="%s" stroke-width="1.5" opacity=".4"/>' % SKIN_SH)
a('</g></g>')

# ═════════ ذراعها حوالين ضهره ═════════
a('<g id="her-arm">')
HER = "M384,432 C422,424 464,430 498,450"
a('<path d="%s" fill="none" stroke="%s" stroke-width="40" stroke-linecap="round"/>' % (HER, LINE))
a('<path d="%s" fill="none" stroke="url(#gDress)" stroke-width="37" stroke-linecap="round"/>' % HER)
for _ in range(30):
    t = R.uniform(0, 1)
    px = (1-t)**2*384 + 2*(1-t)*t*442 + t*t*498
    py = (1-t)**2*432 + 2*(1-t)*t*420 + t*t*450
    lace(px + R.uniform(-13,13), py + R.uniform(-15,15), R.uniform(5,9), R.uniform(.5,.9))
a('<ellipse cx="502" cy="454" rx="19" ry="14" fill="%s" transform="rotate(20 502 454)"/>' % SKIN)
for i in range(3):
    a('<path d="M%.0f,%.0f q4,9 -1,13" fill="none" stroke="%s" stroke-width="1.4" opacity=".45"/>' % (496+i*7, 446+i*2, SKIN_SH))
a('</g>')

# ═════════ الشجيرات (شريط سفلي بس) ═════════
a('<g id="bushes">')
def clump(cx, cy, rw, rh, col, n=15):
    for _ in range(n):
        t = R.uniform(0, math.pi*2); rr = R.uniform(0, 1)**.6
        x = cx + math.cos(t)*rw*rr; y = cy + math.sin(t)*rh*rr
        ang = R.uniform(-70, 70)
        a('<ellipse cx="%.0f" cy="%.0f" rx="%.0f" ry="%.0f" fill="%s" opacity="%.2f" transform="rotate(%.0f %.0f %.0f)"/>'
          % (x, y, R.uniform(10,18), R.uniform(4.5,8), col, R.uniform(.8,1), ang, x, y))
for x in range(-30, W+60, 56):
    clump(x + R.uniform(-14,14), R.uniform(452, 468), R.uniform(32,48), R.uniform(13,20), R.choice(BUSH), 14)
for x in range(-20, W+60, 78):
    clump(x + R.uniform(-16,16), R.uniform(470, 492), R.uniform(36,52), R.uniform(14,22), R.choice(BUSH[:2]), 15)
for _ in range(22):
    a('<circle cx="%.0f" cy="%.0f" r="%.1f" fill="%s" opacity=".9"/>'
      % (R.uniform(-10, W+10), R.uniform(448, 470), R.uniform(2.5,5.5), R.choice(BLOSS)))
a('</g>')

svg = ('<svg viewBox="45 0 630 470" xmlns="http://www.w3.org/2000/svg" role="img" '
       'aria-label="رسمة كارتون للعريس عبدالله والعروسة خلود">%s</svg>' % "".join(P))
open(sys.argv[1], "w", encoding="utf-8").write(svg)
print("bytes:", len(svg))

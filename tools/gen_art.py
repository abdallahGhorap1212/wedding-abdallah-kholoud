# -*- coding: utf-8 -*-
import random, math, sys

W, H = 720, 620
R = random.Random(23)
P = []
def a(s): P.append(s)

SKIN="#F3C9AC"; SKIN_SH="#E0AA87"
HAIR_G="#6B4632"; HAIR_G2="#83593F"
HAIR_B="#A24E33"; HAIR_B2="#C06845"; HAIR_B3="#7E3620"
JACK_LN="#242737"; JACK_SH="#4B516A"
TROUS="#343849"; TROUS_SH="#2A2D3B"
SHIRT="#FFFFFF"; SHIRT_LN="#E6E2DC"
BOW="#C08A72"
GOWN="#FFFFFF"; GOWN_LN="#E4DBCF"
INK="#3A3230"
LEAF="#9BAF91"; LEAF2="#82997A"; LEAF3="#BCCBB2"
PETAL=["#FFFFFF","#FCF0E9","#F7DCCF","#F0C9B6","#FBE6DC","#FFFFFF"]
CENTER="#E9C58E"

a('<defs>'
  '<linearGradient id="gGown" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#F1EAE1"/></linearGradient>'
  '<linearGradient id="gJack" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#454A5E"/><stop offset="1" stop-color="#2E3140"/></linearGradient><linearGradient id="gLap" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#525872"/><stop offset="1" stop-color="#3A3E51"/></linearGradient>'
  '<radialGradient id="gCheek"><stop offset="0" stop-color="#EF9F84" stop-opacity=".5"/><stop offset="1" stop-color="#EF9F84" stop-opacity="0"/></radialGradient>'
  '<radialGradient id="gHaze"><stop offset="0" stop-color="#F6DED3" stop-opacity=".85"/><stop offset="1" stop-color="#F6DED3" stop-opacity="0"/></radialGradient>'
  '<radialGradient id="gHaze2"><stop offset="0" stop-color="#DDE6D6" stop-opacity=".7"/><stop offset="1" stop-color="#DDE6D6" stop-opacity="0"/></radialGradient>'
  '</defs>')

def sprig(x, base, h, sc, dotmin, dotmax, dens, op=1.0, stemcol=None):
    sway = R.uniform(-30, 30) * sc
    top = base - h
    c1x, c1y = x + sway*.35, base - h*.55
    a('<path d="M%.0f,%.0f Q%.0f,%.0f %.0f,%.0f" fill="none" stroke="%s" stroke-width="%.1f" stroke-linecap="round" opacity="%.2f"/>'
      % (x, base, c1x, c1y, x+sway, top, stemcol or R.choice([LEAF3, LEAF, "#C9D6C0"]), 1.5*sc, .7*op))
    n = int(dens * h / 22)
    for i in range(n):
        t = R.uniform(.06, 1.0)
        px = (1-t)**2*x + 2*(1-t)*t*c1x + t*t*(x+sway)
        py = (1-t)**2*base + 2*(1-t)*t*c1y + t*t*top
        px += R.uniform(-11, 11)*sc; py += R.uniform(-7, 7)*sc
        a('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity="%.2f"/>'
          % (px, py, R.uniform(dotmin, dotmax)*sc, R.choice(PETAL), R.uniform(.7, 1)*op))
    if R.random() < .5:
        for _ in range(R.randint(1,3)):
            t = R.uniform(.1,.8)
            px = (1-t)**2*x + 2*(1-t)*t*c1x + t*t*(x+sway)
            py = (1-t)**2*base + 2*(1-t)*t*c1y + t*t*top
            ang = R.uniform(-80,80)
            a('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" opacity="%.2f" transform="rotate(%.0f %.1f %.1f)"/>'
              % (px, py, R.uniform(6,11)*sc, R.uniform(2,3.4)*sc, R.choice([LEAF,LEAF3,LEAF2]), .75*op, ang, px, py))

def bloom(x, y, r, col=None, ring="#EFE1D5"):
    col = col or R.choice(["#FFFFFF","#FFFFFF","#FDF2EB","#F6D9CB"])
    for k in range(5):
        aa = k*72 + R.uniform(-9,9)
        a('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width=".7"/>'
          % (x+math.cos(math.radians(aa))*r*.55, y+math.sin(math.radians(aa))*r*.55, r*.47, r*.41, col, ring))
    a('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x, y, r*.23, CENTER))

# ── soft background wash ──
a('<ellipse cx="150" cy="470" rx="230" ry="200" fill="url(#gHaze)"/>')
a('<ellipse cx="590" cy="480" rx="230" ry="200" fill="url(#gHaze)"/>')
a('<ellipse cx="360" cy="590" rx="330" ry="130" fill="url(#gHaze2)"/>')

# ══════ BACK MEADOW — tall side framing ══════
a('<g id="m-back">')
for _ in range(34):
    x = R.uniform(-30, W+30)
    if 215 < x < 512:  continue
    sprig(x, R.uniform(540, 640), R.uniform(210, 400), R.uniform(.8,1.15), 2.4, 5.2, 1.5, .9)
for _ in range(14):
    sprig(R.uniform(-20, W+20), R.uniform(590, 640), R.uniform(120, 230), R.uniform(.7,1.0), 2.2, 4.4, 1.4, .7)
a('</g>')

# ══════════════ GROOM  (x≈290) ══════════════
a('<g id="groom">')
a('<path d="M245,424 L240,620 L288,620 L292,478 L296,620 L344,620 L339,424 Z" fill="%s"/>' % TROUS)
a('<path d="M292,478 L296,620 L344,620 L339,424 L302,424 Z" fill="%s" opacity=".5"/>' % TROUS_SH)
AG = "M234,314 C224,350 219,392 221,426 C223,460 235,490 252,508"
AG2 = "M346,314 C356,350 361,392 359,426 C357,460 345,490 328,508"
for d in (AG, AG2):
    a('<path d="%s" fill="none" stroke="%s" stroke-width="45" stroke-linecap="round"/>' % (d, JACK_LN))
    a('<path d="%s" fill="none" stroke="url(#gJack)" stroke-width="41" stroke-linecap="round"/>' % d)
a('<path d="M270,236 h40 v42 h-40 z" fill="%s"/>' % SKIN)
a('<path d="M270,236 h40 v14 c-13,10 -27,10 -40,0 z" fill="%s" opacity=".5"/>' % SKIN_SH)
a('<path d="M290,266 C264,270 244,282 239,300 L230,496 L350,496 L341,300 C336,282 316,270 290,266 Z" fill="%s" stroke="%s" stroke-width="1.4"/>' % (SHIRT, SHIRT_LN))
a('<path d="M290,300 v190" stroke="%s" stroke-width="1.2" fill="none"/>' % SHIRT_LN)
for by in (346, 382, 418, 454): a('<circle cx="290" cy="%d" r="2.4" fill="#D6CFC6"/>' % by)
# jacket fronts
a('<path d="M268,262 C246,264 228,276 221,300 L216,500 L293,500 L293,372 L276,336 Z" fill="url(#gJack)" stroke="%s" stroke-width="1.6"/>' % JACK_LN)
a('<path d="M312,262 C334,264 352,276 359,300 L364,500 L287,500 L287,372 L304,336 Z" fill="url(#gJack)" stroke="%s" stroke-width="1.6"/>' % JACK_LN)
# notch lapels
a('<path d="M268,264 L288,282 L277,340 L262,300 L258,276 Z" fill="url(#gLap)" stroke="%s" stroke-width="1.1"/>' % JACK_LN)
a('<path d="M312,264 L292,282 L303,340 L318,300 L322,276 Z" fill="url(#gLap)" stroke="%s" stroke-width="1.1"/>' % JACK_LN)
a('<path d="M274,258 L290,278 L306,258 L301,253 L290,265 L279,253 Z" fill="%s" stroke="%s" stroke-width="1.1"/>' % (SHIRT, SHIRT_LN))
a('<path d="M290,278 L271,269 L269,291 L290,284 Z" fill="%s"/>' % BOW)
a('<path d="M290,278 L309,269 L311,291 L290,284 Z" fill="%s"/>' % BOW)
a('<ellipse cx="290" cy="281" rx="4.6" ry="5.6" fill="#A87259"/>')
a('<path d="M330,344 l17,4 -2,8 -16,-5 z" fill="#F3DACC"/>')
a('<circle cx="291" cy="378" r="3.4" fill="#5A6078"/>')
a('<path d="M287,398 v96" stroke="#5A6078" stroke-width="1.2" opacity=".5" fill="none"/>')
a('<path d="M316,320 q6,10 2,20" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round"/>' % LEAF2)
a('<ellipse cx="325" cy="322" rx="8" ry="4" fill="%s" transform="rotate(38 325 322)"/>' % LEAF)
bloom(316, 314, 15, "#FFFFFF")
a('<circle cx="308" cy="322" r="4.5" fill="#F3D8CB"/>')
a('<path d="M232,430 h26 M322,430 h26" stroke="%s" stroke-width="1.4" fill="none" opacity=".55"/>' % "#5A6078")
a('<path d="M228,296 C240,308 246,326 247,348 M352,296 C340,308 334,326 333,348" fill="none" stroke="%s" stroke-width="1.4" opacity=".55"/>' % "#5A6078")
a('<ellipse cx="290" cy="524" rx="22" ry="13" fill="%s"/>' % SKIN)
a('<path d="M283,514 v18 M290,513 v20 M297,514 v18" stroke="%s" stroke-width="1.1" opacity=".4" fill="none"/>' % SKIN_SH)
a('<path d="M271,519 q19,11 38,0" fill="none" stroke="%s" stroke-width="1.2" opacity=".45"/>' % SKIN_SH)
# head
a('<g transform="rotate(5 290 238)">')
a('<ellipse cx="252" cy="202" rx="9" ry="13" fill="%s"/>' % SKIN)
a('<ellipse cx="290" cy="194" rx="43" ry="50" fill="%s"/>' % SKIN)
a('<path d="M247,194 C243,157 262,137 291,137 C322,137 336,157 335,188 C332,174 326,164 316,160 C300,174 272,178 258,170 C250,176 248,184 247,194 Z" fill="%s"/>' % HAIR_G)
a('<path d="M258,170 C274,178 300,174 316,160 C306,154 292,152 280,156 C270,159 262,164 258,170 Z" fill="%s"/>' % HAIR_G2)
a('<path d="M266,188 q10,-8 20,-1" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round" opacity=".65"/>' % INK)
a('<path d="M302,186 q10,-6 18,2" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round" opacity=".65"/>' % INK)
a('<path d="M266,206 q10,-9 20,0" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round"/>' % INK)
a('<path d="M303,204 q10,-9 19,1" fill="none" stroke="%s" stroke-width="2.4" stroke-linecap="round"/>' % INK)
a('<path d="M297,210 q7,11 -1,15" fill="none" stroke="%s" stroke-width="1.9" stroke-linecap="round" opacity=".6"/>' % SKIN_SH)
a('<path d="M281,234 q11,10 23,-2" fill="none" stroke="%s" stroke-width="2.3" stroke-linecap="round"/>' % INK)
a('<ellipse cx="268" cy="220" rx="13" ry="8" fill="url(#gCheek)"/><ellipse cx="316" cy="218" rx="12" ry="8" fill="url(#gCheek)"/>')
a('</g></g>')

# ══════════════ BRIDE  (x≈432) ══════════════
a('<g id="veil">')
a('<path d="M478,186 C528,202 554,262 558,334 C562,414 554,496 540,566 L616,600 C634,508 638,398 622,316 C602,226 552,178 496,170 Z" fill="#FFFDFB" opacity=".9" stroke="#E5D3C4" stroke-width="1.8" stroke-linejoin="round"/>')
a('<path d="M498,196 C544,222 572,286 576,356 C579,414 574,470 564,520" fill="none" stroke="#EADAcb" stroke-width="1.7" opacity=".95"/>')
a('<path d="M512,222 C548,258 566,318 568,382 C569,428 565,470 558,506" fill="none" stroke="#F0E2D5" stroke-width="1.3" opacity=".9"/>')
a('<path d="M540,566 C566,576 592,588 616,600" fill="none" stroke="#E5D3C4" stroke-width="1.4" opacity=".8"/>')
a('<path d="M470,192 C502,212 516,258 516,306 C516,332 512,354 506,372 L488,366 C494,340 496,308 492,280 C488,248 478,214 462,200 Z" fill="#FFFDFB" opacity=".7" stroke="#EFE0D2" stroke-width="1.2"/>')
a('</g>')
a('<g id="bride">')
a('<path d="M392,412 C370,462 348,536 338,620 L532,620 C520,536 498,462 476,412 Z" fill="url(#gGown)" stroke="%s" stroke-width="1.6"/>' % GOWN_LN)
for (x1,y1,x2,y2) in ((406,432,376,614),(424,434,414,618),(446,434,458,618),(466,432,496,614)):
    a('<path d="M%d,%d C%d,%d %d,%d %d,%d" fill="none" stroke="%s" stroke-width="1.4" opacity=".75"/>'
      % (x1,y1,(x1+x2)//2-3,(y1+y2)//2,(x1+x2)//2+3,(y1+y2)//2+40,x2,y2, GOWN_LN))
# arms (slim, tapered)
AB = "M398,284 C384,320 376,362 378,404 C380,436 390,460 400,472"
AB2 = "M466,284 C480,320 488,362 486,404 C484,436 474,460 464,472"
for d in (AB, AB2):
    a('<path d="%s" fill="none" stroke="%s" stroke-width="27" stroke-linecap="round"/>' % (d, SKIN))
a('<path d="%s" fill="none" stroke="%s" stroke-width="9" stroke-linecap="round" opacity=".35"/>' % (AB2, SKIN_SH))
a('<path d="M412,234 h40 v34 h-40 z" fill="%s"/>' % SKIN)
a('<path d="M412,234 h40 v14 c-13,10 -27,10 -40,0 z" fill="%s" opacity=".5"/>' % SKIN_SH)
# bodice
a('<path d="M432,272 C414,272 400,276 394,282 L392,416 L472,416 L470,282 C464,276 450,272 432,272 Z" fill="url(#gGown)" stroke="%s" stroke-width="1.6"/>' % GOWN_LN)
a('<path d="M394,282 C399,274 410,270 419,274 C426,277 430,284 432,290 C434,284 438,277 445,274 C454,270 465,274 470,282 C462,300 449,308 432,308 C415,308 402,300 394,282 Z" fill="%s" stroke="%s" stroke-width="1.5"/>' % (GOWN, GOWN_LN))
for (dx,dy) in ((404,300),(418,308),(432,312),(446,308),(460,300)):
    a('<circle cx="%d" cy="%d" r="1.7" fill="%s" opacity=".9"/>' % (dx, dy, GOWN_LN))
a('<path d="M366,292 C372,280 384,275 394,280 L396,306 C386,312 373,310 366,303 Z" fill="url(#gGown)" stroke="%s" stroke-width="1.5"/>' % GOWN_LN)
a('<path d="M498,292 C492,280 480,275 470,280 L468,306 C478,312 491,310 498,303 Z" fill="url(#gGown)" stroke="%s" stroke-width="1.5"/>' % GOWN_LN)
a('<path d="M410,382 h44" stroke="%s" stroke-width="1.2" opacity=".7" fill="none"/>' % GOWN_LN)
# head
a('<g transform="rotate(-5 432 238)">')
a('<circle cx="482" cy="220" r="25" fill="%s"/>' % HAIR_B)
a('<path d="M482,195 a25,25 0 0 1 19,40 C496,220 490,206 478,198 Z" fill="%s"/>' % HAIR_B3)
a('<path d="M468,208 q17,-7 26,6" fill="none" stroke="%s" stroke-width="2" opacity=".85"/>' % HAIR_B2)
bloom(470, 190, 13, "#FFFFFF")
bloom(487, 196, 10, "#FDF2EB")
a('<circle cx="500" cy="206" r="3.4" fill="#F6DFD3"/>')
a('<ellipse cx="432" cy="194" rx="41" ry="48" fill="%s"/>' % SKIN)
a('<path d="M392,198 C387,157 407,135 434,135 C463,135 477,157 475,194 C478,204 480,218 476,230 C468,212 464,194 460,180 C438,194 410,194 399,180 C395,186 393,192 392,198 Z" fill="%s"/>' % HAIR_B)
a('<path d="M399,180 C412,194 440,194 460,180 C450,166 433,160 419,164 C408,167 401,173 399,180 Z" fill="%s"/>' % HAIR_B2)
a('<path d="M394,196 C390,222 392,244 398,258 C392,240 390,218 392,198 Z" fill="%s"/>' % HAIR_B)
a('<path d="M472,192 C478,214 478,236 472,252 C478,232 480,210 476,190 Z" fill="%s"/>' % HAIR_B)
a('<path d="M404,188 q10,-7 19,0" fill="none" stroke="%s" stroke-width="2.1" stroke-linecap="round" opacity=".65"/>' % INK)
a('<path d="M441,186 q10,-6 18,2" fill="none" stroke="%s" stroke-width="2.1" stroke-linecap="round" opacity=".65"/>' % INK)
a('<path d="M403,206 q10,-9 19,0" fill="none" stroke="%s" stroke-width="2.3" stroke-linecap="round"/>' % INK)
a('<path d="M441,204 q10,-9 18,1" fill="none" stroke="%s" stroke-width="2.3" stroke-linecap="round"/>' % INK)
a('<path d="M411,210 q-7,11 1,15" fill="none" stroke="%s" stroke-width="1.9" stroke-linecap="round" opacity=".6"/>' % SKIN_SH)
a('<path d="M421,234 q11,10 23,-2" fill="none" stroke="%s" stroke-width="2.2" stroke-linecap="round"/>' % INK)
a('<ellipse cx="407" cy="220" rx="12" ry="8" fill="url(#gCheek)"/><ellipse cx="452" cy="218" rx="12" ry="8" fill="url(#gCheek)"/>')
a('<circle cx="466" cy="212" r="2.8" fill="#E9C58E"/>')
a('</g></g>')

# ══════════════ BOUQUET ══════════════
a('<g id="bouquet">')
for i in range(11):
    ang = -104 + i*11
    a('<path d="M432,474 q%.0f,%.0f %.0f,%.0f" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round" opacity=".85"/>'
      % (math.cos(math.radians(ang))*34, math.sin(math.radians(ang))*34,
         math.cos(math.radians(ang))*72, math.sin(math.radians(ang))*72, LEAF2))
for _ in range(22):
    ang = R.uniform(-3.5, 0.4); rad = R.uniform(14, 70)
    lx = 432 + math.cos(ang)*rad; ly = 436 + math.sin(ang)*rad*.78
    a('<ellipse cx="%.0f" cy="%.0f" rx="%.0f" ry="%.0f" fill="%s" transform="rotate(%.0f %.0f %.0f)" opacity=".92"/>'
      % (lx, ly, R.uniform(10,18), R.uniform(4,7), R.choice([LEAF,LEAF2,LEAF3]), R.uniform(-75,75), lx, ly))
for _ in range(19):
    ang = R.uniform(-3.3, 0.25); rad = R.uniform(3, 54)
    bloom(432 + math.cos(ang)*rad, 434 + math.sin(ang)*rad*.8, R.uniform(10,16))
a('<path d="M424,470 q7,28 3,58 M440,470 q-6,28 -2,58" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % LEAF2)
a('<ellipse cx="400" cy="478" rx="15" ry="11" fill="%s"/>' % SKIN)
a('<ellipse cx="464" cy="478" rx="15" ry="11" fill="%s"/>' % SKIN)
a('<path d="M418,486 q14,-8 28,0 l-3,14 q-11,-6 -22,0 z" fill="#F2DACC" stroke="#E1C3B2" stroke-width="1"/>')
a('</g>')

# ══════════════ FRONT MEADOW ══════════════
a('<g id="m-front">')
for _ in range(46):
    sprig(R.uniform(-30, W+30), R.uniform(628, 672), R.uniform(70, 165), R.uniform(.85,1.25), 2.2, 4.6, 1.9)
for _ in range(9):
    x = R.choice([R.uniform(-10, 190), R.uniform(530, 730)])
    bloom(x, R.uniform(540, 610), R.uniform(13, 20))
for _ in range(16):
    x = R.uniform(-20, W+20); y = R.uniform(600, 640)
    a('<ellipse cx="%.0f" cy="%.0f" rx="%.0f" ry="%.0f" fill="%s" transform="rotate(%.0f %.0f %.0f)" opacity=".8"/>'
      % (x, y, R.uniform(10,20), R.uniform(3.5,6), R.choice([LEAF,LEAF3]), R.uniform(-60,60), x, y))
a('</g>')

svg = ('<svg viewBox="70 108 580 512" xmlns="http://www.w3.org/2000/svg" role="img" '
       'aria-label="رسمة العريس عبدالله والعروسة خلود">%s</svg>' % ("".join(P),))
open(sys.argv[1], "w", encoding="utf-8").write(svg)
print("bytes:", len(svg))

# -*- coding: utf-8 -*-
import math, random, sys
R = random.Random(5)
S = 300
P=[]
def a(x): P.append(x)

PINK="#E4CBA0"; PINK2="#C9A96E"; PINK3="#F1E3C7"; DEEP="#BE9A60"

def bez(pts, t):
    """cubic bezier point + tangent"""
    p0,p1,p2,p3 = pts
    mt=1-t
    x=mt**3*p0[0]+3*mt*mt*t*p1[0]+3*mt*t*t*p2[0]+t**3*p3[0]
    y=mt**3*p0[1]+3*mt*mt*t*p1[1]+3*mt*t*t*p2[1]+t**3*p3[1]
    dx=3*mt*mt*(p1[0]-p0[0])+6*mt*t*(p2[0]-p1[0])+3*t*t*(p3[0]-p2[0])
    dy=3*mt*mt*(p1[1]-p0[1])+6*mt*t*(p2[1]-p1[1])+3*t*t*(p3[1]-p2[1])
    return x,y,math.degrees(math.atan2(dy,dx))

def leaf(x,y,rot,L,w,col=PINK):
    a('<path d="M0,0 C%.0f,%.0f %.0f,%.0f %.0f,0 C%.0f,%.0f %.0f,%.0f 0,0 Z" fill="%s" transform="translate(%.1f %.1f) rotate(%.1f)"/>'
      % (L*.25,-w, L*.72,-w, L, L*.72,w, L*.25,w, col, x, y, rot))

def flower(x,y,r,col=PINK,ctr=DEEP,n=5):
    for k in range(n):
        aa=k*(360.0/n)
        a('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" transform="rotate(%.0f %.1f %.1f)"/>'
          % (x+math.cos(math.radians(aa))*r*.58, y+math.sin(math.radians(aa))*r*.58, r*.5, r*.36, col, aa, x+math.cos(math.radians(aa))*r*.58, y+math.sin(math.radians(aa))*r*.58))
    a('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x,y,r*.26,ctr))

def bud(x,y,rot,r,col=PINK2):
    a('<path d="M0,0 q%.1f,%.1f 0,%.1f q%.1f,%.1f 0,%.1f z" fill="%s" transform="translate(%.1f %.1f) rotate(%.1f)"/>'
      % (r*1.05,-r*.5,-r*1.7, -r*1.05,-r*.5, r*1.7, col, x,y,rot))

VINES = [
  ([(0,8),(70,10),(126,40),(154,92)],   [(154,92),(176,132),(172,168),(150,192)], 3.4),
  ([(8,0),(10,70),(40,126),(92,154)],   [(92,154),(132,176),(168,172),(192,150)], 3.4),
  ([(0,64),(44,66),(76,90),(94,124)],   None, 2.6),
  ([(64,0),(66,44),(90,76),(124,94)],   None, 2.6),
  ([(0,130),(30,134),(52,150),(64,176)],None, 2.1),
  ([(130,0),(134,30),(150,52),(176,64)],None, 2.1),
  ([(0,196),(22,198),(38,210),(46,230)],None, 1.7),
  ([(196,0),(198,22),(210,38),(230,46)],None, 1.7),
]

def draw_vine(seg, w, deco=True):
    p=seg
    a('<path d="M%.0f,%.0f C%.0f,%.0f %.0f,%.0f %.0f,%.0f" fill="none" stroke="%s" stroke-width="%.1f" stroke-linecap="round" opacity=".95"/>'
      % (p[0][0],p[0][1],p[1][0],p[1][1],p[2][0],p[2][1],p[3][0],p[3][1], PINK2, w))
    if not deco: return
    n = 7
    for i in range(n):
        t = (i+.6)/n
        x,y,ang = bez(p,t)
        side = 1 if i%2==0 else -1
        leaf(x, y, ang + side*(58+R.uniform(-14,14)), R.uniform(16,27), R.uniform(4.5,7.5),
             PINK if i%3 else PINK3)
        if i%3==1:
            bud(x, y, ang - side*70, R.uniform(4,6))

a('<g>')
for seg1, seg2, w in VINES:
    draw_vine(seg1, w)
    if seg2: draw_vine(seg2, w*.8)

# blossoms at vine ends / key points
for (x,y,r) in [(150,192,15),(192,150,15),(94,124,11),(124,94,11),(64,176,8),(176,64,8),
                (46,230,6),(230,46,6),(18,18,13),(58,58,9)]:
    flower(x,y,r, PINK if r>9 else PINK3)
for _ in range(16):
    t=R.random()
    x=R.uniform(4,200); y=R.uniform(4,200)
    if x*x+y*y > 190*190 or x*x+y*y < 900: continue
    a('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity=".85"/>' % (x,y,R.uniform(2,4.2), R.choice([PINK,PINK3,DEEP])))
a('</g>')
svg='<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">%s</svg>'%(S,S,''.join(P))
open(sys.argv[1],'w',encoding='utf-8').write(svg); print("bytes",len(svg))

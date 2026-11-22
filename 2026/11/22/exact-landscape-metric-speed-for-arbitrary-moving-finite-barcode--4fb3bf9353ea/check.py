"""Independent exact-rational L2 secant checks for finite persistence landscapes.
Requires only Python standard library.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt

def f(x):return F(x)
def tent(bar, x):
    b,d=bar
    return max(F(0),min(x-b,d-x))
def landscape(bars,x):
    return sorted((tent(bar,x) for bar in bars),reverse=True)
def segments(bar):
    b,d=bar; m=(b+d)/2
    return [(b,m,F(1),-b),(m,d,F(-1),d)]
def breaks(bars):
    pts={v for b,d in bars for v in (b,(b+d)/2,d)}
    ss=[segments(bar) for bar in bars]
    for i in range(len(bars)):
      for j in range(i):
        for aa,bb,s,c in ss[i]:
          for cc,dd,t,e in ss[j]:
            l,r=max(aa,cc),min(bb,dd)
            if l<r and s!=t:
              x=(e-c)/(s-t)
              if l<x<r:pts.add(x)
    return pts

def distance_power(bars0,bars1,power=2):
    bp=sorted(breaks(bars0)|breaks(bars1))
    assert power in (1,2,3)
    total=F(0)
    for l,r in zip(bp,bp[1:]):
        va,vb=landscape(bars0,l),landscape(bars1,l)
        wa,wb=landscape(bars0,r),landscape(bars1,r)
        for a,b,c,d in zip(va,vb,wa,wb):
            u,v=b-a,d-c
            if power==2:
                area=(u*u+u*v+v*v)/3
            else:
                a,b=abs(u),abs(v)
                if u*v>=0:
                    area=(a+b)/2 if power==1 else (a*a*a+a*a*b+a*b*b+b*b*b)/4
                else:
                    area=(a*a+b*b)/(2*(a+b)) if power==1 else (a**4+b**4)/(4*(a+b))
            total+=(r-l)*area
    return total

def predicted(bars,vel,power=2):
    return sum(((d-b)*(abs(v[0])**power+abs(v[1])**power)/2 for (b,d),v in zip(bars,vel)),F(0))

def shift(bars,vel,h):
    return [(b+h*v[0],d+h*v[1]) for (b,d),v in zip(bars,vel)]

cases=[
 ('moving-single',[(F(1),F(5))],[(F(2),F(-1))]),
 ('overlapping',[(F(0),F(5)),(F(1),F(8)),(F(2),F(11))],[(F(1),F(2)),(F(-2),F(-1)),(F(3),F(-1))]),
 ('shared-birth',[(F(0),F(6)),(F(0),F(9)),(F(0),F(12))],[(F(1),F(2)),(F(-1),F(-2)),(F(3),F(1))]),
 ('identical-bar',[(F(1),F(7)),(F(1),F(7))],[(F(2),F(0)),(F(-1),F(3))]),
 ('shared-death',[(F(0),F(8)),(F(3),F(8))],[(F(-2),F(1)),(F(1),F(-2))]),
 ('bar-crossing',[(F(0),F(5)),(F(2),F(7))],[(F(2),F(1)),(F(-2),F(-1))]),
]
rng=Random(20261118)
for t in range(12):
    n=rng.randrange(1,6)
    bars=[]; vel=[]
    for i in range(n):
        b=F(rng.randrange(-8,8),2);d=b+F(rng.randrange(1,14),2)
        bars.append((b,d))
        vel.append((F(rng.randrange(-3,4)),F(rng.randrange(-3,4))))
    cases.append((f'random-{t}',bars,vel))

checks=0
for name,bars,vel in cases:
   for power in (1,2,3):
      goal=predicted(bars,vel,power)
      for den in [128,2048,16384]:
        for sign in [-1,1]:
          h=F(sign,den)
          new=shift(bars,vel,h)
          if not all(b<d for b,d in new): continue
          val=distance_power(bars,new,power)/abs(h)**power
          error=abs(float(val-goal))
          if den==16384 and error>0.0015*max(float(goal),1)+0.03:
             raise AssertionError((name,power,float(val),float(goal)))
          checks+=1
   print(f'{name}: L2 predicted speed^2={float(predicted(bars,vel,2)):.7f}; secant^2 at h=+/-1/2048: '+', '.join(f'{float(distance_power(bars,shift(bars,vel,F(s,2048)),2)/F(1,2048)**2):.7f}' for s in (-1,1)))
print('PASS',checks,'exact rational L1/L2/L3 secant-distance comparisons, across',len(cases),'families')

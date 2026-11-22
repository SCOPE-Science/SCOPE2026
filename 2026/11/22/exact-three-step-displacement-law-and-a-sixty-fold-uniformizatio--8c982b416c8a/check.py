"""Reproducible exact polygon and Fourier certificate for an orthogonal-tent transport law.
All geometric clipping, coefficients, residue checks, and density extrema use rational arithmetic.
"""
from fractions import Fraction as F
from collections import defaultdict
import math, cmath
Z=F(0); O=F(1)

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scl(c,a):return tuple(c*x for x in a)
def val(af,p):return af[0]*p[0]+af[1]*p[1]+af[2]
def area(p):return sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1]))/2

def clip(poly, af, h, above=True):
 def g(p):
  v=val(af,p)-h
  return v if above else -v
 out=[]
 for a,b in zip(poly,poly[1:]+poly[:1]):
  fa,fb=g(a),g(b)
  if fa>=0:out.append(a)
  if (fa>0 and fb<0) or (fa<0 and fb>0):
   t=fa/(fa-fb)
   out.append(tuple(v+t*(w-v) for v,w in zip(a,b)))
 if len(out)>1:
  out2=[]
  for p in out:
   if not out2 or p!=out2[-1]:out2.append(p)
  if len(out2)>1 and out2[0]==out2[-1]:out2.pop()
  out=out2
 if len(out)<3 or area(out)==0:return []
 if area(out)<0:out.reverse()
 return out

def fsplit(poly,af):
 mn=min(val(af,p) for p in poly)*2
 mx=max(val(af,p) for p in poly)*2
 for i in range(math.floor(mn),math.floor(mx)+1):
  pl=clip(poly,af,F(i,2),True)
  if not pl:continue
  pl=clip(pl,af,F(i+1,2),False)
  if not pl:continue
  z = add(scl(F(2 if i%2==0 else -2),af),(Z,Z,F(-i if i%2==0 else i+1)))
  yield pl,z

def split_steps(n):
 states=[([(Z,Z),(O,Z),(O,O),(Z,O)],(O,Z,Z),(Z,O,Z))]
 for step in range(n):
  after=[]
  for pol,x,y in states:
   for pp,fy in fsplit(pol,y):
    xx=add(x,fy)
    for ppp,fx in fsplit(pp,xx):
     yy=add(y,fx)
     after.append((ppp,xx,yy))
  states=after
  assert sum(area(s[0]) for s in states)==1
 return states

from collections import defaultdict

def exact(states):
 A=defaultdict(F);B=defaultdict(F);D=defaultdict(F)
 for p,x,y in states:
  g=add(x,(-O,Z,Z));a,b,c=g
  if a==b==0:A[c%1]+=area(p);continue
  gn=a*a+b*b
  for v,w in zip(p,p[1:]+p[:1]):
   dx=w[0]-v[0];dy=w[1]-v[1];flux=a*dy-b*dx
   if not flux:continue
   da=a*dx+b*dy
   phi=val(g,v); phi2=val(g,w)
   if da==0: B[phi%1]+=flux/gn
   else:
    coeff=flux/(gn*da)
    D[phi2%1]+=coeff;D[phi%1]-=coeff
 return [{r:c for r,c in S.items() if c} for S in [A,B,D]]

EXPECTED={
 F(0):F(2524,1225),F(1,6):F(-432,1225),F(5,6):F(-432,1225),
 F(1,5):F(-250,441),F(4,5):F(-250,441),F(1,4):F(-128,225),
 F(3,4):F(-128,225),F(1,3):F(-486,245),F(2,3):F(-486,245),
 F(2,5):F(250,441),F(3,5):F(250,441),F(1,2):F(41344,11025)
}
COS6=[F(1),F(1,2),F(-1,2),F(-1),F(-1,2),F(1,2)]
COS4=[F(1),F(0),F(-1),F(0)]
COS3=[F(1),F(-1,2),F(-1,2)]
COS5=[(F(1),F(0)),(F(-1,4),F(1,4)),(F(-1,4),F(-1,4)),
      (F(-1,4),F(-1,4)),(F(-1,4),F(1,4))]
COS5X2=[(F(1),F(0)),(F(-1,4),F(-1,4)),(F(-1,4),F(1,4)),
        (F(-1,4),F(1,4)),(F(-1,4),F(-1,4))]

def spectral_pair(k,d):
 """Return (r,s) such that sum_r d[r] cos(2*pi*k*r) = r+s*sqrt(5)."""
 a=d[F(0)]+d[F(1,2)]*(-1)**k
 a+=2*d[F(1,6)]*COS6[k%6]
 a+=2*d[F(1,4)]*COS4[k%4]
 a+=2*d[F(1,3)]*COS3[k%3]
 b=F(0)
 for r,tab in ((F(1,5),COS5),(F(2,5),COS5X2)):
  x,y=tab[k%5]
  a+=2*d[r]*x;b+=2*d[r]*y
 return a,b

def bernoulli_2(t):
 r=t%1
 return r*r-r+F(1,6)

def density(t,d):
 return F(1)-sum(v*bernoulli_2(t-r) for r,v in d.items())/2

def main():
 states=split_steps(3)
 assert len(states)==320
 A,B,D=exact(states)
 assert A=={} and B=={} and D==EXPECTED
 assert sum(D.values())==0
 assert len(D)==12
 assert spectral_pair(1,D)==(F(-646,11025),F(-250,441))
 zeros=[k for k in range(60) if spectral_pair(k,D)==(F(0),F(0))]
 assert zeros==[0]
 values={r:density(r,D) for r in D}
 assert min(values.values())==F(893,1225)
 assert max(values.values())==F(352,315)
 assert {r for r,v in values.items() if v==F(893,1225)}=={F(1,2)}
 assert {r for r,v in values.items() if v==F(352,315)}=={F(1,4),F(3,4)}
 assert all(v>0 for v in values.values())
 print('PASS: 320 exact rational polygon domains; A=B=0; 12 rational phase coefficients')
 print('PASS: exact Fourier zeros precisely k congruent 0 modulo 60')
 print('PASS: exact density extrema 893/1225 and 352/315')

if __name__=='__main__':main()

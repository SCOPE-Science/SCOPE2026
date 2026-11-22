#!/usr/bin/env python3
"""Independent finite diagnostics for the right-square-pyramid brightness formulas.

No external dependencies. Execute: python CHECK.py
The finite diagnostics do not certify the infinite statements.
"""
import math,random,itertools
R=random.Random(102340)
PI=math.pi

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def norm(a):return math.sqrt(dot(a,a))
def B(u,h):
 x,y,c=map(abs,u)
 return 2*c+max(c,h*x)+max(c,h*y)
def hull(points):
 p=sorted(set(points))
 def ccw(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 low=[]
 for x in p:
  while len(low)>1 and ccw(low[-2],low[-1],x)<=0:low.pop()
  low.append(x)
 high=[]
 for x in p[::-1]:
  while len(high)>1 and ccw(high[-2],high[-1],x)<=0:high.pop()
  high.append(x)
 return low[:-1]+high[:-1]
def direct_area(u,h):
 ref=(0,0,1) if abs(u[2])<0.85 else (0,1,0)
 v=cross(u,ref);v=tuple(t/norm(v) for t in v)
 w=cross(u,v)
 vertices=[(x,y,0) for x in [-1,1] for y in [-1,1]]+[(0,0,h)]
 poly=hull([(dot(P,v),dot(P,w)) for P in vertices])
 return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])))/2

def sphere():
 u=[R.gauss(0,1) for _ in range(3)];d=norm(u);return tuple(z/d for z in u)
def extrema(h):return min(h,4*h/math.sqrt(h*h+2)),max(4,math.sqrt(2*h*h+4))
def low(h):
 if h<math.sqrt(14)-1e-10:return 8/(9*PI*h)
 if h>math.sqrt(14)+1e-10:return (h*h+2)**3.5/(16*PI*h*(h*h-2)**2)
 return 8/(PI*math.sqrt(14))
def high(h):
 if h<math.sqrt(6)-1e-10:return .25
 if h>math.sqrt(6)+1e-10:return 4/math.sqrt(2*h*h+4)
 return 1.25
count=0
for h in [0.2,0.5,1,2,math.sqrt(6),3,math.sqrt(14),4,10]:
 mi,ma=extrema(h)
 candidates=[(1,0,0),(0,1,0),(0,0,1),tuple(t/math.sqrt(h*h+2) for t in (1,1,h))]
 assert abs(min(B(u,h) for u in candidates)-mi)<1e-12;count+=1
 maxi=[(0,0,1),tuple(t/math.sqrt(2*h*h+4) for t in (h,h,2))]
 assert abs(max(B(u,h) for u in maxi)-ma)<1e-12;count+=1
 for i in range(333):
  u=sphere();p=B(u,h);d=direct_area(u,h)
  assert abs(p-d)<1e-9*(1+h),(h,u,p,d);count+=1
  assert mi-1e-10 <=p<=ma+1e-10;count+=1
 assert low(h)>0 and high(h)>0;count+=1
# critical coexistence and exact coefficients
s14=math.sqrt(14);s6=math.sqrt(6)
assert abs(8/(9*PI*s14)+64/(9*PI*s14)-low(s14))<1e-12;count+=1
assert abs(.25+1.-high(s6))<1e-12;count+=1
assert abs(s14-4*s14/math.sqrt(16))<1e-12;count+=1
assert abs(4-math.sqrt(2*s6*s6+4))<1e-12;count+=1
print(f'PASS: {count} deterministic finite diagnostics')

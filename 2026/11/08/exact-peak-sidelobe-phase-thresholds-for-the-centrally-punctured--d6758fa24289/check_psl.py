#!/usr/bin/env python3
"""Exact finite phase-alphabet peak-autocorrelation certification.
No floating arithmetic or tolerance is used for any acceptance decision.
"""
from itertools import product
import json
import sys
S=tuple((i,j) for i in range(3) for j in range(3) if (i,j)!=(1,1))
fixed=((0,0),(0,1),(1,0))
free=tuple(s for s in S if s not in fixed)
index={s:i for i,s in enumerate(S)}
shifts=[]
for u in range(3):
 for v in range(-2,3):
  if u==0 and v<=0:continue
  pairs=tuple((index[(i+u,j+v)],index[(i,j)]) for i,j in S if (i+u,j+v) in index)
  if pairs:shifts.append(((u,v),pairs))
assert len(shifts)==12
cos2={2:(2,-2),3:(2,-1,-1),4:(2,0,-2,0),6:(2,1,-1,-2,-1,1)}
# score units: integer for orders 2,3,4,6; Q(sqrt5)/2 for order 5;
# Z[x]/(x^3+x^2-2x-1) for order 7, x=2cos(2pi/7);
# Z[sqrt2] for order 8.
C7=((2,0,0),(0,1,0),(-2,0,1),(1,-1,-1),(1,-1,-1),(-2,0,1),(0,1,0))
C8=((2,0),(0,1),(0,0),(0,-1),(-2,0),(0,-1),(0,0),(0,1))
L7=1246979603717467;H7=1246979603717468;D7=10**15
poly=lambda t:t*t*t + D7*t*t -2*D7*D7*t-D7**3
assert poly(L7)<0<poly(H7)

def sqrtcmp(a,b,radicand):
 u,v=a[0]-b[0],a[1]-b[1]
 if v==0:return (u>0)-(u<0)
 if u==0:return (v>0)-(v<0)
 if (u>0)==(v>0):return (u>0)-(u<0)
 return ((u>0)-(u<0)) if u*u>radicand*v*v else ((v>0)-(v<0))

def cmp7(a,b):
 c=[a[i]-b[i] for i in range(3)]
 if c==[0,0,0]:return 0
 low=c[0]*D7*D7+c[1]*D7*(L7 if c[1]>=0 else H7)+c[2]*(L7*L7 if c[2]>=0 else H7*H7)
 high=c[0]*D7*D7+c[1]*D7*(H7 if c[1]>=0 else L7)+c[2]*(H7*H7 if c[2]>=0 else L7*L7)
 if low>0:return 1
 if high<0:return -1
 raise ArithmeticError('Insufficient isolating bracket for x=2cos(2pi/7): '+str(c))

def cmp(a,b,q):
 if q==7:return cmp7(a,b)
 if q==5:return sqrtcmp(a,b,5)
 if q==8:return sqrtcmp(a,b,2)
 return (a[0]>b[0])-(a[0]<b[0])

def sqnorm(ts,q):
 n=len(ts)
 if q in cos2:
  c=cos2[q];v=n
  for i in range(n):
   for j in range(i):v+=c[(ts[i]-ts[j])%q]
  return (v,)
 if q==5:
  a,b=2*n,0
  for i in range(n):
   for j in range(i):
    d=(ts[i]-ts[j])%5
    if d==0:a+=4
    elif d in (1,4):a-=1;b+=1
    else:a-=1;b-=1
  return (a,b)
 if q==7:
  v=[n,0,0]
  for i in range(n):
   for j in range(i):
    w=C7[(ts[i]-ts[j])%7]
    for k in range(3):v[k]+=w[k]
  return tuple(v)
 if q==8:
  a,b=n,0
  for i in range(n):
   for j in range(i):
    u,v=C8[(ts[i]-ts[j])%8];a+=u;b+=v
  return (a,b)
 raise ValueError(q)

def score(xs,q):
  x=[0]*len(S)
  for i,pt in enumerate(free):x[index[pt]]=xs[i]
  worst=None
  for _,pairs in shifts:
    v=sqnorm(tuple((x[a]-x[b])%q for a,b in pairs),q)
    if worst is None or cmp(v,worst,q)>0:worst=v
  return worst

expected={2:((4,),20),3:((3,),8),4:((2,),24),5:((3,1),240),6:((1,),2),7:((0,0,1),28),8:((2,0),114)}
catalog={}
for q in range(2,9):
  best=None;winners=[]
  for xs in product(range(q),repeat=5):
    z=score(xs,q)
    if best is None or cmp(z,best,q)<0:best=z;winners=[xs]
    elif cmp(z,best,q)==0:winners.append(xs)
  assert (best,len(winners))==expected[q],(q,best,len(winners))
  catalog[str(q)]=[list(row) for row in winners]
  print('q',q,'min representation',best,'normalized',len(winners),'total',len(winners)*q**3,'witness',winners[0])
  if q==6:assert winners==[(1,4,5,2,0),(5,2,1,4,0)]
print('HOLLOW_SQUARE_PSL_EXACT_PASS cases='+str(sum(q**5 for q in range(2,9))))

if len(sys.argv)==3 and sys.argv[1]=='--catalog':
  with open(sys.argv[2],encoding='utf-8') as stream:
    reference=json.load(stream)
  assert reference==catalog,'Optimizer catalog does not match exhaustive exact computation'
  print('OPTIMIZER_CATALOG_EXACT_MATCH')
elif len(sys.argv)!=1:
  raise SystemExit('Usage: python3 check_psl.py [--catalog OPTIMIZERS.json]')

"""Standalone finite checks for the three-coordinate softmax rounding theorem.
Run: python checker.py. Requires numpy and scipy only for optional LP cross-check.
"""
import math,itertools,random
from fractions import Fraction
from collections import defaultdict

BITS=list(itertools.product((0,1),repeat=3))

def bounds(p):
 p1,p2,p3=p
 return max(0,p1*(p2+p3-1),p2*(p1+p3-1),p3*(p1+p2-1)), min(p1*p2,p1*p3,p2*p3,1-sum(p)+p1*p2+p1*p3+p2*p3)

def law(p,t):
 p1,p2,p3=p
 return {(1,1,1):t,(1,1,0):p1*p2-t,(1,0,1):p1*p3-t,(0,1,1):p2*p3-t,
 (1,0,0):p1-p1*p2-p1*p3+t,(0,1,0):p2-p1*p2-p2*p3+t,(0,0,1):p3-p1*p3-p2*p3+t,
 (0,0,0):1-sum(p)+p1*p2+p1*p3+p2*p3-t}

def logsumexp(values):
 M=max(values)
 return M+math.log(sum(math.exp(z-M) for z in values))

def f(bits,lower,upper,extra):
 return logsumexp([lower[i]+upper[i]*bits[i] for i in range(3)]+list(extra))

def mixed(lower,upper,extra):
 return sum((1 if sum(bits)%2 else -1)*f(bits,lower,upper,extra) for bits in BITS)

def expected(p,t,lower,upper,extra,label=0):
 lawdict=law(p,t)
 return sum(lawdict[b]*(f(b,lower,upper,extra)-([lower[i]+upper[i]*b[i] for i in range(3)]+list(extra))[label]) for b in BITS)

checks=0
rng=random.Random(470205)
for _ in range(400):
 p=[rng.uniform(0.03,0.97) for i in range(3)]
 lower=[rng.uniform(-3,3) for i in range(3)]
 upper=[rng.uniform(0.03,4) for i in range(3)]
 extra=[rng.uniform(-3,3) for i in range(rng.randrange(4))]
 lo,hi=bounds(p); t0=math.prod(p)
 assert lo-1e-13<=t0<=hi+1e-13
 for t in [lo,hi,t0,(lo+hi)/2]:
  lawdict=law(p,t)
  assert min(lawdict.values())>=-1e-12
  assert abs(sum(lawdict.values())-1)<1e-12
  for i in range(3):
   assert abs(sum(v for b,v in lawdict.items() if b[i])-p[i])<1e-12
   for j in range(i+1,3):
    assert abs(sum(v for b,v in lawdict.items() if b[i] and b[j])-p[i]*p[j])<1e-12
  checks+=1
 c=mixed(lower,upper,extra)
 assert c>0
 for y in range(3+len(extra)):
  rlo=expected(p,lo,lower,upper,extra,y); rhi=expected(p,hi,lower,upper,extra,y)
  r0=expected(p,t0,lower,upper,extra,y)
  assert rlo+1e-11 < r0 < rhi-1e-11
  assert abs((r0-rlo)-(t0-lo)*c)<3e-12
  checks+=1
# exact fractional certificate for probabilities, no rounding
for i in range(2,10):
 for j in range(2,10):
  for k in range(2,10):
   p=(Fraction(i,11),Fraction(j,11),Fraction(k,11))
   lo,hi=bounds(p)
   assert lo<math.prod(p)<hi
   for t in (lo,hi):
    z=law(p,t)
    assert all(v>=0 for v in z.values())
    assert sum(z.values())==1
   checks+=1
# optional external linear programming check: enumerate exact constraints and minimize E logsumexp
try:
 import numpy as np
 from scipy.optimize import linprog
 eq=[[1.0]*8];
 for i in range(3):eq.append([float(b[i]) for b in BITS])
 for i,j in [(0,1),(0,2),(1,2)]:eq.append([float(b[i]*b[j]) for b in BITS])
 for _ in range(100):
  p=[rng.uniform(0.1,0.9) for _ in range(3)]
  low=[rng.uniform(-2,2) for _ in range(3)]
  gap=[rng.uniform(0.1,4) for _ in range(3)]
  ext=[rng.uniform(-2,2) for _ in range(rng.randrange(3))]
  v=[f(b,low,gap,ext) for b in BITS]
  rhs=[1.0,*p,p[0]*p[1],p[0]*p[2],p[1]*p[2]]
  fit=linprog(v,A_eq=eq,b_eq=rhs,bounds=(0,None),method='highs')
  assert fit.success
  lo,hi=bounds(p)
  optimum=sum(law(p,lo)[b]*v[i] for i,b in enumerate(BITS))
  assert abs(fit.fun-optimum)<1e-8
  checks+=1
 print('scipy LP cross-checks: 100')
except ImportError:
 print('scipy LP cross-checks skipped: scipy or numpy unavailable')
# example and asymptotic
for h in (0.1,0.4,1,2,4,8,20):
 p=[.5]*3; low=[0.]*3; gaps=[h]*3
 lo,hi=bounds(p)
 c=mixed(low,gaps,())
 formula=h+3*math.log(2+math.exp(h))-3*math.log(1+2*math.exp(h))
 assert abs(c-formula)<3e-11
 assert abs((expected(p,math.prod(p),low,gaps,(),0)-expected(p,lo,low,gaps,(),0))-c/8)<1e-11
 checks+=1
# Higher-dimensional moment-preserving couplings and sign-alternating loss laws.
def q_ind(p,b):
 return math.prod((p[i] if b[i] else 1-p[i]) for i in range(len(p)))
def parameter_interval(p):
 z=[(b,q_ind(p,b)) for b in itertools.product((0,1),repeat=len(p))]
 n=len(p)
 return -min(q for b,q in z if (n-sum(b))%2==0), min(q for b,q in z if (n-sum(b))%2==1)
def coupled(p,b,theta):
 return q_ind(p,b)+((-1)**(len(p)-sum(b)))*theta
def general_f(bits,base,gaps,extra=()):
 return logsumexp([base[i]+gaps[i]*bits[i] for i in range(len(bits))]+list(extra))
for n in range(3,7):
 for _ in range(60):
  p=[rng.uniform(.07,.93) for i in range(n)]
  base=[rng.uniform(-2,2) for i in range(n)]
  gaps=[rng.uniform(.2,2) for i in range(n)]
  ext=[rng.uniform(-2,2) for i in range(rng.randrange(3))]
  bs=list(itertools.product((0,1),repeat=n))
  lo,hi=parameter_interval(p)
  assert lo<0<hi
  delta=sum(((-1)**(n-sum(b)))*general_f(b,base,gaps,ext) for b in bs)
  assert (-1 if n%2==0 else 1)*delta>1e-14
  opt=lo if n%2 else hi
  law0=[coupled(p,b,0) for b in bs]
  lawopt=[coupled(p,b,opt) for b in bs]
  assert min(lawopt)>=-1e-12 and abs(sum(lawopt)-1)<1e-12
  for mask in range(1<<n):
   if mask==(1<<n)-1:continue
   m0=sum(v*math.prod(b[j] for j in range(n) if mask>>j&1) for b,v in zip(bs,law0))
   m1=sum(v*math.prod(b[j] for j in range(n) if mask>>j&1) for b,v in zip(bs,lawopt))
   assert abs(m0-m1)<3e-13
  gain=sum((v0-v1)*general_f(b,base,gaps,ext) for b,v0,v1 in zip(bs,law0,lawopt))
  assert abs(gain+opt*delta)<2e-11 and gain>0
  checks+=1
for n in range(3,8):
 h=20
 bs=list(itertools.product((0,1),repeat=n))
 delta=sum((-1)**(n-sum(b))*general_f(b,[0]*n,[h]*n) for b in bs)
 const=(-1)**n*math.log(n)+sum((-1)**(n-k)*math.comb(n,k)*math.log(k) for k in range(1,n+1))
 assert abs(delta-((-1)**(n+1)*h+const))<1e-5
 checks+=1

print('PASS',checks,'checks')
print('halfway h=4 independent->optimal log-loss gain:',(4+3*math.log(2+math.exp(4))-3*math.log(1+2*math.exp(4)))/8)

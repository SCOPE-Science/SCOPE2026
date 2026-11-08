"""Reproduce exact algebraic identities and numerical stress tests for stationary scalar Kalman precision allocation.

Python 3 standard library only. Finite tests supplement, and do not replace, the analytic argument.
"""
from fractions import Fraction as F
from math import sqrt, isfinite
from random import Random

checks=0
def require(condition, msg='assertion failed'):
    global checks
    checks+=1
    if not condition: raise AssertionError(msg)

def update(p,s,q,u):
    z=s*p+q
    return z/(1+u*z)

def stationary(s,q,u):
    # positive root of u*s*p^2 + (u*q+1-s)*p -q=0
    b=u*q+1-s
    return 2*q/(b+sqrt(b*b+4*u*s*q))

def cyc(s,q,prec):
    p=1.
    for j in range(10000):
        prev=p
        for u in prec:p=update(p,s,q,u)
        if abs(p-prev)<1e-13*max(1,abs(p)):break
    vals=[]
    for u in prec:
        p=update(p,s,q,u)
        vals.append(p)
    return vals

# Exact rational inversion, derivative signs, telescoping identity.
for s in [F(0),F(1,8),F(1,2),F(4,5),F(1),F(2),F(10)]:
 for q in [F(1,3),F(1),F(5,2)]:
  for p in [F(1,10),F(1,2),F(3),F(20)]:
   g=1/p - 1/(s*p+q)
   lhs=(s-1)*p+q
   require(g==lhs/(p*(s*p+q)))
   if s>=1 or (s<1 and p<=q/(1-s)):
    gp=-1/(p*p)+s/(s*p+q)**2
    gpp=2/p**3-2*s*s/(s*p+q)**3
    require(gp<0)
    require(gpp>0)

# Exact two-cycle example: s=2, q=1, precisions 0 then 1.
# Orbit entries p0 = sqrt(3)/2, p1=1+sqrt(3).
vals=cyc(2.,1.,[0.,1.])
require(abs(vals[0]-(1+sqrt(3)))<1e-11)
require(abs(vals[1]-sqrt(3)/2)<1e-11)
require((sum(vals)/2)>stationary(2.,1.,0.5))

rng=Random(62720254)
for trial in range(2400):
 s=rng.choice([0.,0.002,0.3,0.99,1.,1.1,2.,5.,30.])
 q=rng.uniform(0.2,4.)
 m=rng.randint(2,13)
 u=[rng.random()*rng.uniform(0.01,4.) for _ in range(m)]
 if trial%7==0: u[rng.randrange(m)]=0.
 avg=sum(u)/m
 vals=cyc(s,q,u)
 mu=sum(vals)/m
 base=stationary(s,q,avg)
 require(mu+3e-9*max(1,mu)>=base, f'optimality {trial}: {mu}, {base}')
 require(all(isfinite(v) and v>0 for v in vals))
 # Cyclic inversion identity, including wrap and zero-precision locations.
 gsum=sum(1/v-1/(s*v+q) for v in vals)
 require(abs(gsum-sum(u))<3e-8*max(1.,sum(u)))

# Continuous finite-horizon boundary identity and Jensen lower bound (s>=1).
for trial in range(200):
 s=rng.choice([1.,2.,6.]);q=rng.uniform(.2,2.);p=rng.uniform(.05,3.)
 n=rng.randint(5,100)
 u=[rng.random()*3 for _ in range(n)]
 prev=p; vals=[]
 for x in u:
  prev=update(prev,s,q,x)
  vals.append(prev)
 gsum=sum(1/x-1/(s*x+q) for x in vals)
 rhs=sum(u)-(1/(s*vals[-1]+q)-1/(s*p+q))
 require(abs(gsum-rhs)<1e-8*max(1.,sum(u)))

print(f'PASS {checks} exact-algebraic and numerical assertions')
print('s=2,q=1,u=(0,1): periodic posterior =',*[round(v,12) for v in cyc(2.,1.,[0.,1.])])
print('period-average =',round(sum(cyc(2.,1.,[0.,1.]))/2,12))
print('constant precision benchmark =',round(stationary(2.,1.,0.5),12))

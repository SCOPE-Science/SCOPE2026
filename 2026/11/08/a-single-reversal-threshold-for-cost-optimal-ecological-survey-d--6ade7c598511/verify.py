#!/usr/bin/env python3
"""Self-contained arithmetic checks of the persistent-rate ecological survey theorem.
All global claims require the analytic proof; sampled grids are diagnostic only.
"""
from fractions import Fraction as F
from math import exp, log, isfinite

def bisect_increasing(fun, lo, hi, iterations=100):
    assert fun(lo) <= 0 < fun(hi), (lo,hi,fun(lo),fun(hi))
    for _ in range(iterations):
        mi=(lo+hi)/2
        if fun(mi)>0: hi=mi
        else: lo=mi
    return (lo+hi)/2

def optimum_gamma(k, q, M):
    alpha=(1-q)/q
    if M<=1/q: return 0.0
    w=bisect_increasing(lambda w:w+alpha*w**(k+1)-M,1.0,max(2.0,M))
    return k*(w-1)

def optimum_fixed(q,M):
    if M<=1/q: return 0.0
    return log((M-1)*q/(1-q))

def cross_time(k,q):
    alpha=(1-q)/q
    fun=lambda x:exp(x)-(1+x/k)**(k+1)-x/(k*alpha)
    # strictly negative close to zero; a single positive zero by F''' > 0.
    lo=1e-5
    hi=1.0
    while fun(hi)<=0: hi*=2
    return bisect_increasing(fun,lo,hi)

checks=0
# Exact identities for integer Gamma shape parameters, rational t and occupancy.
for k in range(1,9):
  for q in [F(1,8),F(1,4),F(1,2),F(3,4),F(7,8)]:
   alpha=(1-q)/q
   for x in [F(0),F(1,10),F(1),F(2),F(5)]:
    w=1+x/k
    S=w**(-k)
    h=S/w
    # Model mean is normalized to one.
    Rgamma=h/(alpha+S)
    Rfixed=1/(1+alpha*F.from_float(exp(float(x)))) if x else q
    assert Rgamma==1/(w+alpha*w**(k+1))
    checks+=1
    # exact positive identity for derivative curvature
    # S''S - (S')^2 = S^2/(k*w^2)>0.
    second=S*(k+1)/(k*w*w)
    assert second*S-h*h==S*S/(k*w*w)
    checks+=1

# Direct derivative sign test for the cost using symmetric finite differences.
for k in [0.3,0.75,1,2,5,10]:
 for q in [0.1,0.3,0.5,0.8,0.95]:
  for M in [1/q-0.001,1/q+0.001,1/q+0.25,1/q+2,1/q+20,1/q+200]:
   t=optimum_gamma(k,q,M)
   assert isfinite(t) and t>=0
   derivative=lambda z:(1-q)+q*(1+z/k)**(-k)-q*M*(1+z/k)**(-k-1)
   if M<=1/q:
    assert derivative(0)>=-1e-10
   else:
    assert abs(derivative(t))<1e-8, (k,q,M,t,derivative(t))
    assert derivative(t/2)<0
    assert derivative(t+0.1)>0
   checks+=3
  xc=cross_time(k,q)
  mc=1+(1-q)/q*exp(xc)
  assert xc>0 and mc>1/q
  for M in [1/q+1e-4, (mc+1/q)/2,mc,mc*1.5,mc*10]:
   dg=optimum_gamma(k,q,M)-optimum_fixed(q,M)
   if M<mc-1e-6: assert dg<-1e-8,(k,q,M,mc,dg)
   if M>mc+1e-6: assert dg>1e-8,(k,q,M,mc,dg)
   if M==mc: assert abs(dg)<1e-7,(k,q,mc,dg)
   checks+=1
  # F'''(x)>0 checked at finite points; exact argument in RESULT.
  for x in [0,0.01,0.1,1,4,9]:
   f3=exp(x)-(1-1/k**2)*(1+x/k)**(k-2)
   assert f3>0
   checks+=1

# Benchmark reproducibility (q=1/2,k=1, normalized mean and cost).
q=0.5;k=1
xc=cross_time(k,q)
mc=1+exp(xc)
assert abs(xc-2.8931164309252364)<1e-11
assert abs(mc-19.049471975664964)<1e-10
for M,tg,tf in [(3,(13**0.5-3)/2,log(2)),(20,3.0,log(19))]:
 assert abs(optimum_gamma(k,q,M)-tg)<1e-12
 assert abs(optimum_fixed(q,M)-tf)<1e-12
 checks+=2
print(f'PASS {checks} arithmetic/finite-grid diagnostic checks')
print(f'one-shape, half-occupancy crossover x_c={xc:.13f}, M_c={mc:.13f}')
for M in [3,20]:
 print(f'M={M}, t_gamma={optimum_gamma(1,.5,M):.12f}, t_fixed={optimum_fixed(.5,M):.12f}')

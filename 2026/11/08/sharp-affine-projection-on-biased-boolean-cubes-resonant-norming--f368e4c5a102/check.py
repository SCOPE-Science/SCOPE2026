#!/usr/bin/env python3
"""Exact finite-rational checks for the biased Boolean-cube affine projector.
Run with Python 3.10+: python check.py. This is supplementary verification;
proof of the all-dimension result is mathematical, not computational.
"""
from fractions import Fraction as F
from math import comb, ceil, exp, factorial, sqrt, pi

def probability(d, k, p):
    if k<0 or k>d: return F(0)
    return comb(d,k)*p**k*(1-p)**(d-k)

def formula(d,p):
    p=min(p,1-p)
    t=p*(d-1)
    k= -1
    for j in range(d+1):
        if F(j)<t: k=j
    q=1-p
    return 1+2*(d*q*probability(d-1,k,p)-sum((probability(d,j,p) for j in range(k+1)),F(0)))

def kernel(d,p,x,y):
    return 1+sum((x[i]-p)*(y[i]-p)/(p*(1-p)) for i in range(d))

def value_direct(d,p,x):
    return sum(((p**sum(y)) * ((1-p)**(d-sum(y))) * abs(kernel(d,p,x,y)) for y in __import__('itertools').product((0,1),repeat=d)), F(0))

count=0
for d in range(2,10):
    for p in [F(1,23),F(1,7),F(1,3),F(2,5),F(1,2),F(3,5),F(6,7)]:
        predicted=formula(d,p)
        values=[]
        for r in range(d+1):
            x=(1,)*r+(0,)*(d-r)
            values.append(value_direct(d,p,x))
            count+=1
        assert predicted==max(values),(d,p,predicted,values)
        q=min(p,1-p)
        if q==F(1,2):
            assert all(v==predicted for v in values)
        elif p<F(1,2):
            norming={r for r,v in enumerate(values) if v==predicted}
            expected={d-1,d} if q*(d-1)==int(q*(d-1)) else {d}
            assert norming==expected,(d,p,norming,expected)
        else:
            norming={r for r,v in enumerate(values) if v==predicted}
            expected={0,1} if q*(d-1)==int(q*(d-1)) else {0}
            assert norming==expected,(d,p,norming,expected)
print('EXACT_ALL_VERTEX_KERNEL_NORMS_AND_RESONANT_TIES_OK', count)

# Independently check the convex-order increment identity for values of z;
# no discretized computation is used to prove the all-real-z identity.
for p in [F(1,9),F(1,3),F(2,5)]:
    q=1-p; a=p/q; b=q/p
    for i in range(-100,101):
        z=F(i,30)
        lhs=q*abs(z-1)+p*abs(z+b)-p*abs(z-1)-q*abs(z+a)
        rhs=(2*p*(z+b) if -b<z<-a else
              2*(q-p)*(1-z) if -a<=z<1 else 0)
        assert lhs==rhs,(p,z,lhs,rhs)
print('EXACT_CONVEX_ORDER_INCREMENT_SPOTCHECKS_OK')

# Regime checks: these are numerical corroborations, not proofs of limits.
for lam in [0.5,1.,1.5,2.,3.3,5.]:
    target=2*exp(-lam)*lam**int(lam)/factorial(int(lam))
    d=1500
    # Stable probability sum from Binomial via recurrence in rare region.
    p=lam/d; q=1-p
    k=max(j for j in range(int(lam)+2) if j<p*(d-1))
    probs=[q**d]
    for j in range(1,k+1): probs.append(probs[-1]*(d-j+1)*p/(j*q))
    v=1+2*(sum((d-1-j/p)*probs[j] for j in range(k+1)))
    assert abs(v/d-target)<0.012,(lam,v/d,target)
print('RARE_POISSON_CROSSOVER_SAMPLES_OK')
for p in [0.14,0.37,0.5]:
    d=2000; q=1-p
    # Stable evaluation of absolute moment via PMF centered at binomial mode.
    from math import lgamma, log
    v=0.
    for j in range(d+1):
        if j==0: lg=0.
        lg=lgamma(d+1)-lgamma(j+1)-lgamma(d-j+1)+j*log(p)+(d-j)*log(q)
        if lg>-745: v+=exp(lg)*abs(1-d+j/p)
    target=sqrt(2*q/(pi*p))
    assert abs(v/sqrt(d)-target)<0.04,(p,v/sqrt(d),target)
print('FIXED_BIAS_GAUSSIAN_SAMPLES_OK')
print('ALL_BIASED_AFFINE_PROJECTION_CHECKS_OK')

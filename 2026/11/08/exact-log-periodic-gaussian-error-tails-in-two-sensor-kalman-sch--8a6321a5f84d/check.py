#!/usr/bin/env python3
"""Independent finite-state, stationary-moment, tail and harmonic checks for two-sensor exact-reset filtering."""
from fractions import Fraction as F
from math import log, sqrt, exp, erfc, pi
import cmath
import mpmath as mp

def age_finite(t, e):
    r = 1-e
    states = {(0,1):F(1,2), (1,1):F(1,2)}
    for _ in range(t):
        new = {}
        for (sensor,age),pr in states.items():
            for target,weight in ((sensor,r),(1-sensor,e)):
                age_next = age+1 if sensor==target else 1
                key = (target,age_next)
                new[key] = new.get(key,F(0)) + pr*weight
        states = new
    return {k:sum((v for (i,j),v in states.items() if j==k),F(0)) for k in range(1,t+2)}

def exact_trace(B,q,k):
    return q*(B**k-1)/(B-1)

def gaussian_tail(z,T):
    return erfc(z/sqrt(2*T))

def tail_error(z,B,q,e,limit=90):
    r=1-e
    return sum(e*r**(k-1)*gaussian_tail(z,float(exact_trace(B,q,k))) for k in range(1,limit+1))

def periodic_amp_clean(theta,B,q,e):
    r=1-e; beta=-log(r)/log(B); C=q/(B-1)
    return (C**beta)*(e/r)*sum(B**(beta*(theta-j))*erfc(sqrt(B**(theta-j)/2)) for j in range(-36,64))

checks=0
for e in [F(1,4),F(1,2),F(3,4),F(9,10)]:
    for t in [2,3,6,10]:
        probs=age_finite(t,e);r=1-e
        for k in range(1,t+1):
            assert probs[k]==e*r**(k-1),(e,t,k,probs[k])
            checks+=1
        assert probs[t+1]==r**t
        assert sum(probs.values(),F(0))==1
        checks+=2
for B in [F(4,1),F(9,4)]:
    for q in [F(1,1),F(3,2)]:
        for e in [F(3,4),F(9,10)]:
            if (1-e)*B<1:
                # Exact partial geometric decomposition and its remainder.
                r=1-e; E=q/(1-r*B)
                for n in [3,5,8,12]:
                    S=sum((e*r**(k-1)*exact_trace(B,q,k) for k in range(1,n+1)),F(0))
                    remainder=q/(B-1)*(e*B*(r*B)**n/(1-r*B)-r**n)
                    assert S+remainder==E
                    checks+=1
B=4.0;q=1.5;e=.75;r=1-e;beta=-log(r)/log(B);C=q/(B-1)
for theta in [.13,.48,.81]:
    H=periodic_amp_clean(theta,B,q,e)
    for n in [10,12,15]:
        z=sqrt(C*B**(n+theta))
        ratio=z**(2*beta)*tail_error(z,B,q,e,limit=n+60)
        assert abs(ratio/H-1)<1e-4,(n,theta,ratio,H)
        checks+=1
    assert abs(periodic_amp_clean(theta+1,B,q,e)-H)/H < 1e-10
    checks+=1
# Rigorous analytic expression is Gamma(s+1/2) * 2**s / (sqrt(pi)*s),
# checked numerically against a separate Fourier quadrature.
N=512; c1=0j
for v in range(N):
    theta=v/N
    c1+=periodic_amp_clean(theta,B,q,e)*cmath.exp(-2j*pi*theta)/N
s=beta-2j*pi/log(B)
expected=complex(C**beta*e/(r*log(B))*2**s*mp.gamma(s+.5)/(mp.sqrt(mp.pi)*s))
assert abs(c1-expected)<1e-8,(c1,expected)
assert abs(expected)>1e-8
checks+=2
# Sharp symmetric switching-cost optimizer, including the boundary case.
B=4.0; q=1.5
for lam in [.1, q*B, 3*q*B, 10*q*B]:
    opt=1.0 if lam<=q*B else (B-1+sqrt(q*B/lam))/B
    def cost(eps):
        return q/(B*eps-(B-1))+lam*eps
    for i in range(1,10001):
        eps=(B-1)/B+(1-(B-1)/B)*i/10001
        assert cost(opt) <=cost(eps)+1e-10
        checks+=1
print(f'PASS {checks} independent checks')
print('example B=4, epsilon=0.75, beta=',beta,'Fourier-first=',expected)
print('example B=4, q=1.5, lambda=18: optimal epsilon=',(B-1+sqrt(q*B/18))/B)

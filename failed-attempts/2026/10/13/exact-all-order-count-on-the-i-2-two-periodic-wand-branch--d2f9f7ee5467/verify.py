#!/usr/bin/env python3
from fractions import Fraction
import math


def exact_case(k, r):
    z=sum(r**j for j in range(1,k))
    t=sum(r**(-j) for j in range(1,k))
    lam=(Fraction(2)**k)*r*(r**(k-1)-1)**(k+1)/((r-1)*(r**k-1)**k)
    alpha=lam/(Fraction(2)**k)
    assert z == alpha*(1+1/t)**k
    assert t == alpha*(1+1/z)**k
    return lam,z,t

count=0
for k in range(2,13):
    for r in (Fraction(5,4),Fraction(3,2),Fraction(2,1),Fraction(5,2)):
        exact_case(k,r); count+=1

# Exact special thresholds already treated separately in the source.
def lcrit_frac(k):
    return Fraction(2**k*(k-1)**(k+1), k**k)
assert lcrit_frac(2)==1
assert lcrit_frac(3)==Fraction(128,27)

# Numerically stable logarithm of the hyperbolic parameterization.
def log_sinh(x):
    if x < 20.0:
        return math.log(math.sinh(x))
    return x-math.log(2.0)+math.log1p(-math.exp(-2.0*x))

def log_lam_s(k,s):
    return (k*math.log(2.0)
            +(k+1)*log_sinh((k-1)*s)
            -log_sinh(s)
            -k*log_sinh(k*s))

def lam_s(k,s):
    return math.exp(log_lam_s(k,s))

# Corroborative monotonicity samples for the hyperbolic formula.
for k in range(2,101):
    vals=[log_lam_s(k,s) for s in (0.01,0.03,0.07,0.15,0.3,0.6,1.0)]
    assert all(vals[i]>vals[i+1] for i in range(len(vals)-1))

# Direct positivity samples for H_s''.
for k in range(2,41):
    for s in (0.03,0.2,0.8):
        for u in (1.0,(k+1)/2,k):
            y=u*s
            h2=2*s/(math.sinh(y)**2)*(y/math.tanh(y)-1)
            assert h2>0

# Near-critical coefficient in |log(z/t)|.
worst=0.0
for k in (2,3,4,7,12):
    lc=float(lcrit_frac(k))
    A=math.sqrt(24*k/(lc*(k+1)))
    for s in (2e-4,4e-4,8e-4):
        lam=lam_s(k,s)
        lhs=2*k*s
        rhs=A*math.sqrt(lc-lam)
        rel=abs(lhs/rhs-1)
        worst=max(worst,rel)
        assert rel < 2e-5

print(f'VERIFY_OK exact_cases={count} orders=2..100 onset_worst_rel={worst:.3e}')

"""Reproduce the exact two-step energy identities for the geometric spectral step."""
from fractions import Fraction
from math import sqrt
import random
import sympy as sp

k,r = sp.symbols('k r', positive=True)
a0 = (1+r)/(1+k*r)
a1_sq = (1+r)/(1+k*k*r)
energy0 = (1+r/k)/2
energy1 = ((1-a0)**2 + r*(1-k*a0)**2/k)/2
assert sp.simplify(energy1/energy0 -(k-1)**2*r/((1+k*r)*(k+r))) == 0
# A symbolic expression after the first (exact line-search) step.
b = sp.symbols('b', positive=True)
energy2 = ((1-a0)**2*(1-b)**2 +r*(1-k*a0)**2*(1-k*b)**2/k)/2
ratio = (k-1)**2*r*(k*r*(1-b)**2+(1-k*b)**2)/((1+k*r)**2*(k+r))
assert sp.simplify(energy2/energy0 - ratio)==0
# Positive-coefficient certificate for the final elementary upper bound.
difference = sp.expand((1+k*r)**2*(k+r) - k*(k*r*r+1+r))
certificate = k*k*r**3 + (k**3-k*k+2*k)*r*r+(2*k*k-k+1)*r
assert sp.expand(difference-certificate)==0
# An exact-rational example that erases the initial decrease after two updates.
kv=Fraction(9);rv=Fraction(1,63);a0v=(1+rv)/(1+kv*rv);a1v=Fraction(2,3)
assert a0v==Fraction(8,9)
assert a1v*a1v == (1+rv)/(1+kv*kv*rv)
f0 = Fraction(1,2)*(1+rv/kv)
f1 = Fraction(1,2)*((1-a0v)**2+rv/kv*(1-kv*a0v)**2)
f2 = Fraction(1,2)*((1-a0v)**2*(1-a1v)**2+rv/kv*(1-kv*a0v)**2*(1-kv*a1v)**2)
assert f1/f0==Fraction(7,71)
assert f2/f1==Fraction(197,9)
assert f2/f0==Fraction(1379,639)>1
# Verify numerical identity, bound, and high-condition asymptotics on a deterministic grid.
rng=random.Random(20260804)
for _ in range(5000):
    kk=1+10**rng.uniform(-5,7)
    rr=10**rng.uniform(-11,11)
    seed=(1+rr)/(1+kk*rr)
    adaptive=sqrt((1+rr)/(1+kk*kk*rr))
    e0=(1+rr/kk)/2
    e2=((1-seed)**2*(1-adaptive)**2+rr/kk*(1-kk*seed)**2*(1-kk*adaptive)**2)/2
    fraction=(kk-1)**2*rr*(kk*rr*(1-adaptive)**2+(1-kk*adaptive)**2)/((1+kk*rr)**2*(kk+rr))
    assert abs(e2/e0-fraction)<=1e-8*max(1,e2/e0)
    assert e2/e0<kk*(1+1e-11)
for kk in (10,100,1000,10**5,10**8):
    rr=kk**(-1.5)
    seed=(1+rr)/(1+kk*rr)
    adaptive=sqrt((1+rr)/(1+kk*kk*rr))
    e0=(1+rr/kk)/2
    e2=((1-seed)**2*(1-adaptive)**2+rr/kk*(1-kk*seed)**2*(1-kk*adaptive)**2)/2
    print(f'k={kk}, normalized two-step energy amplification={e2/e0/kk:.12f}')
print('Exact rational sample: F1/F0=7/71, F2/F1=197/9, F2/F0=1379/639.')
print('Symbolic reduction, certificate, rational witness and 5000 deterministic tests: PASS')

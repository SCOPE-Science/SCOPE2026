#!/usr/bin/env python3
"""Independent algebraic and numerical supplementary checks for the two-stage pulse timing claim."""
import math
import random
import sympy as sp

z=sp.symbols('z')
expr=sp.expand(sum(z**i for i in range(5))*(1+z)**4-(1+z+z*z)**4)
factors=z*(z**3-z-1)*(z**3+z*z-1)
assert sp.expand(expr-factors)==0
z0=0.7548776662466927
assert abs(z0**3+z0**2-1)<2e-15
L0=-math.log(z0)
assert abs(L0-.281199574322962)<2e-12

def lag(r,s,L):
    return (math.log(-math.expm1(-s*L))-math.log(-math.expm1(-r*L)))/(s-r)

def deriv(r,s,L):
    return (s/math.expm1(s*L)-r/math.expm1(r*L))/(s-r)

assert lag(1,5,0.01)<lag(2,3,0.01)
assert lag(1,5,1)>lag(2,3,1)
assert abs(lag(1,5,L0)-lag(2,3,L0))<3e-15
rng=random.Random(4492)
checks=0
for _ in range(3000):
    r=10**rng.uniform(-1,0.5)
    s=r+10**rng.uniform(-1,1)
    L=10**rng.uniform(-3,.7)
    tau=lag(r,s,L)
    assert tau>0 and tau<math.log(s/r)/(s-r)
    assert deriv(r,s,L)<0
    h=L*1e-5
    fd=(lag(r,s,L+h)-lag(r,s,max(1e-15,L-h)))/(h+min(h,L-1e-15))
    assert abs(fd-deriv(r,s,L))<max(1e-5,abs(deriv(r,s,L))*0.001)
    checks+=1
for j in range(1,1001):
    L=j/100
    diff=lag(1,5,L)-lag(2,3,L)
    assert (diff<0 if L<L0 else diff>0)
    checks+=1
print('PASS:',checks,'random/ordered checks; exact polynomial factorization; Lc=',L0)

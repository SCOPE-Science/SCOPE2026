"""Finite independent checks for a four-site probabilistic firebreak model.

The analytic proof is in RESULT.md. This program is supplementary, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product
import math
import random


def exact_mean(q):
    """Enumerate all bond configurations and all four equiprobable ignition sites."""
    total = F(0)
    for state in product([0, 1], repeat=3):
        prob = F(1)
        for i, open_ in enumerate(state):
            prob *= q[i] if open_ else 1-q[i]
        if prob == 0:
            continue
        for ignition in range(4):
            left = ignition
            while left > 0 and state[left-1]:
                left -= 1
            right = ignition
            while right < 3 and state[right]:
                right += 1
            total += prob * F(right-left+1,4)
    return total


def pair_mean(q):
    a,b,c = q
    return 1+ F(1,2)*(a+b+c+a*b+b*c+a*b*c)

assert exact_mean((F(0),)*3)==1
assert exact_mean((F(1),)*3)==4
cases=0
for a,b,c in product([F(0),F(1,6),F(1,2),F(5,6),F(1)],repeat=3):
    assert exact_mean((a,b,c)) == pair_mean((a,b,c))
    cases += 1

# Rational witness: p = 1/2, B = log 2.
# All-middle investment gives open edge probabilities (1/2,1/4,1/2).
# Split investment x1=x3=log(9/8), x2=log(128/81).
central=(F(1,2),F(1,4),F(1,2))
split=(F(4,9),F(81,256),F(4,9))
assert exact_mean(central)==F(57,32)
assert exact_mean(split)==F(8177,4608)
assert exact_mean(split)<exact_mean(central)
cases+=4

# At any p in (0,1], the first-order derivative at x=0
# has the sign of (1+p)exp(-B)-1.
# The monotone stationarity cubic has a unique z>1 precisely when exp(B)>1+p.
for p in [F(1,7),F(1,2),F(3,4),F(1)]:
    for v in [F(1), F(11,10), 1+p, F(2),F(10),F(50)]:
        # v = exp(B), e^x = z, solve monotone cubic numerically.
        v = float(v)
        if v < 1: continue
        lo,hi=1.0,max(2.0,v)
        for _ in range(80):
            z=(lo+hi)/2
            if z**3 + float(p)*z**2 > v:
                hi=z
            else:
                lo=z
        if v > 1+float(p)+1e-10:
            z=(lo+hi)/2
            assert z>1
            assert abs(z**3+float(p)*z**2-v) < 1e-8 * max(1,v)
            assert 2*math.log(z)+math.log(z+float(p)) > 0
            assert math.log(z+float(p)) > math.log(z)
        else:
            assert v <= 1+float(p)+1e-10
        cases += 1

rng=random.Random(116007)
for _ in range(2000):
    p=rng.uniform(.00001,1)
    B=rng.uniform(.0001,8)
    def objective(x1,x2,x3):
        return float(pair_mean(tuple(p*math.exp(-x) for x in (x1,x2,x3))))
    if B<=math.log1p(p):
        optimum=(0,B,0)
    else:
        lo,hi=1.0,math.exp(B/3)
        for k in range(65):
            z=(lo+hi)/2
            if z**3 + p*z**2 > math.exp(B):hi=z
            else:lo=z
        z=(lo+hi)/2
        x=math.log(z); y=math.log(z+p)
        assert abs(2*x+y-B)<1e-12
        optimum=(x,y,x)
    val=objective(*optimum)
    for j in range(12):
        u=B*rng.random();v=(B-u)*rng.random();w=B-u-v
        assert val<=objective(u,v,w)+3e-13
        cases+=1
print('PASS',cases,'exact and floating checks; exact witness',exact_mean(central),exact_mean(split))

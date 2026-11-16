"""Exact elementary arithmetic checks for a sharp first-band torus quadrature.

Run with Python 3.10 or later; no third-party dependencies.
The analytic sign-and-support argument is given separately in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import math

# Pairs (a,b) denote a+i*b*sqrt(2), with a,b rational.
def add(x, y):
    return (x[0]+y[0], x[1]+y[1])
def mul(x, y):
    return (x[0]*y[0]-2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def conj(x):
    return (x[0], -x[1])
def power(x, n):
    if n < 0:
        return power(conj(x), -n) # Each node is on the unit circle.
    out=(F(1), F(0))
    for _ in range(n):
        out=mul(out,x)
    return out

a=(F(-1,3),F(2,3))
b=conj(a)
one=(F(1),F(0))
minus_one=(F(-1),F(0))
pts=[(minus_one,minus_one,F(1,4)),
     (a,one,F(3,16)), (b,one,F(3,16)),
     (one,a,F(3,16)), (one,b,F(3,16))]
assert sum(p[2] for p in pts)==F(1)
checks=1

for k,l in product(range(-1,2),repeat=2):
    z=(F(0),F(0))
    for x,y,w in pts:
        q=mul(power(x,k),power(y,l))
        z=add(z,(w*q[0],w*q[1]))
    expected=one if (k,l)==(0,0) else (F(0),F(0))
    assert z==expected, (k,l,z)
    checks+=1

# Verify exact zero-contact algebra for the three equality cosine pairs.
def H(x,y): return x*y+(x+y)/2
for x,y in [(F(-1),F(-1)),(F(-1,3),F(1)),(F(1),F(-1,3))]:
    assert H(x,y)==0
    checks+=1

# On each forbidden rectangle, H is affine in the other coordinate;
# these boundary checks reproduce the two cases in the paper.
for xx in (F(-1), F(-1,2), F(-1,3)):
    assert H(xx,F(-1))<=0
    assert H(xx,F(1))<=0
    checks+=2
for yy in (F(-1), F(-1,2), F(-1,3)):
    assert H(F(-1),yy)<=0
    assert H(F(1),yy)<=0
    checks+=2

# The equality weights are uniquely fixed by constant and first harmonics.
# With b and c the totals on horizontal/vertical two-point pairs:
# -a-b/3+c=0; -a+b-c/3=0; a+b+c=1.
corner=F(1,4); horizontal=F(3,8); vertical=F(3,8)
assert -corner-horizontal/3+vertical==0
assert -corner+horizontal-vertical/3==0
assert corner+horizontal+vertical==1
checks+=3
assert abs(math.acos(-1/3)/(2*math.pi)-0.3040867239846964)<1e-15
checks+=1
print(f"PASS: {checks-1} exact arithmetic checks and 1 numerical display check.")

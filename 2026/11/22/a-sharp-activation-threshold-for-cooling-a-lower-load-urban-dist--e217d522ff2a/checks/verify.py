"""Exact and numerical checks for a two-zone steady cooling allocation theorem.

Run: python3 cooling_verifier.py
Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def eq(a, k, b, h1, h2, y):
    d = (a + b - y) * (a + y) + k * (2*a + b)
    return ((a + y + k)*h1 + k*h2)/d, (k*h1 + (a + b - y + k)*h2)/d


def q_poly(a, k, b, h1, h2, y):
    q = h1 - h2
    d0 = a * (a + b) + k * (2*a + b)
    c = h1 * (a + 2*k) + h2 * (a + b + 2*k)
    return q*y*y + 2*c*y + q*d0-c*b


def objective_derivative(a, k, b, h1, h2, y):
    # Exact symbolic differentiation of rational N(y)/D(y).
    d = (a + b - y) * (a + y) + k * (2*a + b)
    n = h1 * (a + y + 2*k) + h2 * (a + b - y + 2*k)
    return ((h1-h2)*d - n*(b-2*y))/(d*d)


def threshold(a, k, h1, h2):
    h = h2/h1
    if h == 1:
        return 0.
    bb = k+h*(2*a+3*k)
    aa = (1-h)*a*(a+2*k)
    return 2*aa/(bb+sqrt(bb*bb+4*h*aa))


def optimizer(a, k, b, h1, h2):
    if h1 == h2:
        return b/2
    if b <= threshold(a,k,h1,h2):
        return 0.
    q = h1-h2
    d0 = a*(a+b)+k*(2*a+b)
    c = h1*(a+2*k)+h2*(a+b+2*k)
    return (c*b-q*d0)/(sqrt(c*c+q*(c*b-q*d0))+c)  # stable rationalization


checks = 0
# Exact derivative-numerator identity for a grid of rational data.
for ai in (1,2,5):
 for ki in (1,3,7):
  for bi in (1,4,9):
   for hi,lo in ((1,0),(2,1),(3,2),(1,1)):
    a,k,b,h1,h2 = map(F,(ai,ki,bi,hi,lo))
    for numer in range(0,11):
     y=b*F(numer,10)
     d=(a+b-y)*(a+y)+k*(2*a+b)
     assert d>0
     assert objective_derivative(a,k,b,h1,h2,y)*d*d == q_poly(a,k,b,h1,h2,y)
     checks+=2
# Nonzero source-free optimal allocation is certified by rational witnesses.
a=k=F(1);b=F(5);h1=F(1);h2=F(0)
T0=eq(a,k,b,h1,h2,F(0))
Ty=eq(a,k,b,h1,h2,F(1,3))
assert sum(Ty)<sum(T0) and Ty[0]>T0[0]
assert q_poly(a,k,b,h1,h2,F(316,1000))<0
assert q_poly(a,k,b,h1,h2,F(317,1000))>0
assert sum(eq(a,k,F(3),h1,h2,F(0)))==F(1,3)
checks+=5
# Wide parameter sweeps verify exact first-order optimality and boundaries.
rng=Random(20231115)
for _ in range(1500):
 a=10**rng.uniform(-2,2)
 k=10**rng.uniform(-2,2)
 h1=10**rng.uniform(-2,2)
 h2=h1*rng.uniform(0,1)
 b=10**rng.uniform(-2,3)
 yc=optimizer(a,k,b,h1,h2)
 assert 0<=yc<b/2+1e-8
 bc=threshold(a,k,h1,h2)
 assert (yc==0)==(b<=bc)
 if yc>0:
  assert abs(q_poly(a,k,b,h1,h2,yc)) < 1e-7*max(1.,abs(h1*b*(a+b+k)))
  assert sum(eq(a,k,b,h1,h2,yc)) <= sum(eq(a,k,b,h1,h2,0)) + 1e-10
  assert sum(eq(a,k,b,h1,h2,yc)) <= sum(eq(a,k,b,h1,h2,b)) + 1e-10
 for yy in (0., b/4, b/2, 3*b/4, b):
  val=sum(eq(a,k,b,h1,h2,yy))
  bound=sum(eq(a,k,b,h1,h2,yc))
  assert val >= bound-1e-7*max(1.,abs(val))
 checks+=9
# Peak is always hottest zone, and strictly increases with y for source-free district.
for a0 in (F(1),F(2),F(10)):
 for k0 in (F(1),F(3)):
  for b0 in (F(1),F(3),F(10)):
   prev=None
   for j in range(21):
    y=b0*F(j,20)
    t1,t2=eq(a0,k0,b0,F(1),F(0),y)
    assert t1>t2
    if prev is not None: assert t1>prev
    prev=t1
    checks+=2
print('PASS', checks, 'assertion groups; all exact-rational and reproducible numerical checks succeeded')

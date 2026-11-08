"""Exact arithmetic checks for the double-ring Gaussian polynomial peak theorem.

Uses only Python's standard library. The infinite-degree argument is analytic;
these checks replay the rational degree-eleven certificate and degree-twelve
integer example and verify the discriminant and radial polynomial identities.
"""
from fractions import Fraction

def q(n, a, b, u):
    u = Fraction(u)
    r = u**n
    return Fraction(n)*r/(r+a) + Fraction(n)*r/(r+b) - u*u

def p(n, a, b, u):
    u = Fraction(u)
    return u**(2*n) - 2*n*u**(2*n-2) + (a+b)*u**n - n*(a+b)*u**(n-2) + a*b

cases = [Fraction(3),Fraction(7,2),Fraction(37,10),Fraction(79,20),Fraction(81,20)]
expected = [-1,1,-1,1,-1]
for u,sgn in zip(cases,expected):
    v = q(11,50000,4800000,u)
    assert v*sgn>0, (u, v)
    assert (u*u)*p(11,50000,4800000,u)==-(u**11+50000)*(u**11+4800000)*v

for t,sgn in [(0,1),(1,-1),(15,-1),(16,1),(18,-1),(19,1)]:
    val=t**12-24*t**11+33800001*t**6-12*33800001*t**5+33800000
    assert val*sgn>0,(t,val)

# The algebraic discriminant identity at arbitrary integer values.
for n in (3,4,11,12,19):
  for a,b in ((1,2),(50000,4800000),(1,33800000)):
    for t in (0,1,n,2*n,3*n):
      lhs=(n-t)**2*(a+b)**2-4*t*(t-2*n)*a*b
      rhs=(a-b)**2*t*(t-2*n)+n*n*(a+b)**2
      assert lhs==rhs and lhs>0

# For n=12 the two critical points of B_n in (n,2n) are t=16,18.
n=12
B=lambda t: Fraction(t**6*(2*n-t),t-n)
assert B(16)==33554432 and B(18)==34012224
assert B(16)<33800000<B(18)
print('TWO_RING_MAXIMA_CERTIFICATE_PASS rational_signs=5 integer_signs=6 discriminants=75 B_12_bounds=2')

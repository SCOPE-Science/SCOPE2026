"""Exact algebra and finite diagnostics for the sharp quadratic Hardy-Hankel kernel-testing bound.

Run with Python 3 standard library: python3 check_quadratic_hankel.py
The analytic proof, not this finite test, establishes the all-coefficient theorem.
"""
from fractions import Fraction as F
from math import sqrt
import cmath

checks = 0
# For 0 <= t <= 1, f(t)-25/27=(8-3t)(3t-2)^2/432.
for k in range(1001):
    t = F(k, 1000)
    f = (1-t/4)*(1+t*t/4)
    assert f-F(25,27) == (8-3*t)*(3*t-2)**2/432
    assert f >= F(25,27)
    checks += 2
assert (1-F(2,3)/4)*(1+F(2,3)**2/4) == F(25,27)
checks += 1

# Kernel norm is computed from the genuine 2x2 Hankel matrix, not a
# pre-tabulated scalar approximation. Compare all phases in small grids.
def k_norm_sq(a,b,w):
    r2=abs(w)**2
    v0=(1-r2)**.5
    v1=v0*w.conjugate()
    y0=a.conjugate()*v0+b.conjugate()*v1
    y1=b.conjugate()*v0
    return abs(y0)**2+abs(y1)**2

for a in [0j,1+0j,2+3j,-3j]:
 for b in [0j,1j,-1+0j,2-1j]:
  if a == b == 0: continue
  A,B=abs(a),abs(b)
  norm=(A+sqrt(A*A+4*B*B))/2
  u=B/norm
  for r in [0.,.2,.4,.7,.9]:
   for theta in [0.,.25,1.1,2.7]:
    w=r*cmath.exp(1j*theta)
    val=k_norm_sq(a,b,w)
    assert abs(val-(1-r*r)*(abs(a.conjugate()+b.conjugate()*w.conjugate())**2+B**2))<1e-10
    assert val <= norm*norm*(1+1e-10)
    checks += 2
  # Phases can be aligned, and the explicit witness r=u/2 gives a uniform bound.
  w=u/2 * cmath.exp(1j*(cmath.phase(a)-cmath.phase(b))) if A*B else u/2
  witness=k_norm_sq(a,b,w)
  assert witness + 1e-9 >= norm*norm*25/27
  checks += 1

# The extremal symbol psi=z+sqrt(6)z^2 has Hankel norm 3.
a,b=1.,sqrt(6)
r=1/sqrt(6)
norm=(a+sqrt(a*a+4*b*b))/2
assert abs(norm-3.)<1e-13
assert abs(k_norm_sq(complex(a),complex(b),complex(r))-25/3)<1e-12
assert abs(norm/sqrt(k_norm_sq(complex(a),complex(b),complex(r)))-3*sqrt(3)/5)<1e-12
checks+=3
print('QUADRATIC_HANKEL_CHECK_OK',checks)

"""Standalone symbolic checks for a two-band spherical Fourier-extension profile.

Requires Python 3 and sympy. This script verifies exact finite polynomial and
integration identities used in the accompanying analytic proof. Its finite
numerical spot checks are not substitutes for the analytic inequalities.
"""
import sympy as S

r, t = S.symbols('r t', real=True)
q = {0: S.Rational(1, 2), 2: (1 - 3*t**2)/4}

def pair(a, b):
    return S.factor(S.integrate(q[a] * q[b].subs(t, r-t), (t, r-1, 1)))

H00 = pair(0, 0)
H02 = pair(0, 2)
H22 = pair(2, 2)
assert S.simplify(H00 - (2-r)/4) == 0
assert S.factor(H02 - r*(r-2)*(r-1)/8) == 0
assert S.factor(H22 + (r-2)*(3*r**4+6*r**3-8*r**2-16*r+8)/160) == 0

def radial(a, b):
    return S.factor(2*S.integrate(S.diff(a,r)*S.diff(b,r), (r,0,2)))

assert radial(H00,H00) == S.Rational(1,4)
assert radial(H00,H22) == S.Rational(1,20)
assert radial(H02,H22) == -S.Rational(1,28)
assert radial(H22,H22) == S.Rational(11,140)

# Exact spherical monomial expectation on S^2 in coordinate eigenaxes.
x,y,z = S.symbols('x y z', real=True)
def sphere_moment(expr):
    total = 0
    poly = S.Poly(S.expand(expr),x,y,z)
    for (i,j,k), coeff in poly.terms():
        if i%2 or j%2 or k%2:
            continue
        a,b,c = i//2,j//2,k//2
        total += coeff*S.rf(S.Rational(1,2),a)*S.rf(S.Rational(1,2),b)*S.rf(S.Rational(1,2),c)/S.rf(S.Rational(3,2),a+b+c)
    return S.factor(total)

A,B = S.symbols('A B',real=True)
U = A*x*x + B*y*y - (A+B)*z*z
tr2 = A*A+B*B+(A+B)**2
assert S.simplify(sphere_moment(U**2)-S.Rational(2,15)*tr2)==0
assert S.simplify(sphere_moment(U**4)-S.Rational(4,105)*tr2**2)==0
# With unit quadratic norm, fourth moment is 15/7.
assert S.simplify((S.Rational(4,105)*tr2**2)/(S.Rational(2,15)*tr2)**2 - S.Rational(15,7)) == 0

Y = S.sqrt(5)/2*(3*z*z-1)
assert sphere_moment(Y**2)==1
assert S.simplify(sphere_moment(Y**3)-2*S.sqrt(5)/7)==0
assert sphere_moment(Y**4)==S.Rational(15,7)

# For symmetric traceless 3x3 A, norm of the quadratic projection of U^2.
trA4 = A**4 + B**4 + (A+B)**4
assert S.factor(trA4-tr2**2/2)==0
proj_tr2 = S.factor(trA4-tr2**2/3)
proj_norm_sq = (S.Rational(4,7)**2)*S.Rational(2,15)*proj_tr2
assert S.simplify(proj_norm_sq/(S.Rational(2,15)*tr2)**2 - S.Rational(20,49)) == 0

# Exact quartic profile for normalized optimal zonal data.
a,s = S.symbols('a s', real=True, nonnegative=True)
normalized_quartic = a**4 + S.Rational(6,5)*a**2*s**2 + (4*a/7)*(2*S.sqrt(5)/7)*s**3 + S.Rational(11,35)*S.Rational(15,7)*s**4
claimed = a**4+S.Rational(6,5)*a*a*s*s+8*S.sqrt(5)/49*a*s**3+S.Rational(33,49)*s**4
assert S.simplify(normalized_quartic-claimed)==0
print('PASS: four radial integrals, spherical quadratic identities, cubic saturation, and exact quartic profile')

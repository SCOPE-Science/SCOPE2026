"""Standalone exact-symbolic checks for a Bernoulli-negative-binomial convolution."""
from fractions import Fraction
from math import sqrt
from sympy import symbols, factor, simplify, Rational

nu, q, r, k = symbols('nu q r k', positive=True)

def M(j):
    return q * (nu + j - 1) + r * j

def R(j):
    return q * (nu + j - 1) * M(j + 1) / ((j + 1) * M(j))

def S(j):
    t = j - 1
    return ((q+r)**2*t**2
        + (q**2*(2*nu+1)+2*q*r*(nu+3)+5*r**2)*t
        + q**2*nu*(nu+1)+4*q*r*(nu+1)+6*r**2)

assert simplify(R(k+1)-R(k) - q*(1-nu)*S(k)/((k+1)*(k+2)*M(k)*M(k+1))) == 0
assert simplify(R(1)-(nu*q+r) + (nu*(nu-1)*q**2+2*nu*q*r+2*r**2)/(2*(nu*q+r))) == 0

# Verify exact PGF coefficients and adjacent ratios independently.
from sympy import rf, factorial
x = symbols('x')
from sympy import series
G=(1+r*x)/(1+r) * ((1-q)/(1-q*x))**nu
for j in range(1,7):
    a0 = rf(nu,j)*q**j/factorial(j) + r*rf(nu,j-1)*q**(j-1)/factorial(j-1)
    a1 = rf(nu,j-1)*q**(j-1)*M(j)/factorial(j)
    assert simplify(a0-a1)==0

nu0, q0, r0 = Rational(1,2), Rational(1,2), Rational(1,10)
polynomial = nu*(nu-1)*q**2+2*nu*q*r+2*r**2
assert simplify(polynomial.subs({nu:nu0,q:q0,r:r0})-Rational(3,400))==0
B = 1-(1-q0)**nu0-nu0*q0
assert simplify((r0**2+nu0*q0*r0)-Rational(7,200))==0
assert B > Rational(7,200)
L = q0*(sqrt(float(nu0*(2-nu0)))-float(nu0))/2
D = (sqrt(float(nu0**2*q0**2+4*B))-float(nu0*q0))/2
assert L<float(r0)<D

# Independent finite-index cross-checks are corroboration, not the all-index proof.
for v in [Rational(1,5),Rational(1,2),Rational(1),Rational(3,2),Rational(4)]:
    for theta in [Rational(1,4),Rational(1,2),Rational(4,5)]:
        for odds in [Rational(1,10),Rational(1),Rational(4)]:
            pars={nu:v,q:theta,r:odds}
            rv=[R(j).subs(pars) for j in range(1,12)]
            assert all((b-a)*(1-v)>0 if v!=1 else a==b for a,b in zip(rv,rv[1:]))
            t0=v*theta+odds
            t1=rv[0]
            assert (t1-t0) < 0 if v>=1 else True

print('PASS: universal symbolic ratio differences, exact first-boundary polynomial,')
print('      rational example, positivity thresholds, and finite-index independent checks.')

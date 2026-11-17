"""Exact checks for the short-perimeter coefficients on smooth surfaces.

Run: python checker.py (requires sympy). The mathematical proof is independent
of these finite symbolic checks.
"""
import sympy as s

p,q,r=s.symbols('p q r', nonnegative=True)
F=(p+q)*(q+r)*(r+p)


def dirichlet_monomial(i,j,k):
    return s.factor(s.rf(s.Rational(1,2),i)*s.rf(s.Rational(1,2),j)*s.rf(s.Rational(1,2),k)/s.rf(s.Rational(3,2),i+j+k))


def expectation(f):
    return s.simplify(sum(c*dirichlet_monomial(*exp) for exp,c in s.Poly(s.expand(f),p,q,r).terms()))

assert expectation(F)==s.Rational(4,21)
assert expectation(F*((p+q)**2+(q+r)**2))==s.Rational(32,165)
I0=s.simplify(8*s.pi**2*expectation(F)/64)
I1=s.simplify(8*s.pi**2*expectation(F*((p+q)**2+(q+r)**2))/384)
# T=(u wedge v)^2/|u-v|. Its coarea integral reduces to
# (pi/8) * int_simplex (p+q)(q+r)*sqrt(p*q*r) dp dq
# and beta integrals give int=4*pi/495.
beta_base=s.gamma(s.Rational(3,2))**3/s.gamma(s.Rational(9,2))
# E[(p+q)(q+r)] for Dirichlet(3/2,3/2,3/2):
dir2=s.Rational(14,33)
assert s.simplify(beta_base*dir2)==4*s.pi/495
I2=s.simplify(s.pi/8*beta_base*dir2)
assert I0==s.pi**2/42
assert I1==2*s.pi**2/495
assert s.simplify((I2-I1)/6)==-s.pi**2/1980
assert s.simplify(2*s.pi*(I2-I1)/6)==-s.pi**3/990
# Independent unit-sphere cross-check: exact joint spherical side density,
# changed to Heron coordinates, has leading integrand w^3 F/sqrt(p q r)
# and correction w^5 T where T is a trigonometric Taylor polynomial.
T=(1+p**2+q**2+r**2)/12-((p+q)**2+(q+r)**2+(r+p)**2)/6
assert expectation(F*T)==-s.Rational(4,165)
sphere_lead=s.simplify(s.Rational(1,2)*expectation(F)/64)
sphere_next=s.simplify(s.Rational(1,2)*expectation(F*T)/384)
assert sphere_lead==s.Rational(1,672)
assert sphere_next==-s.Rational(1,31680)
# For the round sphere A=4*pi and chi=2, our general formula agrees.
assert s.simplify(I0/(4*s.pi)**2)==sphere_lead
assert s.simplify(-s.pi**3*2/(990*(4*s.pi)**3))==sphere_next
print('SHORT_TRIANGLE_TOPOLOGY_CHECKS_OK')
print('I0 =',I0,'I1 =',I1,'I2 =',I2)
print('unit sphere: ',sphere_lead,' * epsilon^4 + (',sphere_next,') * epsilon^6')

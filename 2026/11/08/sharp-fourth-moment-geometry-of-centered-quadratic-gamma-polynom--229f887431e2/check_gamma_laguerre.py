#!/usr/bin/env python3
"""Exact rational and symbolic checks of sharp two-mode gamma Laguerre fourth moments.

Requires Python 3 and SymPy. Optional numerical quadrature uses mpmath.
"""
from fractions import Fraction
import sympy as S

x, k, t = S.symbols('x k t', real=True)
P1 = x - k
P2 = x**2 - 2*(k+1)*x + k*(k+1)

def gamma_moment(p):
    ans = 0
    for (j,), c in S.Poly(S.expand(p), x).terms():
        ans += c*S.rf(k,j)
    return S.factor(ans)

B = (k+2 + 16*(k+1)*t + (20*k**2+116*k+96)*t**2
     + (128*k**2+448*k+320)*t**3
     + (20*k**3+296*k**2+772*k+496)*t**4)
M2 = k*(1+2*(k+1)*t**2)
M4 = 3*k*B
assert S.simplify(gamma_moment((P1+t*P2)**2) - M2) == 0
assert S.simplify(gamma_moment((P1+t*P2)**4) - M4) == 0
assert S.simplify(gamma_moment(P1*P2)) == 0
print('EXACT_GAMMA_MOMENTS_AND_ORTHOGONALITY_OK')

K = S.factor(M4/M2**2)
Q = ((16*k**2+56*k+40)*t**4 - (40*k+100)*t**3
     - (18*k+54)*t**2 - (2*k+11)*t - 1)
K_deriv = -48*(k+1)*Q/(k*(1+2*(k+1)*t**2)**3)
assert S.factor(S.diff(K,t) - K_deriv) == 0
print('EXACT_QUARTIC_STATIONARY_EQUATION_OK')

q = 4*k**4-10*k**3-62*k**2+168*k+441
sos = (2*k**2-S.Rational(5,2)*k-21)**2+S.Rational(63,4)*k**2+63*k
assert S.factor(q-sos)==0
assert S.factor(S.discriminant(Q,t) + 6912*(k+2)**2*(2*k+5)**2*q)==0
print('EXACT_NEGATIVE_DISCRIMINANT_POSITIVITY_CERTIFICATE_OK')

assert S.factor(K.subs(t,0)-3*(k+2)/k)==0
Kinf = S.limit(K,t,S.oo)
assert S.factor(Kinf-3*(20*k**3+296*k**2+772*k+496)/(4*k*(k+1)**2))==0
s = S.symbols('s',real=True)
assert S.simplify(S.diff((M4.subs(t,1/s)/(M2.subs(t,1/s)**2)).cancel(),s).subs(s,0) -
  3*(128*k**2+448*k+320)/(4*k*(k+1)**2)) == 0
print('PROJECTIVE_BOUNDARY_NONSTATIONARITY_OK')

# Each rational example uses raw gamma moments, independently of endpoint root finding.
for ka in [S.Rational(1,10),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(5),S.Integer(10),S.Integer(100)]:
    for ta in [S.Rational(-5,2),S.Rational(-1,2),S.Rational(-1,6),S.Integer(0),S.Rational(1,10),S.Rational(1,2),S.Integer(3)]:
        direct = gamma_moment((P1+t*P2)**4).subs({k:ka,t:ta})/gamma_moment((P1+t*P2)**2).subs({k:ka,t:ta})**2
        formula = K.subs({k:ka,t:ta})
        assert direct==formula
print('RATIONAL_GAMMA_MOMENT_CASES_OK 49')

# Analytically deduced uniqueness is also corroborated with 6 independent
# fixed rational parameter specializations, not used as a universal proof.
for ka in [S.Rational(1,10),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(10),S.Integer(100)]:
    roots = S.nroots(Q.subs(k,ka), maxsteps=200)
    rr=sorted(float(S.re(r)) for r in roots if abs(float(S.im(r)))<1e-8)
    assert len(rr)==2 and rr[0]<0<rr[1]
    lo=float(K.subs({k:ka,t:rr[0]})); hi=float(K.subs({k:ka,t:rr[1]}))
    for sample in [-50,-5,-1,-0.3,-0.01,0,0.01,0.3,1,5,50]:
        val=float(K.subs({k:ka,t:sample}))
        assert lo-1e-8<=val<=hi+1e-8
assert S.factor(Q.subs({k:2,t:-S.Rational(1,6)}))==0
assert S.factor(K.subs({k:2,t:-S.Rational(1,6)})-S.Rational(15,7))==0
print('ROOT_ISOLATION_AND_EXACT_SHAPE_TWO_WITNESS_OK')

# Gaussian limit: centered and normalized first two Laguerre modes
# converge in eighth-moment polynomial data to Z and (Z^2-1)/sqrt(2).
A,C,z = S.symbols('A C z', real=True)
U = z
V = (z*z-1)/S.sqrt(2)
poly = S.Poly(S.expand((A*U+C*V)**4),z)
limit4 = sum(cc*(S.factorial2(j-1) if j else 1) for (j,),cc in poly.terms() if j%2==0)
assert S.simplify(limit4-(3*A**4+30*A**2*C**2+15*C**4))==0
print('GAUSSIAN_LIMIT_MOMENT_GEOMETRY_OK')
# Independent quadrature uses the density directly, rather than moments.
try:
    import mpmath as mp
    mp.mp.dps=35
    for shape, coeff in [(1,-0.20),(2,-1/6),(5,0.4)]:
        ka, ta = mp.mpf(shape), mp.mpf(str(coeff))
        def density(z): return z**(ka-1)*mp.exp(-z)/mp.gamma(ka)
        def f(z): return z-ka + ta*(z*z-2*(ka+1)*z+ka*(ka+1))
        m2 = mp.quad(lambda z:f(z)**2*density(z), [0,1,5,20,mp.inf])
        m4 = mp.quad(lambda z:f(z)**4*density(z), [0,1,5,20,mp.inf])
        a = m4/m2**2
        b = mp.mpf(str(S.N(K.subs({k:S.Rational(shape),t:S.Rational(str(coeff))}),32)))
        assert abs(a-b)<mp.mpf('1e-23')
    print('DIRECT_GAMMA_DENSITY_QUADRATURE_OK 3')
except ImportError:
    print('DIRECT_GAMMA_DENSITY_QUADRATURE_SKIPPED_OPTIONAL_DEPENDENCY')
print('ALL_TWO_MODE_GAMMA_LAGUERRE_EXACT_CHECKS_PASSED')

"""Exact finite algebra checks for a quadratic-tilt beta density.

The global assertion rests on the endpoint and polynomial proof in RESULT.md;
these finite symbolic/rational checks are supporting reproducibility checks only.
"""
import sympy as s

x,a,b,r,d = s.symbols('x a b r d', positive=True)
Z=1+r-2*d*a/(a+b)+d*d*a*(a+1)/((a+b)*(a+b+1))
Q=r+(1-d*x)**2
# Exact normalization from beta moments.
m1=a/(a+b)
m2=a*(a+1)/((a+b)*(a+b+1))
assert s.simplify((1+r)-2*d*m1+d*d*m2-Z)==0
# Endpoint factor case and beta-function ratio.
assert s.expand(Q.subs({r:0,d:1})-(1-x)**2)==0
assert s.simplify(Z.subs({r:0,d:1})-b*(b+1)/((a+b)*(a+b+1)))==0
# Delta zero eliminates rho exactly.
assert s.simplify((Q/Z).subs(d,0)-1)==0
# Recover the deformation parameters from normalized polynomial coefficients.
B=-2*d/(1+r)
C=d*d/(1+r)
assert s.simplify(-2*C/B-d)==0
assert s.simplify(4*C/B**2-1-r)==0
# The alpha, beta, delta score functions on the delta=0 surface.
mu=a/(a+b)
score_delta=s.simplify(s.diff(s.log(Q)-s.log(Z),d).subs(d,0))
assert s.simplify(score_delta+2*(x-mu)/(1+r))==0
assert s.simplify(s.diff(s.log(Q)-s.log(Z),r).subs(d,0))==0
# All rational demonstration pairs show exact equality as unnormalized PDFs.
for A,BB in [(s.Rational(2),s.Rational(1)),(s.Rational(3,2),s.Rational(7,3)),(s.Rational(6),s.Rational(4))]:
    zz=s.simplify(Z.subs({a:A,b:BB,r:0,d:1}))
    ratio=s.simplify((1-x)**2/zz/s.beta(A,BB))
    target=1/s.beta(A,BB+2)*(1-x)**2
    assert s.simplify(s.expand_func(ratio-target))==0
# Numeric component checks for two analytically identical distributions.
for xx in [s.Rational(1,10),s.Rational(1,3),s.Rational(7,10)]:
    A,BB=s.Rational(2),s.Rational(1)
    lhs=s.simplify(((1-xx)**2/Z.subs({a:A,b:BB,r:0,d:1}))*xx**(A-1)*(1-xx)**(BB-1)/s.beta(A,BB))
    rhs=s.simplify(xx**(A-1)*(1-xx)**(BB+1)/s.beta(A,BB+2))
    assert lhs==rhs
print('PASS: exact symbolic normalization, endpoint reparameterization, recovery identities, zero-tilt scores; exact rational demonstrations.')

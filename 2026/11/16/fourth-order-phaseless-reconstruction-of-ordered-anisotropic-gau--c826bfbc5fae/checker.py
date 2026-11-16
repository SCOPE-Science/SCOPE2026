"""Reproducible exact symbolic checks for Gaussian two-packet intensity jets.

Requires Python 3 and SymPy. These finite checks accompany, but do not
replace, the polynomial factorization and rank proof in RESULT.md.
"""
import sympy as sp

x,y,z,t=sp.symbols('x y z t',real=True)
Rt=sp.sqrt
# For covariance forms S,Q and a linear separation H, intensity at t*xi is
# 2 exp(-t^2 S)(cosh(t^2 Q)+cos(t H)).
S=3*x*x+4*y*y+5*z*z+x*y
Q=2*x*x+3*y*y+4*z*z+x*y
H=x+2*y-3*z
I=2*sp.exp(-t*t*S)*(sp.cosh(t*t*Q)+sp.cos(t*H))
# Truncated logarithm evaluated formally through order four.
L=sp.series(sp.log(I/4),t,0,6).removeO().expand()
assert sp.simplify(L.coeff(t,2)+S+H**2/4)==0
assert sp.simplify(L.coeff(t,4)-Q**2/4+H**4/96)==0
print('OK: second and fourth logarithmic Fourier jets')

# A pair of distinct, strictly Loewner-ordered, planar Gaussian mixtures
# having exactly equal intensity jets through fourth order.
c=1/(2*sp.sqrt(6))
Q1=x*x+y*y
R1=sp.Rational(3,5)*x*x
Q2=sp.Rational(4,5)*x*x+sp.Rational(5,4)*y*y
R2=sp.Rational(3,4)*y*y
assert sp.factor(Q1**2-R1**2-(Q2**2-R2**2))==0
H1_sq=sp.simplify(R1/c)
H2_sq=sp.simplify(R2/c)
S1=10*(x*x+y*y)
S2=sp.expand(S1+(H1_sq-H2_sq)/4)
assert sp.simplify(S1+H1_sq/4-S2-H2_sq/4)==0
assert sp.simplify(Q1-Q2)!=0
# All four covariance matrices S_i +/- Q_i are positive definite:
for P in (S1+Q1,S1-Q1,S2+Q2,S2-Q2):
    assert sp.simplify(sp.diff(P,x,2)/2)>0
    assert sp.simplify(sp.diff(P,y,2)/2)>0
print('OK: exact noncongruent planar counterexample; all covariances positive')

# Original d=3 example: irreducible quadratic factors with one potentially
# indefinite factor; exact product and rank-one difference.
Q3=2*x*x+3*y*y+5*z*z
R3=sp.Rational(1,2)*(x+y+z)**2
U=sp.expand(Q3+R3)
V=sp.expand(Q3-R3)
assert sp.expand(U*V-Q3**2+R3**2)==0
assert sp.factor(U)==U or sp.simplify(sp.factor(U)-U)==0
for F in (U,V):
    Hess=sp.hessian(F,(x,y,z))/2
    assert Hess.det()!=0
assert sp.hessian(U-V,(x,y,z)).rank()==1
print('OK: three-dimensional factor-and-rank identities')

# Minimal order: same zeroth/second jets, different fourth jets.
base=5*(x*x+y*y+z*z)
assert sp.simplify((x*x+y*y+z*z)**2-(2*x*x+2*y*y+2*z*z)**2)!=0
for q in (x*x+y*y+z*z,2*(x*x+y*y+z*z)):
    assert (sp.hessian(base+q,(x,y,z))/2).is_positive_definite
    assert (sp.hessian(base-q,(x,y,z))/2).is_positive_definite
print('OK: fourth-order necessity within strictly ordered covariance pairs')

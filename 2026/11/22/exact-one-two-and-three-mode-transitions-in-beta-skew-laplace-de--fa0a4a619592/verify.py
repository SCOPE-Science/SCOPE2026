#!/usr/bin/env python3
"""Exact algebra and supplementary numerical checkpoints for a beta-skew-Laplace mode diagram.

Requires SymPy; the analytic all-parameter proof is in RESULT.md.
"""
import sympy as sp

z,x,b=sp.symbols('z x b', positive=True)
N_R=(1-z)**2+1
N_L=(1+z)**2+1
Q_R=(1-b*x**3)**2+1
Q_L=(1+b*x**3)**2+1

# The two normalized positive-halfline contributions total one.
I_R=sp.integrate(sp.expand(Q_R)*sp.exp(-x),(x,0,sp.oo))
I_L=sp.integrate(sp.expand(Q_L)*sp.exp(-x),(x,0,sp.oo))
assert sp.simplify(I_R+I_L-4*(1+360*b**2))==0

# Slope change on each side, with z=b*x^3 and c=b^(1/3):
#  g'(x)/exp(-x) = 6 c z^(2/3) (z-eps) - ((z-eps)^2+1).
for eps,N in ((1,N_R),(-1,N_L)):
    H=N/(6*z**sp.Rational(2,3)*(z-eps))
    P=sp.factor(3*z*(z-eps)*sp.diff(N,z)-N*(5*z-2*eps))
    assert sp.expand(P)==z**3-8*z+4*eps
    assert sp.simplify(sp.diff(H,z)/H-P/(3*z*(z-eps)*N))==0
    Q=(1-eps*b*x**3)**2+1
    derivative_part=sp.expand(sp.diff(Q,x)-Q)
    check=6*b*x**2*(b*x**3-eps)-Q
    assert sp.simplify(derivative_part-check)==0

# The root intervals are certified by exact rational signs.
P_R=z**3-8*z+4
P_L=z**3-8*z-4
assert P_R.subs(z,sp.Rational(5,2))<0<P_R.subs(z,sp.Rational(13,5))
assert P_L.subs(z,sp.Integer(3))<0<P_L.subs(z,sp.Rational(31,10))
assert sp.simplify(N_R*(z+1)-N_L*(z-1)-(4-2*z**2))==0

# At any fixed z>1, compare H_R and H_L; it is negative for z>sqrt(2).
assert sp.simplify(N_R/(z-1)-N_L/(z+1)-(4-2*z**2)/(z**2-1))==0

# The limiting two-mode density is normalized.
assert sp.integrate(x**6*sp.exp(-x)/1440,(x,0,sp.oo))*2==1
assert sp.solve(sp.diff(x**6*sp.exp(-x),x),x)==[6]

# Numerical values are printed only as reproducibility aids; they do not
# prove uniqueness of the stationary points or the global phase diagram.
Rroot=sp.nsolve(P_R,sp.Rational(5,2),tol=sp.Float('1e-35'),prec=55)
Lroot=sp.nsolve(P_L,sp.Integer(3),tol=sp.Float('1e-35'),prec=55)
B_R=((N_R/(6*z**sp.Rational(2,3)*(z-1)))**3).subs(z,Rroot)
B_L=((N_L/(6*z**sp.Rational(2,3)*(z+1)))**3).subs(z,Lroot)
assert 0<B_R<sp.Rational(1,100)<B_L<sp.Rational(1,20)
print('right root:',sp.N(Rroot,17),'right onset:',sp.N(B_R,17))
print('left root: ',sp.N(Lroot,17),'left onset: ',sp.N(B_L,17))
print('PASS: normalization, derivative identities, exact cubic signs, threshold ordering identity, limiting density, and numerical brackets')

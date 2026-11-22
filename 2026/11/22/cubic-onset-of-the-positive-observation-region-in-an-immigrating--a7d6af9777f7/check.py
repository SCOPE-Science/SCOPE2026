"""Reproducibility checks for the positive-output fold and area formula.

Uses exact SymPy identities and numerical quadrature. Numerical tests are
consistency diagnostics; the proof is given separately.
"""
from math import isclose, sqrt
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

u, t, r, a, b, eps, X, Y = sp.symbols('u t r a b eps X Y', positive=True)
q = 2*t - 1
R = 2*q*u+(5-1/t)*u**2+2*u**3/t
Xfold = eps-r*R
Yfold = r*b*(q+2*u)*u**2/(a*t)
P = 2*q**2*u**3/sp.Integer(3)+q*(7-1/t)*u**4/sp.Integer(2)+(sp.Rational(32,5)-2/t)*u**5+2*u**6/t
assert sp.simplify(sp.diff(P,u) - (q+2*u)*u**2*sp.diff(R,u)) == 0
assert sp.simplify(sp.diff(Xfold,u)+r*sp.diff(R,u)) == 0
H=eps-r*q*u-r*u**2-a*(t+u)*Y/(b*u)
assert sp.simplify(sp.diff(H,u).subs(Y,Yfold)) == 0
assert sp.simplify(H.subs(Y,Yfold)-Xfold)==0
# Jacobian of the original mapping in positive coordinates x=t+u.
y=sp.symbols('y', positive=True)
xx=t+u
Fx=r*xx*(1-xx)-a*xx*y+r*t*(t-1)+eps
Fy=b*u*y
J=sp.det(sp.Matrix([[sp.diff(Fx,u),sp.diff(Fx,y)], [sp.diff(Fy,u),sp.diff(Fy,y)]]))
assert sp.simplify(J - (r*b*(1-2*xx)*u + a*b*t*y)) == 0
assert sp.simplify(J.subs(y, Yfold/(b*u))) == 0
assert sp.simplify(sp.limit(r**2*b*P / (a*t*(r*R)**3),u,0) - b/(12*a*t*r*q)) == 0

# A direct inverse test with rational parameter values and an independent
# numerical integration along the target-X axis.
for e in [0.25, 0.05, 0.01]:
    tt,rr,aa,bb=2.,1.,2.,1.
    Q=2*tt-1
    def Rnum(z): return 2*Q*z+(5-1/tt)*z*z+2*z**3/tt
    def Xf(z): return e-rr*Rnum(z)
    def Yf(z): return rr*bb*(Q+2*z)*z*z/(aa*tt)
    def inv_u(target): return brentq(lambda z:Xf(z)-target,0.,1.)
    root=inv_u(0.)
    poly=float((r**2*b*P/(a*t)).subs({t:tt,r:rr,a:aa,b:bb,u:root}))
    integral=quad(lambda target: Yf(inv_u(target)),0,e,epsabs=1e-13)[0]
    assert isclose(poly,integral,rel_tol=2e-7,abs_tol=1e-12),(poly,integral)
    asy=bb*e**3/(12*aa*tt*rr*Q)
    assert 0.75 < poly/asy <= 1.
    # Every interior target has two positive ancestors, fold has one.
    xf=e/2
    ymax=Yf(inv_u(xf))
    def HH(z,yyy): return e-rr*Q*z-rr*z*z-aa*(tt+z)*yyy/(bb*z)
    from scipy.optimize import minimize_scalar
    for frac in [0.2,0.75]:
        yy=frac*ymax
        umax=minimize_scalar(lambda z:-HH(z,yy),bounds=(1e-12,1.0),method='bounded').x
        assert HH(umax,yy)>xf
        left=brentq(lambda z:HH(z,yy)-xf,1e-12,umax)
        right=brentq(lambda z:HH(z,yy)-xf,umax,1.0)
        for z in [left,right]:
            y0=yy/(bb*z)
            assert z>0 and y0>0
            assert isclose(float(Fx.subs({t:tt,r:rr,a:aa,u:z,y:y0,eps:e})),xf,rel_tol=2e-9,abs_tol=1e-10)
            assert isclose(bb*z*y0,yy,rel_tol=2e-9,abs_tol=1e-10)
    print('epsilon',e,'exact-area',format(poly,'.15g'), 'quadrature', format(integral,'.15g'), 'cubic-ratio',format(poly/asy,'.12g'))
print('All symbolic identities and numerical diagnostics passed.')

"""Standalone executable symbolic checks and finite examples for the stated sine-flow formulae.

Run with: python check.py  (requires sympy and scipy).
Finite samples are diagnostics, not a substitute for the analytic proof.
"""
import math
import sympy as S
from scipy.optimize import brentq

x,b,k,g,R,theta=S.symbols('x b k g R theta', positive=True, real=True)
sinc=S.sin(x)/x
phi=g*x**2+k*b**2*sinc**2
expansion=S.series(phi,x,0,8).removeO()
expected=k*b**2+(g-k*b**2/3)*x**2+2*k*b**2*x**4/45-k*b**2*x**6/315
assert S.simplify(expansion-expected)==0

x_of_theta=R/S.sqrt(g)*S.cos(theta)
F=b*S.sqrt(g*k)*S.sin(x_of_theta)+R**2*S.cos(theta)*S.sin(theta)
assert S.simplify(S.diff(F,theta).subs(theta,3*S.pi/2)-R*(b*S.sqrt(k)-R))==0
assert S.simplify(S.diff(F,theta).subs(theta,S.pi/2)+R*(b*S.sqrt(k)+R))==0

# At an off-axis root, z_R=-b*sinc; verify the coordinate slope identity.
z=S.symbols('z',real=True)
Qprime_at_root=x*(b*S.diff(sinc,x)-g*x/(k*z))
assert S.simplify(Qprime_at_root.subs(z,-b*sinc)-x*S.diff(phi,x)/(2*k*b*sinc))==0

# Nonlinear fourth-root and the fold depth, for a representative positive b,k.
bv,kv=2.,3.
g0=kv*bv*bv/3
r0sq=kv*bv*bv
for eps in (1e-3,1e-4,1e-5):
    f=lambda a:g0*a*a+kv*bv*bv*(math.sin(a)/a)**2-r0sq-eps
    root=brentq(f,1e-8,0.7)
    approximation=(45*eps/(2*kv*bv*bv))**.25
    assert abs(root/approximation-1)<.002
for delta in (-.03,-.015,-.0075):
    gv=g0+delta
    f=lambda a:gv*a*a+kv*bv*bv*(math.sin(a)/a)**2-r0sq
    # The strict local minimum is at a>0; the derived quadratic coefficient is asymptotically exact.
    from scipy.optimize import minimize_scalar
    opt=minimize_scalar(f,bounds=(.001,.5),method='bounded',options={'xatol':1e-13})
    assert opt.success
    fold_approx=-45*delta**2/(8*kv*bv*bv)
    assert opt.fun<0 and abs(opt.fun/fold_approx-1)<.05
print('Symbolic identities and finite diagnostics: PASS')

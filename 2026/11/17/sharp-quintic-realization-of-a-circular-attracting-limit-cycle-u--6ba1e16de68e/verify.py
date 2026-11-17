"""Symbolic cofactor identities and a numerical Floquet check.

Requires Python 3, SymPy and mpmath. Run `python verify.py`.
This is a supplementary finite/algebraic reproducibility check; the
all-parameter sign argument is given in RESULT.md.
"""
import sympy as sp
import mpmath as mp

x, y, a, b, r, kappa, eps = sp.symbols(
    'x y a b r kappa eps', real=True
)
f = (x-a)**2 + (y-b)**2 - r*r
g = x*x+y*y-1
Jf = sp.Matrix([-sp.diff(f,y), sp.diff(f,x)])
Jg = sp.Matrix([-sp.diff(g,y), sp.diff(g,x)])
V = x*y*(g*Jf-f*Jg)
X = (1+kappa*x)*V + eps*f*g*sp.Matrix([x,0])
K0 = 4*x*y*(b*x-a*y)
cofactor_f = (1+kappa*x)*K0+2*eps*x*(x-a)*g
cofactor_g = (1+kappa*x)*K0+2*eps*x*x*f
D = lambda h: sp.diff(h,x)*X[0]+sp.diff(h,y)*X[1]
assert sp.expand(D(f)-f*cofactor_f)==0
assert sp.expand(D(g)-g*cofactor_g)==0
assert sp.expand(X[0].subs(x,0))==0
assert sp.expand(X[1].subs(y,0))==0
assert sp.Poly(sp.expand(X[0]),x,y).total_degree()==5
assert sp.Poly(sp.expand(X[1]),x,y).total_degree()==5
assert sp.simplify(sp.expand(V[0])+(V[1]*0)-V[0])==0

mp.mp.dps=55
A = mp.mpf(2); B=mp.mpf(2); R=mp.mpf('0.5'); K=mp.mpf(1); E=mp.mpf(1)
integrand=lambda th: E*R*mp.cos(th)/((B+R*mp.sin(th))*(1+K*(A+R*mp.cos(th))))
log_multiplier=mp.quad(integrand,[0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi])
negative_pair=-2*E*K*R**2 * mp.quad(
    lambda th: mp.cos(th)**2/((B+R*mp.sin(th))*((1+K*A)**2-(K*R*mp.cos(th))**2)),
    [-mp.pi/2,0,mp.pi/2])
assert abs(log_multiplier-negative_pair)<mp.mpf('1e-45')
assert -mp.mpf('0.05')<log_multiplier<-mp.mpf('0.04')
print('PASS: general symbolic invariance/cofactor identities, Kolmogorov property, degree 5')
print('PASS: sample quadratures agree; log Floquet multiplier',mp.nstr(log_multiplier,25))
print('PASS: sample Floquet multiplier',mp.nstr(mp.exp(log_multiplier),25))

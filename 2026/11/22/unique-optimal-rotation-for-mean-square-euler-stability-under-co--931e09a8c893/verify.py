"""Exact symbolic and finite numerical checks for the stated Euler stability theorem.

Requires Python 3, SymPy and NumPy. Numerical experiments do not replace
proofs of the infinite-domain monotonicity or uniqueness statements.
"""
import sympy as S
import numpy as np

x, s, tau = S.symbols('x s tau', positive=True, real=True)
c = 1-x
d = S.sqrt(s)*x
q = c*c+d*d
F = (2*(2+s)-2*(2+s)*x+(1+s)*x*x)/((1+s)*(2-(1+s)*x)*(4-4*x+(1+s)*x*x))
R = S.Rational(1,2)/(1-q) + (1-c*c+d*d)/(2*((1-c*c+d*d)**2+4*c*c*d*d))
assert S.simplify(x*R-F)==0, 'return gain rational identity'
print('PASS: exact return-gain identity')

C = S.Matrix([[c,-d],[d,c]])
T0 = S.Matrix([[c*c,-2*c*d,d*d],[c*d,c*c-d*d,-c*d],[d*d,2*c*d,c*c]])
T = T0+S.diag(tau*x,0,0)
assert S.simplify(S.det(S.eye(3)-T)/S.det(S.eye(3)-T0)-(1-tau*F))==0
print('PASS: exact rank-one covariance determinant identity')

t=S.symbols('t',positive=True)
F_t=(s*(s+1)+2*s*t+2*t*t)/(4*(1+s)*t*(s+t*t))
assert S.simplify(F.subs(x,2*(1-t)/(1+s))-F_t)==0
F_x=(s**3+s**2+(3*s**2+s)*t*t+4*s*t**3+2*t**4)/(8*t*t*(s+t*t)**2)
assert S.simplify(S.diff(F,x).subs(x,2*(1-t)/(1+s))-F_x)==0
print('PASS: strict timestep derivative identity')

G=x**3*((x-1)**2+1)*s**3+x*(3*(x-1)**4-(x-1)**2+2)*s*s+x*(x-2)**2*(3*(x-1)**2+1)*s+(x-2)**3*(x-1)**2
# Check the same sign, by comparing cleared nonnegative denominators.
N=2*(2+s)-2*(2+s)*x+(1+s)*x*x
D=(1+s)*(2-(1+s)*x)*(4-4*x+(1+s)*x*x)
assert S.simplify(S.diff(N,s)*D-N*S.diff(D,s)-2*G)==0
print('PASS: frequency-derivative numerator identity')

cases=0
for xv in [S.Rational(1,10),S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),S.Integer(1),S.Rational(3,2)]:
 for sv in [S.Integer(0),S.Rational(1,4),S.Integer(1),S.Integer(2),S.Integer(5)]:
  if xv*(1+sv)>=2: continue
  for tv in [S.Rational(1,10),S.Integer(1),S.Integer(2),S.Integer(3),S.Integer(5)]:
   Tnum=np.array(T.subs({x:xv,s:sv,tau:tv}),dtype=float)
   rho=max(abs(np.linalg.eigvals(Tnum)))
   yes=(tv*F.subs({x:xv,s:sv})<1)
   if abs(rho-1)>1e-8:
    assert (rho<1)==yes, (xv,sv,tv,rho,yes)
    cases+=1
print('PASS:',cases,'independent 3-by-3 covariance spectral tests')

import mpmath as mp
mp.mp.dps=35
f= S.lambdify((x,s),F,'mpmath')
fs=S.lambdify((x,s),S.diff(F,s),'mpmath')
xstar,sstar=mp.findroot((lambda X,Z:3*f(X,Z)-1,lambda X,Z:fs(X,Z)),(.042,5.0))
assert xstar>0 and sstar>2 and xstar<2/(1+sstar)
assert abs(3*f(xstar,sstar)-1)<mp.mpf('1e-28')
assert abs(fs(xstar,sstar))<mp.mpf('1e-28')
print('PASS: tau=3 stationary pair, scaled step',mp.nstr(xstar,20), 's',mp.nstr(sstar,20))

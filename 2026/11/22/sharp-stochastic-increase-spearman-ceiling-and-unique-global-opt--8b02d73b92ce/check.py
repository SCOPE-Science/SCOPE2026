#!/usr/bin/env python3
"""Independent reproducibility checks for the exponential-quadratic copula envelope.

All numerical claims are diagnostic. The analytic uniqueness argument is in RESULT.md.
Requires mpmath>=1.3, sympy>=1.12, scipy>=1.10.
"""
from math import isfinite
import mpmath as mp
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

mp.mp.dps=85
x=sp.symbols('x',positive=True)
A=sp.sqrt(sp.pi)/2 * sp.erf(x)
Q=A-x*(1+x**2)*sp.exp(-x**2)
assert sp.simplify(sp.diff(Q,x)-x**2*(2*x**2-1)*sp.exp(-x**2)) == 0
J=A/x**2-sp.exp(-x**2)/x
assert sp.simplify(sp.diff(J,x)+2*Q/x**3)==0
print('symbolic Q derivative and envelope derivative: PASS')

E=mp.exp; erf=mp.erf; pi=mp.pi
A_mp=lambda s: mp.sqrt(pi)/2*erf(s)
Q_mp=lambda s: A_mp(s)-s*(1+s*s)*E(-s*s)
J_mp=lambda s: A_mp(s)/(s*s)-E(-s*s)/s
rho_of_s=lambda s: mp.mpf(3)*E(1)/2*J_mp(s)**2
s_lo=mp.sqrt(mp.mpf('0.5'))
assert Q_mp(s_lo)<0 and Q_mp(1)>0
sstar=mp.findroot(Q_mp,(mp.mpf('.9'),mp.mpf('1.0')))
assert s_lo<sstar<1
astar=4*sstar*sstar
rfull=rho_of_s(sstar)
I=lambda a: mp.quad(lambda u: E(a*u*(1-u))-1,[0,mp.mpf('.5'),1])
r_si=3*I(2)**2
assert mp.mpf('3.746989957972')<astar<mp.mpf('3.746989957974')
assert mp.mpf('0.586623892839')<rfull<mp.mpf('0.586623892841')
assert mp.mpf('0.505989303562')<r_si<mp.mpf('0.505989303564')
assert rfull>r_si
print('root and envelopes:')
for label,z in [('s*',sstar),('alpha*',astar),('unrestricted max rho',rfull),('SI max rho',r_si)]:
 print(label,mp.nstr(z,40))

def rho_envelope(a):
 a=mp.mpf(a)
 if a==0: return mp.mpf(0)
 val=I(a)
 if a<=2: return 12*(val/a)**2
 return (6/a)*E(1-a/2)*val*val

for a in [mp.mpf('-50'),mp.mpf('-10'),mp.mpf('-1'),mp.mpf('0.01'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('2'),mp.mpf('2.01'),mp.mpf('3'),mp.mpf('3.5'),mp.mpf('3.74698995797'),mp.mpf('4'),mp.mpf('5'),mp.mpf('10'),mp.mpf('40')]:
 r=rho_envelope(a)
 if a!=0:
  assert 0<r<=rfull+mp.mpf('1e-19')
  if a<=2: assert r<=r_si+mp.mpf('1e-19')
  else:
   s=mp.sqrt(a)/2
   assert mp.almosteq(r,rho_of_s(s),rel_eps=mp.mpf('1e-65'))
print('independent envelope evaluation at 14 representative shapes: PASS')

# Conditional CDF F(v|u)=partial_u C(u,v). Its u-derivative has sign
# sign(delta * (-alpha)*(alpha*(1-2u)^2-2) * (1-exp(alpha*v*(1-v))))
def conditional_cdf_u_derivative(u,v,a,d):
 u,v,a,d=map(mp.mpf,(u,v,a,d))
 gprime=E(a*u*(1-u))*(a*(1-2*u)**2-2)
 f_v=1-E(a*v*(1-v))
 return d*(-a)*gprime*f_v
for a in [-10,-1,mp.mpf('.5'),2]:
 for u in [mp.mpf('0.03'),mp.mpf('.24'),mp.mpf('.51'),mp.mpf('.98')]:
  assert conditional_cdf_u_derivative(u,mp.mpf('0.37'),a,mp.mpf('.1'))<=0
for a in [mp.mpf('2.01'),astar,8]:
 assert conditional_cdf_u_derivative(mp.mpf('.0001'),mp.mpf('.37'),a,mp.mpf('.01'))>0
 assert conditional_cdf_u_derivative(mp.mpf('.5'),mp.mpf('.37'),a,mp.mpf('.01'))<0
print('conditional stochastic monotonicity signs: PASS')

# Independent quadrature/optimization of Spearman upper envelope.
def scipy_rho(a):
 def integ(u):return __import__('math').expm1(a*u*(1-u))
 h=quad(integ,0,1,epsabs=2e-13,epsrel=2e-13)[0]
 if a<=2: return 12*(h/a)**2
 return 6/a*__import__('math').exp(1-a/2)*h*h
result=minimize_scalar(lambda a:-scipy_rho(a),bounds=(2.001,12),method='bounded',options={'xatol':1e-12})
assert result.success
assert abs(result.x-float(astar))<1e-6
assert abs(-result.fun-float(rfull))<2e-12
print('independent scipy quadrature and bounded optimization: PASS')
print('ALL CHECKS PASSED')

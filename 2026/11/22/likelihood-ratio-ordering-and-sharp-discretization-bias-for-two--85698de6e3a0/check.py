"""Public scientific reproduction: two half-logistic count discretizations."""
import sympy as s
from math import exp, log
import mpmath as mp
u, q, t = s.symbols('u q t', positive=True)
g = u/(1+u)**2
# Normalized mass ratio algebra, without the unknown positive normalization constant.
f = (1+u)/(1+q*u)
assert s.simplify(s.diff(f,u) - (1-q)/(1+q*u)**2)==0
# Sharp TV coefficient from sign-changing continuum density.
integrand = (3*t-1)/(2*(1+t)**3)
assert s.simplify(s.integrate(integrand,(t,s.Rational(1,3),1))-s.Rational(1,16))==0
# Exact parent half-logistic integrals.
y=s.symbols('y',real=True,nonnegative=True)
assert s.simplify(s.integrate(s.exp(-y)/(1+s.exp(-y))**2,(y,0,s.oo))-s.Rational(1,2))==0
assert s.simplify(s.integrate(y*s.exp(-y)/(1+s.exp(-y))**2,(y,0,s.oo))-s.log(2))==0
# Finite high-precision numerical tests; proof remains analytic.
mp.mp.dps=60
for theta in [mp.mpf('0.1'),mp.mpf('0.04'),mp.mpf('0.02')]:
 Q=mp.exp(-theta); N=int(45/float(theta));
 w=[Q**n/(1+Q**n)**2 for n in range(N)]; Z=sum(w)
 B=[z/Z for z in w]
 A=[2*(1-Q)*Q**n/((1+Q**n)*(1+Q**(n+1))) for n in range(N)]
 ratios=[a/b for a,b in zip(A,B)]
 assert all(ratios[n]>ratios[n+1] for n in range(N-1))
 tv=sum(abs(a-b) for a,b in zip(A,B))/2
 dmean=sum(n*(b-a) for n,(a,b) in enumerate(zip(A,B)))
 assert abs(float(tv/theta-mp.mpf(1)/16))<0.0001
 assert abs(float(dmean-(1-mp.log(2))/2))<0.001
 print('theta',theta,'TV/theta',mp.nstr(tv/theta,12),'mean gap',mp.nstr(dmean,12))
print('exact and numerical reproduction passed')

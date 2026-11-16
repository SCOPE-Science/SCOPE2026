"""Finite checks and independent symbolic identities for Haar-Grassmannian one-coordinate cap spectra."""
import sympy as S
from mpmath import mp

n,k,x = S.symbols('n k x', positive=True)
m=n-1
c=2*k*(n-k)/(n*(n-1)*(n+2))
A=S.factor((x-k/n)**2*n/(m*c))
C=S.factor(2*x*(1-x)/(m*c))
T=S.factor(2*(k-2*x+x*x-(k-x)**2/m)/((m-1)*(m+2))/c)
dimT=S.Rational(1,2)*n*(n-1)-1
dimV=S.Rational(1,2)*n*(n+1)-1
assert S.simplify(A+m*C+dimT*T-dimV)==0
assert S.simplify(A.subs(x,S.Rational(1,3)).subs({n:6,k:3})-C.subs(x,S.Rational(1,3)).subs({n:6,k:3})) !=0

def coeff(d):
  u,v=S.symbols('u v')
  a=k/2;b=(n-k)/2
  poly=S.Poly(S.expand(a*(1-x)*(u+v*x)-b*x*(u+v*x)+v*x*(1-x)+d),x)
  return {t:S.factor(y) for t,y in S.solve(poly.all_coeffs(),[u,v],dict=True)[0].items()}
for d,target in [(A-C,k/n),(A-T,(k*(n+2)-2*n)/(n*(n-2))),(C-T,(n-k-1)/(n-2))]:
  z=coeff(d);u,v=S.symbols('u v')
  assert S.simplify(z[u]+target*z[v])==0
  assert S.simplify(z[u].subs({n:7,k:3})) !=0
print('GRASSMANNIAN_CAP_SYMBOLIC_PASS trace_and_three_crossings')
mp.dps=45
for N,K in [(4,1),(4,2),(5,1),(5,2),(6,2),(6,3),(7,2),(7,3),(9,4),(10,6)]:
  a=mp.mpf(K)/2;b=mp.mpf(N-K)/2
  vals=[S.lambdify(x,t.subs({n:N,k:K}),'mpmath') for t in (A,C,T)]
  for t in (mp.mpf('0.15'),mp.mpf('0.37'),mp.mpf('0.65'),mp.mpf('0.88')):
    lam=[mp.quad(lambda z: f(z)*z**(a-1)*(1-z)**(b-1)/mp.beta(a,b),[t,1]) for f in vals]
    p=mp.betainc(a,b,t,1,regularized=True)
    assert abs(lam[0]+(N-1)*lam[1]+(N*(N-1)//2-1)*lam[2] - (N*(N+1)//2-1)*p)<mp.mpf('1e-30')
    assert all(0<y<1 for y in lam)
  if N==2*K:
    t=mp.mpf('0.5');lam=[mp.quad(lambda z:f(z)*z**(a-1)*(1-z)**(b-1)/mp.beta(a,b),[t,1]) for f in vals]
    assert all(abs(z-mp.mpf('0.5'))<mp.mpf('1e-30') for z in lam)
print('GRASSMANNIAN_CAP_NUMERIC_PASS dimensions_rank_cases=10 thresholds=40')

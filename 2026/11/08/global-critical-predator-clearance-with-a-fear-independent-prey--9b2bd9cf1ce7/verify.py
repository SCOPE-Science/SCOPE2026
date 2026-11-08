"""Exact coefficient checks and non-probative finite-time diagnostics for a predator model."""
import sympy as sp
from scipy.integrate import solve_ivp

L=sp.Rational(1)
r=sp.Rational(2); d1=sp.Rational(1); d2=sp.Rational(1)
a=sp.Rational(1); c=sp.Rational(6); m=sp.Rational(1,2); c1=sp.Rational(1,2)
d3=sp.Rational(1); d4=sp.Rational(2)
x=sp.symbols('x',positive=True)
f=c*(1-m)*x/(a+(1-m)*x)
assert sp.simplify(c1*f.subs(x,L)-d3)==0
assert sp.simplify(c1*sp.diff(f,x).subs(x,L)-sp.Rational(2,3))==0
for K,lim in [(sp.Rational(1,2),sp.Rational(1,2)),(sp.Rational(1,4),sp.Rational(3,5))]:
 B=r*L*K+f.subs(x,L)
 D=c1*sp.diff(f,x).subs(x,L)*B/(r-d1)
 assert sp.simplify(1/D-lim)==0
 assert sp.simplify(B/(r-d1)/D-sp.Rational(3,2))==0
 lam=3.; b=1.; e=.5; mu=.25; gam=.5; beta=1.
 kk=float(K)
 def rhs(t,y):
  X,S,I=y; P=S+I
  ff=3.*X/(1.+.5*X)
  inc=lam*S*I/(1.+b*I)
  tr=gam*I/(beta+I)
  return [2.*X/(1.+kk*P)-X-X*X-ff*(S+e*I), .5*ff*S-inc-S+mu*I+tr, inc-2.*I-mu*I-tr]
 sol=solve_ivp(rhs,(0,20000),[.8,.2,.1],method='DOP853',rtol=2e-11,atol=1e-13,t_eval=[5000,10000,20000],max_step=50)
 assert sol.success
 for t,(X,S,I) in zip(sol.t,sol.y.T):
  print('fear',K,'t',t,'t*S',t*S,'t*(1-X)',t*(1-X),'I',I)
 assert abs(sol.t[-1]*sol.y[1,-1]-float(lim))<.01
 assert abs(sol.t[-1]*(1-sol.y[0,-1])-1.5)<.025
print('VERIFY_OK')

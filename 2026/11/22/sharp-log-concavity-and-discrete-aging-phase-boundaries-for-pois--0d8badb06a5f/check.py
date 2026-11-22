"""Exact algebra and sampled rational cross-checks for Poisson--Loai ageing."""
import sympy as s
from fractions import Fraction
n,a,t = s.symbols('n a t', integer=True, positive=True)
A=a*t; B=2+3*A; C=2*(2+t+A); q=1/(1+t)
P=lambda k: A*k*k+B*k+C
K=t*t/(2*(1+a)*(1+t)**3)
N=s.simplify(K*(A*q*(1+q)/(1-q)**3+B*q/(1-q)**2+C/(1-q)))
assert s.factor(N-1)==0
Delta=s.factor(P(n)**2-P(n-1)*P(n+1))
assert s.factor(Delta-(2*A*A*n*n+2*A*B*n+B*B-A*A-2*A*C))==0
L=s.factor(Delta.subs(n,1)/4)
assert s.factor(L-(3*a*a*t*t-a*t*t+2*a*t+1))==0
assert s.factor(Delta.subs(n,n+1)-Delta)==s.factor(2*A*A*(2*n+1)+2*A*B)
Q=lambda k: P(k)/(1-q)+(2*A*k+B)*q/(1-q)**2+A*q*(1+q)/(1-q)**3
hazD=s.factor((P(n+1)*Q(n)-P(n)*Q(n+1))*(1-q)**3/q)
F=s.factor(hazD*(1+t)/(4*t))
H=3*a*a*t*t-a*t*t+2*a*a*t+2*a*t+a+1
assert s.factor(F.subs(n,0)-H)==0
assert s.factor(H-L-(a+2*a*a*t))==0
assert s.factor(F-(H + a*a*t*t*n*n/2 + (5*a*a*t*t/2 + a*a*t + a*t)*n))==0
assert s.factor(F.subs(n,n+1)-F)==s.factor(a*a*t*t*(n+3)+a*a*t+a*t)
# Conventions: h_n = P(X=n) / P(X>=n). Sign of h_{n+1}-h_n equals numerator.
# Exact-rational comparisons using polynomially summed survival tails.
for aa,tt in [(s.Rational(1,10),s.Rational(53,10)),(s.Rational(1,10),s.Rational(56,10)),(s.Rational(1,10),s.Rational(6)),(s.Rational(1,3),s.Rational(100)),(s.Rational(1,100),s.Rational(15))]:
 args={a:aa,t:tt}
 probs=[s.factor((K*q**k*P(k)).subs(args)) for k in range(8)]
 hh=[s.factor((P(k)/Q(k)).subs(args)) for k in range(8)]
 d1=s.sign((probs[1]**2-probs[0]*probs[2]))
 dh=s.sign(hh[1]-hh[0]); assert d1==s.sign(L.subs(args)); assert dh==s.sign(H.subs(args))
 for j in range(2,7):
  assert s.sign(hh[j+1]-hh[j])==s.sign(F.subs({n:j,**args}))
 print('a',aa,'theta',tt,'L',int(d1),'IFR-start',int(dh),'h0,h1',str(hh[0]),str(hh[1]))
print('ALL_CHECKS_PASSED')

"""Exact checks for two-landmark trace Nyström designs on complete bipartite kernels.

Run: python verify.py (requires SymPy). Finite tests supplement the general algebraic proof.
"""
import itertools
from fractions import Fraction
import sympy as sp

p,q,t=sp.symbols('p q t', positive=True)
N=p+q
x=1/t; y=1/(t+N); u=1/(t+q); v=1/(t+p)
a=x/N+q*y/(p*N)+u*(1-1/p)
b=x/N+q*y/(p*N)-u/p
c=x/N+p*y/(q*N)+v*(1-1/q)
d=x/N+p*y/(q*N)-v/q
e=(x-y)/N
a2,b2,c2,d2,e2=(-sp.diff(z,t) for z in (a,b,c,d,e))
score_A=sp.factor((a2+b2)/(a+b)+(a2-b2)/(a-b))
score_B=sp.factor((c2+d2)/(c+d)+(c2-d2)/(c-d))
score_X=sp.factor((c*a2+a*c2-2*e*e2)/(a*c-e**2))
U=(p-q)*t**4+2*(p**2-p-q**2+q+1)*t**3+(p**3+p**2*q-2*p**2-p*q**2+2*p*q+2*p-q**3+4*q)*t**2+2*q*(p*q+2*p-q**2+q)*t-q*(p**3-3*p**2-p*q**2-p*q+2*p+2*q**2-2*q)
V=(q-p)*t**4-2*(p**2-p-q**2+q-1)*t**3+(-p**3-p**2*q+p*q**2+2*p*q+4*p+q**3-2*q**2+2*q)*t**2-2*p*(p**2-p*q-p-2*q)*t+p*(p**2*q-2*p**2+p*q+2*p-q**3+3*q**2-2*q)
DA=(t+1)*(t+p)*(t+q)*(t+p+q-1)*(t**2+t*p+t*q+2*q)
DB=(t+1)*(t+p)*(t+q)*(t+p+q-1)*(t**2+t*p+t*q+2*p)
assert sp.cancel(score_A-score_X-U/DA)==0
assert sp.cancel(score_B-score_X-V/DB)==0
assert sp.simplify(sp.limit(U/q**3,q,sp.oo) - (p-2-t*t-2*t))==0
assert sp.simplify(sp.limit(V/q**3,q,sp.oo) - (t*t-p))==0
assert sp.factor(score_A-score_B).subs(p,q)==0
assertions=5

# Independent inverse + all possible pairs (no use of spectral formulas for computation).
for P in (3,4,5):
 for Q in (P,P+1,2*P,3*P,7*P):
  nn=P+Q
  L=sp.zeros(nn)
  for i in range(P):
   for j in range(P,nn):
    L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
  for T in (sp.Rational(1,3),sp.Rational(1),sp.Rational(5,2)):
   K=(T*sp.eye(nn)+L).inv();K2=K*K
   f=[z.subs({p:P,q:Q,t:T}) for z in (score_A,score_X,score_B)]
   for i,j in itertools.combinations(range(nn),2):
    z=(K2[i,i]*K[j,j]+K2[j,j]*K[i,i]-2*K2[i,j]*K[i,j])/(K[i,i]*K[j,j]-K[i,j]**2)
    typ=0 if j<P else (2 if i>=P else 1)
    assert sp.cancel(z-f[typ])==0,(P,Q,T,i,j)
    assertions+=1

# Exact sign-pattern and root-order certificates on representative, nonexceptional sizes.
for P in range(3,12):
 for Q in (20*P*P,30*P*P):
  polyU=sp.Poly(U.subs({p:P,q:Q}),t)
  polyV=sp.Poly(V.subs({p:P,q:Q}),t)
  assert polyU.all_coeffs()[0] < 0 and all(z<0 for z in polyU.all_coeffs()[:-1]) and polyU.all_coeffs()[-1]>0
  assert polyV.all_coeffs()[-1]<0 and all(z>0 for z in polyV.all_coeffs()[:-1])
  midpoint=sp.sqrt(P)-sp.Rational(1,2)
  assert U.subs({p:P,q:Q,t:midpoint})<0
  assert V.subs({p:P,q:Q,t:midpoint})<0
  assertions+=4

print('PASS',assertions,'exact assertions; all three orbit scores match direct matrices')

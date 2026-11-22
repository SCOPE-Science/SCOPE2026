#!/usr/bin/env python3
"""Exact symbolic certificates and finite rational cross-checks for a weighted-biclique two-leader theorem."""
from itertools import combinations
import sympy as s

n, t, u, v, z = s.symbols('n t u v z')
d = n - 1 + t
h = t - 1
q = n - 2
f = lambda w: 2*(d*d+w)/(d*d-w)**2
sigma = h*h + q*(n+2*h)
S = 2/d**2 + (n-3)*f(h*h) + f(sigma)
M = (n-2)*f(h*h) + f((d-1)**2)
T = d-1
P = d**4 - d**2*(T**2-2*h)+h*h
A = 2*d*d - T*T+2*h
U = (n-3)*f(h*h) + 4*d*d*(A*A-2*P)/P**2 - 2*A/P
D = n**2*d**2*(n+2*t-2)**2*(2*n+2*t-3)**2
Q = s.factor(s.cancel((M-S)*D))
assert s.denom(Q)==1
Q = s.expand(Q)
# The non-matched-pair comparison denominator is positive for n>=3,t>=1.
E = (d**2)*(n+2*t-2)**2*(2*n*n+4*n*t-5*n+2*t*t-4*t+2)**2
R = s.expand(s.cancel((U-S)*E))
assert s.denom(R)==1
# Coefficient-sign certificates are exact operations over rational polynomials.
qu = s.Poly(s.expand(Q.subs(n,u+3)),t)
assert qu.degree()==6
assert all(c<0 for c in s.Poly(qu.nth(0),u).coeffs())
assert all(c>0 for k in range(2,7) for c in s.Poly(qu.nth(k),u).coeffs())
assert all(c>0 for c in s.Poly(qu.nth(6),u).coeffs())
assert s.factor(Q.subs(t,s.Rational(1,2)))==(n-1)**2*(6*n*n-6*n+1)
assert s.factor(Q.subs(t,0)).subs(n,3)<0
rv = s.Poly(s.expand(R.subs({n:u+3,t:v+1})),u,v)
assert all(c>0 for c in rv.coeffs())
assert s.degree(R,t)==6
# First-order formula and a concrete exact objective disagreement witness.
g = lambda w: 2*d/(d*d-w)
S1 = 2/d+(n-3)*g(h*h)+g(sigma)
M1 = (n-2)*g(h*h)+g((d-1)**2)
W = {n:3,t:s.Rational(9,20)}
assert s.factor((M1-S1).subs(W)) == s.Rational(745,72618)
assert s.factor((M-S).subs(W)) == -s.Rational(83084401,5273373924)
# Asymptotic expansion certificate for the root t=1/2-a/n^3-b/n^4.
x, a,b=s.symbols('x a b')
poly=s.Poly(s.expand(Q.subs({n:1/x,t:s.Rational(1,2)-a*x**3-b*x**4})*x**7),x)
assert s.simplify(poly.nth(3)-(6-8*a))==0
assert s.simplify(poly.nth(4)-(28*a-8*b-18))==0

# Independent direct matrix checks at a set of exact rational weights.
count=0
for N in range(3,7):
 for wt in (s.Rational(1,7),s.Rational(9,20),s.Rational(1,2),s.Integer(1),s.Rational(5,2)):
  B=s.ones(N,N)+(wt-1)*s.eye(N)
  deg=N-1+wt
  L=s.diag(*([deg]*(2*N)))
  for i in range(N):
   for j in range(N):
    L[i,N+j]=L[N+j,i]=-B[i,j]
  vals={}
  for lab, pair in (('same',(0,1)),('matched',(0,N)),('unmatched',(0,N+1))):
   F=[k for k in range(2*N) if k not in pair]
   C=L.extract(F,F)
   inv=C.inv()
   vals[lab]=s.trace(inv*inv)
   assert s.factor(vals[lab]-{'same':S,'matched':M,'unmatched':U}[lab].subs({n:N,t:wt}))==0
   count+=1
  # The orbit representative costs must agree with every possible unordered pair.
  if N<=5:
   for a0,b0 in combinations(range(2*N),2):
    lab=('same' if a0<N and b0<N or a0>=N and b0>=N else
      'matched' if (a0 % N)==(b0 % N) else 'unmatched')
    F=[k for k in range(2*N) if k not in (a0,b0)]
    C=L.extract(F,F); inv=C.inv()
    assert s.trace(inv*inv)==vals[lab]
    count+=1
print('PASS symbolic factorizations, positivity, roots, rational mismatch, and',count,'exact grounded-matrix tests')

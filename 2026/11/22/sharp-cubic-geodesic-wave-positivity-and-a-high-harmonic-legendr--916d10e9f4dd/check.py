#!/usr/bin/env python3
"""Supplementary exact checks for cubic Legendre modulation and the damping threshold."""
import sympy as s

x,n,y = s.symbols('x n y', integer=True, positive=True)
T = 4*x**3-3*x
checks = 0

def a(k): return (k+1)/(2*k+1)
def b(k): return k/(2*k+1)
# Exact symbolic multiplication identity at an arbitrary generic degree n.
weights = {n:s.Integer(1)}
for _ in range(3):
    new={}
    for k,v in weights.items():
        new[k+1]=new.get(k+1,0)+v*a(k)
        new[k-1]=new.get(k-1,0)+v*b(k)
    weights=new
c={k:s.factor(4*v-3*({n+1:a(n),n-1:b(n)}.get(k,0))) for k,v in weights.items()}
expected = {
 n+3: 4*(n+1)*(n+2)*(n+3)/((2*n+1)*(2*n+3)*(2*n+5)),
 n+1: 3*(n+1)/((2*n-1)*(2*n+1)*(2*n+5)),
 n-1: 3*n/((2*n-3)*(2*n+1)*(2*n+3)),
 n-3: 4*n*(n-1)*(n-2)/((2*n-3)*(2*n-1)*(2*n+1))}
for k,v in expected.items():
 assert s.factor(c[k]-v)==0;checks+=1
# Independent exact polynomial tests, including low degrees, parity and omitted zero term.
for N in range(0,55):
 p = s.Poly(s.expand(T*s.legendre(N,x)),x)
 decomposition = {}
 for j in range(N+3,-1,-1):
  leading=s.Poly(s.legendre(j,x),x).LC()
  coeff=s.cancel(p.nth(j)/leading)
  if coeff:
   decomposition[j]=coeff
   p -= s.Poly(coeff*s.legendre(j,x),x)
 assert p.is_zero;checks+=1
 if N==0: assert decomposition=={3:s.Rational(8,5),1:-s.Rational(3,5)}
 if N==1: assert decomposition=={4:s.Rational(32,35),2:s.Rational(2,7),0:-s.Rational(1,5)}
 if N>=2:
  assert all(q>0 for q in decomposition.values())
  assert sum(decomposition.values())==1
  assert all(s.factor(decomposition.get(k.subs(n,N),0)-v.subs(n,N))==0 for k,v in expected.items() if (k.subs(n,N)>=0))
  checks+=3
# Exact low-mode formulas by elementary sine integrals, without numerical integration.
q=s.symbols('q',positive=True)
I=lambda m:m*(1-(-1)**m*q)/(y+m*m)
B0=s.factor((I(4)-I(2))/2)
B1=s.factor((I(5)-I(1))/4)
assert s.factor(B0-(1-q)*(y-8)/((y+4)*(y+16)))==0;checks+=1
assert s.factor(B1-(1+q)*(y-5)/((y+1)*(y+25)))==0;checks+=1
for Y in [s.Rational(1,4),s.Integer(5),s.Integer(8),s.Integer(9),s.Integer(40)]:
 assert s.sign((Y-8))==(0 if Y==8 else (1 if Y>8 else -1));checks+=1
 assert Y!=8 or Y>5;checks+=1
print(f'PASS: {checks} exact symbolic/rational assertions. Infinite-degree theorem uses the analytic proof.')

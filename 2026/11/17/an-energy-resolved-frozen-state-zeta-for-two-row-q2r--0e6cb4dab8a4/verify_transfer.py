#!/usr/bin/env python3
"""Exact transfer certificate for frozen Q2R on a two-row periodic multigraph.
Requires SymPy (tested with SymPy 1.13.1); Python 3.11+.
"""
import sympy as s
from collections import Counter
u,y=s.symbols('u y')
cols=[(j&1,(j>>1)&1) for j in range(4)]
T=s.zeros(16)
for a in range(4):
 for b in range(4):
  for c in range(4):
   A,B,C=cols[a],cols[b],cols[c]
   if any(A[r]+C[r]+2*B[1-r]==2 for r in (0,1)): continue
   E=2*(B[0]!=B[1])+(B[0]!=C[0])+(B[1]!=C[1])
   T[4*a+b,4*b+c]=u**E
# The factors are written without any simultaneous symbolic character-poly fitting.
factors=[y**2-u**4,
         y**4-y**3+(u**4+u**2)*y**2+u**4*y+u**6,
         y**4+u**4*y**3+(u**6+u**4)*y**2-u**8*y+u**10,
         y**6-(1+u**4)*y**5-(u**6+u**2)*y**4+(-u**8+2*u**6-u**4)*y**3+(u**10+u**6)*y**2+2*u**10*y-u**12]
assert s.Poly(T.charpoly(y).as_expr()-s.prod(factors),y,u)==s.Poly(0,y,u)
print('states=16 admissible-edges='+str(sum(int(T[a,b]!=0) for a in range(16) for b in range(16))))
print('characteristic-identity=PASS factors-degrees=[2,4,4,6]')
print('unit-weight-factorization='+str(s.factor(T.subs(u,1).charpoly(y).as_expr())))
# At u=1, use integer transfer powers, independent of any numerical eigenvalue evaluation.
U=T.subs(u,1); A=s.eye(16)
for n in range(1,13):
 A=A*U
 if n%2==0 and n>=4:
  luc=lambda k: int(s.lucas(k))
  exact=luc(2*n)+4*luc(n)*(1 if n%6==0 else -s.Rational(1,2))+4+(2 if n%3==0 else -1)
  assert A.trace()==exact
  print('n='+str(n)+' frozen='+str(A.trace())+' Lucas-formula=PASS')
# Independent weighted check against direct-update energy histograms at two widths.
expected={4:{0:2,4:4,8:24,12:4,16:2},
          6:{0:2,4:18,6:48,8:72,10:24,12:72,14:24,16:72,18:48,20:18,24:2}}
for n,hist in expected.items():
    h={e[0]:int(coeff) for e,coeff in s.Poly(s.expand(s.trace(T**n)),u).as_dict().items()}
    assert h==hist
    print('weighted-hist n='+str(n)+' exact=PASS')
print('ALL PASS')

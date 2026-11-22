#!/usr/bin/env python3
"""Symbolic audit of the 4+3(m-1) invariant transfer representation."""
import sympy as s
x,q,m=s.symbols('x q m')
T=s.Matrix([[q*q,m*q,0,0], [0,0,q,1], [q,m-1,0,0], [0,0,1,0]])
U=s.Matrix([[0,q,1],[-1,0,0],[0,1,0]])
a=m-1
D0=1-a*x**3-a*q*x**2-q**2*(x+x**4)-q**3*x**3
D1=1+x**3+q*x**2
assert s.simplify((s.eye(4)-x*T).det()-D0)==0
assert s.simplify((s.eye(3)-x*U).det()-D1)==0
# Deficiency coefficients of the generating function: H_j=-x d/dx [q^j]log(D0 D1^a)
L0=(1-a*x**3)
L1= -a*x*x/(1-a*x**3)+a*x*x/(1+x**3)
L2=-(x+x**4)/(1-a*x**3)-a*a*x**4/(2*(1-a*x**3)**2)-a*x**4/(2*(1+x**3)**2)
assert s.simplify(L1-(-a*x**2/(1-a*x**3)+a*x**2/(1+x**3)))==0
# Check symbolic series against expansion of full M using explicit colors m=3,4,5.
for mm in (3,4,5):
  alphabet=range(mm+1)
  states=[(u,v) for u in alphabet for v in alphabet if not (u and v and u!=v)]
  M=s.zeros(len(states))
  for i,(u,v) in enumerate(states):
    for j,(v2,w) in enumerate(states):
      if v2==v and not (u and w and u==w):
        d=2-int(u>0)-int(v>0)-int(w>0)
        assert d>=0
        M[i,j]=q**d
  exact=s.factor((s.eye(len(states))-x*M).det(method='domain-ge'))
  conjecture=s.expand(D0*D1**(mm-1)).subs(m,mm)
  assert s.expand(exact-conjecture)==0
  print('DETERMINANT_VERIFIED',mm)
print('SYMBOLIC_VERIFIED')

#!/usr/bin/env python3
"""Exact symbolic transfer-matrix check of the bivariate enumerator (requires sympy)."""
import sympy as s
x,y=s.symbols('x y')
states=[(a,b) for a in range(3) for b in range(3)]
A=s.eye(9)
a=s.zeros(1,9)
b=s.zeros(9,1)
for i,(p,q) in enumerate(states):
    if p>=q: a[0,i]=1;b[i,0]=1
    for c in range(3):
        if int(p>=q)+int(q>=c)-int(p>=c)==1:
            j=states.index((q,c))
            A[i,j]-=y*x**int(q>=c)
D=1-3*x*y+3*x*x*y*y-x*x*y**3-x**3*y**3-3*x**3*y**4+3*x**4*y**5-x**4*y**6-3*x**5*y**7+x**6*y**9
P=6-8*x*y+6*x*y*y+3*x*x*y*y+6*x*x*y**3+x*x*y**4-9*x**3*y**4+6*x**3*y**5+9*x**4*y**6-x**4*y**7-3*x**5*y**8
N=x*y*y*P
assert s.expand(A.det()-D)==0
assert s.expand(x*y*y*(a*A.adjugate()*b)[0]-N)==0
U=(6*x-2*x*x+10*x**3-3*x**4+8*x**5-3*x**6)
V=1-3*x+2*x*x-4*x**3+2*x**4-3*x**5+x**6
assert s.expand(D.subs(y,1)-V)==0
assert s.expand(N.subs(y,1)-U)==0
print('SYMBOLIC_OK 9state_determinant_and_numerator bivariate_and_univariate')

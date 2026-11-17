#!/usr/bin/env python3
"""Exact transfer-matrix verification for 3-row periodic BML fixed states."""
from itertools import product
import sympy as s

z,x,y=s.symbols('z x y')
cols=[a for a in product(range(3), repeat=3) if all(a[r]!=2 or a[(r+1)%3]!=0 for r in range(3))]
assert len(cols)==18
A=s.Matrix(18,18,lambda i,j: int(all(cols[i][r]!=1 or cols[j][r]!=0 for r in range(3))))
weighted=s.Matrix(18,18,lambda i,j: A[i,j]*x**cols[i].count(1)*y**cols[i].count(2))
assert len(cols)==18
C=s.factor(A.charpoly().as_expr())
expected=s.Symbol('lambda')**10*(s.Symbol('lambda')**4-13*s.Symbol('lambda')**3+14*s.Symbol('lambda')**2-10*s.Symbol('lambda')+1)*(s.Symbol('lambda')**4-5*s.Symbol('lambda')**3+9*s.Symbol('lambda')**2-5*s.Symbol('lambda')+1)
assert s.expand(C-expected)==0
print('columns',cols)
print('charpoly',C)
print('weighted_det_factor',s.factor((s.eye(18)-z*weighted).det(method='domain-ge')))
for n in range(3,10):
    count=s.trace(A**n)
    print('n',n,'stationary',count)
assert [s.trace(A**n) for n in range(3,10)]==[1686,19988,237828,2829334,33652161,400231244,4759942476]
root=max(float(s.re(r)) for r in s.nroots(s.Symbol('q')**4-13*s.Symbol('q')**3+14*s.Symbol('q')**2-10*s.Symbol('q')+1))
print('per_column_growth',format(root,'.15f'))
print('per_cell_entropy',format((s.log(root)/3).evalf(16),'.15f'))
D=s.factor_list((s.eye(18)-z*weighted).det(method='domain-ge'))[1]
P=[f for f,_ in D if s.expand(f.subs({x:1,y:1})).coeff(z,1)==-13][0]
assert s.factor(s.diff(P,x).subs({x:1,y:1}))==z*(6*z**3-38*z**2+39*z-17)
assert s.factor(s.diff(P,y).subs({x:1,y:1}))==-2*z*(4*z**2+7)
z0=s.Float(1/root,25)
qe=(6*z0**3-38*z0**2+39*z0-17)
qn=-2*(4*z0**2+7)
qprime=4*z0**3-30*z0**2+28*z0-13
print('east_cars_per_column',s.N(qe/qprime,13))
print('north_cars_per_column',s.N(qn/qprime,13))
print('occupied_fraction',s.N((qe+qn)/(3*qprime),13))

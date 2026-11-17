#!/usr/bin/env python3
# Exact finite-dimensional determinant / generating function computation.
import sympy as s
z=s.symbols('z')
T=s.Matrix([[1,1,0,0],[0,0,1,1],[1,0,0,0],[0,0,1,1]])
R=(s.eye(4)-z*T).inv()
F=s.factor(s.trace(z*T*R)-(R[2,2]-1)-z*z*R[1,2]-2*z-2*z*z)
expect=z**3*(3+z+2*z*z)/(1-2*z+z*z-z**3)
assert s.cancel(F-expect)==0
assert s.factor((s.eye(4)-z*T).det())==1-2*z+z*z-z**3
print('T=',T.tolist())
print('det(I-zT)=',s.factor((s.eye(4)-z*T).det()))
print('sum_n>=3 image_count(n) z^n =',F)
print('PASS: symbolic matrix computation')

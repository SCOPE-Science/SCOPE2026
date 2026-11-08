#!/usr/bin/env python3
"""Exact algebraic checks for a twelve-point cubic polynomial phaseless design.
Requires Python 3 and SymPy. No external data or network access.
"""
import itertools
import sympy as S
I=S.I
z=[]
for r, omega in [(1,1),(1+I,1),(S.sqrt(3),1)]:
    z += [S.expand(r*I**j) for j in range(4)]
assert len(z)==12 and len(set(z))==12
basis=[]
for j in range(4):
    H=S.zeros(4); H[j,j]=1;basis.append(H)
for j in range(4):
    for k in range(j+1,4):
        R=S.zeros(4);R[j,k]=R[k,j]=1;basis.append(R)
        J=S.zeros(4);J[j,k]=I;J[k,j]=-I;basis.append(J)
assert len(basis)==16
M=S.Matrix([[S.simplify(sum(B[j,k]*w**j*S.conjugate(w)**k for j in range(4) for k in range(4))) for B in basis] for w in z]);assert M.rank()==12
c,t,a,b=S.symbols('c t a b',real=True);u=a+I*b
H=S.zeros(4)
for j,v in enumerate([-6*c,11*c,-6*c,c]):H[j,j]=v
for j,k,v in [(1,0,-12*u),(2,1,15*u),(3,2,-4*u),(0,3,u),(2,0,-2*I*t),(3,1,I*t)]:
    H[j,k]=v;H[k,j]=S.conjugate(v)
for w in z:
    assert S.simplify(sum(H[j,k]*w**j*S.conjugate(w)**k for j in range(4) for k in range(4)))==0
A=[]
for inds in itertools.combinations(range(4),3):
    m=S.Poly(S.expand(H.extract(inds,inds).det()),a,b,c,t)
    xy=[c*(a*a+b*b),a*b*t,c**3,c*t*t]
    expr=S.expand(m.as_expr()); coefs=[]
    for target in [a*a*c,a*b*t,c**3,c*t*t]:
        coefs.append(S.expand(expr).coeff(target))
    # For the a^2+b^2 coefficient use coefficient of a^2 c
    assert S.expand(expr-sum(v*w for v,w in zip(coefs,xy)))==0
    A.append(coefs)
B=S.Matrix(A)
assert B.det()!=0
assert S.expand(H.det().subs(c,0)- (1089*(a*a+b*b)**2+11520*a*a*b*b+132*(a*a+b*b)*t*t+4*t**4))==0
print('CUBIC_THREE_SQUARES_CHECKS_PASS: sites=12 lift_rank=12 kernel_dim=4 minor_coefficient_det=',B.det())

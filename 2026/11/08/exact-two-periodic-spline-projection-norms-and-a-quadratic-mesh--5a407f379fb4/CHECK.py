#!/usr/bin/env python3
"""Exact symbolic and independent finite-mesh checks for the alternating spline endpoint theorem.
Scientific mathematics only; Python 3 and SymPy are required.
"""
from fractions import Fraction as F
from math import sqrt
import sympy as sp

r, q = sp.symbols('r q', positive=True)
s = r+1
A=(r+q)/(2*s)
B=(r*q+1)/(2*s)
phi=lambda u,v: (u*u+v*v)/(2*(u+v))
C=12*s*q/(r*(1-q*q))
limit=C/(1-q)*(r*phi(1,A)+phi(A,q)+r*phi(q,B)+phi(B,1))
target=(5*r*r+22*r+5)/(3*r*r+10*r+3)
rel=r*q*q-(3*r*r+8*r+3)*q+r
num=sp.together(limit-target).as_numer_denom()[0]
assert sp.rem(num,rel,q)==0
assert sp.simplify(2-target-(r-1)**2/((r+3)*(3*r+1)))==0
print('EXACT_ALTERNATING_GREEN_LIMIT_IDENTITY_OK')

def inv_rat(a):
    n=len(a)
    M=[[F(0) for j in range(2*n)] for i in range(n)]
    for i in range(n):
        M[i][i]=(a[i-1]+a[i])/3
        M[i][(i+1)%n]+=a[i]/6
        M[i][(i-1)%n]+=a[i-1]/6
        M[i][n+i]=F(1)
    for j in range(n):
        k=next(i for i in range(j,n) if M[i][j])
        M[j],M[k]=M[k],M[j]
        pivot=M[j][j];M[j]=[z/pivot for z in M[j]]
        for i in range(n):
            if i!=j:
                mul=M[i][j];M[i]=[x-mul*y for x,y in zip(M[i],M[j])]
    return [row[n:] for row in M]

def phiF(u,v):return (u*u+v*v)/(2*(u+v))
def mesh_exact(m,a,b):
    hs=[a if i%2==0 else b for i in range(2*m)]
    I=inv_rat(hs)
    vals=[]
    for i in range(2*m):
        vals.append(sum(hs[j]*phiF(abs(I[i][j]),abs(I[i][(j+1)%(2*m)])) for j in range(2*m)))
    return vals, I

def predicted(m,a,b):
    a=float(a);b=float(b)
    s=a+b;H=3*a*a+8*a*b+3*b*b
    delta=sqrt(H*H-4*a*a*b*b)
    q=2*a*b/(H+delta)
    U=lambda k:12*s/delta*(q**k+q**(m-k))/(1-q**m)
    V=lambda k:(a*U(k)+b*U((k+1)%m))/(2*s)
    J=lambda x,y:(x*x+y*y)/(2*(x+y))
    return sum(a*J(U(k),V(k))+b*J(V(k),U((k+1)%m)) for k in range(m))

for m in [2,3,4,5,6]:
    for a,b in [(1,1),(1,2),(2,5),(5,1),(7,3)]:
        vals,I=mesh_exact(m,F(a),F(b))
        assert all(v==vals[0] for v in vals), (m,a,b,'knots')
        assert all(((-1)**(i+j))*I[i][j]>0 for i in range(2*m) for j in range(2*m)), (m,a,b,'signs')
        assert abs(float(vals[0])-predicted(m,a,b))<1e-10, (m,a,b,vals[0],predicted(m,a,b))
print('INDEPENDENT_RATIONAL_GRAM_AND_EXACT_INTEGRAL_CHECKS_OK 25 CASES')
for a,b in [(1,1),(1,2),(2,5),(5,1),(7,3)]:
    formula=(5*a*a+22*a*b+5*b*b)/(3*a*a+10*a*b+3*b*b)
    assert abs(predicted(60,a,b)-formula)<1e-12
print('ASYMPTOTIC_FORMULA_NUMERICAL_CONSISTENCY_OK')
print('ALL_ALTERNATING_SPLINE_CHECKS_PASSED')

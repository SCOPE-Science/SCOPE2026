"""Reproduce exact first-jet quadrupole identities using SymPy and rational arithmetic.

Run: python verify.py
Requires: sympy (all displayed identities are also proved in RESULT.md).
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as s

d,t,a=s.symbols('d t a', real=True)
V0=(d+2)*(d*t-1)**2/(2*(d-1))
V1=d*(d+2)*t*(1-t)/(d-1)
V2=d*(d+2)*(1-t)**2/((d-1)*(d+1))
G0=V1
G1=(d+2)*(1+(d-6)*t+4*t**2)/(2*(d-1))
G2=(d+2)*(1-t)*(d-1+2*t)/((d-1)*(d+1))
E=[s.factor(a*V+(1-a)*G) for V,G in zip((V0,V1,V2),(G0,G1,G2))]
checks=0

def eq(left,right=0):
    global checks
    if s.factor(left-right)!=0:
        raise AssertionError(s.factor(left-right))
    checks+=1

# Structural identity and sharp equality case in symbolic dimension.
eq(2*(E[0]-E[1])+(d+1)*(E[1]-E[2]), (a+1)*(d+2)*(d*t-1)/2)
eq((E[0]-E[1]).subs(t,1/d),-(d+2)*(a*(d+2)-2)/d**2)
for e in E: eq(s.factor(e.subs({t:1/d,a:2/(d+2)})),1)
for V,G in zip((V0,V1,V2),(G0,G1,G2)):
    eq(s.factor(V.subs(t,1/d)*s.Rational(2,1)/(d+2)+G.subs(t,1/d)*d/(d+2)),1)
mult=(1,d-1,(d-2)*(d+1)/2)
eq(s.factor(sum(m*v for m,v in zip(mult,(V0,V1,V2)))),(d-1)*(d+2)/2)
eq(s.factor(sum(m*g for m,g in zip(mult,(G0,G1,G2)))),(d-1)*(d+2)/2)

# Finite orthonormal-axis first-jet forms, checked independently of the sector formulas.
def matmul_vec(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(v))]

def dot(u,v): return sum(x*y for x,y in zip(u,v))

def trAB(A,B):
    n=len(A)
    return sum(A[i][j]*B[i][j] for i in range(n) for j in range(n))

def q(A,x): return dot(x,matmul_vec(A,x))

def grad(A,x):
    v=matmul_vec(A,x); h=q(A,x)
    return [2*(v[i]-h*x[i]) for i in range(len(x))]

def form(A,B,weights):
    n=len(A); alpha=F(2,n+2)
    total=F(0)
    for k,w in enumerate(weights):
        x=[F(int(i==k)) for i in range(n)]
        total+=w*(alpha*q(A,x)*q(B,x)+(1-alpha)*dot(grad(A,x),grad(B,x))/F(2*n))
    return total

for n in range(3,7):
    basis=[]
    for i,j in combinations(range(n),2):
        A=[[F(0) for _ in range(n)] for _ in range(n)]
        A[i][i]=F(1); A[j][j]=F(-1);basis.append(A)
        B=[[F(0) for _ in range(n)] for _ in range(n)]
        B[i][j]=B[j][i]=F(1);basis.append(B)
    w=[F(1,n)]*n
    for A in basis:
        for B in basis:
            goal=F(2,n*(n+2))*trAB(A,B)
            got=form(A,B,w)
            if got!=goal: raise AssertionError((n,goal,got))
            checks+=1

# An anisotropic rule is *not* mistakenly identified as tight.
A=[[F(1),F(0),F(0)],[F(0),F(-1),F(0)],[F(0),F(0),F(0)]]
assert form(A,A,[F(1,2),F(1,4),F(1,4)])!=F(2,3*5)*trAB(A,A)
checks+=1
print('PASS exact symbolic identities and independent finite-node bilinear tests:',checks)

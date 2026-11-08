#!/usr/bin/env python3
"""Exact Cartier-power verification for the genus-14 one-pole family in characteristic five.
Requires Python 3 and SymPy. No network access or external inputs.
"""
import itertools
from collections import Counter
from math import comb
import sympy as sp

p=5
x=sp.Symbol('x')
a,b,c,e,f=sp.symbols('a b c e f')
par=(a,b,c,e,f)
F=x**8+a*x**6+b*x**4+c*x**3+e*x**2+f*x
g=14
basis=[(i,j) for j in range(4) for i in range((2*g-2-8*j)//5+1) if 2*g-2>=8*j]
assert len(basis)==g
index={m:i for i,m in enumerate(basis)}
M=sp.zeros(g)
for col,(i,j) in enumerate(basis):
    for ell in range(j+1):
        H=sp.Poly(x**i*F**(j-ell),x)
        for (k,),v in H.terms():
            if k%5!=4: continue
            row=index[((k-4)//5,ell)]
            M[row,col]+=(-1)**(j-ell)*comb(j,ell)*v
reduce=lambda z:sp.Poly(z,*par,modulus=5).as_expr()
M=M.applyfunc(reduce)
assert all(index[(i,j)]==n for n,(i,j) in enumerate(basis))
# The only nonzero 2nd-iterate rows are 0,1,2,6. Only columns 10--13 occur.
M2=(M.xreplace({z:z**5 for z in par})*M).applyfunc(reduce)
allowed={(0,10),(0,11),(0,12),(0,13),(1,11),(1,13),(2,13),(6,13)}
assert all(M2[i,j]==0 for i in range(g) for j in range(g) if (i,j) not in allowed)
assert reduce(M2[0,10]-2*b**6)==0
assert reduce(M2[0,11]-(2*b**5*c+2*c**5))==0
assert reduce(M2[0,12]-2*b**5*e)==0
assert reduce(M2[1,11]-2)==0
assert reduce(M2[2,13]+a**5*b)==0
assert reduce(M2[6,13]-b**6)==0
# Setting b=0 reduces rank(M2) to a 2x2; its determinant is 2(a e^5+1).
minor=sp.det(M2.extract([0,1],[11,13])).subs({b:0})
assert reduce(minor-2*(a*e**5+1))==0
M3=(M2.xreplace({z:z**5 for z in par})*M).applyfunc(reduce)
assert reduce(M3[0,13]+b**31)==0
assert all(M3[i,j]==0 for i in range(g) for j in range(g) if (i,j)!=(0,13))
M4=(M3.xreplace({z:z**5 for z in par})*M).applyfunc(reduce)
assert M4==sp.zeros(g)
# A selected 6x6 determinant controls generic rank of M.
minor6=reduce(sp.det(M.extract([0,1,7,4,2,6],[4,7,11,13,10,12])))
Delta=a*e+2*a**2*b-b**2
assert minor6!=0 and reduce(minor6.subs({e:(b**2-2*a**2*b)/a}))==0

def rank5(A):
    A=[list(map(lambda z:int(z)%5,row)) for row in A]
    rows=len(A);cols=len(A[0]);r=0
    for col in range(cols):
        pivot=next((j for j in range(r,rows) if A[j][col]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][col],-1,5)
        A[r]=[(q*inv)%5 for q in A[r]]
        for j in range(r+1,rows):
            mul=A[j][col]
            if mul: A[j]=[(u-mul*v)%5 for u,v in zip(A[j],A[r])]
        r+=1
        if r==rows:break
    return r

def matmul5(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%5 for j in range(len(B[0]))] for i in range(len(A))]
# Exhaustive independent finite-field profile test for all 5^5 coefficient choices.
fn=sp.lambdify(par,M,'math') if False else None
entries=[[sp.Poly(M[i,j],*par,modulus=5) for j in range(g)] for i in range(g)]
def eval5(vals):
    subs=dict(zip(par,vals))
    return [[int(entries[i][j].eval(subs))%5 for j in range(g)] for i in range(g)]
def predicted(vals):
    aa,bb,cc,ee,ff=vals
    delta=(aa*ee+2*aa*aa*bb-bb*bb)%5
    r1=6 if delta else (4 if aa==bb==ee==0 else 5)
    if bb:
        return (r1,3,1,0)
    return (r1, 1 if (aa*pow(ee,5,5)+1)%5==0 else 2,0)
counts=Counter()
for vals in itertools.product(range(5),repeat=5):
    A=eval5(vals)
    B=A
    rr=[]
    for i in range(4):
        rr.append(rank5(B))
        if rr[-1]==0: break
        B=matmul5(A,B)
    tup=tuple(rr)
    assert tup==predicted(vals), (vals,tup,predicted(vals))
    counts[tup]+=1
assert counts=={
    (6,3,1,0):2100,(5,3,1,0):400,(6,2,0):300,
    (5,2,0):200,(6,1,0):100,(4,2,0):25}
print('BASIS_SIZE',len(basis))
print('SIX_MINOR',minor6)
print('FIRST_RANK_DELTA',Delta)
print('SECOND_RANK_B0_MINOR',reduce(minor))
print('THIRD_POWER_ONLY_NONZERO',M3[0,13])
print('FOURTH_POWER_ZERO',M4==sp.zeros(g))
print('EXHAUSTIVE_F5',sum(counts.values()),sorted(counts.items(),reverse=True))
print('ALL_CHECKS_PASSED')

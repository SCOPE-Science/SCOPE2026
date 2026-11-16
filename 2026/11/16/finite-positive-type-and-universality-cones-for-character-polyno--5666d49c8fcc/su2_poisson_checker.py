#!/usr/bin/env python3
"""Exact finite algebra tests for character-polynomial Abel kernel formulas.

Tests are supplementary; the infinite positivity criterion is proved analytically.
Only the Python standard library is used.
"""
from fractions import Fraction as F
import random

CHECKS=0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)

def a(k, r):
    return (k+1)*r**k

def coefficient(n, b, r):
    d=len(b)-1
    return sum((b[j]*sum((a(abs(n-j)+2*h,r) for h in range(min(n,j)+1)),F(0)) for j in range(d+1)), F(0))

def slope(b,r):
    return sum((b[j]*sum((r**(-j+2*h) for h in range(j+1)),F(0)) for j in range(len(b))),F(0))

def determinant(M):
    M=[row[:] for row in M]; n=len(M); out=F(1)
    for col in range(n):
        k=next((i for i in range(col,n) if M[i][col]),None)
        if k is None:return F(0)
        if k!=col: M[k],M[col]=M[col],M[k];out=-out
        p=M[col][col];out*=p
        for i in range(col+1,n):
            t=M[i][col]/p
            for j in range(col,n):M[i][j]-=t*M[col][j]
    return out

rng=random.Random(26081114)
for r in (F(1,3),F(2,5),F(5,7)):
    for d in range(1,10):
        for _ in range(5):
            b=[F(rng.randrange(-7,8),rng.randrange(1,9)) for _ in range(d+1)]
            S=slope(b,r); lead=coefficient(d-1,b,r)
            for n in range(d-1,3*d+12):
                check(coefficient(n,b,r)==r**(n-d+1)*lead+(n-d+1)*r**n*S, f'tail failure r={r},d={d},n={n}')
        matrix=[]
        for i in range(d):
            matrix.append([coefficient(i,[F(int(k==j)) for k in range(d+1)],r) for j in range(d+1)])
        matrix.append([slope([F(int(k==j)) for k in range(d+1)],r) for j in range(d+1)])
        check(determinant(matrix)!=0, f'coordinate system singular at d={d}, r={r}')

# Degree two, r=1/2: a strictly PD but nonuniversal extreme ray
r=F(1,2); b=[F(1,12),F(-1,3),F(1,3)]
check([coefficient(0,b,r),coefficient(1,b,r),slope(b,r)]==[0,0,1], 'gap example')
for n in range(2,32):
    check(coefficient(n,b,r)==F(n-1)*r**n,'gap tail')
# Degree two, a universal kernel on the asymptotic-slope facet
b=[F(11,12),F(1,3),F(-1,3)]
check([coefficient(0,b,r),coefficient(1,b,r),slope(b,r)]==[1,1,0], 'universal facet')
for n in range(1,32):
    check(coefficient(n,b,r)==r**(n-1),'universal facet tail')

# Analytic function versus character expansion (finite high precision check).
def U(n,x):
    if n==0:return F(1)
    u0,u1=F(1),2*x
    for _ in range(1,n):u0,u1=u1,2*x*u1-u0
    return u1
for x in (F(-1),F(-2,3),F(0),F(1,2),F(1)):
    r=F(1,3);b=[F(2),F(-1,3),F(2,5)]
    den=1-2*r*x+r*r
    target=(1-r*r)/(den*den)*sum((v*U(j,x) for j,v in enumerate(b)),F(0))
    partial=sum((coefficient(n,b,r)*U(n,x) for n in range(130)),F(0))
    check(abs(target-partial)<F(1,10**48),'pointwise series')

print(f'PASS {CHECKS} supplementary exact comparisons')

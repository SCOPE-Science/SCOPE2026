#!/usr/bin/env python3
"""Independent finite-subspace and orthogonal-group checks of averaging rank formula.
For prime q; the structural classification itself is over arbitrary fields.
"""
from itertools import combinations, product
from fractions import Fraction
from math import prod

def rref_spaces(q,m,r):
    for pivots in combinations(range(m),r):
        free=[(i,j) for i,p in enumerate(pivots) for j in range(p+1,m) if j not in pivots]
        for vals in product(range(q),repeat=len(free)):
            A=[[0]*m for _ in range(r)]
            for i,p in enumerate(pivots):A[i][p]=1
            for (i,j),v in zip(free,vals):A[i][j]=v
            yield A

def determinant(A,q):
    n=len(A)
    if not n:return 1
    M=[list(row) for row in A];d=1
    for j in range(n):
        k=next((i for i in range(j,n) if M[i][j]%q),None)
        if k is None:return 0
        if k!=j:M[j],M[k]=M[k],M[j];d=-d
        a=M[j][j]%q;d=d*a%q;inv=pow(a,-1,q)
        for i in range(j+1,n):
            c=M[i][j]*inv%q
            for h in range(j,n):M[i][h]=(M[i][h]-c*M[j][h])%q
    return d%q

def inner(u,v,B,q):return sum(u[i]*B[i][j]*v[j] for i in range(len(u)) for j in range(len(v)))%q

def subspace_counts(q,B):
    m=len(B);ND=[];TI=[]
    for r in range(m+1):
        nd=iso=0
        for U in rref_spaces(q,m,r):
            G=[[inner(u,v,B,q) for v in U] for u in U]
            if determinant(G,q):nd+=1
            if all(v==0 for row in G for v in row):iso+=1
        ND.append(nd);TI.append(iso)
    return ND,TI

def orth_order(s,delta,q):
    if s==0:return 1
    h=s//2
    if s%2:return 2*q**(h*h)*prod(q**(2*i)-1 for i in range(1,h+1))
    sign= (1 if q%4==1 or h%2==0 else -1)*delta
    return 2*q**(h*(h-1))*(q**h-sign)*prod(q**(2*i)-1 for i in range(1,h))

def char(a,q):
    return 0 if a%q==0 else (1 if pow(a%q,(q-1)//2,q)==1 else -1)

def odd_formulas(q,B):
    m=len(B);delta=char(determinant(B,q),q)
    O=orth_order(m,delta,q)
    ND=[1]+[int(sum(Fraction(O,orth_order(r,d,q)*orth_order(m-r,delta*d,q)) for d in (1,-1))) for r in range(1,m)]+[1]
    TI=[1]
    for r in range(1,m+1):
        if 2*r>m:TI.append(0);continue
        numerator=1
        for j in range(r):
            s=m-2*j;d=delta*((-1)**j if q%4==3 else 1)
            nu=q**(s-1)-1
            if s%2==0:
                sign=d*((-1)**(s//2) if q%4==3 else 1)
                nu+=(q-1)*q**(s//2-1)*sign
            numerator*=nu
        denominator=prod(q**i-1 for i in range(1,r+1))
        assert numerator%denominator==0
        TI.append(numerator//denominator)
    return ND,TI

def rank_hist(q,m,ND,TI):
    a=[0]*(m+3);a[0]=1;a[1]=q**(m+1)
    for r,n in enumerate(ND):a[r+2]+=n*q**(m-r)
    a[2]+=TI[1]*q**(m+1)
    for r in range(2,m//2+1):a[r+1]+=TI[r]*q**(r*(m-r+1))
    return a

cases=[(2,[[0,1],[1,0]],[1,8,28,0,1]),(3,[[0,1],[1,0]],[1,27,63,6,1]),(3,[[1,0],[0,1]],[1,27,9,12,1]),(2,[[1,0,0],[0,1,0],[0,0,1]],[1,16,56,16,8,1]),(3,[[1,0,0],[0,1,0],[0,0,1]],[1,81,351,81,27,1])]
for q,B,expected in cases:
    nd,ti=subspace_counts(q,B)
    if q%2:assert (nd,ti)==odd_formulas(q,B),(q,B,nd,ti,odd_formulas(q,B))
    got=rank_hist(q,len(B),nd,ti)
    assert got==expected,(q,B,got,expected)
    print(f'q={q} m={len(B)} Gram={B} nondegenerate={nd} totally_isotropic={ti} ranks={got} total={sum(got)}')
print('FINITE_SUBSPACE_AND_ORTHOGONAL_FORMULAS_OK')

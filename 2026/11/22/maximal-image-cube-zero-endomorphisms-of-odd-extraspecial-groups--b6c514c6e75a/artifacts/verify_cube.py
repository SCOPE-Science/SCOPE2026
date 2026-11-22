#!/usr/bin/env python3
"""Reproduce maximal-image cube-zero endomorphism counts from matrix operations.
For the odd-prime Heisenberg group, matrices model the singular endomorphism
block after the canonical central-coordinate adjustment. The additional
characteristic-two cases are linear Lie-algebra test instances only.
"""
from itertools import product
from math import prod

def rank(rows,p):
    if not rows: return 0
    m=[list(map(lambda t:t%p,row)) for row in rows]
    h=len(m);w=len(m[0]);r=0
    for c in range(w):
        k=next((i for i in range(r,h) if m[i][c]),None)
        if k is None: continue
        m[r],m[k]=m[k],m[r]
        inv=pow(m[r][c],-1,p)
        m[r]=[(x*inv)%p for x in m[r]]
        for i in range(h):
            if i!=r and m[i][c]:
                factor=m[i][c]
                m[i]=[(a-factor*b)%p for a,b in zip(m[i],m[r])]
        r+=1
        if r==h:break
    return r

def mul(A,B,p):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def mat_vec(A,v,p):
    return [sum(a*b for a,b in zip(row,v))%p for row in A]

def independent_count(n,p):
    dim=2*n
    J=[[0]*dim for _ in range(dim)]
    for i in range(n): J[i][n+i]=1;J[n+i][i]=p-1
    result=0; suitable=0
    # Enumerate full matrices, no use of Lagrangian/extension formula.
    for ent in product(range(p),repeat=dim*dim):
        A=[ent[i*dim:(i+1)*dim] for i in range(dim)]
        if rank(A,p)!=n: continue
        JA=mul(J,A,p)
        if any(sum(A[k][i]*JA[k][j] for k in range(dim))%p for i in range(dim) for j in range(dim)):continue
        A2=mul(A,A,p);A3=mul(A2,A,p)
        if any(v for row in A3 for v in row):continue
        suitable+=1
        for ell in product(range(p),repeat=dim):
            if any(sum(ell[k]*A2[k][j] for k in range(dim))%p for j in range(dim)):continue
            if rank([list(row) for row in A]+[list(ell)],p)==n+1:
                result+=1
    return result,suitable

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    num=prod(q**(n-i)-1 for i in range(k))
    den=prod(q**(k-i)-1 for i in range(k))
    return num//den

def expected(n,q):
    lagrangians=prod(q**i+1 for i in range(1,n+1))
    total=0; stratum={}
    for s in range(n//2+1):
        # Square-zero endomorphisms B of an n-space having rank s.
        B=gaussian(n,s,q)*gaussian(n-s,s,q)*prod(q**s-q**i for i in range(s))
        extensions=q**(n*s)*prod(q**n-q**i for i in range(n-s))
        linearforms=q**(2*n-s)-q**n
        stratum[s]=lagrangians*B*extensions*linearforms
        total+=stratum[s]
    return total,stratum

for n,q in [(1,3),(1,5),(2,2)]:
    found,mats=independent_count(n,q)
    want,parts=expected(n,q)
    print('n,p',n,q,'expected',want,'observed',found,'qualifying_A',mats,'summands',parts,flush=True)
    assert found==want
for n,q in [(2,3),(3,3),(4,5)]:
    print('symbolic summand reconstruction',n,q,expected(n,q),flush=True)
print('MAXIMAL_CUBE_NILPOTENCE_VERIFIED',flush=True)

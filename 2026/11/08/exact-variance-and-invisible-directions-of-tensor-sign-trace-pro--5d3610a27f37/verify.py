#!/usr/bin/env python3
"""Exact finite checks for tensor-sign trace variance and nullspace structure.
Uses Python 3 standard library, exact integer and rational arithmetic."""
from itertools import product, combinations
from random import Random
from fractions import Fraction
from math import prod

def labels(dims):
    return list(product(*(range(d) for d in dims)))

def classes(dims):
    idx=labels(dims)
    groups={}
    for a,b in combinations(range(len(idx)),2):
        label=tuple(None if idx[a][j]==idx[b][j] else tuple(sorted((idx[a][j],idx[b][j]))) for j in range(len(dims)))
        groups.setdefault(label,[]).append((a,b))
    return groups

def cvals(A,groups):
    return {key:2*sum(A[a][b] for a,b in pairs) for key,pairs in groups.items()}

def predicted_var(A,groups):
    return sum(v*v for v in cvals(A,groups).values())

def predicted_distance(A,groups):
    return sum(Fraction(c*c,2*len(groups[key])) for key,c in cvals(A,groups).items())

def exhaustive_variance(A,dims):
    idx=labels(dims)
    m=sum(dims); N=len(idx)
    q=[]
    for signs in product((-1,1),repeat=m):
        block=[];i=0
        for d in dims:
            block.append(signs[i:i+d]);i+=d
        v=[prod(block[j][a[j]] for j in range(len(dims))) for a in idx]
        q.append(sum(A[a][b]*v[a]*v[b] for a in range(N) for b in range(N)))
    mean=Fraction(sum(q),len(q))
    variance=sum((x-mean)**2 for x in q)/len(q)
    return mean, variance

def projector(A,groups):
    B=[list(map(Fraction,row)) for row in A]
    for pairs in groups.values():
        avg=Fraction(sum(A[a][b] for a,b in pairs),len(pairs))
        for a,b in pairs:B[a][b]-=avg;B[b][a]-=avg
    return B

def normdiff2(A,B):
    N=len(A)
    return sum((Fraction(A[i][j])-Fraction(B[i][j]))**2 for i in range(N) for j in range(N))

checks=0
rng=Random(190417)
for dims in ((2,2),(2,3),(3,2),(2,2,2),(2,3,2)):
    idx=labels(dims);N=len(idx);groups=classes(dims)
    M=prod(1+d*(d-1)//2 for d in dims)
    assert len(groups)==M-1;checks+=1
    assert sum(map(len,groups.values()))==N*(N-1)//2;checks+=1
    for key,pairs in groups.items():
        J=sum(v is not None for v in key)
        expected=2**(J-1)*prod(dims[i] for i in range(len(dims)) if key[i] is None)
        assert len(pairs)==expected;checks+=1
    for rep in range(6):
        A=[[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(i,N):
                A[i][j]=A[j][i]=rng.randrange(-4,5)
        avg,variance=exhaustive_variance(A,dims)
        assert avg==sum(A[i][i] for i in range(N));checks+=1
        assert variance==predicted_var(A,groups);checks+=1
        B=projector(A,groups)
        assert normdiff2(A,B)==predicted_distance(A,groups);checks+=1
        assert predicted_var(B,groups)==0;checks+=1
        assert exhaustive_variance(B,dims)[1]==0;checks+=1

# Exact two-factor PSD sign-cancellation and addition witnesses.
N=4
for sign in (-1,1):
    K=[[0]*N for i in range(N)]
    # label order (11),(12),(21),(22), zero-based: 0,1,2,3.
    K[0][3]=K[3][0]=1
    K[1][2]=K[2][1]=sign
    assert [[sum(K[i][t]*K[t][j] for t in range(N)) for j in range(N)] for i in range(N)]==[[int(i==j) for j in range(N)] for i in range(N)];checks+=1
    A=[[Fraction(int(i==j))+Fraction(1,2)*K[i][j] for j in range(N)] for i in range(N)]
    # Since K symmetric and K^2=I, A has eigenvalues 1/2 and 3/2, hence SPD.
    rv=exhaustive_variance(A,(2,2))[1]
    full_rv=4*sum(A[i][j]**2 for i in range(N) for j in range(i+1,N))
    assert rv==(Fraction(0) if sign==-1 else Fraction(4));checks+=1
    assert full_rv==Fraction(2);checks+=1
    assert rv==predicted_var(A,classes((2,2)));checks+=1

# Explicit basis gives independent coefficients, so rank M-1.
for dims in ((2,2),(2,3),(2,2,2),(3,3)):
    N=prod(dims);groups=classes(dims)
    labels_coeff=[]
    for g in groups.values():
        i,j=g[0];A=[[0]*N for _ in range(N)];A[i][j]=A[j][i]=1
        c=cvals(A,groups)
        assert sum(v!=0 for v in c.values())==1;checks+=1
        labels_coeff.append(tuple(c.values()))
    assert len(labels_coeff)==prod(1+d*(d-1)//2 for d in dims)-1;checks+=1
    kernel_dimension=N*(N+1)//2-len(groups)
    assert kernel_dimension>=N;checks+=1
print(f'PASS: {checks} exact integer/rational assertions; domains (2,2),(2,3),(3,2),(2,2,2),(2,3,2), plus rank tests (3,3).')

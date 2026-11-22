#!/usr/bin/env python3
"""Reproducible finite-field checks for isotropic-image Nijenhuis theorem.
Only the elementary prime fields F_3 and F_5 are used; the theorem is symbolic.
"""
from itertools import product
from math import prod


def qbin(n,k,q):
    if k < 0 or k > n: return 0
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def surj(n,r,q): return prod(q**n-q**i for i in range(r))

def isozero(d,q,eps):
    if d < 1: return 0
    if d%2: return q**(d-1)-1
    return q**(d-1)-1+eps*(q-1)*q**(d//2-1)

def isotropic_numbers(n,q,eps=1):
    a=[1]
    for r in range(1,n//2+1):
        t=isozero(n-2*r+2,q,eps)
        if t==0: break
        assert a[-1]*t%(q**r-1)==0
        a.append(a[-1]*t//(q**r-1))
    return a

def h_exact_image(n,q,r,j):
    def endom(w,j): return qbin(w,j,q)*surj(w,w-j,q)
    return sum(qbin(r,w,q)*(-1)**(r-w)*q**((r-w)*(r-w-1)//2)
               *q**(w*(n-w))*endom(w,j) for w in range(j,r+1))

def rank_census(n,q,eps=1):
    i_numbers=isotropic_numbers(n,q,eps)
    out=[0]*(n+2)
    for r,I in enumerate(i_numbers):
        s=surj(n,r,q)
        out[r]+=I*s*q**r
        out[r+1]+=I*s*(q**n-q**r)
        for j in range(r+1):
            z=h_exact_image(n,q,r,j)
            assert z>=0
            out[n+1-j]+=(q-1)*q**n*I*z
    assert sum(out)==q**(n+1)*sum(I*surj(n,r,q) for r,I in enumerate(i_numbers))
    return i_numbers,out

def rank(matrix,p):
    A=[list(row) for row in matrix]
    if not A: return 0
    i=0; cols=len(A[0])
    for j in range(cols):
        pivot=next((r for r in range(i,len(A)) if A[r][j]%p),None)
        if pivot is None: continue
        A[i],A[pivot]=A[pivot],A[i]
        inv=pow(A[i][j]%p,-1,p)
        A[i]=[(x*inv)%p for x in A[i]]
        for r in range(len(A)):
            if r!=i:
                v=A[r][j]%p
                A[r]=[(x-v*y)%p for x,y in zip(A[r],A[i])]
        i+=1
        if i==len(A): break
    return i

def bil(x,y,B,p):
    n=len(B)
    return sum(x[i]*B[i][j]*y[j] for i in range(n) for j in range(n))%p

def nij_identity(N,B,p):
    n=len(B); d=n+1
    def M(x,y):return [0]*n+[bil(x,y,B,p)]
    def L(x):return [sum(N[i][j]*x[j] for j in range(d))%p for i in range(d)]
    basis=[[int(i==j) for i in range(d)] for j in range(d)]
    for x in basis:
        for y in basis:
            Nx,Ny=L(x),L(y)
            lhs=M(Nx,Ny)
            z1,z2,z3=M(Nx,y),M(x,Ny),L(M(x,y))
            arg=[(z1[i]+z2[i]-z3[i])%p for i in range(d)]
            if lhs!=L(arg):return False
    return True

def predicted(N,B,p):
    n=len(B); a=N[n][n]
    if any(N[i][n]%p for i in range(n)):return False
    S=[[((N[i][j]-(a if i==j else 0))%p) for j in range(n)] for i in range(n)]
    cols=[[S[i][j] for i in range(n)] for j in range(n)]
    return all(bil(x,y,B,p)==0 for x in cols for y in cols)

def matrix_from_flat(flat,d):return [flat[i*d:(i+1)*d] for i in range(d)]

def rref_bases(n,r,p):
    for pivots in __import__('itertools').combinations(range(n),r):
        free=[(i,j) for i,c in enumerate(pivots) for j in range(c+1,n) if j not in pivots]
        for vals in product(range(p),repeat=len(free)):
            A=[[0]*n for _ in range(r)]
            for i,c in enumerate(pivots): A[i][c]=1
            for (i,j),v in zip(free,vals): A[i][j]=v
            yield A

def verify():
    for p,B,eps in [(3,[[0,1],[1,0]],1),(3,[[1,0],[0,1]],-1),(5,[[0,1],[1,0]],1)]:
        n=2; d=n+1; observed=[0]*(d+1); accepted=0
        for v in product(range(p),repeat=d*d):
            N=matrix_from_flat(v,d)
            satisfies=nij_identity(N,B,p)
            normal=predicted(N,B,p)
            assert satisfies==normal,('equivalence failure',p,B,N)
            if satisfies:
                accepted+=1;observed[rank(N,p)]+=1
        I,expected=rank_census(n,p,eps)
        assert observed==expected,(p,B,observed,expected)
        print('exhaustive_all_operators',p,B,'accepted',accepted,'ranks',observed)
    n=3; p=3; B=[[int(i==j) for j in range(n)] for i in range(n)]
    # For n=3 enumerate all generator blocks S (3^9 possibilities) and
    # recover rank counts with the exact number of possible lower rows phi.
    counts=[0]*(n+2); num_s=0
    for flat in product(range(p),repeat=n*n):
        S=matrix_from_flat(flat,n)
        cols=[[S[i][j] for i in range(n)] for j in range(n)]
        if any(bil(x,y,B,p) for x in cols for y in cols):continue
        num_s+=1
        r=rank(S,p)
        counts[r]+=p**r
        counts[r+1]+=p**n-p**r
        for a in range(1,p):
            T=[[ (S[i][j]+(a if i==j else 0))%p for j in range(n)] for i in range(n)]
            counts[1+rank(T,p)]+=p**n
    I,exp=rank_census(n,p)
    assert counts==exp
    print('exhaustive_S_n3_F3',num_s,'isotropic_subspaces',I,'ranks',counts)
    # Direct original identities on a deterministic sample of n=3 maps.
    examples=0
    for flat in product(range(p),repeat=9):
        S=matrix_from_flat(flat,3)
        for a in [0,1,2]:
            N=[[ (S[i][j]+(a if i==j else 0))%p for j in range(3)]+[0] for i in range(3)]
            N.append([1,2,1,a])
            assert nij_identity(N,B,p)==predicted(N,B,p)
        examples+=1
        if examples==1000:break
    print('n3_original_equation_pairs',examples*3)
    for B,eps in [([[int(i==j) for j in range(4)] for i in range(4)],1),
                  ([[2 if i==j==3 else int(i==j) for j in range(4)] for i in range(4)],-1)]:
        observed=[1]
        for r in (1,2):
            c=0
            for U in rref_bases(4,r,3):
                if all(bil(x,y,B,3)==0 for x in U for y in U):c+=1
            observed.append(c)
        theory=isotropic_numbers(4,3,eps)
        assert observed[:len(theory)]==theory and all(x==0 for x in observed[len(theory):])
        print('n4_isotropic_subspaces',eps,observed,'rank_census',rank_census(4,3,eps)[1])
    print('ISOTROPIC_NIJENHUIS_VERIFIED')

if __name__=='__main__':verify()

#!/usr/bin/env python3
"""Finite-field direct checks for square-zero endomorphisms of the 2-step free associative algebra.
The algebra has the word basis of lengths one and two, and every word of length >=3 is zero.
No external libraries are used. All test results are deterministic.
"""
from itertools import product
from math import prod


def matrix_rank(A,p):
    if not A: return 0
    B=[list(row) for row in A]
    rows=len(B);cols=len(B[0]); k=0
    for j in range(cols):
        pivot=next((i for i in range(k,rows) if B[i][j]%p),None)
        if pivot is None: continue
        B[k],B[pivot]=B[pivot],B[k]
        z=pow(B[k][j]%p,-1,p)
        B[k]=[(v*z)%p for v in B[k]]
        for i in range(rows):
            if i==k: continue
            t=B[i][j]%p
            if t: B[i]=[(B[i][h]-t*B[k][h])%p for h in range(cols)]
        k+=1
        if k==rows: break
    return k


def mul(A,B,p):
    rows=len(A); inner=len(B); cols=len(B[0]);
    return [[sum(A[i][k]*B[k][j] for k in range(inner))%p for j in range(cols)] for i in range(rows)]


def tensor(T):
    m=len(T)
    return [[T[i][j]*T[a][b] for j in range(m) for b in range(m)] for i in range(m) for a in range(m)]


def polynomial(m,p):
    def gauss(n,k):
        if k<0 or k>n:return 0
        return prod(p**(n-i)-1 for i in range(k))//prod(p**(k-i)-1 for i in range(k))
    counts={}
    for r in range(m//2+1):
        a=m-2*r; b=m*m-2*r*r
        H=m**3-r*m*m-m*r*r+2*r**3
        Q=gauss(m,r)*gauss(m-r,r)*prod(p**r-p**i for i in range(r))
        for s in range(a+1):
            w=Q*p**(H-a*b)*gauss(a,s)*prod(p**b-p**i for i in range(s))
            k=r+r*r+s
            counts[k]=counts.get(k,0)+w
    return dict(sorted(counts.items()))


def square_zero(T,p):
    return not any(v%p for row in mul(T,T,p) for v in row)


def direct(m,p):
    result={}
    dim=m+m*m
    unit=[tuple(int(i==j) for j in range(m)) for i in range(m)]
    Ts=[ [list(a[i*m:(i+1)*m]) for i in range(m)] for a in product(range(p),repeat=m*m)]
    for T in Ts:
        if not square_zero(T,p): continue
        U=[[v%p for v in row] for row in tensor(T)]
        for flat in product(range(p),repeat=m**3):
            S=[list(flat[i*m:(i+1)*m]) for i in range(m*m)]
            left=mul(S,T,p); right=mul(U,S,p)
            if any((left[i][j]+right[i][j])%p for i in range(m*m) for j in range(m)):
                continue
            Phi=[T[i]+[0]*(m*m) for i in range(m)]+[S[i]+U[i] for i in range(m*m)]
            assert not any(v%p for row in mul(Phi,Phi,p) for v in row)
            # Check the original multiplication on every ordered pair of word basis vectors.
            # Product of two length-one words is their concatenation; all other products vanish.
            for i in range(m):
                for j in range(m):
                    # Image of the word ij is tensor of images of letters i and j.
                    for u in range(m*m):
                        assert Phi[m+u][m+i*m+j]%p == (T[u//m][i]*T[u%m][j])%p
            rk=matrix_rank(Phi,p)
            result[rk]=result.get(rk,0)+1
    return dict(sorted(result.items()))


def linear_equation_dimension(m,p):
    seen={}
    for flat in product(range(p),repeat=m*m):
        T=[list(flat[i*m:(i+1)*m]) for i in range(m)]
        if not square_zero(T,p):continue
        r=matrix_rank(T,p)
        U=[[v%p for v in row] for row in tensor(T)]
        cols=[]
        for a in range(m*m):
            for b in range(m):
                S=[[0]*m for _ in range(m*m)];S[a][b]=1
                ST=mul(S,T,p);US=mul(U,S,p)
                cols.append([(ST[i][j]+US[i][j])%p for i in range(m*m) for j in range(m)])
        L=list(map(list,zip(*cols)))
        H=m**3-matrix_rank(L,p)
        expected=m**3-r*m*m-m*r*r+2*r**3
        assert H==expected,(m,p,r,H,expected)
        seen[r]=seen.get(r,0)+1
    return seen

if __name__=='__main__':
    for m,p in [(2,2),(2,3)]:
        actual=direct(m,p); expected=polynomial(m,p)
        assert actual==expected,(m,p,actual,expected)
        print(f'DIRECT m={m} q={p} ranks={actual} total={sum(actual.values())} PASS')
    for m,p in [(2,2),(2,3),(3,2),(3,3)]:
        seen=linear_equation_dimension(m,p)
        expected=polynomial(m,p)
        print(f'LINEAR_KERNEL m={m} q={p} matrix_rank_strata={seen} polynomial={expected} PASS')
    print('FREE_TWO_STEP_SQUARE_ZERO_ENDOMORPHISM_RANK_POLYNOMIAL_OK')

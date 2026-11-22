#!/usr/bin/env python3
"""Independent two-method finite-field rank enumeration for sums of rook matrices."""
from itertools import permutations, combinations
from collections import defaultdict, Counter
from fractions import Fraction
from math import factorial

def rook_matrices(n):
    out=[]
    for r in range(n+1):
        for rows in combinations(range(n),r):
            for cols in combinations(range(n),r):
                for perm in permutations(cols):
                    A=[[0]*n for _ in range(n)]
                    for i,j in zip(rows,perm): A[i][j]=1
                    out.append(A)
    return out

def mat_rank(a,p):
    m=[row[:] for row in a]; n=len(m);rank=0
    for c in range(n):
        pivot=next((i for i in range(rank,n) if m[i][c]%p),None)
        if pivot is None:continue
        m[rank],m[pivot]=m[pivot],m[rank]
        d=pow(m[rank][c],-1,p)
        for k in range(c,n):m[rank][k]=(m[rank][k]*d)%p
        for i in range(rank+1,n):
            v=m[i][c]
            if v:
                for k in range(c,n):m[i][k]=(m[i][k]-v*m[rank][k])%p
        rank+=1
    return rank

def predicted(n,p):
    # Coefficients of exp(E(x,y,u)) as exact rationals.
    terms=defaultdict(Fraction)
    terms[(1,0,0)]+=1;terms[(0,1,0)]+=1
    for k in range(1,n+1):
        terms[(k,k,k)]+=2 # paths with equal row and column counts
        if k+1<=n:
            terms[(k+1,k,k)]+=1
            terms[(k,k+1,k)]+=1
        defect= int(p==2 or k%2==0)
        terms[(k,k,k-defect)]+=Fraction(1,k)
    ans={(0,0,0):Fraction(1)}
    for j in range(1,n+1):
        # x^0 terms are exp(y), hence 1/j! at rank zero
        ans[(0,j,0)]=Fraction(1,factorial(j))
    for i in range(1,n+1):
        for j in range(n+1):
            for r in range(n+1):
                v=Fraction(0)
                for (a,b,s),c in terms.items():
                    if 1<=a<=i and b<=j and s<=r:
                        v+=a*c*ans.get((i-a,j-b,r-s),0)
                if v:ans[(i,j,r)]=v/i
    counts={r:int(ans.get((n,n,r),0)*factorial(n)**2) for r in range(n+1)}
    return counts

def brute(n,p):
    mats=rook_matrices(n); ans=Counter()
    for a in mats:
        for b in mats:
            ans[mat_rank([[(a[i][j]+b[i][j])%p for j in range(n)] for i in range(n)],p)]+=1
    return dict(ans),len(mats)

if __name__=='__main__':
    for n in range(1,5):
        for p in (2,3):
            observed, size=brute(n,p)
            expected=predicted(n,p)
            assert all(observed.get(j,0)==expected.get(j,0) for j in range(n+1)), (n,p,observed,expected)
            assert sum(expected.values())==size**2
            print(f'n={n},char={p},|R_n|={size},rank_distribution={expected}: PASS')
    for n in range(5,9):
        for p in (2,3):
            expected=predicted(n,p)
            size=sum(__import__('math').comb(n,j)**2*factorial(j) for j in range(n+1))
            assert sum(expected.values())==size**2,(n,p)
            print(f'n={n},char={p},rank_polynomial_total={size**2},invertible_count={expected[n]}: PASS')

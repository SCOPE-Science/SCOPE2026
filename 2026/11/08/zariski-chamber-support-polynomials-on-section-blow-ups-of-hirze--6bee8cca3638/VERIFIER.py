"""Exact integer-matrix check of chamber-support polynomial for section blow-ups.
No external packages required. The matrix enumerator uses rational LDL pivots rather
than the closed Schur-complement inequalities from the proof.
"""
from fractions import Fraction
from math import comb
from collections import Counter

def predicted(e, n):
    r = n-e
    v = Counter()
    for j in range(n+1):
        v[j] += comb(n,j)*2**j
    for cap in (e,r):
        for k in range(cap):
            for j in range(n-k+1):
                v[1+k+j] += comb(n,k)*comb(n-k,j)
    for f in range(e):
        for a in range(r):
            v[2+f+a] += comb(n,f)*comb(n-f,a)
    return tuple(v[i] for i in range(n+3))

def matrix(e, n):
    r=n-e
    m=2*n+2
    A=[[0]*m for _ in range(m)]
    # C0 and C+ at positions 0,1, then E_i, F_i' in adjacent pairs
    A[0][0]=-e
    A[1][1]=-r
    for i in range(n):
        E,F=2+2*i,3+2*i
        A[E][E]=A[F][F]=-1
        A[E][F]=A[F][E]=1
        A[0][F]=A[F][0]=1
        A[1][E]=A[E][1]=1
    return A

def neg_def(M, subset):
    # Rational LDL decomposition of -M; strictly positive diagonal pivots.
    p=len(subset)
    B=[[-M[i][j] for j in subset] for i in subset]
    for k in range(p):
        d=B[k][k]
        if d<=0:
            return False
        for i in range(k+1,p):
            for j in range(i,p):
                B[j][i] = B[i][j] = B[i][j] - Fraction(B[i][k]*B[j][k],d)
    return True

def exhaustive(e,n):
    M=matrix(e,n)
    N=2*n+2
    count=Counter()
    for mask in range(1<<N):
        supp=[i for i in range(N) if (mask>>i)&1]
        if neg_def(M,supp):
            count[len(supp)] += 1
    return tuple(count[i] for i in range(n+3))

def main():
    for n in range(3,7):
        for e in range(1,n):
            actual=exhaustive(e,n)
            expected=predicted(e,n)
            assert actual==expected,(e,n,actual,expected)
            assert expected==predicted(n-e,n)
            max_count=sum(comb(n,f) for f in range(e))+sum(comb(n,a) for a in range(n-e))
            assert expected[n+1]==max_count
            assert expected[n+2]==0
            print(f'e={e} n={n} total={sum(actual)} coefficients={actual}')
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':
    main()

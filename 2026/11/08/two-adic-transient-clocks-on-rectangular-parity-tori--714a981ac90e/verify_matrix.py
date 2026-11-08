#!/usr/bin/env python3
"""Independent bit-matrix checks for the toroidal parity-update theorem.

Run: python3 verify_matrix.py. Standard library only. Each row is a GF(2)
integer bitset; multiplication and rank use Gaussian elimination over GF(2).
"""
from math import gcd


def rank(rows):
    piv = {}
    for v in rows:
        while v:
            i = v.bit_length()-1
            if i in piv:
                v ^= piv[i]
            else:
                piv[i] = v
                break
    return len(piv)


def prod(A, B):
    out = []
    for row in A:
        v = 0
        while row:
            b = row & -row
            v ^= B[b.bit_length()-1]
            row ^= b
        out.append(v)
    return out


def adj(m,n):
    # Index i*n+j; self-disjoint nearest neighbors since m,n>=3.
    A=[]
    for i in range(m):
        for j in range(n):
            v=0
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                v ^= 1 << (((i+di)%m)*n + ((j+dj)%n))
            A.append(v)
    return A


def c_pred(m,n,t):
    mm,nn=m,n
    a=b=1
    while mm%2==0: mm//=2; a*=2
    while nn%2==0: nn//=2; b*=2
    g=gcd(mm,nn);k=min(a,b);L=max(a,b)
    if L==1:
        return min(t,1)*(2*g-1)
    return 2*k*min(t,L//2)+2*(g-1)*k*min(t,L)


def main():
    checks=0
    largest=(0,0,0)
    for m in range(3,25):
        for n in range(3,25):
            N=m*n
            if N>260: continue
            A=adj(m,n)
            B=[1<<i for i in range(N)]
            tmax=max(m & -m,n & -n)
            for t in range(tmax+2):
                c=N-rank(B)
                assert c==c_pred(m,n,t),(m,n,t,c,c_pred(m,n,t))
                checks+=1
                if N>largest[2]:largest=(m,n,N)
                B=prod(B,A)
    print('PASS matrix-nullities: {} (m,n,t) cases; max dimension {} ({} x {})'.format(checks,largest[2],largest[0],largest[1]))
    print('PASS: direct Cayley-grid adjacency ranks agree with all predicted Fitting nullities')

if __name__=='__main__': main()

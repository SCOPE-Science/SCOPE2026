#!/usr/bin/env python3
"""Supplementary numerical checks for normalized-path low-pass dynamical sampling.

No external dependencies. The analytic inequalities, not floating-point checks,
establish the all-parameter statements.
"""
import math


def values(n, r):
    q = []
    for j in range(n+1):
        d = 1 if j in (0,n) else 2
        prod = 1.0
        for k in range(1,r):
            prod *= abs(math.cos(math.pi*j*k/n))
        q.append(d**(r/2)*prod)
    return q


def eigenvector(n, k):
    d = [1]+[2]*(n-1)+[1]
    norm = math.sqrt(2*n if k in (0,n) else n)
    return [math.sqrt(d[j])*math.cos(math.pi*k*j/n)/norm for j in range(n+1)]


def apply_B(n, v):
    d = [1]+[2]*(n-1)+[1]
    out = []
    for j in range(n+1):
        a = (v[j-1]/math.sqrt(d[j-1]) if j else 0.0)
        b = (v[j+1]/math.sqrt(d[j+1]) if j<n else 0.0)
        out.append((a+b)/math.sqrt(d[j]))
    return out


def determinant(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    prod = 1.0
    for k in range(n):
        piv = max(range(k,n),key=lambda i:abs(a[i][k]))
        if abs(a[piv][k]) < 1e-13:
            return 0.0
        if piv!=k:
            a[piv],a[k] = a[k],a[piv]
            prod = -prod
        v=a[k][k]
        prod*=v
        for i in range(k+1,n):
            u=a[i][k]/v
            for j in range(k+1,n):
                a[i][j]-=u*a[k][j]
    return prod


def verify():
    count = 0
    # Check eigenvector formula independently against tridiagonal action.
    for n in range(2,18):
        for k in range(n+1):
            v=eigenvector(n,k)
            lhs=apply_B(n,v)
            lam=math.cos(math.pi*k/n)
            assert max(abs(a-lam*b) for a,b in zip(lhs,v))<5e-13
            assert abs(sum(x*x for x in v)-1)<5e-13
            count+=1
    # Independently build the entire three-time sensing matrix from B iterations,
    # and compare its determinant with the claimed ratio by vertex.
    for n in range(2,16):
        r=3
        cols=[]
        for k in range(r):
            col=[]
            w=eigenvector(n,k)
            for t in range(r):
                col.append(w[:])
                w=apply_B(n,w)
            cols.append(col)
        base = determinant([[cols[k][t][0] for k in range(r)] for t in range(r)])
        assert abs(base)>1e-9
        q=values(n,r)
        for j in range(n+1):
            det=determinant([[cols[k][t][j] for k in range(r)] for t in range(r)])
            assert abs(abs(det/base)-q[j])<1e-8
            count+=1
    # All path sizes through 250: sharp classification for three modes.
    for n in range(2,251):
        q=values(n,3)
        maxima=[j for j,z in enumerate(q) if abs(z-max(q))<1e-9]
        assert maxima==([0,n] if n<=5 else [1,n-1]),(n,maxima)
        count+=1
    # Sufficient all-band threshold, tested near its boundary for many ranks.
    for r in range(2,15):
        k=r-1
        for n in (4*k**3,4*k**3+1):
            q=values(n,r)
            maxima=[j for j,z in enumerate(q) if abs(z-max(q))<1e-9]
            assert maxima==[1,n-1],(r,n,maxima)
            count+=1
    print('CHECK_OK eigenvectors=%d three_mode_paths=249 general_threshold_cases=26 checks=%d'%
          (sum(n+1 for n in range(2,18)),count))

if __name__=='__main__':
    verify()

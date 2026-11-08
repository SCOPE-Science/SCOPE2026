#!/usr/bin/env python3
"""Exact checks for the uniform-composition part-size precision theorem.

Uses only the Python standard library. Finite checks are diagnostics; the
proof for arbitrary sizes is supplied separately.
"""
from collections import Counter
from fractions import Fraction as F

checks = 0

def eq(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1

def parts(n, mask):
    out = []
    last = 0
    for i in range(1, n):
        if mask & (1 << (i - 1)):
            out.append(i - last)
            last = i
    out.append(n - last)
    return out

def p(r):
    return F(1, 2**(r+1))

def sigma(r, s):
    return (p(r) if r == s else F(0)) + (3-r-s)*p(r)*p(s)

def finite_cov(n,r,s):
    # Valid when n>=2*max(r,s)+1; same formula for r=s and r!=s.
    base = F(n-r+3, 2**(r+1)) if r == s else F(0)
    constant = r*r+r*s+s*s-6*r-6*s+5
    return base + F(n*(3-r-s)+constant, 2**(r+s+2))

def inverse(a):
    m=len(a)
    t=[[F(a[i][j]) for j in range(m)] + [F(i==j) for j in range(m)] for i in range(m)]
    for i in range(m):
        k=next(k for k in range(i,m) if t[k][i])
        t[i],t[k]=t[k],t[i]
        pivot=t[i][i];t[i]=[z/pivot for z in t[i]]
        for j in range(m):
            if j!=i:
                f=t[j][i]
                t[j]=[x-f*y for x,y in zip(t[j],t[i])]
    return [row[m:] for row in t]

for n in range(2,13):
    den=2**(n-1)
    sums=[0]*(n+1)
    sums2=[[0]*(n+1) for _ in range(n+1)]
    for mask in range(den):
        counts=Counter(parts(n,mask))
        for r,v in counts.items():
            sums[r]+=v
            for s,w in counts.items():
                sums2[r][s]+=v*w
    for r in range(1,n+1):
        ex=F(sums[r],den)
        if n>=r+1:
            eq(ex,F(n-r+3,2**(r+1)))
        else:
            eq(ex,F(1,den))
        for s in range(1,n+1):
            cov=F(sums2[r][s],den) - F(sums[r]*sums[s],den*den)
            if n>=2*max(r,s)+1:
                eq(cov,finite_cov(n,r,s))
            if r!=s:
                eq(cov<0, True)
    # Exact assertion of conservation of total size.
    eq(sum(r*sums[r] for r in range(1,n+1)), n*den)

for m in range(1,15):
    mat=[[sigma(i,j) for j in range(1,m+1)] for i in range(1,m+1)]
    prec=inverse(mat)
    a=F(1,2)*(1-F(1,2**m))
    d=F(m+2,2**(m+1))
    e=F(m*m+4*m+6,2**(m+1))
    delta=a*e+d*d
    for i in range(1,m+1):
        for j in range(1,m+1):
            formula=(F(1,p(i)) if i==j else F(0)) + F(a*i*j+d*(i+j)-e,delta)
            eq(prec[i-1][j-1],formula)
            if i!=j:
                eq(prec[i-1][j-1]>0, m>=3)
    for i in range(m):
        for j in range(m):
            eq(sum(mat[i][k]*prec[k][j] for k in range(m)), F(i==j))

for m in range(3,30):
    eq(2**(m+1)>m*m+m+2, True)

print('VERIFY_OK exact_assertions=',checks)

#!/usr/bin/env python3
"""Exact checks for uniform two-layer Boolean first-Walsh sampling."""
from fractions import Fraction
from itertools import product
from math import comb, isqrt

checks = 0

def require(p, msg):
    global checks
    checks += 1
    assert p, msg

def shells(n):
    return range(n+1)

def gram_parameters(n, k, ell):
    assert 0 <= k < ell <= n
    a,b = n-2*k, n-2*ell
    A,B=comb(n,k),comb(n,ell)
    mu=Fraction(A*a+B*b,A+B)
    nu=Fraction(A*a*a+B*b*b,A+B)
    r=(nu-n)/Fraction(n*(n-1))
    return mu,nu,r

def is_tight(n,k,l):
    mu,nu,_=gram_parameters(n,k,l)
    return mu==0 and nu==n

def predicted(n):
    v=set()
    s=isqrt(n)
    if s*s==n:
        k=(n-s)//2; l=(n+s)//2
        if k<l and k>=0 and l<=n and (n-s)%2==0: v.add((k,l))
    if (s+1)**2==n+1:
        # s(s+2) = n
        for a,b in ((s,s+2),(s+2,s)):
            k=(n-a)//2; l=(n+b)//2
            if 0<=k<l<=n and (n-a)%2==0 and (n+b)%2==0: v.add((k,l))
    return v

# Exhaustive exact rational classification; no floating arithmetic.
for n in range(2,101):
    actual={(k,l) for k in range(n+1) for l in range(k+1,n+1) if is_tight(n,k,l)}
    require(actual==predicted(n),(n,actual,predicted(n)))

# Independent Gram construction on all vertices, independent moment calculation.
for n in range(2,11):
    layer={k:[] for k in range(n+1)}
    for x in product((-1,1), repeat=n):
        layer[x.count(-1)].append((1,*x))
    for k in range(n+1):
        for ell in range(k+1,n+1):
            pts=layer[k]+layer[ell]
            M=len(pts)
            G=[[Fraction(sum(x[i]*x[j] for x in pts), M) for j in range(n+1)] for i in range(n+1)]
            mu,nu,r=gram_parameters(n,k,ell)
            require(all(G[0][j]==mu/Fraction(n) for j in range(1,n+1)),(n,k,ell,'linear'))
            require(all(G[i][j]==r for i in range(1,n+1) for j in range(1,n+1) if i!=j),(n,k,ell,'quadratic'))
            require(all(G[i][i]==1 for i in range(n+1)),(n,k,ell,'diagonal'))
            require(is_tight(n,k,ell)==(all(G[i][j]==int(i==j) for i in range(n+1) for j in range(n+1))),(n,k,ell,'tight'))
            if n >= 3 and is_tight(n,k,ell):
                a,b=n-2*k,2*ell-n
                measured=Fraction(sum(x[1]*x[2]*x[3] for x in pts), M)
                require(measured == Fraction(a-b,(n-1)*(n-2)),(n,k,ell,'triple'))

# Product pairing proof factorization for all tested integer divisors.
for n in range(2,601):
    for a in range(1,isqrt(n)+1):
        if n%a: continue
        b=n//a
        if (a-b)%2 or (n-a)%2: continue
        R=lambda x: Fraction((x+2)*(n-x),x*(n+x+2))
        if b==a+2:
            require(R(a)==1,('adjacent',n,a,b))
        if b>=a+4:
            r=(b-a)//2
            for t in range(a,b,2):
                v=a+b-2-t;z=t-a
                lhs=1-R(t)*R(v)
                rhs=Fraction(2*n*(a+b)*(2*(r-1)*(z+1)-z*z),t*(n+t+2)*v*(n+v+2))
                require(lhs==rhs and rhs>0,(n,a,b,t,v))

print('CHECK_OK assertions='+str(checks))

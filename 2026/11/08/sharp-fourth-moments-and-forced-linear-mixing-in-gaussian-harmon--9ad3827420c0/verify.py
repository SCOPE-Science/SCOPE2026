#!/usr/bin/env python3
"""Exact, independent diagnostics for Gaussian harmonic first/second-layer moments.

Requires only the Python standard library. The infinite-dimensional claims
and global optimizations are established by the mathematical proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial
from random import Random


def poly_product(p, q, n):
    out = {}
    for a, ca in p.items():
        for b, cb in q.items():
            e = tuple(a[i] + b[i] for i in range(n))
            out[e] = out.get(e, Q(0)) + ca*cb
    return {k: v for k, v in out.items() if v}


def gaussian_integral(p):
    ans = Q(0)
    for multi, c in p.items():
        if any(k % 2 for k in multi):
            continue
        t = Q(1)
        for k in multi:
            t *= factorial(k) // (2**(k//2)*factorial(k//2))
        ans += c*t
    return ans


def moments_by_direct_expansion(A, b):
    n=len(b)
    z=(0,)*n
    p={z: Q(-sum(A[i][i] for i in range(n)))}
    for i in range(n):
        e=tuple(int(j==i) for j in range(n))
        p[e]=p.get(e,Q(0))+Q(b[i])
        for j in range(n):
            f=tuple(int(k==i)+int(k==j) for k in range(n))
            p[f]=p.get(f,Q(0))+Q(A[i][j])
    p={k:v for k,v in p.items() if v}
    p2=poly_product(p,p,n)
    return gaussian_integral(p2),gaussian_integral(poly_product(p2,p2,n))


def traces(A,b):
    n=len(b)
    square=[[sum(A[i][k]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    S=sum(square[i][i] for i in range(n))
    U=sum(square[i][j]*square[j][i] for i in range(n) for j in range(n))
    T=sum(b[i]*square[i][j]*b[j] for i in range(n) for j in range(n))
    B=sum(v*v for v in b)
    return Q(S),Q(U),Q(T),Q(B)


def raw_prediction(A,b):
    S,U,T,B=traces(A,b)
    v=B+2*S
    return v,3*v*v+48*(U+T)


def norm_constants(n):
    beta=Q(n-1,n)
    u=Q(n*n-3*n+3,n*(n-1))
    t=beta*beta/(2*beta-u)
    rstar=1-u/beta
    K=3+12*t
    return beta,u,t,rstar,K


def check_profile(A,b):
    S,U,T,B=traces(A,b)
    v=B+2*S
    if v==0: return
    K=raw_prediction(A,b)[1]/(v*v)
    n=len(b)
    beta,u,t,rstar,Kmax=norm_constants(n)
    assert 3<=K<=Kmax, (n,K,Kmax)
    if S:
        r=B/(2*S)
        c=T/(B*S) if B else Q(0)
        deficit=Q(12)/(1+r)**2*((u-U/S**2)+2*r*(beta-c)+t*(r-rstar)**2)
        assert Kmax-K==deficit,(Kmax-K,deficit)
        assert u>=U/S**2 and (not B or beta>=c)


def run():
    rng=Random(21042026)
    for n in (2,3,4):
        for rep in range(12):
            A=[[Q(0) for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i+1,n):
                    A[i][j]=A[j][i]=Q(rng.randint(-2,2))
            diag=[rng.randint(-2,2) for _ in range(n-1)]
            diag.append(-sum(diag))
            for i in range(n): A[i][i]=Q(diag[i])
            b=[Q(rng.randint(-3,3)) for _ in range(n)]
            measured=moments_by_direct_expansion(A,b)
            predicted=raw_prediction(A,b)
            assert measured==predicted,(n,rep,measured,predicted)
            check_profile(A,b)
    print('DIRECT_NONDIAGONAL_GAUSSIAN_INTEGRATION_EXACT_OK 36')
    for n in range(2,81):
        beta,u,t,rstar,K=norm_constants(n)
        assert rstar==Q(n-2,(n-1)**2)
        assert K==3+Q(12*(n-1)**3,n*(n*n-n-1))
        assert t*(1+rstar)**2==u+2*beta*rstar
        assert t*2*(1+rstar)==2*beta
        assert 0<=rstar<1
        lam=[Q(n-1)]+[Q(-1)]*(n-1)
        S=sum(x*x for x in lam)
        U=sum(x**4 for x in lam)
        assert U/S**2==u
        assert lam[0]**2/S==beta
        assert 3<=K<15
    print('ALL_DIMENSION_SHARP_WITNESSES_EXACT_OK 2_TO_80')
    for n in range(2,6):
        for tail in product(range(-2,3),repeat=n-1):
            a=list(map(Q,tail))+[Q(-sum(tail))]
            S=sum(x*x for x in a)
            if not S: continue
            U=sum(x**4 for x in a)
            beta,u,*_=norm_constants(n)
            assert U<=u*S*S
            assert max(x*x for x in a)<=beta*S
    print('SMALL_INTEGER_SPECTRAL_BOUND_GRID_OK n=2..5')
    print('ALL_GAUSSIAN_HARMONIC_MIXED_FOURTH_MOMENT_CHECKS_OK')

if __name__=='__main__': run()

#!/usr/bin/env python3
"""Exact finite-state and interval checks for the bottleneck dispersion theorem.
No third-party dependencies are required. Mathematical limits are proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import log

CHECKS = 0

def check(statement, context=''):
    global CHECKS
    CHECKS += 1
    if not statement:
        raise AssertionError(f'assertion {CHECKS}: {context}')

def geom_cdf(q, k):
    return 1-q**k

def pfinite(q, m, n, T):
    assert 0 <= n < T
    out=(1-q)/(1-q**(n+1))
    for h in range(1,T-n):
        out *= (1-q**h)/(1-q**(n+1+h))
    return out**m

def direct_stationary_joint(q,m,K,d):
    # Independent lag inequalities for both K-window indicators at 0 and d.
    z=F(1)
    for t in range(1,K+d+1):
        caps=[]
        if 1 <= t <= K:
            caps.append(1 if t==1 else t-1)
        if d+1 <= t <= d+K:
            caps.append(1 if t==d+1 else t-d-1)
        if caps:
            z *= geom_cdf(q,min(caps))**m
    return z

def closed_stationary_single(q,m,K):
    z=1-q
    for t in range(1,K):z*=1-q**t
    return z**m

def closed_b(q,m,j):
    z=1-q
    for t in range(1,j+1):z*=1-q**t
    return z**m

def exhaustive_finite(q,m,T):
    # Exhaustively enumerate all weighted parent histories in a finite graph.
    birth_options=[]
    for t in range(1,T+1):
        one=[(i,(1-q)*q**(t-1-i)/(1-q**t)) for i in range(t)]
        birth_options.append([(tuple(x[0] for x in a), __import__('functools').reduce(lambda z,y:z*y,[x[1] for x in a],F(1))) for a in product(one,repeat=m)])
    singles=[F(0) for _ in range(T)]
    joints={(n,l):F(0) for n in range(T) for l in range(n+1,T)}
    total=F(0)
    for history in product(*birth_options):
        parents=[h[0] for h in history]
        weight=F(1)
        for h in history:weight*=h[1]
        total+=weight
        flags=[]
        for n in range(T):
            flag=all(k==n for k in parents[n]) and all(k>n for t in range(n+2,T+1) for k in parents[t-1])
            flags.append(flag)
            if flag:singles[n]+=weight
        for n,l in joints:
            if flags[n] and flags[l]:joints[n,l]+=weight
    check(total==1,('total',q,m,T))
    for n in range(T):check(singles[n]==pfinite(q,m,n,T),('single',q,m,T,n))
    for n,l in joints:
        check(joints[n,l]==singles[n]*pfinite(q,m,l-n-1,T-n-1),('joint',q,m,T,n,l))

def bounds_S(q,m,J=14,N=36):
    """Exact lower/upper rational bounds for S_m(q), without floating-point truncation."""
    assert J < N and q>0 and q<1
    tailx=q**(N+1)/(1-q)
    check(tailx<1)
    lo=hi=F(0)
    for j in range(J):
        prod=F(1)
        for h in range(j+1,N+1): prod *= 1-q**h
        lo+=prod**(-m)-1
        hi+=(prod*(1-tailx))**(-m)-1
    xj=q**(J+1)/(1-q)
    check(xj<=F(1,2))
    hi += m * 2**(m+1) * q**(J+1)/(1-q)**2
    return lo,hi

def main():
    for q in [F(1,2),F(1,3),F(2,5)]:
        for m in [1,2,3]:
            for K in range(2,11):
                single=closed_stationary_single(q,m,K)
                for d in range(1,K):
                    check(direct_stationary_joint(q,m,K,d)==single*closed_b(q,m,d-1),('stationary pair',q,m,K,d))
    for q in [F(1,2),F(1,3)]:
        for m in (1,2):
            for T in range(1,6):exhaustive_finite(q,m,T)
    for m,qlo,qhi in [(1,F(1,5),F(1,4)),(2,F(1,8),F(1,6)),(3,F(1,10),F(1,8)),(4,F(1,14),F(1,10))]:
        a,b=bounds_S(qlo,m); check(b<F(1,2), ('sub-Poisson',m,qlo,float(a),float(b)))
        a,b=bounds_S(qhi,m); check(a>F(1,2), ('super-Poisson',m,qhi,float(a),float(b)))
    # Two nondegenerate consecutive inter-renewal possibilities: lengths 1, 3.
    for q in (F(1,2),F(1,5),F(2,3)):
        for m in (1,2,4):
            b0=closed_b(q,m,0)
            b2=closed_b(q,m,2)
            check(b0>0 and b2-b0**3>0,('renewal support',q,m))
    print(f'PASS: {CHECKS} exact rational assertions')
    print('Central-limit and large-m asymptotic steps require analytical proof, not finite tests.')

if __name__=='__main__':main()

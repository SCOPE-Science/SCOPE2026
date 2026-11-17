#!/usr/bin/env python3
"""Exact checks for cross-part isolation in fixed-edge bipartite graphs.

Requires Python 3 standard library only. Run: python verify.py
The combinatorial proof applies at every size; enumeration is a finite check.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, exp, sqrt


def binom(n, k):
    return comb(n, k) if 0 <= k <= n and n >= 0 else 0


def formula(a, b, k):
    """Covariance of zero-row and zero-column counts."""
    N = a*b
    den = binom(N, k)
    pr = Fraction(binom(N-b, k), den)
    pc = Fraction(binom(N-a, k), den)
    both = Fraction(binom((a-1)*(b-1), k), den)
    return a*b*(both-pr*pc)


def exact_population(a, b):
    N = a*b
    aggregates = defaultdict(lambda: [0,0,0,0])
    for mask in range(1 << N):
        k = mask.bit_count()
        r = sum(all((mask >> (i*b+j))&1 == 0 for j in range(b)) for i in range(a))
        c = sum(all((mask >> (i*b+j))&1 == 0 for i in range(a)) for j in range(b))
        v = aggregates[k]
        v[0] += 1
        v[1] += r
        v[2] += c
        v[3] += r*c
    return aggregates


def run():
    checks = 0
    for a in range(2, 13):
        for b in range(2, 13):
            N = a*b
            for k in range(N+1):
                f = formula(a,b,k)
                strict = (2 <= k <= N-max(a,b))
                assert (f < 0) == strict, (a,b,k,f)
                assert (f == 0) == (not strict), (a,b,k,f)
                checks += 2
                if k <= (a-1)*(b-1)+1 and k <= N-max(a,b):
                    u = Fraction(binom(N-b,k),binom(N,k))
                    v = Fraction(binom(N-a,k),binom(N,k))
                    z = Fraction(binom((a-1)*(b-1),k),binom(N,k))
                    prod = Fraction(1)
                    for t in range(k):
                        prod *= 1-Fraction(t, (N-b-t)*(N-a-t))
                    assert z == u*v*prod, (a,b,k)
                    checks += 1
    for a,b in [(2,2),(2,3),(3,3),(3,4),(4,4)]:
        d=exact_population(a,b)
        for k,(count,rs,cs,rcs) in d.items():
            assert count == binom(a*b,k)
            direct = Fraction(rcs,count)-Fraction(rs*cs,count*count)
            assert direct == formula(a,b,k), (a,b,k,direct,formula(a,b,k))
            checks += 2
    # In independent-entry sampling, only one common cell connects a row and column.
    for a in range(2,11):
        for b in range(2,11):
            for q in [Fraction(1,8),Fraction(1,3),Fraction(1,2),Fraction(3,4)]:
                cov = a*b*q*(1-q)**(a+b-1)
                assert cov > 0
                checks += 1
    # Numerical check only for the limiting constant; not a substitute for asymptotic proof.
    for alpha,beta,c in [(1,1,1), (1,1,2),(1,2,1),(2,3,3)]:
        limit = -(c*c)/(2*alpha*beta)*exp(-c*(1/alpha+1/beta))
        n=320
        a,b,k=alpha*n,beta*n,c*n
        fv = float(formula(a,b,k))
        assert abs(fv-limit)<0.01, (alpha,beta,c,fv,limit)
        checks+=1
    # Balanced case: directly check covariance and variance normalization.
    for n in [60, 120, 240, 400]:
        N=n*n
        k=n
        den=binom(N,k)
        u=Fraction(binom(N-n,k),den)
        u2=Fraction(binom(N-2*n,k),den)
        variance=n*u*(1-u)+n*(n-1)*(u2-u*u)
        covariance=formula(n,n,k)
        limiting_v=(exp(1)-2)/exp(2)
        limiting_c=-1/(2*exp(2))
        limiting_nc=-1/(2*(exp(1)-2))
        assert variance>0
        assert abs(float(variance/n)-limiting_v)<0.02
        assert abs(float(covariance)-limiting_c)<0.02
        assert abs(float(n*covariance/variance)-limiting_nc)<0.04
        independent_cov=n*n*Fraction(1,n)*Fraction(n-1,n)**(2*n-1)
        independent_variance=n*Fraction(n-1,n)**n*(1-Fraction(n-1,n)**n)
        assert abs(float(independent_cov/independent_variance)-1/(exp(1)-1))<0.03
        checks+=5
    print(f"PASS: {checks} exact/sign/product/ensemble checks plus sparse-scale sanity checks")

if __name__ == '__main__':
    run()

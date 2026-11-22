#!/usr/bin/env python3
"""Finite exact verification for random weak-order one-point type fluctuations.

Uses only the Python standard library. The asymptotic CLT and variance
require the independent analytic proof and are not established by these tests.
"""
from itertools import product
from math import comb
from decimal import Decimal, localcontext


def compositions(n):
    if n == 0:
        yield ()
    else:
        for first in range(1, n+1):
            for tail in compositions(n-first):
                yield (first,)+tail


def direct_one_types(sizes):
    level = tuple(i for i, s in enumerate(sizes) for _ in range(s))
    n = len(level)
    result = 0
    for statuses in product((-1, 0, 1), repeat=n):
        # -1: old point below x; 1: old point above x
        L = [i for i, s in enumerate(statuses) if s == -1]
        U = [i for i, s in enumerate(statuses) if s == 1]
        if any(statuses[a] != -1 for a in range(n) for b in L if level[a] < level[b]):
            continue
        if any(statuses[b] != 1 for a in U for b in range(n) if level[a] < level[b]):
            continue
        if any(level[a] >= level[b] for a in L for b in U):
            continue
        result += 1
    return result


def symbolic_one_types(sizes):
    b = [2**s-1 for s in sizes]
    return 1 + 2*sum(b) + sum(b[i]*b[j] for i in range(len(b)) for j in range(i+1, len(b)))


def exact_moments(nmax):
    # All sums run over labelled weak orders on {1,...,n}. Appending the
    # final antichain is counted with binom(n,k), independently of labels.
    C=[0]*(nmax+1); S=[0]*(nmax+1); S2=[0]*(nmax+1)
    T=[0]*(nmax+1); ST=[0]*(nmax+1); T2=[0]*(nmax+1)
    C[0]=T[0]=T2[0]=1
    for n in range(1, nmax+1):
        for k in range(1, n+1):
            m=n-k; b=2**k-1; w=comb(n,k)
            C[n] += w*C[m]
            S[n] += w*(S[m]+b*C[m])
            S2[n] += w*(S2[m]+2*b*S[m]+b*b*C[m])
            T[n] += w*(T[m]+b*S[m]+2*b*C[m])
            ST[n] += w*(ST[m]+b*S2[m]+2*b*S[m]+b*T[m]+b*b*S[m]+2*b*b*C[m])
            T2[n] += w*(T2[m]+b*b*S2[m]+4*b*b*C[m]+2*b*ST[m]+4*b*T[m]+4*b*b*S[m])
    return C,S,S2,T,ST,T2


def main():
    trials = 0
    for n in range(1, 8):
        for sizes in compositions(n):
            a=direct_one_types(sizes)
            b=symbolic_one_types(sizes)
            assert a==b,(sizes,a,b)
            trials += 1
    print('PASS independent ternary-extension enumerations:', trials)
    C,S,S2,T,ST,T2=exact_moments(200)
    for n in range(1, 8):
        direct_total=0
        direct_sum_S=0
        direct_total_T2=0
        for sizes in compositions(n):
            ways=1
            remaining=n
            for k in sizes:
                ways *= comb(remaining,k);remaining -= k
            direct_total+=ways*symbolic_one_types(sizes)
            direct_total_T2 += ways*symbolic_one_types(sizes)**2
            direct_sum_S+=ways*sum(2**k-1 for k in sizes)
        assert direct_total==T[n]
        assert direct_sum_S==S[n]
        assert direct_total_T2==T2[n]
    print('PASS weighted-composition moment comparisons: 7')
    with localcontext() as ctx:
        ctx.prec=100
        rho=Decimal(2).ln()
        print('n  ES_ratio  VarS_ratio  ET_ratio  VarT_ratio')
        for n in (10,20,40,80,140,200):
            es=Decimal(S[n])/C[n]
            var_s=Decimal(S2[n])/C[n]-es**2
            et=Decimal(T[n])/C[n]
            var_t=Decimal(T2[n])/C[n]-et**2
            vals=(es*rho/n,var_s*rho**2/n,et*2*rho**2/n**2,var_t*rho**4/n**3)
            print(n,*(f'{v:.8f}' for v in vals))
        assert Decimal('0.98') < (Decimal(S2[200])/C[200]-(Decimal(S[200])/C[200])**2)*rho**2/200 < 1
        assert Decimal('0.93') < (Decimal(T2[200])/C[200]-(Decimal(T[200])/C[200])**2)*rho**4/200**3 < 1
    print('FINITE EXACT MOMENTS PASS; infinite limits require the proof')

if __name__ == '__main__':
    main()

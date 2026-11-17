#!/usr/bin/env python3
"""Exact arithmetic checks for skyline/comparability overlap identities.

No random simulation: each experiment enumerates the independent coordinate
rank permutations, fixing the first coordinate ordering by exchangeability.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial


def formulas(n, d):
    if n < 3 or d < 2:
        raise ValueError('requires n>=3, d>=2')
    p = F(1, 2 ** (d - 1))
    mu = sum((-1)**k * comb(n - 1, k) * F(1, (k + 1)**d)
             for k in range(n))
    a = sum((-1)**k * comb(n - 2, k) * F(1, ((k + 1)*(k + 2))**d)
            for k in range(n - 1))
    b = p * sum((-1)**k * comb(n - 3, k) *
                (F(1, (k + 1)**d) - F(k + 4, (k + 2)*(k + 3))**d)
                for k in range(n - 2))
    s = a - p * mu
    t = b - p * mu
    total = n*(n-1)*s + F(n*(n-1)*(n-2), 2)*t
    return s, t, total


def enumerated(n, d):
    perm = list(permutations(range(n)))
    first = tuple(range(n))
    sums = [0, 0, 0, 0, 0]
    total = 0
    for rest in product(perm, repeat=d - 1):
        ranks = list(zip(first, *rest))
        degrees = [0]*n
        C = 0
        for i in range(n):
            for j in range(i+1, n):
                ij = all(ranks[i][k] < ranks[j][k] for k in range(d))
                ji = all(ranks[i][k] > ranks[j][k] for k in range(d))
                if ij or ji:
                    C += 1
                    degrees[i] += 1
                    degrees[j] += 1
        maximal = [int(not any(
            all(ranks[i][k] < ranks[j][k] for k in range(d))
            for j in range(n) if j != i)) for i in range(n)]
        M = sum(maximal)
        sums[0] += M
        sums[1] += C
        sums[2] += M*C
        sums[3] += sum(maximal[i]*degrees[i] for i in range(n))
        sums[4] += sum(maximal[i]*(C - degrees[i]) for i in range(n))
        total += 1
    em = F(sums[0], total)
    ec = F(sums[1], total)
    cov = F(sums[2], total)-em*ec
    s = F(sums[3], total*n*(n-1)) - F(em*ec, n*comb(n,2))
    t = F(sums[4], total*n*comb(n-1,2)) - F(em*ec, n*comb(n,2))
    return s,t,cov,total


def main():
    count = 0
    for n,d in [(3,2), (4,2), (5,2), (6,2), (7,2), (8,2),
                (3,3), (4,3), (5,3), (3,4), (4,4)]:
        s,t,c,k = enumerated(n,d)
        ss,tt,cc = formulas(n,d)
        assert (s,t,c)==(ss,tt,cc), (n,d,s,t,c,ss,tt,cc)
        print('EXHAUSTIVE',n,d,'coordinate rank cases',k,'COV',c)
        count += 3
    for n in range(3,101):
        H=sum(F(1,j) for j in range(1,n+1))
        s,t,c=formulas(n,2)
        assert s==F((n+3)*H-4*n,2*n*(n-1))
        assert t==F(3*n-(n+2)*H,n*(n-1)*(n-2))
        assert c==-(n-H)/2
        assert (s<0 if n<=15 else s>0)
        assert t<0 and c<0
        count+=6
    for d in range(2,9):
        for n in range(3,51):
            assert formulas(n,d)[1]<0
            count+=1
    print('PASS',count,'exact assertions')

if __name__=='__main__':
    main()

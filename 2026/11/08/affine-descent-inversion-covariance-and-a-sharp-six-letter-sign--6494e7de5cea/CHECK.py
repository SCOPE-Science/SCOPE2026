#!/usr/bin/env python3
"""Exact finite checks of descent--inversion affine-kernel identities.

This is a finite diagnostic, not a substitute for the theorem's proof.
Uses independent generation of uniformly sampled multiset words and exact Fractions.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for a in range(1, n - k + 2):
            for tail in compositions(n - a, k - 1):
                yield (a,) + tail


def generate_words(counts):
    counts = list(counts)
    n = sum(counts)
    prefix = [0] * n
    def rec(i):
        if i == n:
            yield tuple(prefix)
            return
        for letter, v in enumerate(counts):
            if v:
                counts[letter] -= 1
                prefix[i] = letter
                yield from rec(i+1)
                counts[letter] += 1
    yield from rec(0)


def expected_values(counts):
    n = sum(counts)
    total = sum_inv = sum_maj = sum_invmaj = sum_des = 0
    sum_local = [0] * (n - 1)
    sum_local_inv = [0] * (n - 1)
    for w in generate_words(counts):
        total += 1
        inv = sum(int(w[i] > w[j]) for i in range(n) for j in range(i+1,n))
        des = [int(w[i] > w[i+1]) for i in range(n-1)]
        maj = sum((i+1)*des[i] for i in range(n-1))
        sum_inv += inv
        sum_maj += maj
        sum_invmaj += inv * maj
        sum_des += sum(des)
        for j in range(n-1):
            sum_local[j] += des[j]
            sum_local_inv[j] += des[j]*inv
    assert total == factorial(n)//__product(factorial(c) for c in counts)
    covlocal = [Fraction(sum_local_inv[j],total)-Fraction(sum_local[j]*sum_inv,total*total)
                for j in range(n-1)]
    covmaj = Fraction(sum_invmaj,total) - Fraction(sum_inv*sum_maj,total*total)
    return covlocal,covmaj,Fraction(sum_maj,total),Fraction(sum_inv,total)


def __product(xs):
    p=1
    for x in xs:p*=x
    return p


def predicted(counts):
    n = sum(counts)
    T = sum(counts[a]*counts[b] for a in range(len(counts)) for b in range(a+1,len(counts)))
    S = sum(counts[a]*counts[b]*(counts[b]-counts[a]) for a in range(len(counts)) for b in range(a+1,len(counts)))
    covs = [Fraction((n-2)*T+(2*j-n)*S,2*n*(n-1)*(n-2))
            for j in range(1,n)] if n>=3 else [Fraction(T,4)]
    return covs, Fraction(3*T+S,12),Fraction(T,2),T,S


def check():
    vectors=0
    rational_checks=0
    outcomes=[]
    for n in range(2,9):
        for k in range(1,min(4,n)+1):
            for counts in compositions(n,k):
                a,b,em,ei=expected_values(counts)
                A,B,mu,T,S=predicted(counts)
                assert a == A, ('kernel',counts,a,A)
                assert b == B, ('maj',counts,b,B)
                assert em == mu == ei, ('means',counts,em,ei,mu)
                rational_checks += n+2
                vectors += 1
                if n<=5:assert b>=0, ('minimality',counts,b)
                if n==6 and b<0:outcomes.append((counts,b))
                assert all(a[j]+a[n-2-j] == Fraction(T,n*(n-1)) for j in range(n-1))
                rational_checks += n-1
    assert outcomes == [((5,1),Fraction(-5,12))], outcomes
    for n in range(6,31):
        counts=(n-1,1)
        A,B,mu,T,S=predicted(counts)
        assert B == Fraction((n-1)*(5-n),12) < 0
        rational_checks += 1
    print('PASS: %d multiset vectors, %d exact rational and symmetry checks, unique n=6 negative profile %s' % (vectors,rational_checks,outcomes))


if __name__ == '__main__':check()

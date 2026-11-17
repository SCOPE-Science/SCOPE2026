#!/usr/bin/env python3
"""Standalone exhaustive checks of palindrome-subsequence occurrence counts.

Counts distinct index selections, not distinct palindrome strings. Only standard Python.
Usage: python3 palindrome_embedding_verifier.py
"""
from collections import Counter
from itertools import combinations
from math import comb


def choose(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def closed_coefficient(q, k, length):
    if length <= 0:
        return 0
    m = (length + 1) // 2
    return q * sum(choose(m-1, e) * (q-1)**(m-1-e) *
                   choose(k+m-e-1, length) for e in range(m))


def direct_embeddings(word):
    counts = Counter()
    for n in range(1, len(word)+1):
        for indices in combinations(range(len(word)), n):
            v = tuple(word[i] for i in indices)
            if v == v[::-1]:
                counts[n] += 1
    return counts


def check_series(q, K, L):
    """The denominator relation implied by the claimed rational generating function."""
    # (1-t)*((1-t)**2-z**2*t*(q-1+t)) G = q*z*t*(1-t+z*t)
    # Polynomial multiplication checks every coefficient of formal power series.
    G = {(ln, k): closed_coefficient(q, k, ln)
         for ln in range(1, L+1) for k in range(1, K+1)}
    terms = {(0,0):1,(0,1):-3,(0,2):3,(0,3):-1,
             (2,1):-(q-1),(2,2):q-2,(2,3):1}
    rhs = {(1,1):q,(1,2):-q,(2,2):q}
    for ln in range(1,L+1):
        for k in range(1,K+1):
            lhs = sum(v * G.get((ln-dln,k-dk),0) for (dln,dk),v in terms.items())
            assert lhs == rhs.get((ln,k),0), (q,ln,k,lhs,rhs.get((ln,k),0))


def main():
    profiles=length_comparisons=0
    for q in range(2,6):
        for k in range(1,7):
            if q*k>17: break
            for perm in (tuple(range(q)), tuple(reversed(range(q)))):
                word = perm*k
                actual = direct_embeddings(word)
                for ln in range(1,len(word)+1):
                    expected=closed_coefficient(q,k,ln)
                    assert actual[ln] == expected, (q,k,ln,actual[ln],expected)
                    length_comparisons += 1
                assert sum(actual.values()) == sum(closed_coefficient(q,k,n) for n in range(1,q*k+1))
                assert actual[2*k-1] == q*(q-1)**(k-1)
                assert not any(actual[t] for t in range(2*k,q*k+1))
                profiles += 1
    coefficient_checks=0
    for q in range(2,10):
        check_series(q,17,22)
        coefficient_checks += 17*22
    print('PASS exhaustive occurrence profiles:',profiles)
    print('PASS length-level comparisons:',length_comparisons)
    print('PASS rational-series coefficient identities:',coefficient_checks)

if __name__=='__main__':
    main()

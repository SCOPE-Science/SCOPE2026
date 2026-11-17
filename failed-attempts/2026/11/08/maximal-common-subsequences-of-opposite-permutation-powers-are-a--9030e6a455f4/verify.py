#!/usr/bin/env python3
"""Independent finite checks of the reverse-permutation MCS classification.

Run: python3 verify.py
Requires only the Python standard library.
"""
from collections import defaultdict
from itertools import combinations, product


def subsequences(host):
    found = {()}
    for x in host:
        found |= {w + (x,) for w in tuple(found)}
    return found


def stats(word):
    return (sum(x < y for x, y in zip(word, word[1:])),
            sum(x > y for x, y in zip(word, word[1:])),
            sum(x == y for x, y in zip(word, word[1:])))


def direct_mcs(common, q):
    return {w for w in common if not any(
        w[:j] + (x,) + w[j:] in common
        for j in range(len(w) + 1) for x in range(q))}


def balanced_count(q, k):
    dp = {(x, 0): 1 for x in range(q)}
    for _ in range(2 * k - 2):
        following = defaultdict(int)
        for (last, d), ways in dp.items():
            for x in range(q):
                if x != last:
                    following[x, d + (last > x)] += ways
        dp = following
    return sum(ways for (_, d), ways in dp.items() if d == k - 1)


def verify():
    configs = [(q,k) for q in range(2,7) for k in range(1,5)
               if q*k <= 16]
    total_common = 0
    total_maximal = 0
    for q,k in configs:
        host = tuple(range(q))*k
        reverse = tuple(reversed(range(q)))*k
        common = subsequences(host) & subsequences(reverse)
        total_common += len(common)
        predicted = {w for w in common if len(w) == 2*k-1
                     and stats(w) == (k-1,k-1,0)}
        actual = direct_mcs(common,q)
        assert actual == predicted, (q,k,actual^predicted)
        assert not any(len(w)>2*k-1 for w in common)
        assert len(actual) == balanced_count(q,k), (q,k)
        pal = sum(w == w[::-1] for w in actual)
        assert pal == q*(q-1)**(k-1), (q,k,pal)
        for w in common:
            a,d,e=stats(w)
            assert a+e <= k-1 and d+e <= k-1
        total_maximal += len(actual)
    # Distinct independent computation of the rational generating function,
    # as an identity of polynomial truncations: N*D = B modulo z**(n+1).
    # dp[n][d] counts Smirnov words, computed from a last-letter DP.
    polynomial_checks = 0
    for q in range(2,8):
        bound = 16
        dp = {(x,0):1 for x in range(q)}
        values = [{} for _ in range(bound+1)]
        for n in range(1,bound+1):
            row=defaultdict(int)
            for (_,d),v in dp.items(): row[d]+=v
            values[n]=dict(row)
            nd=defaultdict(int)
            for (last,d),v in dp.items():
                for x in range(q):
                    if x != last:nd[x,d+(last>x)]+=v
            dp=nd
        # D(z,t) = ((1+tz)^q-t(1+z)^q)/(1-t),
        # B(z,t) = ((1+z)^q-(1+tz)^q)/(1-t).
        from math import comb
        for n in range(1,bound+1):
            for d in range(0,n):
                left=values[n].get(d,0)
                for j in range(1,min(q,n)+1):
                    # coefficient z^j t^h in D is -C(q,j) for 1<=h<=j-1
                    for h in range(1,j):
                        left -= comb(q,j)*values[n-j].get(d-h,0)
                # coefficient B(z,t) at z^n t^d = C(q,n) if 0<=d<n, n<=q
                right=comb(q,n) if n<=q and d<n else 0
                assert left==right,(q,n,d,left,right)
                polynomial_checks+=1
    print('VERIFY_OK configurations=%d common_words=%d maximal_words=%d polynomial_cells=%d'
          % (len(configs), total_common, total_maximal, polynomial_checks))

if __name__=='__main__': verify()

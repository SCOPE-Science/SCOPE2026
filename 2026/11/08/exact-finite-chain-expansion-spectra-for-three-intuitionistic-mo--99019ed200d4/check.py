#!/usr/bin/env python3
"""Exact, self-contained verification of finite-chain modal expansion counts.

Enumerates all order-preserving unary maps on finite Heyting chains;
evaluates the defining modal interaction identities directly.
The infinite-family proof is in RESULT.md, not inferred from enumeration.
"""
from itertools import combinations_with_replacement
from math import comb


def imp(a, b, n):
    return n - 1 if a <= b else b


def formula(n):
    m = comb(2*n - 1, n)
    t = comb(2*n - 2, n - 1)
    cm = m * m
    wm = t * t + 2 * (m - t)
    im = 1 + (m - t) + sum(
        comb(n + h - 2, n - 2) * comb(n + h - 1, n - 1)
        for h in range(1, n)
    )
    return cm, wm, im


def enumerate_directly(n):
    functions = list(combinations_with_replacement(range(n), n))
    cm = wm = im = 0
    for f in functions:
        for g in functions:
            cm += 1
            # The Heyting-chain pseudocomplement is a -> bottom.
            consistency = all(
                min(f[a], g[imp(a, 0, n)]) == 0
                for a in range(n)
            )
            interaction = all(
                imp(imp(f[n - 1], g[a], n), g[a], n) == n - 1
                for a in range(n)
            )
            if consistency:
                wm += 1
                if interaction:
                    im += 1
    return cm, wm, im


def independent_dynamic_count(n):
    """Count IM via DP over all allowed monotone diamond sequences.

    For every monotone f, enumerate allowed g by increasing rank using a
    dynamic program for weakly increasing sequences (not closed binomials).
    """
    m = comb(2*n-1, n)
    t = comb(2*n-2, n-1)
    im = 1 + (m - t)
    # Last box value h>0; first box value must be zero.
    for h in range(1, n):
        dp = [0]*n
        dp[0] = 1
        for _ in range(n-2):
            dp = [sum(dp[:v+1]) if v<=h else 0 for v in range(n)]
        fcount = sum(dp[:h+1])
        allowed = list(range(h)) + [n-1]
        dg = [0]*len(allowed)
        dg[0] = 1
        for _ in range(n-1):
            dg = [sum(dg[:j+1]) for j in range(len(allowed))]
        im += fcount*sum(dg)
    return im


def main():
    expected = {2:(9,6,4), 3:(100,44,29), 4:(1225,430,288),
                5:(15876,5012,3377), 6:(213444,63924,43088)}
    for n in range(2, 7):
        predicted = formula(n)
        brute = enumerate_directly(n)
        assert predicted == brute == expected[n], (n,predicted,brute)
        dynamic = independent_dynamic_count(n)
        assert dynamic == predicted[2], (n,dynamic,predicted[2])
        print('n=%d CM=%d WM=%d IM=%d -- verified' % ((n,)+predicted))
    for n in range(7, 15):
        assert independent_dynamic_count(n) == formula(n)[2]
    print('DP agrees with formula through n=14; exhaustive pairs through n=6.')

if __name__=='__main__':
    main()

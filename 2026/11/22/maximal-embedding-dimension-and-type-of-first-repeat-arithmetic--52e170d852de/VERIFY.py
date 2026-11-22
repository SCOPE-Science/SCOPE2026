#!/usr/bin/env python3
"""Finite integer corroboration of the first-repeat semigroup theorem.
Run: python3 VERIFY.py. No external modules required.
"""
from math import gcd

checks = 0
pairs = 0
for a in range(3, 21):
    for d in range(1, 9):
        if gcd(a, d) != 1:
            continue
        pairs += 1
        u, v, w = a, a + d, a + 2*d
        m = 2*v
        q = a//2
        starters = [m, q*w] if a % 2 == 0 else [m, v+q*w, (q+1)*w]
        # All later steps are exact finite comparisons, not an infinite proof.
        top = 4*(a+d)**2 + 200
        reps = [0]*(top+1)
        reps[0] = 1
        for coin in (u, v, w):
            for n in range(coin, top+1):
                reps[n] += reps[n-coin]
        orig = [n == 0 or reps[n] > 1 for n in range(top+1)]
        in_s0 = [c > 0 for c in reps]
        cover = [False]*(top+1)
        cover[0] = True
        for h in starters:
            for n in range(h, top+1):
                if in_s0[n-h]:
                    cover[n] = True
        for n in range(top+1):
            assert cover[n] == orig[n], (a,d,n,'ideal union')
            checks += 1
        pos = [n for n in range(1,top+1) if orig[n]]
        gens = [n for n in pos if not any(orig[i] and orig[n-i] for i in range(1,n))]
        assert gens[0] == m and len(gens) == m, (a,d,'generators',gens)
        checks += 2
        cutoff = max(n for n in range(top+1) if not orig[n])
        assert cutoff + m < top, (a,d,'insufficient range')
        # The pseudo-Frobenius criterion suffices to check minimal generators:
        # a gap is pseudo-Frobenius iff translating it by all generators lies in S.
        pf = [n for n in range(cutoff+1) if not orig[n] and all(orig[n+g] for g in gens)]
        assert len(pf) == m-1, (a,d,'type',pf)
        checks += 1
print('PASS: %d coprime parameter pairs; %d exact comparisons.' % (pairs,checks))

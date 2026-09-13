#!/usr/bin/env python3
"""Exhaustive verifier for: Admissible 28-set in one class mod 30.

Target claim: does there exist r with gcd(r,30)=1 and H = {h_1<...<h_28}
with 0 <= h_i <= 1000, all h_i == r (mod 30), such that for every prime
p <= 28 the residues {h_i mod p} omit at least one class mod p?

Method: only 8 residue classes mod 30 are coprime (1,7,11,13,17,19,23,29),
so every integer r with gcd(r,30)=1 reduces to one of them. For each class,
enumerate ALL C(n,28) subsets of the pool {x in [0,1000] : x == r mod 30}
(n = 33 or 34) and test admissibility against all primes <= 28 directly.
"""
import itertools
import math
import sys

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]  # all primes <= 28
UNITS = [r for r in range(1, 31) if math.gcd(r, 30) == 1]
assert UNITS == [1, 7, 11, 13, 17, 19, 23, 29], UNITS


def pool(r):
    """All integers h in [0,1000] with h == r (mod 30)."""
    return [x for x in range(0, 1001) if x % 30 == r % 30]


def is_admissible(H):
    """True iff H omits at least one residue class mod p for every prime p <= 28."""
    for p in PRIMES:
        if len({h % p for h in H}) == p:
            return False
    return True


def main():
    total_checked = 0
    for r in UNITS:
        P = pool(r)
        n = len(P)
        expected = math.comb(n, 28)
        assert expected in (237336, 1344904), (r, n, expected)
        assert P[0] % 30 == r % 30 and P[-1] % 30 == r % 30
        assert all(P[i] < P[i + 1] for i in range(len(P) - 1))
        assert all(0 <= h <= 1000 for h in P)
        checked = 0
        for S in itertools.combinations(P, 28):
            checked += 1
            if is_admissible(S):
                print("COUNTEREXAMPLE FOUND: r=%d S=%s" % (r, list(S)))
                return 1
        assert checked == expected, (r, checked, expected)
        total_checked += checked
        print("r=%2d: pool_size=%d subsets_checked=%d admissible_found=0"
              % (r, n, checked))
    assert total_checked == 2 * 1344904 + 6 * 237336 == 4113824, total_checked
    print("TOTAL_SUBSETS_CHECKED=%d" % total_checked)
    print("VERIFIED: no admissible 28-set exists in any coprime class mod 30.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

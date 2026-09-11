"""Exact genus-0 WDVV reconstruction for P^r primaries (exact integer arithmetic).

Target: <H^4 x7>_{0,4} on P^4.
Method: Kontsevich-Manin reconstruction with divisor/string/fundamental axioms,
3-point small-QH base, 2-point line base, and WDVV splitting a_min = 1+(a_min-1)
with gamma=max (kills/controls the one same-(d,n) term). Terminates by
(d, n, lexicographic-min) descent. See DRAFT.md for proof.
"""
import sys
from functools import lru_cache

R = 4  # projective dimension; tests use R=2

def make_engine(r):
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def inv(d, tup):
        # tup: sorted tuple of ints
        n = len(tup)
        # validity
        for a in tup:
            if a < 0 or a > r:
                return 0
        s = sum(tup)
        if s != r + (r + 1) * d + n - 3:
            return 0
        if d == 0:
            return 1 if (n == 3 and s == r) else 0
        if d < 0:
            return 0
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            # only line through two top points survives (dim forces it)
            if d == 1 and tup == (r, r):
                return 1
            return 0
        if n == 3:
            return 1
        lst = list(tup)
        if 0 in lst:
            return 0  # fundamental-class axiom (d>0 or n>3)
        if 1 in lst:
            i = lst.index(1)
            rest = tuple(sorted(lst[:i] + lst[i+1:]))
            return d * inv(d, rest)
        # all >= 2, n >= 4: WDVV
        a1 = lst[0]  # min
        gamma = lst[-1]  # max
        delta = lst[-2]
        S = lst[1:-2]
        m = len(S)
        alpha = 1
        beta = a1 - 1
        e_skip = r - a1
        lhs_rest = 0
        for mask in range(1 << m):
            S1 = [S[i] for i in range(m) if (mask >> i) & 1]
            S2 = [S[i] for i in range(m) if not ((mask >> i) & 1)]
            for d1 in range(d + 1):
                d2 = d - d1
                for e in range(r + 1):
                    if mask == 0 and d1 == 0 and e == e_skip:
                        continue  # target term, coefficient 1
                    A = inv(d1, tuple(sorted([alpha, beta] + S1 + [e])))
                    if A == 0:
                        continue
                    B = inv(d2, tuple(sorted([r - e, gamma, delta] + S2)))
                    lhs_rest += A * B
        rhs = 0
        for mask in range(1 << m):
            S1 = [S[i] for i in range(m) if (mask >> i) & 1]
            S2 = [S[i] for i in range(m) if not ((mask >> i) & 1)]
            for d1 in range(d + 1):
                d2 = d - d1
                for e in range(r + 1):
                    A = inv(d1, tuple(sorted([alpha, gamma] + S1 + [e])))
                    if A == 0:
                        continue
                    B = inv(d2, tuple(sorted([r - e, beta, delta] + S2)))
                    rhs += A * B
        return rhs - lhs_rest

    def call(d, lst):
        return inv(d, tuple(sorted(lst)))

    return inv, call

def main():
    inv4, call4 = make_engine(4)
    # P2 calibration: N3 = 12 (8 pts, d=3), N2=1, N1=1
    inv2, call2 = make_engine(2)
    t1 = call2(1, [2]*2)  # displacement? n=2 base
    n1 = call2(1, [2]*1 + [1]*0)  # placeholder unused
    # plane counts: d=1: 3d-1=2 points -> N1=1 ; d=2: 5 points -> 1 ; d=3: 8 points -> 12
    N1 = call2(1, [2]*2)
    N2 = call2(2, [2]*5)
    N3 = call2(3, [2]*8)
    print("P2 calibration: N1=", N1, " N2=", N2, " N3=", N3)
    assert N1 == 1, N1
    assert N2 == 1, N2
    assert N3 == 12, N3
    print("P2_CALIBRATION_PASS")
    # P4 checks
    b2 = call4(1, [4, 4])          # 2-point line
    b3 = call4(1, [4, 4, 1])       # 3-point
    print("P4 base: <4,4>_1=", b2, " <4,4,1>_1=", b3)
    assert b2 == 1 and b3 == 1
    tgt = call4(4, [4]*7)
    print("TARGET <pt^7>_{0,4} =", tgt)
    print("CLAIM 231733 ->", ("MATCH" if tgt == 231733 else "MISMATCH"))
    # cache stats
    print("cache4:", inv4.cache_info())
    print("cache2:", inv2.cache_info())

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()

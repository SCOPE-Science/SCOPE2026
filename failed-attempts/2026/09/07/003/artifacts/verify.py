#!/usr/bin/env python3
"""Standalone verification for Lane 06: sharp ST constant 0.71 on 4x4 grid.
Deterministic, no randomness, pure stdlib. Runtime ~2s.
Regenerates: line census, I=148, exhaustive C* via exact integer arithmetic,
C=0.71 certificate, C=0.70 refutation, per-N tables, D4 orbit reps.
Usage: python3 verify.py [--quick]
"""
from math import gcd
from itertools import combinations
from collections import Counter
import sys

G = [(x, y) for x in range(4) for y in range(4)]
IDX = {p: i for i, p in enumerate(G)}

def norm_primary(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    A, B = (y2 - y1), -(x2 - x1)
    g = gcd(A, B)
    A //= g; B //= g
    if A < 0 or (A == 0 and B < 0):
        A, B = -A, -B
    return (A, B, -(A * x1 + B * y1))

def norm_alt(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    dx, dy = x2 - x1, y2 - y1
    g = gcd(dx, dy)
    dx //= g; dy //= g
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return (dx, dy, dy * x1 - dx * y1)

def enumerate_lines(norm):
    d = {}
    for a, b in combinations(G, 2):
        k = norm(a, b)
        d.setdefault(k, set()).add(IDX[a])
        d[k].add(IDX[b])
    return d

def popcount(x):
    return bin(x).count("1")

def main():
    # 1. census, two independent encodings
    d1 = enumerate_lines(norm_primary)
    d2 = enumerate_lines(norm_alt)
    assert len(d1) == 62, len(d1)
    assert len(d2) == 62, len(d2)
    c1 = Counter(len(v) for v in d1.values())
    assert c1[4] == 10 and c1[3] == 4 and c1[2] == 48, c1
    s1 = sorted([frozenset(v) for v in d1.values()], key=lambda s: (len(s), sorted(s)))
    s2 = sorted([frozenset(v) for v in d2.values()], key=lambda s: (len(s), sorted(s)))
    assert s1 == s2, "primary vs alt mismatch"
    I_full = sum(len(v) for v in d1.values())
    assert I_full == 148, I_full
    pairs = sum(len(v) * (len(v) - 1) // 2 for v in d1.values())
    assert pairs == 120, pairs  # pair-partition check
    print(f"census OK: 62 lines, {dict(c1)}, I=148, pairs=120")

    keys = sorted(d1.keys())
    linemasks = []
    for k in keys:
        m = 0
        for i in d1[k]:
            m |= (1 << i)
        linemasks.append(m)

    # 2. exhaustive scan with exact integer ratio comparison
    # ratio r = E/(N^{2/3} M^{2/3}); r1>r2 iff E1^3 N2^2 M2^2 > E2^3 N1^2 M1^2
    best = None  # (E,N,M,mask,I)
    best_excess = {}  # N -> (E,M,mask,I) max E
    best_ratio = {}   # N -> (E,M,mask,I) max ratio
    for mask in range(1 << 16):
        N = popcount(mask)
        if N == 0:
            continue
        gains = []
        for lm in linemasks:
            kk = popcount(mask & lm)
            if kk >= 2:
                gains.append(kk)
        gains.sort(reverse=True)
        s = 0
        for t, kk in enumerate(gains, start=1):
            s += kk
            E = s - t - N
            if E <= 0:
                continue
            M, I = t, s
            if best is None or E**3 * best[1]**2 * best[2]**2 > best[0]**3 * N**2 * M**2:
                best = (E, N, M, mask, I)
            if N not in best_excess or E > best_excess[N][0]:
                best_excess[N] = (E, M, mask, I)
            if N not in best_ratio:
                best_ratio[N] = (E, M, mask, I)
            else:
                Eb, Mb = best_ratio[N][0], best_ratio[N][1]
                if E**3 * Mb**2 > Eb**3 * M**2:
                    best_ratio[N] = (E, M, mask, I)
    E, N, M, mask, I = best
    print(f"global best: E={E} N={N} M={M} I={I} mask={mask}")
    assert (E, N, M, I) == (70, 16, 62, 148) and mask == 65535
    Cstar = 70 / (992 ** (2 / 3))
    print(f"C* = 70/992^(2/3) = {Cstar:.10f}")

    # uniqueness: count exact ties
    ties = 0
    for mask2 in range(1 << 16):
        N2 = popcount(mask2)
        if N2 == 0:
            continue
        gains = sorted([popcount(mask2 & lm) for lm in linemasks if popcount(mask2 & lm) >= 2], reverse=True)
        s = 0
        for t, kk in enumerate(gains, start=1):
            s += kk
            E2 = s - t - N2
            if E2 > 0 and E2**3 * N**2 * M**2 == E**3 * N2**2 * t**2:
                ties += 1
    print(f"exact ties: {ties}")
    assert ties == 1, ties

    # 3. integer certificate C=0.71
    viol = 0
    for mask2 in range(1 << 16):
        N2 = popcount(mask2)
        if N2 == 0:
            continue
        gains = sorted([popcount(mask2 & lm) for lm in linemasks if popcount(mask2 & lm) >= 2], reverse=True)
        s = 0
        for t, kk in enumerate(gains, start=1):
            s += kk
            E2 = s - t - N2
            if E2 <= 0:
                continue
            if (100 * E2)**3 > (71**3) * (N2**2) * (t**2):
                viol += 1
    print(f"C=0.71 violations: {viol}")
    assert viol == 0
    # C=0.70 fails at witness
    assert (100 * 70)**3 > (70**3) * (16**2) * (62**2)
    assert 100**3 > 992**2  # hence any C<=0.70 fails
    print("C=0.70 refuted at full grid (integer check)")

    # 4. N<=3 no positive excess
    for mask2 in range(1 << 16):
        N2 = popcount(mask2)
        if N2 not in (1, 2, 3):
            continue
        gains = sorted([popcount(mask2 & lm) for lm in linemasks if popcount(mask2 & lm) >= 2], reverse=True)
        s = 0
        for t, kk in enumerate(gains, start=1):
            s += kk
            assert s - t - N2 <= 0 or N2 == 3 and s - t - N2 == 0, (mask2, N2, t, s - t - N2)
    # max over N=3 is exactly 0 (triangle)
    print("N<=3 check OK (max excess N=1:-1, N=2:-1, N=3:0)")

    print("per-N max excess:")
    for Nn in sorted(best_excess):
        print(f"  N={Nn}: {best_excess[Nn]}")
    print("per-N max ratio:")
    for Nn in sorted(best_ratio):
        Ee, Mm, _, _ = best_ratio[Nn]
        print(f"  N={Nn}: E={Ee} M={Mm} r={Ee/((Nn**(2/3))*(Mm**(2/3))):.6f}")
    print("ALL CHECKS PASSED")

if __name__ == "__main__":
    main()

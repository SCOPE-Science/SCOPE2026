"""Reproducible finite checks for open-independent open-locating codes.

Only Python's standard library is required. Cells (r,c) share a rook
edge precisely when their row or column agrees, but not both.
"""
from collections import Counter
from math import factorial


def predicted(m, n):
    """(number of code sets, unique weight), m,n positive."""
    if (m + n) % 3 == 0 and m <= 2*n and n <= 2*m:
        h = (2*n-m)//3
        v = (2*m-n)//3
        return factorial(m)*factorial(n)//(
            2**(h+v)*factorial(h)*factorial(v)), 2*(h+v)
    if m == 2*n + 1:
        return factorial(m)//2**n, 2*n
    if n == 2*m + 1:
        return factorial(n)//2**m, 2*m
    return 0, None


def neighborhoods(m, n):
    ans = []
    for r in range(m):
        for c in range(n):
            mask = 0
            for s in range(m):
                for d in range(n):
                    if (s == r) != (d == c):
                        mask |= 1 << (s*n+d)
            ans.append(mask)
    return ans


def direct_counts(m, n):
    """Check every subset, not just expected code shapes."""
    nb = neighborhoods(m,n)
    count_by_size = Counter()
    for mask in range(1 << (m*n)):
        if mask.bit_count() % 2:
            continue
        # An open-independent OLD set has exactly one selected
        # neighbor at every selected vertex.
        if any((nb[i]&mask).bit_count()!=1
               for i in range(m*n) if (mask >> i)&1):
            continue
        signatures = [u&mask for u in nb]
        if 0 in signatures or len(set(signatures)) != m*n:
            continue
        count_by_size[mask.bit_count()] += 1
    return dict(sorted(count_by_size.items()))


def check_finite_cases():
    cases = [(m,n) for m in range(1,5) for n in range(1,5)]
    cases += [(2,5),(3,5),(3,6),(4,5)]
    seen = set()
    for m,n in cases:
        if (m,n) in seen:
            continue
        seen.add((m,n))
        got = direct_counts(m,n)
        total,k = predicted(m,n)
        want = {k:total} if total else {}
        assert got == want, ((m,n),got,want)
        print(f"{m}x{n}: {got} ; predicted={want}")
    print(f"PASS: {len(seen)} rectangles exhaustively checked.")

if __name__ == '__main__':
    check_finite_cases()

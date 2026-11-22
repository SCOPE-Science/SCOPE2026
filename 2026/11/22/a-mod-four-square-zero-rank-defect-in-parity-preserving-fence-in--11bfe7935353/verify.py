"""Independent finite checks of saturated square-zero strata.

Run: python verify.py
Only Python standard library is required.
"""
from itertools import combinations
from math import comb


def direct_counts(n):
    """Enumerate maps directly, testing chain, parity, both fence directions, square."""
    universe = range(n)
    out = [0] * (n // 2 + 1)
    for r in range(n // 2 + 1):
        for domain in combinations(universe, r):
            dset = set(domain)
            remaining = tuple(x for x in universe if x not in dset)
            for image in combinations(remaining, r):
                # An increasing partial injection is uniquely determined by these lists.
                f = dict(zip(domain, image))
                assert len(f) == r and len(set(f.values())) == r
                # Test composition on the actual map; absence of square domain is required.
                if any(f[x] in f for x in f):
                    continue
                if any((x - f[x]) % 2 for x in f):
                    continue
                # Explicit fence-preservation and reflection, not the run proof.
                def less_fence(a, b):
                    return abs(a - b) == 1 and a % 2 == 0
                def respects(g):
                    return all(not less_fence(a, b) or less_fence(g[a], g[b])
                               for a in g for b in g)
                inv = {v: k for k, v in f.items()}
                if not respects(f) or not respects(inv):
                    continue
                out[r] += 1
    return out


def theorem(n):
    if n % 4 == 0:
        m = n // 4
        return n // 2, 2 ** m
    if n % 4 == 1:
        m = (n - 1) // 4
        return n // 2, (m + 1) * 2 ** m
    if n % 4 == 3:
        m = (n - 3) // 4
        return n // 2, (m + 2) * 2 ** m
    return n // 2 - 1, None


def compositions(t):
    if t == 0:
        yield ()
    for mask in range(1 << (t - 1)) if t else ():
        cuts = (0,) + tuple(j for j in range(1, t) if mask & (1 << (j - 1))) + (t,)
        yield tuple(b - a for a, b in zip(cuts, cuts[1:]))


def theoretical_run_count(n):
    k = n // 2
    if n % 4 == 0:
        return sum(2 for a in compositions(k) if all(x % 2 == 0 for x in a))
    if n % 4 == 1:
        if k == 0:
            return 1
        return sum(4 * len(a) for a in compositions(k)
                   if all(x % 2 == 0 for x in a))
    if n % 4 == 3:
        return sum(2 for a in compositions(k)
                   if sum(x % 2 for x in a) == 1)
    return None


def main():
    for n in range(1, 14):
        counts = direct_counts(n)
        r, expected = theorem(n)
        top = max(j for j, c in enumerate(counts) if c)
        assert top == r, (n, top, r)
        if expected is not None:
            assert counts[top] == expected, (n, counts, expected)
            assert theoretical_run_count(n) == expected
        print(f"n={n:2d} maximum_rank={top:2d} count={counts[top]:6d} theorem={'rank-only' if expected is None else 'rank-and-count'}")
    print('FENCE_SQUARE_ZERO_SATURATION_VERIFIED')


if __name__ == '__main__':
    main()

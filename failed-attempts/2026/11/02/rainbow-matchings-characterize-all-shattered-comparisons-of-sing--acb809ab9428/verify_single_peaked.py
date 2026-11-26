"""Exact small-order check of shattering for fixed-axis single-peaked rankings.

Uses only the Python standard library. It enumerates all single-peaked orders,
all shattered comparison supports, and the exact recursive Littlestone dimension.
"""
from functools import lru_cache
from itertools import combinations
from math import comb


def rankings(n):
    def low_to_high(lo, hi):
        if lo == hi:
            yield (lo,)
            return
        for order in low_to_high(lo + 1, hi):
            yield (lo,) + order
        for order in low_to_high(lo, hi - 1):
            yield (hi,) + order
    return tuple(tuple(reversed(p)) for p in low_to_high(0, n-1))


def nested_matching(support):
    endpoints = [v for e in support for v in e]
    if len(set(endpoints)) != len(endpoints):
        return False
    ordered = sorted(support)
    return all(ordered[i][0] < ordered[j][0] < ordered[j][1] < ordered[i][1]
               for i in range(len(ordered)) for j in range(i+1, len(ordered)))


def check(n):
    orders = rankings(n)
    assert len(orders) == 2**(n-1)
    queries = tuple(combinations(range(n), 2))
    whole = (1 << len(orders)) - 1
    masks = []
    for a, b in queries:
        masks.append(sum(1 << t for t, order in enumerate(orders)
                         if order.index(a) < order.index(b)))

    @lru_cache(None)
    def littlestone(mask):
        best = 0
        for qmask in masks:
            yes = mask & qmask
            no = mask & (whole ^ qmask)
            if yes and no:
                best = max(best, 1 + min(littlestone(yes), littlestone(no)))
        return best

    actual = set()
    def enumerate_shattered(support, classes, first):
        actual.add(tuple(support))
        for qi in range(first, len(queries)):
            qmask = masks[qi]
            a = [(part & qmask, part & (whole ^ qmask)) for part in classes]
            if all(yes and no for yes, no in a):
                enumerate_shattered(support + (qi,),
                                    tuple(x for pair in a for x in pair), qi+1)
    enumerate_shattered((), (whole,), 0)

    expected = set()
    for d in range(n//2+1):
        for endpoints in combinations(range(n), 2*d):
            pairs = tuple(sorted((endpoints[i], endpoints[-1-i])
                                 for i in range(d)))
            expected.add(tuple(queries.index(e) for e in pairs))
    assert actual == expected, (n, len(actual ^ expected))
    assert all(nested_matching(tuple(queries[j] for j in s)) for s in actual)
    counts = tuple(sum(len(s) == d for s in actual) for d in range(n//2+1))
    assert counts == tuple(comb(n,2*d) for d in range(n//2+1))
    assert len(actual) == len(orders)
    ld = littlestone(whole)
    assert ld == n-1, (n, ld)
    print(f'n={n}; concepts={len(orders)}; shattered={len(actual)}; '
          f'support_counts={counts}; VC={len(counts)-1}; Ldim={ld}; '
          f'ld_states={littlestone.cache_info().currsize}', flush=True)


if __name__ == '__main__':
    for n in range(1,10):
        check(n)
    print('SINGLE_PEAKED_SUPPORT_CLASSIFICATION_ALL_CHECKS_PASS')

"""Finite checks for the Littlestone dimension of finite prefix-cylinder classes.

Run with Python 3 (standard library only). The infinite-dimensional formula
is proved mathematically in RESULT.md, not inferred from these examples.
"""
from functools import lru_cache
from itertools import product, combinations
from math import comb


def cylinders(branching, height, include_empty=False):
    words = list(product(range(branching), repeat=height))
    concepts = {sum(1 << i for i, w in enumerate(words) if w[:j] == v)
                for j in range(height + 1)
                for v in product(range(branching), repeat=j)}
    if include_empty:
        concepts.add(0)
    return words, tuple(sorted(concepts))


def recursive_ldim(words, concepts):
    """Direct minimax recurrence on all membership-query partitions."""
    point_count = len(words)
    @lru_cache(None)
    def rank(family):
        best = 0
        for point in range(point_count):
            positive = tuple(c for c in family if c & (1 << point))
            negative = tuple(c for c in family if not c & (1 << point))
            if positive and negative:
                best = max(best, 1 + min(rank(positive), rank(negative)))
        return best
    return rank(concepts)


def vc_dimension(words, concepts):
    n = len(words)
    best = 0
    for r in range(n + 1):
        for support in combinations(range(n), r):
            traces = set()
            for c in concepts:
                traces.add(tuple(bool(c & (1 << i)) for i in support))
            if len(traces) == (1 << r):
                best = max(best, r)
    return best


def predicted_ldim(b, h, with_empty=False):
    # floor(log_2(h+1)) is bit_length(h+1)-1.
    k = (h + 1).bit_length()
    if with_empty:
        return k
    if h == 0:
        return 0
    if (b, h) == (2, 1):
        return 1
    return k


def predicted_vc(b, h, with_empty=False):
    if h == 0:
        return 1 if with_empty else 0
    if (b, h) == (2, 1) and not with_empty:
        return 1
    return 2


def verify():
    cases = [(2, h) for h in range(4)] + [(3, h) for h in range(3)] \
            + [(4, h) for h in range(2)]
    trials = 0
    for b, h in cases:
        if b ** h > 9:
            continue
        for with_empty in (False, True):
            words, concepts = cylinders(b, h, with_empty)
            ncon = sum(b ** i for i in range(h + 1)) + int(with_empty)
            assert len(concepts) == ncon, (b, h, with_empty, 'count')
            got = recursive_ldim(words, concepts)
            expected = predicted_ldim(b, h, with_empty)
            assert got == expected, (b, h, with_empty, got, expected)
            v = vc_dimension(words, concepts)
            ev = predicted_vc(b, h, with_empty)
            assert v == ev, (b, h, with_empty, v, ev)
            trials += 1
            print(f'PASS b={b} h={h} empty={with_empty} |C|={ncon} Ldim={got} VCdim={v}')
    # Finite induction arithmetic, an audit of the symbolic step (not an
    # infinite proof by enumeration).
    for h in range(2, 1001):
        assert predicted_ldim(2, h - 1, False) >= (h + 1).bit_length() - 1
        assert predicted_ldim(3, h - 1, False) >= (h + 1).bit_length() - 1
    print('ALL_PREFIX_BALL_CHECKS_PASS', trials, 'independent finite cases')


if __name__ == '__main__':
    verify()

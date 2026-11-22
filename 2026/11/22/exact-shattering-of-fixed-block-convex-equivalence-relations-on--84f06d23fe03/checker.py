"""Finite cross-checks for fixed-block interval partition shattering.

Run: python checker.py
No third-party dependencies are required.
"""
from itertools import combinations
from math import comb
import random


def queries(m):
    return [(a, b) for a in range(m) for b in range(a, m)]


def structural(m, c, support):
    """The proposed three-condition characterization (inclusive cut intervals)."""
    union = set()
    for a, b in support:
        union.update(range(a, b + 1))
    if m - len(union) < c:
        return False
    for i, (a, b) in enumerate(support):
        private = False
        for x in range(a, b + 1):
            if all(not (u <= x <= v) for j, (u, v) in enumerate(support) if i != j):
                private = True
                break
        if not private:
            return False
    # Standard greedy interval stabbing, independent of any incidence-pattern code.
    pierce = 0
    rightmost_piercer = -1
    for a, b in sorted(support, key=lambda pair: pair[1]):
        if rightmost_piercer < a:
            pierce += 1
            rightmost_piercer = b
    return pierce <= c


def direct_shattering(m, c, support):
    """Generate actual c-cut partitions and all their interval-query traces."""
    target_count = 1 << len(support)
    attained = set()
    for cuts in combinations(range(m), c):
        cutset = set(cuts)
        trace = 0
        for i, (a, b) in enumerate(support):
            if any(a <= x <= b for x in cutset):
                trace |= 1 << i
        attained.add(trace)
        if len(attained) == target_count:
            return True
    return False


def exhaustive_supports():
    checked = 0
    for m in range(1, 7):
        all_queries = queries(m)
        # All supports for m<=5; supports up to size 5 for m=6.
        cap = len(all_queries) if m <= 5 else 5
        for c in range(m + 1):
            for s in range(cap + 1):
                for support in combinations(all_queries, s):
                    lhs = structural(m, c, support)
                    rhs = direct_shattering(m, c, support)
                    assert lhs == rhs, (m, c, support, lhs, rhs)
                    checked += 1
    return checked


def direct_vc(m, c):
    """Find the largest shattered support by incremental trace-mask splitting."""
    cuts = list(combinations(range(m), c))
    all_queries = queries(m)
    full = (1 << len(cuts)) - 1
    masks = []
    for a, b in all_queries:
        mask = 0
        for j, cutset in enumerate(cuts):
            if any(a <= x <= b for x in cutset):
                mask |= 1 << j
        masks.append(mask)

    best = 0
    def expand(fibres, start, depth):
        nonlocal best
        best = max(best, depth)
        for i in range(start, len(all_queries)):
            mask = masks[i]
            split = []
            for fibre in fibres:
                left = fibre & mask
                right = fibre & (full ^ mask)
                if not left or not right:
                    break
                split.extend((left, right))
            else:
                expand(split, i + 1, depth + 1)
    expand([full], 0, 0)
    return best


def dimension_checks():
    total = 0
    for m in range(0, 9):
        for c in range(m + 1):
            observed = direct_vc(m, c)
            predicted = min(2 * c, m // 2, m - c)
            assert observed == predicted, (m, c, observed, predicted)
            total += 1
    return total


def sampled_supports():
    generator = random.Random(207118)
    checked = 0
    for m in (7, 8, 9, 10):
        all_queries = queries(m)
        for c in range(m + 1):
            for _ in range(80):
                s = generator.randrange(0, min(len(all_queries), 7) + 1)
                support = generator.sample(all_queries, s)
                assert structural(m, c, support) == direct_shattering(m, c, support), (m, c, support)
                checked += 1
    return checked


def main():
    exact = exhaustive_supports()
    dimensions = dimension_checks()
    samples = sampled_supports()
    print("EXACT_SUPPORT_COMPARISONS", exact)
    print("EXACT_VC_DIMENSION_CASES", dimensions)
    print("DETERMINISTIC_ADDITIONAL_SUPPORT_COMPARISONS", samples)
    print("EXAMPLE_DIMENSIONS", {m: [min(2*c, m//2, m-c) for c in range(m+1)] for m in (4, 6, 8)})
    print("FIXED_BLOCK_INTERVAL_SHATTERING_PASS")


if __name__ == '__main__':
    main()

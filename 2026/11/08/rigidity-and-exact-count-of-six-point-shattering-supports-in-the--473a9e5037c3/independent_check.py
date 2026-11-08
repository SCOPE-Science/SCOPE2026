"""Independent compressed-star test for six 3-sets with private points.

This is logically equivalent to the full query test when three unused
coordinates exist, but uses subset-covering rather than enumerating queries.
"""
from itertools import combinations, combinations_with_replacement
from math import comb, factorial


def realizable(pattern):
    pair_types = list(combinations(range(4), 2))
    stars = [sum(1 << i for i, j in enumerate(pattern) if x in pair_types[j])
             for x in range(4)]
    for target in range(64):
        found = False
        for mask in range(16):
            used = mask.bit_count()
            if used > 3:
                continue
            hit = 0
            for x in range(4):
                if (mask >> x) & 1:
                    hit |= stars[x]
            if (hit & ~target) == 0 and used + (target & ~hit).bit_count() <= 3:
                found = True
                break
        if not found:
            return False
    return True


def main():
    wins = []
    count = 0
    for pattern in combinations_with_replacement(range(6), 6):
        count += 1
        if realizable(pattern):
            wins.append(pattern)
    assert count == 462 and len(wins) == 4
    for p in wins:
        pairs = [list(combinations(range(4), 2))[k] for k in p]
        assert any(all(h in e for e in pairs) for h in range(4))
    assert 13 * comb(12, 3) * comb(9, 6) * factorial(6) // 8 == 21621600
    assert factorial(13) // (6 * 8 * 6) == 21621600
    print('INDEPENDENT_STAR_COVER_CLASSIFICATION_PASS', count, len(wins))


if __name__ == '__main__':
    main()

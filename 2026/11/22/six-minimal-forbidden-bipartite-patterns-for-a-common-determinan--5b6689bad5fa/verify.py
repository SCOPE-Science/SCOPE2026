"""Independent finite checks of the formulas and forbidden patterns in RESULT.md.
This finite computation supplements, rather than replaces, the general proof.
"""
from math import comb


def choose(n, k):
    return comb(n, k) if n >= k else 0


def expected(p, q):
    three = 6 * choose(p, 3) * choose(q, 3)
    four = (choose(p, 2) * choose(q, 2)
            + 2 * p * choose(p - 1, 2) * choose(q, 2)
            + 2 * q * choose(q - 1, 2) * choose(p, 2)
            + 6 * choose(p, 2) * choose(q, 4)
            + 6 * choose(q, 2) * choose(p, 4))
    return {k: v for k, v in [(3, three), (4, four)] if v}


def cross(mask, p, q):
    return any(
        all(not ((mask >> (i * q + j)) & 1) or i == row or j == col
            for i in range(p) for j in range(q))
        for row in range(p) for col in range(q)
    )


def direct_split(mask, p, q):
    """Semantic test; independently considers ALL assignment splits."""
    edges = [(i, j) for i in range(p) for j in range(q)
             if (mask >> (i * q + j)) & 1]
    for choice in range(1 << len(edges)):
        left = {i for k, (i, j) in enumerate(edges) if (choice >> k) & 1}
        right = {j for k, (i, j) in enumerate(edges) if not ((choice >> k) & 1)}
        if len(left) <= 1 and len(right) <= 1:
            return True
    return False


def type_of(mask, p, q):
    edges = [(i, j) for i in range(p) for j in range(q)
             if (mask >> (i * q + j)) & 1]
    rd = sorted([sum(1 for i, j in edges if i == t) for t in range(p) if any(i == t for i, j in edges)])
    cd = sorted([sum(1 for i, j in edges if j == t) for t in range(q) if any(j == t for i, j in edges)])
    sizes = {len(edges)}
    if len(edges) == 3:
        assert rd == [1, 1, 1] and cd == [1, 1, 1]
        return 'matching_3'
    if rd == [2, 2] and cd == [2, 2]:
        return 'cycle_4'
    if rd == [1, 1, 2] and cd == [2, 2]:
        return 'path_5_center_Y'
    if rd == [2, 2] and cd == [1, 1, 2]:
        return 'path_5_center_Z'
    if rd == [2, 2] and cd == [1, 1, 1, 1]:
        return 'two_stars_centers_Y'
    if rd == [1, 1, 1, 1] and cd == [2, 2]:
        return 'two_stars_centers_Z'
    raise AssertionError((rd, cd, edges))


def finite_fiber_check(p, q):
    observed = {}
    patterns = {}
    for mask in range(1 << (p * q)):
        good = cross(mask, p, q)
        if p <= 3 and q <= 3:
            assert good == direct_split(mask, p, q), (p, q, mask)
        if not good and all(cross(mask ^ (1 << k), p, q)
                            for k in range(p * q) if (mask >> k) & 1):
            size = mask.bit_count()
            observed[size] = observed.get(size, 0) + 1
            tag = type_of(mask, p, q)
            patterns[tag] = patterns.get(tag, 0) + 1
    assert observed == expected(p, q), (p, q, observed, expected(p, q))
    return patterns


def multi_fiber_check():
    """For 2x2x2 inputs, compare all 256 teams to 2^8 split semantics."""
    p = q = 2
    tuples = [(a, b, c) for a in range(2) for b in range(p) for c in range(q)]
    minimal = {}
    for mask in range(1 << len(tuples)):
        good = True
        for a in range(2):
            local = sum(1 << (b * q + c) for index, (x, b, c) in enumerate(tuples)
                        if x == a and (mask >> index) & 1)
            if not cross(local, p, q):
                good = False
                break
        if not good:
            is_minimal = True
            for index in range(len(tuples)):
                if not (mask >> index) & 1:
                    continue
                reduced = mask ^ (1 << index)
                if not all(cross(sum(1 << (b * q + c)
                                     for k, (x, b, c) in enumerate(tuples)
                                     if x == a and (reduced >> k) & 1), p, q)
                           for a in range(2)):
                    is_minimal = False
                    break
            if is_minimal:
                minimal[mask.bit_count()] = minimal.get(mask.bit_count(), 0) + 1
    assert minimal == {4: 2}, minimal


if __name__ == '__main__':
    tested = [(p, q) for p in range(1, 5) for q in range(1, 5)]
    for p, q in tested:
        got = finite_fiber_check(p, q)
        print(f'alphabets {p}x{q}: {expected(p, q)}; patterns {got}')
    multi_fiber_check()
    print('VERIFY_OK 16 alphabet pairs; all 2x2x2 team subsets; raw split semantics through 3x3')

"""Exact, finite checks of the five-vertex illumination incidence theorem.

The mathematical proof in RESULT.md applies to all strictly convex pentagons.
Here Q encodes the exterior turns as integer multiples of pi/Q.  No
floating-point trigonometry or optimization library is used.
"""
from itertools import product
from functools import lru_cache


def incidence_masks(b, Q):
    """Generic direction cells for a cyclic edge-turn list b, sum(b)=2Q."""
    E = [0]
    for j in range(1, 5):
        E.append(E[-1] + b[j])
    assert (E[-1] + b[0]) == 2 * Q
    critical = sorted(set([v % (2 * Q) for e in E for v in (e, e + Q)]))
    masks = set()
    for i, a in enumerate(critical):
        c = critical[(i + 1) % len(critical)]
        if i == len(critical) - 1:
            c += 2 * Q
        u2 = a + c  # twice a generic angular coordinate (in units of pi/Q)
        mask = 0
        for j in range(5):
            if all(0 < ((u2 - 2 * E[h]) % (4 * Q)) < 2 * Q
                   for h in ((j - 1) % 5, j)):
                mask |= 1 << j
        masks.add(mask)
    return frozenset(masks - {0})


def pair_graph(masks):
    return frozenset((i, j) for i in range(5) for j in range(i + 1, 5)
                     if any((mask & (1 << i)) and (mask & (1 << j)) for mask in masks))


def predicted_pairs(b, Q):
    out = set()
    for i in range(5):
        if b[i] + b[(i + 1) % 5] < Q:
            out.add(tuple(sorted((i, (i + 1) % 5))))
        if b[i] + b[(i + 1) % 5] + b[(i + 2) % 5] < Q:
            out.add(tuple(sorted((i, (i + 2) % 5))))
    return frozenset(out)


def minimum_cover(masks, k):
    """Breadth-first search on five-dimensional capped coverage states."""
    vectors = [tuple(int(bool(mask & (1 << i))) for i in range(5)) for mask in masks]
    frontier = {(0, 0, 0, 0, 0)}
    goal = (k,) * 5
    for count in range(1, 3 * k + 1):
        frontier = {tuple(min(k, state[j] + vec[j]) for j in range(5))
                    for state in frontier for vec in vectors}
        if goal in frontier:
            return count
    raise AssertionError('Three-direction upper bound failed')


def classify(b, Q):
    bad = [i for i in range(5) if b[i] + b[(i + 1) % 5] >= Q]
    assert len(bad) <= 2
    if len(bad) == 2:
        assert (bad[1] - bad[0]) % 5 in (1, 4)
    return not bad


def run():
    total = 0
    profiles = {}
    boundary_cases = 0
    good = bad = 0
    for Q in range(5, 14):
        for a, b, c, d in product(range(1, Q), repeat=4):
            e = 2 * Q - a - b - c - d
            if not 1 <= e < Q:
                continue
            turns = (a, b, c, d, e)
            total += 1
            masks = incidence_masks(turns, Q)
            assert pair_graph(masks) == predicted_pairs(turns, Q)
            favorable = classify(turns, Q)
            if favorable:
                good += 1
                assert max(mask.bit_count() for mask in masks) <= 2
            else:
                bad += 1
                assert any(not any(((mask >> i) & 1) + ((mask >> j) & 1) > 1
                                   for mask in masks)
                           and not any(((mask >> i) & 1) + ((mask >> h) & 1) > 1
                                       for mask in masks)
                           and not any(((mask >> j) & 1) + ((mask >> h) & 1) > 1
                                       for mask in masks)
                           for i in range(5) for j in range(i + 1, 5)
                           for h in range(j + 1, 5))
            if any(turns[i] + turns[(i + 1) % 5] == Q for i in range(5)):
                boundary_cases += 1
            profiles.setdefault(masks, favorable)
            assert profiles[masks] == favorable
    assert good > 0 and bad > 0 and boundary_cases > 0
    # A concrete nonsymmetric convex pentagon has two consecutive
    # failed angle-pair tests, determined with integer cross products.
    points = ((0, 0), (1, 0), (3, 1), (0, 4), (-2, 1))
    edges = [tuple(points[(i + 1) % 5][c] - points[i][c] for c in range(2))
             for i in range(5)]
    cross = lambda x, y: x[0] * y[1] - x[1] * y[0]
    assert all(cross(edges[i], edges[(i + 1) % 5]) > 0 for i in range(5))
    bad_turn_pairs = [i for i in range(5)
                      if cross(edges[(i - 1) % 5], edges[(i + 1) % 5]) <= 0]
    assert bad_turn_pairs == [2, 3]
    print("Incidence profiles:",len(profiles),flush=True)
    for masks, favorable in profiles.items():
        for k in range(1, 5):
            observed = minimum_cover(masks, k)
            expected = (5*k + 1)//2 if favorable else 3*k
            assert observed == expected, (masks, k, observed, expected)
    print('PASS: %d exact rational-turn pentagons; %d favorable, %d other; %d boundary cases; %d incidence profiles; all incidence profiles m=1..4.'
          % (total, good, bad, boundary_cases, len(profiles)))

if __name__ == '__main__':
    run()

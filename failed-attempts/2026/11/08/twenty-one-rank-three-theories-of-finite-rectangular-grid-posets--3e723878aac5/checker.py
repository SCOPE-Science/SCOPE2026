#!/usr/bin/env python3
"""Exact finite certificates for rank-three theories of two-chain grid posets.

No external dependencies. Run with: python3 checker.py
"""
from itertools import product
from functools import lru_cache


def grid(a, b):
    assert 1 <= a <= b
    return tuple(product(range(a), range(b)))


def relation(x, y):
    if x == y:
        return 0
    if x[0] <= y[0] and x[1] <= y[1]:
        return 1
    if x[0] >= y[0] and x[1] >= y[1]:
        return 2
    return 3


def three_round_signature(a, b):
    """Exact 3-round EF invariant via sets of all atomic triple types."""
    pts = grid(a, b)
    n = len(pts)
    rel = tuple(tuple(relation(x, y) for y in pts) for x in pts)

    # Atomic type of x,y,z (equality/ordered comparability for every pair).
    pair_profiles = {}
    for i in range(n):
        for j in range(n):
            triple_types = frozenset(
                (rel[i][j], rel[i][k], rel[j][k]) for k in range(n)
            )
            pair_profiles[i, j] = (rel[i][j], triple_types)
    return frozenset(
        frozenset(pair_profiles[i, j] for j in range(n))
        for i in range(n)
    )


def expected_representative(a, b):
    # This is the CLAIM, not an algorithm used to compute the signatures.
    if a == 1:
        return (1, min(b, 7))
    if a == 2:
        return (2, min(b, 6))
    if a == 3:
        return (3, min(b, 6))
    if a == 4:
        return (4, min(b, 6))
    return (5, 5) if (a, b) == (5, 5) else (5, 6)


def exact_small_ef(a, b, c, d):
    """Separate directly recursive Spoiler/Duplicator game, 3 rounds."""
    P, Q = grid(a, b), grid(c, d)
    rp, rq = tuple(tuple(relation(x, y) for y in P) for x in P), \
             tuple(tuple(relation(x, y) for y in Q) for x in Q)

    @lru_cache(maxsize=None)
    def dupl_wins(r, ids_p, ids_q):
        if any(rp[ids_p[i]][ids_p[j]] != rq[ids_q[i]][ids_q[j]]
               for i in range(len(ids_p)) for j in range(len(ids_p))):
            return False
        if r == 0:
            return True
        for x in range(len(P)):
            if not any(dupl_wins(r - 1, ids_p + (x,), ids_q + (y,))
                       for y in range(len(Q))):
                return False
        for y in range(len(Q)):
            if not any(dupl_wins(r - 1, ids_p + (x,), ids_q + (y,))
                       for x in range(len(P))):
                return False
        return True
    return dupl_wins(3, (), ())


def main():
    cases = [(a, b) for a in range(1, 8) for b in range(a, 8)]
    assert len(cases) == 28
    profiles = {g: three_round_signature(*g) for g in cases}
    partitions = {}
    for g, signature in profiles.items():
        partitions.setdefault(signature, []).append(g)
    assert len(partitions) == 21, len(partitions)

    # Compare EVERY pair's independent exact signature equality to claimed
    # parameter classification; this checks same-class and distinct-class cases.
    checks = 0
    for g in cases:
        for h in cases:
            expected = expected_representative(*g) == expected_representative(*h)
            assert (profiles[g] == profiles[h]) == expected, (g, h)
            checks += 1
    assert checks == 784

    # Independent direct three-move game, restricted to manageable orders.
    small = [(a, b) for a in range(1, 5) for b in range(a, 5)]
    for i, g in enumerate(small):
        for h in small[i:]:
            assert exact_small_ef(*g, *h) == (profiles[g] == profiles[h]), (g,h)

    # End class has minimum 5 x 6 = 30 grid points within that class.
    terminal = [g for g in cases if expected_representative(*g) == (5, 6)]
    assert sorted(terminal, key=lambda x:x[0]*x[1])[0] == (5, 6)
    assert terminal == [(5, 6), (5, 7), (6, 6), (6, 7), (7, 7)]
    # The 25-point square is distinguishable already by this 3-round invariant.
    assert profiles[(5, 5)] != profiles[(5, 6)]
    print("GRID_RANK3_CERTIFICATE_OK cases=28 classes=21 pair_checks=784"
          " direct_games=55 terminal_minimum=30")


if __name__ == "__main__":
    main()

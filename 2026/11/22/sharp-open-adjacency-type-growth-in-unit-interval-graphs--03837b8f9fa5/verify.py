"""Reproducible finite checks for exact unit-interval adjacency traces.

Run with: python3 verify.py
All geometry is rational (integers represent quarters of a unit).
The all-size argument is in RESULT.md; finite checks do not replace it.
"""
from itertools import combinations, combinations_with_replacement


def signatures(centres, marked):
    """Independent adjacency-matrix evaluation, scaled unit length four."""
    n = len(centres)
    adj = [[i != j and abs(centres[i] - centres[j]) <= 4
            for j in range(n)] for i in range(n)]
    closed = [[i == j or adj[i][j] for j in range(n)] for i in range(n)]
    return ({tuple(j for j in marked if adj[i][j]) for i in range(n)},
            {tuple(j for j in marked if closed[i][j]) for i in range(n)})


def limit(m):
    return 1 if m == 0 else min(2**m, 3*m)


def witness(m):
    """Marked centres spaced 3/4; put witnesses in all breakpoint cells."""
    a = [3*i for i in range(m)]
    if m == 0:
        return [0], set()
    breakpoints = sorted({x+step for x in a for step in [-4, 4]})
    # All breakpoints lie at integers; doubled coordinates allow half-integers.
    positions2 = [2*breakpoints[0]-2]
    positions2 += [breakpoints[i]+breakpoints[i+1]
                   for i in range(len(breakpoints)-1)]
    # Map scale 4 to scale 8; marks still distinct vertices if coincident
    # coordinate representatives are present (we avoid equality below).
    centres = [2*x for x in a] + positions2  # one tail + all interior cells
    return centres, set(range(m))


def geom_types(centres, marked):
    n = len(centres)
    op = {tuple(j for j in marked if i != j and abs(centres[i] - centres[j]) <= 8)
          for i in range(n)}
    cl = {tuple(j for j in marked if abs(centres[i] - centres[j]) <= 8)
          for i in range(n)}
    return op, cl


def run():
    tests = 0
    for n in range(1, 8):
        # Exhaust all multisets of n centres on a nine-point lattice.
        for xs in combinations_with_replacement(range(9), n):
            for m in range(n+1):
                for a in combinations(range(n), m):
                    o, c = signatures(xs, a)
                    assert len(o) <= limit(m), (xs, a, len(o), limit(m))
                    assert len(c) <= (1 if m == 0 else 2*m)
                    tests += 1
    for m in range(0, 41):
        xs, A = witness(m)
        op, cl = geom_types(xs, A)
        assert len(op) == limit(m), (m, len(op), limit(m))
        assert len(cl) == (1 if m == 0 else 2*m), (m, len(cl))
        if m >= 4:
            assert len(xs) == 3*m, (m, len(xs))
            assert len(op) == len(xs), (m, len(op), len(xs))
    print('GRID_CASES_OK', tests)
    print('ALL_SIZE_CONSTRUCTED_WITNESSES_OK', '0..40')
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    run()

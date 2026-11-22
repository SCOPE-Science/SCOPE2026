"""Exact integer certificate for Kuhn-packet octahedral frame census.

Requires Python 3 and only the standard library. Recomputes candidates,
Chebyshev LP facet tests, and signed-coordinate orbit decomposition.
No floating-point arithmetic is used.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from fractions import Fraction

SIGNS = tuple(product((-1, 1), repeat=3))
PARITY = {z: tuple(e for e in SIGNS if e[0] * e[1] * e[2] == z)
          for z in (-1, 1)}
OPPOSITE_REPS = tuple(e for e in SIGNS if e[0] == 1)
ZERO = (0, 0, 0)


def dot(e, p):
    return sum(x * y for x, y in zip(e, p))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def l1(v):
    return sum(abs(i) for i in v)


def determinant(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def square_solve(a, b):
    """Return a unique rational solution or None for a square system."""
    n = len(a)
    m = [[Fraction(a[i][j]) for j in range(n)] + [Fraction(b[i])]
         for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if m[i][j]), None)
        if pivot is None:
            return None
        m[j], m[pivot] = m[pivot], m[j]
        den = m[j][j]
        m[j] = [v / den for v in m[j]]
        for i in range(n):
            if i != j:
                fac = m[i][j]
                m[i] = [m[i][t] - fac * m[j][t] for t in range(n + 1)]
    return tuple(m[i][n] for i in range(n))


def extreme_sign_distributions():
    """Enumerate basic feasible solutions of the 4-by-8 dual constraints."""
    rows = [[1 for e in SIGNS]] + [[e[i] for e in SIGNS] for i in range(3)]
    extrema = []
    for size in range(1, 5):
        for cols in combinations(range(8), size):
            for rset in combinations(range(4), size):
                matrix = [[rows[i][j] for j in cols] for i in rset]
                target = [int(i == 0) for i in rset]
                weights = square_solve(matrix, target)
                if weights is None:
                    continue
                if not all(w > 0 for w in weights):
                    continue
                if any(sum(weights[k] * rows[i][j]
                           for k, j in enumerate(cols)) != int(i == 0)
                       for i in range(4)):
                    continue
                extrema.append((tuple(SIGNS[j] for j in cols), weights))
                break
    return extrema


def tetra_fits(vertices, twice_radius):
    """Exact criterion for an integer tetrahedron to fit an l1-ball.

    For radius R=twice_radius/2, the four opposite-pair width
    inequalities require <= twice_radius; each parity-quartet sum
    requires <= 2*twice_radius.
    """
    heights = {e: max(dot(e, v) for v in vertices) for e in SIGNS}
    if any(heights[e] + heights[tuple(-t for t in e)] > twice_radius
           for e in OPPOSITE_REPS):
        return False
    return all(sum(heights[e] for e in PARITY[parity]) <= 2 * twice_radius
               for parity in (-1, 1))


def tetra_below_three_halves(vertices):
    """Integer vertices: exact strict radius < 3/2 inequalities.

    Opposite-pair width must be <= 2 (an integer < 3), while
    each four-sign parity sum must be <= 5 (an integer < 6).
    """
    heights = {e: max(dot(e, v) for v in vertices) for e in SIGNS}
    if any(heights[e] + heights[tuple(-t for t in e)] > 2
           for e in OPPOSITE_REPS):
        return False
    return all(sum(heights[e] for e in PARITY[parity]) <= 5
               for parity in (-1, 1))


def packet_below_three_halves(frame):
    for ordered in permutations(frame):
        a, b, c = ordered
        vertices = (ZERO, a, add(a, b), add(add(a, b), c))
        if not tetra_below_three_halves(vertices):
            return False
    return True


def packet_fits(frame, twice_radius):
    for ordered in permutations(frame):
        a, b, c = ordered
        vertices = (ZERO, a, add(a, b), add(add(a, b), c))
        if not tetra_fits(vertices, twice_radius):
            return False
    return True


def necessary_sums_fit(frame, max_l1):
    a, b, c = frame
    return all(l1(v) <= max_l1 for v in
               (add(a, b), add(a, c), add(b, c), add(add(a, b), c)))


def possible_columns(max_l1):
    return tuple(v for v in product(range(-max_l1, max_l1 + 1), repeat=3)
                 if 0 < l1(v) <= max_l1)


def enumerate_at(twice_radius):
    pool = possible_columns(twice_radius)
    necessary = Counter()
    accepted = Counter()
    frames = set()
    for frame in combinations(pool, 3):
        if not necessary_sums_fit(frame, twice_radius):
            continue
        det = abs(determinant(*frame))
        if not det:
            continue
        necessary[det] += 1
        if packet_fits(frame, twice_radius):
            accepted[det] += 1
            frames.add(frame)
    return pool, necessary, accepted, frames


def enumerate_strict_lower():
    """Complete search below 3/2; not equivalent to radius <= 1."""
    pool = possible_columns(2)
    necessary = 0
    winners = set()
    for frame in combinations(pool, 3):
        if not necessary_sums_fit(frame, 2):
            continue
        if determinant(*frame) == 0:
            continue
        necessary += 1
        if packet_below_three_halves(frame):
            winners.add(frame)
    return pool, necessary, winners


def symmetry_images(frame):
    for coords in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            yield tuple(sorted(tuple(signs[j] * b[coords[j]] for j in range(3))
                               for b in frame))


def orbits(frames):
    unused = set(frames)
    entries = []
    while unused:
        seed = min(unused)
        orbit = set(symmetry_images(seed))
        assert orbit <= frames, 'The accepted set must be invariant.'
        unused.difference_update(orbit)
        det = abs(determinant(*seed))
        entries.append((det, len(orbit), min(orbit)))
    entries.sort()
    return entries


def main():
    dual = extreme_sign_distributions()
    assert len(dual) == 6
    assert Counter(len(support) for support, weights in dual) == {2: 4, 4: 2}
    assert all(all(w == Fraction(1, len(support)) for w in weights)
               for support, weights in dual)
    pool2, need2, frames2 = enumerate_strict_lower()
    assert len(pool2) == 24
    assert not frames2, ('A frame below radius 3/2 would contradict optimality.', frames2)
    pool3, need3, accept3, frames3 = enumerate_at(3)
    assert len(pool3) == 62
    assert dict(sorted(need3.items())) == {1: 512, 2: 408, 3: 288, 4: 56}
    assert dict(sorted(accept3.items())) == {1: 512, 2: 408, 4: 8}
    assert len(frames3) == 928
    entries = orbits(frames3)
    orbit_hist = Counter(det for det, size, representative in entries)
    assert dict(sorted(orbit_hist.items())) == {1: 12, 2: 10, 4: 1}
    assert sum(size for det, size, representative in entries) == 928
    assert len(entries) == 23
    print('Chebyshev dual: 4 opposite pairs and 2 parity tetrahedra.')
    print('Radius less than 3/2: 24 candidate nonzero columns,', need2, 'filtered independent frames, 0 fitting packets.')
    print('Radius at most 3/2: 62 candidate nonzero columns.')
    print('After necessary subset-sum filter: ', dict(sorted(need3.items())))
    print('After six exact packet checks:     ', dict(sorted(accept3.items())))
    print('Symmetry-orbit counts by index:    ', dict(sorted(orbit_hist.items())))
    print('Orbit representatives: index orbit_size column_triple')
    for entry in entries:
        print(*entry)
    print('PASS: complete integer arithmetic enumeration and orbit partition')


if __name__ == '__main__':
    main()

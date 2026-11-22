"""Reproduce reflection-fixed simplicial models of pure strong-cycle complexes.

Python 3 standard library. Facets are the maximal strong Morse matchings
of the unfilled cycle, in the published two-consecutive-gap form.
"""
from itertools import combinations


def all_facets(n):
    assert n >= 6
    return [frozenset((2 * ((b + 2 + k) % n) + int(k >= j))
                      for k in range(n - 2))
            for b in range(n) for j in range(n - 1)]


def reflected_vertex(v, n, a):
    return 2 * ((a - (v // 2) - 1) % n) + 1 - (v % 2)


def observed_orbit_facets(n, a):
    fv = all_facets(n)
    orbits = sorted({tuple(sorted((v, reflected_vertex(v, n, a))))
                     for v in range(2 * n)})
    assert len(orbits) == n and all(len(o) == 2 for o in orbits)
    projected = [frozenset(i for i, o in enumerate(orbits)
                           if all(v in f for v in o)) for f in fv]
    observed = set(projected)
    maximal = {s for s in observed if not any(s < t for t in observed)}
    return orbits, maximal


def predicted_orbit_facets(n, a, orbits):
    assert a in (0, 1)
    m = n // 2
    if n % 2:
        assert a == 0
        pa = set(range(1, m))
        pb = set(range(0, m - 1))
    elif a == 0:
        pa = set(range(1, m))
        pb = set(range(0, m - 1))
    else:
        pa = set(range(2, m))
        pb = set(range(1, m - 1))

    oi = {frozenset(o): i for i, o in enumerate(orbits)}
    rho = lambda j: (a - j - 1) % n
    # The positive branch is the displayed positive-edge interval; the other
    # branch is the displayed negative-edge interval.
    positive = frozenset(oi[frozenset((2 * j, 2 * rho(j) + 1))] for j in pa)
    negative = frozenset(oi[frozenset((2 * j + 1, 2 * rho(j)))] for j in pb)
    assert positive.isdisjoint(negative) and positive and negative
    return {positive, negative}


def orbit_faces(maximal):
    faces = {frozenset()}
    for f in maximal:
        z = list(f)
        for k in range(1, len(z) + 1):
            faces.update(map(frozenset, combinations(z, k)))
    return faces


def main():
    total_tests = 0
    total_faces = 0
    full_invariant_checks = 0
    for n in range(6, 51):
        for a in ((0, 1) if n % 2 == 0 else (0,)):
            orbits, maximal = observed_orbit_facets(n, a)
            formula = predicted_orbit_facets(n, a, orbits)
            assert maximal == formula, (n, a, maximal ^ formula)
            m = n // 2
            size = m - 1 if (n % 2 or a == 0) else m - 2
            assert {len(f) for f in maximal} == {size}
            total_tests += 1
            if n <= 17:
                faces = orbit_faces(maximal)
                assert len(faces) == 2 ** (size + 1) - 1
                # The augmented Euler alternating orbit-count equals -1, so
                # the reduced geometric Lefschetz number is +1.
                assert -sum((-1) ** len(f) for f in faces) == 1
                total_faces += len(faces)
            if n <= 11:
                # Independent face-level approach: enumerate every simplex
                # of the original matching complex and test reflection directly.
                direct = set()
                for facet in all_facets(n):
                    ff = list(facet)
                    for z in range(1 << len(ff)):
                        simplex = frozenset(ff[t] for t in range(len(ff))
                                             if (z >> t) & 1)
                        if {reflected_vertex(v, n, a) for v in simplex} != set(simplex):
                            continue
                        direct.add(frozenset(i for i, o in enumerate(orbits)
                                            if set(o).issubset(simplex)))
                assert direct == orbit_faces(formula), (n, a, len(direct))
                full_invariant_checks += 1
    # The conjugacy class of every reflection equals one of the tested axes:
    # rotations translate a by two and conjugate orbit complexes.
    print(f'ALL_VERIFY_OK checked_axes={total_tests} n_min=6 n_max=50 '
          f'fully_enumerated_fixed_faces={total_faces} full_invariant_axes={full_invariant_checks}')

if __name__ == '__main__':
    main()

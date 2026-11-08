"""Reproducible numerical checks for complete-bipartite zonotope incenter loci.

This finite test corroborates, but does not replace, the all-parameter proof.
Standard-library Python 3.9+; run: python verify_bipartite_centers.py
"""
from itertools import combinations
from math import comb, floor, sqrt
from random import Random


def constants(p, q):
    n = p + q
    rho = (p / 2) * sqrt(n / (n - 1))
    delta = (q - p) / 2
    middle = p * q / 4 - p / 2 * sqrt((n * n // 4) / (n - 1))
    return rho, delta, middle


def cut_slack(p, q, a, b):
    n = p + q
    s = a + b
    if s == 0 or s == n:
        return float('inf')
    rho, _, _ = constants(p, q)
    boundary = a * (q - b) + b * (p - a)
    norm = sqrt(s * (n - s) / n)
    return boundary / 2 - rho * norm


def predicted(p, q, x, tol=1e-9):
    _, delta, middle = constants(p, q)
    if abs(sum(x)) > tol or max(abs(v) for v in x) > delta + tol:
        return False
    if p % 2 == 0:
        for subset in combinations(range(p), p // 2):
            if abs(sum(x[i] for i in subset)) > middle + tol:
                return False
    return True


def from_all_cuts(p, q, x, tol=1e-9):
    # The entries on the q-vertex part are all zero. Every cut depends
    # only on its intersection with the p-vertex part and the number
    # of q-part vertices it contains.
    for a in range(p + 1):
        for subset in combinations(range(p), a):
            t = abs(sum(x[i] for i in subset))
            for b in range(q + 1):
                if t > cut_slack(p, q, a, b) + tol:
                    return False
    return True


def check_pair(p, q, rng):
    rho, delta, middle = constants(p, q)
    assert rho > 0
    # Check the spectral-gap prediction independently against all
    # cut-cardinality pairs; exclude empty/full vertex sets.
    best = 1e99
    best_params = []
    for a in range(p + 1):
        for b in range(q + 1):
            s = a + b
            if s in (0, p + q):
                continue
            value = (a * (q - b) + b * (p - a)) / sqrt(s * (p + q - s) / (p + q))
            if value < best - 1e-9:
                best = value
                best_params = [(a, b)]
            elif abs(value - best) < 1e-9:
                best_params.append((a, b))
    assert abs(best - 2 * rho) < 1e-9
    if q > p:
        assert set(best_params) == {(0, 1), (p, q - 1)}
    else:
        assert set(best_params) == {(0, 1), (p, q - 1), (1, 0), (p - 1, q)}

    for _ in range(120):
        vals = [rng.uniform(-delta * 1.4, delta * 1.4) for i in range(p - 1)]
        vals.append(-sum(vals))
        expected = predicted(p, q, vals)
        actual = from_all_cuts(p, q, vals)
        assert expected == actual, (p, q, vals, delta, middle, expected, actual)
    if q == p:
        assert from_all_cuts(p, q, [0.0] * p)
    elif p % 2 == 0:
        a = p // 2
        special = [delta] * a + [-delta] * a
        assert (middle >= a * delta - 1e-9) == (p + q <= p * p - 1)
        assert predicted(p, q, special) == (p + q <= p * p - 1)


def check_cube_vertex_counts():
    for p in range(4, 12):
        delta = 1.0
        candidates = []
        for zero in range(p):
            if p % 2 == 0:
                break
            other = [i for i in range(p) if i != zero]
            for plus in combinations(other, (p - 1) // 2):
                v = [-delta] * p
                v[zero] = 0
                for i in plus:
                    v[i] = delta
                candidates.append(tuple(v))
        if p % 2 == 0:
            for plus in combinations(range(p), p // 2):
                v = [-delta] * p
                for i in plus:
                    v[i] = delta
                candidates.append(tuple(v))
        expected = comb(p, p // 2) if p % 2 == 0 else p * comb(p - 1, (p - 1) // 2)
        assert len(set(candidates)) == expected
        assert all(sum(v) == 0 for v in candidates)


def main():
    rng = Random(134971)
    for p, q in [(4, 4), (4, 5), (4, 11), (4, 12), (4, 15),
                 (5, 5), (5, 6), (5, 20), (6, 6), (6, 7),
                 (6, 29), (6, 30), (7, 7), (7, 8), (7, 50)]:
        check_pair(p, q, rng)
    check_cube_vertex_counts()
    print('BIPARTITE_GRAPHICAL_ZONOTOPE_CENTER_CHECKS_PASSED')

if __name__ == '__main__':
    main()

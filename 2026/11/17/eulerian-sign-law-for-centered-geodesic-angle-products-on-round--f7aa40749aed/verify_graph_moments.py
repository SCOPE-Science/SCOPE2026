"""Reproduce finite circuit-partition identities and numerical angular-cycle checks.

Run: python verify_graph_moments.py (requires NumPy >= 1.24).
All mathematical results are proved in RESULT.md; sampling is a non-proof diagnostic.
"""
from collections import Counter
from itertools import product
from math import pi
import numpy as np


def pairings(items):
    items = tuple(items)
    if not items:
        yield ()
    else:
        first = items[0]
        for j in range(1, len(items)):
            second = items[j]
            for rest in pairings(items[1:j] + items[j + 1:]):
                yield ((first, second),) + rest


def circuit_polynomial(n, edges):
    """Returns exponents and coefficients in Z_G(d) by local pairings."""
    inc = [[] for _ in range(n)]
    for e, (u, v) in enumerate(edges):
        inc[u].append(2 * e)
        inc[v].append(2 * e + 1)
    if any(len(h) % 2 for h in inc):
        return {}
    pairing_choices = [tuple(pairings(h)) for h in inc]
    poly = Counter()
    for local in product(*pairing_choices):
        parent = list(range(2 * len(edges)))
        def root(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def join(a, b):
            aa, bb = root(a), root(b)
            if aa != bb:
                parent[aa] = bb
        for e in range(len(edges)):
            join(2 * e, 2 * e + 1)
        for vertex_pairs in local:
            for a, b in vertex_pairs:
                join(a, b)
        loops = len({root(i) for i in range(2 * len(edges))})
        poly[loops] += 1
    return dict(poly)


def direct_coordinate_numerator(n, edges, dimension):
    """Independent sum over coordinate colors, avoiding pairing enumeration."""
    ans = 0
    for assignment in product(range(dimension), repeat=len(edges)):
        counts = [[0] * dimension for _ in range(n)]
        for (u, v), color in zip(edges, assignment):
            counts[u][color] += 1
            counts[v][color] += 1
        term = 1
        for histogram in counts:
            if any(c % 2 for c in histogram):
                term = 0
                break
            for c in histogram:
                for k in range(1, c, 2):
                    term *= k
        ans += term
    return ans


def cycle_moment_s2(length, count=500):
    """Signed exact arc-length cycle moment via spherical harmonics."""
    c = 1.0
    total = 0.0
    for k in range(count):
        lam = pi * c * c / (8.0 * (k + 1)**2)
        total += (4 * k + 3) * lam**length
        c *= (2 * k + 1) / (2 * k + 2)
    # Upper bound for discarded terms using c_k <= 1 and integral comparison.
    r = length
    tail = 4 * (pi / 8)**r * ((count + 1)**(1 - 2 * r)
                                  + count**(2 - 2 * r) / (2 * r - 2))
    return (-1)**length * total, tail


def simulated_cycle(length, sample_count, seed):
    rng = np.random.default_rng(seed)
    vals = []
    for count in range(0, sample_count, 50000):
        n = min(50000, sample_count - count)
        x = rng.standard_normal((n, length, 3))
        x /= np.linalg.norm(x, axis=-1, keepdims=True)
        dot = np.sum(x * np.roll(x, -1, axis=1), axis=-1)
        ang = -np.arcsin(np.clip(dot, -1.0, 1.0))
        vals.append(np.prod(ang, axis=-1))
    z = np.concatenate(vals)
    return float(z.mean()), float(z.std(ddof=1) / np.sqrt(len(z)))


def main():
    triangle = [(0, 1), (1, 2), (0, 2)]
    square = [(0, 1), (1, 2), (2, 3), (0, 3)]
    bowtie = [(0, 1), (1, 2), (0, 2), (0, 3), (3, 4), (0, 4)]
    complete5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    complete24 = [(i, j) for i in range(2) for j in range(2, 6)]
    cases = [(3, triangle), (4, square), (5, bowtie), (5, complete5), (6, complete24)]
    for n, edges in cases:
        poly = circuit_polynomial(n, edges)
        for d in (2, 3):
            from_pairings = sum(multiplicity * d**loops for loops, multiplicity in poly.items())
            from_coordinates = direct_coordinate_numerator(n, edges, d)
            assert from_pairings == from_coordinates, (n, d, poly, from_coordinates)
        print('exact', n, len(edges), sorted(poly.items()))
    assert circuit_polynomial(6, complete24) == {1: 6, 2: 3}
    assert circuit_polynomial(5, complete5) == {1: 132, 2: 96, 3: 15}
    assert circuit_polynomial(5, bowtie) == {1: 2, 2: 1}
    for length in (3, 4):
        exact, error = cycle_moment_s2(length)
        assert error < 1e-10
        assert (-1)**length * exact > 3**(1-length)
        estimate, se = simulated_cycle(length, 900000, 310521 + length)
        assert abs(estimate - exact) < 6 * se + 0.001, (length, estimate, exact, se)
        print('cycle', length, f'exact={exact:.12f}', f'MC={estimate:.12f}', f'SE={se:.6f}', f'tail_bound={error:.2e}')
    print('SPHERICAL_GRAPH_EULERIAN_PARITY_CHECKS_OK')


if __name__ == '__main__':
    main()

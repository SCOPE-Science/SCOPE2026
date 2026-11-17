"""Finite exact checks of sharp anchored graph-variation superposition norms.

Run with Python 3; no third-party packages, downloads, or external data.
The proof of the unrestricted theorem is in RESULT.md, not this checker.
"""
from fractions import Fraction
from itertools import combinations, product
from math import tanh


def norm(h, edges):
    return abs(h[0]) + sum(abs(h[u] - h[v]) for u, v in edges)


def connected(n, edges):
    seen = {0}
    while True:
        new = seen | {v for u, v in edges if u in seen} | {u for u, v in edges if v in seen}
        if new == seen:
            return len(seen) == n
        seen = new


def cut_count(edges, mask):
    return sum(((mask >> u) & 1) != ((mask >> v) & 1) for u, v in edges)


def max_cut(n, edges):
    return max(cut_count(edges, mask) for mask in range(1 << n))


def diagonal_multiplier_norm_exhaustive(n, edges, a, b):
    value = Fraction(0)
    for slopes in product((a, b), repeat=n):
        for h in product((-1, 0, 1), repeat=n):
            denominator = norm(h, edges)
            if not denominator:
                continue
            numerator = norm(tuple(slopes[v] * h[v] for v in range(n)), edges)
            value = max(value, Fraction(numerator, denominator))
    return value


def all_small_graphs():
    tested = 0
    slope_pairs = [(Fraction(0), Fraction(1)),
                   (Fraction(-1), Fraction(1)),
                   (Fraction(1), Fraction(2)),
                   (Fraction(-2), Fraction(-1))]
    for n in range(2, 5):
        possible_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(possible_edges)):
            edges = [e for i, e in enumerate(possible_edges) if (mask >> i) & 1]
            if not connected(n, edges):
                continue
            mc = max_cut(n, edges)
            for a, b in slope_pairs:
                obtained = diagonal_multiplier_norm_exhaustive(n, edges, a, b)
                predicted = max(abs(a), abs(b)) + (b-a)*mc
                assert obtained == predicted, (n, edges, a, b, obtained, predicted)
                tested += 1
    print('ALL_CONNECTED_LABELLED_GRAPHS_N2_TO_N4_EXACT_DIAGONAL_PASS', tested)


def families():
    count = 0
    for n in range(2, 13):
        path = [(i, i+1) for i in range(n-1)]
        complete = list(combinations(range(n), 2))
        cycle = path + ([(n-1, 0)] if n >= 3 else [])
        assert max_cut(n, path) == n-1
        assert max_cut(n, complete) == (n*n)//4
        assert max_cut(n, cycle) == (n-(n & 1) if n >= 3 else 1)
        for edges in (path, complete, cycle):
            mc = max_cut(n, edges)
            for a, b in ((0, 1), (-1, 1), (1, 2)):
                m = max(abs(a), abs(b))
                witness = max(abs(b if mask & 1 else a)+(b-a)*cut_count(edges,mask)
                              for mask in range(1 << n))
                assert witness == m+(b-a)*mc
                count += 1
    print('PATH_CYCLE_COMPLETE_EXACT_CUT_WITNESSES_PASS', count)


def smooth_limit():
    n = 5
    edges = [(i, (i+1) % n) for i in range(n)]
    mc = max_cut(n, edges)
    cut = max(range(1 << n), key=lambda mask: cut_count(edges, mask))
    if not (cut & 1):
        cut ^= (1 << n)-1
    x = [0.0 if (cut >> v) & 1 else 15.0 for v in range(n)]
    eps = 1e-5
    h = [(tanh(v+eps)-tanh(v))/eps for v in x]
    ratio = norm(h, edges)
    assert ratio > 1+mc-1e-4, (ratio, mc)
    print('SMOOTH_TANH_APPROXIMATE_SLOPE_EXTREMA_PASS')


if __name__ == '__main__':
    all_small_graphs()
    families()
    smooth_limit()
    print('ALL_ANCHORED_GRAPH_VARIATION_CHECKS_PASS')

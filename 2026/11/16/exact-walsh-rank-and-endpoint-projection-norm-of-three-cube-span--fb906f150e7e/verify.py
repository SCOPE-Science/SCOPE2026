"""Reproduce the exact Fourier and endpoint-projection census for the 3-cube.

Requires Python 3.10+ standard library. `python verify.py` checks the two
accompanying certificates; `python verify.py --emit` regenerates them.
All arithmetic is integral except final exact Fraction simplification.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
import csv
import io
import sys

EDGE_LIST = tuple((v, v ^ (1 << k)) for v in range(8) for k in range(3)
                  if v < (v ^ (1 << k)))
assert len(EDGE_LIST) == 12
DIM = 12
N = 1 << DIM


def spanning_tree(mask):
    """Seven selected cube edges make a tree iff all eight nodes are joined."""
    parent = list(range(8))
    def root(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for edge_index, (u, v) in enumerate(EDGE_LIST):
        if (mask >> edge_index) & 1:
            ru, rv = root(u), root(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return len({root(i) for i in range(8)}) == 1


def fwht_inplace(values):
    """Unnormalized 12-bit binary Walsh-Hadamard transform."""
    for offset in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048):
        for start in range(0, N, 2 * offset):
            for i in range(start, start + offset):
                a, b = values[i], values[i + offset]
                values[i], values[i + offset] = a + b, a - b
    return values


def determinant_bareiss(matrix):
    """Exact integer determinant by fraction-free elimination."""
    a = [row[:] for row in matrix]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n-1):
        pivot = next((r for r in range(k, n) if a[r][k] != 0), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        d = a[k][k]
        for r in range(k + 1, n):
            for c in range(k + 1, n):
                numerator = a[r][c] * d - a[r][k] * a[k][c]
                assert numerator % prev == 0
                a[r][c] = numerator // prev
        for r in range(k+1, n):
            a[r][k] = 0
        prev = d
    return sign * a[-1][-1]


def matrix_tree(mask):
    """Signed weighted Matrix-Tree determinant for a 7-by-7 minor."""
    lap = [[0] * 7 for _ in range(7)]
    for edge_index, (u, v) in enumerate(EDGE_LIST):
        weight = -1 if ((mask >> edge_index) & 1) else 1
        if u < 7:
            lap[u][u] += weight
        if v < 7:
            lap[v][v] += weight
        if u < 7 and v < 7:
            lap[u][v] -= weight
            lap[v][u] -= weight
    return determinant_bareiss(lap)


def permute_mask(mask, edge_map):
    return sum(((mask >> i) & 1) << edge_map[i] for i in range(12))


def automorphisms():
    indices = {e: i for i, e in enumerate(EDGE_LIST)}
    maps = []
    for p in permutations(range(3)):
        for shift in range(8):
            def image(v):
                return shift ^ sum(((v >> i) & 1) << p[i] for i in range(3))
            maps.append(tuple(indices[tuple(sorted((image(u), image(v))))]
                              for u, v in EDGE_LIST))
    assert len(maps) == len(set(maps)) == 48
    return maps


def generate():
    f = [0] * N
    for positions in combinations(range(12), 7):
        mask = sum(1 << i for i in positions)
        if spanning_tree(mask):
            f[mask] = 1
    assert sum(f) == 384
    w = fwht_inplace(f.copy())
    assert all(matrix_tree(mask) == w[mask] for mask in range(N))
    assert sum(x*x for x in w) == N * 384
    histogram = dict(sorted(Counter(w).items()))
    assert histogram == {
        -384:1,-72:24,-64:18,-56:24,-40:24,-32:228,-24:8,
        -16:144,-8:816,0:1522,8:816,16:144,24:8,
        32:228,40:24,56:24,64:18,72:24,384:1}
    support = [int(x != 0) for x in w]
    h = fwht_inplace(support.copy())
    assert sum(support) == 2574
    assert fwht_inplace(h.copy()) == [N * x for x in support]
    assert sum(x*x for x in h) == N * sum(support)
    assert sum(abs(x) for x in h) == 56972
    assert Fraction(sum(abs(x) for x in h), N) == Fraction(14243, 1024)
    assert set(abs(x) for x in w if x) == {8,16,24,32,40,56,64,72,384}
    assert all(x % 8 == 0 for x in w)
    maps = automorphisms()
    visited = set()
    orbits = []
    for mask in range(N):
        if mask in visited:
            continue
        orbit = {permute_mask(mask, emap) for emap in maps}
        assert not orbit & visited
        assert all(w[p] == w[mask] for p in orbit)
        visited |= orbit
        orbits.append((mask, len(orbit), w[mask]))
    assert len(visited) == N and len(orbits) == 144
    assert sum(count for _, count, signed in orbits if signed == 0) == 1522
    nonzero_frequencies = [s for s in range(N) if support[s]]
    for rep, count, wvalue in orbits:
        direct_h = sum(1 - 2 * ((rep & s).bit_count() % 2) for s in nonzero_frequencies)
        assert direct_h == h[rep]
        assert (h[rep] == h[permute_mask(rep, maps[7])])
    return w, h, orbits


def csv_bytes(headers, rows):
    stream = io.StringIO(newline='')
    writer = csv.writer(stream, lineterminator='\n')
    writer.writerow(headers)
    writer.writerows(rows)
    return stream.getvalue().encode('utf-8')


def main():
    w, h, orbits = generate()
    out = {
        'frequency_certificate.csv':csv_bytes(
            ('frequency_mask','walsh','projection_numerator'),
            ((i, w[i], h[i]) for i in range(N))),
        'automorphism_orbits.csv':csv_bytes(
            ('representative_mask','orbit_size','walsh'),orbits),
    }
    root = Path(__file__).resolve().parent
    if '--emit' in sys.argv:
        for name, content in out.items():
            (root / name).write_bytes(content)
    else:
        for name, content in out.items():
            actual = (root / name).read_bytes()
            assert actual == content, f'Certificate mismatch: {name}'
    print('Q3_SPANNING_TREE_WALSH_EXACT_PASS trees=384 frequencies=4096 orbits=144 rank=2574 lambda=14243/1024')

if __name__ == '__main__':
    main()

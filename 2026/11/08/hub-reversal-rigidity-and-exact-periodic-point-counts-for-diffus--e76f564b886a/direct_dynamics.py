"""Direct exhaustive graph-edge updates for integer diffusion on a windmill of triangles.
Run: python direct_dynamics.py (requires NumPy)."""
from collections import Counter
import numpy as np


def graph_edges(r):
    # Vertex 0 is the hub, vertices 2j+1 and 2j+2 are the j-th triangle.
    return [(0, 2*j+1) for j in range(r)] + [(0, 2*j+2) for j in range(r)] + [(2*j+1, 2*j+2) for j in range(r)]


def update(x, edges):
    delta = np.zeros_like(x)
    for u, v in edges:
        e = np.sign(x[:, u] - x[:, v])
        delta[:, u] -= e
        delta[:, v] += e
    return x + delta


def count_exhaustive(r, max_magnitude, block=100000):
    n = 2*r
    base = 2*max_magnitude+1
    total = base**n
    edges = graph_edges(r)
    by_hub_displacement = Counter()
    for lo in range(0, total, block):
        idx = np.arange(lo, min(total, lo+block), dtype=np.int64)
        x = np.zeros((len(idx), n+1), dtype=np.int16)
        for i in range(n):
            x[:, i+1] = (idx % base).astype(np.int16)-max_magnitude
            idx //= base
        y = update(x, edges)
        z = update(y, edges)
        good = np.all(z == x, axis=1)
        values, counts = np.unique(y[good, 0], return_counts=True)
        by_hub_displacement.update({int(a):int(b) for a,b in zip(values,counts)})
    return dict(sorted(by_hub_displacement.items())), total


if __name__ == '__main__':
    for r, B in [(1, 5), (2, 7), (3, 6)]:
        counts, searched = count_exhaustive(r, B)
        expected = ( {-2:4,-1:4,0:3,1:4,2:4} if r == 1 else
                   {-2*r:(6*r-2)**r, 0:3**r, 2*r:(6*r-2)**r} )
        assert counts == expected, (r, counts, expected)
        print(f'r={r} coordinate_window=[{-B},{B}] states={searched} signed_hub_displacement={counts} PASS')
    print('DIRECT_EXHAUSTIVE_PASS')

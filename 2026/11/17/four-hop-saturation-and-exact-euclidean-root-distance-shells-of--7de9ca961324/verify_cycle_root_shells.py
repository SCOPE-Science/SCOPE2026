"""Exact rational tests for Euclidean projection certificates on cycle root polytopes.

Requires only the Python standard library. Run: python verify_cycle_root_shells.py
Finite tests corroborate, but do not replace, the proof for every n.
"""
from fractions import Fraction as F


def data(n, i, j):
    assert n >= 4 and 0 <= i < n and 0 <= j < n and i != j
    k = (j - i) % n
    d = min(k, n-k)
    s = 1 if k <= n // 2 else -1
    edges = []
    if d == 1:
        edges = [(i, j, F(1))]
    elif d == 2:
        edges = [(i, (i+s) % n, F(1, 2)),
                 ((i+s) % n, j, F(1, 2))]
    elif d == 3:
        edges = [(i, (i+s) % n, F(3, 11)),
                 ((i+s) % n, (i+2*s) % n, F(1, 11)),
                 ((i+2*s) % n, j, F(3, 11)),
                 (i, (i-s) % n, F(2, 11)),
                 ((j+s) % n, j, F(2, 11))]
    else:
        edges = [(i, (i+1) % n, F(1, 4)),
                 (i, (i-1) % n, F(1, 4)),
                 ((j+1) % n, j, F(1, 4)),
                 ((j-1) % n, j, F(1, 4))]
    assert all((u-v) % n in (1, n-1) for u,v,_ in edges)
    assert sum((w for _,_,w in edges), F(0)) == 1
    y = [F(0)] * n
    for u,v,w in edges:
        y[u] += w
        y[v] -= w
    x = [F(0)] * n
    x[i] = F(1)
    x[j] = F(-1)
    residual = [a-b for a,b in zip(x,y)]
    squared = sum((v*v for v in residual), F(0))
    expected = [F(0), F(0), F(1,2), F(8,11)][d] if d <= 3 else F(3,4)
    assert squared == expected, (n,i,j,squared,expected)
    support = max(abs(residual[k] - residual[(k+1)%n]) for k in range(n))
    assert support == sum((residual[k]*y[k] for k in range(n)), F(0)), (n,i,j,support)
    # Euclidean projection iff <x-y,z-y> <= 0 for all signed edge roots z.
    if d >= 2:
        assert residual[i] > 0 and residual[j] < 0
        assert residual[i] == max(residual) and residual[j] == min(residual)
        assert residual.count(residual[i]) == 1 and residual.count(residual[j]) == 1
    return squared


def max_count(n):
    if n <= 5: return n*(n-3), F(1,2)
    if n <= 7: return n*(n-5), F(8,11)
    return n*(n-7), F(3,4)


def run():
    exhaustive = long_separations = orientations = 0
    for n in range(4, 31):
        values = []
        for i in range(n):
            for j in range(n):
                if i == j: continue
                values.append(data(n,i,j))
                exhaustive += 1
        expected_count, m = max_count(n)
        assert max(values) == m and values.count(m) == expected_count
    for n in range(31, 201):
        values = []
        for d in range(1, n//2+1):
            values.append(data(n,0,d)); long_separations += 1
            values.append(data(n,0,n-d)); orientations += 1
        assert max(values) == max_count(n)[1]
    print('CYCLE_ROOT_PROJECTION_PASS exhaustive_ordered_roots=%d long_separations=%d reverse_separations=%d n=4..200'
          % (exhaustive,long_separations,orientations))


if __name__ == '__main__':
    run()

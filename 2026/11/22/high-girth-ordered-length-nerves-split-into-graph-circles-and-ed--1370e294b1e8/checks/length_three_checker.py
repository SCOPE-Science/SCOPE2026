#!/usr/bin/env python3
"""Exact cellular boundary and finite-field checks for ordered length-filtered graph nerves.

This script is self-contained and uses only Python's standard library. It
corroborates finite cases; the infinite-family homotopy theorem has a proof
independent of numerical extrapolation.
"""
from collections import defaultdict, deque


def distances(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert u != v
        adj[u].add(v)
        adj[v].add(u)
    D = []
    for start in range(n):
        d = {start: 0}
        todo = deque([start])
        while todo:
            x = todo.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y] = d[x] + 1
                    todo.append(y)
        assert len(d) == n
        D.append(d)
    return D


def normalized_chains(n, edges, cutoff):
    dist = distances(n, edges)
    cells = [[(i,) for i in range(n)]]
    lengths = [[0] * n]
    for k in range(1, cutoff + 1):
        next_cells = []
        next_lengths = []
        for t, length in zip(cells[-1], lengths[-1]):
            for v in range(n):
                if v != t[-1] and length + dist[t[-1]][v] <= cutoff:
                    next_cells.append(t + (v,))
                    next_lengths.append(length + dist[t[-1]][v])
        cells.append(next_cells)
        lengths.append(next_lengths)
    matrices = []
    for k in range(1, cutoff + 1):
        lookup = {t: i for i, t in enumerate(cells[k - 1])}
        columns = []
        for t in cells[k]:
            col = defaultdict(int)
            for j in range(k + 1):
                face = t[:j] + t[j + 1:]
                if any(face[i] == face[i + 1] for i in range(len(face) - 1)):
                    continue  # degenerate face vanishes in normalized chains
                col[lookup[face]] += (-1) ** j
            columns.append({i: x for i, x in col.items() if x})
        matrices.append(columns)
    return cells, matrices


def sparse_rank(columns, prime):
    pivots = {}
    rank = 0
    for column in columns:
        x = {i: val % prime for i, val in column.items() if val % prime}
        while x:
            i = min(x)
            if i in pivots:
                scale = x[i]
                for j, val in pivots[i].items():
                    new = (x.get(j, 0) - scale * val) % prime
                    if new:
                        x[j] = new
                    elif j in x:
                        del x[j]
            else:
                inv = pow(x[i], -1, prime)
                pivots[i] = {j: (val * inv) % prime for j, val in x.items()}
                rank += 1
                break
    return rank


def check_boundaries(cells, matrices):
    for k in range(2, len(cells)):
        first = matrices[k - 1]
        second = matrices[k - 2]
        for col in first:
            result = defaultdict(int)
            for mid, weight in col.items():
                for row, coefficient in second[mid].items():
                    result[row] += weight * coefficient
            assert all(v == 0 for v in result.values()), 'Nonzero boundary square'


def check_top_edge_cycles(cells, matrices, edges, cutoff):
    index = {cell: i for i, cell in enumerate(cells[cutoff])}
    boundary = matrices[cutoff - 1]
    for u, v in edges:
        forward = tuple(u if j % 2 == 0 else v for j in range(cutoff + 1))
        reverse = tuple(v if j % 2 == 0 else u for j in range(cutoff + 1))
        total = defaultdict(int)
        for path, sign in ((forward, 1), (reverse, (-1) ** (cutoff + 1))):
            for row, val in boundary[index[path]].items():
                total[row] += sign * val
        assert all(c == 0 for c in total.values()), 'Broken alternating edge cycle'


def test(name, n, edges, cutoff, expected):
    cells, matrices = normalized_chains(n, edges, cutoff)
    check_boundaries(cells, matrices)
    check_top_edge_cycles(cells, matrices, edges, cutoff)
    dimensions = [len(v) for v in cells]
    for prime in (2, 1000003):
        ranks = [sparse_rank(mat, prime) for mat in matrices]
        betti = [dimensions[k] - (ranks[k - 1] if k else 0)
                 - (ranks[k] if k < len(ranks) else 0)
                 for k in range(cutoff + 1)]
        assert betti == expected, (name, prime, betti, expected)
    print(f'{name}: cutoff={cutoff}, vertices={n}, edges={len(edges)}, '
          f'cell_counts={dimensions}, Betti_0_to_{cutoff}={expected}, '
          'boundary_squared=0, alternating_cycles=closed, primes=2/1000003')


def main():
    for n in (7, 8, 9):
        test(f'C_{n}', n, [(i, (i + 1) % n) for i in range(n)],
             3, [1, 1, 0, n])
    edges = [(i, (i + 1) % 7) for i in range(7)]
    # Two heptagons sharing one vertex.
    second = [0, 7, 8, 9, 10, 11, 12, 0]
    edges += list(zip(second, second[1:]))
    test('two_heptagons_sharing_one_vertex', 13, edges, 3, [1, 2, 0, 14])
    test('path_on_five_vertices', 5, [(i, i + 1) for i in range(4)],
         3, [1, 0, 0, 4])
    for n, cutoff in ((9, 4), (11, 5)):
        test(f'C_{n}', n, [(i, (i + 1) % n) for i in range(n)],
             cutoff, [1, 1] + [0] * (cutoff - 2) + [n])
    for n, cutoff, middle in ((6, 3, 5), (8, 4, 7), (10, 5, 9)):
        wanted = [1, 0] + [0] * (cutoff - 1)
        wanted[2] = middle
        wanted[-1] = n
        test(f'C_{n}_excluded_boundary', n,
             [(i, (i + 1) % n) for i in range(n)], cutoff, wanted)
    print('ALL FINITE CHECKS PASSED')


if __name__ == '__main__':
    main()

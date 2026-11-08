#!/usr/bin/env python3
"""Exact finite-field Krylov checks of central three-vertex trapping on Sierpinski gaskets.

Uses only Python's standard library. For each generation, independently builds the
combinatorial graph Laplacian and computes its central-corner cyclic rank modulo
independent large primes. These finite checks support, but do not establish, the
all-generation theorem proved in RESULT.md.
"""


def gasket(level):
    edges = {tuple(sorted((a, b))) for a, b in (
        ((0, 0), (1, 0)), ((0, 0), (0, 1)), ((1, 0), (0, 1)))}
    for i in range(level):
        step = 1 << i
        edges = {
            tuple(sorted(((a[0] + dx, a[1] + dy),
                          (b[0] + dx, b[1] + dy))))
            for a, b in edges
            for dx, dy in ((0, 0), (step, 0), (0, step))
        }
    points = sorted({x for edge in edges for x in edge})
    index = {p: i for i, p in enumerate(points)}
    adj = [[] for _ in points]
    for a, b in edges:
        x, y = index[a], index[b]
        adj[x].append(y)
        adj[y].append(x)
    for row in adj:
        row.sort()
    return points, adj


def laplacian_step(vector, adj, prime):
    return [(len(row) * vector[i] - sum(vector[j] for j in row)) % prime
            for i, row in enumerate(adj)]


def krylov_rank(adj, marked, prime):
    n = len(adj)
    vectors = [[int(i == mark) for i in range(n)] for mark in marked]
    pivots = {}
    rounds = 0
    for level in range(n + 1):
        previous = len(pivots)
        for src in vectors:
            v = src[:]
            for pivot in sorted(pivots):
                factor = v[pivot]
                if factor:
                    basis = pivots[pivot]
                    for j in range(pivot, n):
                        v[j] = (v[j] - factor * basis[j]) % prime
            pivot = next((j for j, x in enumerate(v) if x), None)
            if pivot is not None:
                inv = pow(v[pivot], prime - 2, prime)
                pivots[pivot] = [x * inv % prime for x in v]
        rounds = level + 1
        if len(pivots) == previous:
            break
        vectors = [laplacian_step(v, adj, prime) for v in vectors]
    else:
        raise AssertionError('Krylov closure did not stabilize')
    return len(pivots), rounds


def main():
    checked = 0
    for g in range(1, 6):
        vertices, adj = gasket(g)
        center = 1 << (g - 1)
        coordinates = ((center, 0), (0, center), (center, center))
        index = {v: j for j, v in enumerate(vertices)}
        marks = [index[coord] for coord in coordinates]
        expected_n = (3 ** (g + 1) + 3) // 2
        expected_b = 6 if g == 1 else 13 * 2 ** (g - 2) + 1
        assert len(vertices) == expected_n
        assert len(set(marks)) == 3
        assert sum(map(len, adj)) == 3 ** (g + 1) * 2
        for prime in (1000000007, 1000000009):
            rank, rounds = krylov_rank(adj, marks, prime)
            assert rank == expected_b, (g, prime, rank, expected_b)
            assert rounds <= len(vertices)
            checked += 1
        print('g=%d N=%d central_bright=%d central_dark=%d' %
              (g, expected_n, expected_b, expected_n - expected_b))
    print('VERIFY_OK prime_rank_checks=%d' % checked)


if __name__ == '__main__':
    main()

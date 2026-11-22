#!/usr/bin/env python3
"""Reproducible numerical checks for a two-community spectral theorem.

Uses the standard Python library only. Finite checks supplement, but do not
replace, the uniform analytic proof in RESULT.md.
"""
from math import sqrt


def cartesian_cycles(a, b):
    assert a >= 3 and b >= 3
    n = a * b
    adj = [set() for _ in range(n)]
    for i in range(a):
        for j in range(b):
            u = i * b + j
            for v in (((i + 1) % a) * b + j, i * b + (j + 1) % b):
                adj[u].add(v)
                adj[v].add(u)
    return adj


def cycle(n):
    assert n >= 3
    return [set(((i - 1) % n, (i + 1) % n)) for i in range(n)]


def fan(adjacency, v=0):
    n = len(adjacency)
    result = [set(neighbors) for neighbors in adjacency] + [set(n + j for j in neighbors) for neighbors in adjacency]
    for j in range(n):
        result[v].add(n + j)
        result[n + j].add(v)
    return result


def perron(graph, tolerance=1e-12, max_iterations=30000):
    # Positive averaging of iterates avoids bipartite sign oscillations.
    x = [1.0] * len(graph)
    norm = sqrt(sum(z * z for z in x))
    x = [z / norm for z in x]
    for iteration in range(max_iterations):
        y = [sum(x[j] for j in row) for row in graph]
        rayleigh = sum(a * b for a, b in zip(x, y))
        residual = sqrt(sum((a - rayleigh * b) ** 2 for a, b in zip(y, x)))
        if residual < tolerance:
            return rayleigh, iteration, residual
        # Lazy power iteration, ensuring aperiodicity, with same eigenvector.
        norm = sqrt(sum((a + b) ** 2 for a, b in zip(x, y)))
        x = [(a + b) / norm for a, b in zip(x, y)]
    raise AssertionError('positive power iteration did not converge')


def closed_walk_three(graph, v=0):
    return sum(1 for i in graph[v] for j in graph[i] if v in graph[j])


def root_by_resolvent(graph, v=0):
    n = len(graph)
    d = len(graph[0])
    assert all(len(row) == d for row in graph)

    def f(lam):
        # At every term k, scaled = A^k e_v / lambda^k.
        scaled = [float(i == v) for i in range(n)]
        res = 1. / lam
        for k in range(1, 1500):
            scaled = [sum(scaled[j] for j in row) / lam for row in graph]
            res += scaled[v] / lam
            # Remaining tail <= (d/lambda)^(k+1) /
            # (lambda * (1-d/lambda)) for undirected d-regular graphs.
            if (d / lam) ** (k + 1) / (lam * (1 - d / lam)) < 2e-16:
                break
        else:
            raise AssertionError('resolvent tail did not converge')
        return lam - d - n * res

    low = max(d + 1e-8, sqrt(n))
    high = sqrt(n) + d + 1
    assert f(low) < 0 and f(high) > 0
    for _ in range(70):
        mid = (low + high) / 2
        if f(mid) < 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def expansion(n, d, t):
    return sqrt(n) + d / 2 + (d / 2 + d * d / 8) / sqrt(n) + (t - d * d) / (2 * n)


def check(label, graph):
    n = len(graph)
    d = len(graph[0])
    assert len(graph) == n and all(len(row) == d for row in graph)
    assert all(i in graph[j] for j, row in enumerate(graph) for i in row)
    assert d >= 2
    full = fan(graph)
    assert len(full) == 2 * n
    assert sum(len(row) for row in full) == n * (d + 1) * 2
    eigen, count, resid = perron(full)
    exact, tris = root_by_resolvent(graph), closed_walk_three(graph)
    assert abs(exact - eigen) < 5e-10, (label, exact, eigen)
    expected = expansion(n, d, tris)
    err_scaled = abs(exact - expected) * n ** 1.5
    assert err_scaled < 300 * (d + 1) ** 4, (label, err_scaled)
    # Matching case is exactly (d+1)-regular and positive Perron vector = 1.
    matching_degree = d + 1
    assert matching_degree < exact if n >= (d + 1) ** 2 + 1 else True
    print('%s n=%d d=%d triangles_at_v=%d hub_lambda=%.12f '
          'matching_lambda=%d expansion=%.12f error_times_n^1.5=%.5f '
          'power_iterations=%d residual=%.2g' %
          (label, n, d, tris // 2, exact, matching_degree, expected,
           err_scaled, count, resid))


def main():
    for n in (12, 30, 100, 300):
        check('cycle_%d' % n, cycle(n))
    check('4regular_triangle_free_120', cartesian_cycles(30, 4))
    check('4regular_triangle_at_v_120', cartesian_cycles(40, 3))
    for a, b in ((10, 5), (25, 4), (40, 5)):
        check('cartesian_%d_%d' % (a, b), cartesian_cycles(a, b))
    print('ALL TESTS PASSED: 9 spectral/resolvent comparisons; no infinite assertion inferred')


if __name__ == '__main__':
    main()

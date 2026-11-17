#!/usr/bin/env python3
"""Reproducible finite graph tests for the Fibonacci cover fluctuation theorem.

Uses the standard library only. Finite graph tests corroborate, but do not
replace, the all-order Fibonacci Rauzy-graph theorem cited in RESULT.md.
"""
import math


def fibonacci(kmax):
    f = [0, 1]
    while len(f) <= kmax:
        f.append(f[-1] + f[-2])
    return f


def fibonacci_prefix(min_length):
    word = '0'
    while len(word) < min_length:
        word = ''.join('01' if ch == '0' else '0' for ch in word)
    return word


def graph_for_cover(word, n):
    factors = {word[i:i + n] for i in range(len(word) - n + 1)}
    assert len(factors) == n + 1, (n, len(factors))
    edges = {}
    for factor in factors:
        edges.setdefault(factor[:-1], []).append((factor[1:], int(factor[-1])))
    assert len(edges) == n
    assert sorted(map(len, edges.values())) == [1] * (n - 1) + [2]
    return edges


def first_returns(graph):
    fork = next(v for v in graph if len(graph[v]) == 2)
    result = []
    for nxt, digit in graph[fork]:
        length, ones, curr = 1, digit, nxt
        seen = {fork}
        while curr != fork:
            assert curr not in seen, 'unexpected directed cycle away from fork'
            seen.add(curr)
            outgoing = graph[curr]
            assert len(outgoing) == 1, 'second branching vertex'
            curr, digit = outgoing[0]
            length += 1
            ones += digit
        result.append((length, ones))
    return sorted(result)


def pressure(p, a, q, b, t):
    # Monotone-root bisection, no external eigensolver and no perturbative formula.
    def f(z):
        return math.exp(a * t - p * z) + math.exp(b * t - q * z) - 1.0
    lo = min(a / p, b / q) * t - 2.0
    hi = max(a / p, b / q) * t + 2.0
    assert f(lo) > 0 > f(hi)
    for _ in range(85):
        mid = (lo + hi) / 2.0
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def variance(p, a, q, b):
    h = pressure(p, a, q, b, 0.0)
    u, v = math.exp(-p * h), math.exp(-q * h)
    assert abs((u + v) - 1) < 2e-13
    mean_length = p * u + q * v
    mean = (a * u + b * v) / mean_length
    # Independent renewal-reward expression; exact equality with pressure derivative.
    renewal = (u * (a - mean * p) ** 2 + v * (b - mean * q) ** 2) / mean_length
    closed = u * v * (a * q - b * p) ** 2 / mean_length ** 3
    assert abs(renewal - closed) <= 1e-12 * max(1.0, closed)
    return closed


def run():
    F = fibonacci(15)
    w = fibonacci_prefix(60000)
    for k in range(5, 13):
        q, p = F[k], F[k - 1]
        graph = graph_for_cover(w, q)
        loops = first_returns(graph)
        expected = sorted([(F[k - 1], F[k - 3]), (F[k], F[k - 2])])
        assert loops == expected, (k, q, loops, expected)
        a, b = F[k - 3], F[k - 2]
        assert abs(a * q - b * p) == 1
        sigma = variance(p, a, q, b)
        assert sigma > 0
        print(f'k={k:2d} n={q:3d} loops={loops} scaled_variance={q**3*sigma:.12f}')
    for k in (5, 6, 7):
        p, q = F[k - 1], F[k]
        a, b = F[k - 3], F[k - 2]
        eps = 0.025
        numerical = (pressure(p, a, q, b, eps) - 2 * pressure(p, a, q, b, 0)
                     + pressure(p, a, q, b, -eps)) / eps ** 2
        exact = variance(p, a, q, b)
        assert abs(numerical / exact - 1) < 0.005, (k, numerical, exact)
        print(f'finite_difference k={k} empirical={numerical:.12g} analytic={exact:.12g}')
    phi = (1 + math.sqrt(5)) / 2
    r = 1 / phi
    c = pressure(1, 0, 1, 0, 0)  # overwritten by explicit scalar bisection
    lo, hi = 0., 2.
    for _ in range(90):
        mid = (lo + hi) / 2
        if math.exp(-r * mid) + math.exp(-mid) > 1:
            lo = mid
        else:
            hi = mid
    c = (lo + hi) / 2
    U, V = math.exp(-r * c), math.exp(-c)
    C = U * V / (r * U + V) ** 3
    assert 0.51749 < C < 0.51750
    print(f'limit_C={C:.15f}, full_scaled_interval=[{C:.15f}, {phi**3*C:.15f}]')
    print('PASS: finite Rauzy loop labels, Cassini, renewal moments, and pressure tests')


if __name__ == '__main__':
    run()

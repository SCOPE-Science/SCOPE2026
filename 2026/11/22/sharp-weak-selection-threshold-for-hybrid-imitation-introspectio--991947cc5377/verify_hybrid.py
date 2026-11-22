"""Checks for the finite heterogeneous hybrid learning theorem.

Run: python3 verify_hybrid.py
Only Python standard-library modules are required.
The symbolic proof of the all-size theorem is supplied separately in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import exp


def solve(A, b):
    """Dense linear solver, supporting both rational and floating input."""
    n = len(b)
    a = [list(A[i]) + [b[i]] for i in range(n)]
    for j in range(n):
        k = max(range(j, n), key=lambda i: abs(a[i][j]))
        assert a[k][j] != 0
        a[j], a[k] = a[k], a[j]
        pivot = a[j][j]
        for t in range(j, n + 1):
            a[j][t] /= pivot
        for i in range(n):
            if i == j:
                continue
            factor = a[i][j]
            if factor:
                for t in range(j, n + 1):
                    a[i][t] -= factor * a[j][t]
    return [a[i][n] for i in range(n)]


def get_states(n):
    states = list(product((0, 1), repeat=n))
    return states, {x: i for i, x in enumerate(states)}


def payoff(x, contributions, multiplier):
    n = len(x)
    shared = multiplier * sum(a * v for a, v in zip(contributions, x)) / n
    return [shared - a * v for a, v in zip(contributions, x)]


def stationary_cooperation(n, e, contributions, mu, r, beta):
    """Independent construction of the full 2^n-state transition matrix."""
    states, idx = get_states(n)
    m = len(states)
    P = [[0.0] * m for _ in range(m)]
    for si, x in enumerate(states):
        current = payoff(x, contributions, r)
        for i in range(n):
            y = list(x)
            y[i] ^= 1
            if i < e:
                imitation_sum = sum(
                    1 / (1 + exp(beta * (current[i] - current[j])))
                    for j in range(n) if j != i and x[j] != x[i]
                )
                flip_rate = mu / n + (1 - 2 * mu) * imitation_sum / (n * (n - 1))
            else:
                counter = payoff(y, contributions, r)
                flip_rate = mu / n + (1 - 2 * mu) / (
                    n * (1 + exp(beta * (current[i] - counter[i])))
                )
            P[si][idx[tuple(y)]] = flip_rate
        P[si][si] = 1.0 - sum(P[si])
    A = [[P[j][i] - (1.0 if i == j else 0.0) for j in range(m)]
         for i in range(m)]
    A[-1] = [1.0] * m
    pi = solve(A, [0.0] * (m - 1) + [1.0])
    assert min(pi) > -1e-8
    return sum(pi[i] * sum(x) / n for i, x in enumerate(states))


def predicted_coefficient(n, e, contributions, mu, r):
    h = n - e
    t = 1 - 2 * mu
    k = t / (2 * n * (n - 1))
    d = 2 * mu / n
    c = k / (h * k + d + F(1, n))
    b = k * (1 + h * c) / ((h + 1) * k + d) if e > 1 else 0
    ae = sum(contributions[:e])
    ah = sum(contributions[e:])
    q = (1 - c) * (h * ae + e * ah) + 2 * (e - 1) * (1 - b) * ae
    rstar = n * (1 + k * q / (2 * t * (n * k + d) * ah))
    coefficient = t * (n * k + d) * ah * (r - rstar) / (4 * n * n * (h * k + d))
    return coefficient, rstar


def exact_stationary_derivative(r):
    """Exact 8-state first-order perturbation, without moment closure."""
    n, e, mu = 3, 2, F(1, 10)
    contributions = [F(1)] * n
    states, idx = get_states(n)
    m = len(states)
    P0 = [[F(0) for _ in range(m)] for _ in range(m)]
    P1 = [[F(0) for _ in range(m)] for _ in range(m)]
    for si, x in enumerate(states):
        current = payoff(x, contributions, r)
        for i in range(n):
            y = list(x)
            y[i] ^= 1
            if i < e:
                opposite = [j for j in range(n) if j != i and x[j] != x[i]]
                rate0 = mu / n + (1 - 2 * mu) * len(opposite) / (2 * n * (n - 1))
                rate1 = -(1 - 2 * mu) * sum(
                    (current[i] - current[j] for j in opposite), F(0)
                ) / (4 * n * (n - 1))
            else:
                counter = payoff(y, contributions, r)
                rate0 = F(1, 2 * n)
                rate1 = -(1 - 2 * mu) * (current[i] - counter[i]) / (4 * n)
            P0[si][idx[tuple(y)]] = rate0
            P1[si][idx[tuple(y)]] = rate1
        P0[si][si] = F(1) - sum(P0[si])
        P1[si][si] = -sum(P1[si])
    A = [[P0[j][i] - (i == j) for j in range(m)] for i in range(m)]
    A[-1] = [F(1)] * m
    pi0 = solve(A, [F(0)] * (m - 1) + [F(1)])
    rhs = [-sum(P1[j][i] * pi0[j] for j in range(m)) for i in range(m)]
    rhs[-1] = F(0)
    pi1 = solve(A, rhs)
    return sum((pi1[i] * sum(x) / n for i, x in enumerate(states)), F(0))


def run_checks():
    exact_cases = [F(0), F(1), F(323, 56), F(7)]
    for r in exact_cases:
        got = exact_stationary_derivative(r)
        assert got == (56 * r - 323) / 1260, (r, got)
    comparisons = 0
    for n in range(2, 6):
        for e in range(1, n):
            a = [0.6 + 0.33 * i for i in range(n)]
            for mu in (0.0, 0.07, 0.22):
                for r in (0.5 * n, 1.3 * n, 2.7 * n):
                    eps = 0.0001
                    obtained = (stationary_cooperation(n, e, a, mu, r, eps)
                                - stationary_cooperation(n, e, a, mu, r, -eps)) / (2 * eps)
                    predicted, _ = predicted_coefficient(n, e, a, mu, r)
                    assert abs(obtained - predicted) < 1e-7, (n, e, mu, r, obtained, predicted)
                    comparisons += 1
    for n in range(2, 21):
        _, star = predicted_coefficient(n, n - 1, [F(1)] * n, F(0), F(0))
        assert star == F(n**3, 2 * n - 1)
    print('PASS: 4 exact eight-state rational perturbation cases')
    print('PASS:', comparisons, 'independent finite-state stationary derivative comparisons')
    print('PASS: 19 exact zero-mutation single-introspector threshold identities')
    print('Finite checks supplement rather than establish the all-size proof.')


if __name__ == '__main__':
    run_checks()

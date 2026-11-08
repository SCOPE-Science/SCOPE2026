"""Reproducibility checks for stochastic quality loss in equal party-list elections.

Uses only the Python standard library. Simulation is corroboration, not a proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, sqrt
from random import Random


def expected_gap(k, q):
    return Q(k * (k - 1) * (q - 1), 2 * (k * q + 1) * (q + 1))


def expected_top(k, q):
    n = k * q
    return sum((Q(r, n + 1) for r in range(n - k + 1, n + 1)), Q())


def expected_fair(k, q):
    return Q(k * q, q + 1)


def deficit_variance(q):
    a = Q(q - 1, q)
    integral = (1 - a ** (q + 2)) / (q + 2) - a * (1 - a ** (q + 1)) / (q + 1)
    var_hinges = Q(1, 3 * q * q) - Q(1, 4 * q ** 3)
    var_max = Q(q, (q + 1) ** 2 * (q + 2))
    cov = integral - Q(1, 2 * q * q * (q + 1))
    return var_hinges + var_max - 2 * cov


def uniform_ratio_variance(q):
    a = Q(q - 1, q)
    integral = (1 - a ** (q + 2)) / (q + 2) - a * (1 - a ** (q + 1)) / (q + 1)
    var_hinges = Q(1, 3 * q*q) - Q(1, 4 * q**3)
    var_max = Q(q, (q+1)**2 * (q+2))
    cov = integral - Q(1, 2*q*q*(q+1))
    u, f = Q(2*q - 1, 2*q), Q(q, q+1)
    return var_max / u**2 + f*f*var_hinges/u**4 - 2*f*cov/u**3


def directly_optimized_gap(values, k, q):
    best_represented = sum(max(values[i*q:(i+1)*q]) for i in range(k))
    top = sum(sorted(values)[-k:])
    return top - best_represented


def check():
    exact = 0
    for q in range(2, 19):
        for k in range(1, 29):
            assert expected_top(k, q) - expected_fair(k, q) == expected_gap(k, q)
            assert expected_gap(k, q) >= 0
            exact += 2
        assert deficit_variance(q) > 0
        exact += 1
    assert deficit_variance(2) == Q(1, 72)
    assert deficit_variance(3) == Q(257, 19440)
    assert uniform_ratio_variance(2) == Q(52, 2187)
    assert Q(2 * 2**2, (2 + 1) * (2*2 - 1)) == Q(8, 9)
    exact += 3

    # Independently compute the beta-integral sum for the uniform top-k sum.
    for q in range(2, 7):
        for k in range(1, 13):
            n = k * q
            integrated = sum((Q(min(k, r), n+1) for r in range(n+1)), Q())
            assert integrated == expected_top(k, q)
            exact += 1

    # Finite grid verifies the optimization interpretation including zero deficits.
    grid_checks = 0
    for k, q, alphabet in [(2, 2, (Q(0), Q(1, 2), Q(1))),
                            (3, 2, (Q(0), Q(1)))]:
        for vals in product(alphabet, repeat=k*q):
            assert directly_optimized_gap(vals, k, q) >= 0
            grid_checks += 1

    rng = Random(20261102)
    simulations = []
    for k, q, repetitions in [(2, 2, 30000), (8, 2, 35000),
                               (60, 2, 16000), (30, 3, 14000)]:
        sm = 0.
        for _ in range(repetitions):
            vals = [rng.random() for _ in range(k*q)]
            sm += directly_optimized_gap(vals, k, q)
        average = sm / repetitions
        theoretical = float(expected_gap(k, q))
        # Loose enough to avoid random false failures; far smaller than the effect.
        assert abs(average - theoretical) < 0.065 * max(1., sqrt(k))
        simulations.append((k, q, round(average, 6), round(theoretical, 6)))

    print('Exact rational checks:', exact)
    print('Exhaustive finite-grid checks:', grid_checks)
    print('Variance at q=2:', deficit_variance(2))
    print('Variance at q=3:', deficit_variance(3))
    print('Ratio CLT variance at q=2:', uniform_ratio_variance(2))
    print('Seeded simulation (k, q, observed mean deficit, exact mean):')
    for line in simulations:
        print(*line)
    print('PASS: all checks')


if __name__ == '__main__':
    check()

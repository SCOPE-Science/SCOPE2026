#!/usr/bin/env python3
"""Independent numerical diagnostics for marked Brownian resetting excursions.

The finite-state test enumerates a reflected lattice random walk with resetting,
without using the continuous-space hyperbolic first-exit formulas.  The
continuous limiting calculations are additionally checked by exact formulae.
"""
import math
from collections import defaultdict


def normalized(weights):
    total = sum(weights)
    assert total > 0
    return [x / total for x in weights]


def free_hitting(start, barrier, upper=9, q=0.25, outcome="zero"):
    """Directly accumulate first-exit probabilities before the next reset."""
    alive = {start: 1.0}
    result = 0.0
    for _ in range(800):
        next_alive = defaultdict(float)
        for x, weight in alive.items():
            for direction in (-1, 1):
                y = x + direction
                if y > upper:
                    y = upper - 1
                amount = weight * (1 - q) / 2
                if y == 0:
                    if outcome == "zero":
                        result += amount
                elif y == barrier and outcome == "barrier":
                    result += amount
                else:
                    next_alive[y] += amount
        alive = next_alive
        if sum(alive.values()) < 1e-14:
            break
    return result


def enumerate_full_process(barrier, upper=9, q=0.25):
    points = (2, 4)
    weights = (0.4, 0.6)
    none = -1
    states = {(2, 2, none): 0.4, (4, 4, none): 0.6}
    joint = defaultdict(float)
    no_barrier_absorption = 0.0
    for step in range(12000):
        next_states = defaultdict(float)
        for (x, origin, first_mark), prob in states.items():
            for new_origin, w in zip(points, weights):
                next_states[(new_origin, new_origin, first_mark)] += prob * q * w
            for direction in (-1, 1):
                y = x + direction
                if y > upper:
                    y = upper - 1
                amount = prob * (1 - q) / 2
                if y == 0:
                    if first_mark != none:
                        joint[(first_mark, origin)] += amount
                    else:
                        no_barrier_absorption += amount
                else:
                    mark = origin if first_mark == none and y == barrier else first_mark
                    next_states[(y, origin, mark)] += amount
        states = next_states
        if sum(states.values()) < 4e-13:
            break
    else:
        raise AssertionError("enumeration failed to converge")
    assert abs(sum(joint.values()) + no_barrier_absorption - 1.0) < 2e-11
    return joint


def discrete_factorization_test(barrier):
    points = (2, 4)
    mu = (0.4, 0.6)
    upper = 9
    q = 0.25
    direct = enumerate_full_process(barrier, upper, q)
    mark_weight = [w * free_hitting(x, barrier, upper, q, "barrier")
                   for x, w in zip(points, mu)]
    capture_weight = [w * free_hitting(x, barrier, upper, q, "zero")
                      for x, w in zip(points, mu)]
    extreme_law = normalized(mark_weight)
    capture_law = normalized(capture_weight)
    return_to_zero = free_hitting(barrier, barrier, upper, q, "zero")
    observed_prob = sum(direct.values())
    for i, x in enumerate(points):
        for j, y in enumerate(points):
            expected = extreme_law[i] * (return_to_zero * (i == j)
                                         + (1 - return_to_zero) * capture_law[j])
            actual = direct[(x, y)] / observed_prob
            assert abs(actual - expected) < 5e-10, (barrier, x, y, actual, expected)
    marginal = [sum(direct[(x, y)] for y in points) / observed_prob for x in points]
    for i in range(2):
        assert abs(marginal[i] - extreme_law[i]) < 5e-10
    return return_to_zero, observed_prob


def brownian_atom_test():
    x = (1.0, 2.0)
    mu = (0.4, 0.6)
    k = 1.0
    m = 3.0
    b = normalized([p * math.sinh(k * z) for p, z in zip(mu, x)])
    a = normalized([p * math.exp(-k * z) for p, z in zip(mu, x)])
    t = math.exp(-k * m)
    joint = [[b[i] * (t * (i == j) + (1 - t) * a[j])
              for j in range(2)] for i in range(2)]
    assert abs(sum(map(sum, joint)) - 1.0) < 1e-14
    assert b[1] > a[1]
    # The diagonal-mixture structure implies this exact covariance identity.
    cov = sum(joint[i][j] * x[i] * x[j] for i in range(2) for j in range(2))
    cov -= sum(joint[i][j] * x[i] for i in range(2) for j in range(2)) * \
           sum(joint[i][j] * x[j] for i in range(2) for j in range(2))
    var_b = b[0] * b[1] * (x[1] - x[0]) ** 2
    assert abs(cov - t * var_b) < 3e-14
    assert abs(joint[0][0] - 0.11761957068539448) < 2e-14


def killed_lattice_continuum_test():
    k, m, x = 1.1, 3.0, 1.0
    analytic = math.sinh(k * x) / math.sinh(k * m)
    errors = []
    for n in (60, 120, 240, 480):
        h = m / n
        lam = math.acosh(1 + k * k * h * h / 2)
        approximate = math.sinh(lam * int(round(x / h))) / math.sinh(lam * n)
        errors.append(abs(approximate - analytic))
    assert all(errors[i + 1] < errors[i] / 3.7 for i in range(3)), errors


def beta_boundary_layer_test():
    # Density proportional to (x-a)^(alpha-1)*(b-x)^(beta-1).
    alpha, beta, lower, upper = 2, 3, 1.0, 2.0
    n = 20000
    distances = [(j + 0.5) / n for j in range(n)]
    density = [d ** (alpha - 1) * (1 - d) ** (beta - 1)
               for d in distances]
    errors = []
    for k in (12, 25, 55):
        near_lower = [v * math.exp(-k * d) for v, d in zip(density, distances)]
        near_upper = [v * (math.exp(-k * (1 - d)) - math.exp(-k * (lower + upper + d)))
                      for v, d in zip(density, distances)]
        # Second factor is proportional to sinh(k*(lower+d)) after scaling.
        lower_mean = k * sum(w * d for w, d in zip(near_lower, distances)) / sum(near_lower)
        upper_mean = k * sum(w * (1 - d) for w, d in zip(near_upper, distances)) / sum(near_upper)
        errors.append(abs(lower_mean - alpha) + abs(upper_mean - beta))
    assert errors[2] < errors[1] < errors[0], errors
    assert errors[2] < 0.35, errors


def main():
    brownian_atom_test()
    killed_lattice_continuum_test()
    for barrier in (5, 6):
        direct_return, exceed = discrete_factorization_test(barrier)
        print(f"Discrete threshold {barrier}: joint-mark factorization within tolerance; "
              f"post-threshold return probability {direct_return:.9f}; "
              f"exceedance probability {exceed:.9f}")
    beta_boundary_layer_test()
    print("PASS: numerical and finite-state consistency diagnostics; "
          "continuous-space proof is in RESULT.md")


if __name__ == '__main__':
    main()

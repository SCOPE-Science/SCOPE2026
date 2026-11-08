"""Independent finite checks for Euclidean inballs of b-parking-function polytopes.

Requires numpy and scipy. Finite checks support but do not establish the general theorem.
"""
from itertools import combinations
import math
import random
import numpy as np
from scipy.optimize import linprog


def capacities(b):
    partial = []
    s = 0
    for a in b:
        assert isinstance(a, int) and a > 0
        s += a
        partial.append(s)
    return [sum(partial[-k:]) for k in range(1, len(b) + 1)]


def formula(b):
    h = capacities(b)
    r_candidates = [(h[k - 1] - k) / (k + math.sqrt(k)) for k in range(1, len(b) + 1)]
    radius = min(r_candidates)
    return radius, [k for k in range(1, len(b) + 1)
                    if abs(r_candidates[k - 1] - radius) <= 1e-9 * max(1, radius)]


def independent_linear_program(b):
    n = len(b)
    h = capacities(b)
    a = []
    rhs = []
    # Euclidean distances to every lower coordinate hyperplane.
    for i in range(n):
        row = [0.] * (n + 1)
        row[i] = -1.
        row[-1] = 1.
        a.append(row)
        rhs.append(-1.)
    # Euclidean distances to every upper subset hyperplane.
    for k in range(1, n + 1):
        for subset in combinations(range(n), k):
            row = [0.] * (n + 1)
            for i in subset:
                row[i] = 1.
            row[-1] = math.sqrt(k)
            a.append(row)
            rhs.append(float(h[k - 1]))
    cost = np.array([0.] * n + [-1.])
    ans = linprog(cost, A_ub=a, b_ub=rhs, bounds=[(None, None)] * n + [(0., None)], method='highs')
    assert ans.success, ans.message
    return ans.x[-1]


def crossover(k):
    t = math.sqrt(k)
    t2 = math.sqrt(k + 1)
    u = lambda z: 1. / (z * (z + 1))
    v = lambda z: z / (z + 1)
    return (v(t2) - v(t)) / (u(t) - u(t2))


def test():
    rng = random.Random(20261103)
    tested = 0
    for n in range(2, 8):
        for _ in range(25):
            b = [rng.randint(1, 13) for _ in range(n)]
            predicted, _ = formula(b)
            optimized = independent_linear_program(b)
            assert abs(predicted - optimized) < 2e-7 * max(1., predicted), (b, predicted, optimized)
            tested += 1
    example = [1001] + [1] * 6 + [500]
    r, contact = formula(example)
    assert contact == [2], (r, contact)
    assert abs(independent_linear_program(example) - r) < 1e-6
    # Every rank k can be made the unique metric contact orbit, while the
    # b-parking polytope stays in one fixed combinatorial class (b1 > 1).
    phase_examples = 0
    for n in range(2, 15):
        thresholds = [crossover(k) for k in range(1, n)]
        assert all(x < y for x, y in zip(thresholds, thresholds[1:]))
        for k in range(1, n + 1):
            if k == 1:
                theta = thresholds[0] / 2
            elif k == n:
                theta = thresholds[-1] + 1
            else:
                theta = (thresholds[k - 2] + thresholds[k - 1]) / 2
            scale = 10**8
            b = [scale + 1] + [1] * (n - 2) + [max(1, round(scale * theta))]
            _, active = formula(b)
            assert active == [k], (n, k, active)
            phase_examples += 1
    print('GENERAL_PARKING_INBALL_CHECKS_PASSED', tested, phase_examples,
          'explicit_rank2_radius', format(r, '.12f'))


if __name__ == '__main__':
    test()

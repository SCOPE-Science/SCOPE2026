"""Independent finite diagnostics for the cube--crosspolytope support and angular law.

Finite tests are not substitutes for the analytic all-dimensional arguments.
"""
import itertools
import math
import random


def p_two(t):
    if not 1 < t < 2:
        raise ValueError("the two-dimensional mixed-vertex range is 1<t<2")
    return 4 * math.atan(t - 1) / math.pi


def direct_support(g, t):
    n = len(g)
    vertices = list(itertools.product((-1, 1), repeat=n))
    for j in range(n):
        for sign in (-1, 1):
            v = [0.0] * n
            v[j] = sign * t
            vertices.append(tuple(v))
    return max(sum(a * b for a, b in zip(g, v)) for v in vertices)


def formula_support(g, t):
    return max(sum(abs(x) for x in g), t * max(abs(x) for x in g))


def main():
    rng = random.Random(20261114)
    cases = 0
    for n in (2, 3, 4, 5):
        for t in (1.01, (n + 1) / 2, n - 0.01):
            for _ in range(250):
                g = [rng.gauss(0, 1) for j in range(n)]
                assert abs(direct_support(g, t) - formula_support(g, t)) < 1e-11
                cases += 1
    for t in (1.1, math.sqrt(2), 1.8):
        count = 0
        N = 160000
        for _ in range(N):
            x, y = abs(rng.gauss(0, 1)), abs(rng.gauss(0, 1))
            count += (t * max(x, y) > x + y)
        empirical = count / N
        analytic = p_two(t)
        assert abs(empirical - analytic) < 0.009, (t, empirical, analytic)
    assert abs(p_two(math.sqrt(2)) - 0.5) < 1e-14
    # 2n=4 apex vertices and 2**n=4 cube vertices: eight equal cone weights.
    assert abs((0.5**2 / 4 + 0.5**2 / 4) - 1/8) < 1e-14
    print(f'CUBE_CROSS_GAUSSIAN_ANGLE_DIAGNOSTICS_PASS support_cases={cases} two_dimensional_sweeps=480000')


if __name__ == '__main__':
    main()

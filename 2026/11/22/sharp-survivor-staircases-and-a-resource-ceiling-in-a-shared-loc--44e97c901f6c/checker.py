#!/usr/bin/env python3
"""Exact rational checks for the shared/local nutrient survivor-staircase theorem.

Requires Python 3 standard library only. These checks are finite supporting tests;
the all-parameter theorem rests on the analytical proof in RESULT.md.
"""
from fractions import Fraction as F
from random import Random


def state(q, theta, beta, gamma, alpha, R):
    n = len(q)
    assert F(0) < theta <= 1 and beta > 0 and gamma > 0 and R > 0
    present = [i for i, v in enumerate(q) if v < R]
    assert present
    assert all((theta == 1 or R < v / (1 - theta)) for i, v in enumerate(q) if i in present)
    T = []
    N = []
    for a, v in zip(alpha, q):
        if v < R:
            ti = (v - (1 - theta) * R) / theta
            ni = beta * (R - v) / (gamma * theta * a * (v - (1 - theta) * R))
            assert 0 < ti < R and ni > 0
        else:
            ti, ni = R, F(0)
        T.append(ti)
        N.append(ni)
    R0 = R + gamma * sum((a * v * ni for a, v, ni in zip(alpha, q, N)), F(0))
    return N, T, R0


def check_rhs(q, theta, beta, gamma, alpha, R, N, T, R0):
    dN = [ni * (a * ((1 - theta) * R + theta * ti) - a * v)
          for v, ni, ti, a in zip(q, N, T, alpha)]
    dR = R0 - R - gamma * R * sum(((1 - theta) * a * ni for a, ni in zip(alpha, N)), F(0)) - beta * sum((R - ti for ti in T), F(0))
    dT = [beta * (R - ti) - gamma * theta * a * ti * ni for a, ti, ni in zip(alpha, T, N)]
    assert dN == [0] * len(q) and dR == 0 and dT == [0] * len(q)
    # Scalar closure and its positive derivative.
    h = R + beta / theta * sum((v * (R - v) / (v - (1 - theta) * R) for v in q if v < R), F(0))
    hp = 1 + beta * sum((v * v / (v - (1 - theta) * R) ** 2 for v in q if v < R), F(0))
    assert h == R0 and hp > 1
    # Every active transfer block is strictly positive definite; absent blocks are semidefinite.
    for ni, ti in zip(N, T):
        determinant = 1 / ti ** 2 - (1 / R + 1 / ti) ** 2 / 4
        if ni > 0:
            assert determinant > 0
            assert determinant == ((1 - ti / R) * (3 + ti / R)) / (4 * ti ** 2)
        else:
            assert ti == R and determinant == 0


def cutoff(q, theta, beta, j):
    if theta != 1 and q[j] >= q[0] / (1 - theta):
        return None
    z = q[j]
    return z + beta / theta * sum((v * (z - v) / (v - (1 - theta) * z) for v in q[:j]), F(0))


def run():
    q = [F(1), F(6, 5), F(7, 5)]
    theta, beta, gamma = F(1, 2), F(1), F(1)
    alpha = [F(1)] * 3
    R = F(3, 2)
    N, T, R0 = state(q, theta, beta, gamma, alpha, R)
    assert N == [F(4), F(4, 3), F(4, 13)]
    assert T == [F(1, 2), F(9, 10), F(13, 10)]
    assert R0 == F(979, 130)
    assert cutoff(q, theta, beta, 1) == F(11, 5)
    assert cutoff(q, theta, beta, 2) == F(377, 75)
    assert cutoff(q, F(1, 4), beta, 1) == F(46, 5)
    assert cutoff(q, F(1, 4), beta, 2) is None
    check_rhs(q, theta, beta, gamma, alpha, R, N, T, R0)
    rg = Random(315381)
    tested = 0
    # Exact-rational multi-species equilibria; vary positive parameters and active-set sizes.
    for rep in range(800):
        n = rg.randrange(2, 8)
        values = sorted(rg.sample(range(12, 95), n))
        q = [F(v, 10) for v in values]
        theta = F(rg.randint(2, 9), 10)
        beta = F(rg.randint(1, 15), rg.randint(1, 9))
        gamma = F(rg.randint(1, 9), rg.randint(1, 7))
        alpha = [F(rg.randint(1, 13), rg.randint(1, 9)) for _ in range(n)]
        cap = q[0] / (1 - theta)
        candidates = [q[0]] + [x for x in q[1:] if x < cap]
        low = rg.choice(candidates)
        upper = min([x for x in q if x > low] + [cap])
        if low >= cap or upper <= low:
            continue
        R = low + (upper - low) * F(rg.randint(1, 9), 10)
        N, T, R0 = state(q, theta, beta, gamma, alpha, R)
        check_rhs(q, theta, beta, gamma, alpha, R, N, T, R0)
        # Supply thresholds increase with q and with beta; deceased beyond the nutrient ceiling.
        finite = [cutoff(q, theta, beta, j) for j in range(1, n)]
        finite = [v for v in finite if v is not None]
        assert all(finite[i] < finite[i + 1] for i in range(len(finite) - 1))
        tested += 1
    assert tested > 600
    print('PASS: exact three-species example, thresholds, transfer-block determinants,', tested, 'rational steady states')


if __name__ == '__main__':
    run()

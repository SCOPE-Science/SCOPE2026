"""Independent numerical reproduction checks for a power-mean copula theorem.

All inequalities over continuous parameter domains are proved analytically in
RESULT.md, not by these finite checks. Uses Python's standard library only.
"""
import math
import random


def P(a, b, u):
    if u == 0:
        return a ** (1 / b) if b > 0 else 0.0
    x, y = math.log(a), math.log1p(-a) + b * math.log(u)
    hi = max(x, y)
    return math.exp((hi + math.log(math.exp(x - hi) + math.exp(y - hi))) / b)


def k(a, b, u):
    if u == 0:
        return 1 - a ** (1 / b) if b > 0 else 1.0
    z = P(a, b, u)
    q = math.log(a) - math.log1p(-a) - b * math.log(u)
    t = 1.0 / (1.0 + math.exp(max(-700, min(700, q))))
    return 1.0 - z * (1 + t)


def envelope(a, b):
    assert 0 < a < 1 and b != 0
    M = 1 - a ** (1 / b) if b > 0 else 1.0
    if b >= 1 - 2 / a:
        L = 1 - a
    else:
        L = -1 - 2 * b / (1 - b) * (a * (1 - b) / 2) ** (1 / b)
    return M, L


def turn(a, b):
    if b >= 1 - 2 / a:
        return None
    return (-a * (b + 1) / (2 * (1 - a))) ** (1 / b)


def interval(a1, b1, a2, b2):
    M1, L1 = envelope(a1, b1)
    M2, L2 = envelope(a2, b2)
    return -1 / max(M1*M2, L1*L2), 1 / max(M1*L2, L1*M2)


def density(alpha, pars, u, v):
    a1, b1, a2, b2 = pars
    return 1 + alpha * k(a1, b1, u) * k(a2, b2, v)


def check():
    assert envelope(.5, 1) == (.5, .5)
    assert interval(.5, 1, .5, 1) == (-4.0, 4.0)
    p = (.5, -5, .5, 1)
    lo, hi = interval(*p)
    assert math.isclose(lo, -2) and math.isclose(hi, 2)
    ustar = turn(.5, -5)
    assert ustar is not None and 0 < ustar < 1
    assert k(.5, -5, ustar) < k(.5, -5, 1)
    assert k(.5, -5, ustar) < k(.5, -5, .5)
    assert turn(.5, 1) is None
    for alpha in [-2, -1.5, 0, 1.5, 2]:
        for i in range(101):
            for j in range(21):
                assert density(alpha, p, i/100, j/20) >= -1e-12
    assert density(2.01, p, 0.0, 1.0) < 0.0
    assert density(-2.01, p, 0.0, 0.0) < 0.0
    rng = random.Random(32024)
    for _ in range(180):
        a = rng.uniform(.05, .95)
        b = rng.choice([-1, 1]) * 10**rng.uniform(-1.0, 2.0)
        M, L = envelope(a, b)
        assert 0 < M <= 1 and 0 < L <= 1
        for j in range(101):
            assert -L-1e-9 <= k(a, b, j/100) <= M+1e-9
    print('PASS: exact benchmark, sharp-boundary witnesses, 180 deterministic envelope grids')
    print('Example alpha interval:', (lo, hi), 'conditional switch:', ustar)


if __name__ == '__main__':
    check()

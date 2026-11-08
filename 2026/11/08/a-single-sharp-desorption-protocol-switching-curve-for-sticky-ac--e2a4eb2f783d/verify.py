"""Reproduce numerical checks of exact sticky-boundary protocol comparison.

Python 3 standard library only; deterministic and dependency-free.
The analytical proof in RESULT.md, not these finite tests, establishes the theorem.
"""
from math import acosh, cosh, exp, log, sinh, sqrt, tanh
from random import Random


def transforms(alpha, r, distance_over_speed):
    theta = acosh(1 + r / alpha)
    w = sqrt(r * (r + 2 * alpha))
    return exp(-distance_over_speed * w), exp(-theta), theta, w


def means(alpha, r, u, p, dwell, direction):
    f_minus, c, theta, w = transforms(alpha, r, u)
    f = f_minus if direction == -1 else f_minus * c
    a_home = (1 - f) / (r * f)
    a_wall = (1 - c) / (r * f)
    g = (1 - p) / p
    return (1 + g) * (a_home + dwell), a_home + dwell + g * (a_wall + dwell)


def solve_theta(beta):
    assert 0 < beta < 1
    lo, hi = 0.0, 2.0
    while hi / sinh(hi) > beta:
        hi *= 2
    for _ in range(95):
        mid = (lo + hi) * 0.5
        if mid / sinh(mid) > beta:
            lo = mid
        else:
            hi = mid
    return (lo + hi) * 0.5


def simulate_hit_before_exp_reset(start, direction, alpha, r, u, rng):
    # Units with velocity = 1, so initial position = x_0/v = u.
    t = 0.0
    x = start
    for _ in range(200000):
        tumble = rng.expovariate(alpha)
        reset = rng.expovariate(r)
        hit = x if direction < 0 else float('inf')
        dt = min(tumble, reset, hit)
        x += direction * dt
        t += dt
        if dt == hit:
            return True
        if dt == reset:
            return False
        direction *= -1
    raise RuntimeError("event cap exceeded")


def check():
    tests = 0
    for alpha in (0.17, 0.6, 1., 2.4, 8.):
        for r in (0.03, 0.1, 0.8, 2., 10.):
            for u in (0.2, 0.7, 1.4):
                fm, c, theta, w = transforms(alpha, r, u)
                assert abs(cosH(theta) - (1 + r/alpha)) < 1e-12
                assert abs((r + alpha - w) / alpha - c) < 1e-11
                for direction in (-1, 1):
                    f = fm if direction == -1 else fm * c
                    p, dwell = 0.3, 0.35
                    H, W = means(alpha, r, u, p, dwell, direction)
                    gap = (1-p)/p/r * (1 - c/f)
                    assert abs((W-H)-gap) < 2e-9 * (1+abs(gap))
                    for p2, b2 in ((0.14, 3.0), (0.88, .01)):
                        H2, W2 = means(alpha, r, u, p2, b2, direction)
                        assert abs((W2-H2)/((1-p2)/p2)-(W-H)/((1-p)/p)) < 1e-7 * (1+abs(gap))
                        tests += 1
                    if direction == +1:
                        assert gap < 0
                    else:
                        assert (gap > 0) == (alpha*u < theta/sinh(theta))
                    tests += 4
    for beta in (0.05, 0.15, 0.25, 0.5, 0.8, 0.95, 0.999):
        theta = solve_theta(beta)
        assert abs(beta*sinh(theta) - theta) < 1e-11*(1+theta)
        alpha = 1.0
        u = beta
        rc = cosh(theta) - 1.0
        a,b = means(alpha, rc*0.7, u, .35, 2., -1)
        assert b-a > 0
        a,b = means(alpha, rc*1.4, u, .35, 2., -1)
        assert b-a < 0
        tests += 3
    # Independent event-driven Monte Carlo checks the backward hitting transforms.
    alpha, r, u = 1.0, 0.8, 0.7
    f, c, _, _ = transforms(alpha, r, u)
    rng = Random(20260202)
    n = 60000
    hit_home = sum(simulate_hit_before_exp_reset(u, -1, alpha, r, u, rng) for _ in range(n)) / n
    hit_wall = sum(simulate_hit_before_exp_reset(0.0, +1, alpha, r, u, rng) for _ in range(n)) / n
    assert abs(hit_home-f) < .012, (hit_home, f)
    assert abs(hit_wall-c) < .012, (hit_wall, c)
    tests += 2
    print(f'PASS: {tests} deterministic and simulation checks')
    print('F and C analytic versus event-driven empirical:', f, hit_home, c, hit_wall)
    for beta in (.25, .5, .8, .95):
        theta = solve_theta(beta)
        print('beta, theta, rc/alpha:', beta, theta, cosh(theta)-1)


def cosH(x):
    return cosh(x)


if __name__ == '__main__':
    check()

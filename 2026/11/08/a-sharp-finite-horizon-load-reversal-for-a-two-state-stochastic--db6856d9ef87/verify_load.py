"""Independent finite-horizon calculations for a two-state Markov load.

Requires only Python's standard library. Numerical checks complement, but do not
replace, the analytic proof in RESULT.md.
"""
import math
import random


def occupancy(w, beta, E):
    z = beta * (E - w)
    if z >= 0:
        y = math.exp(-z)
        return y / (1.0 + y)
    y = math.exp(z)
    return 1.0 / (1.0 + y)


def rates(w, beta, E, k):
    return k * math.exp(-beta * (E - w) / 2), k * math.exp(beta * (E - w) / 2)


def work(w, t, beta, E, p, k):
    up, down = rates(w, beta, E, k)
    lam = up + down
    return w * (p - up / lam) * (-math.expm1(-lam * t))


def work_from_transitions(w, t, beta, E, p, k):
    up, down = rates(w, beta, E, k)
    lam = up + down
    factor = -math.expm1(-lam * t) / lam
    return w * (p * down * factor - (1 - p) * up * factor)


def a_fun(y):
    if y > 700:
        return 1.0
    if y < 1.0e-4:
        return y / 2 - y * y / 12 + y ** 4 / 720
    return 1 - y / math.expm1(y)


def critical_voltage(beta, E, p):
    return float('inf') if p == 1.0 else E + math.log(p / (1 - p)) / beta


def log_derivative(w, t, beta, E, p, k):
    x = beta * (w - E)
    r = (1 - p) * math.exp(x)
    c = math.cosh(x / 2)
    return (1 / w - beta * r / (p - r) - beta / 2
            - (beta / 2) * math.tanh(x / 2) * a_fun(2 * k * t * c))


def optimizer(t, beta, E, p, k):
    cap = critical_voltage(beta, E, p)
    lo = 1e-12
    hi = cap * (1 - 1e-12) if math.isfinite(cap) else max(25 / beta, E + 25 / beta)
    assert log_derivative(lo, t, beta, E, p, k) > 0
    assert log_derivative(hi, t, beta, E, p, k) < 0
    for _ in range(92):
        mid = (lo + hi) / 2
        if log_derivative(mid, t, beta, E, p, k) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def check():
    checks = 0
    rng = random.Random(142008)
    samples = [(1.0, 1.0, 1.0, 1.0), (1.0, 2.0, 1.0, 1.0),
               (1.0, 3.0, 1.0, 1.0), (.7, .6, 1.0, 1.0),
               (.7, .8, 1.0, 1.0), (.7, 1.5, 1.0, 1.0),
               (.25, 3.0, 1.0, 1.0)]
    for _ in range(80):
        beta = rng.uniform(.4, 2.2)
        E = rng.uniform(.2, 3.8)
        peq = occupancy(0, beta, E)
        p = peq + rng.uniform(.05, .98) * (1 - peq)
        k = rng.uniform(.3, 2.5)
        samples.append((p, E, beta, k))

    for p, E, beta, k in samples:
        optima = []
        cap = critical_voltage(beta, E, p)
        for t in (.03, .15, .8, 3):
            w = optimizer(t, beta, E, p, k)
            optima.append(w)
            assert w > 0 and (w < cap if math.isfinite(cap) else True)
            checks += 1
            assert abs(log_derivative(w, t, beta, E, p, k)) < 2e-9
            checks += 1
            assert abs(work(w, t, beta, E, p, k) - work_from_transitions(w, t, beta, E, p, k)) < 3e-13
            checks += 1
            for ratio in (.3, .7, 1.2, 2.0):
                v = w * ratio
                if v < cap:
                    assert work(w, t, beta, E, p, k) >= work(v, t, beta, E, p, k) - 1e-12
                checks += 1
            h = min(w / 3, (cap - w) / 3 if math.isfinite(cap) else w / 3, 1e-5)
            derivative = (math.log(work(w + h, t, beta, E, p, k)) -
                          math.log(work(w - h, t, beta, E, p, k))) / (2 * h)
            assert abs(derivative) < 8e-5
            checks += 1
        threshold = 2 * (2 * p - 1)
        gap = beta * E - threshold
        if gap > 1e-8:
            assert all(a < b + 1e-9 for a, b in zip(optima, optima[1:]))
        elif gap < -1e-8:
            assert all(a > b - 1e-9 for a, b in zip(optima, optima[1:]))
        else:
            assert all(abs(w - E) < 1e-7 for w in optima)
        checks += 1

    for p, beta, k in ((.6, 2., .5), (.7, 1., 2), (.95, .5, 3), (1., 1., 1.)):
        E = 2 * (2 * p - 1) / beta
        for t in (.001, .1, 1, 9):
            w = optimizer(t, beta, E, p, k)
            assert abs(w - E) < 5e-8
            checks += 1

    for E in (.3, 1, 2, 3.6):
        beta = 1.0
        for t in (.0001, .01, 1, 100):
            w = optimizer(t, beta, E, 1.0, 1)
            assert abs(log_derivative(w, t, beta, E, 1.0, 1)) < 2e-9
            checks += 1
    print('PASS:', checks, 'independent numerical and transition-law checks')


if __name__ == '__main__':
    check()

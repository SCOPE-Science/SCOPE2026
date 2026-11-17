#!/usr/bin/env python3
"""Standalone numerical consistency tests for a hierarchical population model.
Run with Python 3; no third-party modules required. Finite tests supplement, not replace, the analytical proof.
"""
import math
import random


def deriv(y, r, d, pred):
    n = len(pred) + 1
    x, h = y[:n], y[n:]
    s = sum(x)
    growth = r * (1.0 - s) - d
    dx = [x[0] * growth]
    for i in range(1, n):
        dx.append(x[i] * (growth - pred[i - 1] * x[i - 1]))
    return dx + list(x[:-1])


def integrate(x0, r, d, pred, horizon, step=0.02, checkpoints=()):
    n = len(x0)
    m = round(horizon / step)
    assert abs(m * step - horizon) < 1.e-8
    y = list(x0) + [0.0] * (n - 1)
    stored = {0.0: y[:n]}
    checkset = set(round(t / step) for t in checkpoints)
    if 0 in checkset:
        stored[0.0] = y[:n]
    for k in range(1, m + 1):
        a = deriv(y, r, d, pred)
        b = deriv([z + step * v / 2 for z, v in zip(y, a)], r, d, pred)
        c = deriv([z + step * v / 2 for z, v in zip(y, b)], r, d, pred)
        e = deriv([z + step * v for z, v in zip(y, c)], r, d, pred)
        y = [z + step * (v1 + 2*v2 + 2*v3 + v4)/6 for z, v1, v2, v3, v4 in zip(y, a, b, c, e)]
        if k in checkset:
            stored[round(k*step, 10)] = y[:n]
    return y, stored


def test_finite_ratio():
    rng = random.Random(20260908)
    checks = 0
    for n in range(2, 10):
        for _ in range(15):
            raw = [0.2 + rng.random() for _ in range(n)]
            x0 = [0.5 * z / sum(raw) for z in raw]
            r = 1.2 + rng.random() * 1.8
            d = 0.1 + rng.random() * 0.7
            pred = [0.3 + rng.random() * 2.5 for _ in range(n - 1)]
            y, _ = integrate(x0, r, d, pred, 6.0, 0.02)
            xf, hazard = y[:n], y[n:]
            assert 0 < sum(xf) < 1.0
            ratio0 = x0[0]
            for i in range(1, n):
                predicted = x0[i] / ratio0 * math.exp(-pred[i-1] * hazard[i-1])
                observed = xf[i] / xf[0]
                assert abs(predicted - observed) <= 2e-8 * max(1., abs(observed))
                checks += 1
    return checks


def test_asymptotics():
    checks = 0
    for n in range(2, 7):
        x0 = [.24] + [0.11 * (.88**j) for j in range(n-1)]
        assert sum(x0) < 1
        pred = [3.0] * (n - 1)
        _, values = integrate(x0, 2., .6, pred, 200., 0.02, checkpoints=[160., 200.])
        a,b = values[160.],values[200.]
        q = .7
        assert abs(sum(b)-q) < 5e-6, (n, sum(b))
        for i in range(n):
            if i%2==0:
                assert b[i] > .001, (n,i,b[i])
                assert abs(b[i]-a[i]) < 1e-5, (n,i,b[i]-a[i])
            else:
                # Exact exponential rate, with the predecessor's limiting density.
                measured = -math.log(b[i]/a[i])/40.
                rate = 3 * b[i-1]
                assert abs(measured-rate) < 4.e-4, (n,i,measured,rate)
            checks += 1
    return checks


def main():
    f = test_finite_ratio()
    a = test_asymptotics()
    print('PASS:',f,'finite-time ratio/integral identities;',a,'long-time selection/rate assertions')
    print('Numerical tests are not an infinite-dimensional or all-initial-condition proof.')

if __name__ == '__main__':
    main()

"""Independent numerical spot checks for the six-shape Erlang stability theorem.

Run with Python 3.10+ and numpy; the mathematical proof does not rely on this.
"""
import math
import numpy as np
from numpy.polynomial.polynomial import polymul


def cuts(q, a, b):
    return [(j, q * math.tan(j * math.pi / q) /
             math.sqrt(a - (-1) ** j * b * math.cos(j * math.pi / q) ** q))
            for j in range(1, (q - 1) // 2 + 1)]


def characteristic(q, a, b, tau):
    p = np.array([1.0])
    for _ in range(q):
        p = polymul(p, [1, tau / q])
    p = polymul(p, [a, 0, 1])
    p[0] -= b
    return p


def count_unstable(q, a, b, tau):
    roots = np.roots(characteristic(q, a, b, tau)[::-1])
    assert min(abs(z.real) for z in roots) > 1e-6, (q, a, b, tau, roots)
    return sum(z.real > 0 for z in roots)


def validate():
    scenarios = [(4.0, 2.0), (2.2, 0.7), (5.0, 4.0), (0.8, 0.11)]
    total = 0
    for a, b in scenarios:
        assert a > b > 0
        for q in range(1, 7):
            th = cuts(q, a, b)
            assert len(th) == (q - 1) // 2
            assert all(th[i][1] < th[i + 1][1] for i in range(len(th) - 1))
            for j, tau in th:
                ang = j * math.pi / q
                omega = math.sqrt(a - (-1) ** j * b * math.cos(ang) ** q)
                lam = 1j * omega
                delta = lam ** 2 + a - b * (1 + lam * tau / q) ** (-q)
                assert abs(delta) < 1e-10, (q, a, b, j, delta)
                x = tau * omega / q
                B = (-1) ** j * b * math.cos(ang) ** q
                h = 1 / (1 + 1j * x)
                deriv = -B * lam * h / (2 * lam + B * tau * h)
                assert deriv.real * ((-1) ** (j + 1)) > 0
                total += 2
            boundaries = [0.0] + [t for _, t in th]
            sample = []
            for left, right in zip(boundaries, boundaries[1:]):
                sample.append((left + right) / 2 if left else right / 3)
            sample.append(boundaries[-1] * 1.5 if th else 1.0)
            for zone, t in enumerate(sample):
                predicted = 2 if (q in (3, 4) and zone > 0) or (q in (5, 6) and zone == 1) else 0
                # Thresholds for nearly degenerate cases can be weakly hyperbolic.
                n = count_unstable(q, a, b, t)
                assert n == predicted, (q, a, b, t, n, predicted)
                total += 1
    print(f"PASS: {total} characteristic/threshold/crossing and root-count checks")


if __name__ == '__main__':
    validate()

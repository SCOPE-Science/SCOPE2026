"""Reproduce exact finite-instance identities and example flows for the incremental voter mean field.

Python standard library only; the analytic proof in RESULT.md establishes all k.
"""
from fractions import Fraction as Q
from math import isclose


def field(tails):
    m = len(tails)
    a = sum(tails) / m
    z = [1] + list(tails) + [0]
    return [a * z[i - 1] + (1 - a) * z[i + 1] - z[i] for i in range(1, m + 1)]


def recovered_masses(tails):
    return [1 - tails[0]] + [tails[i] - tails[i + 1] for i in range(len(tails) - 1)] + [tails[-1]]


def exact_checks():
    count = 0
    for k in range(2, 17):
        m = 2 * k
        u = [Q(m + 1 - i, m + 1) for i in range(1, m + 1)]
        w = [i * (m + 1 - i) for i in range(1, m + 1)]
        assert field(u) == [0] * m
        assert sum(w) == Q(m * (m + 1) * (m + 2), 6)
        assert Q(2, m * (m + 1)) * sum(w) == Q(m + 2, 3) > 1
        assert all(2 * w[i] - (w[i - 1] if i else 0) - (w[i + 1] if i + 1 < m else 0) == 2 for i in range(m))
        eps = Q(1, 3 * (m + 1) * (m + 2))
        for sign in [-1, 1]:
            s = [x + sign * eps * y for x, y in zip(u, w)]
            p = recovered_masses(s)
            assert sum(p) == 1 and all(x > 0 for x in p)
            expected = [
                sign * eps * Q(m - 1, 3)
                + eps * eps * Q((m + 1) * (m + 2) * (2 * i - m - 1), 3)
                for i in range(1, m + 1)
            ]
            actual = field(s)
            assert actual == expected, (k, sign)
            assert all(sign * x > 0 for x in actual)
            count += 1
    return count


def rk4(q, dt=0.05, steps=5000):
    m = len(q) - 1
    s = [float(sum(q[i:])) for i in range(1, m + 1)]

    def rhs(x):
        a = sum(x) / m
        z = [1.0] + x + [0.0]
        return [a * z[i - 1] + (1 - a) * z[i + 1] - z[i] for i in range(1, m + 1)]

    for _ in range(steps):
        a = rhs(s)
        b = rhs([v + dt * d / 2 for v, d in zip(s, a)])
        c = rhs([v + dt * d / 2 for v, d in zip(s, b)])
        d = rhs([v + dt * e for v, e in zip(s, c)])
        s = [v + dt * (aa + 2 * bb + 2 * cc + dd) / 6 for v, aa, bb, cc, dd in zip(s, a, b, c, d)]
    return s


def witness_checks():
    up = [Q(i, 100) for i in (19, 19, 19, 19, 24)]
    down = list(reversed(up))
    u = [Q(5 - i, 5) for i in range(1, 5)]
    su = [sum(up[i:]) for i in range(1, 5)]
    sd = [sum(down[i:]) for i in range(1, 5)]
    assert all(a > b for a, b in zip(su, u))
    assert all(a < b for a, b in zip(sd, u))
    assert sum(i * x for i, x in enumerate(up)) == Q(21, 10)
    assert sum(i * x for i, x in enumerate(down)) == Q(19, 10)
    final_up, final_down = rk4(up), rk4(down)
    assert all(isclose(v, 1.0, rel_tol=0, abs_tol=1e-8) for v in final_up), final_up
    assert all(isclose(v, 0.0, rel_tol=0, abs_tol=1e-8) for v in final_down), final_down
    return (final_up, final_down)


if __name__ == '__main__':
    print('Exact barrier configurations:', exact_checks())
    print('Verified convergence witnesses (tail limits):', witness_checks())
    print('PASS: all reproducibility checks')

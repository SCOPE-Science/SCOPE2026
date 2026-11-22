"""Reproduce rational orbit tests for a planar nonsmooth-fold return map.

The proof is analytical; finite checks guard algebra, branch conditions and
sample asymptotic formulas, not the quantified theorem.
"""
from fractions import Fraction as Q
from math import sqrt, log


def orbit(alpha, delta, mu, h=Q(1), max_steps=5000):
    tl = 1 + delta - alpha
    tr = 1 + delta + alpha
    x, y = -h, Q(0)
    history = [(x, y)]
    first_switch = None
    for n in range(1, max_steps + 1):
        xx = (tl if x < 0 else tr) * x + y + mu
        yy = -delta * x
        x, y = xx, yy
        history.append((x, y))
        if first_switch is None and x >= 0:
            first_switch = n
        if x >= h:
            assert first_switch is not None
            return first_switch, n, history
    raise AssertionError('Expected finite passage, reached iteration cap')


def predict(alpha, delta, mu, h):
    a, d = float(alpha), float(delta)
    t = 1 - sqrt(a)
    tl = 1 + d - a
    tr = 1 + d + a
    lam = (tl + sqrt(max(0, tl * tl - 4 * d))) / 2
    gamma = (tr + sqrt(tr * tr - 4 * d)) / 2
    L = log(float(alpha * h / mu))
    main = L / -log(lam) + L / log(gamma)
    if delta == Q(1, 4) and alpha == Q(1, 4):
        main += log(L) / -log(t)
    return main


def check():
    a, h = Q(1, 4), Q(1)
    for d in (Q(4, 25), Q(1, 4)):
        for power in (5, 10, 20, 40):
            mu = Q(1, 10 ** power)
            N, T, hist = orbit(a, d, mu, h)
            assert hist[N-1][0] < 0 <= hist[N][0]
            assert all(x < 0 for x, _ in hist[:N])
            assert all(hist[n+1][0] > hist[n][0] >= 0
                       for n in range(N, T))
            # The exact second-order recurrence holds for each actual branch.
            for n in range(1, T):
                xp = hist[n-1][0]
                xn = hist[n][0]
                expected = (1+d+(a if xn >= 0 else -a))*xn-d*xp+mu
                assert hist[n+1][0] == expected
            if d == Q(1, 4):
                # Critical Jordan formula, exact for every left-branch index.
                q = mu / a
                for n in range(N+1):
                    formula = q - (h+q+n*(h+q/2)) / 2**n
                    assert hist[n][0] == formula
            err = T - predict(a, d, mu, h)
            assert abs(err) < 4.0, (d, power, err)
            print(f'delta={d}, mu=1e-{power}: switch={N}, exit={T}, remainder={err:.6f}')
    print('PASS: 8 exact-rational trajectory and asymptotic comparisons')

if __name__ == '__main__':
    check()

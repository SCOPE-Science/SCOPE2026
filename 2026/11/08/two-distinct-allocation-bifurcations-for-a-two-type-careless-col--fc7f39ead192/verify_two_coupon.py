"""Exact finite-chain checks for a two-type post-loss collector.

Python 3 standard library only. Tests are checks, not substitutes for the
analytic monotonicity and classification argument.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random

COUNT = 0


def check(ok):
    global COUNT
    assert ok
    COUNT += 1


def solve(A, b):
    n = len(b)
    a = [[F(z) for z in row] + [F(bi)] for row, bi in zip(A, b)]
    for i in range(n):
        k = next(j for j in range(i, n) if a[j][i])
        a[i], a[k] = a[k], a[i]
        v = a[i][i]
        a[i] = [u / v for u in a[i]]
        for j in range(n):
            if j != i:
                u = a[j][i]
                a[j] = [w - u * h for w, h in zip(a[j], a[i])]
    return [row[-1] for row in a]


def chain(p1, p2):
    q1, q2 = 1 - p1, 1 - p2
    rows = []
    for state in range(4):
        row = [F(0)] * 4
        for drawn in (0, 1):
            held = state | (1 << drawn)
            for out in range(4):
                if out & ~held:
                    continue
                prob = F(1, 2)
                for i, qi in enumerate((q1, q2)):
                    if held & (1 << i):
                        prob *= qi if out & (1 << i) else (1 - qi)
                row[out] += prob
        check(sum(row) == 1)
        rows.append(row)
    return rows


def formulas(p1, p2):
    q1, q2 = 1 - p1, 1 - p2
    s, t = q1 + q2, q1 * q2
    pi = t * (s - t) / (4 - 2 * s + t)
    hit = ((5 - s) * t + 4 - 2 * s) / (t * (s - t))
    return pi, hit


def direct(p1, p2):
    P = chain(p1, p2)
    A = [[(int(i == j) - P[i][j]) for j in range(3)] for i in range(3)]
    h = solve(A, [1, 1, 1])[0]
    K = [[P[j][i] - int(i == j) for j in range(4)] for i in range(4)]
    K[-1] = [F(1)] * 4
    stat = solve(K, [0, 0, 0, 1])
    check(sum(stat) == 1)
    check(all(z >= 0 for z in stat))
    return stat[3], h


def d_pi(s, t):
    return (4 - 2 * s) * (s - 2 * t) - t * t


def d_h(s, t):
    return (5 - s) * t * t + 2 * (4 - 2 * s) * t - s * (4 - 2 * s)


def station_opt_t(s):
    low, high = s - 1, s * s / 4
    A = 4 - 2 * s
    r = sqrt(float(A * (A + s))) - float(A)
    return max(float(low), min(float(high), r))


def hitting_opt_t(s):
    low, high = s - 1, s * s / 4
    A = 4 - 2 * s
    r = (sqrt(float(A * A + s * (5 - s) * A)) - float(A)) / float(5 - s)
    return max(float(low), min(float(high), r))


def main():
    rng = Random(31)
    for d in range(1, 26):
        for i in range(d + 1):
            p1, p2 = F(i, 2 * d), F(d - i, 2 * d)
            check(direct(p1, p2) == formulas(p1, p2))
    # Extra unequal internal probabilities and substantial erasure budgets.
    for _ in range(150):
        p1 = F(rng.randrange(0, 99), 100)
        p2 = F(rng.randrange(0, 100 - int(100 * p1)), 100)
        check(direct(p1, p2) == formulas(p1, p2))
    # Endpoint derivative signs classify all optimizers; compare each
    # analytic projected root to grid minima/maxima (numerical diagnostics).
    for d in range(1, 200):
        B = d / 200
        s = 2 - B
        lo, hi = s - 1, s * s / 4
        ps, hs = station_opt_t(s), hitting_opt_t(s)
        for j in range(41):
            t = lo + (hi - lo) * j / 40
            pi = t * (s - t) / (4 - 2 * s + t)
            h = ((5 - s) * t + 4 - 2 * s) / (t * (s - t))
            pi_opt = ps * (s - ps) / (4 - 2 * s + ps)
            h_opt = ((5 - s) * hs + 4 - 2 * s) / (hs * (s - hs))
            check(pi <= pi_opt + 1e-12)
            check(h >= h_opt - 1e-11)
    pi_uniform, hit_uniform = direct(F(1,4), F(1,4))
    pi_boundary, hit_boundary = direct(F(0), F(1,2))
    check((pi_uniform, hit_uniform) == (F(27,80), F(152,27)))
    check((pi_boundary, hit_boundary) == (F(1,3), F(11,2)))
    check(pi_uniform > pi_boundary and hit_uniform > hit_boundary)
    for i in range(1, 100):
        s = F(1) + F(i, 100)
        lo, hi = s - 1, s * s / 4
        check(d_pi(s, lo) >= d_pi(s, hi))
        check(d_h(s, lo) <= d_h(s, hi))
    print(f'PASS: {COUNT} exact-rational assertions and finite numerical diagnostics')


if __name__ == '__main__':
    main()

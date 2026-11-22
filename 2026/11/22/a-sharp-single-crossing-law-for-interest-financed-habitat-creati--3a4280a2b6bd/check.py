"""Dependency-free finite checks for the one-patch restoration timing theorem.

Run: python check.py
These finite checks supplement, but do not establish, the all-parameter proof.
"""
from math import exp, expm1, isclose

N = 0

def test(condition, label):
    global N
    N += 1
    if not condition:
        raise AssertionError(label)


def occupancy(s, a, e, r, H):
    q = a * exp(r * s)
    y = q + e
    return q / y * (-expm1(-y * (H - s)))


def B(q, e, t):
    y = q + e
    return t + e * (expm1(y * t) - y * t) / (y * y)


def Bq(q, e, t):
    y = q + e
    x = y * t
    return e / y**3 * ((x - 2) * exp(x) + 2 + x)


def Bt(q, e, t):
    y = q + e
    return (q + e * exp(y * t)) / y


def positive_identity(q, e, t):
    y = q + e
    x = y * t
    theta = q / y
    phi = e / y
    return (phi**2 * exp(x) * expm1(x)
            + theta * phi * (3 * expm1(x) - x)
            + theta**2 * x) / y


def G(s, a, e, r, H):
    return r * B(a * exp(r * s), e, H - s) - 1


def optimal(a, e, r, H):
    if G(0, a, e, r, H) <= 0:
        return 0.
    lo, hi = 0., H
    for _ in range(90):
        mid = (lo + hi) / 2
        if G(mid, a, e, r, H) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def ode_probability(q, e, t, steps=1000):
    # Independent constant-rate Kolmogorov forward ODE integration (RK4).
    h = t / steps
    y = 0.
    def f(x):
        return q * (1 - x) - e * x
    for _ in range(steps):
        k1 = f(y)
        k2 = f(y + h * k1 / 2)
        k3 = f(y + h * k2 / 2)
        k4 = f(y + h * k3)
        y += h * (k1 + 2*k2 + 2*k3 + k4)/6
    return y


def main():
    from itertools import product
    for q, e, t in product((.2, .5, 1., 2., 3.), (.1, .4, 1., 2.), (.1, .4, 1., 1.8)):
        b = B(q, e, t)
        test(b > t, 'strict effect of extinction on threshold')
        test(Bq(q, e, t) > 0, 'derivative in colonization rate')
        test(Bt(q, e, t) > 1, 'derivative in horizon')
        lhs = Bt(q, e, t)*b - q*Bq(q, e, t)
        rhs = positive_identity(q, e, t)
        test(lhs > 0 and rhs > 0, 'global single-crossing determinant')
        test(isclose(lhs, rhs, rel_tol=1e-10, abs_tol=1e-12), 'determinant identity')
        test(B(q, e + .01, t) > b, 'extinction lowers critical interest')
        test(B(q+.01, e, t) > b, 'higher baseline colonization lowers critical interest')
    for a, e, H, r in product((.25, 1., 2.), (.25, 1., 2.), (.35, 1., 1.8), (.1, .3, .7, 1.5)):
        s = optimal(a, e, r, H)
        test(0 <= s < H, 'optimal time feasible')
        test((s == 0) == (r <= 1/B(a, e, H)), 'sharp interest threshold')
        if s > 0:
            test(abs(G(s, a, e, r, H)) < 1e-8, 'unique interior first order condition')
        v = occupancy(s, a, e, r, H)
        for j in range(31):
            test(v + 1e-11 >= occupancy(H*j/30, a, e, r, H), 'global maximum grid')
        for trial_s in (0., H/3, 2*H/3):
            q = a * exp(r*trial_s)
            v0 = ode_probability(q, e, H-trial_s, 400)
            test(isclose(v0, occupancy(trial_s, a, e, r, H), rel_tol=2e-10, abs_tol=2e-11), 'ODE vs closed form')
    a = e = H = 1.
    critical = 4/(exp(2)+1)
    test(isclose(critical, 1/B(a, e, H), rel_tol=1e-14), 'exact example threshold')
    s = optimal(1, 1, 1, 1)
    test(.36 < s < .37, 'exact example optimal time bracket')
    test(occupancy(s,1,1,1,1) > occupancy(0,1,1,1,1)+.03, 'strict gain')
    print(f'PASS: {N} deterministic supplementary assertions')

if __name__ == '__main__':
    main()

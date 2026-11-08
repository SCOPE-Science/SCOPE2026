"""Standalone exact and numerical checks for the critical quadratic composition theorem.

Only standard-library modules are needed. Numerical tests illustrate asymptotics;
all unbounded-time conclusions are proved analytically in RESULT.md.
"""
from fractions import Fraction as F


def composition_step(p, r):
    theta = [r] + [F(1)] * (len(p) - 1)
    raw = [t * x * (2 - x) for t, x in zip(theta, p)]
    total = sum(raw)
    return [v / total for v in raw]


def original_step(x, r, a):
    s = sum(x)
    theta = [r * a] + [a] * (len(x) - 1)
    return [t * v * (2 * s - v) / 2 for t, v in zip(theta, x)]


def checks():
    # Exact rational agreement of normalized physical and projective iterates.
    for r in [F(3, 2), F(2), F(5, 2)]:
        for m in [2, 3, 5]:
            x = [F(i + 1, m + 3) for i in range(m + 1)]
            p = [v / sum(x) for v in x]
            for _ in range(6):
                x = original_step(x, r, F(7, 11))
                p = composition_step(p, r)
                assert p == [v / sum(x) for v in x]
                assert sum(p) == 1 and min(p) > 0
    # Exact fixed compositions on the coexistence side.
    for m in range(2, 8):
        for r in [F(1), F(3, 2), F(19, 10)]:
            q = (2 - r) / (1 + m * r)
            p = [1 - m * q] + [q] * m
            assert min(p) > 0 and composition_step(p, r) == p

    # Check the exact critical algebraic scalar drift and ordering identity.
    for m in range(2, 8):
        p = [F(8, 13)] + [F(5 * j, 13 * m * (m + 1) // 2) for j in range(1, m + 1)]
        assert sum(p) == 1
        u = sum(p[1:]); b = sum(q*q for q in p[1:])
        E = 2 + 2*u - 2*u*u - b
        pn = composition_step(p, F(2))
        un = sum(pn[1:])
        assert un == (2*u-b)/E
        assert u-un == (1-u)*(2*u*u+b)/E
        assert all(pn[j] == p[j]*(2-p[j])/E for j in range(1,m+1))
        assert un < u

    # Quantitative convergence: total minority mass is universal even when
    # the individual minority fractions equilibrate relatively slowly.
    for m in range(2, 8):
        w = [float(j) for j in range(1, m+1)]
        q = [0.37 * v/sum(w) for v in w]
        u = sum(q)
        initial_ratio = max(q)/min(q)
        N = 260000
        for t in range(1,N+1):
            b = sum(v*v for v in q)
            E = 2 + 2*u - 2*u*u - b
            q = [v*(2-v)/E for v in q]
            u = sum(q)
        target = 2*m/(2*m+1)
        assert abs(N*u-target) < 0.008, (m, N*u, target)
        assert max(q)/min(q) < initial_ratio
        assert max(abs(N*v - 2/(2*m+1)) for v in q) < 0.075

    # Supercritical ratio formula, and nonzero geometric rescaled limit.
    r = 2.5
    p = [0.45, 0.10, 0.25, 0.20]
    previous = [p[j]/p[0] for j in range(1,4)]
    for n in range(1,550):
        nxt = [r*p[0]*(2-p[0])] + [p[j]*(2-p[j]) for j in range(1,4)]
        s = sum(nxt)
        pn = [v/s for v in nxt]
        w = [pn[j]/pn[0] for j in range(1,4)]
        assert all(0 < a/b <= 2/r+1e-13 for a,b in zip(w,previous))
        previous = w; p = pn
    print('PASS: exact rational identities, equilibrium threshold, critical and supercritical numerical checks')


if __name__ == '__main__':
    checks()

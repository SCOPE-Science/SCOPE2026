"""Independent finite checks for the Fourier-mode stability theorem.
Run with the Python 3 standard library: python verify_modes.py
"""
import cmath
import math
from fractions import Fraction


def parameters(r, d):
    c = d / (5 * (1 - r))
    b = 5 * c + math.log((1 - r) / r)
    return c, b


def symbol(j, k, h, w):
    x = 2 * math.pi * j / h
    y = 2 * math.pi * k / w
    return ((1 + 2 * math.cos(x)) * (1 + 2 * math.cos(y)) - 1) / 8


def eigenvalues(r, d, a):
    trace = 1 - r + d * a
    determinant = d * (r + (1 - r) * a)
    root = cmath.sqrt(trace * trace - 4 * determinant)
    return ((trace + root) / 2, (trace - root) / 2)


def mode_stable(r, d, a):
    flip = -1 / d - r / (2 - r)
    ns = (1 / d - r) / (1 - r)
    return flip < a < ns


def update(S, R, h, w, p, c, b):
    ans_S = [[0.0] * w for _ in range(h)]
    ans_R = [[0.0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            near = sum(R[(i+u) % h][(j+v) % w]
                       for u in (-1, 0, 1) for v in (-1, 0, 1) if (u, v) != (0, 0)) / 8
            avg = (1-p) * R[i][j] + p * near
            ans_S[i][j] = S[i][j] * (1 - R[i][j]) + c
            ans_R[i][j] = 1 / (1 + math.exp(b - 5 * S[i][j] * avg))
    return ans_S, ans_R


def checks():
    count = 0
    for r in (.05, .25, .6, .9):
        for d in (.15, .75, 1, 1.5, 3, 6, 14):
            for h, w in ((4, 4), (6, 5), (7, 6), (8, 8)):
                for p in (0, .03, .2, .5, .7, .99, 1):
                    for j in range(h):
                        for k in range(w):
                            a = 1 - p + p * symbol(j, k, h, w)
                            eig = eigenvalues(r, d, a)
                            delta = max(abs(z) for z in eig) - 1
                            if abs(delta) > 1e-9:
                                assert (delta < 0) == mode_stable(r, d, a), (r, d, h, w, p, j, k)
                            count += 1
    # The two sharp crossings also hold over exact rational arithmetic.
    rr = Fraction(1, 4); dd = Fraction(3)
    ans = Fraction(1, 9)
    T = 1-rr + dd*ans
    D = dd*(rr+(1-rr)*ans)
    assert T == Fraction(13, 12) and D == 1
    afl = -Fraction(10, 21)
    Tfl = 1-rr+dd*afl
    Dfl = dd*(rr+(1-rr)*afl)
    assert Tfl == -Fraction(19, 28) and Dfl == -Fraction(9, 28)
    assert 1+Tfl+Dfl == 0
    r, d = .25, 3.
    assert abs((-1/d-r/(2-r)) + 10/21) < 1e-14
    assert abs(((1/d-r)/(1-r)) - 1/9) < 1e-14
    for p, stable in ((.5, False), (.6, True), (.95, True), (.99, False)):
        a = 1 - 1.5 * p
        assert (max(abs(z) for z in eigenvalues(r, d, a)) < 1) == stable
        count += 1
    # Nonlinear two-component map, direct directional finite-difference check
    # against its 2x2 Fourier block for multiple wave numbers.
    h = w = 4
    p = .7
    c, b = parameters(r, d)
    s0, r0 = c/r, r
    eps = 1e-6
    for j, k in ((0, 0), (2, 0), (1, 1), (2, 2)):
        mode = [[math.cos(2*math.pi*(j*i/h+k*ii/w))
                 for ii in range(w)] for i in range(h)]
        mu = symbol(j, k, h, w)
        a = 1 - p + p * mu
        for ds, dr in ((1., 0.), (0., 1.)):
            Splus = [[s0+eps*ds*mode[i][ii] for ii in range(w)] for i in range(h)]
            Rplus = [[r0+eps*dr*mode[i][ii] for ii in range(w)] for i in range(h)]
            Sminus = [[s0-eps*ds*mode[i][ii] for ii in range(w)] for i in range(h)]
            Rminus = [[r0-eps*dr*mode[i][ii] for ii in range(w)] for i in range(h)]
            P = update(Splus, Rplus, h, w, p, c, b)
            M = update(Sminus, Rminus, h, w, p, c, b)
            derivative = ((P[0][0][0]-M[0][0][0])/(2*eps),
                          (P[1][0][0]-M[1][0][0])/(2*eps))
            predicted = ((1-r)*ds-c/r*dr,
                         5*r*r*(1-r)*ds+d*a*dr)
            assert max(abs(x-y) for x,y in zip(derivative,predicted)) < 1e-8
            count += 1
    print('VERIFY_OK mode_samples=%d finite_difference_modes=4 exact_window=(16/27,62/63)' % count)


if __name__ == '__main__':
    checks()

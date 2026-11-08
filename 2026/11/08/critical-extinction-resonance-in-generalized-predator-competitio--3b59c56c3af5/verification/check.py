"""Reproduce exact coefficients and finite-time tests for the critical extinction theorem.

Requires Python 3, scipy and numpy. No finite integration certifies an asymptotic limit.
"""
from fractions import Fraction as F
from math import log
from scipy.integrate import solve_ivp

K = F(2)
alpha = F(1)
xi = F(1, 2)
eta = F(3, 2)
c = F(4, 5)
B = 1 + alpha * xi
beta = c * xi
delta = eta * (K + xi) / (B + K)
A = K / (B + K)
lam = eta * K * (B - xi) / (B + K) ** 3
assert (B, beta, delta, A, lam) == (F(3, 2), F(2, 5), F(15, 14), F(4, 7), F(24, 343))
assert beta + lam == F(806, 1715)

case_count = 0
for p in (1.25, 1.5, 1.75, 2.0):
    r = p - 1
    a = r * float(beta)
    for x0, y0 in ((0.7, 0.6), (3.5, 2.2)):
        def rhs(t, state):
            x, u = state
            y = u ** (-1 / r)
            return (x * (1 - x / float(K)) - x * y / (float(B) + x),
                    r * (float(beta) + float(eta) *
                         (float(delta / eta) - (x + float(xi)) / (float(B) + x)) * u))

        tvec = (2000., 10000., 50000.)
        sol = solve_ivp(rhs, (0, tvec[-1]), (x0, y0 ** (-r)),
                        t_eval=tvec, rtol=2e-11, atol=2e-13, max_step=100.)
        assert sol.success and len(sol.t) == 3
        assert min(sol.y[0]) > 0 and min(sol.y[1]) > 0
        u0, u1, u2 = sol.y[1]
        assert abs(u2 / tvec[-1] - (float(beta + lam) if p == 2 else a)) < (0.0002 if p == 2 else .005)
        if p == 1.25:
            assert abs((u2 - a * tvec[2]) - (u1 - a * tvec[1])) < 1e-3
        elif p == 1.5:
            obtained = ((u2 - a * tvec[2]) - (u1 - a * tvec[1])) / log(tvec[2] / tvec[1])
            assert abs(obtained - float(lam / beta)) < .003
        elif p == 1.75:
            exponent = (2 * r - 1) / r
            h = (1 - r) / r
            expected = r * float(lam) * a ** (-h) / exponent
            assert abs((u2 - a * tvec[2]) / tvec[2] ** exponent - expected) < .004
        else:
            assert abs(u2 / tvec[-1] - float(beta + lam)) < .0002
        if p >= 1.5:
            x = sol.y[0][1]
            y = u1 ** (-1/r)
            assert abs((float(K) - x) / y - float(A)) < .003
        case_count += 1

print('VERIFY_OK rational_coefficients=5 fractional_regimes=3 quadratic_endpoint=1 parameter_cases=8 finite_times=3')

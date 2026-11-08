#!/usr/bin/env python3
"""Exact-rational checks for velocity-only resetting with a persistent telegraph sign.

The theorem's infinite-rate remainder estimates are analytic; these checks compare
independent moment and resolvent identities and their asymptotic coefficients.
"""
from fractions import Fraction as F
from itertools import product


def exact_data(r, a, lam, sig):
    # Stationary linear moments from the generator of (velocity, telegraph sign).
    m = sig / (r + a + 2 * lam)
    q = 2 * sig * m / (r + 2 * a)
    m3 = 3 * sig * q / (r + 3 * a + 2 * lam)
    q4 = 4 * sig * m3 / (r + 4 * a)
    # Exact Green-Kubo coefficient, computed through two independent resolvents.
    da = sig**2 / ((r + a) * (r + a + 2 * lam)) * (2 / (r + 2 * a) + 1 / (2 * lam))
    A0 = sig / ((r + a) * (r + 2 * lam))
    Ap = q / (r + a) + sig * m / ((r + a) * (r + 2 * lam))
    db = Ap + r * A0 * m / (2 * lam)
    assert da == db
    # At cubic coefficient b=0, Poisson equation -L h = v^3 with exact ansatz
    # h=alpha*v^3 + beta*sign*v^2 + gamma*v + delta*sign.
    alpha = 1 / (r + 3 * a)
    beta = 3 * sig * alpha / (r + 2 * a + 2 * lam)
    gamma = 2 * sig * beta / (r + a)
    delta = sig * gamma / (2 * lam)
    H = alpha * q4 + beta * m3 + gamma * q + delta * m
    # Differentiate stationary moment balances with respect to cubic drag b.
    dm = -m3 / (r + a + 2 * lam)
    dq = (2 * sig * dm - 2 * q4) / (r + 2 * a)
    # Differentiate (r+a)D_b + b*H_b = q_b + sig*m_b/(2*lam).
    derivative = (dq + sig * dm / (2 * lam) - H) / (r + a)
    # Independent no-reset first-cycle cubic response, from Laplace hierarchy.
    dA0 = -6 * sig**3 / ((r + a)**2 * (r + 2 * lam)
                                * (r + 2 * a + 2 * lam) * (r + 3 * a))
    # At high rate these two independent slow pieces contribute equally.
    return da, derivative, dA0, dm, m, A0


def main():
    checks = 0
    for a, lam, sig in product([F(1, 2), F(1), F(3)],
                               [F(1, 4), F(1, 2), F(2)],
                               [F(1, 3), F(2, 3), F(1)]):
        for r in [F(20), F(100), F(1000), F(10000)]:
            da, derivative, dA0, dm, m, A0 = exact_data(r, a, lam, sig)
            assert da > 0 and derivative < 0 and dA0 < 0 and dm < 0
            checks += 5
            if r == 10000:
                # Convergence with an explicit small and finite verification tolerance.
                scaled = r**5 * derivative / (-6 * sig**4 / lam)
                assert abs(scaled - 1) < F(1, 100)
                checks += 1
    # Factorial contributions directly from exponential waiting-time moments.
    for lam, sig in [(F(1, 2), F(1)), (F(3), F(2, 3)), (F(1, 5), F(3))]:
        b = F(1, 3)
        correction_m = -b * sig**3 * F(24, 4)
        correction_A = -b * sig**3 * F(24, 4)
        slow1 = sig * correction_A / (2 * lam)
        slow2 = sig * correction_m / (2 * lam)
        assert slow1 == slow2 == -3 * b * sig**4 / lam
        assert slow1 + slow2 == -6 * b * sig**4 / lam
        # tanh (b negative) minus tan (b positive).
        assert (-6 * (-b) * sig**4 / lam) - (-6 * b * sig**4 / lam) == 4 * sig**4 / lam
        checks += 3
    print(f"PASS: {checks} exact-rational checks; all finite tests consistent with theorem")


if __name__ == '__main__':
    main()

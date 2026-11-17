"""Independent finite numerical checks of an exact q-product spectral model.

Requires mpmath. Results check a sample of parameters; the theorem uses
analytic product identities and Rouche's theorem, not these finite tests.
"""
import mpmath as mp

mp.mp.dps = 115
checks = 0


def qprod(q, n):
    return mp.fprod(1 - q ** (2 * k) for k in range(1, n + 1))


def G(q, z):
    return z ** 3 * mp.fprod(1 + q ** (2 * m) * z * z for m in range(1, 240))


for qtxt in ('0.2', '0.3', '0.5'):
    q = mp.mpf(qtxt)
    Qinf = qprod(q, 220)
    # Euler product coefficients; the explicit rank-one coefficients agree.
    for r in range(1, 12):
        k = r + 1
        W = q ** (k * (2 * k + 1) / 4)
        gamma = q ** ((2 * k * k - 5 * k) / 4) / qprod(q, k - 1)
        expected = q ** (r * (r + 1)) / qprod(q, r)
        assert mp.almosteq(W * gamma, expected, rel_eps=mp.mpf('1e-98'))
        checks += 1
    for z in (mp.mpc('0.125', '0.21'), mp.mpc('-0.36', '0.07')):
        S = mp.fsum(q ** (r * (r + 1)) / qprod(q, r) * z ** (2 * r + 3)
                    for r in range(50))
        assert abs(G(q, z) - S) < mp.mpf('1e-93')
        checks += 1
    for j in range(2, 7):
        zp = mp.j * q ** (-j)
        derivative = 2 * (-1) ** (j - 1) * q ** (-j * (j + 1)) * qprod(q, j - 1) * Qinf
        computed = mp.diff(lambda z: G(q, z), zp)
        assert abs((computed - derivative) / derivative) < mp.mpf('1e-88')
        checks += 1
        for c in (mp.mpf(1), mp.mpf(-2), mp.mpc('1.0', '0.2')):
            d = c / derivative
            z = mp.findroot(lambda zz: G(q, zz) - c,
                            (zp + d * mp.mpf('0.90'), zp + d * mp.mpf('1.10')),
                            tol=mp.mpf('1e-85'), maxsteps=50, solver='secant')
            assert abs(G(q, z) - c) < mp.mpf('1e-65')
            # The relative error in the first displacement is o(1).
            assert abs((z - zp) / d - 1) < mp.mpf('0.07')
            if j >= 4:
                assert abs((z - zp) / d - 1) < mp.mpf('1e-4')
            # The perturbed root is in the annulus predicted by the theorem.
            assert q ** (-j + mp.mpf('0.5')) < abs(z) < q ** (-j - mp.mpf('0.5'))
            checks += 3
print('PASS:', checks, 'numerical coefficient, product, derivative and root checks')

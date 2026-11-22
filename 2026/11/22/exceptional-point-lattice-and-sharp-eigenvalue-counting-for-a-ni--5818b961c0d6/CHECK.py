"""Finite diagnostic checks for an explicit compact rank-one perturbation.

Requires mpmath. The infinite-dimensional conclusions require the analytic proof.
"""
import mpmath as mp

mp.mp.dps = 70
checks = 0

def verify(test):
    global checks
    assert test
    checks += 1

for coupling in [mp.mpf('1'), mp.mpc('0.5', '0.7'), mp.mpc('-0.2', '0.3')]:
    c = 1 + 1 / coupling
    for k in [-100, -20, -10, -3, -2, -1, 0, 1, 2, 3, 10, 20, 100]:
        z = -c - mp.lambertw(-mp.exp(-c), k)
        verify(abs(mp.exp(z) - 1 - z - 1 / coupling) < mp.mpf('1e-57'))
        if abs(z) > mp.mpf('1e-30'):
            lam = 1 / z
            verify(abs(1 - coupling * (mp.exp(1 / lam) - 1 - 1 / lam)) < mp.mpf('1e-57'))

for k in [-10, -5, -2, -1, 1, 2, 5, 10]:
    z0 = 2 * mp.pi * 1j * k
    alpha0 = 1 / (mp.exp(z0) - 1 - z0)
    verify(abs(alpha0 - 1j / (2 * mp.pi * k)) < mp.mpf('1e-61'))
    verify(abs(mp.exp(z0) - 1) < mp.mpf('1e-61'))
    verify(abs(mp.exp(z0) - 1 - z0 - 1 / alpha0) < mp.mpf('1e-61'))

for coupling in [mp.mpf('0.1'), mp.mpf('1'), mp.mpf('10')]:
    b = 1 / coupling
    zplus = mp.findroot(lambda z: mp.exp(z) - 1 - z - b, (1, 5))
    zminus = mp.findroot(lambda z: mp.exp(z) - 1 - z - b, (-b-3, -b))
    verify(zplus > 0 and zminus < 0)
    verify(abs(mp.exp(zplus) - 1 - zplus - b) < mp.mpf('1e-61'))
    verify(abs(mp.exp(zminus) - 1 - zminus - b) < mp.mpf('1e-61'))
    verify(abs(zminus) > zplus)

for coupling in [mp.mpf('1'), 1j, mp.mpc('0.7', '-0.2')]:
    for sgn in [-1, 1]:
        for k0 in [20, 100, 500]:
            k = sgn * k0
            center = mp.log(2 * mp.pi * k0) + 1j * (2 * mp.pi * k + sgn * mp.pi / 2)
            root = mp.findroot(lambda z: mp.exp(z) - 1 - z - 1 / coupling,
                               (center-mp.mpf('0.05'), center+mp.mpf('0.05')))
            verify(abs(root-center) < 5 * mp.log(k0) / k0)

for k in [-4, -2, -1, 1, 2, 4]:
    z0 = 2 * mp.pi * 1j * k
    beta0 = -z0
    for delta in [mp.mpf('1e-8'), mp.mpf('1e-12'), -mp.mpf('1e-8')]:
        h = mp.sqrt(2 * delta)
        zp = mp.findroot(lambda z: mp.exp(z) - 1 - z - beta0 - delta,
                         (z0 + h * mp.mpf('0.99'), z0 + h * mp.mpf('1.01')))
        zm = mp.findroot(lambda z: mp.exp(z) - 1 - z - beta0 - delta,
                         (z0 - h * mp.mpf('0.99'), z0 - h * mp.mpf('1.01')))
        verify(abs((zp - z0) / h - 1) < mp.mpf('1e-3'))
        verify(abs((zm - z0) / h + 1) < mp.mpf('1e-3'))
        verify(abs(zp - zm) > mp.mpf('1e-8'))

print('PASS:', checks, 'finite diagnostic checks')

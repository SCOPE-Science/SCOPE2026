"""Reproduce checks for the orientationally averaged active-Brownian exit-time coefficient.

Only numerical diagnostics; the accompanying RESULT.md supplies the analytical proof.
Run: python verify.py  (requires mpmath)
"""
import mpmath as mp

mp.mp.dps = 65


def f(gamma, rho):
    if gamma == 0:
        return (rho**3 - rho) / 16
    k = mp.sqrt(gamma)
    return (mp.besseli(1, k * rho) / mp.besseli(1, k) - rho) / (2 * gamma)


def G(gamma, rho):
    if gamma == 0:
        return -(1-rho**2)**2 / 128
    k = mp.sqrt(gamma)
    return ((mp.besseli(0, k) - mp.besseli(0, k * rho)) /
            (k * mp.besseli(1, k)) - (1-rho**2)/2) / (4 * gamma)


def close(a, b, tol=mp.mpf('1e-35')):
    assert abs(a-b) < tol, (a, b)


for g in map(mp.mpf, ['0', '0.001', '0.1', '1', '10', '100']):
    for r in map(mp.mpf, ['0', '0.2', '0.6', '0.9']):
        close(G(g,r), mp.quad(lambda s: f(g,s), [r, 1])/2)
        assert G(g,r) < 0
        if r:
            radial = (mp.diff(lambda s: f(g,s),r,2) +
                      mp.diff(lambda s: f(g,s),r)/r -
                      (r**-2+g)*f(g,r))
            close(radial, r/2)
        assert G(g,r) > G(mp.mpf(0),r) if g>0 else True

for r in map(mp.mpf, ['0','0.2','0.6','0.9']):
    vals = [G(mp.mpf(g),r) for g in ['0','0.001','0.1','1','10','100']]
    assert all(x < y < 0 for x,y in zip(vals, vals[1:]))

for z in map(mp.mpf, ['0.1', '1', '3']):
    target = (1-mp.exp(-z)-z)/4
    for gamma in map(mp.mpf, ['10000','1000000']):
        scaled = gamma**mp.mpf('1.5')*G(gamma, 1-z/mp.sqrt(gamma))
        assert abs(scaled-target) < mp.mpf('0.03'), (z, gamma, scaled, target)

print('PASS: radial PDE, quadrature identity, endpoint polynomial, sampled signs, monotone samples, wall-layer values')

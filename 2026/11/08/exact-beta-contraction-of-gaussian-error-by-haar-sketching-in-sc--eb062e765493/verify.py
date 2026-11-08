"""Independent numerical diagnostics for scalar sketch-and-solve laws.
Run with python 3 and numpy. Finite checks support, not replace, proofs.
"""
import math
import numpy as np

RNG = np.random.default_rng(20261105)
checks = 0

def check(expr, info):
    global checks
    assert expr, info
    checks += 1

def shape_params(n, ell, is_complex):
    h = 1.0 if is_complex else 0.5
    return h, h * ell, h * (n - ell), h * (ell - 1)

def moment(n, ell, is_complex, power):
    h, a, b, c = shape_params(n, ell, is_complex)
    if power >= a:
        return math.inf
    g = math.exp(math.lgamma(h + power) + math.lgamma(a - power)
                 - math.lgamma(h) - math.lgamma(a))
    f = math.exp(math.lgamma(b + power) + math.lgamma(b + c)
                 - math.lgamma(b) - math.lgamma(b + c + power)) if c else 1.
    return g * f

def tail_constant(n, ell, is_complex):
    h, a, b, c = shape_params(n, ell, is_complex)
    g = math.exp(math.lgamma(a + h) - math.lgamma(h) - math.lgamma(a + 1))
    f = math.exp(math.lgamma(b + a) + math.lgamma(b + c)
                 - math.lgamma(b) - math.lgamma(b + c + a)) if c else 1.
    return g * f

def sample_direct(n, ell, complex_, count=2800):
    out_h = np.empty(count)
    out_g = np.empty(count)
    for k in range(count):
        if complex_:
            G = (RNG.standard_normal((n, ell)) + 1j * RNG.standard_normal((n, ell))) / math.sqrt(2)
        else:
            G = RNG.standard_normal((n, ell))
        q, _ = np.linalg.qr(G, mode='reduced')
        q1, q2 = q[0, :], q[1, :]
        out_h[k] = abs(np.vdot(q1, q2) / np.vdot(q1, q1)) ** 2
        g1, g2 = G[0, :], G[1, :]
        out_g[k] = abs(np.vdot(g1, g2) / np.vdot(g1, g1)) ** 2
        if k < 40:
            P = q @ q.conj().T
            check(abs(P[0, 0].real - np.vdot(q1, q1).real) < 2e-13, 'projector diagonal')
            check(abs(P[1, 0]) ** 2 <= P[0,0].real * (1 - P[0,0].real) + 1e-13, 'projector bound')
    return out_h, out_g

def ks(x, y):
    x = np.sort(x)
    y = np.sort(y)
    n, m = len(x), len(y)
    vals = np.sort(np.r_[x, y])
    return float(np.max(np.abs(np.searchsorted(x, vals, side='right') / n
                               - np.searchsorted(y, vals, side='right') / m)))

for is_complex in (False, True):
    for n, ell in ((8, 5), (7, 4)) if not is_complex else ((7, 4), (6, 3)):
        h, a, b, c = shape_params(n, ell, is_complex)
        direct_h, direct_g = sample_direct(n, ell, is_complex)
        count = len(direct_h)
        W = RNG.gamma(shape=a, scale=1., size=count)
        Z = RNG.gamma(shape=h, scale=1., size=count)
        beta = RNG.beta(b, c, size=count)
        model_g, model_h = Z / W, beta * Z / W
        dg = ks(direct_g, model_g)
        dh = ks(direct_h, model_h)
        check(dg < .062, f'Gaussian distribution ({n},{ell},{is_complex}): {dg}')
        check(dh < .062, f'Haar distribution ({n},{ell},{is_complex}): {dh}')
        expected_g = h / (a - 1)
        expected_h = moment(n, ell, is_complex, 1.)
        check(abs(expected_h / expected_g - b / (b+c)) < 1e-11, 'source expectation')
        if a > 2:
            for direct, truth, name in ((direct_h, expected_h, 'Haar'), (direct_g, expected_g, 'Gauss')):
                # Finite-variance cases only; loose Monte Carlo statistical tolerance
                check(abs(float(np.mean(direct)) - truth) < .22 * truth + .02,
                      f'finite-sample mean {name}, n={n},ell={ell},obs={np.mean(direct)},truth={truth}')
        for p in (.1, .25, .5, .75, .9):
            check(float(np.quantile(model_h,p)) < float(np.quantile(model_g,p)), 'distributional coupling')
        print(f'field={"complex" if is_complex else "real"}, n={n}, ell={ell}, KS Haar={dh:.4f}, Gaussian={dg:.4f}, ER_H={expected_h:.6g}, ER_G={expected_g:.6g}, tailconst={tail_constant(n,ell,is_complex):.7g}')

# Boundary shape tests, including ell=1 where the factor degenerates.
for is_complex in (False, True):
    for n in range(3, 10):
        check(moment(n, 1, is_complex, 0.25) > 0, 'ell=1 positive moment')
        check(math.isinf(moment(n, 1, is_complex, 1.)), 'ell=1 infinite mean')
        for ell in range(2,n):
            h, a, b, c = shape_params(n,ell,is_complex)
            check(moment(n,ell,is_complex,a - 1e-4) > 0, 'finite lower moment')
            check(math.isinf(moment(n,ell,is_complex,a)), 'critical infinite moment')
            check(math.isinf(moment(n,ell,is_complex,a+0.25)), 'supercritical infinite moment')
            check(0 < tail_constant(n,ell,is_complex) < math.inf, 'positive tail coeff')
print('VERIFIER_OK', checks)

"""Independent finite-grid diagnostics for an upwind target Gramian theorem.

Dependencies: Python 3, NumPy, SciPy. Run without arguments.
Finite tests are corroboration, not a proof of the limiting statements.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.special import gammaln, ndtr


def impulse(h, cells_width, cells_gap, speed, time):
    """Exact semidiscrete impulse response for two aligned interval indicators."""
    z = speed * time / h
    if z <= 0:
        return 0.0
    r = np.arange(1, 2 * cells_width)
    ks = cells_gap + r
    triangular = np.minimum(r, 2 * cells_width - r)
    pmfs = np.exp(-z + ks * np.log(z) - gammaln(ks + 1))
    return h * float(triangular @ pmfs)


def direct_impulse(h, A, n, v, t):
    size = 2 * A + n
    shift = np.diag(np.ones(size - 1), -1)
    generator = v / h * (shift - np.eye(size))
    b = np.r_[np.ones(A), np.zeros(size - A)]
    c = np.r_[np.zeros(A + n), np.ones(A)]
    return h * float(c @ expm(generator * t) @ b)


def gramian(h, A, n, v, T):
    return quad(lambda t: impulse(h, A, n, v, t) ** 2, 0, T,
                epsabs=1e-17, epsrel=1e-9, limit=300)[0]


def gramian_subcritical_scaled(h, A, n, v, T):
    """Endpoint change of variable; accurate when the answer is tiny."""
    endpoint = impulse(h, A, n, v, T)
    assert endpoint > 0
    upper = min(T / h, 90)
    ratio_integral = quad(
        lambda y: (impulse(h, A, n, v, max(T-h*y, 0)) / endpoint) ** 2,
        0, upper, epsabs=1e-12, epsrel=1e-10, limit=300)[0]
    return h * endpoint**2 * ratio_integral


def subcritical_prediction(h, gap, speed, T):
    theta = speed * T / gap
    assert 0 < theta < 1
    rate = gap * (theta - 1 - math.log(theta))
    prefactor = T * theta**2 / (4 * math.pi * gap**2 * (1-theta)**5)
    return prefactor * h**4 * math.exp(-2 * rate / h)


def layer_prediction(gap, speed, s):
    phi = lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)
    normal_positive_part = lambda z: phi(z) + z*ndtr(z)
    return gap**1.5/speed * quad(
        lambda z: normal_positive_part(z)**2, -12, s,
        epsabs=1e-13, epsrel=1e-11)[0]


def check():
    cases = 0
    for A, n in [(2, 2), (3, 2), (4, 3), (3, 4)]:
        h = 1/max(A, n)
        for t in [0.1, 0.5, 1.2, 2.1]:
            a = impulse(h, A, n, 1.0, t)
            b = direct_impulse(h, A, n, 1.0, t)
            assert abs(a-b) <= 2e-11
            cases += 1
    print('Finite semigroup versus Poisson identities: PASS', cases)

    for width_ratio, speed in [(1, 1), (0.5, 2)]:
        # Physical gap = 1, physical interval width = width_ratio.
        # T=0.4/speed stays before the physical arrival T=1/speed.
        T = .4 / speed
        ratios = []
        for n in [50, 100, 250, 500]:
            assert abs(n*width_ratio-round(n*width_ratio)) < 1e-12
            A = round(n*width_ratio)
            h = 1/n
            approx = gramian_subcritical_scaled(h, A, n, speed, T)
            target = subcritical_prediction(h, 1, speed, T)
            ratios.append(approx/target)
        assert all(0 < x < 1.02 for x in ratios)
        assert all(x < y for x, y in zip(ratios, ratios[1:]))
        assert ratios[-1] > 0.96, (width_ratio, speed, ratios)
        print('Prearrival refinement:', width_ratio, speed,
              [round(x, 6) for x in ratios])

    K = (1 - 1/math.sqrt(2)) / (3*math.sqrt(math.pi))
    numerical_K = layer_prediction(1, 1, 0)
    assert abs(K-numerical_K) < 1e-11
    ratios = []
    for n in [50, 100, 200, 400]:
        h = 1/n
        value = gramian(h, n, n, 1, 1)
        ratios.append(value/(K*h**1.5))
    assert all(.90 < x < 1.01 for x in ratios)
    assert all(x < y for x, y in zip(ratios, ratios[1:]))
    assert ratios[-1] > .97
    print('Critical horizon refinement:', [round(x, 6) for x in ratios])

    n = 250
    h = 1/n
    for s in [-1.0, 0.0, 1.0]:
        T = 1 + s*math.sqrt(h)
        value = gramian(h, n, n, 1, T)
        predicted = h**1.5 * layer_prediction(1, 1, s)
        ratio = value/predicted
        assert .78 < ratio < 1.03, (s, ratio)
        print('Critical-window parameter', s, 'ratio', round(ratio, 6))
    print('VERIFY_OK')


if __name__ == '__main__':
    check()

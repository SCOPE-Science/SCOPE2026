"""Independent numerical checks of flat-Klein-bottle injectivity-radius formulas.

Requires Python 3, NumPy and SciPy. Deck transformations are enumerated
independently from the explicit one-dimensional probability formula.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


def deck_injectivity(q: float, x: np.ndarray) -> np.ndarray:
    """Directly enumerate images of basepoints (x,0) under deck maps.

    Generators: a(x,y)=(x+q,y), b(x,y)=(-x,y+1).
    """
    sq = np.full(x.shape, np.inf)
    for j in range(-3, 4):
        for k in range(-4, 5):
            if k == 0 and j == 0:
                continue
            ximage = ((-1)**j) * x + k * q
            sq = np.minimum(sq, (ximage - x)**2 + j*j)
    return 0.5 * np.sqrt(sq)


def closed_radius(q: float, x: np.ndarray) -> np.ndarray:
    t = np.remainder(2*x, q)
    delta = np.minimum(t, q-t)
    return 0.5 * np.minimum(np.minimum(q, 2.0), np.sqrt(1+delta**2))


def mean_injectivity_normalized(q: float) -> float:
    if q <= 1:
        return math.sqrt(q)/2
    if q < 2/math.sqrt(3):
        z = math.sqrt(q*q-1)
        return (q*q - q*z + math.acosh(q))/(2*q**1.5)
    if q < 2*math.sqrt(3):
        return ((q/2)*math.sqrt(1+q*q/4)+math.asinh(q/2))/(2*q**1.5)
    return (q-math.sqrt(3)+math.asinh(math.sqrt(3))/2)/q**1.5


def cdf_normalized_doubled(q: float, y: float) -> float:
    """CDF of Y=2 inj/sqrt(area) for uniform basepoint."""
    if q <= 1:
        return float(y >= math.sqrt(q))
    lower = 1/math.sqrt(q)
    upper = min(q, 2, math.sqrt(1+q*q/4))/math.sqrt(q)
    if y < lower:
        return 0.
    if y >= upper:
        return 1.
    return (2/q)*math.sqrt(max(0., q*y*y-1))


def optimizer_equation(q: float) -> float:
    return q*q - q*math.sqrt(q*q - 1) - 3*math.acosh(q)


def check():
    rng = np.random.default_rng(2026)
    qs = [0.3, 0.9, 1, 1.001, 1.036, 1.14, 1.155, 1.7, 2.2, 3.4, 3.47, 7, 15]
    max_direct = 0.
    max_integral = 0.
    for q in qs:
        x = rng.uniform(0, q, 50000)
        d = deck_injectivity(q, x)
        exact = closed_radius(q, x)
        max_direct = max(max_direct, np.max(np.abs(d-exact)))
        assert np.allclose(d, exact, atol=1e-12), q
        num = quad(lambda u: min(q, 2., math.sqrt(1+u*u)), 0, q/2,
                   epsabs=4e-12, points=([math.sqrt(min(q,2)**2-1)]
                   if 1 < min(q,2) and math.sqrt(min(q,2)**2-1) < q/2 else None))[0] / q**1.5
        # q<=1 follows from the same integral, integrand=min(q,...)=q.
        f = mean_injectivity_normalized(q)
        max_integral = max(max_integral, abs(num-f))
        assert abs(num-f) < 1e-9, (q,num,f)
        y = 2*d/math.sqrt(q)
        # Compare empirical CDF on nontrivial continuity thresholds.
        lo, hi = y.min(), y.max()
        for frac in ([0.2, 0.5, 0.8] if hi-lo > 1e-10 else []):
            t = lo+(hi-lo)*frac
            p = cdf_normalized_doubled(q, t)
            emp = np.mean(y <= t)
            assert abs(emp-p) < 0.015, (q,t,emp,p)
    qstar=brentq(optimizer_equation,1.000001,2/math.sqrt(3),xtol=1e-14)
    assert abs(qstar-1.035267) < 2e-6
    vstar=mean_injectivity_normalized(qstar)
    assert 0.50278 < vstar < 0.50279
    assert vstar > mean_injectivity_normalized(1)
    # Sampled comparison is supplementary; uniqueness is proven analytically.
    grid=np.r_[np.linspace(0.02,qstar-0.00005,250),
               np.linspace(qstar+0.00005,30,600)]
    assert np.all(np.array([mean_injectivity_normalized(q) for q in grid]) < vstar)
    # Check continuity at both nontrivial transitions.
    for a in [1,2/math.sqrt(3),2*math.sqrt(3)]:
        assert abs(mean_injectivity_normalized(a*(1-1e-9)) -
                   mean_injectivity_normalized(a*(1+1e-9))) < 1e-7
    print('FLAT_KLEIN_INJECTIVITY_LAW_CHECKS_OK',
          'qstar',format(qstar,'.13f'), 'optimal_value', format(vstar,'.13f'),
          'deck_error', format(max_direct,'.3e'),
          'integral_error',format(max_integral,'.3e'))

if __name__ == '__main__':
    check()

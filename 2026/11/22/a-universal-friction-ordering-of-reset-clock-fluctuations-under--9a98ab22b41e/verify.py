"""Reproducible numerical checks of the friction/reset-clock ordering.

Requires Python 3, scipy, numpy. Analytical arguments are in RESULT.md; this
script deliberately tests only representative parameters, not all parameters.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma


def cumulative_hazard_shape(alpha: float, y: float) -> float:
    """H_alpha(y) = integral_0^y (1-exp(-u))**alpha du.

    Closed forms for three exponents spanning both monotonicity directions.
    """
    if y == 0:
        return 0.0
    if alpha == -0.5:
        return y + 2.0 * math.log1p(math.sqrt(-math.expm1(-y)))
    if alpha == 1.0:
        if y < 0.001:
            return sum((-1)**k * y**k / math.factorial(k) for k in range(2, 11))
        return y + math.expm1(-y)
    if alpha == 2.0:
        if y < 0.001:
            # Direct noncancelling numerical integration near the origin.
            return quad(lambda u: (-math.expm1(-u))**2, 0, y, epsabs=1e-15)[0]
        return y - 1.5 + 2*math.exp(-y) - 0.5*math.exp(-2*y)
    raise ValueError("Checker supports alpha=-1/2,1,2")


def raw_quantile(alpha, damping, p):
    z = -math.log1p(-p)
    target = z * damping**(alpha+1)  # Force and rate scales = 1.
    hi = max(1., target * 3)
    while cumulative_hazard_shape(alpha, hi) < target:
        hi *= 2
    return brentq(lambda u: cumulative_hazard_shape(alpha,u)-target,
                  0,hi,xtol=1e-12)/damping


def cv2(alpha, damping):
    # Scale time by a characteristic scale to keep quadrature stable.
    tscale = 1.0 if damping <= 1 else damping**alpha
    def survival(u):
        y = damping*tscale*u
        h = damping**(-alpha-1)*cumulative_hazard_shape(alpha,y)
        return math.exp(-h)
    m1 = quad(survival, 0, math.inf, epsabs=1e-11,
              epsrel=1e-11, limit=300)[0]
    m2 = 2*quad(lambda u: u*survival(u), 0, math.inf,
                epsabs=1e-11, epsrel=1e-11, limit=300)[0]
    return m2/m1**2-1


def main():
    for a in [-.5, 1., 2.]:
        gs = [.1,.3,1.,3.,10.]
        v = [cv2(a,g) for g in gs]
        left = gamma(1+2/(a+1))/gamma(1+1/(a+1))**2-1
        assert all(min(left,1) < x < max(left,1) for x in v)
        assert all((v[i+1]>v[i]) if a>0 else (v[i+1]<v[i]) for i in range(len(v)-1))
        ps = np.linspace(.02,.98,41)
        r = [raw_quantile(a,3,p)/raw_quantile(a,.3,p) for p in ps]
        assert all((r[i+1]>r[i]) if a>0 else (r[i+1]<r[i]) for i in range(len(r)-1))
        print(f'alpha={a:4g}, zero-drag CV2={left:.10f}, tested CV2={v}')
    # High-friction coefficient check: c_alpha = integral_0^infty[(1-e^-u)^alpha-1]du.
    for a, c in [(-.5, 2*math.log(2)),(1.,-1.),(2.,-1.5)]:
        g = 100. if a>0 else 1.e4
        eps = g**(-a-1)
        observed = cv2(a,g)
        leading = 1+2*c*eps
        assert abs(observed-leading) < 10*eps**2
        print(f'alpha={a:4g}, epsilon={eps:.6g}, CV2={observed:.10f}, first-order={leading:.10f}')
    print('PASS: numerical moments, quantile-ratio directions, limiting coefficients')

if __name__ == '__main__':
    main()

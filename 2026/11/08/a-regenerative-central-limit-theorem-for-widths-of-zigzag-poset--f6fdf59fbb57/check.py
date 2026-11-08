"""Independent checks for Gaussian projection widths of zigzag-poset polytopes.
Only standard definitions and reproducible numerical tests are used here.
"""
import math
import itertools
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import ndtr


def path_stable_support(g):
    prev = 0.0
    total = 0.0
    for a in g:
        prev = max(0.0, a - prev)
        total += prev
    return total


def enumerate_support(g):
    n = len(g)
    best = 0.0
    for mask in range(1 << n):
        if mask & (mask << 1):
            continue
        best = max(best, sum(g[j] for j in range(n) if (mask >> j) & 1))
    return best


def c_integral():
    # Gaussian quadrature for the explicit stationary fixed-point density.
    N = 180
    nodes, w = leggauss(N)
    xs = (nodes + 1.0) * 4.0
    ws = 4.0 * w
    normalizer = 1.0 / math.sqrt(2.0 * math.pi)
    phi = lambda a: normalizer * np.exp(-a*a/2.0)
    density = np.zeros(N)
    p0 = 1.0
    K = phi(xs[:, None] + xs[None, :]) * ws[None, :]
    for _ in range(60):
        p0, density = (0.5*p0 + np.dot(ndtr(xs)*ws, density), p0*phi(xs)+K @ density)
    mass = p0 + density @ ws
    c = (xs*density) @ ws
    assert abs(mass-1.0) < 1e-8, mass
    return c


def simulation():
    rng=np.random.default_rng(1422019)
    for n in range(1,11):
        for _ in range(40):
            g=rng.standard_normal(n)
            assert abs(enumerate_support(g)-path_stable_support(g)) < 1e-11
            # Coordinate complementation on even sites is an isometry;
            # enumerate 0/1 order labels x_odd <= x_even and stable sets y.
            if n <= 8:
                for bits in itertools.product((0,1),repeat=n):
                    ord_ok=all((bits[j]<=bits[j+1] if j%2==0 else bits[j]>=bits[j+1]) for j in range(n-1))
                    y=tuple(bits[j] if j%2==0 else 1-bits[j] for j in range(n))
                    stab_ok=all(y[j]+y[j+1]<=1 for j in range(n-1))
                    assert ord_ok == stab_ok
    c=c_integral()
    assert .22 < c < .35, c
    # Random finite-path sample widths and their fluctuations.
    reps=16000
    n=512
    plus=np.zeros(reps)
    minus=np.zeros(reps)
    H=np.zeros(reps)
    Q=np.zeros(reps)
    for i in range(n):
        g=rng.standard_normal(reps)
        plus=np.maximum(g-plus,0.0)
        minus=np.maximum(-g-minus,0.0)
        H+=plus+minus
        Q+=g*g
    W=H/np.sqrt(Q)
    assert abs(W.mean()-2*c*math.sqrt(n)) < .11, (W.mean(),2*c*math.sqrt(n))
    # Euler-Gaussian identity implies Cov(H, sum G_i^2)=E(H), finite sample.
    cov=np.cov(H,Q,ddof=0)[0,1]
    assert abs(cov/H.mean()-1) < .10, (cov,H.mean())
    # The width does not concentrate to a deterministic constant after subtracting leading mean.
    assert .002 < W.var() < 4.0
    print('ZIGZAG_WIDTH_CHECKS_PASSED', 'c=',round(c,9), 'n=',n, 'sample_width_mean=',round(W.mean(),6),'sample_width_var=',round(W.var(),6),'gaussian_stein_ratio=',round(cov/H.mean(),4))

if __name__=='__main__':
    simulation()

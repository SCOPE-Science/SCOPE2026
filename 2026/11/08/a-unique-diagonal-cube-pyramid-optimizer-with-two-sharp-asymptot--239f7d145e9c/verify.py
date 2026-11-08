"""Finite reproducibility checks for diagonal-section cube pyramids.

Run: python verify.py. Requires SciPy (see requirements.txt).
Finite numerical checks support but do not replace the proof in RESULT.md.
"""
import math
from fractions import Fraction
from scipy.optimize import minimize_scalar, brentq
from scipy.stats import irwinhall


def exact_density(n, s):
    """Irwin-Hall density at rational s, using inclusion/exclusion."""
    s = Fraction(s)
    z = sum(((-1)**k) * math.comb(n, k) * max(s-k, 0)**(n-1)
            for k in range(n+1))
    return z / math.factorial(n-1)


def exact_density_prime(n, s):
    s = Fraction(s)
    z = sum(((-1)**k) * math.comb(n, k) * max(s-k, 0)**(n-2)
            for k in range(n+1))
    return z / math.factorial(n-2)


def stationarity(n, s):
    return irwinhall.pdf(s, n) + s * (irwinhall.pdf(s+1e-4, n) - irwinhall.pdf(s-1e-4, n)) / 2e-4


def optimum(n):
    r = minimize_scalar(lambda x: -(n/2+x)/n * irwinhall.pdf(n/2+x, n),
                        bounds=(0.0, min(1.0, n/2)), method='bounded',
                        options={'xatol': 1e-12})
    return r.x, -r.fun


def verify():
    count = 0
    # Normalize the exact density and its first derivative at rational knots.
    for n in range(3, 14):
        for k in range(7, 19):
            s = Fraction(n*k, 26)  # strictly in (0,n)
            if s.denominator == 1:
                continue
            f = float(exact_density(n, s))
            fp = float(exact_density_prime(n, s))
            sf = float(irwinhall.pdf(float(s), n))
            # Numerical central derivative, with quadratic centered approximation.
            h = 2e-5
            sdf = (float(irwinhall.pdf(float(s)+h,n)) -
                   float(irwinhall.pdf(float(s)-h,n))) / (2*h)
            assert abs(f-sf) < 2e-8 * max(1.0, abs(f)), (n,s,f,sf)
            assert abs(fp-sdf) < 6e-6 * max(1.0, abs(fp)), (n,s,fp,sdf)
            count += 2
    # n=3 exact global pyramid from the motivating work, and the unique diagonal position.
    x3, d3 = optimum(3)
    assert abs(x3 - (1/math.sqrt(2)-1/2)) < 5e-7
    assert abs(d3 - (1+math.sqrt(2))/6) < 5e-10
    count += 2
    # Strict unique critical maximum and value exceeding the centered choice.
    for n in range(3, 60):
        x, d = optimum(n)
        assert 0 < x < 1, (n,x)
        assert d > 0.5*irwinhall.pdf(n/2,n)
        for z in [0.0, x/2, x, (x+1)/2, 1.0]:
            val=(n/2+z)/n*irwinhall.pdf(n/2+z,n)
            assert val <= d * (1+5e-11), (n,z,val,d)
            count += 1
        count += 2
    # Second-order asymptotics: errors decrease faster than the retained orders.
    previous_x = None
    previous_r = None
    for n in [20, 40, 80, 160, 320, 640]:
        x, d = optimum(n)
        c = 0.5*irwinhall.pdf(n/2,n)
        xp = 1/6 + 2/(45*n)
        rp = 1 + 1/(6*n) + 7/(120*n*n)
        vp = math.sqrt(3/(2*math.pi*n))*(1 + 1/(60*n) + 73/(3360*n*n))
        ex = abs(x-xp)
        er = abs(d/c-rp)
        ev = abs(d/vp-1)
        assert ex < 3/(n*n), (n, x, xp, ex)
        assert er < 3/(n**3), (n,d/c,rp,er)
        assert ev < 3/(n**3), (n,d,vp,ev)
        if previous_x is not None:
            assert ex < previous_x*0.55, (n,ex,previous_x)
            assert er < previous_r*0.55, (n,er,previous_r)
            count += 2
        previous_x, previous_r = ex, er
        count += 3
    # Degenerate n=2 case, with central optimum.
    x2, d2 = optimum(2)
    assert x2 < 1e-4 and abs(d2-1/2)<1e-7
    count += 1
    print('All', count, 'finite reproducibility checks passed.')
    for n in [3,4,10,20,80,320]:
        x, d = optimum(n)
        print(f'n={n:3d}  s-n/2={x:.12f}  optimal_volume={d:.12f} '
              f'ratio_to_central={d/(0.5*irwinhall.pdf(n/2,n)):.12f}')


if __name__ == '__main__':
    verify()

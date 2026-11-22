"""Independent numerical checks of the two-erasure sine-Korobov formulas.

Requires numpy and scipy. Run: python verify.py
Finite checks corroborate, and do not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi


def density(t):
    return 0.5 * PI * abs(math.sin(2 * PI * t))


def kernel(d, gamma):
    z = d % 1.0
    return 1.0 + 2 * PI**2 * gamma * (z*z - z + 1/6)


def integrate(fn, left, right):
    breaks = [left, right]
    # Density's nondifferentiability points occur at integer half-periods.
    for j in range(math.floor(2*left)+1, math.ceil(2*right)):
        z = j/2
        if left < z < right:
            breaks.append(z)
    breaks = sorted(set(breaks))
    return sum(quad(fn, a, b, epsabs=2e-12, epsrel=2e-12)[0]
               for a, b in zip(breaks, breaks[1:]))


def formula(n):
    assert n >= 8 and n % 2 == 0
    x = np.array([j/n for j in range(n) if j not in (0, n//2)], dtype=float)
    m = len(x)
    extended = np.r_[x, x[0]+1]
    gaps = np.diff(extended)
    a = (gaps + np.roll(gaps, 1))/2
    hats = np.zeros(m)
    bubble = 0.0
    for j in range(m):
        l, r = extended[j:j+2]
        h = r-l
        hats[j] += integrate(lambda t: density(t)*(r-t)/h, l, r)
        hats[(j+1)%m] += integrate(lambda t: density(t)*(t-l)/h, l, r)
        bubble += integrate(lambda t: density(t)*(t-l)*(r-t), l, r)
    s3 = sum(gaps**3)
    q = min(hats/a)
    denom = 2*PI**2*bubble-(PI**2/3)*q*s3
    threshold = q/denom if denom > 0 else math.inf
    return x, a, hats, bubble, s3, q, threshold


def run():
    count = 0
    for n in (10, 12, 16, 20, 24, 40, 64):
        x, a, hats, bubble, s3, q, gc = formula(n)
        assert abs(s3 - (n+12)/n**3)<2e-13
        count+=1
        if n >= 12:
            closest = np.sort(np.argsort(hats/a)[:4])
            intended = np.sort(np.where(np.minimum(np.mod(x,0.5), 0.5-np.mod(x,0.5)) < 1.1/n)[0])
            assert np.array_equal(closest,intended), (n,closest,intended)
            count+=1
        for gamma in (0.5,3, 0.65*gc if np.isfinite(gc) else 3, 1.35*gc if np.isfinite(gc) else 10):
            G = np.array([[kernel(u-v,gamma) for v in x] for u in x])
            b = np.array([integrate(lambda t: density(t)*kernel(u-t,gamma),0,1) for u in x])
            direct = np.linalg.solve(G,b)
            correction = 2*PI**2*gamma*bubble/(1+PI**2*gamma*s3/3)
            predicted = hats - a*correction
            assert np.max(abs(direct-predicted))<1e-8, (n,gamma,np.max(abs(direct-predicted)))
            count+=1
            if np.isfinite(gc):
                assert (predicted.min() >= -1e-12) == (gamma <= gc*(1+1e-12)), (n,gamma,gc)
                count+=1
        if np.isfinite(gc):
            corrected=hats-a*2*PI**2*gc*bubble/(1+PI**2*gc*s3/3)
            assert abs(corrected.min())<1e-11
            count+=1
    for n in (80, 160, 320):
        _, _, _, _, _, _, gc=formula(n)
        constant=49*PI**2/27
        residue=gc-7*n/3
        assert abs(residue-constant)<300/n, (n,residue,constant)
        count+=1
    print(f'VERIFY_OK {count} checks; exact formula and threshold diagnostics passed')


if __name__ == '__main__':
    run()

"""Independent finite-state and numerical checks of a local-resetting pair observable.

Requires Python 3 with mpmath, numpy, scipy.  Finite calculations are
consistency checks, not proofs of the infinite-size or critical limits.
"""
import mpmath as mp
import numpy as np
from scipy.linalg import solve

checks = 0

def check(ok, description):
    global checks
    assert ok, description
    checks += 1


def site_moments(fitness, immigration, excess, reset):
    gap = 1 + excess - fitness
    return (immigration / (gap + reset),
            2 * (fitness + immigration) * immigration / ((gap + reset) * (2 * gap + reset)))


def numerical_site_moments(fitness, immigration, excess, reset, cutoff=240):
    generator = np.zeros((cutoff + 1, cutoff + 1), dtype=float)
    for n in range(cutoff + 1):
        if n < cutoff:
            generator[n, n + 1] += fitness * n + immigration
        if n:
            generator[n, n - 1] += (1 + excess) * n
            generator[n, 0] += reset
        generator[n, n] = -sum(generator[n, k] for k in range(cutoff + 1) if k != n)
    M = generator.T.copy()
    M[-1, :] = 1
    rhs = np.zeros(cutoff + 1)
    rhs[-1] = 1
    stat = solve(M, rhs)
    counts = np.arange(cutoff + 1)
    return np.dot(stat, counts), np.dot(stat, counts * (counts - 1))


def integrate(func, scale):
    breaks = [mp.mpf('0'), scale/30, scale/3, scale, scale*3, scale*30,
              mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('1')]
    return mp.quad(func, sorted(set(x for x in breaks if 0 <= x <= 1)))


def densities(nu, excess, C=mp.mpf('1.2'), beta=mp.mpf('0.3')):
    """q(ell)=2(1-ell), r(ell)=C(1-ell)^nu in the continuum model."""
    nu = mp.mpf(str(nu))
    excess = mp.mpf(str(excess))
    scale = (excess/C)**(1/nu)
    def denominator(e):
        return excess + e + C * e**nu
    mean_source = integrate(lambda e: (1-e)/denominator(e), scale)
    feedback = integrate(lambda e: 2*e/denominator(e), scale)
    rho = mean_source/(1-beta*feedback)
    pairs = integrate(lambda e: 2*(1-e)*(1-e+2*beta*rho*e) /
                       (denominator(e)*(2*(excess+e)+C*e**nu)), scale)
    return rho, pairs


def critical_constant(nu, C=mp.mpf('1.2')):
    p = 1/mp.mpf(str(nu))
    return (2*mp.pi* C**(-p) * (1-mp.power(2,p-1)) /
            (mp.mpf(str(nu)) * mp.sin(mp.pi*p)))


def run():
    global checks
    mp.mp.dps = 40
    # Independent finite generator solution, not obtained from moment identities.
    for pars in [(0.72, 0.4, 0.3, 0.23), (0.48, 0.31, 0.44, 0.22),
                 (0.81, 0.13, 0.51, 0.62)]:
        expected = site_moments(*pars)
        observed = numerical_site_moments(*pars)
        for k in (0,1):
            check(abs(expected[k]-observed[k]) < 3e-8,
                  'finite site occupation factorial moment')
    # Mean density must remain bounded as the pair density diverges.
    for nu in ('0.4','0.5','0.6','0.75'):
        rhos = []
        pairs = []
        for z in ('1e-3','1e-5','1e-7'):
            mean, pair = densities(nu,z)
            check(mean>0 and pair>0, 'positive mean and pair densities')
            rhos.append(mean)
            pairs.append(pair)
        check(rhos[0]<rhos[1]<rhos[2], 'finite mean approaches limiting value')
        check(pairs[0]<pairs[1]<pairs[2], 'pair density nondecreasing')
        if nu == '0.4':
            check(pairs[2] < mp.mpf('5.5'), 'subcritical pairs remain bounded in example')
        if nu == '0.5':
            ratio = pairs[2]/((4/mp.mpf('1.2')**2)*mp.log(10**7))
            check(mp.mpf('.75') < ratio < 1, 'logarithmic asymptotic approaching')
        if nu in ('0.6','0.75'):
            n=mp.mpf(nu)
            scale=critical_constant(n)*mp.mpf('1e-7')**(1/n-2)
            ratio=pairs[2]/scale
            check(mp.mpf('.95') < ratio < 1, 'power law approaching correct coefficient')
            # Independent beta integral for exact special-function coefficient.
            p=1/n
            quad = (2/n)*mp.quad(lambda x: x**(p-1)/((1+x)*(2+x)),[0,1,mp.inf])
            check(abs(quad*mp.mpf("1.2")**(-p)/critical_constant(n)-1)<mp.mpf('1e-14'),
                  'Euler beta integral amplitude')
    print('PASS:', checks, 'independent numerical consistency assertions')
    for nu in ('0.4','0.5','0.6','0.75'):
        rho, pair = densities(nu,'1e-7')
        print('nu=',nu,'rho=',mp.nstr(rho,9),'pair=',mp.nstr(pair,10))

if __name__ == '__main__':
    run()

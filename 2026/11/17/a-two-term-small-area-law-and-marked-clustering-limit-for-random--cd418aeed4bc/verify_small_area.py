"""Numerical diagnostics for the small-area law of four circle-uniform points.

Requirements: Python 3, NumPy, SciPy. Simulation is not a proof.
"""
import numpy as np
from math import pi
from scipy.integrate import quad


def coeff_integral():
    # Integrate over s=u+v, u in [0,s], w=1-s.
    def integrand(u, s):
        a, b, c = u, s - u, 1 - s
        p = (1-a)*(1-b)*(1-c)
        h = p/4
        q = (1-a)**2+(1-b)**2+(1-c)**2
        return q * h**(-5/3)

    def inner(s):
        return quad(lambda u: integrand(u, s), 0, s, epsabs=2e-7,
                    epsrel=2e-8, limit=250)[0]

    val = quad(inner, 0, 1, epsabs=2e-5, epsrel=2e-7,
               limit=250)[0]
    return val/(24*pi**3)


def sim(n=4_000_000, seed=42016):
    rng = np.random.default_rng(seed)
    counts = {t: 0 for t in [0.20, 0.10, 0.05, 0.02, 0.01]}
    count_clustering = 0
    for _ in range((n + 199_999)//200_000):
        m=min(200_000, n)
        n-=m
        if not m: break
        theta=np.sort(rng.uniform(0,2*pi,size=(m,4)),axis=1)
        gaps=np.diff(np.column_stack((theta,theta[:,0]+2*pi)),axis=1)
        a=0.5*np.sum(np.sin(gaps),axis=1)
        assert (a > -1e-12).all()
        for t in counts: counts[t]+=int(np.count_nonzero(a<t))
    return counts


def main():
    from scipy.integrate import quad
    # The leading integral is pi^2/4 and its normalized asymptotic constant is 1/pi.
    i=quad(lambda s: -2*np.log1p(-s)/(s*(2-s)), 0, 1,
           epsabs=2e-10)[0]
    assert abs(i-pi*pi/4)<1e-8, (i,pi*pi/4)
    c1=1/pi
    c2=coeff_integral()
    assert 0.2421<c2<0.2425, c2
    counts=sim()
    n=4_000_000
    for t,k in counts.items():
        obs=k/n
        theory=c1*t+c2*t**(5/3)
        # The neglected remainder is o(t^(5/3)), and sampling is stochastic;
        # use loose, diagnostic tolerances rather than treating this as a proof.
        print(f't={t:.3g} observed={obs:.7f} two_term={theory:.7f} diff={obs-theory:+.7f}')
        assert abs(obs-theory)<0.035*t*t+0.00025
    print(f'C1={c1:.12f} C2={c2:.12f}')
    print('CYCLIC_QUAD_SMALL_AREA_TWO_TERM_DIAGNOSTIC_OK')

if __name__=='__main__':main()

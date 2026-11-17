#!/usr/bin/env python3
"""Independent moment and exact-sign checks for uniform points in circular sectors.

Uses only Python's standard library.  Rational enclosures certify the
parameter inequalities without treating floating-point experiments as proof.
"""
from fractions import Fraction as F
from math import pi, sin, sqrt, cos
from random import Random


def atan_series_enclosure(x, terms=10):
    x = F(x)
    def partial(count):
        return sum(((-1)**j * x**(2*j + 1) / (2*j + 1) for j in range(count)), F(0))
    return partial(terms), partial(terms - 1)  # even count -> lower, odd -> upper


def pi_enclosure():
    lo5, hi5 = atan_series_enclosure(F(1, 5))
    lo239, hi239 = atan_series_enclosure(F(1, 239))
    return 16 * lo5 - 4 * hi239, 16 * hi5 - 4 * lo239


def k_rational_endpoints(a, b, qlo, qhi):
    # 1-a/q and 5/3-b/q increase with q>0.
    a, b = F(a), F(b)
    m2_lo, m2_hi = 1-a/qlo, 1-a/qhi
    m4_lo, m4_hi = F(5, 3)-b/qlo, F(5, 3)-b/qhi
    assert m2_lo > 0 and m4_lo > 0
    return m4_lo / m2_hi**2, m4_hi / m2_lo**2


def sinc(x):
    return sin(x)/x if x else 1.0


def moments_unit(theta):
    c1, c2 = sinc(theta/2), sinc(theta)
    m2 = 1 - F(8, 9).__float__()*c1*c1
    m4 = 5/3 - 32/15*c1*c1 + .5*c2*c2
    return m2, m4


def K(theta):
    m2, m4 = moments_unit(theta)
    return m4/(m2*m2)


def solve(k, lo, hi):
    vl = K(lo)-k
    vr = K(hi)-k
    assert vl*vr < 0
    for _ in range(80):
        mid = (lo+hi)/2
        vm = K(mid)-k
        if vl*vm <= 0: hi = mid
        else: lo, vl = mid, vm
    return (lo+hi)/2


def simulate(theta, n=160000, seed=0):
    rng = Random(seed)
    s2=s4=0.
    for j in range(n):
        r1=sqrt(rng.random());r2=sqrt(rng.random())
        dphi=theta*(rng.random()-rng.random())
        t=max(0.,r1*r1+r2*r2-2*r1*r2*cos(dphi))
        s2 += t; s4 += t*t
    return s2/n, s4/n


def main():
    pilo, pihi=pi_enclosure()
    assert F(3) < pilo < pihi < F(22,7)
    qlo,qhi=pilo*pilo,pihi*pihi
    ratios={
        'half':k_rational_endpoints(F(64,9),F(226,15),qlo,qhi),
        'full':k_rational_endpoints(F(32,9),F(128,15),qlo,qhi),
        'three_half':k_rational_endpoints(F(64,81),F(226,135),qlo,qhi),
    }
    assert ratios['half'][1] < F(9,5)
    assert ratios['full'][0] > F(39,20)
    assert ratios['three_half'][1] < F(9,5)
    for tag,(lo,hi) in ratios.items():
        print(f'{tag:12s} rigorous K in [{float(lo):.12f}, {float(hi):.12f}]')
    assert F(27,10)>F(39,20)
    for k in [1.8,1.9,1.94]:
        roots=[solve(k,1e-8,pi/2),solve(k,pi/2,pi),solve(k,pi,1.5*pi)]
        radius=[1/sqrt(moments_unit(t)[0]) for t in roots]
        assert roots[0] < pi/2 < roots[1] < pi < roots[2] < 1.5*pi
        for theta,r in zip(roots,radius):
            u,v=moments_unit(theta)
            assert abs(r*r*u-1) < 1e-12
            assert abs(r**4*v-k) < 1e-12
        print('K',k,'angles',*[f'{r:.10f}' for r in roots],
              'radii',*[f'{r:.10f}' for r in radius])
    for theta in [0.6,1.7,4.3,2*pi]:
        m2,m4=moments_unit(theta)
        em2,em4=simulate(theta,seed=int(theta*1000)+73)
        assert abs(m2-em2) < .007
        assert abs(m4-em4) < .03
        print(f'theta={theta:.5f} M2={m2:.7f} MC2={em2:.7f} M4={m4:.7f} MC4={em4:.7f}')
    print('CIRCULAR_SECTOR_TRIPLE_MOMENT_AMBIGUITY_OK')

if __name__=='__main__': main()

"""Independent reproducibility checks for synchronized partial resetting.

Requires Python 3, numpy; no external data or network access.
"""
import math
import numpy as np


def closed_form(a1, a2, d1, d2, rate, contraction):
    u = 1 - contraction**2
    delta = rate*u
    l1 = 2*a1 + delta
    l2 = 2*a2 + delta
    b = 2*(a1+a2) + rate*(1-contraction**4)
    means = (2*d1/l1, 2*d2/l2)
    c0 = 4*d1*d2*rate*u*u/(l1*l2*b)
    return means, c0, l1, l2


def replicate_from_stationary_clock(a1, a2, d1, d2, rate, contraction,
                                    count=180_000, jumps=48, seed=38417):
    # Conditional on the common backward Poisson clock, the two coordinates
    # are independent centered Gaussians with different random variances.
    rng = np.random.default_rng(seed)
    age = np.zeros(count, dtype=float)
    v1 = np.zeros(count, dtype=float)
    v2 = np.zeros(count, dtype=float)
    u = contraction**2
    factor = 1.
    for k in range(jumps):
        waiting = rng.exponential(1/rate, size=count)
        end = age + waiting
        v1 += (d1/a1)*factor*(np.exp(-2*a1*age)-np.exp(-2*a1*end))
        v2 += (d2/a2)*factor*(np.exp(-2*a2*age)-np.exp(-2*a2*end))
        age = end
        factor *= u
    return v1.mean(), v2.mean(), np.mean((v1-v1.mean())*(v2-v2.mean()))


def assert_approx(actual, target, relative):
    assert abs(actual-target) <= relative*max(abs(target),1e-12), (actual,target)


def checks():
    # Test moment equations for several unequal drift strengths including full reset.
    for a1,a2,d1,d2,rate,q in [
            (.7, 1.4, .8, 1.2, 2.1, 0.),
            (1.7, .9, .6, 1.4, 3.2, .45),
            (.4, 2.3, 1.5, .3, .6, .8)]:
        (m1,m2), c0, l1,l2=closed_form(a1,a2,d1,d2,rate,q)
        b=2*(a1+a2)+rate*(1-q**4)
        cross=m1*m2+c0
        assert_approx(b*cross,2*d1*m2+2*d2*m1,1e-13)
        assert_approx(l1*m1,2*d1,1e-13)
        assert_approx(l2*m2,2*d2,1e-13)
        assert c0>0
        for t in [0.03,.23,.9,2.]:
            f=c0*math.exp(-l2*t)
            back=c0*math.exp(-l1*t)
            assert_approx(f-back,c0*(math.exp(-l2*t)-math.exp(-l1*t)),1e-14)
        h=c0/(m1*m2)
        delta=l1-2*a1
        recovered_u=h*(l1+l2)/(delta*(1+h))
        recovered_q=math.sqrt(max(0,1-recovered_u))
        recovered_rate=delta/recovered_u
        assert_approx(recovered_q,q,1e-9 if q else 1e-5)
        assert_approx(recovered_rate,rate,1e-12)
        if a1!=a2:
            tstar=math.log(l1/l2)/(l1-l2)
            assert tstar>0
            vals=[abs(math.exp(-l2*t)-math.exp(-l1*t)) for t in [tstar/2,tstar,2*tstar]]
            assert vals[1]>vals[0] and vals[1]>vals[2]

    # Independent pathwise clock-mixture Monte Carlo, not using moment equations.
    a1,a2,d1,d2,rate,q=1.7,.9,.6,1.4,3.2,.45
    (m1,m2),c0,_,_=closed_form(a1,a2,d1,d2,rate,q)
    e1,e2,empirical=replicate_from_stationary_clock(a1,a2,d1,d2,rate,q)
    assert_approx(e1,m1,.012)
    assert_approx(e2,m2,.012)
    assert_approx(empirical,c0,.08)
    print('PASS: stationary moment generator, lag exponentials, shock inversion, unique peak, independent clock-mixture sampling')
    print(f'example stationary means: {m1:.9f}, {m2:.9f}')
    print(f'example connected energy covariance: {c0:.9f}; MC {empirical:.9f}')
    print(f'example forward and reverse decay rates: {2*a2+rate*(1-q*q):.9f}, {2*a1+rate*(1-q*q):.9f}')


if __name__=='__main__':
    checks()

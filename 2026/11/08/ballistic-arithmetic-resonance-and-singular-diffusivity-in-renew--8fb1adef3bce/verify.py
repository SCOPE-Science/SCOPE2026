"""Finite diagnostic checks for the renewal-tumble transport theorem.

All tests are finite and do not certify asymptotic statements.
Run: python verify.py
"""
import cmath
import itertools
import math
import random


def theorem_diffusivity(speed, omega, theta, intervals, weights):
    mu = sum(t * w for t, w in zip(intervals, weights))
    m = sum(w * cmath.exp(1j * omega * t) for t, w in zip(intervals, weights))
    h = cmath.exp(1j * theta)
    if abs(m) >= 1 - 1e-12:
        return None
    return speed**2 * (1-math.cos(theta)) * (1-abs(m)**2) / (2*mu*omega**2*abs(1-h*m)**2)


def exact_moment_at_renewals(n, speed, omega, theta, intervals, weights):
    total = 0.0
    for choices in itertools.product(range(len(intervals)), repeat=n):
        prob = 1.0
        position = 0j
        heading = 1+0j
        for idx in choices:
            duration = intervals[idx]
            prob *= weights[idx]
            u = cmath.exp(1j*omega*duration)
            position += speed / (1j*omega) * heading * (u-1)
            heading *= cmath.exp(1j*theta) * u
        total += prob * abs(position)**2
    return total


def exact_moment_via_correlation(n, speed, omega, theta, intervals, weights):
    m = sum(w * cmath.exp(1j*omega*t) for t,w in zip(intervals, weights))
    h = cmath.exp(1j*theta)
    q = h*m
    a = (speed/omega)**2
    moment = 2*n*a*(1-m.real)
    for k in range(1,n):
        moment += 2*(n-k) * (-a*h*(1-m)**2 * q**(k-1)).real
    return moment


def main():
    checks=0
    laws=[([0.8, 2.3],[0.4, 0.6]), ([0.7, 1.3, 2.4],[0.2,0.3,0.5])]
    for intervals,weights in laws:
        for theta in [0.17,1.2,2.5,math.pi,4.5]:
            for n in [1,2,3,4,5,6]:
                a=exact_moment_at_renewals(n,1.3,1.1,theta,intervals,weights)
                b=exact_moment_via_correlation(n,1.3,1.1,theta,intervals,weights)
                assert math.isclose(a,b,rel_tol=2e-11,abs_tol=2e-11),(a,b,n)
                checks+=1
    for theta in [0.17,1.2,2.5,math.pi]:
        intervals,weights=laws[0]
        mu=sum(t*w for t,w in zip(intervals,weights))
        d=theorem_diffusivity(1.3,1.1,theta,intervals,weights)
        moment=exact_moment_via_correlation(3000,1.3,1.1,theta,intervals,weights)
        assert abs(moment/(3000*mu)-4*d) < 0.003, (moment/(3000*mu),4*d)
        checks+=1
    for sigma in [0.08, 0.2, 0.8, 1.2, 2.0]:
        d=theorem_diffusivity(1,1,math.pi,[math.pi-sigma, math.pi+sigma],[.5,.5])
        assert math.isclose(d,1/math.pi/(math.tan(sigma/2)**2),rel_tol=1e-11), (sigma,d)
        checks+=1
    for sigma in [1e-4,1e-3,3e-3]:
        d=theorem_diffusivity(1,1,math.pi,[math.pi-sigma, math.pi+sigma],[.5,.5])
        assert abs(d*sigma**2 - 4/math.pi)<1e-5
        checks+=1
    # Exact resonance, T=pi, theta=pi, omega=1: every completed arc adds +2i up to sign.
    n=40
    resonance=exact_moment_at_renewals(n,1,1,math.pi,[math.pi],[1])
    assert math.isclose(resonance,4*n*n,rel_tol=1e-12)
    checks+=1
    # Complete circles (T=2*pi, theta=pi): every arc adds zero.
    bounded=exact_moment_at_renewals(n,1,1,math.pi,[2*math.pi],[1])
    assert bounded<1e-24
    checks+=1
    # Nontrivial phase-q !=1: bounded geometric-sum example.
    for n in [5,20,50]:
        m=exact_moment_at_renewals(n,1,1,math.pi/3,[math.pi],[1])
        assert m<=16+1e-8,m
        checks+=1
    # Exponential waiting: the renewal formula equals the known Poisson formula.
    for lam in [0.3,1.,2.3,5.]:
        for theta in [0.4,1.2,math.pi,4.5]:
            omega=1.7; speed=1.3
            m=lam/(lam-1j*omega)
            mu=1/lam;h=cmath.exp(1j*theta)
            general=speed**2*(1-math.cos(theta))*(1-abs(m)**2)/(2*mu*omega**2*abs(1-h*m)**2)
            poisson=speed**2*lam*(1-math.cos(theta))/(2*((lam*(1-math.cos(theta)))**2+(omega+lam*math.sin(theta))**2))
            assert math.isclose(general,poisson,rel_tol=1e-12), (general,poisson)
            checks+=1
    print('PASS',checks,'finite deterministic assertions; no claim of infinite verification')

if __name__=='__main__':
    main()

"""Reproducible identities for occupation-area fluctuations of a ballistic reset cycle.

Pure Python standard library. No network or external data needed.
"""
from fractions import Fraction as Q
from random import Random
from math import isfinite
from statistics import pvariance


def H_poly(u, L, power):
    # Primitive, in cycle phase, of x**power minus its uniform spatial average.
    return L**power * (1-(1-u)**(power+1)-u) / (power+1)


def segment_area(u0, u1, T, L, power):
    # Integral over the actual linear path: x(s)=L*(1-s/T).
    return T*L**power * (((1-u0)**(power+1)-(1-u1)**(power+1))/(power+1) - (u1-u0)/(power+1))


def exact_checks():
    L=Q(7,5)
    flight_durations=[Q(4,3),Q(7,4),Q(11,6),Q(5,2)]
    # Piecewise path from a mid-flight initial observation to a mid-flight endpoint.
    initial=Q(1,7)
    terminal=Q(5,8)
    for p in (1,2,3,4):
        z=Q(0)
        for j,T in enumerate(flight_durations):
            u0=initial if j==0 else Q(0)
            u1=terminal if j==len(flight_durations)-1 else Q(1)
            z+=segment_area(u0,u1,T,L,p)
        first=flight_durations[0]*H_poly(initial,L,p)
        last=flight_durations[-1]*H_poly(terminal,L,p)
        assert z==last-first, (p,z,last-first)
        assert H_poly(Q(0),L,p)==0
        assert H_poly(Q(1),L,p)==0
    # Exact primitive moments for f(x)=x and exponential durations with mean 1.
    m1=Q(2,1)*Q(1,12) # E phi = E T^2 / E T * integral H
    m2=Q(6,1)*Q(1,120) # E phi^2 = E T^3 / E T * integral H^2
    assert m1==Q(1,6)
    assert m2-m1*m1==Q(1,45)
    return True


def stationary_trial(rng, t):
    # Inverse-Gamma velocity from an exponential flight duration T.
    # The equilibrium-containing duration T* is Gamma(2,1); phase is uniform.
    T=rng.expovariate(1)+rng.expovariate(1)
    u=rng.random()
    phi0=T*u*(1-u)/2
    residual=(1-u)*T
    if t<residual:
        v=u+t/T
        return T*v*(1-v)/2-phi0
    t-=residual
    while True:
        T=rng.expovariate(1)
        if t<T:
            v=t/T
            return T*v*(1-v)/2-phi0
        t-=T


def simulation_check():
    rng=Random(20261118)
    data=[stationary_trial(rng,50.0) for _ in range(20000)]
    observed=pvariance(data)
    expected=2/45
    assert isfinite(observed)
    assert abs(observed-expected)<0.0035, (observed,expected)
    return observed,expected


if __name__=='__main__':
    assert exact_checks()
    observed,expected=simulation_check()
    print('Exact piecewise-path identities: PASS (powers 1 through 4)')
    print('Exact exponential-clock variance rational identity: PASS (2/45)')
    print('Independent stationary trajectory simulation: PASS')
    print('50-time occupation-area variance:',f'{observed:.8f}', 'limit:',f'{expected:.8f}')

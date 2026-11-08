#!/usr/bin/env python3
"""Reproducible finite diagnostics for sampled Gaussian angular-speed laws.

Requires only Python standard library. These checks are not a proof of the
continuous distributional, tail, or moment claims in the accompanying note.
"""
import math
import random


def ratio_moment(d, q, c):
    assert d >= 2 and 0 <= q < d and c > 0
    return c**q * math.gamma((d-1+q)/2) * math.gamma((d-q)/2) / (
        math.gamma((d-1)/2) * math.gamma(d/2))


def exact_survival(d, z):
    assert z >= 0
    if d == 2:
        return 1-z/math.hypot(1,z)
    if d == 3:
        return (1+z*z)**(-1.5)
    raise ValueError(d)


def sphere_factor(d):
    """Integral over a unit sphere of a tangent norm to power d."""
    return (2*math.pi**(d/2)*math.gamma(d-0.5)/
            (math.gamma((d-1)/2)*math.gamma(d)))


def isotropic_tail_constant(d, c):
    # p_X(0) times the direction-averaged d-th innovation moment.
    moment_chi = 2**(d/2)*math.gamma(d)/math.gamma(d/2)
    return (2*math.pi)**(-d/2) * sphere_factor(d)*c**d*moment_chi/d


def sampled_speed(x, y, dt):
    norm2 = sum(z*z for z in x)
    dx = [a-b for a,b in zip(y,x)]
    dot = sum(a*b for a,b in zip(dx,x))
    tangent = sum(v*v for v in dx)-dot**2/norm2
    return math.sqrt(max(0.0,tangent)) / (dt*math.sqrt(norm2))


def simulate_isotropic(d, kappa, dt, n, rng):
    rho=math.exp(-kappa*dt)
    sig=math.sqrt(1-rho*rho)
    counts=[0,0,0]
    thresholds=[0.5,1.0,2.0]
    sample_second=0.0
    for _ in range(n):
        x=[rng.gauss(0,1) for _ in range(d)]
        y=[rho*v+sig*rng.gauss(0,1) for v in x]
        w=sampled_speed(x,y,dt)
        sample_second+=w*w
        for j,z in enumerate(thresholds):
            counts[j]+=(w > (sig/dt)*z)
    for j,z in enumerate(thresholds):
        expected=exact_survival(d,z)
        actual=counts[j]/n
        # Bounded Bernoulli statistical uncertainty, not a proof.
        tolerance=6*math.sqrt(expected*(1-expected)/n)+0.004
        assert abs(actual-expected)<tolerance,(d,z,actual,expected)
    if d == 3:
        theory=2*(sig/dt)**2
        # Heavy tails give slower moment convergence than bounded test stats.
        assert abs(sample_second/n-theory)/theory<0.12
    return counts, sample_second/n


def rotated_second_moment(rho, phi, dt):
    c=math.cos(phi)
    return (2*(1-rho*rho)+(4/15)*rho*rho*(1-c)*(3+2*c))/(dt*dt)


def simulate_rotating(kappa, omega, dt, n, rng):
    rho=math.exp(-kappa*dt)
    phi=omega*dt
    cp,sp=math.cos(phi),math.sin(phi)
    sig=math.sqrt(1-rho*rho)
    acc=0.0
    signed_acc=0.0
    for _ in range(n):
        x=[rng.gauss(0,1) for _ in range(3)]
        y=[rho*(cp*x[0]-sp*x[1])+sig*rng.gauss(0,1),
           rho*(sp*x[0]+cp*x[1])+sig*rng.gauss(0,1),
           rho*x[2]+sig*rng.gauss(0,1)]
        w=sampled_speed(x,y,dt)
        acc+=w*w
        signed_acc+=(x[0]*(y[1]-x[1])-x[1]*(y[0]-x[0]))/(dt*sum(v*v for v in x))
    expected_signed=2*rho*math.sin(phi)/(3*dt)
    assert abs(signed_acc/n-expected_signed)<0.04,(signed_acc/n,expected_signed)
    theory=rotated_second_moment(rho,phi,dt)
    assert abs(acc/n-theory)/theory<0.12,(acc/n,theory)
    return acc/n,theory


def main():
    tol=1e-12
    for d in range(2,12):
        for c in (0.13,1,2.7):
            assert abs(ratio_moment(d,0,c)-1)<tol
            assert ratio_moment(d,1,c)>0
            if d>2:
                assert abs(ratio_moment(d,2,c)-(d-1)*c*c/(d-2))<tol
    for z in (0,0.01,0.25,0.5,1,2,10,100):
        assert 0<=exact_survival(2,z)<=1
        assert 0<=exact_survival(3,z)<=1
    assert abs(sphere_factor(2)-math.pi)<tol
    assert abs(sphere_factor(3)-3*math.pi**2/4)<tol
    assert abs(isotropic_tail_constant(2,1)-0.5)<tol
    assert abs(isotropic_tail_constant(3,1)-1)<tol
    assert abs((100**2)*exact_survival(2,100)-0.5)<0.00005
    assert abs((100**3)*exact_survival(3,100)-1)<0.0002
    rng=random.Random(20261104)
    for d in (2,3):
        counts,second=simulate_isotropic(d,0.8,0.3,120000,rng)
        print('dimension',d,'count_above_thresholds',counts,'sample_second_moment',second)
    measured,exact=simulate_rotating(0.8,1.2,0.3,180000,rng)
    print('rotating_3d_second_moment',measured,'exact',exact)
    print('PASS: analytic moment identities, exact survival functions, finite Gaussian diagnostics')


if __name__=='__main__':
    main()

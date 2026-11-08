#!/usr/bin/env python3
"""Independent analytic-integral and sampled-geodesic checks for a spherical zone."""
from math import acos, asin, atan2, cos, pi, sin, sqrt
from random import Random


def proposed(theta):
    c = cos(theta)
    return c / (2.0 * (1.0 + c))


def quadrature(theta, subdivisions=16000):
    assert subdivisions % 2 == 0
    s = sin(theta)
    extent = pi / 2 - theta
    def integrand(u):
        inc = theta + extent * u*u
        ratio = min(1.0, s / sin(inc))
        length = 2 * asin(ratio)
        return sin(inc) * (length - sin(length)) * 2 * extent * u
    h = 1/subdivisions
    total = integrand(0.0) + integrand(1.0)
    for k in range(1, subdivisions):
        total += (4 if k%2 else 2) * integrand(k*h)
    return (total*h/3) / (2*pi*s*s)


def sample(theta, n=110000, seed=13):
    rng=Random(seed)
    s=sin(theta)
    hits=0
    for i in range(n):
        z1,z2=rng.uniform(-s,s),rng.uniform(-s,s)
        a,b=2*pi*rng.random(),2*pi*rng.random()
        r1,r2=sqrt(1-z1*z1),sqrt(1-z2*z2)
        dot=r1*r2*cos(a-b)+z1*z2
        d=acos(max(-1.0,min(1.0,dot)))
        sd=sin(d)
        if sd<1e-14: continue
        A=z1
        B=(z2-z1*cos(d))/sd
        zmax=max(abs(z1),abs(z2))
        t0=atan2(B,A)
        for k in range(-2,3):
            t=t0+k*pi
            if 0<t<d:
                zmax=max(zmax, abs(A*cos(t)+B*sin(t)))
        if zmax>s+1e-12: hits+=1
    return hits/n


def main():
    for t in (0.08,0.27,0.6,1.0,1.38):
        expected=proposed(t)
        value=quadrature(t)
        print('quadrature theta=%.3f expected=%.12f actual=%.12f error=%.3g' % (t,expected,value,abs(value-expected)))
        assert abs(expected-value)<2e-8
    for j,t in enumerate((0.13,0.64,1.23)):
        expected=proposed(t)
        actual=sample(t, seed=20261105+j)
        se=sqrt(expected*(1-expected)/110000)
        print('Monte Carlo theta=%.3f expected=%.6f observed=%.6f s.e.=%.5f' % (t,expected,actual,se))
        assert abs(expected-actual)<7*se+0.001
    print('SPHERICAL_ZONE_GEODESIC_ESCAPE_ANALYTIC_AND_DIRECT_SAMPLE_OK')

if __name__=='__main__':
    main()

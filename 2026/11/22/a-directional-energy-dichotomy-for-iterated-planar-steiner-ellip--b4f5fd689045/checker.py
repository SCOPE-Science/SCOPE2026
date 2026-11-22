"""Sanity checks for a deterministic planar Steiner ellipse recurrence.

A proof for all ellipses and infinite direction sequences is in RESULT.md.
"""
import math
import random


def direct_step(a, b, c, theta):
    co, si = math.cos(theta), math.sin(theta)
    half_width_squared = a*co*co + 2*b*co*si + c*si*si
    determinant = a*c - b*b
    transverse = determinant/half_width_squared
    aa = half_width_squared*co*co + transverse*si*si
    bb = (half_width_squared-transverse)*co*si
    cc = half_width_squared*si*si + transverse*co*co
    return aa, bb, cc, half_width_squared


def scalar_step(u, delta):
    C = math.cos(2*delta)
    return u*(u+C)/(1+u*C)


def main():
    generator = random.Random(20261118)
    for _ in range(15000):
        eig0 = math.exp(generator.uniform(-2,2))
        eig1 = math.exp(generator.uniform(-2,2))
        theta0 = generator.uniform(-3,3)
        theta = generator.uniform(-3,3)
        c0, s0 = math.cos(theta0),math.sin(theta0)
        a = eig0*c0*c0 + eig1*s0*s0
        b = (eig0-eig1)*c0*s0
        c = eig0*s0*s0 + eig1*c0*c0
        D = a*c - b*b
        aa, bb, cc, x = direct_step(a,b,c,theta)
        u0 = (eig0/math.sqrt(D)-1)/(eig0/math.sqrt(D)+1)
        u1 = (x/math.sqrt(D)-1)/(x/math.sqrt(D)+1)
        assert abs(u1-scalar_step(u0,theta-theta0))<2e-12
        assert abs(aa*cc-bb*bb-D)<1e-10
        if abs(u0)>1e-6:
            C=math.cos(2*(theta-theta0))
            energy=math.sin(2*(theta-theta0))**2
            assert abs(1-(u1/u0)**2-(1-u0*u0)*energy/(1+u0*C)**2)<1e-10

    for initial in (0.01,0.1,0.4,0.8):
        u=initial
        for k in range(1,13):
            u=scalar_step(u,math.pi/4)
            assert abs(u-initial**(2**k))<1e-10

    for initial in (0.1,0.3,0.7):
        u=initial
        cumulative=0.0
        for j in range(2,10001):
            delta=1/j
            u=scalar_step(u,delta)
            cumulative+=math.sin(2*delta)**2
            assert u>0
            exponent=-(1-initial)/(2*(1+initial))*cumulative
            assert u<=initial*math.exp(exponent)+1e-13
        print('harmonic increments:',initial,'truncated anisotropy:',round(u,12))
    print('PASS: 15000 independent matrix tests, 48 quarter-turn checks, 29997 energy checks')


if __name__ == '__main__':
    main()

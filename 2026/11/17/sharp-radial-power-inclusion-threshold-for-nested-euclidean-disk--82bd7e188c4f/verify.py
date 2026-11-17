"""Numerical diagnostics for fractional radial boundary moments on nested disks.

Analytic proof is self-contained in RESULT.md; these checks are finite sanity tests.
"""
import math
import random

def mean_power(p, t, samples=8192):
    # Midpoint periodic quadrature; no numerical differentiation here.
    total = deriv = inv = 0.0
    for j in range(samples):
        phi = 2.0 * math.pi * (j + 0.5) / samples
        c = math.cos(phi)
        x = 1.0 + t*t + 2.0*t*c
        total += x**(p/2.0)
        if x > 0:
            deriv += p*(t+c)*x**(p/2.0-1.0)
            inv += x**(p/2.0-1.0)
    fac = 2.0*math.pi/samples
    return total*fac, deriv*fac, inv*fac

def weighted(p, center, radius, samples=4096):
    return radius**(p+1) * mean_power(p, math.hypot(*center)/radius, samples)[0]

def run():
    checks = 0
    for p in (0.05, 0.2, 0.5, 0.8, 0.99):
        for t in (0.001, .1, .3, .5, .8, .95, .99, 1.01, 1.05, 1.2, 2.0, 4.0, 10.0):
            I,Ip,B=mean_power(p,t,16384)
            J=(p+1)*I-(t+1)*Ip
            assert J > 1e-7, (p,t,J)
            checks += 1
            if t<1:
                assert Ip>=0, (p,t,Ip)
                assert Ip <= (p*t/(1+t*t))*I + 2e-4, (p,t,Ip)
                assert J >= I-2e-4, (p,t,J,I)
                checks += 3
    rng=random.Random(20261110)
    for _ in range(420):
        p=rng.uniform(.03,.97)
        radius=10**rng.uniform(-1,1)
        center=(rng.uniform(-3,3),rng.uniform(-3,3))
        grow=radius*rng.uniform(.08,1.0)
        dirangle=rng.uniform(0,2*math.pi)
        shift=grow*rng.uniform(0,.98)
        bigcenter=(center[0]+shift*math.cos(dirangle),center[1]+shift*math.sin(dirangle))
        small=weighted(p,center,radius,2048)
        large=weighted(p,bigcenter,radius+grow,2048)
        assert large>small*(1+1e-7),(p,center,radius,bigcenter,grow,small,large)
        checks+=1
    # Negative exponents are not part of the new theorem: check familiar failure near the origin.
    for p in (-.25,-.5,-.8):
        t=.9999
        I,Ip,B=mean_power(p,t,65536)
        # For these p and t, a disk expansion with inward center shift can decrease the moment.
        assert (p+1)*I-(t+1)*Ip < 0,(p,I,Ip)
        checks+=1
    print('PASS',checks,'analytic-inequality and independent nested-disk diagnostics')
if __name__=='__main__':run()

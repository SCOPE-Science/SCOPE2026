#!/usr/bin/env python3
"""Independent finite tests of explicit alternating-cell and period identities.
Analytical density and all-angle statements require the proof in RESULT.md.
"""
import cmath
import math
import random
from fractions import Fraction

RNG = random.Random(30629)


def iterate(lam, z):
    return lam * (z - (1 if z.imag >= 0 else -1))


def order_minus_lambda(p, q):
    return 2*q // math.gcd(2*p+q, 2*q)


def in_rational_cell(lam, s, w, n, tol=1e-10):
    return all(s + ((-lam)**k * w).imag > tol for k in range(n))


def check_rational(p, q):
    alpha = 2*math.pi*p/q
    lam = cmath.exp(1j*alpha)
    c = lam/(1+lam)
    s = c.imag
    n = order_minus_lambda(p,q)
    assert s > 0 and n >= 3
    assert n == (2*q if q % 2 else (q if q % 4 == 0 else q//2))
    assert abs(iterate(lam,c)+c)<1e-12
    assert abs(iterate(lam,-c)-c)<1e-12
    count = 0
    for _ in range(200):
        angle = RNG.uniform(0,2*math.pi)
        rad = RNG.uniform(0,1.45*s)
        w = rad*cmath.exp(1j*angle)
        predicted = in_rational_cell(lam,s,w,n)
        z = c+w
        for k in range(2*n+1):
            if (1 if k%2 == 0 else -1)*z.imag <= 1e-9:
                break
            z=iterate(lam,z)
        else:
            assert predicted, (p,q,w,'extra itinerary')
            count+=1
            continue
        assert not predicted, (p,q,w,'false positive')
    # Period and exact rotational return on an off-center interior point.
    z = c + 0.13*s
    assert in_rational_cell(lam,s,z-c,n)
    period = 2*q // math.gcd(q,2)
    orbit=[z]
    for k in range(1,period+1):
        z=iterate(lam,z)
        if k < period:
            assert abs(z-orbit[0])>1e-8,(p,q,k)
    assert abs(z-orbit[0])<1e-8,(p,q,'return')
    # Area identity: polygon formula computed from side lengths vs support-distance.
    side=2*s*math.tan(math.pi/n)
    area_per_cell=n*side*s/2
    assert abs(area_per_cell-n*s*s*math.tan(math.pi/n))<1e-12
    return count


def check_irrational():
    theta = (math.sqrt(5)-1)/4
    alpha=2*math.pi*theta
    lam=cmath.exp(1j*alpha)
    c=lam/(1+lam)
    s=c.imag
    n_inside=n_outside=0
    for _ in range(400):
        angle=RNG.uniform(0,2*math.pi)
        r=RNG.uniform(0.01,0.9)*s if _%2 else RNG.uniform(1.1,1.7)*s
        z=c+r*cmath.exp(1j*angle)
        should_stay=r<s
        alternating=True
        for k in range(2200):
            if (1 if k%2==0 else -1)*z.imag <= 1e-9:
                alternating=False
                break
            z=iterate(lam,z)
        assert alternating==should_stay,(r,s,angle,alternating)
        n_inside+=int(should_stay)
        n_outside+=int(not should_stay)
    assert n_inside==200 and n_outside==200


def run():
    samples=0
    cases=0
    for q in range(3,32):
        for p in range(1,(q+1)//2):
            if 2*p<q and math.gcd(p,q)==1:
                samples+=check_rational(p,q)
                cases+=1
    check_irrational()
    print('ALTERNATING_ISLAND_CHECK_OK rational_angles=%d rational_interior_samples=%d irrational_samples=400'%(cases,samples))

if __name__=='__main__':
    run()

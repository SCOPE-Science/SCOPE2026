#!/usr/bin/env python3
"""Standalone elementary checks for the axis-intercept simplex angle/fullness theorem."""
import math
import random


def simpson(f, lo, hi, n=20000):
    assert n % 2 == 0
    step = (hi-lo)/n
    total = f(lo)+f(hi)
    for j in range(1,n):
        total += (4 if j%2 else 2)*f(lo+j*step)
    return total*step/3


def sharp_constant(d):
    return d*(d-1)*2**(d/2)*simpson(
        lambda t: (1-t)**(d-2)/(1+t*t)**(d/2),0.0,1.0,12000)


def tetra_solid_angle_at_leg(legs,i):
    a=legs[i]
    b,c=(legs[j] for j in range(3) if j!=i)
    p=math.hypot(a,b)
    q=math.hypot(a,c)
    return 2*math.atan2(b*c,p*q+a*(p+q)+a*a)


def tetra_ratio(legs):
    a,b,c=legs
    diameter=max(math.hypot(a,b),math.hypot(a,c),math.hypot(b,c))
    fullness=a*b*c/(6*diameter**3)
    angles=[tetra_solid_angle_at_leg(legs,i) for i in range(3)]
    # At the orthogonal corner the solid angle is pi/2.
    return min(math.pi/2,*angles)/fullness, angles


def main():
    assert abs(sharp_constant(2)-math.pi)<2e-12
    C3_exact=24-12*math.sqrt(2)
    assert abs(sharp_constant(3)-C3_exact)<2e-12
    counts=0
    rng=random.Random(718262)
    for _ in range(2400):
        legs=[math.exp(rng.uniform(-5,5)) for _ in range(3)]
        R,angles=tetra_ratio(legs)
        assert 3<R<C3_exact, (legs,R)
        largest=max(legs)
        assert all(angles[i]<=angles[j]+1e-12 for i in range(3)
                   for j in range(3) if legs[i]==largest)
        for i in range(3):
            for j in range(3):
                if legs[i]>legs[j]:
                    assert angles[i]<angles[j]+1e-13,(legs,angles)
        counts+=1
    for eps in (1e-2,1e-4,1e-6):
        low,_=tetra_ratio([1,eps,eps])
        high,_=tetra_ratio([1,1,eps])
        assert abs(low-3)<0.1 if eps==1e-2 else abs(low-3)<0.001
        assert abs(high-C3_exact)<0.1 if eps==1e-2 else abs(high-C3_exact)<0.001
        counts+=2
    for d in range(2,11):
        cd=sharp_constant(d)
        assert cd>d
        counts+=1
    print(f'RIGHT_SIMPLEX_SHARP_ANGLE_FULLNESS_OK {counts} comparisons')
    print('C2=',format(sharp_constant(2),'.12f'))
    print('C3=',format(C3_exact,'.12f'))
    print('C4=',format(sharp_constant(4),'.12f'))

if __name__=='__main__':
    main()

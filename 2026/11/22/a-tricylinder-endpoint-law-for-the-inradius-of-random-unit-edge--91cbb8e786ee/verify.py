#!/usr/bin/env python3
"""Reproduce geometric and finite-sample consistency checks for the inradius endpoint law.

Python standard library only. Stochastic checks are diagnostics, not proof.
"""
import math
import random


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def norm(x):
    return math.sqrt(dot(x,x))


def random_unit(rng):
    v = tuple(rng.gauss(0,1) for _ in range(3))
    n = norm(v)
    return tuple(w/n for w in v)


def inradius_direct(u,v,w):
    determinant = abs(dot(u,cross(v,w)))
    face_areas = (norm(cross(v,w)),norm(cross(w,u)),norm(cross(u,v)))
    return 0.5*determinant/max(face_areas)


def inradius_gram(a,b,c):
    determinant = 1-a*a-b*b-c*c+2*a*b*c
    return 0.5*math.sqrt(max(0.0,determinant)/(1-min(a*a,b*b,c*c)))


def cylinder_volume_simpson(m=10000):
    # 48 ordered, signed wedges; radial integration gives 16*int_0^(pi/4) sin(theta) dtheta.
    assert m%2==0
    h=math.pi/(4*m)
    ss=math.sin(0)+math.sin(math.pi/4)
    for i in range(1,m):
        ss+=(4 if i%2 else 2)*math.sin(i*h)
    return 16*h*ss/3


def main():
    volume=8*(2-math.sqrt(2))
    constant=2*volume/math.pi
    assert abs(cylinder_volume_simpson()-volume)<1e-11
    assert abs(constant-2.9833858286244523)<1e-12

    rng=random.Random(20261121)
    for _ in range(2000):
        u,v,w=[random_unit(rng) for _ in range(3)]
        a,b,c=dot(u,v),dot(u,w),dot(v,w)
        assert abs(inradius_direct(u,v,w)-inradius_gram(a,b,c))<2e-12

    # Independent spherical-coordinate construction: a,b uniform [-1,1], phi uniform [0,2pi].
    rng=random.Random(841237)
    count=[0,0,0]
    thresholds=(0.04,0.02,0.01)
    n=1500000
    beta_below=0
    for _ in range(n):
        a=2*rng.random()-1
        b=2*rng.random()-1
        phi=2*math.pi*rng.random()
        c=a*b+math.sqrt((1-a*a)*(1-b*b))*math.cos(phi)
        radius=inradius_gram(a,b,c)
        for i,e in enumerate(thresholds):
            if radius>0.5-e:
                count[i]+=1
        if radius>0.5-thresholds[1]/2:
            beta_below+=1
    for e,k in zip(thresholds,count):
        empirical=k/n
        predicted=constant*e**1.5
        print('epsilon',e,'empirical',f'{empirical:.9g}', 'asymptotic',f'{predicted:.9g}', 'ratio',f'{empirical/predicted:.6f}')
        assert abs(empirical/predicted-1)<0.055
    # Threshold ratio: conditional deficit / epsilon tends to Beta(3/2,1).
    beta_empirical=beta_below/count[1]
    print('conditional deficit half-threshold',beta_empirical,'limit',2**(-1.5))
    assert abs(beta_empirical-2**(-1.5))<0.04
    print('tricylinder_volume',format(volume,'.16g'))
    print('tail_constant',format(constant,'.16g'))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()

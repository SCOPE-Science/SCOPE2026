#!/usr/bin/env python3
"""Independent endpoint sampling and numerical checks of the marked flat-band law."""
import math, random

def product_cdf(t):
    if t <= 0: return 0.
    if t >= 1: return 1.
    return t * (1. - math.log(t))

def H(t):
    if t <= 0: return 0.
    if t >= 1: return t - 0.25
    return t * t * (0.75 - 0.5 * math.log(t))

def crossing_probability(r):
    return 0.5 * r*r * H(1./(r*r))

def survival(r,z):
    if z <= 0: return 1.
    if z >= 1: return 0.
    return H((1.-z)/(r*r))/H(1./(r*r))

def density(r,z):
    return product_cdf((1.-z)/(r*r))/(r*r*H(1./(r*r)))

def run():
    rng=random.Random(919203)
    n=160000
    trials=0
    for r in (0.2,0.65,1.,1.5,3.4):
        crossing=0
        survivors=[0,0,0]
        for _ in range(n):
            x1,x2=rng.random(),rng.random()
            y1,y2=r*(rng.random()-.5),r*(rng.random()-.5)
            d=abs(x1-x2)
            even = d*d+(y1-y2)**2
            odd = (1.-d)**2+(y1+y2)**2
            if even<odd:
                hit = y1*y2<0
                ell=d
            else:
                hit = y1*y2>0
                ell=1.-d
            if hit:
                crossing+=1
                z=2.*ell
                assert -1.e-12<z<1.+1.e-12
                for j,t in enumerate((0.25,0.5,0.75)):
                    survivors[j]+=z>t
        difference=abs(crossing/n-crossing_probability(r))
        assert difference<0.009, (r,'crossing frequency',difference)
        for j,t in enumerate((0.25,0.5,0.75)):
            err=abs(survivors[j]/crossing-survival(r,t))
            assert err<0.017,(r,t,err)
        print('aspect',r,'crossing',round(crossing/n,5),'exact',round(crossing_probability(r),5),'n',n)
        trials+=n
    for r in (.14,.61,1.,2.,5.):
        dz=1./700
        integral=sum(density(r,(k+.5)*dz)*dz for k in range(700))
        assert abs(integral-1)<0.001,(r,integral)
    for r1,r2 in ((.1,.2),(.3,.8),(.8,1.),(1.,2.),(2.,7.)):
        ratios=[density(r2,(k+.5)/700)/density(r1,(k+.5)/700) for k in range(700)]
        assert all(ratios[i+1]<=ratios[i]+2.e-11 for i in range(699))
        assert ratios[-1]<ratios[0]
        for z in (.05,.25,.55,.8,.95):
            assert survival(r2,z)<survival(r1,z)
    for z in (.14,.35,.67):
        assert abs(survival(.00001,z)-(1-z))<1.e-6
        assert abs(survival(100000.,z)-(1-z)**2)<0.03
    print('MOBIUS_MARKED_CHECKS_OK',trials)

if __name__ == '__main__': run()

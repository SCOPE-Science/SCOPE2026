#!/usr/bin/env python3
"""Independent numerical consistency checks for exact circular-cap depth law.
Only finite checks; universal statements follow from the mathematical proof.
"""
from math import pi, sin, cos, tan, acos, sqrt, isclose


def simpson(f, lo, hi, n=2000):
    assert n % 2 == 0
    step = (hi-lo)/n
    return step/3 * (f(lo) + f(hi) + 4*sum(f(lo+(2*j+1)*step) for j in range(n//2)) + 2*sum(f(lo+2*j*step) for j in range(1,n//2)))


def cap(q):
    return (acos(q)-q*sqrt(max(0.0,1-q*q)))/pi


def cdf_formula(m,q):
    a=pi/m
    if q>=cos(a):
        return m*cap(q)
    return 1-q*q*tan(a)/a


def cdf_by_radial_integral(m,q):
    a=pi/m
    return simpson(lambda eps:1-(q/cos(eps))**2,0,min(a,acos(q)))/a


def mean_formula(m):
    a=pi/m
    return a/(2*pi)+((pi/2-a)*tan(a)-sin(a)**2)/(4*pi*a)


def mean_by_direct_integration(m):
    a=pi/m
    # Independent angular/radial integration, no use of the CDF formula.
    return simpson(lambda e:simpson(lambda r:2*r*cap(r*cos(e)),0,1,400),0,a,160)/a


def cap_weighted(q,alpha):
    # The normalized density on unit disk is (1+alpha*r^2)/(pi*(1+alpha/2)).
    d=pi*(1+alpha/2)
    return simpson(lambda theta:2*sin(theta)**2*(1+alpha*cos(theta)**2+alpha*sin(theta)**2/3)/d,0,acos(q),1200)


def union_weighted(m,q,alpha):
    a=pi/m
    d=pi*(1+alpha/2)
    def sector(e):
        r=min(1.,q/cos(e))
        return (1-r*r)/2+alpha*(1-r**4)/4
    return 2*m*simpson(sector,0,min(a,acos(q)),1200)/d


def run():
    checks=0
    for m in (3,4,5,6,8,12,30):
        a=pi/m
        for ratio in (0.05,0.2,0.5,0.8,0.99,1.,1.01,1.1,1.2):
            q=min(0.99999,cos(a)*ratio)
            observed=cdf_by_radial_integral(m,q)
            predicted=cdf_formula(m,q)
            assert abs(observed-predicted)<2e-8,(m,q,observed,predicted)
            checks+=1
        exact=mean_formula(m)
        numeric=mean_by_direct_integration(m)
        assert abs(exact-numeric)<4e-9,(m,exact,numeric)
        checks+=1
        q0=cos(a)
        assert abs(cdf_formula(m,q0)-m*cap(q0))<1e-12
        checks+=1
    # Verify the density-independent linear tail and strict post-contact loss
    # using nonconstant radial densities, separately integrating projected caps.
    for m in (3,5,8):
        a=pi/m
        for alpha in (0.,1.,3.):
            for ratio in (0.75,0.95,1.05,1.25):
                q=min(0.99999,cos(a)*ratio)
                mass=cap_weighted(q,alpha)
                union=union_weighted(m,q,alpha)
                if ratio>=1:
                    assert abs(union-m*mass)<3e-8,(m,alpha,q,union,m*mass)
                else:
                    assert union<m*mass-1e-6,(m,alpha,q,union,m*mass)
                checks+=1
    target=pi*pi/24
    for m in (120,300,600):
        ans=(mean_formula(m)-1/8)*m*m
        assert abs(ans-target)<0.01,(m,ans,target)
        checks+=1
    print('PASS:',checks,'independent integration/threshold/mean checks')
    print('mean example m=4:',mean_formula(4))
    print('sharp mean rate:',target)

if __name__=='__main__':run()

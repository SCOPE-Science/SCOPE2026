#!/usr/bin/env python3
"""Independent reproducibility checks for the odd regular-bipyramid silhouette law.
Requires only the Python standard library. Run: python verify_odd_bipyramid.py.
Numerical tests corroborate, but do not replace, the analytic proof.
"""
import math
import random

PI=math.pi

def exact_probability(n, height):
    assert n>=5 and n%2==1 and height>0
    delta=PI/n
    c=math.cos(delta)
    t=height/math.hypot(height,c)
    return (2*n/PI)*(2*math.asin(t*math.sin(delta))
           -math.asin(t*math.sin(delta/2))
           -math.asin(t*math.sin(3*delta/2)))

def radial_probability(n,height):
    # Independent sector quadrature from the two-apex one-edge visibility test.
    d=PI/n;c=math.cos(d)
    def f(alpha):
        l=max(alpha,d-alpha)
        u=min(2*d-alpha,d+alpha)
        return height*(1/math.hypot(height,c/math.cos(l))
             -1/math.hypot(height,c/math.cos(u)))
    panels=2000; dx=d/panels
    return n/PI*(dx/3)*(f(0)+f(d)+4*sum(f(j*dx) for j in range(1,panels,2))+
        2*sum(f(j*dx) for j in range(2,panels,2)))

def hull_size(points):
    p=sorted(set(points))
    def cross(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]
    for x in p:
        while len(lo)>1 and cross(lo[-2],lo[-1],x)<=1e-11:lo.pop()
        lo.append(x)
    up=[]
    for x in reversed(p):
        while len(up)>1 and cross(up[-2],up[-1],x)<=1e-11:up.pop()
        up.append(x)
    return len(lo[:-1]+up[:-1])

def predicate(n,b):
    delta=PI/n;c=math.cos(delta)
    v=[(math.cos(2*PI*j/n), math.sin(2*PI*j/n)) for j in range(n)]
    k=sum(b[0]*x+b[1]*y>c+1e-12 for x,y in v)
    l=sum(-b[0]*x-b[1]*y>c+1e-12 for x,y in v)
    return k==l==1

def sample_b(height,rng):
    theta=2*PI*rng.random(); w=rng.random()
    r=height*math.sqrt((1-w)**(-2)-1)
    return (r*math.cos(theta),r*math.sin(theta))

def main():
    for n in (5,7,11):
        for h in (.35,.75,1.7):
            p=exact_probability(n,h)
            q=radial_probability(n,h)
            assert 0<p<1,(n,h,p)
            assert abs(p-q)<2e-11,(n,h,p,q)
    rng=random.Random(20261101)
    for n in (5,7,11):
        base=[(math.cos(2*PI*j/n), math.sin(2*PI*j/n)) for j in range(n)]
        for h in (.35,.75,1.7):
            for k in range(1800):
                b=sample_b(h,rng)
                actual=hull_size(base+[b,(-b[0],-b[1])])==n+2
                assert actual==predicate(n,b),(n,h,k,b,actual)
    for n in (5,7,11):
        h=.75; N=120000
        observed=sum(predicate(n,sample_b(h,rng)) for _ in range(N))/N
        exact=exact_probability(n,h)
        assert abs(observed-exact)<.009,(n,observed,exact)
        print('n=%d, h=%.2f, exact=%.10f, sampled=%.10f' % (n,h,exact,observed))
    h=1/math.sqrt(2)
    target=PI**2/(3*math.sqrt(3))
    assert abs(401**2*exact_probability(401,h)-target)<.0003
    for n in (5,7,11,31,101):
        c=math.cos(PI/n);delta=PI/n
        lower=c/(math.sqrt(2)*math.cos(delta/2))
        upper=c/(math.sqrt(2)*math.cos(3*delta/2))
        grid=[.015+i*.004 for i in range(650)]
        best=grid[max(range(len(grid)),key=lambda k:exact_probability(n,grid[k]))]
        assert lower<=best<=upper,(n,best,lower,upper)
    print('ALL_ODD_BIPYRAMID_SILHOUETTE_CHECKS_PASSED')

if __name__=='__main__':main()

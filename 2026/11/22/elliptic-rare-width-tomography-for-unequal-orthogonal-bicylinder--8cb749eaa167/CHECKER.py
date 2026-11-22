"""Standalone numerical diagnostics of angular-width asymptotics for crossed circular cylinders.
Run with Python 3 (standard library only). Numerical diagnostics are not a proof.
"""
from math import pi, sin, cos, sqrt, log, asin, isclose

def support(a,b,s,theta,iterations=85):
    # Reduction to a one-dimensional concave maximum over the first cylinder's disk.
    p=sqrt(max(0.0,1-s*s))
    co=abs(cos(theta)); si=sin(theta)
    def f(y):
        return p*(co*sqrt(max(0.0,a*a-y*y))+si*y)+abs(s)*sqrt(b*b-y*y)
    lo,hi=-a,a
    # Golden-section maximum (includes endpoint cases explicitly).
    g=(sqrt(5)-1)/2
    c=hi-g*(hi-lo);d=lo+g*(hi-lo)
    fc=f(c);fd=f(d)
    for j in range(iterations):
        if fc>fd:
            hi=d; d=c; fd=fc; c=hi-g*(hi-lo); fc=f(c)
        else:
            lo=c; c=d; fc=fd; d=lo+g*(hi-lo); fd=f(d)
    return max(f(lo),f(hi),f(-a),f(a),fc,fd)

def K_mod(k,n=16000):
    # Simpson integration for complete elliptic K in modulus convention.
    h=(pi/2)/n
    def f(t):return 1/sqrt(1-k*k*sin(t)**2)
    sm=f(0)+f(pi/2)
    for i in range(1,n):sm+=(4 if i%2 else 2)*f(i*h)
    return sm*h/3

def exact_cdf(a,b,eps,ang_count=100):
    # For each azimuth solve the exact support threshold, then integrate over
    # its uniform vertical spherical coordinate; uses midpoint angular rule.
    sm=0.0
    for j in range(ang_count):
        theta=2*pi*(j+0.5)/ang_count
        lo,hi=0.0,min(0.9,4*eps/sqrt(b*b-a*a))
        while support(a,b,hi,theta)<a+eps/2:
            hi=min(1.0,hi*1.5)
            if hi==1:break
        for _ in range(34):
            mid=(lo+hi)/2
            if support(a,b,mid,theta)<=a+eps/2:lo=mid
            else:hi=mid
        sm+=(lo+hi)/2
    return sm/ang_count

def equal_cdf(a,eps,n=30000):
    # At a=b, condition |U_x U_z| < eps/(2a) + eps^2/(8a^2).
    d=eps/(2*a)+eps*eps/(8*a*a)
    h=1/n
    def f(y):
        return 2/pi*asin(min(1.0,2*d/(1-y*y))) if y<1 else 1.0
    sm=f(0)+f(1)
    for i in range(1,n):sm+=(4 if i%2 else 2)*f(i*h)
    return sm*h/3

def run():
    total=0
    for a,b in [(1.,1.25),(.8,2.),(1.,1.03),(2.,3.)]:
        coefficient=K_mod(a/b)/(pi*b)
        assert coefficient>0
        for eps in [.025,.012,.006]:
            p=exact_cdf(a,b,eps,ang_count=84)
            ratio=p/(coefficient*eps)
            print('a,b,eps,ratio',a,b,eps,ratio)
            # Finite-epsilon effects near equal radii can be larger, so the tolerance
            # deliberately only tests convergence scale and basic normalization.
            assert 0.70<ratio<1.14,(a,b,eps,ratio)
            total+=1
        assert K_mod(a/b)>pi/2
        total+=1
    for eps in [.015,.007,.003]:
        p=equal_cdf(1.,eps)
        r=p/(eps/pi*log(1/eps))
        print('equal eps,ratio',eps,r)
        assert 1.0<r<2.0
        total+=1
    for k in range(1,35):
        t=2*pi*k/36
        for s in [.001,.005,.02]:
            a,b=1,1.8
            h=support(a,b,s,t)
            approx=a+s*sqrt(b*b-a*a*sin(t)**2)
            assert abs(h-approx)<3*s*s+2e-8
            total+=1
    print('passed',total,'diagnostic assertions')
if __name__=='__main__':run()

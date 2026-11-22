"""Reproducibility checks for cone intrinsic/chord distortion; standard Python only.
No network, external data, or package dependencies.
"""
from math import sin,cos,pi,sqrt,log,asinh,exp,expm1
import random

def k(q):
    return sin(pi*q/2)/q

def leading(q):
    S=sin(pi*q/2)
    C=cos(pi*q/2)
    return 16*sqrt(2*q**3*S)/(3*pi*C*sqrt(S*S-q*q))

def f(q,lam,delta):
    return sin(q*delta/2)**2-lam**2*q*q*sin(delta/2)**2

def quadrature_tail(q,lam,n=12000):
    if lam<=1: return 1.
    if lam>=k(q):return 0.
    lo=0.0;hi=pi
    for _ in range(65):
        mid=(lo+hi)/2
        if f(q,lam,mid)>0:hi=mid
        else:lo=mid
    a=(lo+hi)/2
    step=(pi-a)/n
    def g(d):
        value=max(f(q,lam,d),0.)/(lam*lam-1.)
        return -expm1(-4*asinh(sqrt(value)))
    sum_=g(a)+g(pi)
    for j in range(1,n):
        sum_+=(4 if j%2 else 2)*g(a+step*j)
    return (sum_*step/3)/pi

def montecarlo(q,lam,N,seed):
    rng=random.Random(seed)
    count=0
    h=sqrt(1-q*q)
    max_diff=0
    for i in range(N):
        s=sqrt(rng.random())
        t=sqrt(rng.random())
        a=2*pi*rng.random()
        b=2*pi*rng.random()
        delta=abs(a-b)
        delta=min(delta,2*pi-delta)
        # Ambient coordinates, independently assembled in R^3.
        x=(q*s*cos(a),q*s*sin(a),h*s)
        y=(q*t*cos(b),q*t*sin(b),h*t)
        chord=sqrt(sum((xx-yy)**2 for xx,yy in zip(x,y)))
        geo=sqrt(max(0.,s*s+t*t-2*s*t*cos(q*delta)))
        # Independent equality of squared ambient dot-product formula.
        ambient2=(s-t)**2+4*q*q*s*t*sin(delta/2)**2
        max_diff=max(max_diff,abs(chord*chord-ambient2))
        count+=(geo/chord>lam)
    assert max_diff<1e-13
    return count/N

def main():
    num=0
    for q in [0.2,0.48,0.75]:
        K=k(q)
        assert 1<K<pi/2
        for frac in [0.3,0.6]:
            lam=1+frac*(K-1)
            exact=quadrature_tail(q,lam)
            estimate=montecarlo(q,lam,180000,round(q*10000+frac*1000))
            stderr=sqrt(exact*(1-exact)/180000)
            assert abs(estimate-exact)<6*stderr+0.002,(q,frac,estimate,exact)
            num+=1
        # Endpoint law: compare two small tolerances, relative error must shrink.
        e1=1e-3*(K-1)
        e2=2e-5*(K-1)
        r1=quadrature_tail(q,K-e1)/(leading(q)*e1**1.5)
        r2=quadrature_tail(q,K-e2)/(leading(q)*e2**1.5)
        assert abs(r2-1)<abs(r1-1) and abs(r2-1)<0.035,(q,r1,r2)
        num+=1
    print('CONE_RATIO_DISTRIBUTION_AND_TAIL_OK',num)

if __name__=='__main__': main()

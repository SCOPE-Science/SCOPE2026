#!/usr/bin/env python3
"""Reproduce diagnostic checks for the fixed-mean aggregation response theorem.

Standard library only. Sampling is a numerical diagnostic, not a proof of
continuous-parametric uniqueness or of the limiting asymptotics.
"""
import math


def h(t):
    if t <= 0:
        raise ValueError("t must be positive")
    if t < 1e-4:
        return 2 + 2*t/3 - t*t/9 + 7*t**3/135
    return t*t / ((1+t)*math.log1p(t)-t)


def opt_shape(z):
    assert z > 2
    a, b = 1e-12, max(10.0, 4*z*math.log1p(z))
    while h(b) < z:
        b *= 2
    for _ in range(130):
        m=(a+b)/2
        if h(m)<z:
            a=m
        else:
            b=m
    return z/((a+b)/2)


def normalized_recruits(k,z):
    if math.isinf(k):
        return math.exp(-z)
    return math.exp(-(k+1)*math.log1p(z/k))


def log_recruits(k,z):
    if math.isinf(k):
        return -z
    return -(k+1)*math.log1p(z/k)


def nb_direct(mu, k, q):
    p=(k/(k+mu))**k
    ans=0.0
    for n in range(1,10001):
        p*=((n-1+k)/n)*(mu/(k+mu))
        term=n*(q**(n-1))*p
        ans+=term
        if n>200 and abs(term)<1e-22:
            break
    return ans


def crossing(k1,k2):
    assert k1<k2
    def gap(z):return log_recruits(k1,z)-log_recruits(k2,z)
    low=1.0
    high=2.0
    while gap(high)<0:
        high *=2
    for _ in range(120):
        middle=(low+high)/2
        if gap(middle)<0:
            low=middle
        else:
            high=middle
    return (low+high)/2


def run():
    count=0
    for mu in (0.3,0.8,3.0,8.0,15.0):
        for k in (0.25,0.5,1.0,2.5,10.0):
            for q in (0.1,0.5,0.9):
                z=mu*(1-q)
                closed=mu*normalized_recruits(k,z)
                direct=nb_direct(mu,k,q)
                assert math.isclose(direct,closed,rel_tol=2e-11,abs_tol=1e-13),(mu,k,q,direct,closed)
                count+=1

    for z in (0.05,0.5,1.0,1.99,2.0):
        previous=-1.0
        for k in (0.05,0.1,0.3,0.7,1.2,3,10,100,10000,math.inf):
            r=normalized_recruits(k,z)
            assert r>previous, (k,z,r,previous)
            previous=r
            count+=1

    for z in (2.001,2.05,2.3,3,4,10,100):
        ko=opt_shape(z)
        rm=normalized_recruits(ko,z)
        assert rm>normalized_recruits(math.inf,z)
        assert rm>normalized_recruits(ko*0.99,z)
        assert rm>normalized_recruits(ko*1.01,z)
        for frac in (0.01,0.1,0.5,0.9,1.1,2,5,10,100):
            k=ko*frac
            derivative=-math.log1p(z/k)+(k+1)*z/(k*(k+z))
            assert ((derivative>0) == (frac<1)), (z,ko,frac,derivative)
            count+=1
        count+=3

    for k1,k2 in ((0.25,0.8),(1,2.5),(0.7,math.inf),(4,10),(20,math.inf)):
        zc=crossing(k1,k2)
        assert zc>1 and zc<10000
        for v in (0.01,0.2,0.8,0.999):
            assert log_recruits(k1,zc*v)<log_recruits(k2,zc*v)
            assert log_recruits(k1,zc/v)>log_recruits(k2,zc/v)
            count+=2
        count+=1

    for z in (2.0001,2.0005,2.001):
        ratio=opt_shape(z)*(z-2)/(4/3)
        assert abs(ratio-1)<0.0015, (z,ratio)
        count+=1
    for z in (1e6,1e9,1e12):
        k=opt_shape(z)
        assert abs(k*math.log(z)-1)<0.15,(z,k*math.log(z))
        ratio=normalized_recruits(k,z)*math.e*z*math.log(z)
        assert abs(ratio-1)<0.22,(z,ratio)
        count+=2
    z=4
    k=opt_shape(z)
    assert abs(k-0.9718973768147091)<1e-8
    print(f"PASS: {count} deterministic diagnostic assertions")
    print(f"z=4: optimal shape={k:.12f}; recruitment fraction={normalized_recruits(k,4):.12f}; Poisson fraction={math.exp(-4):.12f}")


if __name__=='__main__':
    run()

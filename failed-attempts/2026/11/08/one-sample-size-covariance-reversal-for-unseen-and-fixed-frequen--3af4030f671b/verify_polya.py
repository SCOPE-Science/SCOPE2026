"""Exact, standalone checks for unseen-versus-frequency covariance in symmetric Dirichlet-multinomial sampling.

Only standard-library dependencies. Run: python3 verify_polya.py
"""
from fractions import Fraction as F
from math import factorial, comb
from itertools import product


def rise(x, k):
    z = F(1)
    for i in range(k):
        z *= x + i
    return z


def prob(n, m, a, y):
    assert sum(y) == n
    v = F(factorial(n), 1)
    for k in y:
        v *= rise(a, k) / factorial(k)
    return v / rise(m*a, n)


def compositions(n, m):
    if m == 1:
        yield (n,)
    else:
        for k in range(n+1):
            for rest in compositions(n-k, m-1):
                yield (k,) + rest


def formula(n, m, a, r):
    if n < r:
        return F(0)
    a = F(a)
    p0 = rise((m-1)*a, n) / rise(m*a, n)
    pr = comb(n, r)*rise(a,r)*rise((m-1)*a,n-r) / rise(m*a,n)
    if m == 2:
        p0r = (comb(n,r)*rise(a,r)*rise((m-2)*a,n-r) / rise(m*a,n)) if n == r else F(0)
    else:
        p0r = comb(n,r)*rise(a,r)*rise((m-2)*a,n-r) / rise(m*a,n)
    return m*(m-1)*p0r - m*m*p0*pr


def q(n,m,a,r):
    a=F(a)
    assert m>=3 and n>=r
    return rise((m-2)*a,n-r)*rise(m*a,n)/(rise((m-1)*a,n-r)*rise((m-1)*a,n))


def check():
    tests=0
    for m in range(2,6):
        for a in (F(1,2),F(1),F(2),F(5,2)):
            for n in range(1,10):
                records=list(compositions(n,m))
                # enumeration contains at most 495 vectors
                dist=[(y,prob(n,m,a,y)) for y in records]
                assert sum((p for _,p in dist),F(0))==1
                for r in range(1,min(n+2,6)):
                    e0=er=e0r=F(0)
                    for y,p in dist:
                        z=y.count(0); t=y.count(r)
                        e0+=p*z; er+=p*t; e0r+=p*z*t
                    cov=e0r-e0*er
                    assert cov==formula(n,m,a,r),(m,a,n,r,cov,formula(n,m,a,r))
                    tests+=1
    for m in range(3,14):
        for r in range(1,13):
            for a in (F(1,4),F(1),F(5,2),F(10)):
                old=q(r,m,a,r)
                assert (old==F(m,m-1)) if r==1 else (old>F(m,m-1))
                for n in range(r, r+29):
                    cur=q(n,m,a,r)
                    assert old==cur
                    nxt=q(n+1,m,a,r)
                    ratio=(F(n-r)+(m-2)*a)*(F(n)+m*a)/((F(n-r)+(m-1)*a)*(F(n)+(m-1)*a))
                    assert nxt==cur*ratio
                    assert nxt<cur
                    old=nxt
                    tests+=1
    for m in range(3,15):
        for r in range(1,15):
            boundary=F(m*(r-1)+2,2)
            for n in range(max(1,r),max(r+1,2*m*r+5)):
                cov=formula(n,m,F(1),r)
                predicted=(1 if n<boundary else (-1 if n>boundary else 0))
                assert (cov>0)-(cov<0)==predicted,(m,r,n,cov,boundary)
                tests+=1
    print('PASS',tests,'exact rational identities, exhaustive distributions, strict ratios and sample-size sign checks')

if __name__=='__main__':
    check()

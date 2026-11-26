"""Independent finite-parameter checks for the geometric-shift q-Berezin radius."""
import math
import random


def root(q, beta):
    h = math.sqrt((1.0-q)*(1.0+q))
    def poly(r):
        return 1.0+(beta-3.0)*r*r+2.0*h*(1.0-beta)*r**3+beta*r**4
    lo, hi = 0.0, 1.0
    for _ in range(110):
        mid = (lo+hi)/2.0
        if poly(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2.0


def radius(q,beta,r):
    h=math.sqrt((1-q)*(1+q))
    return q*r*(1-r*r)/(1-beta*r*r-(1-beta)*h*r)


def main():
    rng=random.Random(260102334)
    checks=0
    for _ in range(1800):
        q=0.01+0.99*rng.random()
        beta=0.9*rng.random()
        h=math.sqrt((1-q)*(1+q))
        r=root(q,beta)
        R=radius(q,beta,r)
        w1=(r-h)/(1-h*r)
        overlap=math.sqrt((1-w1*w1)*(1-r*r))/(1-w1*r)
        direct=q*(1-w1*r)*r/(1-beta*w1*r)
        assert abs(overlap-q)<3e-12
        assert abs(direct-R)<3e-12
        checks+=2
        for j in range(20):
            s=(j+.5)/20
            assert radius(q,beta,s)<=R+2e-12
            checks+=1
        assert R>0
        checks+=1
    q=beta=0.5
    r=5.0/6.0
    w1=(r-math.sqrt(3)/2)/(1-r*math.sqrt(3)/2)
    assert abs(math.sqrt((1-w1*w1)*(1-r*r))/(1-w1*r)-q)<1e-13
    assert radius(q,beta,r)>q*math.sqrt(1-q*q)
    assert 490**2>3*282**2
    checks+=3
    for q in (0.2,0.5,1.0):
        h=math.sqrt((1-q)*(1+q))
        for beta in (0.9999,0.999999):
            r=root(q,beta)
            coefficient=(q-radius(q,beta,r))/math.sqrt(1-beta)
            limit=q*math.sqrt(2*(1-h))
            assert abs(coefficient-limit)/limit<0.04
            checks+=1
    for beta in (0.0,0.3,0.7):
        q=1e-5
        limit=2/(1+beta)
        observed=radius(q,beta,root(q,beta))/q
        assert abs(observed-limit)<0.04
        checks+=1
    print('PASS:',checks,'finite algebraic, kernel, and asymptotic checks')


if __name__=='__main__':main()

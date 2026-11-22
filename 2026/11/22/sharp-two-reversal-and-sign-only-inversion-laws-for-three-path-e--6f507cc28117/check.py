"""Deterministic numerical checks for a three-mode passive salinity model.

Requires only Python 3 standard library. The analytic proof is independent of these tests.
"""
import math
import random


def threshold(a, c, alpha, beta, gamma):
    p, q = beta-alpha, gamma-beta
    if not (a > 0 and c > 0 and 0 < p and 0 < q):
        raise ValueError('positive amplitudes and ordered rates required')
    ratio = c*q/(a*p)
    if ratio <= 1:
        return (None, a+c)
    star = math.log(ratio)/(p+q)
    low = a*math.exp(p*star) + c*math.exp(-q*star)
    return star, low


def g(z, a, c, p, q):
    return a*math.exp(p*z) + c*math.exp(-q*z)


def bisect_root(a, c, b, p, q, left, right):
    fl = g(left,a,c,p,q)-b
    fr = g(right,a,c,p,q)-b
    assert fl*fr <= 0
    for _ in range(100):
        m = (left+right)/2
        fm = g(m,a,c,p,q)-b
        if fl*fm <= 0:
            right,fr=m,fm
        else:
            left,fl=m,fm
    return (left+right)/2


def positive_roots(a, c, b, alpha, beta, gamma):
    p, q = beta-alpha, gamma-beta
    star, minimum = threshold(a,c,alpha,beta,gamma)
    if star is not None and b > minimum and b < a+c:
        end = max(star+1.,1.)
        while g(end,a,c,p,q)<=b:
            end += 1.
        return [bisect_root(a,c,b,p,q,0.,star),bisect_root(a,c,b,p,q,star,end)]
    if star is not None and abs(b-minimum)<1e-14:
        return [star]
    if b >= a+c and (b>a+c or star is not None):
        start=star or 0.
        if b==a+c and star is None:
            return []
        end=max(start+1.,1.)
        while g(end,a,c,p,q)<=b:
            end +=1.
        return [bisect_root(a,c,b,p,q,start,end)]
    if star is None and b>a+c:
        end=1.
        while g(end,a,c,p,q)<=b:
            end +=1.
        return [bisect_root(a,c,b,p,q,0.,end)]
    return []


def check():
    rng=random.Random(20231103)
    num=0
    for _ in range(5000):
        a=math.exp(rng.uniform(-1,1));c=math.exp(rng.uniform(-1,1))
        alpha=rng.uniform(.2,2);p=rng.uniform(.2,1.5);q=rng.uniform(.2,1.5)
        beta=alpha+p;gamma=beta+q
        star,lo=threshold(a,c,alpha,beta,gamma)
        b=(a+c)*rng.uniform(.3,1.7)
        roots=positive_roots(a,c,b,alpha,beta,gamma)
        predicted=2 if star is not None and lo<b<a+c else 1 if b>a+c else 0
        assert len(roots)==predicted,(a,c,alpha,beta,gamma,b,roots)
        for z in roots:
            assert z>=0 and abs(g(z,a,c,p,q)-b)<2e-10
        if len(roots)==2:
            l,r=roots
            assert 0<l<star<r
            U=math.exp(p*l);V=math.exp(p*r)
            X=math.exp(-q*l);Y=math.exp(-q*r)
            D=V*X-U*Y
            arel=(X-Y)/D;crel=(V-U)/D
            assert abs(arel-a/b)<1e-9
            assert abs(crel-c/b)<1e-9
            num+=1
    a,c,b,alpha,beta,gamma=1.,4.,4.5,1.,2.,3.
    roots=positive_roots(a,c,b,alpha,beta,gamma)
    expected=[math.log((9-math.sqrt(17))/4),math.log((9+math.sqrt(17))/4)]
    for x,y in zip(roots,expected): assert abs(x-y)<1e-12
    assert abs((roots[0]+roots[1])/2-math.log(2))<1e-12
    star,lo=threshold(a,c,alpha,beta,gamma)
    for eps in [1e-2,1e-3,1e-4,1e-5,1e-6]:
        x1,x2=positive_roots(a,c,lo+eps,alpha,beta,gamma)
        pred=2*math.sqrt(2*eps/(lo*(beta-alpha)*(gamma-beta)))
        assert abs((x2-x1)/pred-1)<.01
    # Boundary counts and the single-path impossibility are analytic.
    print(f'passed: 5000 random parameter regimes; {num} two-reversal inverse tests; exact witness and five fold checks')

if __name__=='__main__':
    check()

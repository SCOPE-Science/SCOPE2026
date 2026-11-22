"""Independent direct-geometry checks for a three-receiver early-warning idealization.

Run: python3 checker.py
Uses only the Python standard library. Finite tests supplement, not replace, the proof.
"""
from math import isclose
import random


def values(p, theta):
    assert 0 < p < 1 and 0 <= theta <= 1
    return (0., (1-theta)*p,
            (1-theta)*(2*p-p*p)+theta*p*p,
            (1-theta)*(3*p-3*p*p+p**3)+theta*(3*p*p-2*p**3))


def multiplicity_lengths(centers, reach, circumference=1.):
    assert len(centers) == 3 and 0 < reach <= circumference/3
    segments = []
    edges = [0., circumference]
    for x in centers:
        lo = (x-reach/2) % circumference
        hi = (x+reach/2) % circumference
        if lo < hi:
            intervals = [(lo, hi)]
        else:
            intervals = [(lo, circumference), (0., hi)]
        segments.append(intervals)
        for a,b in intervals:
            edges += [a,b]
    edges.sort()
    masses = [0.] * 4
    for a,b in zip(edges[:-1],edges[1:]):
        if b <= a:
            continue
        mid = (a+b)/2
        n = sum(any(s <= mid <= t for s,t in i) for i in segments)
        masses[n] += b-a
    return masses


def direct(centers, reach, p, theta, circumference=1.):
    lengths = multiplicity_lengths(centers, reach, circumference)
    fs = values(p,theta)
    return sum(a*b for a,b in zip(lengths,fs))/circumference


def bound(reach,p,theta,circumference=1.):
    _,f1,f2,f3=values(p,theta)
    return reach/circumference * max(3*f1,f1+f2,f3)


def phase(p,theta):
    crit=(2-p)/(4-3*p)
    if theta < .5:
        return 0
    if theta > crit:
        return 2
    if theta > .5 and theta < crit:
        return 1
    return -1


def check():
    rng=random.Random(20231203)
    total=0
    for i in range(18000):
        p=rng.uniform(.01,.99)
        theta=rng.random()
        reach=rng.uniform(.001,1/3)
        centers=[rng.random() for _ in range(3)]
        lengths=multiplicity_lengths(centers,reach)
        assert isclose(sum(lengths),1.,abs_tol=1.e-12)
        assert isclose(sum(k*lengths[k] for k in range(4)),3*reach,abs_tol=1.e-12)
        assert lengths[2]+lengths[3] <= reach+1.e-12
        b=bound(reach,p,theta)
        val=direct(centers,reach,p,theta)
        assert val <= b+2.e-12, (val,b,p,theta,centers)
        distinct=direct([reach/2,3*reach/2,5*reach/2],reach,p,theta)
        paired=direct([reach/2,reach/2,5*reach/2],reach,p,theta)
        chain=direct([reach/2,reach,3*reach/2],reach,p,theta)
        assert isclose(chain,paired,abs_tol=1.e-12)
        tripled=direct([reach/2]*3,reach,p,theta)
        assert isclose(max(distinct,paired,tripled),b,abs_tol=1.e-12)
        _,f1,f2,f3=values(p,theta)
        assert isclose(distinct,3*reach*f1,abs_tol=1.e-12)
        assert isclose(paired,reach*(f1+f2),abs_tol=1.e-12)
        assert isclose(tripled,reach*f3,abs_tol=1.e-12)
        regime=phase(p,theta)
        if regime>=0:
            assert isclose((distinct,paired,tripled)[regime], b,abs_tol=1.e-12)
        total += 1
    for p in (.01,.15,.4,.6,.8,.95,.99):
        for theta in (.5,(2-p)/(4-3*p)):
            d=direct([.1,.3,.5],.2,p,theta)
            q=direct([.1,.1,.5],.2,p,theta)
            t=direct([.1]*3,.2,p,theta)
            if theta==.5:
                assert isclose(d,q,abs_tol=1.e-12)
            else:
                assert isclose(q,t,abs_tol=1.e-12)
    p=.8; theta=.625; reach=.25
    assert isclose(bound(reach,p,theta),.265,abs_tol=1e-14)
    assert phase(p,theta)==1
    print('PASS:',total,'random geometry/detection comparisons; 14 boundary cases')
    print('illustration (p, theta, reach) =',p,theta,reach)
    print('disjoint/pair/triple:',*[round(direct(c,reach,p,theta),12) for c in ([.125,.375,.625],[.125,.125,.625],[.125]*3)])
    print('phase threshold theta_c=',(2-p)/(4-3*p))
    print('distinct-receiver chain:',round(direct([.125,.25,.375],reach,p,theta),12))

if __name__=='__main__':
    check()

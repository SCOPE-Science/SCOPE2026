"""Exact integer-arithmetic checks for lattice-width/mixed-area results.

Run: python3 verify.py
No third-party dependencies. Finite checks complement, not replace, the proofs.
"""
from itertools import product
from math import gcd
import random


def hull(points):
    pts = sorted(set(map(tuple, points)))
    if len(pts) <= 1:
        return pts
    def cross(a,b,c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    lo=[]
    for p in pts:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0:
            lo.pop()
        lo.append(p)
    up=[]
    for p in reversed(pts):
        while len(up)>1 and cross(up[-2],up[-1],p)<=0:
            up.pop()
        up.append(p)
    return lo[:-1]+up[:-1]


def vol2(points):
    h=hull(points)
    if len(h)<=2:
        return 0
    return abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(h,h[1:]+h[:1])))


def mixed(P,Q):
    S=[(p[0]+q[0],p[1]+q[1]) for p,q in product(P,Q)]
    w=vol2(S)-vol2(P)-vol2(Q)
    assert w>=0 and w%2==0, (P,Q,w)
    return w//2


def width(P):
    return max(p[1] for p in P)-min(p[1] for p in P)


def example(a,b,d,k):
    return [(0,0),(a,a*d)],[(0,0),(b,b*d),(0,k)]


def semigroup_example(d,m1,m2):
    q1,r1=divmod(m1,d)
    q2,r2=divmod(m2,d)
    P0=[(0,0),(3,3*d),(3,3*d-r2)]
    Q0=[(0,0),(0,r1),(5,5*d)]
    P=[(x+e,y) for x,y in P0 for e in (0,q2)]
    Q=[(x+e,y) for x,y in Q0 for e in (0,q1)]
    return P,Q


def seven(d):
    return [(0,0),(3,3*d),(1,d+1),(0,1)],[(0,0),(5,5*d),(3,3*d+1),(0,2)]


def four(d):
    return [(0,0),(1,3*d)],[(0,0),(2,5*d),(1,2*d+4)]


def main():
    checks=0
    for a in range(1,9):
        for b in range(a+1,12):
            for d in range(1,11):
                for k in range(1, min(d,b)//a+1):
                    if a*k>=min(d,b):continue
                    P,Q=example(a,b,d,k)
                    assert (width(P),width(Q),mixed(P,Q))==(a*d,b*d,a*k)
                    checks+=1
    for d in range(1,41):
        for m1 in range(12):
            for m2 in range(12):
                P,Q=semigroup_example(d,m1,m2)
                assert (width(P),width(Q),mixed(P,Q))==(3*d,5*d,3*m1+5*m2)
                checks+=1
        P,Q=seven(d)
        assert (width(P),width(Q),mixed(P,Q))==(3*d,5*d,7)
        assert (vol2(P),vol2(Q),vol2([(p[0]+q[0],p[1]+q[1]) for p,q in product(P,Q)]))==(4,11,29)
        checks+=2
    for d in (2,3,4):
        P,Q=four(d)
        assert (width(P),width(Q),mixed(P,Q))==(3*d,5*d,4)
        checks+=1
    P=[(0,0),(1,3)];Q=[(0,0),(1,5)]
    assert (width(P),width(Q),mixed(P,Q))==(3,5,2)
    checks+=1
    P=[(0,0),(1,3)];Q=[(0,0),(2,5),(0,3)]
    assert (width(P),width(Q),mixed(P,Q))==(3,5,4)
    checks+=1
    for d in (1,2):
        P=[(0,0),(2,3*d)]
        Q=[(0,0),(3,5*d)]
        assert mixed(P,Q)==d
        checks+=1
    rng=random.Random(260216104)
    for _ in range(16000):
        P=hull([(rng.randrange(-10,11),rng.randrange(-10,11)) for i in range(rng.randrange(2,7))])
        Q=hull([(rng.randrange(-10,11),rng.randrange(-10,11)) for i in range(rng.randrange(2,7))])
        w1,w2=width(P),width(Q)
        if not w1 or not w2: continue
        d=gcd(w1,w2)
        a,b=w1//d,w2//d
        if a>b:
            a,b=b,a
            P,Q=Q,P
        v=mixed(P,Q)
        if 0<v<min(d,b):
            assert v%a==0 and len(hull(P))==2,(a,b,d,v,P,Q)
        checks+=1
    print('PASS: %d integer-arithmetic checks. Universal statements require the accompanying proof.'%checks)

if __name__=='__main__':main()

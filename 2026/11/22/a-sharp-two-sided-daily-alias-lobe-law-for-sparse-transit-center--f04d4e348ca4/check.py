#!/usr/bin/env python3
"""Independent exact-rational checks for the window function theorem.

Uses an event-phase partition rather than the interval-intersection proof.
"""
from fractions import Fraction as Q
import random

def formula(n, r, w, p):
    d=abs(p-1)
    ell=w-(r-1)*d
    if ell <= 0:
        return Q(0)
    return (ell + (n-r)*min(d,ell))/p

def enumerate_phases(n, r, w, p):
    # Each observation [j,j+w] projects modulo period p onto at most two arcs.
    arcs=[]
    for j in range(n):
        a=Q(j)%p
        b=a+w
        if b<=p:
            arcs.append((a,b,j))
        else:
            arcs.append((a,p,j))
            arcs.append((Q(0),b-p,j))
    cuts=sorted(set([Q(0),p]+[x for a,b,j in arcs for x in (a,b)]))
    covered=Q(0)
    for a,b in zip(cuts,cuts[1:]):
        mid=(a+b)/2
        count=sum(1 for x,y,j in arcs if x<=mid<y)
        if count>=r:
            covered+=b-a
    return covered/p

def run():
    rng=random.Random(18213)
    trials=0
    for n in range(4,31):
        for r in range(2,n//2+1):
            for k in (3,5,11):
                w=Q(1,k*n)
                for sign in (-1,1):
                    ds=[Q(0),w/Q(3*r),w/r,w*(Q(2,r+1)), w/(r-1), Q(1,2*n)]
                    for i in range(3):
                        ds.append(Q(rng.randrange(0,100000),100000)*Q(1,2*n))
                    for d in ds:
                        if d>Q(1,2*n):continue
                        p=Q(1)+sign*d
                        a=formula(n,r,w,p)
                        b=enumerate_phases(n,r,w,p)
                        assert a==b, (n,r,w,p,a,b)
                        trials+=1
                    # Prove unique optimizer algebraically in the writeup;
                    # sample additional points to detect implementation flaws.
                    optimum=formula(n,r,w,Q(1)+sign*w/r)
                    for i in range(15):
                        d=Q(rng.randrange(0,100000),100000)*Q(1,2*n)
                        assert formula(n,r,w,Q(1)+sign*d) <= optimum
                        trials+=1
                    assert formula(n,r,w,Q(1)+sign*w/r)==w*(n-r+1)/(r+sign*w)
                    trials+=1
                assert w*(n-r+1)/(r-w) > w*(n-r+1)/(r+w) > w
                trials+=1
    n,r,w=30,2,Q(1,144)
    assert formula(n,r,w,Q(1)-w/r)==Q(29,1)*w/(r-w)
    print('PASS',trials,'exact rational checks')
    print('example 30 nights 10 min, >=2 transits')
    print('Pshort',Q(1)-w/r,'Pexact',Q(1),'Plong',Q(1)+w/r)
    print('short_prob',float(formula(n,r,w,Q(1)-w/r)))
    print('at_alias_prob',float(w))
    print('long_prob',float(formula(n,r,w,Q(1)+w/r)))

if __name__=='__main__':run()

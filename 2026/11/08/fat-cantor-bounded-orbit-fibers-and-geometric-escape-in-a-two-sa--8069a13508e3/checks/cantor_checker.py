"""Exact-rational checks for a nonautonomous full-tent fiber census."""
from fractions import Fraction as Q
from collections import Counter


def interval(s, q, n):
    return (-1-q*s**n, 1+q*s**n)


def fibers(s, q, n):
    pieces = [interval(s, q, n)]
    for j in range(n-1, -1, -1):
        k = (2-s)*q*s**j
        lo_dom, hi_dom = interval(s, q, j)
        children = []
        for lo, hi in pieces:
            a, b = (lo-1-k)/2, (hi-1-k)/2
            c, d = (1+k-hi)/2, (1+k-lo)/2
            assert lo_dom <= a <= b < 0 < c <= d <= hi_dom
            children.extend([(a,b),(c,d)])
        pieces = sorted(children)
    return pieces


def norm(z):
    return 1-2*abs(z)


def planar_step(s, x, y):
    t = s+(2 if x<=0 else -2)
    d = s*(2 if x<=0 else -2)
    return (1+t*x+y, -d*x)


def verify():
    samples=0
    for s in (Q(1,5), Q(1,2), Q(2,3), Q(4,5)):
        for q in (Q(1,9),Q(1,3),Q(4,5),Q(2,1)):
            for n in range(0,10):
                pcs=fibers(s,q,n)
                assert len(pcs)==2**n
                target=Q(2,2**n)*(1+q*s**n)
                assert all(b-a==target for a,b in pcs)
                assert sum((b-a for a,b in pcs),Q())==2*(1+q*s**n)
                assert pcs[0][0]==-1-q and pcs[-1][1]==1+q
                for i,((a,b),(c,d)) in enumerate(zip(pcs,pcs[1:])):
                    assert b<c
                if n:
                    gaps=Counter(c-b for ((a,b),(c,d)) in zip(pcs,pcs[1:]))
                    expected=Counter({2*(1-s)*q*(s/2)**j: 2**j for j in range(n)})
                    assert gaps==expected,(s,q,n,gaps,expected)
                samples+=1
            w_star=s/(1-s)
            for z in (Q(-7,6),Q(-1,3),Q(0),Q(1,2),Q(4,3)):
                x=z/(1-s)
                y=w_star+(2-s)*q/(1-s)-s*x
                xn,yn=planar_step(s,x,y)
                zn=(1-s)*xn
                assert zn==norm(z)+(2-s)*q
                wn=yn+s*xn
                assert wn-w_star==s*(y+s*x-w_star)
    for s in (Q(1,2),Q(3,4)):
        for q in (Q(-1,1),Q(-1,2),Q(0),Q(1,3)):
            for z in (Q(-3,2),Q(-1,2),Q(0),Q(1,2),Q(3,2)):
                z0=z
                for n in range(10):
                    next_z=norm(z)+(2-s)*q*s**n
                    l,r=interval(s,q,n)
                    if q>=-1 and l<=z<=r:
                        lnext,rnext=interval(s,q,n+1)
                        if q<=0: assert lnext<=next_z<=rnext
                    z=next_z
    print('FIBER_CANTOR_EXACT_INTERVAL_GAPS_OK',samples,'cylinders_max',512)
    print('AFFINE_SKEW_PRODUCT_AND_FIBER_PHASE_CHECK_OK')

if __name__=='__main__':
    verify()

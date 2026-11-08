#!/usr/bin/env python3
"""Exact rational checks of a two-lag symbolic correlation theorem."""
from fractions import Fraction as Q


def raw_density(x, alpha):
    a, c, d = alpha-Q(1), 2*alpha-Q(2), Q(2)-alpha
    return (Q(1) + int(abs(x)<a) + Q(1,2)*int(abs(x)<c)
            + Q(1,2)*int(abs(x)<d))


def images(alpha):
    a, c, d = alpha-Q(1), 2*alpha-Q(2), Q(2)-alpha
    breaks = {Q(-1),Q(1),Q(0)}
    knots = [-a,a,-c,c,-d,d]
    breaks.update(v for v in knots if -1<v<1)
    for v in knots:
        for u in (2*v,2*v+alpha,2*v-alpha):
            if -1<u<1: breaks.add(u)
    for v in (alpha-Q(2),alpha-Q(1),Q(1)-alpha,Q(2)-alpha):
        if -1<v<1: breaks.add(v)
    return sorted(breaks)


def check_one(alpha):
    assert Q(5,4)<=alpha<=Q(3,2)
    a,c,d=alpha-Q(1),2*alpha-Q(2),Q(2)-alpha
    # Midpoints exhaust all continuity pieces of both sides of the PF identity.
    endpoints=images(alpha)
    for lo,hi in zip(endpoints,endpoints[1:]):
        x=(lo+hi)/2
        right=raw_density(x/2,alpha)
        if alpha-Q(2)<x<alpha-Q(1):
            right+=raw_density((x-alpha)/2,alpha)
        if Q(1)-alpha<x<Q(2)-alpha:
            right+=raw_density((x+alpha)/2,alpha)
        assert 2*raw_density(x,alpha)==right,(alpha,x,lo,hi)
    # Direct exact integration of the step density.
    qs=sorted({Q(-1),Q(1),-a,a,-c,c,-d,d})
    assert sum((r-l)*raw_density((l+r)/2,alpha) for l,r in zip(qs,qs[1:]))==3*alpha
    # Compute lag-two zero-pair event by disjoint inverse-branch intervals.
    b=(alpha+Q(1,2))/4
    # Event is [-1/8,1/8] union +/-[1/4,b].
    def area_pos(lo,hi):
        pts=sorted({lo,hi}|{v for v in (a,c,d) if lo<v<hi})
        return sum((r-l)*raw_density((l+r)/2,alpha)/(3*alpha)
                   for l,r in zip(pts,pts[1:]))
    p2=2*area_pos(Q(0),Q(1,8))+2*area_pos(Q(1,4),b)
    assert p2==1-Q(3,4)/alpha,(alpha,p2)
    # Lag-one zero pair equals x in [-1/4,1/4].
    p1=2*area_pos(Q(0),Q(1,4))
    assert p1==1/(2*alpha)
    # Opposite signs cannot occur in one step; same-sign two-step interval.
    t=(alpha+Q(1,2))/2
    ppp=area_pos(t,Q(1))
    assert ppp==(Q(3)-2*alpha)/(12*alpha)
    cov1=p1-Q(4,9)
    cov2=p2-Q(4,9)
    assert cov1==(Q(9)-8*alpha)/(18*alpha)
    assert cov2==(20*alpha-27)/(36*alpha)
    assert (cov2<0)==(alpha<Q(27,20)) if alpha!=Q(27,20) else cov2==0
    print(f'alpha={alpha}: p00={p1} p0_2={p2} p++={ppp} cov1={cov1} cov2={cov2} cells={len(endpoints)-1}')


def main():
    for p in (Q(5,4),Q(51,40),Q(13,10),Q(4,3),Q(27,20),Q(7,5),Q(29,20),Q(3,2)):
        check_one(p)
    print('ALL_EXACT_CYLINDER_AND_TRANSFER_CHECKS_PASS')


if __name__=='__main__': main()

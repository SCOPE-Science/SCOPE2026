#!/usr/bin/env python3
"""Exact rational diagnostics for a three-mode periodic service-design theorem.

This file uses only the Python standard library. Finite diagnostics do not prove
statements over all real operating probabilities; see the analytic proof.
"""
from fractions import Fraction as Q
from itertools import product


def optimal(u, v, w):
    assert u > 0 and v > 0 and w > 0 and u + v + w <= 1
    delta = u*v - w*(u + v + w)
    if delta >= 0:
        denominator = 4*u + 3*v + 3*w
        a = (2*u + v + w)/denominator
        b = Q(0)
        c = d = (u + v + w)/denominator
    else:
        denominator = 2*(3*u*v + 3*u*w + 3*v*w + 2*w*w)
        a = (3*u + w)*(v + w)/denominator
        b = (w*(u + v + w) - u*v)/denominator
        c = d = (u + w)*(2*v + w)/denominator
    return a,b,c,d


def loss(g,u,v,w):
    a,b,c,d = g
    # Half-period-normalized waiting time, including the no-optional-service state.
    return (u*(a*a+(b+c+d)**2) + v*((a+b)**2+c*c+d*d)
            + w*(a*a+b*b+c*c+d*d) + (1-u-v-w))/2


def gradients(a,b,u,v,w):
    # For F=2 loss after minimization over c=d, omit the constant no-service term.
    da = (8*a*u + 6*a*v + 6*a*w + 6*b*v + 2*b*w - 4*u - 2*v - 2*w)/2
    db = (6*a*v + 2*a*w + 6*b*v + 6*b*w - 2*v - 2*w)/2
    return da,db


def check(u,v,w):
    a,b,c,d = optimal(u,v,w)
    assert all(x>=0 for x in [a,b,c,d])
    assert a+b+c+d == 1 and c == d
    da,db = gradients(a,b,u,v,w)
    assert da == 0
    assert db == 0 if b>0 else db>=0
    assert (b==0) == (u*v>=w*(u+v+w))
    # Positive definite Hessian in the two free coordinates. Strict convexity
    # in the four gaps follows immediately from the all-services term w>0.
    h11=4*u+3*v+3*w
    h12=3*v+w
    h22=3*v+3*w
    assert h11>0 and h11*h22-h12*h12>0
    for aa,bb,cc in product(range(0,7),repeat=3):
        if aa+bb+cc>6: continue
        g=tuple(Q(x,6) for x in (aa,bb,cc,6-aa-bb-cc))
        assert loss(g,u,v,w)>=loss((a,b,c,d),u,v,w)


def main():
    count=0
    for iu in range(1,10):
        for iv in range(1,10):
            for iw in range(1,10):
                if iu+iv+iw>11: continue
                u,v,w=(Q(x,11) for x in (iu,iv,iw))
                check(u,v,w);count+=1
    u=v=Q(9,20);w=Q(1,10)
    a,b,c,d=optimal(u,v,w)
    assert (a,b,c,d)==(Q(29,69),Q(0),Q(20,69),Q(20,69))
    assert loss((a,b,c,d),u,v,w)==Q(29,138)
    assert loss((Q(1,4),)*4,u,v,w)==Q(19,80)
    assert Q(1)-loss((a,b,c,d),u,v,w)/loss((Q(1,4),)*4,u,v,w)==Q(151,1311)
    u=v=Q(2,5);w=Q(1,5)
    assert optimal(u,v,w)==(Q(21,52),Q(1,52),Q(15,52),Q(15,52))
    print('PASS: %d exact-rational probability triples, simplex comparisons and both benchmark cases' % count)
    print('All-real-parameter uniqueness and the radical threshold require the accompanying proof.')

if __name__=='__main__': main()

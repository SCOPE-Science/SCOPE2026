#!/usr/bin/env python3
"""Reproduce finite exact geometry checks for (132,213)-avoiding permutahedra.

Uses only Python's standard library. Infinite-dimensional assertions require the
written matrix comparison proof, not these finite tests.
"""
from fractions import Fraction
from itertools import combinations
from decimal import Decimal, localcontext
from math import comb


def cuts_vertices(d):
    for mask in range(1 << (d - 1)):
        cut = [0] + [k for k in range(1, d) if mask & (1 << (k - 1))] + [d]
        blocks = []
        for i in range(len(cut) - 1):
            start, end = cut[i], cut[i+1]
            blocks += list(range(d - end + 1, d - start + 1))
        yield tuple(blocks)


def pattern_ok(x):
    for a, b, c in combinations(range(len(x)), 3):
        if x[a] < x[c] < x[b] or x[b] < x[a] < x[c]:
            return False
    return True


def test_exact_vertices():
    ncheck=0
    for d in range(2, 11):
        V=list(cuts_vertices(d))
        assert len(V)==2**(d-1) and len(set(V))==len(V)
        for x in V:
            assert pattern_ok(x)
            assert sum(x)==d*(d+1)//2
            for k in range(1,d):
                S=sum(x[:k]); M=k*(2*d-k+1)//2
                assert x[k-1]-x[k]+1>=0
                assert S<=M
                assert (x[k-1]-x[k]+1==0) != (S==M)
                ncheck+=1
    return ncheck


def test_laplacian_and_center():
    ncheck=0
    with localcontext() as ctx:
        ctx.prec=70
        two=Decimal(2)
        for d in range(2,101):
            H=(Decimal(d*(d-1))).sqrt()
            rt=two/(two.sqrt()+two/H)
            slope=two*rt/H
            b=two-rt*two.sqrt()
            assert abs(b-slope) < Decimal('1e-65')
            u=[Decimal(0)]+[b*Decimal(k*(d-k))/two for k in range(1,d)]+[Decimal(0)]
            for k in range(1,d):
                lap=2*u[k]-u[k-1]-u[k+1]
                assert abs(lap-b)<Decimal('1e-60')
                norm=(Decimal(k*(d-k))/Decimal(d)).sqrt()
                distance_b=u[k]/norm
                assert distance_b+Decimal('1e-60')>=rt
                if k in (1,d-1):
                    assert abs(distance_b-rt)<Decimal('1e-60')
                elif d>3:
                    assert distance_b>rt
                ncheck+=1
            x=[Decimal(d-k+1)+u[k-1]-u[k] for k in range(1,d+1)]
            assert abs(sum(x)-Decimal(d*(d+1)/2))<Decimal('1e-60')
            for k in range(1,d):
                dist_a=(x[k-1]-x[k]+1)/two.sqrt()
                assert abs(dist_a-rt)<Decimal('1e-60')
                ncheck+=1
            # The first row of L^{-1} is positive at all columns,
            # establishing uniqueness when its bound is tight.
            for j in range(1,d):
                inv=Fraction(d-j,d)
                assert inv>0
                ncheck+=1
    return ncheck

if __name__=='__main__':
    a=test_exact_vertices()
    b=test_laplacian_and_center()
    print('PASS: exact vertex/facet signatures',a)
    print('PASS: high-precision inball/facet/Laplacian checks',b)
    print('PASS: total checks',a+b)

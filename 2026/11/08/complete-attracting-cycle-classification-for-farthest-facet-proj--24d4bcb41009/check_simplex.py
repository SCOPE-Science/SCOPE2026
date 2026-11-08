#!/usr/bin/env python3
"""Exact-rational finite consistency checks for a regular-simplex face projection theorem.

This tests formulas, not their validity for all dimensions or all initial points.
Run: python3 check_simplex.py
"""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
from random import Random

checks = 0

def eq(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1


def project(lam, j):
    d = len(lam) - 1
    assert lam[j] >= 0
    t = lam[j] / d
    z = [v + t for v in lam]
    z[j] = Q(0)
    return z


def target(d, order):
    # order=(last face selected, then descending next face labels)
    assert len(order) == d + 1
    out = [Q(0)] * (d + 1)
    for k in range(1, d + 1):
        out[order[k]] = Q(2 * (d + 1 - k), d * (d + 1))
    return out


def gap(vec):
    v = sorted(vec)
    return [v[k+1] - v[k] for k in range(len(v)-1)]


def gapstep(g):
    d = len(g)
    return [sum(g) / d] + g[:-1]


def ambient_project(lam, j):
    # Points in H={z in Q^(d+1):sum z=0} represented as z=lam-1/(d+1).
    # The affine face F_j is z_j=-1/(d+1).
    d = len(lam) - 1
    z = [v-Q(1,d+1) for v in lam]
    vj = [-Q(1,d+1)]*(d+1)
    vj[j] = Q(d,d+1)
    dot = sum(z[k]*vj[k] for k in range(d+1)) + Q(1,d+1)
    norm = sum(v*v for v in vj)
    zp = [z[k] - dot* vj[k] / norm for k in range(d+1)]
    return [v+Q(1,d+1) for v in zp]


def one_step(lam):
    maxval=max(lam)
    inds=[j for j,v in enumerate(lam) if v==maxval]
    if len(inds)>1: return lam[:], None
    return project(lam, inds[0]), inds[0]

rng=Random(20261102)
for d in range(3,8):
    n=d+1
    # all (d+1)!/ (d+1) cyclic orientations represented by starting at facet 0.
    orbits=set()
    for tail in permutations(range(1,n)):
        order=(0,)+tail
        a=target(d,order)
        eq(sum(a),Q(1))
        eq(a[0],Q(0))
        eq(sorted(a),[Q(2*k,d*(d+1)) for k in range(d+1)])
        b=a[:]
        for k in range(1,n+1):
            j=order[k%n]
            eq(j,max(range(n),key=lambda i:b[i]))
            b=project(b,j)
            eq(sum(b),Q(1))
        eq(a,b)
        orbits.add(tuple(tuple(target(d,order)) for _ in range(1)))
    eq(len(orbits),factorial(d))
    for _ in range(60):
        positive=list(range(1,n))
        rng.shuffle(positive)
        sizes=rng.sample(range(1,100),d)
        lam=[Q(0)]*n
        for j,s in zip(positive,sizes): lam[j]=Q(s,sum(sizes))
        eq(sum(lam),Q(1))
        for k in range(3*n):
            oldg=gap(lam)
            y,j=one_step(lam)
            eq(j is not None, True)
            eq(y,ambient_project(lam,j))
            eq(gap(y),gapstep(oldg))
            eq(sum(y),Q(1))
            lam=y
    # Tied smaller coordinates remain tied and eventually trigger a fixed point.
    for num_tied in range(2,d+1):
        sizes=[num_tied]*num_tied + list(range(num_tied+1,d+1))
        assert len(sizes)==d
        lam=[Q(0)]+[Q(t,sum(sizes)) for t in sizes]
        froze=False
        for k in range(n+1):
            new,j=one_step(lam)
            if j is None:
                eq(new,lam)
                froze=True
                break
            lam=new
        eq(froze,True)
print(f'PASS: {checks} exact-rational assertions (dimensions 3 through 7)')

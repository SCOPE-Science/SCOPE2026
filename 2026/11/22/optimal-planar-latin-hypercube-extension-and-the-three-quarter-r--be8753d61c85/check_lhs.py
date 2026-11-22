#!/usr/bin/env python3
"""Reproducibility checks for two-coordinate Latin-hypercube extension.

Uses only Python's standard library. All exact checks are separate from
Monte Carlo illustration; simulation is not a proof of asymptotics.
"""
from fractions import Fraction
from itertools import permutations, product
from collections import defaultdict
import math
import random

CHECKS=0

def check(cond, message):
    global CHECKS
    CHECKS+=1
    if not cond: raise AssertionError(message)


def collision_edges(coords, new_size):
    """Return all conflicts by occupancy in the new one-dimensional bins."""
    first={}
    edges=[]
    for i,x in enumerate(coords):
        b=(x.numerator*new_size)//x.denominator if isinstance(x,Fraction) else int(new_size*x)
        if b in first: edges.append((first[b],i))
        else:first[b]=i
    return edges


def components_optimum(n,edges_x,edges_y):
    """Exact max independent-set size of the union of two matchings."""
    neighbors=[set() for _ in range(n)]
    for a,b in edges_x+edges_y:
        assert a!=b
        neighbors[a].add(b);neighbors[b].add(a)
    check(all(len(nb)<=2 for nb in neighbors),'degree > 2')
    visited=set(); opt=0
    for v in range(n):
        if v in visited:continue
        queue=[v];visited.add(v)
        for u in queue:
            for w in neighbors[u]:
                if w not in visited:visited.add(w);queue.append(w)
        size=len(queue)
        is_cycle=(size>=3 and all(len(neighbors[u])==2 for u in queue))
        if is_cycle:
            check(size%2==0,'odd cycle')
            opt+=size//2
        else:opt+=(size+1)//2
    return opt


def brute_independence(n,edges):
    best=0
    for mask in range(1<<n):
        if all(not ((mask>>a)&1 and (mask>>b)&1) for a,b in edges):
            best=max(best,mask.bit_count())
    return best


def exact_one_coordinate_law():
    for n in range(1,10):
        noncollision=Fraction(0)
        expected_edges=Fraction(0)
        for bits in product((0,1),repeat=n):
            w=Fraction(1)
            for i,b in enumerate(bits):
                w*=Fraction(n-i,n+1) if b==0 else Fraction(i+1,n+1)
            c=sum(bits[i] and not bits[i+1] for i in range(n-1))
            expected_edges+=w*c
            if not c:noncollision+=w
        check(noncollision == Fraction(2**n*math.factorial(n),(n+1)**n),f'exact full retention n={n}')
        check(expected_edges == Fraction(n*(n-1),6*(n+1)),f'exact collision mean n={n}')


def structural_exhaustion():
    # Enumerate every pair of binary within-stratum sides and coordinate pairing,
    # on the exactly n -> n+1 grid, through n=4.
    for n in range(2,5):
        for yy in permutations(range(n)):
            for xx_bits in product((0,1), repeat=n):
                for yy_bits in product((0,1),repeat=n):
                    # New bin i for 0 and i+1 for 1. This is every positive-probability
                    # within-stratum occupancy pattern (not probabilities).
                    x=[i+xx_bits[i] for i in range(n)]
                    y=[yy[i]+yy_bits[yy[i]] for i in range(n)]
                    def ed(labels):
                        bins=defaultdict(list)
                        for i,k in enumerate(labels):bins[k].append(i)
                        check(all(len(v)<=2 for v in bins.values()),'triple occupancy')
                        return [(v[0],v[1]) for v in bins.values() if len(v)==2]
                    ex,ey=ed(x),ed(y)
                    check(len({v for e in ex for v in e})==2*len(ex),'x nonmatching')
                    check(len({v for e in ey for v in e})==2*len(ey),'y nonmatching')
                    opt=components_optimum(n,ex,ey)
                    check(opt==brute_independence(n,ex+ey),'wrong component optimum')


def general_grid_test():
    rng=random.Random(424242)
    for n in range(2,11):
        for new_size in (n+1,n+2,2*n,3*n+1):
            for _ in range(50):
                ys=list(range(n));rng.shuffle(ys)
                xx=[Fraction(i,n)+Fraction(rng.randrange(1,1000),1000*n) for i in range(n)]
                yy=[Fraction(ys[i],n)+Fraction(rng.randrange(1,1000),1000*n) for i in range(n)]
                ex,ey=collision_edges(xx,new_size),collision_edges(yy,new_size)
                check(len({v for e in ex for v in e})==2*len(ex),'x matching general')
                check(len({v for e in ey for v in e})==2*len(ey),'y matching general')
                opt=components_optimum(n,ex,ey)
                check(opt==brute_independence(n,ex+ey),'general grid optimum')


def asymptotic_sanity():
    rng=random.Random(20261116)
    n=500
    values=[]
    for _ in range(350):
        perm=list(range(n));rng.shuffle(perm)
        xx=[(i+rng.random())/n for i in range(n)]
        yy=[(perm[i]+rng.random())/n for i in range(n)]
        ex,ey=collision_edges(xx,n+1),collision_edges(yy,n+1)
        values.append(n-components_optimum(n,ex,ey))
    mean=sum(values)/(len(values)*n)
    check(abs(mean-0.25)<0.02,'Monte Carlo illustration far from 1/4')
    print(f'350 seeded draws at n=500: mean deletion proportion {mean:.5f} (illustration only)')

if __name__=='__main__':
    exact_one_coordinate_law()
    structural_exhaustion()
    general_grid_test()
    asymptotic_sanity()
    print(f'PASS {CHECKS} deterministic/exact assertions and one seeded simulation tolerance check')

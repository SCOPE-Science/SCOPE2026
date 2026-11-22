#!/usr/bin/env python3
"""Exact finite checks for threshold-entry order theorems.

No external dependencies; Python 3.10 or newer. The mathematical proofs
for arbitrary n are in RESULT.md; these tests do not replace those proofs.
"""
from fractions import Fraction
from itertools import permutations, combinations
from math import comb
from random import Random
from pathlib import Path
import csv


def closure(points, indices):
    if not indices:
        return frozenset()
    xmax=max(points[i][0] for i in indices)
    ymax=max(points[i][1] for i in indices)
    return frozenset(i for i,(x,y) in enumerate(points) if x<=xmax and y<=ymax)


def admissible(points, order):
    prefix=set()
    for i in order:
        prefix.add(i)
        if closure(points,prefix)!=prefix:
            return False
    return True


def exact_lattice_orders(points):
    """Independently traverse every unit monotone path; distinct coordinates."""
    n=len(points)
    limit=max(max(x,y) for x,y in points)+1
    out=set()
    for east_positions in combinations(range(2*limit),limit):
        east_positions=set(east_positions)
        x=y=0
        seen=set()
        order=[]
        for step in range(2*limit):
            if step in east_positions:
                x+=1
            else:
                y+=1
            newly=[i for i,(a,b) in enumerate(points) if i not in seen and a<=x and b<=y]
            assert len(newly)<=1, (points,x,y,newly)
            if newly:
                order.extend(newly)
                seen.update(newly)
        assert len(order)==n
        out.add(tuple(order))
    return out


def all_line_orders(n):
    """Exact rational chamber enumeration for affine positive-slope lines."""
    lines=[(i,j) for i in range(1,n+1) for j in range(i+1,n+1)]
    slopes=sorted({Fraction(j-l,k-i) for (i,j) in lines for (k,l) in lines
                   if i<k and j>l})
    ws=([Fraction(1)] if not slopes else
        [slopes[0]/2]+[(a+b)/2 for a,b in zip(slopes,slopes[1:])]+[slopes[-1]+1])
    orders=set()
    for w in ws:
        zs=sorted({Fraction(j)+w*i for i,j in lines})
        cuts=([Fraction(0)] if not zs else
              [zs[0]-1]+[(a+b)/2 for a,b in zip(zs,zs[1:])]+[zs[-1]+1])
        for z in cuts:
            ts=[(max(Fraction(i),z-w*i),i) for i in range(1,n+1)]
            assert len(set(t for t,i in ts))==n
            orders.add(tuple(i-1 for t,i in sorted(ts)))
    return orders


def main():
    checked=0
    for n in range(1,9):
        points=[(i,n+1-i) for i in range(1,n+1)]
        closure_orders={p for p in permutations(range(n)) if admissible(points,p)}
        lattice_orders=exact_lattice_orders(points)
        assert closure_orders==lattice_orders, n
        assert len(closure_orders)==2**(n-1),n
        print('ANTICHAIN',n,len(closure_orders),'PASS')
        checked+=1
    rng=Random(148251)
    for n in range(2,7):
        for trial in range(9):
            ys=list(range(1,n+1))
            rng.shuffle(ys)
            points=list(zip(range(1,n+1),ys))
            by_closure={p for p in permutations(range(n)) if admissible(points,p)}
            by_paths=exact_lattice_orders(points)
            assert by_closure==by_paths,(n,ys)
            checked+=1
    print('ARBITRARY_GENERIC_GRADES',45,'PASS')
    for n in range(2,14):
        lines=all_line_orders(n)
        antichain=[(i,n+1-i) for i in range(1,n+1)]
        assert all(admissible(antichain,p) for p in lines)
        bound=1+comb(n,2)+comb(comb(n,2),2)
        assert len(lines)<=bound
        if n==6:
            assert len(lines)==30
            missing=(2,3,4,1,0,5)
            assert admissible(antichain,missing) and missing not in lines
            with (Path(__file__).parent/'LINE_WITNESSES.csv').open(newline='') as f:
                witnesses=list(csv.DictReader(f))
            witnessed=set()
            for row in witnesses:
                order=tuple(int(x)-1 for x in row['order_indices_1_based'].split())
                w=Fraction(row['w'])
                z=Fraction(row['z'])
                assert w>0
                times=[(max(Fraction(i),z-w*i),i-1) for i in range(1,7)]
                assert len(set(t for t,i in times))==6
                assert order==tuple(i for t,i in sorted(times))
                witnessed.add(order)
            assert len(witnesses)==30 and witnessed==lines
            print('LINE_WITNESSES_CSV',len(witnesses),'PASS')
        if n==13:
            assert len(lines)==638 and 2**12>bound
        checked+=1
        print('LINES',n,len(lines),'bound',bound,'PASS')
    print('TOTAL_FINITE_FAMILIES',checked,'PASS')

if __name__=='__main__':
    main()

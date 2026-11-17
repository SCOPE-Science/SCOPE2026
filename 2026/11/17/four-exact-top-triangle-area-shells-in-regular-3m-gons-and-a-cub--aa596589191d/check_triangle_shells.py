#!/usr/bin/env python3
"""Independent numerical reconstruction of the four upper area shells.

The theorem for all orders follows from the analytical proof; this program
checks complete vertex triples at a substantial finite collection of orders.
Only Python's standard library is required.
"""
from collections import defaultdict
from itertools import combinations
from math import cos, sin, pi, isclose


def area_from_coordinates(p, q, r):
    return abs((q[0]-p[0])*(r[1]-p[1])
               -(q[1]-p[1])*(r[0]-p[0]))/2


def expected(m):
    return [
        (m, m, m),
        (m-1, m, m+1),
        (m-1, m-1, m+2),
        (m-2, m+1, m+1),
    ]


def shell_area(N, gaps):
    return 2*__import__('math').prod(sin(pi*a/N) for a in gaps)


def check(N):
    m = N // 3
    pts = [(cos(2*pi*k/N), sin(2*pi*k/N)) for k in range(N)]
    shells = defaultdict(list)
    tested = 0
    for i,j,k in combinations(range(N),3):
        key = round(area_from_coordinates(pts[i],pts[j],pts[k]), 10)
        gaps = tuple(sorted((j-i,k-j,N+i-k)))
        shells[key].append(gaps)
        tested += 1
    keys = sorted(shells, reverse=True)[:4]
    assert len(keys) == 4
    shapes = expected(m)
    counts = [N//3,2*N,N,N]
    for idx, (value, shape, count) in enumerate(zip(keys, shapes, counts)):
        observed = shells[value]
        assert len(observed) == count, (N,idx,len(observed),count)
        assert set(observed) == {shape}, (N,idx,set(observed),shape)
        assert isclose(value, shell_area(N,shape), rel_tol=0, abs_tol=1.1e-10)
    theta = pi/N
    differences = [
        3*3**.5/4 - 3**.5*(.75-sin(theta)**2),
        2*cos(theta)*sin(theta)**2*(3**.5*cos(theta)-sin(theta)),
        4*cos(theta)*sin(theta)**3,
    ]
    for j in range(3):
        assert isclose(keys[j]-keys[j+1], differences[j], rel_tol=0, abs_tol=1.1e-10), (N,j,keys)
    return tested


def main():
    orders=list(range(9,85,3))
    ntriples=sum(check(n) for n in orders)
    print(f'REGULAR_TRIANGLE_FOUR_SHELL_CHECKS_PASSED orders={len(orders)} triples={ntriples} range={orders[0]}..{orders[-1]}')

if __name__ == '__main__':
    main()

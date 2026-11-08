#!/usr/bin/env python3
"""Exhaustive three-step simulation of the threshold-one Greenberg-Hastings rule.

For the triangular cactus chain with m blocks, every configuration is
enumerated for m=1,...,5.  This checker does not call the transfer code.
"""
from itertools import product


def graph(m):
    n = 2*m + 1
    neighbors = [set() for _ in range(n)]
    for j in range(1, m+1):
        tri = [j-1, j, m+j]
        for a in tri:
            for b in tri:
                if a != b:
                    neighbors[a].add(b)
    return tuple(tuple(sorted(row)) for row in neighbors)


def next_state(x, neighbors):
    updated = []
    for v, value in enumerate(x):
        if value == 0:
            updated.append(1 if any(x[w] == 1 for w in neighbors[v]) else 0)
        elif value == 1:
            updated.append(2)
        else:
            updated.append(0)
    return tuple(updated)


def expected(m):
    if m == 1:
        return 6
    if m == 2:
        return 24
    a,b=6,24
    for _ in range(3,m+1):
        a,b=b,4*b+a
    return b


def main():
    checked = 0
    for m in range(1,6):
        g = graph(m)
        fixed = periodic3 = 0
        for x in product(range(3), repeat=len(g)):
            y = next_state(x,g)
            z = next_state(y,g)
            t = next_state(z,g)
            if t == x:
                if y == x:
                    fixed += 1
                else:
                    periodic3 += 1
            checked += 1
        assert fixed == 1, (m,fixed)
        assert periodic3 == expected(m), (m,periodic3,expected(m))
        print('m=%d vertices=%d primitive3=%d fixed=%d' %(m,len(g),periodic3,fixed))
    print('PASS: exhaustive direct synchronous dynamics; total states checked=%d'%checked)


if __name__ == '__main__':
    main()

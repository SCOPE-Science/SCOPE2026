#!/usr/bin/env python3
"""Independent exact enumeration of vertices and facet incidence for two
alternating adjacent-sum path polytopes. Python standard library only.

The infinite-family classification is proved separately; finite checks are
consistency tests, not its proof.
"""
from fractions import Fraction
from itertools import product


def caps(s, d, low_first):
    return tuple(s + ((i % 2) if low_first else (1 - i % 2))
                 for i in range(d - 1))


def rank(matrix, cols):
    m = [list(map(Fraction, row)) for row in matrix]
    p = 0
    for j in range(cols):
        k = next((k for k in range(p, len(m)) if m[k][j]), None)
        if k is None:
            continue
        m[p], m[k] = m[k], m[p]
        q = m[p][j]
        m[p] = [x / q for x in m[p]]
        for k in range(p + 1, len(m)):
            if m[k][j]:
                q = m[k][j]
                m[k] = [a - q*b for a,b in zip(m[k],m[p])]
        p += 1
        if p == cols:
            break
    return p


def active(s, v, low_first):
    d = len(v)
    b = caps(s,d,low_first)
    if any(v[i] + v[i+1] > b[i] for i in range(d-1)) or any(x < 0 for x in v):
        return None
    rows = []
    for i,x in enumerate(v):
        if x == 0:
            row = [0]*d
            row[i] = 1
            rows.append(row)
    for i,c in enumerate(b):
        if v[i]+v[i+1] == c:
            row = [0]*d
            row[i] = row[i+1] = 1
            rows.append(row)
    return rows


def vertices(s,d,low_first):
    n_vertices = 0
    singular = []
    feasible = 0
    for v in product(range(s+2),repeat=d):
        rows = active(s,v,low_first)
        if rows is None:
            continue
        feasible += 1
        if len(rows)<d or rank(rows,d)!=d:
            continue
        n_vertices += 1
        if len(rows)>d:
            singular.append((v,len(rows)))
    return n_vertices,singular,feasible


def staircase(s):
    v = []
    for k in range(s+1):
        v.extend((k,s-k))
    return tuple(v)


def main():
    tests = 0
    points = 0
    for s in (2,3):
        q = staircase(s)
        for low_first in (True,False):
            wall = 2*s+2 if low_first else 2*s+3
            expected = [(q,wall+1)] if low_first else [((0,)+q,wall+1),((s+1,)+q,wall+1)]
            for d in range(2,wall+1):
                count, singular, feasible = vertices(s,d,low_first)
                points += feasible
                tests += 1
                if d<wall:
                    assert not singular, (s,d,low_first,singular)
                else:
                    assert sorted(singular)==sorted(expected),(s,d,low_first,singular,expected)
                print('s=%d, d=%d, low_first=%s, vertices=%d, nonsimple=%d, feasible_lattice_points=%d' %
                      (s,d,low_first,count,len(singular),feasible))
    for s in range(2,21):
        q=staircase(s)
        for low_first in (True,False):
            wall=2*s+2 if low_first else 2*s+3
            witnesses=[q] if low_first else [(0,)+q,(s+1,)+q]
            for v in witnesses:
                rows=active(s,v,low_first)
                assert len(v)==wall and rows is not None and len(rows)==wall+1
                assert rank(rows,wall)==wall
    print('CHECK_OK cases=%d feasible_points=%d witnesses=%d' % (tests,points,19*3))

if __name__=='__main__':
    main()

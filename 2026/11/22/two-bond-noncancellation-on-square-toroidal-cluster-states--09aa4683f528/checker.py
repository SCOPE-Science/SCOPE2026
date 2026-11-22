"""Exact binary-rank checks for two omitted edges of square torus graph states.

Run: python checker.py
Only the Python standard library is needed.
"""
from collections import Counter
from itertools import combinations
from random import Random


def binary_rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def grid(m):
    n = 2 * m
    even = [(x, y) for x in range(n) for y in range(n) if (x + y) % 2 == 0]
    odd = [(x, y) for x in range(n) for y in range(n) if (x + y) % 2 == 1]
    index = {site: j for j, site in enumerate(even)}
    rows = []
    for x, y in odd:
        sites = [((x + 1) % n, y), ((x - 1) % n, y),
                 (x, (y + 1) % n), (x, (y - 1) % n)]
        assert len(set(sites)) == 4
        rows.append(sum(1 << index[s] for s in sites))
    edges = [(i, j) for i, row in enumerate(rows)
             for j in range(len(even)) if row & (1 << j)]
    return rows, edges


def rank_after(rows, edges):
    altered = list(rows)
    for i, j in edges:
        assert altered[i] & (1 << j)
        altered[i] ^= 1 << j
    return binary_rank(altered)


def run():
    rng = Random(32685)
    tested = 0
    for m in range(2, 9):
        rows, edges = grid(m)
        base = binary_rank(rows)
        expected = 2 * m * m - 2 * m
        assert base == expected, (m, base, expected)
        for e in edges:
            assert rank_after(rows, [e]) == base + 1
        counts = Counter()
        candidates = list(combinations(range(len(edges)), 2))
        if m >= 6:
            rng.shuffle(candidates)
            candidates = candidates[:1800]
        for a, b in candidates:
            e, f = edges[a], edges[b]
            gain = 1 if e[0] == f[0] or e[1] == f[1] else 2
            got = rank_after(rows, [e, f]) - base
            assert got == gain, (m, e, f, got, gain)
            counts[gain] += 1
        tested += len(candidates)
        print('m=%d: matrix=%d, base=%d, edges=%d, pairs=%d, gains=%s' %
              (m, len(rows), base, len(edges), len(candidates), dict(counts)))
    # A sharp boundary: the non-square 4-by-6 periodic grid admits
    # disjoint missing edges whose combined rank gain vanishes.
    nx, ny = 4, 6
    even = [(x, y) for x in range(nx) for y in range(ny) if (x+y)%2==0]
    odd = [(x, y) for x in range(nx) for y in range(ny) if (x+y)%2==1]
    EI = {v:i for i,v in enumerate(even)}
    OI = {v:i for i,v in enumerate(odd)}
    rectangles = []
    for x,y in odd:
        z=[((x+1)%nx,y),((x-1)%nx,y),(x,(y+1)%ny),(x,(y-1)%ny)]
        rectangles.append(sum(1 << EI[t] for t in z))
    e1=(OI[(0,1)],EI[(0,0)])
    e2=(OI[(0,3)],EI[(0,4)])
    assert e1[0]!=e2[0] and e1[1]!=e2[1]
    assert binary_rank(rectangles)==10
    assert rank_after(rectangles,[e1])==11
    assert rank_after(rectangles,[e2])==11
    assert rank_after(rectangles,[e1,e2])==10
    print('4-by-6 boundary: disjoint singles gain one each; pair gains zero')
    print('PASS: %d exact two-edge square-torus rank comparisons' % tested)


if __name__ == '__main__':
    run()

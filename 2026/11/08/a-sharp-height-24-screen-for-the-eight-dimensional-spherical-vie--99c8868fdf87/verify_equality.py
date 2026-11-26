"""Clipped-quadratic exact threshold census for eight speeds capped at 24."""
from fractions import Fraction as F
from itertools import combinations_with_replacement as tuples, islice
from math import comb
import sys
import numpy as np

edges = sorted({F(0), F(1, 2)} | {F(k, a) for a in range(1, 25) for k in range(1, (a+1)//2)})
cells = []
for l, r in zip(edges, edges[1:]):
    mid = (l+r)/2
    centers = np.array([2*(a*mid//1)+1 for a in range(25)], dtype=np.int64)
    cells.append((l, r, centers*np.arange(25, dtype=np.int64), centers**2))
assert len(cells) == 90
cells.sort(key=lambda cell: abs((cell[0]+cell[1])/2-F(1, 6)))


def score(v, q, cell):
    l, r, bs, cs = cell
    b, c = bs[v].sum(axis=1), cs[v].sum(axis=1)
    ln, ld, rn, rd = l.numerator, l.denominator, r.numerator, r.denominator
    left, right = b*ld < 2*q*ln, b*rd > 2*q*rn
    n, d = np.where(left, ln, rn), np.where(left, ld, rd)
    end = left | right
    return (np.where(end, 4*q*n*n - 4*b*n*d + c*d*d, q*c-b*b),
            np.where(end, 4*d*d, 4*q))


def census(lo, hi):
    assert 1 <= lo <= hi <= 24
    w = (1, 2, 3, 4, 5, 7, 9, 11)
    expected = {11: [(w, '8/17')], 22: [(tuple(2*x for x in w), '8/17')]}
    total = 0
    for h in range(lo, hi+1):
        it = tuples(range(1, h+1), 7)
        count, finals = 0, []
        while True:
            block = list(islice(it, 50000))
            if not block:
                break
            count += len(block)
            v = np.full((len(block), 8), h, dtype=np.int16)
            v[:, :7] = block
            q = (v*v).sum(axis=1, dtype=np.int64)
            for cell in cells:
                n, d = score(v, q, cell)
                keep = 17*n >= 8*d
                v, q = v[keep], q[keep]
                if not len(v):
                    break
            for u, q_u in zip(v, q):
                trial = (score(u[None, :], np.array([q_u]), cell) for cell in cells)
                best = min(F(int(n[0]), int(d[0])) for n, d in trial)
                finals.append((tuple(map(int, u)), str(best)))
        assert count == comb(h+6, 7)
        assert finals == expected.get(h, []), (h, finals)
        total += count
        print(f'height={h:2d} tuples={count:7d} survivors={finals}', flush=True)
    assert total == comb(hi+7, 8) - comb(lo+6, 8)
    print(f'cells={len(cells)} total={total}', flush=True)


if __name__ == '__main__':
    census(*map(int, sys.argv[1:]))

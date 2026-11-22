"""Exact finite checks for Euclidean chord counts of alternating shard polytopes.

Run with Python 3: python verify.py
All computations in the finite checks use integer arithmetic.
"""
from collections import Counter
from math import comb


def vertices(r):
    """Enumerate matching supports as bit masks, independently of a transfer matrix."""
    out = []
    def rec(pos, open_pair, mask):
        if pos == 2*r:
            if open_pair == 0:
                out.append(mask)
            return
        rec(pos+1, open_pair, mask)
        if pos % 2 == 0 and not open_pair:
            rec(pos+1, 1, mask | (1 << pos))
        elif pos % 2 == 1 and open_pair:
            rec(pos+1, 0, mask | (1 << pos))
    rec(0, 0, 0)
    return out


def add(x, y):
    z = x[:]
    for i, a in enumerate(y):
        if i < len(z):
            z[i] += a
        else:
            z.append(a)
    return z


def scale_shift(x, c, k):
    return [0]*k + [c*a for a in x]


def sub(x, y):
    return add(x, [-v for v in y])


def recurrence_values(maxr):
    w = [[1], [2, 2], [5, 16, 4]]
    for r in range(3, maxr+1):
        a = add(scale_shift(w[-1], 4, 0), scale_shift(w[-1], 4, 1))
        b = add(scale_shift(w[-2], -4, 0), scale_shift(w[-2], -4, 2))
        w.append(add(add(a, b), w[-3]))
    return w[:maxr+1]


def fibonacci(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a


def main():
    ww=recurrence_values(16)
    checked=0
    for r in range(1,8):
        verts=vertices(r)
        assert len(verts)==len(set(verts))==fibonacci(2*r+1)
        count=Counter((u ^ v).bit_count()//2 for u in verts for v in verts)
        assert all((u ^ v).bit_count()%2 == 0 for u in verts for v in verts)
        assert [count[k] for k in range(r+1)]==ww[r]
        assert count[0]==len(verts)
        assert count[r]==2**r
        if r>=2: assert count[r-1]==r*r*2**r
        assert sum(count.values())==len(verts)**2
        checked+=len(verts)**2
    for r in range(8,17):
        assert sum(ww[r])==fibonacci(2*r+1)**2
        assert ww[r][-1]==2**r and ww[r][-2]==r*r*2**r
        assert ww[r][0]==fibonacci(2*r+1)
    print(f'ALTERNATING_SHARD_CHORD_PASS checked_ordered_pairs={checked} max_r=16')


if __name__=='__main__':main()

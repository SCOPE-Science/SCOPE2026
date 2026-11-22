#!/usr/bin/env python3
"""Independent recomputation of interval-graph Walsh parity recovery."""
import itertools
import random


def independent_masks(edges, n):
    return [m for m in range(1 << n)
            if all(not ((m >> i) & 1 and (m >> j) & 1) for i, j in edges)]


def interval_data(intervals):
    n = len(intervals)
    ordering = sorted(range(n), key=lambda i: (intervals[i][1], intervals[i][0], i))
    a = [intervals[i] for i in ordering]
    pred = [sum(a[j][1] < a[i][0] for j in range(i)) for i in range(n)]
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)
             if max(a[i][0], a[j][0]) <= min(a[i][1], a[j][1])]
    return a, pred, edges


def greedy(pred):
    val = [1]; signs = []
    for i, k in enumerate(pred, 1):
        left, right = val[i - 1], val[k]
        s = -1 if left * right > 0 else 1
        val.append(left + s * right)
        signs.append(s)
        assert abs(val[-1]) <= 1
    return signs, val


def signed_direct(masks, signs):
    neg = sum((1 << i) for i, s in enumerate(signs) if s == -1)
    return sum(1 - 2 * ((m & neg).bit_count() % 2) for m in masks)


def test(intervals, brute_all=False):
    _, pred, edges = interval_data(intervals)
    signs, val = greedy(pred)
    masks = independent_masks(edges, len(intervals))
    assert signed_direct(masks, signs) == val[-1]
    assert val[-1] % 2 == len(masks) % 2
    assert abs(val[-1]) == len(masks) % 2
    if brute_all:
        vals = [signed_direct(masks, s) for s in itertools.product([1,-1],repeat=len(intervals))]
        assert (0 not in vals) == (len(masks)%2 == 1)
        assert min(map(abs, vals)) == len(masks)%2
    return 1


def octahedron():
    n = 6
    edges = [(i, j) for i in range(n) for j in range(i+1,n)
             if {i,j} not in ({0,1}, {2,3}, {4,5})]
    masks = independent_masks(edges,n)
    assert len(masks)==10
    vals = [signed_direct(masks,s) for s in itertools.product([1,-1], repeat=n)]
    levels = {v: vals.count(v) for v in sorted(set(vals))}
    assert levels == {-2:27,2:27,6:9,10:1},levels
    return levels


def run():
    R=random.Random(27112026); checks=0
    for n in range(0,10):
        for trial in range(60):
            z=[(a,a+R.randrange(0,8)) for a in (R.randrange(0,20) for _ in range(n))]
            checks += test(z,brute_all=n<=7)
    for h in range(0,9):
        for n in range(1,45):
            pred=[max(0,i-h-1) for i in range(1,n+1)]
            signs,values=greedy(pred)
            cnt=[1]
            for i,k in enumerate(pred,1):cnt.append(cnt[i-1]+cnt[k])
            assert abs(values[-1]) == cnt[-1]%2
            checks += 1
    print('PASS: interval examples and path powers:',checks)
    print('PASS: octahedral obstruction:',octahedron())

if __name__=='__main__':run()

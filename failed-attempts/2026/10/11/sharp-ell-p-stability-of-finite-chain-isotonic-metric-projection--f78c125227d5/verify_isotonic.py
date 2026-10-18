#!/usr/bin/env python3
"""Finite numerical checks for the sharp norm of unweighted isotonic best approximation.

The published mathematical argument, not these tests, establishes all dimensions.
No third-party packages are needed.
"""
import math
import random


def pmean(p, xs):
    lo, hi = min(xs), max(xs)
    if hi == lo:
        return lo
    for _ in range(120):
        mid = (lo + hi) / 2
        s = sum(math.copysign(abs(x-mid)**(p-1), x-mid) if x != mid else 0. for x in xs)
        if s > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def iso(p, xs):
    blocks = [[i] for i in range(len(xs))]
    k = 0
    while k < len(blocks)-1:
        if pmean(p, [xs[i] for i in blocks[k]]) > pmean(p, [xs[i] for i in blocks[k+1]]):
            blocks[k].extend(blocks.pop(k+1))
            k = max(0, k-1)
        else:
            k += 1
    out = [0.0]*len(xs)
    for b in blocks:
        mean = pmean(p, [xs[i] for i in b])
        for i in b:
            out[i] = mean
    return out


def norm(p, v):
    return sum(abs(x)**p for x in v)**(1/p)


def theoretical(n, p):
    if n <= 2 or p == 2:
        return 1.
    if p < 2:
        return n**(1/p)
    return (n/2)**(1/p)


def sharp_test(n, p, h):
    if p < 2:
        c = sum(j**(p-1) for j in range(1, n-1))**(-1/(p-1))
        x = [1., 0.] + [-j*c for j in range(1,n-1)]
        step = [0., 1.] + [0.]*(n-2)
    else:
        x = [1.] + [0.]*(n-2) + [-1.]
        step = [1.] + [0.]*(n-2) + [1.]
    base = iso(p, x)
    moved = iso(p, [a+h*d for a,d in zip(x,step)])
    return norm(p,[u-v for u,v in zip(moved,base)])/(h*norm(p,step))


def main():
    random.seed(119)
    tests=0
    for n in (1,2,3,5,8):
        for p in (1.25,1.5,2.,3.,4.,7.):
            L=theoretical(n,p)
            for _ in range(20):
                x=[random.uniform(-5,5) for i in range(n)]
                y=[random.uniform(-5,5) for i in range(n)]
                ratio=norm(p,[a-b for a,b in zip(iso(p,x),iso(p,y))])/norm(p,[a-b for a,b in zip(x,y)])
                assert ratio <= L+1e-8, (n,p,ratio,L)
                tests += 1
            if n>=3 and p!=2:
                r=sharp_test(n,p,1.e-5 if p>2 else 1.e-7)
                assert r <= L+1e-7, (n,p,r,L)
                assert r >= L-0.03, (n,p,r,L)
                tests += 1
    print('ISOTONIC_LP_SHARP_NORM_FINITE_CHECK_OK',tests)

if __name__=='__main__':
    main()

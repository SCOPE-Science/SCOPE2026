#!/usr/bin/env python3
"""Exact integer checks of finite generalized-theta forest Fourier identities.

The mathematical all-parameter argument is in RESULT.md; these tests are corroboration.
No external dependencies or files are required.
"""
from math import comb


def amplitudes(lengths):
    k = len(lengths)
    n = sum(lengths)
    masks = []
    off = 0
    for ell in lengths:
        masks.append(((1 << ell) - 1) << off)
        off += ell
    a = [0] * (1 << n)
    for x in range(1 << n):
        complete = 0
        for mask in masks:
            complete += (x & mask) == mask
            if complete > 1:
                break
        a[x] = complete <= 1
    return a, masks


def walsh(a):
    h = list(a)
    n = len(h)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = h[j], h[j + step]
                h[j], h[j + step] = u + v, u - v
        step *= 2
    return h


def closed_multiplier(x, masks):
    k = len(masks)
    ds = []
    sign = 1
    for m in masks:
        if x & m:
            sign *= -1 if ((x & m).bit_count() + 1) % 2 else 1
        else:
            ds.append((1 << m.bit_count()) - 1)
    z = len(ds)
    p = 1
    for d in ds:
        p *= d
    return sign * ((1 - k + z) * p + sum(p // d for d in ds))


def run():
    tests = [(2, 3, 2), (2, 2, 2, 2), (2, 2, 2, 2, 2),
             (2, 2, 2, 3, 3), (2, 2, 2, 2, 2, 2, 2),
             (2, 2, 2, 2, 2, 2, 2, 2, 2)]
    total = 0
    for lengths in tests:
        k = len(lengths)
        a, masks = amplitudes(lengths)
        H = walsh(a)
        for freq, value in enumerate(H):
            predicted = closed_multiplier(freq, masks)
            assert value == predicted, (lengths, freq, value, predicted)
            assert value % 4 == ((-1 if ((freq.bit_count() + k) & 1) else 1) * (1 - k)) % 4
            if k % 4 != 1:
                assert value != 0
            total += 1
        nzero = sum(w == 0 for w in H)
        if lengths == (2,)*5:
            assert nzero == comb(5, 3) * 3**2 == 90
        if lengths == (2, 2, 2, 3, 3):
            assert nzero == 7**2 == 49
        if lengths == (2,)*9:
            assert nzero == comb(9, 6)*3**3 == 2268
        print('lengths=',lengths,'edges=',sum(lengths),'forests=',sum(a),
              'nullity=',nzero,'rank=',len(H)-nzero)
    print('PASS:',total,'individual exact Fourier comparisons and congruence checks')


if __name__ == '__main__':
    run()

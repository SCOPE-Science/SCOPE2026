#!/usr/bin/env python3
"""Exact integer finite verifier for singleton-free partition arc incidence Fourier claims.
Requires NumPy for integer butterfly vectorization; there are no floats.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
import numpy as np


def partitions(n):
    out = [()]
    for v in range(1, n + 1):
        nxt = []
        for blocks in out:
            nxt.append(blocks + ((v,),))
            for i in range(len(blocks)):
                q = list(blocks)
                q[i] = blocks[i] + (v,)
                nxt.append(tuple(q))
        out = nxt
    return out


def setup(n):
    edges = tuple((i, j) for j in range(2, n + 1) for i in range(1, j))
    index = {e: k for k, e in enumerate(edges)}
    masks = []
    for blocks in partitions(n):
        if any(len(b) == 1 for b in blocks):
            continue
        m = 0
        for b in blocks:
            for e in zip(b, b[1:]):
                m |= 1 << index[e]
        masks.append(m)
    return edges, index, masks


def rook_enumeration(n, edges):
    """Independent enumeration: nonattacking upper-triangular rooks with no isolated node."""
    all_masks = set()
    def rec(k, left, right, selected):
        if k == len(edges):
            if (left | right) & (((1 << (n + 1)) - 1) ^ 1) == (((1 << (n + 1)) - 1) ^ 1):
                all_masks.add(selected)
            return
        i, j = edges[k]
        rec(k + 1, left, right, selected)
        if not ((left >> i) & 1 or (right >> j) & 1):
            rec(k + 1, left | (1 << i), right | (1 << j), selected | (1 << k))
    rec(0, 0, 0, 0)
    return all_masks


def transform(a):
    a = a.copy()
    step = 1
    while step < len(a):
        v = a.reshape(-1, 2*step)
        left, right = v[:, :step].copy(), v[:, step:].copy()
        v[:, :step] = left + right
        v[:, step:] = left - right
        step *= 2
    return a


def scalar_signed_sum(masks, s):
    return sum(1 if ((m & s).bit_count() % 2 == 0) else -1 for m in masks)


def verify():
    counts = {3:(1,0),4:(4,24),5:(11,0),6:(41,0),7:(162,157808)}
    for n, (count, zeros) in counts.items():
        edges, idx, ms = setup(n)
        assert len(ms) == count and len(set(ms)) == count
        if n == 7:
            assert set(ms) == rook_enumeration(n, edges)
        size = 1 << len(edges)
        a = np.zeros(size, dtype=np.int64)
        a[ms] = 1
        signed = transform(a)
        assert int(np.count_nonzero(signed == 0)) == zeros
        assert signed[0] == count
        assert int(np.dot(signed, signed)) == size*count
        if n == 7:
            assert int(np.max(np.abs(signed))) == 162
            assert int(np.min(np.abs(signed[signed != 0]))) == 2
            assert int(np.count_nonzero(signed)) == 1939344
            by_degree = [0] * (len(edges)+1)
            first_zeros=[]
            for s in range(size):
                if signed[s] == 0:
                    d=s.bit_count()
                    by_degree[d]+=1
                    if d==3: first_zeros.append(s)
            expected_by_degree=[0,0,0,19,227,997,3079,7304,13883,21423,26413,27570,23576,17005,9864,4506,1575,340,27,0,0,0]
            assert by_degree == expected_by_degree
            assert len(first_zeros)==19
            example= sum(1 << idx[e] for e in ((1,2),(1,3),(3,4)))
            assert example in first_zeros
            assert Counter((m & example).bit_count() for m in ms) == {0:51, 1:81, 2:30}
            for s in [0, 1, 3, example, size-1, 56789, 1048575]:
                assert signed[s] == scalar_signed_sum(ms, s)
            for s in first_zeros:
                assert scalar_signed_sum(ms, s) == 0
            p = (signed != 0).astype(np.int64)
            kernel_num = transform(p)
            assert kernel_num[0] == 1939344
            assert np.count_nonzero(kernel_num) == 521828
            abs_total = int(np.abs(kernel_num).sum())
            assert abs_total == 298503520
            assert Fraction(abs_total,size) == Fraction(9328235,65536)
            assert int(np.dot(kernel_num,kernel_num)) == size*1939344
            # Fourier inversion: kernel_num is the integer numerator of 2^(-21) cutoff kernel.
            assert np.array_equal(transform(kernel_num),size*p)
            print('n7 first 19 cubic zeros:', [tuple(edges[i] for i in range(len(edges)) if (s>>i)&1) for s in first_zeros])
            print('n7 rank 1939344 nullity 157808 gap 2; endpoint 9328235/65536; support 521828')
        print('verified order', n, 'count',count,'zeros',zeros)
    print('PASS')

if __name__=='__main__':
    verify()

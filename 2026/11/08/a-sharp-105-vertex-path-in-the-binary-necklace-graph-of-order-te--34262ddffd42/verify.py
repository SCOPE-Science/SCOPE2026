#!/usr/bin/env python3
"""Standalone verification of a 105-class binary necklace-graph path."""
from pathlib import Path
from collections import Counter

N = 10

def rotations(w):
    return [w[k:] + w[:k] for k in range(len(w))]

def canonical(w):
    return min(rotations(w))

def adjacent(a, b):
    return any(sum(x != y for x,y in zip(a,r)) == 1 for r in rotations(b))

def verify(path):
    all_words = (format(i, f'0{N}b') for i in range(2**N))
    classes = {canonical(w) for w in all_words}
    even = {w for w in classes if w.count('1') % 2 == 0}
    odd = classes - even
    assert (len(classes), len(even), len(odd)) == (108, 56, 52)
    seq = path.read_text(encoding='utf-8').splitlines()
    assert len(seq) == 105
    assert len(set(seq)) == len(seq)
    assert all(len(w) == N and set(w) <= {'0', '1'} for w in seq)
    assert all(w == canonical(w) for w in seq)
    assert set(seq) <= classes
    assert all(adjacent(a, b) for a, b in zip(seq, seq[1:]))
    assert seq[0] == '0'*N and seq[-1] == '1'*N
    assert all(a.count('1')%2 != b.count('1')%2 for a,b in zip(seq,seq[1:]))
    assert len(odd & set(seq)) == 52
    assert len(even & set(seq)) == 53
    omitted = sorted(classes - set(seq))
    assert omitted == ['0001101001', '0011110101', '0110111111'], omitted
    # Bipartite upper bound: all edges switch Hamming-weight parity.
    assert len(seq) == 2 * min(len(even),len(odd)) + 1
    print('CERTIFICATE_VALIDATED classes=108 even=56 odd=52 path=105 edges=104')
    print('OMITTED', ','.join(omitted))

if __name__ == '__main__':
    verify(Path(__file__).with_name('CERTIFICATE.txt'))

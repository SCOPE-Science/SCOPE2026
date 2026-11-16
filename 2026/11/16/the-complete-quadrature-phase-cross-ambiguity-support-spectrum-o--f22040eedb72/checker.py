#!/usr/bin/env python3
"""Exact Gaussian-integer census of C4 cross-Gabor supports.
Pure standard-library Python; no numerical floating point.
"""
from collections import Counter
from itertools import product

ROOTS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def mul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def conj(a):
    return (a[0], -a[1])

def add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def neg(a):
    return (-a[0], -a[1])

def direct(f, g):
    nonzero = 0
    for shift in range(4):
        for freq in range(4):
            accum = (0, 0)
            for t in range(4):
                x = mul(f[t], conj(g[(t-shift) % 4]))
                x = mul(x, ROOTS[(-freq*t) % 4])
                accum = add(accum, x)
            nonzero += accum != (0, 0)
    return nonzero

def factored(f, g):
    nonzero = 0
    for shift in range(4):
        a, b, c, d = (mul(f[t], conj(g[(t-shift) % 4])) for t in range(4))
        u = add(a, c)
        v = add(b, d)
        left = add(a, neg(c))
        right = add(d, neg(b))
        spect = (add(u, v), add(u, neg(v)),
                 add(left, mul(ROOTS[1], right)),
                 add(left, neg(mul(ROOTS[1], right))))
        nonzero += sum(x != (0, 0) for x in spect)
    return nonzero

def census(phases):
    cnt = Counter()
    profiles = Counter()
    examples = {}
    one = ROOTS[0]
    for aa in product(phases, repeat=3):
        f = (one,) + tuple(ROOTS[j] for j in aa)
        for bb in product(phases, repeat=3):
            g = (one,) + tuple(ROOTS[j] for j in bb)
            a = direct(f, g)
            b = factored(f, g)
            assert a == b, ('independent computation mismatch', aa, bb, a, b)
            cnt[a] += 1
            row_sizes = []
            for shift in range(4):
                h = tuple(mul(f[t], conj(g[(t-shift) % 4])) for t in range(4))
                nz = 0
                for freq in range(4):
                    z = (0, 0)
                    for t in range(4):
                        z = add(z, mul(h[t], ROOTS[(-freq*t) % 4]))
                    nz += (z != (0, 0))
                row_sizes.append(nz)
            assert sum(row_sizes) == a
            profiles[(a, tuple(sorted(row_sizes)))] += 1
            examples.setdefault(a, (aa, bb))
    return dict(sorted(cnt.items())), dict(sorted(profiles.items())), examples

if __name__ == '__main__':
    binary, binary_profiles, ex2 = census((0, 2))
    qpsk, qpsk_profiles, ex4 = census((0, 1, 2, 3))
    assert binary == {4: 8, 6: 16, 8: 8, 16: 32}, binary
    assert qpsk == {4: 32, 6: 64, 8: 32, 11: 768, 12: 1024, 16: 2176}, qpsk
    assert qpsk_profiles == {
        (4,(1,1,1,1)):32, (6,(1,1,2,2)):64,
        (8,(2,2,2,2)):32,
        (11,(1,2,4,4)):256, (11,(1,3,3,4)):512,
        (12,(2,3,3,4)):512, (12,(3,3,3,3)):512,
        (16,(4,4,4,4)):2176}, qpsk_profiles
    assert sum(binary.values()) == 2**6
    assert sum(qpsk.values()) == 4**6
    print('BPSK:', binary)
    print('QPSK:', qpsk)
    print('QPSK shift-profile census:', qpsk_profiles)
    print('QPSK witnesses (exponents f[1:], g[1:]):', ex4)
    print('PASS: two exact algorithms, complete normalized domains, checked totals')

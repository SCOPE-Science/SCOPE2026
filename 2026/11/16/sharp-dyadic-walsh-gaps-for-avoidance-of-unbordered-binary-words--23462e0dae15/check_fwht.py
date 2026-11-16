#!/usr/bin/env python3
"""Exact Walsh checks for unbordered single-factor avoidance; Python 3 standard library."""
from math import gcd

def unbordered(w):
    return all(w[:d] != w[-d:] for d in range(1, len(w)))

def spectrum(w, n):
    size = 1 << n
    a = [int(w not in format(x, '0%db' % n)) for x in range(size)]
    count = sum(a)
    stride = 1
    while stride < size:
        for base in range(0, size, 2 * stride):
            for j in range(stride):
                u, v = a[base + j], a[base + j + stride]
                a[base + j], a[base + j + stride] = u + v, u - v
        stride *= 2
    assert sum(v*v for v in a) == size * count
    return a

def main():
    tested = 0
    for k in range(2, 7):
        for code in range(1 << k):
            w = format(code, '0%db' % k)
            if not unbordered(w):
                continue
            for n in range(1, 13):
                values = spectrum(w, n)
                gap = 1 << (n % k)
                nonzero = [abs(v) for v in values if v]
                assert min(nonzero) == gap, (w, n, gap, min(nonzero))
                assert all(v % gap == 0 for v in values)
                assert gcd(*values) == gap
                if n % k == 0:
                    assert all(v & 1 for v in values)
                if n % k == 1:
                    assert sum(1 for v in values if (v//gap) & 1) == (1 << (n-1))
                tested += 1
    # A bordered pattern fails the universal gap already at length three.
    assert min(abs(v) for v in spectrum('11', 3) if v) == 1
    print('FWHT_OK: %d complete spectra, all divisibility/gap/parity tests passed' % tested)

if __name__ == '__main__':
    main()

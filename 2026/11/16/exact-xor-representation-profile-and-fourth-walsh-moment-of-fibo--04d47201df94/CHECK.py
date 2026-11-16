#!/usr/bin/env python3
"""Reproduce exact convolution and fourth Walsh moment for Fibonacci cubes.

No external dependencies. Run: python3 CHECK.py
"""
from collections import Counter


def fib(j):
    a, b = 0, 1
    for _ in range(j):
        a, b = b, a + b
    return a


def xor_profile_formula(mask, n):
    bits = tuple((mask >> k) & 1 for k in range(n))
    one_runs = sum(bit and (i == 0 or not bits[i-1]) for i, bit in enumerate(bits))
    product = 1 << one_runs
    i = 0
    while i < n:
        if bits[i]:
            i += 1
            continue
        j = i
        while j < n and not bits[j]:
            j += 1
        free = max(0, j - i - int(i > 0) - int(j < n))
        product *= fib(free + 2)
        i = j
    return product


def fwt(values):
    arr = list(values)
    h = 1
    while h < len(arr):
        for i in range(0, len(arr), 2*h):
            for j in range(i, i+h):
                a, b = arr[j], arr[j+h]
                arr[j], arr[j+h] = a+b, a-b
        h <<= 1
    return arr


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def energy_transfer(n):
    if n == 0:
        return 1
    B = ((1, 6, 1), (1, 1, 0), (1, 0, 0))
    vector = [1, 1, 1]
    for _ in range(n-1):
        vector = [sum(B[i][j]*vector[j] for j in range(3)) for i in range(3)]
    return vector[0] + 6*vector[1] + vector[2]


def main():
    B = [[1,6,1], [1,1,0], [1,0,0]]
    square = matmul(B, B)
    cube = matmul(square, B)
    for i in range(3):
        for j in range(3):
            assert cube[i][j] - 2*square[i][j] - 6*B[i][j] + (i==j) == 0
    energies = [energy_transfer(n) for n in range(19)]
    assert energies[:7] == [1,8,21,89,296,1105,3897]
    for n in range(3, len(energies)):
        assert energies[n] == 2*energies[n-1] + 6*energies[n-2] - energies[n-3]
    for n in range(1, 14):
        eligible = [x for x in range(1 << n) if (x & (x >> 1)) == 0]
        conv = Counter(a ^ b for a in eligible for b in eligible)
        assert len(conv) == (1 << n)
        assert sum(conv.values()) == len(eligible)**2
        assert len(eligible) == fib(n+2)
        for x in range(1 << n):
            assert conv[x] == xor_profile_formula(x, n), (n, x, conv[x], xor_profile_formula(x,n))
        assert min(conv.values()) == 2
        assert max(conv.values()) == fib(n+2)
        if n >= 2:
            assert {x for x in conv if conv[x] == fib(n+2)} == {0}
        assert sum(k*k for k in conv.values()) == energies[n]
        if n <= 12:
            char = fwt([int(x in eligible) for x in range(1 << n)])
            assert sum(v**4 for v in char) == (1 << n)*energies[n]
            assert sum(v*v for v in char) == (1 << n)*len(eligible)
        print(f'n={n}: |A|={len(eligible)}, energy={energies[n]}, profile, extrema, and Fourier checks pass')
    print('FIBONACCI_XOR_PROFILE_AND_FOURTH_MOMENT_PASS')


if __name__ == '__main__':
    main()

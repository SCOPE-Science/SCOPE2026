#!/usr/bin/env python3
"""Exact finite verification of the explicitly stated polynomial and its modular factorization."""
from collections import Counter


def mul(a, b, m):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % m
    return out


def linear_product(modulus):
    coeffs = [1]
    for sign, exponent in [(-1, 112), (1, 143)]:
        for _ in range(exponent):
            coeffs = mul(coeffs, [sign % modulus, 1], modulus)
    return coeffs


def stretch(a, factor):
    out = [0] * ((len(a) - 1) * factor + 1)
    for i, x in enumerate(a):
        out[factor * i] = x
    return out


def main():
    c = linear_product(10)
    assert len(c) == 256
    assert all(x in (1, 3, 7, 9) for x in c)
    histogram = Counter(c)
    assert histogram == Counter({1: 74, 3: 102, 7: 20, 9: 60})
    assert linear_product(2) == [1] * 256

    p = 5
    a = mul(mul([p-1, 1], [p-1, 1], p), mul(mul([1, 1], [1, 1], p), [1, 1], p), p)
    b = [1, 1, 1, 1, 1]
    assert a == [1, 1, 3, 3, 1, 1]
    h = mul(a, stretch(a, 5), p)
    assert len(h) == 31 and all(h)
    assert h[:6] == [1, 1, 3, 3, 1, 2]
    assert h[-6:] == [2, 1, 3, 3, 1, 1]
    assert [(x + y) % 5 for x, y in zip(h[:6], h[-6:])] == [3, 2, 1, 1, 2, 3]
    g = mul(h, stretch(b, 25), p)
    assert len(g) == 131 and all(g)
    f = mul(g, [1] + [0] * 124 + [1], p)
    assert len(f) == 256 and all(f)
    assert f == linear_product(5)
    assert f == [x % 5 for x in c]
    print('VERIFY_OK degree=255 coefficients=256')
    print('residue_histogram_mod10=' + str(dict(sorted(histogram.items()))))
    print('Frobenius_factorization_mod5=PASS; parity_mod2=PASS')


if __name__ == '__main__':
    main()

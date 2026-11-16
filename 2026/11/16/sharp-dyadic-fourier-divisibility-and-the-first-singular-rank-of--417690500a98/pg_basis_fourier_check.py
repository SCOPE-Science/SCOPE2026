#!/usr/bin/env python3
"""Exact finite checks for binary projective-base Walsh congruences.

Run: python3 pg_basis_fourier_check.py
Only the Python standard library is required.
"""
from itertools import combinations
from collections import Counter
from math import factorial, prod, gcd, comb


def independent(points):
    pivots = [0] * 32
    rank = 0
    for v in points:
        x = v
        while x:
            h = x.bit_length() - 1
            if not pivots[h]:
                pivots[h] = x
                rank += 1
                break
            x ^= pivots[h]
    return rank == len(points)


def bases(r):
    for row in combinations(range(1, 1 << r), r):
        if independent(row):
            yield row


def count_extensions(r, k):
    return prod((1 << r) - (1 << j) for j in range(k, r)) // factorial(r-k)


def v2(n):
    assert n
    return (n & -n).bit_length() - 1


def fft_in_place(a):
    step = 1
    while step < len(a):
        for j in range(0, len(a), step * 2):
            for i in range(j, j + step):
                x, y = a[i], a[i + step]
                a[i], a[i + step] = x+y, x-y
        step *= 2


def check_four():
    r = 4
    n = (1 << r)-1
    size = 1 << n
    data = [0] * size
    count = 0
    for b in bases(r):
        mask = sum(1 << (v-1) for v in b)
        assert data[mask] == 0
        data[mask] = 1
        count += 1
    assert count == 840
    fft_in_place(data)
    assert all(w % 16 == 8 for w in data)
    assert all(w != 0 for w in data)
    assert gcd(*data) == 8
    expected = {-56: 3000, -40: 2016, -8: 6720, 8: 15120,
                24: 5600, 72: 70, 136: 210, 392: 30, 840: 2}
    assert Counter(data) == expected
    print('PG4_WALSH_PASS rank=32768 gcd=8 levels=9')


def check_five():
    r = 5
    base_list = list(bases(r))
    assert len(base_list) == 83328
    target = set(range(1,9)) | {16}
    assert len(target) == 9
    direct = sum(-1 if sum(v in target for v in b) % 2 else 1 for b in base_list)
    assert direct == 0
    a = [1,7,21,28,0,0]
    c = [sum(comb(2,i)*a[k-i] for i in range(3) if 0 <= k-i < len(a))
         for k in range(6)]
    assert c == [1,9,36,77,77,28]
    assert [sum(independent(t) for t in combinations(sorted(target), k))
            for k in range(6)] == c
    for k in range(6):
        fixed = set((1 << j) for j in range(k))
        assert sum(fixed.issubset(b) for b in base_list) == count_extensions(5, k)
    predicted = sum((-2)**k * c[k] * count_extensions(5,k) for k in range(6))
    assert predicted == direct == 0
    B0 = {1,2,4,8,16}
    w0 = sum(-1 if sum(v in B0 for v in b) % 2 else 1 for b in base_list)
    assert w0 % 64 == 32
    assert v2(w0) == 5
    print('PG5_WALSH_PASS bases=83328 witness_zero=0 witness_v2=5')


def check_general_arithmetic():
    vals = []
    for r in range(1, 65):
        vals.append(min(k + v2(count_extensions(r,k)) for k in range(r+1)))
    assert vals[:5] == [0,0,2,3,5]
    assert all(vals[r-1] == r for r in range(5,65))
    print('PG_ALL_RANK_FORMULA_TEST_PASS ranks=1..64')


if __name__ == '__main__':
    check_four()
    check_five()
    check_general_arithmetic()
    print('PG_BINARY_BASE_FOURIER_PASS')

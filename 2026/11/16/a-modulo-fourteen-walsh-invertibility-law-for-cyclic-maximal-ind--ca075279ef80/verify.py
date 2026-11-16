#!/usr/bin/env python3
"""Exact tests for the Walsh transform of maximal independent sets on cycles.

All calculations use Python integers. No dependencies outside the standard library.
"""

I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

def multiply(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))

def transfer(sign):
    return ((0, 1, 0), (sign, 0, 1), (sign, 0, 0))

def product(signs):
    mat = I
    for sign in signs:
        mat = multiply(mat, transfer(sign))
    return mat

def trace(mat):
    return mat[0][0] + mat[1][1] + mat[2][2]

def is_maximal_independent(mask, n):
    for i in range(n):
        here = (mask >> i) & 1
        left = (mask >> ((i-1) % n)) & 1
        right = (mask >> ((i+1) % n)) & 1
        if here and (left or right):
            return False
        if not here and not left and not right:
            return False
    return True

def fwht(arr):
    n, step = len(arr), 1
    while step < n:
        for start in range(0, n, 2 * step):
            for j in range(start, start+step):
                a, b = arr[j], arr[j+step]
                arr[j] = a+b
                arr[j+step] = a-b
        step *= 2

# Periodicity is a consequence of matching triples in the order-three recurrence.
p = [3, 0, 2]
q = [1, 0, 1]
for n in range(3, 120):
    p.append(p[n-2] + p[n-3])
    q.append(q[n-2] + q[n-3])
assert all((p[n+14] - p[n]) % 4 == 0 for n in range(106))
assert all((p[n+7] - p[n]) % 2 == 0 for n in range(113))
assert all((q[n+7] - q[n]) % 2 == 0 for n in range(113))
assert all(p[n] % 4 == 2 and q[n] % 2 == 0 for n in range(8, 120, 14))

# Fixed 7-letter sign block has matrix order two.
block = (1, 1, 1, -1, 1, 1, -1)
assert product(block) == ((-1, 0, 2), (0, -1, 2), (0, 0, 1))
assert product(block+block) == I

witnesses = {4: (1,), 9: (1, 4), 11: (1, 2, 7),
             15: (1, 3, 7), 16: (1, 3, 7)}
for n, negative_positions in witnesses.items():
    signs = tuple(-1 if i+1 in negative_positions else 1 for i in range(n))
    assert trace(product(signs)) == 0, (n, negative_positions)
    assert trace(product(signs+block+block)) == 0

zero_counts = {}
for n in range(3, 19):
    arr = [int(is_maximal_independent(mask, n)) for mask in range(1 << n)]
    assert sum(arr) == p[n], (n, sum(arr), p[n])
    assert sum(arr[mask] for mask in range(1 << n) if mask & 1) == q[n]
    fwht(arr)
    zeros = sum(value == 0 for value in arr)
    zero_counts[n] = zeros
    assert (zeros > 0) == (n % 14 in {1,2,4,9,11}), (n, zeros)
    if n % 14 == 8:
        assert all(value % 4 == 2 for value in arr)

# Transfer identity is checked independently against direct signed enumeration.
for n in range(3, 11):
    maximal = [mask for mask in range(1 << n) if is_maximal_independent(mask, n)]
    for frequency in range(1 << n):
        direct = sum(-1 if ((frequency & mask).bit_count() % 2) else 1
                     for mask in maximal)
        signs = tuple(-1 if (frequency >> i) & 1 else 1 for i in range(n))
        assert trace(product(signs)) == direct, (n, frequency)

print('PASS: transfer/direct n=3..10; Walsh n=3..18; periodic residues; seed/nullword/block')
print('zero_counts_3_to_18:', ','.join(str(zero_counts[n]) for n in range(3,19)))

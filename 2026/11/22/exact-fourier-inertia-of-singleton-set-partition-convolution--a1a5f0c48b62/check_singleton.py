#!/usr/bin/env python3
"""Exact verifier for the spectrum of singleton-set partition counting convolution.

Uses integer arithmetic. Reconstructs partitions independently from the Bell recurrence
and independently from a restricted-growth-string recursion, then tests the Fourier
transform, spectral ranks, and all finite base cases used by the proof.
"""
from math import comb

assertions = 0

def check(test, message):
    global assertions
    assertions += 1
    if not test:
        raise AssertionError(message)

def bells(limit):
    b = [1]
    for m in range(1, limit + 1):
        b.append(sum(comb(m - 1, j) * b[j] for j in range(m)))
    return b

def direct_singleton_counts(n):
    # Each restricted-growth string is uniquely a set partition of [n].
    counts = [0] * (1 << n)
    rgs = [0] * n
    total = 0
    def rec(i, high):
        nonlocal total
        if i == n:
            block_sizes = [0] * (high + 1)
            for t in rgs:
                block_sizes[t] += 1
            bits = sum(1 << j for j, v in enumerate(rgs) if block_sizes[v] == 1)
            counts[bits] += 1
            total += 1
            return
        for v in range(high + 2):
            rgs[i] = v
            rec(i + 1, max(high, v))
    if n:
        rgs[0] = 0
        rec(1, 0)
    else:
        counts[0] = 1
        total = 1
    return counts, total

def walsh(a):
    a = a[:]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                p, q = a[j], a[j+h]
                a[j], a[j+h] = p+q, p-q
        h *= 2
    return a

def multiplier(n, k, b):
    return sum(comb(k, j)*((-2)**j)*b[n-j] for j in range(k+1))

def expected_sign(n, k):
    if n == 2 and k == 1:
        return 0
    if n in (1,3,5,7) and k == n:
        return -1
    return 1

B = bells(90)
for n in range(1, 12):
    counts, total = direct_singleton_counts(n)
    check(total == B[n], f'Bell enumeration n={n}')
    check(sum(counts) == B[n], f'partition count n={n}')
    fw = walsh(counts)
    for mask, actual in enumerate(fw):
        k = mask.bit_count()
        expected = multiplier(n,k,B)
        check(actual == expected, f'Walsh formula n={n}, mask={mask}')
        check((actual > 0)-(actual < 0) == expected_sign(n,k),
              f'inertia n={n}, mask={mask}')
    if n <= 7:
        for mask in range(1 << n):
            direct = sum((-1 if (mask & state).bit_count()%2 else 1)*num
                         for state,num in enumerate(counts))
            check(direct == fw[mask], f'direct character n={n}, mask={mask}')

for n in range(1,91):
    for k in range(n+1):
        v = multiplier(n,k,B)
        check((v > 0)-(v < 0) == expected_sign(n,k),
              f'Bell-moment sign n={n}, k={k}')

check([multiplier(k,k,B) for k in (1,3,5,7,9)] == [-1,-3,-10,-21,307],
      'finite odd centered moments')
check(3**9*720+4**9*120 > (2**9+1)*120*720,
      'strict r=5,6 tail bound at k=9')
check(multiplier(2,1,B) == 0, 'sole zero')
print(f'PASS: {assertions} exact assertions; direct enumeration through n=11; all sign classes through n=90')

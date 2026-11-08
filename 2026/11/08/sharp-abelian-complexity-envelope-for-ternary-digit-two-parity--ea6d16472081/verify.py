#!/usr/bin/env python3
"""Independent finite consistency checks for the ternary-digit parity word.
These checks supplement rather than replace the arbitrary-length proof.
"""
from itertools import product

def from_digit_parity(n):
    parity = 0
    while n:
        parity ^= (n % 3 == 2)
        n //= 3
    return parity

def morph_iter(k):
    w = '0'
    for _ in range(k):
        w = ''.join('001' if a == '0' else '110' for a in w)
    return w

prefix = morph_iter(11)
assert len(prefix) == 3**11
for i in range(len(prefix)):
    assert int(prefix[i]) == from_digit_parity(i)

for k in range(9):
    w = morph_iter(k)
    signs = [1 if c == '0' else -1 for c in w]
    p = 0
    prefix_vals = [0]
    for s in signs:
        p += s
        prefix_vals.append(p)
    assert p == 1
    assert max(prefix_vals) == k + 1
    assert min(prefix_vals) == min(0, 2-k)
    assert morph_iter(k+1) == w+w+''.join('1' if c == '0' else '0' for c in w)

signed = [1 if c == '0' else -1 for c in prefix]
partial = [0]
for s in signed:
    partial.append(partial[-1] + s)

for k in range(8):
    n = 3**k
    sums = [partial[i+n] - partial[i] for i in range(len(prefix)-n+1)]
    assert min(sums) == -(2*k+1), (k, min(sums))
    assert max(sums) == 2*k+1, (k, max(sums))
    ones_counts = {(n - x)//2 for x in sums}
    assert len(ones_counts) == 2*k+2
    print(f'k={k}: n={n}, signed extrema={min(sums)},{max(sums)}, types={len(ones_counts)}')

for n in range(1,301):
    k = 0
    while 3**k < n:
        k += 1
    observed = [partial[i+n] - partial[i] for i in range(len(prefix)-n+1)]
    assert max(abs(x) for x in observed) <= 2*k+1, (n,k)

print('VERIFY_OK: digit recurrence, block extrema, scale complexity, and bounds')

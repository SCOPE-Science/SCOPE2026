#!/usr/bin/env python3
"""Exact finite checks accompanying a constructive theorem on triangular digit weights."""
R = 36853059
SEED_HEX = [
    '2699d3c61f266', '2699d3e9447aa', '2699d40c69cef',
    '2699d42f8f235', '2699d452b477c', '2699d475d9cc4',
    '2699d498ff20d', '2699d4bc24757', '2699d4df49ca2',
    '2699d5026f1ee', '2699d5259473b'
]

def triangular(n):
    return n * (n + 1) // 2

for j, value in enumerate(SEED_HEX):
    assert triangular(R+j) == int(value, 16)
    assert triangular(R+j).bit_count() == 26

for L in range(5, 17):
    B = (1 << L) - 1
    assert (B*B).bit_count() == L
    assert (9*B*B).bit_count() == L+1
    for A in range(1, 1 << L):
        assert (A*B).bit_count() == L

pairs = 0
for t in range(13, 27):
    H = triangular(t)
    L = (H - (26 if H % 2 == 0 else 27)) // 2
    q = ((1 << L) - 1) * (1 if H % 2 == 0 else 3)
    for K in (L + 30, L + 31, L + 40):
        N = q * (1 << K) + R
        for j in range(11):
            assert triangular(N+j).bit_count() == H
        pairs += 1
print(f'VERIFY_OK seed=11 repunit_L=5..16 constructed_parameter_pairs={pairs} fixed_weight_11=all')

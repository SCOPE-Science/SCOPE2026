#!/usr/bin/env python3
"""Finite checks for the Brik-word 010-frequency identity and sliding-block repetition."""
from fractions import Fraction

blocks = ['101']
for n in range(1, 19):
    old = blocks[-1]
    blocks.append(old + old[n:])
for n, w in enumerate(blocks, 1):
    assert len(w) == 2**(n-1)+n+1, (n, len(w))
    assert w.endswith('01')
    assert '00' not in w

w = blocks[-1]
encoded = ''.join('1' if w[i] == '1' or w[i:i+3] == '010' else '0'
                  for i in range(len(w)-2))

for n in range(1, len(blocks)):
    small = blocks[n-1]
    large = blocks[n]
    Qsmall = sum(small[i:i+3] == '010' for i in range(len(small)-2))
    Qlarge = sum(large[i:i+3] == '010' for i in range(len(large)-2))
    q = sum(w[i:i+3] == '010' for i in range(n))
    rhs = 2*Qsmall - q + (1-int(w[n]))
    assert Qlarge == rhs, (n, Qlarge, rhs)

for n in range(3, 14):
    L = 2**(n-1)+1
    assert encoded[n:n+L-2] == encoded[n+L:n+2*L-2], n

# An unbounded family of all-one runs is guaranteed analytically by the full-language theorem.
# The finite check below verifies a growing collection and infinitely-many-zero witnesses locally.
for k in range(1, 7):
    assert '1'*k in encoded
assert encoded.count('0') > 100
assert w.count('011') > 100

K = 60
T = sum(Fraction(int(encoded[i]), 2**(i+1)) for i in range(K))
lo = 2-2*(T+Fraction(1, 2**K))
hi = 2-2*T
empirical = Fraction(sum(w[i:i+3] == '010' for i in range(len(w)-2)), len(w)-2)
assert abs(empirical-hi) < Fraction(1, 50000)  # empirical finite-prefix discrepancy is small
print('Brik levels:', len(blocks), 'last block length:', len(w))
print('Exact length/suffix/no-00 identities: PASS')
print('Exact 010 recurrence stages:', len(blocks)-1, 'PASS')
print('Sliding-block repetitions at levels 3..13: PASS')
print('Long ones and zero witnesses: PASS')
print('Theta interval (60 bits):', float(T), float(T + Fraction(1, 2**K)))
print('Predicted 010 frequency interval:', float(lo), float(hi))
print('Empirical length-%d frequency:' % len(w), float(empirical))

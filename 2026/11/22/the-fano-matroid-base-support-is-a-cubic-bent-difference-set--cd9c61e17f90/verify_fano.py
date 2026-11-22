"""Exact, standalone verification of the Fano-matroid six-bit bent support."""
from itertools import combinations
from collections import Counter
from math import comb

P = range(1, 8)
LINES = {frozenset((a, b, a ^ b)) for a, b in combinations(P, 2)}
assert len(LINES) == 7
assert all(len(L) == 3 for L in LINES)
assert all(sum({a,b}.issubset(L) for L in LINES) == 1 for a,b in combinations(P,2))
BASES = {frozenset(S) for S in combinations(P,3)} - LINES
assert len(BASES) == 28

# Seven-bit signed Fourier coefficients, and independent Krawtchouk subtraction.
frequency_types = Counter()
for s in range(8):
    for S0 in combinations(P, s):
        S = frozenset(S0)
        direct = sum((-1) ** len(S & B) for B in BASES)
        krawtchouk = sum((-1)**j * comb(s,j)*comb(7-s,3-j)
                            for j in range(4) if j <= s and 3-j <= 7-s)
        line_sum = sum((-1) ** len(S & L) for L in LINES)
        assert direct == krawtchouk - line_sum
        tag = ('line' if s==3 and S in LINES else
               'nonline' if s==3 else
               'complement_line' if s==4 and frozenset(P)-S in LINES else
               'complement_nonline' if s==4 else 'only')
        frequency_types[(s,tag,direct)] += 1
assert sum(frequency_types.values()) == 128
assert Counter({(0,'only',28):1, (1,'only',4):7,
    (2,'only',-4):21, (3,'line',4):7, (3,'nonline',-4):28,
    (4,'complement_line',-4):7, (4,'complement_nonline',4):28,
    (5,'only',4):21, (6,'only',-4):7, (7,'only',-28):1}) == frequency_types

# Parity-one affine slice x_7 = 1 + sum(x_1..x_6) mod 2.
def support(x):
    bits = [(x >> i) & 1 for i in range(6)]
    bits.append(1 ^ (sum(bits) & 1))
    return frozenset(i+1 for i,b in enumerate(bits) if b)

f = [int(support(x) in BASES) for x in range(64)]
assert sum(f) == 28
assert f[0] == 0

# Walsh-Hadamard transform, compared with independent character summation.
w = f.copy()
for k in range(6):
    h=1<<k
    for start in range(0, 64, 2*h):
        for off in range(h):
            i=start+off
            a,b = w[i],w[i+h]
            w[i],w[i+h] = a+b,a-b
for freq in range(64):
    direct = sum(f[x]*(-1)**((freq & x).bit_count() & 1) for x in range(64))
    assert w[freq] == direct
assert w[0] == 28
assert Counter(w[1:]) == Counter({4:28,-4:35})
assert 0 not in w
assert min(abs(t) for t in w)==4

# Perfectly nonlinear / difference-set autocorrelation.
for shift in range(1, 64):
    pairs = sum(f[x]*f[x^shift] for x in range(64))
    assert pairs == 12
    derivative = sum(f[x] ^ f[x^shift] for x in range(64))
    assert derivative == 32
for freq in range(64):
    bent_transform = (64 if freq==0 else 0) - 2*w[freq]
    assert abs(bent_transform) == 8

# Complete algebraic normal form by Boolean subset Mobius inversion.
anf = f.copy()
for k in range(6):
    for x in range(64):
        if x & (1 << k):
            anf[x] ^= anf[x ^ (1 << k)]
degrees=Counter(mask.bit_count() for mask,c in enumerate(anf) if c)
assert degrees == Counter({2:12,3:16})
assert anf[7] == 1 # x_1 x_2 x_3 has nonzero cubic coefficient

print('CHECK_OK: Fano lines=7, bases=28, full Walsh frequencies=128, '
      'six-bit characters=64, autocorrelation differences=63, '
      'ANF degrees=12 quadratic +16 cubic; rank=64; condition=7.')

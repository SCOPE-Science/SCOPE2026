#!/usr/bin/env python3
"""Exact, dependency-free verification of Catalan matroid C_5 Walsh recovery."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

N = 10
SIZE = 1 << N

def ballot_bases():
    out = set()
    for up in combinations(range(N), 5):
        mask = sum(1 << i for i in up)
        h = 0
        for i in range(N):
            h += 1 if (mask >> i) & 1 else -1
            if h < 0:
                break
        else:
            assert h == 0
            out.add(mask)
    return out

def recursive_bases():
    ans = set()
    def rec(i, h, up, mask):
        if i == N:
            if h == 0 and up == 5:
                ans.add(mask)
            return
        if up < 5:
            rec(i + 1, h + 1, up + 1, mask | (1 << i))
        if h > 0:
            rec(i + 1, h - 1, up, mask)
    rec(0, 0, 0, 0)
    return ans

def signed_ballot_dp(frequency):
    dp = {(0, 0): 1}
    for i in range(N):
        new = defaultdict(int)
        eps = -1 if (frequency >> i) & 1 else 1
        for (h, up), count in dp.items():
            if up < 5:
                new[(h + 1, up + 1)] += eps * count
            if h > 0:
                new[(h - 1, up)] += count
        dp = new
    return dp.get((0, 5), 0)

def hadamard(vals):
    vals = list(vals)
    stride = 1
    while stride < len(vals):
        for start in range(0, len(vals), 2 * stride):
            for j in range(start, start + stride):
                a, b = vals[j], vals[j + stride]
                vals[j] = a + b
                vals[j + stride] = a - b
        stride *= 2
    return vals

def parity(v, positions):
    return sum((v >> (p-1)) & 1 for p in positions) % 2

bases = ballot_bases()
assert bases == recursive_bases()
assert len(bases) == 42
assert all((b & 1) and not (b & (1 << 9)) for b in bases)
W = []
for s in range(SIZE):
    direct = sum(-1 if ((s & b).bit_count() & 1) else 1 for b in bases)
    assert direct == signed_ballot_dp(s)
    W.append(direct)
indicator = [int(x in bases) for x in range(SIZE)]
assert hadamard(indicator) == W
assert sum(x*x for x in W) == SIZE * len(bases)

# Conditions are stated in one-based step indices.
def expected_zero(s):
    return parity(s, [2,3]) == 1 and parity(s, [8,9]) == 1 and parity(s, [4,5,6,7]) == 1

zero = {s for s in range(SIZE) if W[s] == 0}
assert zero == {s for s in range(SIZE) if expected_zero(s)}
assert len(zero) == 128
assert min(abs(x) for x in W if x) == 2
assert max(abs(x) for x in W) == 42
assert Counter(W) == Counter({
 -42:4, -14:32, -12:16, -10:12, -6:32, -4:176, -2:176,
 0:128, 2:176, 4:176, 6:32, 10:12, 12:16, 14:32, 42:4})

class_expected = {
 (0,0,0): {-14:8,-6:8,2:8,10:6,42:2},
 (0,0,1): {-12:4,-4:12,4:12,12:4},
 (0,1,0): {-2:28,14:4},
 (0,1,1): {-4:16,4:16},
 (1,0,0): {-14:4,2:28},
 (1,0,1): {-4:16,4:16},
 (1,1,0): {-6:8,2:24},
 (1,1,1): {0:32},
}
by_class = defaultdict(list)
for s in range(SIZE):
    if s & 1 or s & (1 << 9):
        continue
    key=(parity(s,[2,3]), parity(s,[8,9]), parity(s,[4,5,6,7]))
    by_class[key].append(W[s])
assert {key:dict(Counter(values)) for key,values in by_class.items()} == class_expected

# Fourier inversion of the nonzero-multiplier indicator.
projection = hadamard([int(v != 0) for v in W])
a = (1 << 1) | (1 << 2) # steps 2,3
b = (1 << 7) | (1 << 8) # steps 8,9
c = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6) # steps 4..7
span = {u*a ^ v*b ^ w*c: (u,v,w) for u in (0,1) for v in (0,1) for w in (0,1)}
assert len(span) == 8
assert sum(1 for x in projection if x) == 8
for x in range(SIZE):
    if x == 0:
        assert projection[x] == 896
    elif x in span:
        assert projection[x] in (-128,128)
    else:
        assert projection[x] == 0
assert Fraction(sum(abs(x) for x in projection), SIZE) == Fraction(7,4)
assert [x//SIZE if x%SIZE==0 else Fraction(x,SIZE) for x in hadamard(projection)] == [int(v!=0) for v in W]
print('CATALAN5_AFFINE_WALSH_ZERO_LOCUS_AND_SHARP_PROJECTION_PASS')
print('bases=42; characters=1024; zeros=128; rank=896; gap=2; sharp_norm=7/4')

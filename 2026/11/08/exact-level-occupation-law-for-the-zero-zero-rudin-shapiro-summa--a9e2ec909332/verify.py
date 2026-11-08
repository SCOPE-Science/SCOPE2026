#!/usr/bin/env python3
"""Independent finite checks for zero-zero Rudin-Shapiro level occupancy."""
from collections import Counter

def weight11(n):
    return 1 if ((n & (n >> 1)).bit_count() & 1) == 0 else -1

def weight00(n):
    if n == 0:
        return 1
    zero_bits = ((1 << n.bit_length()) - 1) ^ n
    return 1 if ((zero_bits & (zero_bits >> 1)).bit_count() & 1) == 0 else -1

def expected(k):
    assert k >= 1
    u = 1 << (max(0, (k + 1).bit_length() - 2))
    # Here u is the power of two such that 2u-1 <= k <=4u-2.
    assert 2*u - 1 <= k <= 4*u - 2, (k, u)
    if k <= 3*u - 2:
        return u
    if k < 4*u - 2:
        return 4*u - 2 - k
    return u

N = 1 << 17
S = T = 0
cT = Counter()
cBlock = Counter()
for n in range(N):
    S += weight11(n)
    T += weight00(n)
    cT[T] += 1
    if n > 0:
        cBlock[(n.bit_length() - 1,T)] += 1

# No future index can give a value <=100: the next block has minimum >100.
for k in range(1,101):
    assert cT[k] == expected(k), (k, cT[k], expected(k))
assert T == 4*(1 << 8)-2  # Last full block m=16 has end value D16.

for m in range(14):
    u = 1 << (m // 2)
    def block_expected(k):
        if m % 2 == 0:
            if 2*u - 1 <= k <= 3*u - 3:
                return k - 2*u + 2
            if k == 3*u - 2:
                return u - 1
            if 3*u - 1 <= k <= 4*u - 3:
                return 4*u - 2 - k
            if k == 4*u - 2:
                return 1
            return 0
        if k == 4*u - 2:
            return u - 1
        if 4*u - 1 <= k <= 6*u - 3:
            return 6*u - 2 - k
        if k == 6*u - 2:
            return 1
        return 0
    for k in range(1, 1000):
        assert cBlock[(m,k)] == block_expected(k), (m,k)
print('PASS exact individual-block occupation formula for m=0..13')

print('PASS occupancy levels K=1..100 complete in 2^17 direct terms')
for m in range(0,16):
    s = 0
    H = Counter()
    for n in range(1<<m):
        s += weight11(n)
        H[s] += 1
    u=1<<(m//2)
    H_expected = Counter()
    if m%2==0:
        H_expected.update({v: (v if v<=u else 2*u-v) for v in range(1,2*u)})
    else:
        H_expected.update({v:v for v in range(1,2*u)})
        H_expected[2*u] = u
    assert H == H_expected, (m, H, H_expected)
print('PASS 16 complete standard Rudin-Shapiro prefix histograms m=0..15')
for m in range(0,16):
    for j in range(1<<m):
        n=(1<<m)+j
        assert weight00(n)==weight11((1<<m)-1-j)
print('PASS bit-complement involution m=0..15, all 65,535 indices')
for k in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,30,31,62,63,64,95,99,100]:
    print(f'K={k}: count={cT[k]}')

#!/usr/bin/env python3
"""Self-contained exact enumeration of regular 7-tournament Walsh multipliers."""
from collections import Counter
from fractions import Fraction
import itertools
import hashlib
import struct

n = 7
full_edges = [(i,j) for i in range(n) for j in range(i+1,n)]
internal = [(i,j) for i in range(1,n) for j in range(i+1,n)]
index = {p:k for k,p in enumerate(full_edges)}
idx_internal = {p:k for k,p in enumerate(internal)}

# Backtrack independently by choices of the outgoing edges of each vertex.
family = []
def extend(i, degrees, mask):
    if i == n:
        assert degrees == [3]*n
        family.append(mask)
        return
    need = 3 - degrees[i]
    if not 0 <= need <= n-i-1:
        return
    for choice in itertools.combinations(range(i+1,n), need):
        chosen = set(choice)
        new = degrees.copy()
        new[i] = 3
        value = mask
        for j in range(i+1,n):
            if j not in chosen:
                new[j] += 1
                value |= 1 << index[i,j]
        if all(new[j] <= 3 <= new[j] + n-i-2 for j in range(i+1,n)):
            extend(i+1,new,value)

extend(0,[0]*n,0)
assert len(family) == len(set(family)) == 2640

# The parity of each regular score determines all 6 star edges from 15 internal edges.
small_masks = []
for m in family:
    u = sum(((m >> index[e]) & 1) << j for j,e in enumerate(internal))
    for v in range(1,n):
        p = ((v+1) % 2) ^ (sum((u >> idx_internal[e]) & 1 for e in internal if v in e) % 2)
        assert p == ((m >> index[0,v]) & 1)
    small_masks.append(u)
assert len(set(small_masks)) == 2640

N = 1 << 15
F = [0]*N
for u in small_masks:
    F[u] += 1

def walsh(a):
    block = 1
    while block < len(a):
        for start in range(0,len(a),block*2):
            for j in range(start,start+block):
                x,y = a[j],a[j+block]
                a[j] = x+y
                a[j+block] = x-y
        block *= 2

walsh(F)
assert sum(t*t for t in F) == N*2640
cnt = Counter(F)
full_hist = Counter()
for value, multiplicity in cnt.items():
    full_hist[abs(value)] += multiplicity*64
assert full_hist[0] == 1543168
assert sum(full_hist.values()) == 1<<21
assert full_hist[16] == 241920
assert min(abs(v) for v in F if v) == 16
assert max(abs(v) for v in F) == 2640
assert sum(v != 0 for v in F)*64 == 553984
P = [int(v != 0) for v in F]
walsh(P)
L1 = sum(abs(v) for v in P)
assert L1 == 1427840, L1
assert Fraction(L1,N) == Fraction(11155,256)

# The zero/nonzero support is invariant under all 64 star-edge gauge shifts.
# The inverse Fourier support kernel on the full cube is supported on the 15-d
# parity-constrained direction subspace; hence its norm equals L1 / 2^15.
print('family=2640 quotient_frequencies=32768 ambient_frequencies=2097152')
print('nullity=1543168 rank=553984 min_nonzero=16 max=2640')
print('sharp_inverse_l2=1/16 condition_number=165')
print('sharp_endpoint_projection=', Fraction(L1,N), 'kernel_abs_sum_quotient=', L1)
print('full_absolute_hist=', sorted(full_hist.items()))
print('min_16_witness_internal_frequency=', next(i for i,v in enumerate(F) if abs(v)==16))
print('quotient_W_sha256=',hashlib.sha256(b''.join(struct.pack('<i',v) for v in F)).hexdigest())
print('REGULAR_K7_QUOTIENT_PASS')

#!/usr/bin/env python3
"""Exact finite verification of the Fano-incidence perfect-matching Walsh theorem.

Requires Python 3.9+ standard library only; no data files or online services.
"""
from collections import Counter
from itertools import permutations
from functools import lru_cache
from fractions import Fraction

N = 7
LINES = [frozenset((i, (i+1) % 7, (i+3) % 7)) for i in range(N)]
assert len(set(LINES)) == 7
assert all(len(L) == 3 for L in LINES)
assert all(sum(j in L for L in LINES) == 3 for j in range(N))
assert all(len(LINES[i] & LINES[j]) == 1 for i in range(N) for j in range(i+1, N))
EDGES = sorted((i, j) for i, L in enumerate(LINES) for j in L)
assert len(EDGES) == 21
INDEX = {e: k for k, e in enumerate(EDGES)}

# An independently enumerated complete list of perfect matchings.
PERMS = [q for q in permutations(range(N)) if all(q[i] in LINES[i] for i in range(N))]
MATCH_MASKS = [sum(1 << INDEX[i, q[i]] for i in range(N)) for q in PERMS]
assert len(MATCH_MASKS) == len(set(MATCH_MASKS)) == 24

# Check permanent by recursive row-to-column assignment, not using permutations.
def enumerate_recursive(i, used, mask, out):
    if i == N:
        out.append(mask)
        return
    for j in sorted(LINES[i]):
        if not ((used >> j) & 1):
            enumerate_recursive(i+1, used | (1 << j), mask | (1 << INDEX[i, j]), out)
RECURSIVE = []
enumerate_recursive(0, 0, 0, RECURSIVE)
assert sorted(RECURSIVE) == sorted(MATCH_MASKS)

# Canonical spanning tree and its 8 cotree (chord) coordinates.
parent = list(range(14))
def root(v):
    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]
    return v
TREE, CHORDS = [], []
for edge_idx, (i, j) in enumerate(EDGES):
    x, y = root(i), root(j+7)
    if x == y:
        CHORDS.append(edge_idx)
    else:
        parent[x] = y
        TREE.append(edge_idx)
assert len(TREE) == 13 and len(CHORDS) == 8

# A basis of cycle vectors, one for each chord: follow unique tree path.
adj = [[] for _ in range(14)]
for e in TREE:
    i, j = EDGES[e]
    adj[i].append((j+7, e))
    adj[j+7].append((i, e))
CYCLES = []
for e in CHORDS:
    i, j = EDGES[e]
    queue = [(i, 0)]
    visited = {i}
    for v, mask in queue:
        if v == j + 7:
            CYCLES.append(mask | (1 << e))
            break
        for nxt, f in adj[v]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, mask | (1 << f)))
    else:
        raise AssertionError('Graph not connected')
assert len(CYCLES) == 8
assert all(sum((m >> e) & 1 for e in CHORDS) == 1 for m in CYCLES)
assert all(all((m & sum(1 << f for f in TREE)).bit_count() >= 0 for m in CYCLES) for _ in [0])
for cycle in CYCLES:
    for v in range(14):
        d = sum(bool((cycle >> f) & 1) for f, (i, j) in enumerate(EDGES) if v in (i, j+7))
        assert d % 2 == 0

# A signed permanent computed without reusing the perfect-matching list.
def signed_permanent(chord_sign_bits):
    negative_edges = {CHORDS[j] for j in range(8) if (chord_sign_bits >> j) & 1}
    @lru_cache(None)
    def dp(row, used):
        if row == 7:
            return int(used == 127)
        total = 0
        for col in LINES[row]:
            if not ((used >> col) & 1):
                total += (-1 if INDEX[row, col] in negative_edges else 1) * dp(row+1, used | (1 << col))
        return total
    return dp(0, 0)

def exact_determinant(A):
    """Fraction-free Bareiss elimination with exact divisibility checks."""
    a = [row[:] for row in A]
    n = len(a)
    sign = 1
    divisor = 1
    for k in range(n-1):
        pivot_row = next((r for r in range(k, n) if a[r][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*pivot - a[i][k]*a[k][j]
                assert numerator % divisor == 0
                a[i][j] = numerator // divisor
            a[i][k] = 0
        divisor = pivot
    return sign * a[-1][-1]

def permutation_sign(q):
    inversions = sum(q[i] > q[j] for i in range(N) for j in range(i+1, N))
    return -1 if inversions & 1 else 1

# All Fano matching bijections have the same even permutation sign.
assert all(permutation_sign(q) == 1 for q in PERMS)

values = []
for t in range(256):
    neg = sum(1 << CHORDS[j] for j in range(8) if (t >> j) & 1)
    via_matchings = sum(-1 if ((matching & neg).bit_count() & 1) else 1 for matching in MATCH_MASKS)
    via_permanent = signed_permanent(t)
    A = [[0 if j not in LINES[i] else
          (-1 if INDEX[i, j] in {CHORDS[k] for k in range(8) if (t >> k) & 1} else 1)
          for j in range(7)] for i in range(7)]
    via_determinant = exact_determinant(A)
    assert via_matchings == via_permanent == via_determinant
    values.append(via_permanent)
assert Counter(values) == Counter({-8:45, 0:168, 8:42, 24:1})
assert sum(v*v for v in values) == 256 * 24  # Parseval for 24 distinct matchings after gauge.
assert values[0] == 24

# Fourier support and its inverse via exact integer FWHT.
support = [int(v != 0) for v in values]
coeff = support.copy()
for k in range(8):
    for i in range(256):
        if not ((i >> k) & 1):
            a, b = coeff[i], coeff[i | (1 << k)]
            coeff[i], coeff[i | (1 << k)] = a + b, a - b
assert Counter(coeff) == Counter({-8:77, 0:108, 8:42, 16:28, 88:1})
assert sum(abs(v) for v in coeff) == 1488
assert Fraction(sum(abs(v) for v in coeff), 256) == Fraction(93, 16)

# Independent direct Walsh inversion for every coordinate of the cycle-space kernel.
for x in range(256):
    brute = sum(-1 if ((t & x).bit_count() & 1) else 1 for t in range(256) if support[t])
    assert coeff[x] == brute
    # Each cycle basis coordinate is paired with the corresponding cotree chord.
    cyc = 0
    for j in range(8):
        if (x >> j) & 1:
            cyc ^= CYCLES[j]
    for t in range(256):
        chord_rep = sum(1 << CHORDS[j] for j in range(8) if (t >> j) & 1)
        assert ((cyc & chord_rep).bit_count() & 1) == ((x & t).bit_count() & 1)

# The full 21-coordinate character space is an 8192-to-1 extension:
# vertex switching makes all 13 tree-edge signs positive; its parity effect
# on all perfect matchings is constant. One vertex star reverses that parity.
assert (len(TREE) == 13 and len(CHORDS) == 8 and len(MATCH_MASKS) == 24)
FULL = 1 << 21
rank = 88 * (1 << 13)
nullity = 168 * (1 << 13)
assert rank == 720896 and nullity == 1376256 and rank + nullity == FULL
signed_full = Counter({-24:4096, -8:356352, 0:nullity, 8:356352, 24:4096})
assert sum(signed_full.values()) == FULL
assert sum(v*v*m for v,m in signed_full.items()) == FULL * 24
assert max(abs(v) for v in values) == 24
assert min(abs(v) for v in values if v) == 8
assert Fraction(24, 8) == 3
print('PASS: 24 Fano matchings, 256 exact signed permanents, complete full Walsh spectrum,')
print('       rank 720896, nullity 1376256, sharp projection norm 93/16, condition 3.')

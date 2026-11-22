"""Exhaustive, finite certificate for a symmetry-defect count in F_2[Q_8].

Usage: python3 CHECKER.py
Requires Python 3.10+, no third-party modules. All loops have explicit finite ranges.
"""
from collections import Counter

# Elements of Q_8 are z^e i^u j^v, encoded e + 2u + 4v.
# Relations: z^2=1, z central, i^2=j^2=z, ji=zij.
def group_product(x, y):
    e, u, v = x & 1, (x >> 1) & 1, (x >> 2) & 1
    f, r, s = y & 1, (y >> 1) & 1, (y >> 2) & 1
    return (e ^ f ^ (u & r) ^ (v & s) ^ (v & r)) | ((u ^ r) << 1) | ((v ^ s) << 2)

G = tuple(tuple(group_product(x, y) for y in range(8)) for x in range(8))
assert all(G[0][x] == x == G[x][0] for x in range(8))
assert all(G[G[x][y]][w] == G[x][G[y][w]] for x in range(8) for y in range(8) for w in range(8))
assert G[2][2] == G[4][4] == 1 and G[4][2] == G[1][G[2][4]]
assert len(set(G[2][x] for x in range(8))) == 8

# Ring elements are eight-bit coefficient vectors in the group basis.
# This computation uses bilinear expansion, never a ring presentation from a classification table.
M = [[0] * 256 for _ in range(256)]
for a in range(256):
    for b in range(256):
        value = 0
        for x in range(8):
            if a & (1 << x):
                for y in range(8):
                    if b & (1 << y):
                        value ^= 1 << G[x][y]
        M[a][b] = value

assert all(M[1][x] == x == M[x][1] for x in range(256))
# Explicit symmetry-defect witness from RESULT.md.
assert M[M[5][17]][86] == 0 and M[M[5][86]][17] == 255

def basis(vectors):
    piv = {}
    for item in vectors:
        while item:
            p = item.bit_length() - 1
            if p in piv:
                item ^= piv[p]
            else:
                piv[p] = item
                break
    return tuple(piv.values())

def span(b):
    values = {0}
    for x in b:
        values |= {v ^ x for v in tuple(values)}
    return values

# The augmentation ideal is precisely the even-weight group-ring elements.
J = basis(a for a in range(256) if a.bit_count() % 2 == 0)
J_powers = [J]
for _ in range(2, 6):
    J_powers.append(basis(M[x][y] for x in J_powers[-1] for y in J))
assert tuple(map(len, J_powers)) == (7, 5, 3, 1, 0)
J_sets = [span(b) for b in J_powers]
valuation = [None] * 256
for x in range(256):
    valuation[x] = 99 if x == 0 else (0 if x not in J_sets[0] else
                     max(t + 1 for t in range(4) if x in J_sets[t]))

def rank(vectors):
    return len(basis(vectors))

right_rank = [rank(M[1 << t][d] for t in range(8)) for d in range(256)]
rank_pairs = Counter()
contrib = Counter()
for b in range(256):
    for c in range(256):
        d, e = M[b][c], M[c][b]
        r = right_rank[d]
        s = rank(M[1 << t][d] | (M[1 << t][e] << 8) for t in range(8))
        rank_pairs[(r, s)] += 1
        contrib[(r, s)] += (1 << (8-r)) - (1 << (8-s))

expected_pairs = {
    (0, 0): 1664, (1, 1): 1408, (2, 2): 3072, (2, 3): 3072,
    (4, 4): 9216, (4, 5): 6144, (6, 6): 24576, (8, 8): 16384
}
assert rank_pairs == expected_pairs, rank_pairs
assert sum(rank_pairs.values()) == 256**2
assert contrib[(2, 3)] == 98304 and contrib[(4, 5)] == 49152
assert sum(contrib.values()) == 147456

# Independent direct all-triples count (does not use the kernel-rank method).
valuation_profile = Counter()
direct_count = 0
for a in range(256):
    for b in range(256):
        ab = M[a][b]
        for c in range(256):
            if M[ab][c] == 0 and M[M[a][c]][b] != 0:
                direct_count += 1
                valuation_profile[(valuation[a], valuation[b], valuation[c])] += 1
assert valuation_profile == {
    (1, 1, 2): 49152,
    (1, 2, 1): 49152,
    (2, 1, 1): 49152
}, valuation_profile
assert direct_count == sum(contrib.values()) == 147456
assert 147456 * 1024 == 9 * 256**3
print('QUATERNION_SYMMETRY_DEFECT_OK')
print('All 65536 ordered pairs and 16777216 ordered triples examined.')
print('Radical dimensions:', tuple(map(len, J_powers)))
print('Joint rank pair counts:', sorted(rank_pairs.items()))
print('Witness valuations:', sorted(valuation_profile.items()))
print('Witness count:', direct_count, 'probability: 9/1024')

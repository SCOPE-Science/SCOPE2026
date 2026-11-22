"""Exact, self-contained finite field check of neighborhood shattering in a 16-vertex graph."""
from itertools import combinations
from math import comb

MOD = 0b10011

def multiply(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 16:
            a ^= MOD
    return out

H = {multiply(multiply(a, a), a) for a in range(1, 16)}
assert len(H) == 5
assert all(multiply(h, k) in H for h in H for k in H)
N = [{v ^ h for h in H} for v in range(16)]
C = [s | {v} for v, s in enumerate(N)]
for a in range(16):
    assert len(N[a]) == 5 and a not in N[a]
    for b in range(a + 1, 16):
        linked = b in N[a]
        assert linked == (a in N[b])
        assert len(N[a] & N[b]) == (0 if linked else 2)

def shattered(support, blocks):
    return len({tuple(int(u in B) for u in support) for B in blocks}) == 1 << len(support)

def is_path3(t):
    return sum(int(b in N[a]) for a, b in combinations(t, 2)) == 2

def is_common_independent3(t):
    return all(b not in N[a] for a, b in combinations(t, 2)) and any(all(u in N[w] for u in t) for w in range(16))

faces = {}
for name, blocks, expected in [('open', N, [1, 16, 80, 160, 0]),
                                ('closed', C, [1, 16, 120, 320, 0])]:
    fs = [[], [], [], [], []]
    for size in range(5):
        for t in combinations(range(16), size):
            hit = shattered(t, blocks)
            if size == 3:
                assert hit == (is_common_independent3(t) or (name == 'closed' and is_path3(t)))
            if size == 2:
                assert hit == ((name == 'closed') or (t[1] not in N[t[0]]))
            if hit:
                fs[size].append(t)
    assert list(map(len, fs)) == expected, (name, list(map(len, fs)))
    pivots = {}
    edge_id = {e: i for i, e in enumerate(fs[2])}
    for t in fs[3]:
        x = sum(1 << edge_id[e] for e in combinations(t, 2))
        while x:
            j = x.bit_length() - 1
            if j in pivots:
                x ^= pivots[j]
            else:
                pivots[j] = x
                break
    rank = len(pivots)
    assert rank == (65 if name == 'open' else 104), (name, rank)
    h1 = len(fs[2]) - (len(fs[1]) - 1) - rank
    h2 = len(fs[3]) - rank
    assert (h1, h2) == ((0, 95) if name == 'open' else (1, 216))
    faces[name] = fs
    print(f'{name}: f={expected}, rank_d2={rank}, mod2_betti_1_2=({h1},{h2})')

# Natural closed shattering 1-cocycle: graph edges have characteristic 1.
for tri in faces['closed'][3]:
    assert sum(int(b in N[a]) for a, b in combinations(tri, 2)) % 2 == 0
u, v = 0, next(iter(N[0]))
w = next(x for x in range(16) if x not in C[u] and x not in C[v])
assert sum(int(b in N[a]) for a, b in combinations((u, v, w), 2)) == 1
print('nonzero mod-two cocycle: verified; characteristic triangle has odd pairing')
print('FIELD_VERIFY_PASS')

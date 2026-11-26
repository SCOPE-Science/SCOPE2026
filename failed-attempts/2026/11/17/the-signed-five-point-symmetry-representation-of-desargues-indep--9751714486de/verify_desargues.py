#!/usr/bin/env python3
"""Exact finite-chain and signed-character verification for a Desargues graph complex."""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations

P = list(combinations(range(5), 2))
P_INDEX = {v: i for i, v in enumerate(P)}
PET_EDGES = [(i, j) for i, a in enumerate(P) for j, b in enumerate(P)
             if i < j and set(a).isdisjoint(b)]
assert len(PET_EDGES) == 15
ADJ = [0] * 20
for i, j in PET_EDGES:
    for u, v in ((i, j + 10), (j, i + 10)):
        ADJ[u] |= 1 << v
        ADJ[v] |= 1 << u
assert all(a.bit_count() == 3 for a in ADJ)
assert sum(a.bit_count() for a in ADJ) // 2 == 30

# Exhaustive face enumeration by vertex extension, including empty face.
FACES = [0]
for v in range(20):
    FACES += [s | (1 << v) for s in FACES if not (ADJ[v] & s)]
assert len(FACES) == len(set(FACES)) == 6212
BY_DIM = {k: sorted(s for s in FACES if s.bit_count() == k + 1)
          for k in range(-1, 10)}
F_VECTOR = tuple(len(BY_DIM[k]) for k in range(10))
assert F_VECTOR == (20, 160, 660, 1510, 1924, 1320, 480, 115, 20, 2)

# Exact ranks over F_2: each column is a single arbitrary-precision binary vector.
def boundary_rank_mod2(k):
    lower = {face: i for i, face in enumerate(BY_DIM[k - 1])}
    pivots = {}
    for face in BY_DIM[k]:
        column = 0
        remaining = face
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            column ^= 1 << lower[face ^ bit]
        while column:
            lead = column.bit_length() - 1
            if lead not in pivots:
                pivots[lead] = column
                break
            column ^= pivots[lead]
    return len(pivots)
RANKS = {k: boundary_rank_mod2(k) for k in range(10)}
BETTI_F2 = {k: len(BY_DIM[k]) - RANKS[k] - RANKS.get(k + 1, 0)
            for k in range(10)}
assert tuple(RANKS[k] for k in range(10)) == (1,19,141,519,991,932,383,97,18,2)
assert {k: b for k, b in BETTI_F2.items() if b} == {4: 1, 5: 5}

# Petersen strongly regular identity A^2=2I-A+J, an invertible adjacency matrix.
A = [[0] * 10 for _ in range(10)]
for u, v in PET_EDGES:
    A[u][v] = A[v][u] = 1
assert all(sum(A[i][t] * A[t][j] for t in range(10)) ==
           2 * (i == j) - A[i][j] + 1
           for i in range(10) for j in range(10))


def cycletype(p):
    seen, sizes = set(), []
    for v in range(5):
        if v in seen:
            continue
        w, n = v, 0
        while w not in seen:
            seen.add(w)
            n += 1
            w = p[w]
        sizes.append(n)
    return tuple(sorted(sizes, reverse=True))


def act_on_vertices(p, flip):
    pi = [P_INDEX[tuple(sorted((p[a], p[b])))] for a, b in P]
    return tuple(pi[i % 10] + 10 * ((i // 10) ^ flip) for i in range(20))


def fixed_orbit_euler(g):
    """Lefschetz reduced Euler trace via independent unions of vertex orbits."""
    seen = set()
    allowed = []
    for x in range(20):
        if x in seen:
            continue
        y, orbit = x, 0
        while y not in seen:
            seen.add(y)
            orbit |= 1 << y
            y = g[y]
        if any(ADJ[v] & orbit for v in range(20) if orbit >> v & 1):
            continue
        allowed.append(orbit)
    q = len(allowed)
    conflict = [0] * q
    for i, o in enumerate(allowed):
        for j, o2 in enumerate(allowed):
            if i != j and any(ADJ[v] & o2 for v in range(20) if o >> v & 1):
                conflict[i] |= 1 << j
    @lru_cache(None)
    def independent_at_minus_one(mask):
        if not mask:
            return 1
        bit = mask & -mask
        i = bit.bit_length() - 1
        return (independent_at_minus_one(mask ^ bit)
                - independent_at_minus_one(mask & ~(bit | conflict[i])))
    return -independent_at_minus_one((1 << q) - 1)


def direct_signed_euler(g):
    """Independent Lefschetz evaluation using oriented fixed simplices."""
    ans = -1  # Empty face of augmented complex, degree -1.
    for face in FACES[1:]:
        verts = [i for i in range(20) if face & (1 << i)]
        moved = [g[i] for i in verts]
        if sum(1 << j for j in moved) != face:
            continue
        inv = sum(moved[i] > moved[j] for i in range(len(moved))
                  for j in range(i + 1, len(moved)))
        ans += -1 if ((len(verts) - 1 + inv) & 1) else 1
    return ans

E_TABLE = {
    (1, 1, 1, 1, 1): -4,
    (2, 1, 1, 1): -4,
    (2, 2, 1): 0,
    (3, 1, 1): -1,
    (3, 2): -1,
    (4, 1): -2,
    (5,): 1,
}
CLASS = defaultdict(list)
for perm in permutations(range(5)):
    c = cycletype(perm)
    sgn = (-1) ** (5 - len(c))
    fixed = sum(perm[i] == i for i in range(5))
    for flip in (0, 1):
        g = act_on_vertices(perm, flip)
        assert len(set(g)) == 20
        assert all(bool(ADJ[i] >> j & 1) == bool(ADJ[g[i]] >> g[j] & 1)
                   for i in range(20) for j in range(20))
        e = fixed_orbit_euler(g)
        assert e == ((-1) ** flip) * E_TABLE[c]
        chi4 = sgn * ((-1) ** flip)
        chi5 = fixed * ((-1) ** flip)
        assert chi4 - chi5 == e
        CLASS[(c, flip)].append((g, e, chi4, chi5))

assert sum(len(v) for v in CLASS.values()) == 240 and len(CLASS) == 14
# One representative per conjugacy class is independently verified by signed chains.
for key, vals in CLASS.items():
    assert direct_signed_euler(vals[0][0]) == vals[0][1]

# The displayed character in degree 5 is the signed five-point permutation character.
# The displayed character in degree 4 is sign(S5)*sign(layer swap).
# Over Q, the mod-two ranks bound b_4<=1, b_5<=5; Euler imposes b_5=b_4+4.
# If b_4 were zero, a transposition would act trivially on H_5 of dimension 4,
# making all of S5 trivial, contradicting its 3-cycle Euler trace.
# Thus b_4=1, b_5=5. A 1D S5 character is trivial or sign; the former is
# excluded by the same argument. Finally the layer flip must act negatively
# on H_4: otherwise the + eigenspace in degree 5 has the sign character,
# which does not occur in the natural five-point permutation module.
assert E_TABLE[(2, 1, 1, 1)] == E_TABLE[(1, 1, 1, 1, 1)] == -4
assert E_TABLE[(3, 1, 1)] == -1

GROUPS = {
    'S5': lambda c, flip: flip == 0,
    'A5': lambda c, flip: flip == 0 and ((5 - len(c)) % 2 == 0),
    'deck_C2': lambda c, flip: c == (1, 1, 1, 1, 1),
    'full_G': lambda c, flip: True,
}
INVARIANTS = {}
for name, criterion in GROUPS.items():
    chosen = [v for (c, f), vals in CLASS.items() if criterion(c, f)
              for v in vals]
    sum4 = sum(v[2] for v in chosen)
    sum5 = sum(v[3] for v in chosen)
    assert sum4 % len(chosen) == sum5 % len(chosen) == 0
    INVARIANTS[name] = (sum4 // len(chosen), sum5 // len(chosen))
assert INVARIANTS == {'S5': (0, 1), 'A5': (1, 1),
                      'deck_C2': (0, 0), 'full_G': (0, 0)}

print('Graph: Petersen bipartite double cover = Desargues (20 vertices, 30 edges)')
print('Face vector:', F_VECTOR, '; nonempty total', len(FACES) - 1)
print('Augmented F2 boundary ranks:', tuple(RANKS[k] for k in range(10)))
print('Reduced F2 Betti:', BETTI_F2)
print('Full group: S5 x C2, 240 verified automorphisms; 14 conjugacy classes')
print('Class cycle_type / count / E(flip=0) / E(flip=1) / H4(flip=0) / H5(flip=0):')
for c in sorted(E_TABLE, key=lambda c: (5-len(c), c)):
    row = CLASS[(c, 0)]
    print(c, len(row), row[0][1], CLASS[(c,1)][0][1], row[0][2], row[0][3])
print('All 240 orbit-polynomial traces checked; 14 direct signed-chain traces match')
print('Invariant dimensions (H4,H5):', INVARIANTS)
print('DESARGUES_SIGNED_PERMUTATION_HOMOLOGY_PASS')

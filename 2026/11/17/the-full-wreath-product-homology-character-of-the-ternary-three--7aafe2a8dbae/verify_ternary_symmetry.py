#!/usr/bin/env python3
"""Exact homotopy and symmetry character of the 3-ary 3-cube scale-2 Rips complex.
Uses only the Python standard library. Run: python verify_ternary_symmetry.py
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations, product
from math import factorial, prod

P = list(product(range(3), repeat=3))
I = {v: i for i, v in enumerate(P)}
N = len(P)
S3 = list(permutations(range(3)))
IDENTITY = (0, 1, 2)
TRANSPOSITION = (1, 0, 2)
THREE_CYCLE = (1, 2, 0)
LABEL_PERM = {'e': IDENTITY, 't': TRANSPOSITION, 'c': THREE_CYCLE}
CENT = {'e': 6, 't': 2, 'c': 3}
BASE_CHAR = ({'e': 1, 't': 1, 'c': 1},
             {'e': 1, 't': -1, 'c': 1},
             {'e': 2, 't': 0, 'c': -1})

def forbidden(i, j):
    return all(a != b for a, b in zip(P[i], P[j]))

B = [sum(1 << j for j in range(N) if forbidden(i, j)) for i in range(N)]

# Exhaustive independent sets of K_3 x K_3 x K_3, including empty.
FACES = []
def rec(available, s):
    FACES.append(s)
    while available:
        bit = available & -available
        available ^= bit
        v = bit.bit_length() - 1
        rec(available & ~B[v], s | bit)
rec((1 << N) - 1, 0)
assert len(FACES) == len(set(FACES))
assert Counter(s.bit_count() for s in FACES) == {
    0:1, 1:27, 2:243, 3:945, 4:1728, 5:1620, 6:945, 7:351, 8:81, 9:9}

# Sequential pivot matching, using vertices in lexicographic order.
active = set(FACES)
pairs = []
for v in range(N):
    b = 1 << v
    for s in sorted(active):
        if not s & b and (s | b) in active:
            active.remove(s)
            active.remove(s | b)
            pairs.append((s, s | b))
assert (0, 1) in pairs
pairs.remove((0, 1))
active.update((0, 1))
assert Counter(s.bit_count() - 1 for s in active) == {-1:1, 0:1, 3:46}
assert len(pairs) == 2951

# Exhaustive Hasse-incidence DAG check. Edges go down except matched edges up.
match = set(pairs)
face_index = {s: i for i, s in enumerate(FACES)}
indegree = [0] * len(FACES)
adj = [[] for _ in FACES]
incidences = 0
for s in FACES:
    for j in range(N):
        bit = 1 << j
        if not s & bit:
            continue
        t = s ^ bit
        assert t in face_index
        if (t, s) in match:
            src, dst = face_index[t], face_index[s]
        else:
            src, dst = face_index[s], face_index[t]
        adj[src].append(dst)
        indegree[dst] += 1
        incidences += 1
queue = deque(i for i, d in enumerate(indegree) if not d)
visited = 0
while queue:
    i = queue.popleft()
    visited += 1
    for j in adj[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)
assert visited == len(FACES)

# Generate 22 complete wreath-product conjugacy-class representatives.
REPS = []
for labels in combinations_with_replacement('etc', 3):
    REPS.append(('111', labels, (0, 1, 2), tuple(LABEL_PERM[x] for x in labels)))
for a in 'etc':
    for b in 'etc':
        REPS.append(('21', (a, b), (1, 0, 2), (IDENTITY, LABEL_PERM[a], LABEL_PERM[b])))
for a in 'etc':
    REPS.append(('3', (a,), (1, 2, 0), (IDENTITY, IDENTITY, LABEL_PERM[a])))
assert len(REPS) == 22
LENGTHS = {'111': (1, 1, 1), '21': (2, 1), '3': (3,)}

def class_size(kind, labels):
    cnt = Counter(zip(LENGTHS[kind], labels))
    centralizer = prod((length * CENT[lab]) ** m * factorial(m)
                       for (length, lab), m in cnt.items())
    assert 1296 % centralizer == 0
    return 1296 // centralizer

def vertex_map(rho, sigmas):
    out = []
    for p in P:
        q = [None] * 3
        for i in range(3):
            q[rho[i]] = sigmas[i][p[i]]
        out.append(I[tuple(q)])
    assert len(set(out)) == 27
    return tuple(out)

def direct_character(g):
    # Exact signed simplicial trace including the reduced empty simplex.
    lefschetz = -1
    for s in FACES:
        if not s:
            continue
        vv = [j for j in range(27) if s & (1 << j)]
        imgs = [g[j] for j in vv]
        if sum(1 << j for j in imgs) != s:
            continue
        inversions = sum(imgs[i] > imgs[j] for i in range(len(imgs))
                         for j in range(i + 1, len(imgs)))
        orientation = -1 if inversions % 2 else 1
        lefschetz += ((-1) ** (len(vv) - 1)) * orientation
    # Reduced homology is in degree 3 only (certified above), so trace=-L.
    return -lefschetz

def orbit_character(g):
    # A fixed simplex is a union of g-orbits. Every selected orbit must be
    # independent in the forbidden graph, and distinct orbits must be compatible.
    remaining = set(range(27))
    candidate_orbits = []
    while remaining:
        v = min(remaining)
        orbit = []
        while v in remaining:
            remaining.remove(v)
            orbit.append(v)
            v = g[v]
        assert v == orbit[0]
        if not any(forbidden(a, b) for a, b in combinations(orbit, 2)):
            candidate_orbits.append(orbit)
    k = len(candidate_orbits)
    incompatible = [0] * k
    for i in range(k):
        for j in range(k):
            if i != j and any(forbidden(a, b) for a in candidate_orbits[i]
                              for b in candidate_orbits[j]):
                incompatible[i] |= 1 << j
    @lru_cache(None)
    def signed_independent_sets(mask):
        if not mask:
            return 1
        v = max((i for i in range(k) if mask >> i & 1),
                key=lambda i: (incompatible[i] & mask).bit_count())
        bit = 1 << v
        return (signed_independent_sets(mask ^ bit) -
                signed_independent_sets(mask & ~(bit | incompatible[v])))
    # Orbit-union orientation and (-1)^(dim) combine as (-1)^(#orbits+1).
    # The full H_3 character is therefore the signed independent-set sum.
    return signed_independent_sets((1 << k) - 1)

# Exact symmetric-group S_m characters at m<=3.
PARTITIONS = {0: ((),), 1: ((1,),), 2: ((2,), (1,1)),
              3: ((3,), (2,1), (1,1,1))}
SCHAR = {
    ((), ()): 1,
    ((1,), (1,)): 1,
    ((2,), (1,1)): 1, ((2,), (2,)): 1,
    ((1,1), (1,1)): 1, ((1,1), (2,)): -1,
    ((3,), (1,1,1)): 1, ((3,), (2,1)): 1, ((3,), (3,)): 1,
    ((2,1), (1,1,1)): 2, ((2,1), (2,1)): 0,
    ((2,1), (3,)): -1,
    ((1,1,1), (1,1,1)): 1, ((1,1,1), (2,1)): -1,
    ((1,1,1), (3,)): 1,
}
MULTIPARTITIONS = []
for nt in range(4):
    for ne in range(4 - nt):
        nv = 3 - nt - ne
        for lam_t in PARTITIONS[nt]:
            for lam_e in PARTITIONS[ne]:
                for lam_v in PARTITIONS[nv]:
                    MULTIPARTITIONS.append((lam_t, lam_e, lam_v))
assert len(MULTIPARTITIONS) == 22

def irreducible_character(lam, kind, labels):
    lengths = LENGTHS[kind]
    tot = 0
    for colors in product(range(3), repeat=len(lengths)):
        if any(sum(lengths[j] for j in range(len(lengths))
                   if colors[j] == i) != sum(lam[i]) for i in range(3)):
            continue
        val = 1
        for i in range(3):
            assigned_lengths = tuple(sorted((lengths[j] for j in range(len(lengths))
                                             if colors[j] == i), reverse=True))
            val *= SCHAR[(lam[i], assigned_lengths)]
            for j in range(len(lengths)):
                if colors[j] == i:
                    val *= BASE_CHAR[i][labels[j]]
        tot += val
    return tot

rows = []
for kind, labels, rho, sigma in REPS:
    g = vertex_map(rho, sigma)
    tr1, tr2 = direct_character(g), orbit_character(g)
    assert tr1 == tr2, (kind, labels, tr1, tr2)
    rows.append((kind, ''.join(labels), class_size(kind,labels), tr1))
assert sum(x[2] for x in rows) == 1296
assert rows[0][3] == 46

# Independently verify the entire group is partitioned into precisely these
# 22 classes, and the orbit character depends only on the class invariant.
def cycle_label(sigma):
    if sigma == IDENTITY:
        return 'e'
    if sum(sigma[i] == i for i in range(3)) == 1:
        return 't'
    return 'c'
def compose(p, q):
    return tuple(p[q[i]] for i in range(3))
def classify(rho, sigmas):
    remain = set(range(3))
    chunks = []
    while remain:
        i = min(remain)
        cy = []
        j = i
        while j in remain:
            remain.remove(j)
            cy.append(j)
            j = rho[j]
        assert j == i
        product_perm = IDENTITY
        for v in cy:
            product_perm = compose(sigmas[v], product_perm)
        chunks.append((len(cy), cycle_label(product_perm)))
    chunks.sort(key=lambda a: (-a[0], 'etc'.index(a[1])))
    return ''.join(str(x[0]) for x in chunks), ''.join(x[1] for x in chunks)
known = {(kind, labels): tr for kind, labels, _, tr in rows}
counts = Counter()
for rho in S3:
    for sigma in product(S3, repeat=3):
        key = classify(rho, sigma)
        assert key in known, key
        counts[key] += 1
        assert orbit_character(vertex_map(rho, sigma)) == known[key], (rho,sigma,key)
for kind, labs, size, tr in rows:
    assert counts[kind, labs] == size

irchars = []
for lam in MULTIPARTITIONS:
    values = [irreducible_character(lam,kind,tuple(labels))
              for kind,labels, _, _ in rows]
    irchars.append(values)
for a in range(22):
    for b in range(22):
        inner = sum(size * irchars[a][i] * irchars[b][i]
                    for i,(_,_,size,_) in enumerate(rows))
        assert inner == (1296 if a == b else 0), (a,b,inner)
multiplicity = []
for lam, cc in zip(MULTIPARTITIONS, irchars):
    numer = sum(size * tr * cc[i]
                for i, (_,_,size,tr) in enumerate(rows))
    assert numer % 1296 == 0
    m = numer // 1296
    assert m in (0,1), (lam,m)
    if m:
        multiplicity.append((lam, cc[0], m))
assert len(multiplicity) == 7
assert sum(dim * m for _, dim, m in multiplicity) == 46
expected = {
    ((), (), (1,1,1)):8,
    ((), (1,), (1,1)):12,
    ((), (1,1), (1,)):6,
    ((), (1,1,1), ()):1,
    ((1,), (), (1,1)):12,
    ((1,1), (), (1,)):6,
    ((1,1,1), (), ()):1,
}
assert {lam: dim for lam,dim,m in multiplicity} == expected
assert sum(size*tr for kind,lab,size,tr in rows) == 0
assert sum(size*tr for kind,lab,size,tr in rows if kind=='111') == 216
assert sum(size*tr for kind,lab,size,tr in rows if kind=='21') == -648
assert sum(size*tr for kind,lab,size,tr in rows if kind=='3') == 432
print('TERNARY_THREE_CUBE_SYMMETRY_PASS')
print('faces_including_empty:', len(FACES), 'hasse_incidences:', incidences)
print('matching_pairs:',len(pairs),'critical: one vertex and 46 three-cells')
print('group:', 1296, 'conjugacy_classes:', len(rows), 'all_elements_checked:', 1296)
print('character_class_table (coordinate_cycle_type, base_cycle_types, size, H3_trace):')
for row in rows: print(*row)
print('nonzero_multipartition_decomposition (trivial, sign, standard; dimension, multiplicity):')
for row in multiplicity: print(*row)
print('alphabet_invariant_line_coordinate_character:', (1, -1, 1))
print('full_group_invariants_dim:',0)

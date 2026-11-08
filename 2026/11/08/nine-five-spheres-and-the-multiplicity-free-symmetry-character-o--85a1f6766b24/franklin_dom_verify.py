#!/usr/bin/env python3
"""Exact, standalone certificate for a finite dominance complex and symmetry character.
Python 3.10+ standard library only. Run: python3 franklin_dom_verify.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations

n = 12
edges = {tuple(sorted((i, (i + 1) % n))) for i in range(n)}
for i in range(n):
    edges.add(tuple(sorted((i, (i + (5 if i % 2 == 0 else -5)) % n))))
assert len(edges) == 18
adj = [set() for _ in range(n)]
for a, b in edges:
    adj[a].add(b); adj[b].add(a)
assert all(len(x) == 3 for x in adj)
closed = [sum(1 << u for u in adj[v] | {v}) for v in range(n)]
full = (1 << n) - 1

def face(m):
    return not any(m & N == N for N in closed)

def dominating_complement(m):
    D = full ^ m
    return all((D >> v & 1) or any(D >> u & 1 for u in adj[v]) for v in range(n))

faces = {m for m in range(1 << n) if face(m)}
assert all(face(m) == dominating_complement(m) for m in range(1 << n))
assert 0 in faces and len(faces) == 2417
fdim = Counter(m.bit_count() - 1 for m in faces)
assert [fdim.get(i, 0) for i in range(-1, 8)] == [1, 12, 66, 220, 483, 696, 612, 276, 51]

# A partial matching on the nonempty face poset, specified by successive toggles.
remaining = faces - {0}
pairs = []
for v in range(n):
    bit = 1 << v
    for m in sorted(remaining):
        if not m & bit and (m | bit) in remaining:
            remaining.remove(m)
            remaining.remove(m | bit)
            pairs.append((m, m | bit))
assert len(pairs) == 1203
assert Counter(m.bit_count() - 1 for m in remaining) == {0: 1, 5: 9}
matched = {(low, high) for low, high in pairs}
assert len({x for a, b in pairs for x in (a, b)}) == 2 * len(pairs)

# Directed Hasse diagram: reverse matching incidences, all others go down.
nonempty = faces - {0}
indegree = {m: 0 for m in nonempty}
out = {m: [] for m in nonempty}
cover_count = 0
for high in nonempty:
    for v in range(n):
        if not high >> v & 1:
            continue
        low = high & ~(1 << v)
        if low == 0:
            continue
        cover_count += 1
        if (low, high) in matched:
            a, b = low, high
        else:
            a, b = high, low
        out[a].append(b)
        indegree[b] += 1
assert len(matched) == len(pairs)
queue = deque(v for v in nonempty if indegree[v] == 0)
visited = 0
while queue:
    u = queue.popleft(); visited += 1
    for v in out[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
assert visited == len(nonempty), 'Matching has a directed cycle'

# Independent mod-two chain calculation, with the augmentation chain at degree -1.
rank = {}
for d in range(0, 8):
    lower = sorted(m for m in faces if m.bit_count() == d)
    upper = sorted(m for m in faces if m.bit_count() == d + 1)
    index = {m: i for i, m in enumerate(lower)}
    basis = {}
    for m in upper:
        col = 0
        for v in range(n):
            if m >> v & 1:
                col ^= 1 << index[m & ~(1 << v)]
        while col:
            p = col.bit_length() - 1
            if p in basis:
                col ^= basis[p]
            else:
                basis[p] = col
                break
    rank[d] = len(basis)
assert {d: len([m for m in faces if m.bit_count() == d + 1]) - rank[d] - rank.get(d + 1, 0)
        for d in range(8)} == {0:0,1:0,2:0,3:0,4:0,5:9,6:0,7:0}

# Exhaustively enumerate graph automorphisms by adjacency-preserving backtracking.
def automorphisms():
    results = []
    def visit(assign, unused):
        if len(assign) == n:
            results.append(tuple(assign[i] for i in range(n)))
            return
        v = max((i for i in range(n) if i not in assign),
                key=lambda i: (len(adj[i] & assign.keys()), -i))
        for w in sorted(unused):
            if all(((u in adj[v]) == (assign[u] in adj[w])) for u in assign):
                assign[v] = w
                visit(assign, unused - {w})
                del assign[v]
    visit({}, set(range(n)))
    return sorted(set(results))

group = automorphisms()
assert len(group) == 48
for p in group:
    assert all(tuple(sorted((p[a], p[b]))) in edges for a, b in edges)
perms = {p: i for i, p in enumerate(group)}
identity = perms[tuple(range(n))]
def compose(a, b):
    return tuple(a[b[i]] for i in range(n))
table = [[perms[compose(a, b)] for b in group] for a in group]
def inv(i):
    return next(j for j in range(len(group)) if table[i][j] == identity and table[j][i] == identity)
inverses = [inv(i) for i in range(len(group))]
center = [i for i in range(len(group)) if all(table[i][j] == table[j][i] for j in range(len(group)))]
z = perms[tuple((i + 6) % n for i in range(n))]
assert center == sorted([identity, z])

def orient_sign(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq))) % 2 else 1

def direct_lefschetz(p):
    total = 0
    for m in faces:
        vs = [i for i in range(n) if m >> i & 1]
        moved = [p[i] for i in vs]
        if sum(1 << j for j in moved) != m:
            continue
        total += (1 if len(vs) % 2 else -1) * orient_sign(moved)
    return total

def cycle_lefschetz(p):
    orbit_masks = []
    seen = set()
    for v in range(n):
        if v in seen:
            continue
        u = v; orbit = []
        while u not in seen:
            seen.add(u); orbit.append(u); u = p[u]
        orbit_masks.append(sum(1 << x for x in orbit))
    total = 0
    for selector in range(1 << len(orbit_masks)):
        m = 0
        for i, orbit in enumerate(orbit_masks):
            if selector >> i & 1:
                m |= orbit
        if face(m):
            cycle_sign = (-1) ** sum((orbit.bit_count() - 1) for i, orbit in enumerate(orbit_masks) if selector >> i & 1)
            total += (1 if m.bit_count() % 2 else -1) * cycle_sign
    return total

chi = []
for p in group:
    lefschetz = direct_lefschetz(p)
    assert lefschetz == cycle_lefschetz(p)
    # All reduced homology is in dimension five.
    chi.append(-lefschetz)
assert chi[identity] == 9 and chi[z] == -1
assert sum(chi) == 0 and sum(t*t for t in chi) == 48 * 5

# Construct an explicit splitting Aut(F)=H x <z>, with H acting faithfully
# on four Sylow-three subgroups and hence H isomorphic to S4.
rows = []
for i in range(48):
    for j in range(48):
        rows.append((1 << i) ^ (1 << j) ^ (1 << table[i][j]))
rows.extend([1 << identity, (1 << z) | (1 << 48)])
basis = {}
for x in rows:
    while x:
        b = (x & ((1 << 48) - 1)).bit_length() - 1
        if b < 0:
            assert not (x >> 48 & 1)
            break
        if b in basis:
            x ^= basis[b]
        else:
            basis[b] = x
            break
solution = 0
for b in sorted(basis):
    eq = basis[b]
    if ((eq >> 48) & 1) ^ ((eq & solution).bit_count() % 2):
        solution |= 1 << b
assert solution >> z & 1
assert all(((solution >> table[i][j]) & 1) == (((solution >> i) & 1) ^ ((solution >> j) & 1))
           for i in range(48) for j in range(48))
H = [i for i in range(48) if not (solution >> i & 1)]
assert len(H) == 24

def order(i):
    cur = i; k = 1
    while cur != identity:
        cur = table[cur][i]; k += 1
    return k
sylow3 = sorted({tuple(sorted((identity, i, table[i][i]))) for i in H if order(i) == 3})
assert len(sylow3) == 4
sylowidx = {q: i for i, q in enumerate(sylow3)}
S4map = {}
for h in H:
    image = []
    for q in sylow3:
        conj = tuple(sorted(table[table[h][a]][inverses[h]] for a in q))
        image.append(sylowidx[conj])
    S4map[h] = tuple(image)
assert len(set(S4map.values())) == 24

def cycle_type(p):
    seen = set(); sizes = []
    for i in range(len(p)):
        if i not in seen:
            j = i; k = 0
            while j not in seen:
                seen.add(j); k += 1; j = p[j]
            sizes.append(k)
    return tuple(sorted(sizes, reverse=True))

@lru_cache(None)
def tabloid_char(alpha, cyc):
    if min(alpha) < 0 or sum(alpha) != sum(cyc):
        return 0
    def fit(j, rem):
        if j == len(cyc):
            return int(all(x == 0 for x in rem))
        count = 0
        for i in range(len(rem)):
            if rem[i] >= cyc[j]:
                nxt = list(rem); nxt[i] -= cyc[j]
                count += fit(j + 1, tuple(nxt))
        return count
    return fit(0, alpha)

def irreducible_S4(lam, cyc):
    k = len(lam)
    return sum(orient_sign(p) * tabloid_char(tuple(lam[i] - i + p[i] for i in range(k)), cyc)
             for p in permutations(range(k)))

parts = [(4,), (3,1), (2,2), (2,1,1), (1,1,1,1)]
conj = defaultdict(list)
for h in H:
    conj[cycle_type(S4map[h])].append(h)
assert all(len({chi[h] for h in hs}) == 1 and len({chi[table[z][h]] for h in hs}) == 1 for hs in conj.values())
assert sorted((key, len(val)) for key, val in conj.items()) == sorted([
    ((1,1,1,1),1),((2,1,1),6),((2,2),3),((3,1),8),((4,),6)])
decomposition = []
for lam in parts:
    for epsilon in (1, -1):
        numerator = 0
        for cyc, hs in conj.items():
            h = hs[0]
            numerator += len(hs) * irreducible_S4(lam, cyc) * (chi[h] + epsilon * chi[table[z][h]])
        assert numerator % 48 == 0
        multiplicity = numerator // 48
        assert multiplicity >= 0
        if multiplicity:
            decomposition.append((lam, epsilon, multiplicity))
assert sum((irreducible_S4(lam,(1,1,1,1)) * mult) for lam, eps, mult in decomposition) == 9
assert sum(mult * mult for lam, eps, mult in decomposition) == 5

print('GRAPH vertices=12 edges=18 automorphisms=48 center=(identity, shift-by-6)')
print('FACE_VECTOR dimensions -1..7:', [fdim[d] for d in range(-1,8)])
print('MATCHING pairs=', len(pairs), 'critical=', sorted(Counter(m.bit_count()-1 for m in remaining).items()),
      'cover_relations=', cover_count, 'acyclic_vertices=', visited)
print('BOUNDARY_RANKS_MOD2 degrees 0..7:', [rank[d] for d in range(8)])
print('HOMOLOGY integral: reduced H5=Z^9 only (by discrete Morse)')
print('CHARACTER_H5 value_multiset=',sorted(Counter(chi).items()),'invariants=',sum(chi)//48,'inner_product=',sum(t*t for t in chi)//48)
print('CENTRAL_INVOLUTION_H5 trace=', chi[z], 'even_dim=', (9+chi[z])//2,'odd_dim=',(9-chi[z])//2)
print('S4_X_C2_CONJUGACY classes (cycle_type,size,chi_plus,chi_minus):')
for c, hs in sorted(conj.items()):
    h = hs[0]
    print(' ',c,len(hs),chi[h],chi[table[z][h]])
print('S4_X_C2_IRRED_DECOMPOSITION (partition,central_sign,multiplicity):',decomposition)
print('FRANKLIN_DOMINANCE_TOPOLOGY_CHARACTER_PASS')

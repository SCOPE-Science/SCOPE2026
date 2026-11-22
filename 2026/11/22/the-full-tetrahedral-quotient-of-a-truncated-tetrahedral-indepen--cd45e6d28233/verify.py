"""Reconstructs a finite regular CW orbit complex and a complete homotopy certificate.
Only Python 3 standard-library modules are needed. Run: python verify.py
"""
import json
from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path

V = tuple(permutations(range(4), 2))
index = {vertex: i for i, vertex in enumerate(V)}
E = {
    (i, j)
    for i, (a, b) in enumerate(V)
    for j, (c, d) in enumerate(V)
    if i < j and (a == c or (a == d and b == c))
}
assert len(V) == 12 and len(E) == 18

faces = []
for k in range(1, 13):
    for f in combinations(range(12), k):
        if not any(u in f and v in f for (u, v) in E):
            faces.append(f)
assert dict(Counter(len(f) - 1 for f in faces)) == {0: 12, 1: 48, 2: 72, 3: 30}

# Every graph automorphism induced by a tetrahedral label permutation.
G = [tuple(index[p[a], p[b]] for a, b in V) for p in permutations(range(4))]
assert len(set(G)) == 24

def image(face, g):
    return tuple(sorted(g[v] for v in face))

def image_flag(flag, g):
    return tuple(image(f, g) for f in flag)

def canonical(flag):
    return min(image_flag(flag, g) for g in G)

# A flag in the barycentric subdivision is a nonempty strict face chain.
# This enumerates all ordered face chains, including rank-skipping chains.
cache = {}
def all_chains_ending(face):
    if face in cache:
        return cache[face]
    result = [(face,)]
    for k in range(1, len(face)):
        for subset in combinations(face, k):
            for chain in all_chains_ending(subset):
                result.append(chain + (face,))
    cache[face] = tuple(result)
    return cache[face]

flags = [chain for f in faces for chain in all_chains_ending(f)]
assert len(flags) == 3342
cells = sorted({canonical(flag) for flag in flags}, key=lambda c: (len(c), c))
assert len(cells) == 146
assert dict(Counter(len(c)-1 for c in cells)) == {0:11, 1:42, 2:63, 3:30}
cidx = {cell: i for i, cell in enumerate(cells)}
faces_of = {
    i: tuple(cidx[canonical(cell[:j] + cell[j + 1:])] for j in range(len(cell)))
    for i, cell in enumerate(cells) if len(cell) > 1
}
assert all(len(set(v)) == len(v) for v in faces_of.values())

# A regular cellular free-face collapse: the lower cell has one higher
# incidence, the higher cell is maximal, and the incidence has degree 1.
active = set(range(len(cells)))
certificate = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
assert certificate['initial_cells_by_dimension'] == [11,42,63,30]
for lo, hi in certificate['collapses']:
    assert lo in active and hi in active
    assert lo in faces_of[hi] and len(cells[hi]) == len(cells[lo]) + 1
    assert [i for i in active if lo in faces_of.get(i, ())] == [hi]
    assert not any(hi in faces_of.get(i, ()) for i in active)
    active.remove(lo)
    active.remove(hi)
assert len(certificate['collapses']) == 60
assert Counter(len(cells[i])-1 for i in active) == {0:6, 1:12, 2:8}
assert max(len(cells[i]) for i in active) == 3

vertices = sorted(i for i in active if len(cells[i]) == 1)
edges = sorted(i for i in active if len(cells[i]) == 2)
triangles = sorted(i for i in active if len(cells[i]) == 3)
endpoints = {e: faces_of[e] for e in edges}  # (higher-rank vertex, lower-rank vertex)
reachable = {vertices[0]}
tree = set()
while True:
    new_edge = next((e for e in edges if (endpoints[e][0] in reachable) != (endpoints[e][1] in reachable)), None)
    if new_edge is None:
        break
    tree.add(new_edge)
    reachable.update(endpoints[new_edge])
assert len(reachable) == 6 and len(tree) == 5
assert sorted(tree) == certificate['tree_edges']
non_tree = sorted(set(edges) - tree)
assert non_tree == certificate['generator_edges']
number = {e: i + 1 for i, e in enumerate(non_tree)}

def oriented_edge(e, u, v):
    if e in tree:
        return []
    assert {u,v} == set(endpoints[e])
    return [number[e] if (u, v) == tuple(reversed(endpoints[e])) else -number[e]]

def reduce_word(seq):
    out = []
    for x in seq:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out

def inverse(seq):
    return [-x for x in reversed(seq)]

words = []
for t in triangles:
    A, B, C = cells[t]
    a, b, c = (cidx[canonical((f,))] for f in (A,B,C))
    eBC, eAC, eAB = faces_of[t]
    assert set(endpoints[eAB]) == {a,b}
    assert set(endpoints[eBC]) == {b,c}
    assert set(endpoints[eAC]) == {a,c}
    words.append(reduce_word(oriented_edge(eAB,a,b)+oriented_edge(eBC,b,c)+oriented_edge(eAC,c,a)))
assert triangles == certificate['triangle_cells']
assert words == certificate['attaching_words']

# Relators with a generator appearing exactly once permit elementary
# 1-cell/2-cell cancellation, preserving the homotopy type of the 2-complex.
remaining_generators = set(number.values())
for step in certificate['generator_eliminations']:
    g = step['generator']
    j = step['relator_index']
    word = words[j]
    k = step['occurrence_index']
    assert g in remaining_generators and abs(word[k]) == g
    assert sum(abs(x) == g for x in word) == 1
    cycle = word[k+1:] + word[:k]
    substitution = reduce_word(inverse(cycle) if word[k] > 0 else cycle)
    assert substitution == step['replacement']
    assert all(abs(x) != g for x in substitution)
    updated = []
    for h, rel in enumerate(words):
        if h == j:
            continue
        new_relator = []
        for x in rel:
            new_relator.extend(
                (substitution if x > 0 else inverse(substitution)) if abs(x) == g else [x]
            )
        updated.append(reduce_word(new_relator))
    words = updated
    remaining_generators.remove(g)
assert remaining_generators == set() and words == [[]]
# One vertex, one 2-cell with constant attaching map: S^2.
print('FACE_F_VECTOR', [12,48,72,30]);print('FLAG_ORBITS', [11,42,63,30])
print('VALID_ELEMENTARY_COLLAPSES', len(certificate['collapses']))
print('REMAINING_CELLS', [6,12,8])
print('SPANNING_TREE', sorted(tree))
print('GENERATOR_CANCELLATIONS', len(certificate['generator_eliminations']))
print('TERMINAL_CW', [1,0,1]); print('TRUNCATED_TETRA_ORBIT_SPHERE_OK')

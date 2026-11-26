#!/usr/bin/env python3
"""Finite cellular certificate for the 7-rotation quotient of the K7 matching complex.

The free action and homotopy-preserving 2-cell eliminations are explained in RESULT.md.
Uses Python 3 standard library only. Run: python3 VERIFY_M7_C7.py
"""
from itertools import combinations
from collections import Counter

N = 7
EDGES = list(combinations(range(N), 2))
INDEX = {e: i for i, e in enumerate(EDGES)}

def action_vertex(v, t):
    return INDEX[tuple(sorted(((x + t) % N for x in EDGES[v])))]

def action_face(f, t):
    return tuple(sorted(action_vertex(v, t) for v in f))

def canonical(face):
    return min(action_face(face, t) for t in range(N))

FACES = [[(v,) for v in range(len(EDGES))]]
FACES.append([f for f in combinations(range(len(EDGES)), 2)
              if set(EDGES[f[0]]).isdisjoint(EDGES[f[1]])])
FACES.append([f for f in combinations(range(len(EDGES)), 3)
              if len(set().union(*(set(EDGES[x]) for x in f))) == 6])
assert [len(f) for f in FACES] == [21, 105, 105]

REPS = [sorted({canonical(f) for f in level}) for level in FACES]
assert [len(rs) for rs in REPS] == [3, 15, 15]
MAPS = [{action_face(r, t): j for j, r in enumerate(rs)
         for t in range(N)} for rs in REPS]
for dim, level in enumerate(FACES):
    assert len(MAPS[dim]) == len(level)
    assert all(len({action_face(f, t) for t in range(N)}) == 7
               for f in level)

def oriented_cell(face):
    target = tuple(sorted(face))
    r = canonical(target)
    matching_shifts = [t for t in range(N) if action_face(r, t) == target]
    assert len(matching_shifts) == 1
    translated = [action_vertex(v, matching_shifts[0]) for v in r]
    positions = [translated.index(v) for v in face]
    parity = sum(positions[i] > positions[j]
                 for i in range(len(positions)) for j in range(i+1, len(positions))) % 2
    return MAPS[len(face)-1][target], -1 if parity else 1

# Each oriented triangle attaches along ab, bc, ca; tree edges are set to identity.
EDGE_ENDPOINTS = [(MAPS[0][(e[0],)], MAPS[0][(e[1],)])
                  for e in REPS[1]]
TREE = []
seen = {0}
while len(seen) < 3:
    choices = [i for i,(a,b) in enumerate(EDGE_ENDPOINTS)
               if (a in seen) != (b in seen)]
    assert choices
    i = min(choices)
    TREE.append(i)
    seen.update(EDGE_ENDPOINTS[i])
assert TREE == [1,2]
GENERATORS = [i for i in range(len(REPS[1])) if i not in TREE]
GEN_NO = {j: i+1 for i,j in enumerate(GENERATORS)}

def freely_reduce(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return stack

def invert(word):
    return [-x for x in word[::-1]]

INITIAL = []
for a,b,c in REPS[2]:
    boundary = [oriented_cell((a,b)), oriented_cell((b,c)), oriented_cell((c,a))]
    # Boundary of an oriented triangle is the concatenation a->b->c->a.
    assert all(isinstance(sign, int) and abs(sign) == 1 for _,sign in boundary)
    INITIAL.append(freely_reduce([GEN_NO[e]*sign for e,sign in boundary
                                 if e not in TREE]))

EXPECTED_INITIAL = [
    [1,1,3], [1,-6], [7,-4], [8,-5], [-2,-3], [12,-5],
    [-9,-6], [2,-5,-3], [2,-11,-4], [4,7,-6],
    [7,10,10], [8,-9,-10], [8,-13,-11], [9,13,-11],
    [12,12,13]
]
assert INITIAL == EXPECTED_INITIAL

# Check oriented cellular boundary composition = 0 before tree contraction.
for a,b,c in REPS[2]:
    boundary = [oriented_cell((a,b)), oriented_cell((b,c)), oriented_cell((c,a))]
    coeffs = [0] * len(REPS[0])
    for ei,sgn in boundary:
        u,v = EDGE_ENDPOINTS[ei]
        coeffs[u] -= sgn
        coeffs[v] += sgn
    assert coeffs == [0,0,0]

# A 2-cell whose attaching word uses one generator exactly once permits
# homotopy-preserving cancellation of that 2-cell and 1-cell; substitute
# the solved word into all remaining attaching maps.
WORDS = [w[:] for w in INITIAL]
TRANSCRIPT = []
while True:
    pick = None
    for ri, word in enumerate(WORDS):
        frequencies = Counter(map(abs, word))
        for pos, letter in enumerate(word):
            if frequencies[abs(letter)] == 1:
                pick = (ri, pos, letter)
                break
        if pick is not None:
            break
    if pick is None:
        break
    ri, pos, letter = pick
    word = WORDS[ri]
    rest = word[pos+1:] + word[:pos]
    solved = invert(rest) if letter > 0 else rest
    g = abs(letter)
    new = []
    for j, old in enumerate(WORDS):
        if j == ri:
            continue
        expanded = []
        for x in old:
            if abs(x) != g:
                expanded.append(x)
            else:
                expanded.extend(solved if x > 0 else invert(solved))
        new.append(freely_reduce(expanded))
    assert all(g not in {abs(x) for x in w} for w in new)
    TRANSCRIPT.append((ri, letter, len(word)))
    WORDS = new

assert TRANSCRIPT == [
    (0, 3, 3), (0, 1, 2), (0, 7, 2), (0, 8, 2),
    (0, -2, 3), (0, 12, 2), (0, -9, 2), (0, -5, 5),
    (0, -11, 4), (0, -6, 3), (0, 4, 3), (1, -13, 23)
], TRANSCRIPT
assert len(WORDS) == 3
assert {abs(x) for word in WORDS for x in word} == {10}
EXPS = [sum(1 if x == 10 else -1 for x in w) for w in WORDS]
assert sorted(map(abs, EXPS)) == [0,21,42], EXPS
assert len([w for w in WORDS if not w]) == 1
assert sum(1 for w in WORDS for x in w) == 63
assert 3 - 15 + 15 == 3
print('M7_C7_HOMOTOPY_OK')
print('simplicial_faces=21,105,105 quotient_cells=3,15,15')
print('spanning_tree=', TREE, 'remaining_circle_generators_before_elimination=',len(GENERATORS))
print('Tietze_2cell_1cell_pairs=',len(TRANSCRIPT),'presentation_power_exponents=',EXPS)
print('identified_type=M(Z/21,1) wedge S2 wedge S2')

"""Exact four-palette two-homogeneous recolouring census of the Heawood graph.
Run: python3 verify.py. Requires the Python standard library only.
"""
from itertools import product
from collections import Counter, deque

Q = range(4)
lines = [frozenset(((j) % 7, (j + 1) % 7, (j + 3) % 7)) for j in range(7)]
through = [tuple(j for j in range(7) if i in lines[j]) for i in range(7)]
assert all(len(line) == 3 for line in lines)
assert all(len(js) == 3 for js in through)
assert all(sum({a, b} <= line for line in lines) == 1
           for a in range(7) for b in range(a+1, 7))

# Method A: enumerate seven-vertex words on the two shores independently.
points = [w for w in product(Q, repeat=7)
          if all(len({w[i] for i in line}) == 2 for line in lines)]
linewords = [w for w in product(Q, repeat=7)
             if all(len({w[j] for j in js}) == 2 for js in through)]
assert len(points) == len(linewords) == 504
C = sorted(p + q for p in points for q in linewords
           if all(p[i] != q[j] for j in range(7) for i in lines[j]))
assert len(C) == 6048
assert Counter(len(set(x)) for x in C) == {3: 504, 4: 5544}

# Method B: one normalized Fano flag, plus a bounded seven-bit extension.
point_template = (2,1,0,1,0,0,0)
line_template = (0,2,2,2,1,2,1)
assert tuple(({0,1,2} - {point_template[i] for i in line}).pop()
             for line in lines) == line_template
valid_masks = []
for m in range(128):
    word = tuple(3 if (m >> j) & 1 else line_template[j] for j in range(7))
    if all(len({word[j] for j in through[i]}) == 2 for i in range(7)):
        valid_masks.append(m)
assert valid_masks == [0,1,17,23,46,57,65,75,80,92,101,114]
assert len(points)*len(valid_masks) == len(C)

# Exact single-vertex recolouring graph, without precomputed adjacency data.
index = {word:i for i,word in enumerate(C)}
adj = [set() for _ in C]
for i, word in enumerate(C):
    for v in range(14):
        for new in Q:
            if new == word[v]: continue
            candidate = word[:v] + (new,) + word[v+1:]
            j = index.get(candidate)
            if j is not None:
                adj[i].add(j)
assert all(i in adj[j] for j,ngh in enumerate(adj) for i in ngh)
deg = Counter(len(n) for n in adj)
assert deg == {0:2520, 1:2016, 2:504, 3:1008}, deg
assert all((len(adj[i]) == 2) == (len(set(word)) == 3)
           for i,word in enumerate(C))
assert {m: len(adj[index[point_template + tuple(3 if (m >> j) & 1
               else line_template[j] for j in range(7))]])
        for m in valid_masks} == {
            0:2, 1:3, 17:1, 23:0, 46:3, 57:0,
            65:1, 75:0, 80:0, 92:1, 101:0, 114:1}

# Independent graph-shape assertion: every nontrivial component is the
# seven-vertex tree with degree multiset (3,3,2,1,1,1,1).
seen = set(); component_types = Counter()
for i in range(len(C)):
    if i in seen: continue
    todo = deque([i]); seen.add(i); comp = []
    while todo:
        v = todo.popleft(); comp.append(v)
        for j in adj[v]:
            if j not in seen:
                seen.add(j); todo.append(j)
    signature = (len(comp), sum(len(adj[v]) for v in comp)//2,
                 tuple(sorted(Counter(len(adj[v]) for v in comp).items())))
    component_types[signature] += 1
assert component_types == {
  (1,0,((0,1),)):2520,
  (7,6,((1,4),(2,1),(3,2))):504,
},component_types
assert sum(len(adj[i]) for i in range(len(C)))//2 == 3024
print('FANO_SHORE_ENUMERATION_PASS',len(points),len(linewords))
print('TWELVE_MASK_FLAG_CERTIFICATE_PASS',valid_masks)
print('ALL_FOUR_PALETTE_COLOURINGS_PASS',len(C))
print('RECOLOURING_COMPONENT_STRUCTURE_PASS',component_types)
print('VERIFY_OK')

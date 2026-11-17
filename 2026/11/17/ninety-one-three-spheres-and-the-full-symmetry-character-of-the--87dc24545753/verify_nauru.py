#!/usr/bin/env python3
"""Exact, self-contained finite verification for the Nauru third non-matching complex."""
from itertools import permutations, combinations
from collections import Counter, defaultdict, deque
import json

vertices = list(permutations(range(4), 3))
vertex_index = {v: i for i, v in enumerate(vertices)}
assert len(vertices) == 24
edge_set = set()
for i, x in enumerate(vertices):
    unused = next(z for z in range(4) if z not in x)
    for coordinate in range(3):
        y = tuple(unused if j == coordinate else x[j] for j in range(3))
        edge_set.add(tuple(sorted((i, vertex_index[y]))))
edges = sorted(edge_set)
edge_index = {e: i for i, e in enumerate(edges)}
assert len(edges) == 36
# Explicit labeled graph isomorphism to the generalized Petersen GP(12,5).
# Outer edges: i--(i+1) mod 12; spokes i--(12+i);
# inner edges: (12+i)--(12+(i+5) mod 12).
to_petersen = [0,1,14,2,19,12,22,15,4,3,5,17,
               8,20,18,13,6,7,9,10,23,11,16,21]
assert sorted(to_petersen) == list(range(24))
gp_edges = set()
for i in range(12):
    gp_edges.add(tuple(sorted((i,(i+1)%12))))
    gp_edges.add((i,12+i))
    gp_edges.add(tuple(sorted((12+i,12+(i+5)%12))))
assert len(gp_edges) == 36
assert {tuple(sorted((to_petersen[a],to_petersen[b])))
        for a,b in edges} == gp_edges
neighbours = [set() for _ in vertices]
for a, b in edges:
    neighbours[a].add(b)
    neighbours[b].add(a)
assert all(len(n) == 3 for n in neighbours)

# Check bipartiteness, needed for the vertex-cover argument.
colour = [-1] * 24
for root in range(24):
    if colour[root] != -1:
        continue
    colour[root] = 0
    queue = deque([root])
    while queue:
        a = queue.popleft()
        for b in neighbours[a]:
            if colour[b] == -1:
                colour[b] = 1 - colour[a]
                queue.append(b)
            else:
                assert colour[b] != colour[a]
assert Counter(colour) == {0: 12, 1: 12}

# First enumeration: each legal face has a vertex cover of at most two
# by the bipartite matching-cover theorem. Verify that model exactly.
incident = [0] * 24
for j, (a, b) in enumerate(edges):
    incident[a] |= 1 << j
    incident[b] |= 1 << j
faces = {0}
for a, b in combinations(range(24), 2):
    cover = incident[a] | incident[b]
    sub = cover
    while sub:
        faces.add(sub)
        sub = (sub - 1) & cover

# Second enumeration: independent direct recursive forbidden-triple test.
# Every possible extension is tried, so no legal face is omitted.
disjoint = [[not (set(edges[a]) & set(edges[b]))
             for b in range(36)] for a in range(36)]
by_matching = {0}

def search(face, chosen, start):
    for j in range(start, 36):
        if any(disjoint[j][a] and disjoint[j][b] and disjoint[a][b]
               for a, b in combinations(chosen, 2)):
            continue
        nxt = face | (1 << j)
        assert nxt not in by_matching
        by_matching.add(nxt)
        search(nxt, chosen + (j,), j + 1)
search(0, (), 0)
assert by_matching == faces
fvector = [sum(1 for f in faces if f.bit_count() == d) for d in range(7)]
assert fvector == [1, 36, 630, 2256, 2988, 1476, 240]
assert max(f.bit_count() for f in faces) == 6

# Sequential edge-toggling acyclic matching; the empty face participates.
unpaired = set(faces)
pairs = []
for j in range(36):
    bit = 1 << j
    for lower in tuple(unpaired):
        upper = lower | bit
        if not lower & bit and upper in unpaired:
            unpaired.remove(lower)
            unpaired.remove(upper)
            pairs.append((lower, upper))
crit = Counter(f.bit_count() - 1 for f in unpaired)
assert crit == {3: 91}
assert len(pairs) == 3768

# Direct global test of discrete-Morse acyclicity. Matched covers point
# upward; all other covers point downward in the augmented Hasse graph.
matched = set(pairs)
indegree = {f: 0 for f in faces}
successors = {f: [] for f in faces}
num_covers = 0
for upper in faces:
    for j in range(36):
        bit = 1 << j
        if upper & bit:
            lower = upper ^ bit
            assert lower in faces
            source, target = ((lower, upper) if (lower, upper) in matched
                              else (upper, lower))
            successors[source].append(target)
            indegree[target] += 1
            num_covers += 1
queue = deque(f for f, d in indegree.items() if d == 0)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for g in successors[f]:
        indegree[g] -= 1
        if indegree[g] == 0:
            queue.append(g)
assert visited == len(faces)
assert num_covers == 28836

# All natural 4-box, 3-token symmetries; signed simplicial Lefschetz
# formula determines the degree-three rational character.
by_size = {d: [f for f in faces if f.bit_count() == d]
           for d in range(1, 7)}
permutations4 = list(permutations(range(4)))
permutations3 = list(permutations(range(3)))

def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))

def homology_trace(edge_perm):
    lefschetz = 0
    for d, fs in by_size.items():
        tr = 0
        for face in fs:
            support = [j for j in range(36) if face & (1 << j)]
            images = [edge_perm[j] for j in support]
            if set(images) != set(support):
                continue
            inversions = sum(images[i] > images[j]
                             for i in range(len(images))
                             for j in range(i+1, len(images)))
            tr += -1 if inversions % 2 else 1
        lefschetz += (-1)**(d-1) * tr
    # Only ordinary H_0=Q and H_3=Q^91 are nonzero.
    return 1 - lefschetz

class_traces = defaultdict(list)
vertex_actions = set()
for a in permutations4:
    for b in permutations3:
        inverse_b = tuple(b.index(j) for j in range(3))
        action = tuple(vertex_index[tuple(a[v[inverse_b[j]]]
                                          for j in range(3))]
                       for v in vertices)
        assert action not in vertex_actions
        vertex_actions.add(action)
        edge_action = tuple(edge_index[tuple(sorted((action[x], action[y])))]
                            for x, y in edges)
        assert len(set(edge_action)) == 36
        cls = (cycle_type(a), cycle_type(b))
        class_traces[cls].append(homology_trace(edge_action))
assert len(vertex_actions) == 144

# Independent graph-automorphism completeness check: a graph automorphism
# sends vertex 0 to one of 24 vertices and its ordered three neighbours
# to one of 6 permutations of the image neighbourhood. Exhaustively
# backtrack every adjacency-preserving extension of these seeds.
full_automorphism_count = 0

def extend(mapping, used):
    global full_automorphism_count
    if len(mapping) == 24:
        full_automorphism_count += 1
        return
    source = max((u for u in range(24) if u not in mapping),
                 key=lambda u: (len(neighbours[u] & mapping.keys()), -u))
    for target in range(24):
        if target in used:
            continue
        if all(((u in neighbours[source]) ==
                (mapping[u] in neighbours[target])) for u in mapping):
            mapping[source] = target
            used.add(target)
            extend(mapping, used)
            used.remove(target)
            del mapping[source]

for image0 in range(24):
    source_neighbours = sorted(neighbours[0])
    for images in permutations(sorted(neighbours[image0])):
        seed = {0:image0, **dict(zip(source_neighbours, images))}
        extend(seed, set(seed.values()))
assert full_automorphism_count == 144
assert len(class_traces) == 15
assert all(len(set(v)) == 1 for v in class_traces.values())
C4 = [(1,1,1,1), (2,1,1), (2,2), (3,1), (4,)]
C3 = [(1,1,1), (2,1), (3,)]
values = [[class_traces[(a,b)][0] for b in C3] for a in C4]
assert values == [[91,7,1], [19,7,1], [7,11,1], [1,1,1], [1,1,1]]
sizes = [[len(class_traces[(a,b)]) for b in C3] for a in C4]
assert sizes == [[1,3,2], [6,18,12], [3,9,6], [8,24,16], [6,18,12]]
assert sum(sizes[i][j] * values[i][j]
           for i in range(5) for j in range(3)) == 144 * 4

char4 = {'4':(1,1,1,1,1), '31':(3,1,-1,0,-1),
         '22':(2,0,2,-1,0), '211':(3,-1,-1,0,1),
         '1111':(1,-1,1,1,-1)}
char3 = {'3':(1,1,1), '21':(2,0,-1), '111':(1,-1,1)}
multiplicities = {}
for a, va in char4.items():
    for b, vb in char3.items():
        scalar = sum(sizes[i][j] * values[i][j] * va[i] * vb[j]
                     for i in range(5) for j in range(3))
        assert scalar % 144 == 0
        m = scalar // 144
        assert m >= 0
        if m:
            multiplicities[a+'x'+b] = m
assert multiplicities == {
  '4x3':4, '4x21':3, '31x3':3, '31x21':5,
  '31x111':2, '22x3':3, '22x21':3,
  '211x21':2, '211x111':2}
assert sum(multiplicities[a+'x'+b]*char4[a][0]*char3[b][0]
           for a,b in ((k.split('x',1)) for k in multiplicities)) == 91

print(json.dumps({
    'graph_vertices':24, 'graph_edges':36, 'bipartition':[12,12],
    'enumeration_methods':['König vertex-cover','direct forbidden-triplet recursion'],
    'augmented_faces':len(faces),
    'f_vector_including_empty':fvector,
    'morse_pairs':len(pairs), 'critical_cells':dict(crit),
    'hasse_covers':num_covers, 'acyclic':True,
    'group_order':len(vertex_actions), 'full_graph_automorphisms':full_automorphism_count,
    'character_S4_classes_rows_S3_columns':values,
    'class_sizes':sizes,'trivial_representation_multiplicity':4,
    'irreducible_multiplicities':multiplicities},
    sort_keys=True, indent=2))

"""Exact finite certificate for the Kreweras orbit space of NC(D4).

Python 3.10+; standard library only. The presentation simplification uses
free reductions and single-occurrence generator/2-cell cancellations.
"""
from collections import Counter, defaultdict, deque

N = 4
IDENTITY = tuple(range(1, N + 1))


def act(p, x):
    return p[abs(x) - 1] * (1 if x > 0 else -1)


def multiply(p, q):
    return tuple(act(p, x) for x in q)


def inverse(p):
    out = [0] * N
    for i, x in enumerate(p):
        out[abs(x) - 1] = (i + 1) * (1 if x > 0 else -1)
    return tuple(out)


def swap(i):
    result = list(IDENTITY)
    result[i], result[i + 1] = result[i + 1], result[i]
    return tuple(result)


simples = [(-2, -1, 3, 4), swap(0), swap(1), swap(2)]
coxeter = IDENTITY
for simple in simples:
    coxeter = multiply(coxeter, simple)
assert coxeter == (-1, 3, 4, -2)
reflections = set()
for i in range(N):
    for j in range(i + 1, N):
        pos = list(IDENTITY)
        pos[i], pos[j] = pos[j], pos[i]
        reflections.add(tuple(pos))
        neg = list(IDENTITY)
        neg[i], neg[j] = -(j + 1), -(i + 1)
        reflections.add(tuple(neg))
assert len(reflections) == 12

# Exact word length in all reflections, by exhaustive breadth-first search.
length = {IDENTITY: 0}
queue = deque([IDENTITY])
while queue:
    w = queue.popleft()
    for t in reflections:
        new = multiply(w, t)
        if new not in length:
            length[new] = length[w] + 1
            queue.append(new)
assert len(length) == 192
assert length[coxeter] == 4

nc = {w for w in length
      if length[w] + length[multiply(inverse(w), coxeter)] == 4}
assert len(nc) == 50
assert Counter(length[w] for w in nc) == {0: 1, 1: 12, 2: 24, 3: 12, 4: 1}
proper = sorted(nc - {IDENTITY, coxeter})


def smaller(a, b):
    return length[a] + length[multiply(inverse(a), b)] == length[b]


def complement(w):
    return multiply(inverse(w), coxeter)

assert all(complement(w) in nc for w in nc)
assert all(smaller(a, b) == smaller(complement(b), complement(a))
           for a in nc for b in nc)
periods = Counter()
for w in proper:
    y, k = complement(w), 1
    while y != w:
        y, k = complement(y), k + 1
    periods[k] += 1
assert periods == {6: 42, 3: 6}

# The unreduced rank-chain complex: faces are strict chains of ranks 1,2,3.
faces = [[(w,) for w in proper]]
faces.append([(a, b) for a in proper for b in proper
              if length[a] < length[b] and smaller(a, b)])
faces.append([(a, b, d) for a in proper for b in proper for d in proper
              if length[a] < length[b] < length[d]
              and smaller(a, b) and smaller(b, d)])
assert tuple(map(len, faces)) == (48, 189, 162)
all_faces = sum(faces, [])


def face_complement(face):
    return tuple(sorted((complement(w) for w in face), key=lambda w: length[w]))

for family in faces:
    valid = set(family)
    assert all(face_complement(face) in valid for face in family)

# Barycentric subdivision makes the action without inversions. A quotient
# k-cell is an orbit of a strictly nested (k+1)-tuple of nonempty faces.
contained = defaultdict(list)
for large in all_faces:
    for small in all_faces:
        if len(small) < len(large) and set(small) < set(large):
            contained[large].append(small)
complex_cells = [[(face,) for face in all_faces]]
complex_cells.append([(small, large) for large in all_faces
                      for small in contained[large]])
complex_cells.append([(small, middle, top) for top in faces[2]
                      for middle in contained[top] if len(middle) == 2
                      for small in contained[middle] if len(small) == 1])
assert tuple(map(len, complex_cells)) == (399, 1350, 972)


def chain_complement(chain):
    return tuple(face_complement(face) for face in chain)

representatives, orbit_index = [[], [], []], {}
for dimension, cells in enumerate(complex_cells):
    for cell in cells:
        if cell in orbit_index:
            continue
        orbit = []
        current = cell
        while current not in orbit:
            orbit.append(current)
            current = chain_complement(current)
        index = len(representatives[dimension])
        representatives[dimension].append(cell)
        for member in orbit:
            assert member not in orbit_index
            orbit_index[member] = index
assert tuple(map(len, representatives)) == (72, 231, 162)
assert 72 - 231 + 162 == 3

# Signed cellular boundaries; all action maps preserve inclusion-order
# orientation of barycentric flags, so orbit representatives suffice.
boundary = [[], [], []]
for dimension in (1, 2):
    for cell in representatives[dimension]:
        terms = Counter()
        for i in range(dimension + 1):
            sub = cell[:i] + cell[i + 1:]
            terms[orbit_index[sub]] += (-1) ** i
        boundary[dimension].append({j: coefficient
                                    for j, coefficient in terms.items() if coefficient})
for column in boundary[2]:
    assert not any(sum(coefficient * boundary[1][edge].get(vertex, 0)
                       for edge, coefficient in column.items())
                   for vertex in range(72))

# Choose a spanning tree and collapse it, leaving 160 loops and 162 2-cells.
parent = list(range(72))


def root(i):
    while parent[i] != i:
        i = parent[i]
    return i


def merge(i, j):
    i, j = root(i), root(j)
    if i == j:
        return False
    parent[j] = i
    return True

tree = set()
for edge, endpoints in enumerate(boundary[1]):
    if len(endpoints) == 2:
        u, v = endpoints
        if merge(u, v):
            tree.add(edge)
assert len(tree) == 71 and len({root(i) for i in range(72)}) == 1
remaining = [edge for edge in range(231) if edge not in tree]
assert len(remaining) == 160
edge_label = {edge: index + 1 for index, edge in enumerate(remaining)}


def edge_word(a, b):
    idx = orbit_index[(a, b)]
    return [edge_label[idx]] if idx in edge_label else []


def freely_reduce(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return stack


def cyclically_reduce(word):
    word = freely_reduce(word)
    while len(word) > 1 and word[0] == -word[-1]:
        word = word[1:-1]
    return word


def reversed_inverse(word):
    return [-letter for letter in reversed(word)]

relations = []
for a, b, c in representatives[2]:
    # The oriented triangle path is a->b->c->a.
    edge_ac = edge_word(a, c)
    relations.append(cyclically_reduce(
        edge_word(a, b) + edge_word(b, c) + reversed_inverse(edge_ac)))
assert Counter(map(len, relations)) == {1: 56, 2: 53, 3: 53}

# Each elimination removes one 1-cell and one 2-cell in a presentation
# complex using a relator containing that 1-cell exactly once.
active_generators = set(range(1, 161))
cancelled_lengths = Counter()
cancel_count = 0
while True:
    relations = [cyclically_reduce(rel) for rel in relations if rel]
    best = None
    for rel_index, rel in enumerate(relations):
        frequency = Counter(abs(x) for x in rel)
        for position, letter in enumerate(rel):
            if frequency[abs(letter)] != 1:
                continue
            option = (len(rel), rel_index, position, letter)
            if best is None or option < best:
                best = option
    if best is None:
        break
    rel_length, rel_index, position, letter = best
    rel = relations.pop(rel_index)
    rest = rel[position + 1:] + rel[:position]
    replacement = reversed_inverse(rest) if letter > 0 else rest
    generator = abs(letter)
    updated_relations = []
    for relation in relations:
        substituted = []
        for x in relation:
            if x == generator:
                substituted.extend(replacement)
            elif x == -generator:
                substituted.extend(reversed_inverse(replacement))
            else:
                substituted.append(x)
        updated_relations.append(cyclically_reduce(substituted))
    relations = updated_relations
    active_generators.remove(generator)
    cancelled_lengths[rel_length] += 1
    cancel_count += 1
assert cancel_count == 159
assert cancelled_lengths == {1: 112, 2: 47}
assert len(active_generators) == 1
g = next(iter(active_generators))
assert len(relations) == 2
assert relations == [[-g, -g, -g], [g, g, g]]
# There are three surviving 2-cells: the two displayed attaching words
# and one with trivial attaching word (removed empty relator).
assert len(representatives[2]) - cancel_count == 3
# One cellular 2-cell slide turns the inverse pair into a null attaching
# word, yielding the degree-three Moore complex wedged with two 2-spheres.
print('D4_KREWERAS_MOORE3_TWO_SPHERES_OK')
print('W=192 NC=50 K_orbits=9+33+30 barycentric_quotient=(72,231,162)')
print('CW_after_159_cancellations: 1_vertex 1_edge 3_two_cells')
print('attaching_words: (-x)^3, x^3, trivial')
print('homotopy: M(Z/3,1) wedge S^2 wedge S^2')

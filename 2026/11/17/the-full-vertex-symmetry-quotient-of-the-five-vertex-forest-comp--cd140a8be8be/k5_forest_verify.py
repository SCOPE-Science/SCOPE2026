"""Exact verification of the five-label forest-complex symmetry quotient.

Requires Python 3.10+ and SymPy. This enumerates every forest, every strict
nonempty forest flag, and all 120 label permutations. Its quotient chain
complex is the flag-orbit CW structure on the ordinary geometric quotient.
"""
from collections import Counter
from itertools import combinations, permutations
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

N = 5
E = list(combinations(range(N), 2))
edge_id = {e: i for i, e in enumerate(E)}
perms = list(permutations(range(N)))
actions = [tuple(edge_id[tuple(sorted((p[u], p[v])))] for u, v in E)
           for p in perms]


def is_forest(mask):
    parent = list(range(N))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for j, (u, v) in enumerate(E):
        if mask & (1 << j):
            x, y = root(u), root(v)
            if x == y:
                return False
            parent[x] = y
    return True


forests = [m for m in range(1, 1 << len(E)) if is_forest(m)]
assert Counter(m.bit_count() for m in forests) == {1: 10, 2: 45, 3: 110, 4: 125}


def transform(mask, p_action):
    value = 0
    for i, j in enumerate(p_action):
        if mask & (1 << i):
            value |= 1 << j
    return value


transforms = {m: tuple(transform(m, p_action) for p_action in actions)
              for m in forests}


def canonical(flag):
    return min(tuple(transforms[m][i] for m in flag)
               for i in range(len(perms)))


# Every nonempty face of the barycentric subdivision is a strict forest flag.
flags_by_dim = [[] for _ in range(4)]
for maximal in forests:
    flags_by_dim[0].append((maximal,))
    for a in forests:
        if a != maximal and a & maximal == a:
            flags_by_dim[1].append((a, maximal))
            for b in forests:
                if b != a and b & a == b:
                    flags_by_dim[2].append((b, a, maximal))
                    for c in forests:
                        if c != b and c & b == c:
                            flags_by_dim[3].append((c, b, a, maximal))

orbits = []
for flags in flags_by_dim:
    canonical_flags = sorted({canonical(f) for f in flags})
    orbits.append({f: k for k, f in enumerate(canonical_flags)})
assert [len(o) for o in orbits] == [9, 33, 49, 25]
print('Forest counts by edge number:', [10, 45, 110, 125])
print('Barycentric quotient cell counts:', [len(o) for o in orbits])

D = []
for degree in range(1, 4):
    boundary = zeros(len(orbits[degree - 1]), len(orbits[degree]))
    for flag, col in orbits[degree].items():
        for deletion in range(degree + 1):
            face = flag[:deletion] + flag[deletion + 1:]
            row = orbits[degree - 1][canonical(face)]
            boundary[row, col] += (-1) ** deletion
    D.append(boundary)
for degree in (0, 1):
    assert D[degree] * D[degree + 1] == zeros(
        D[degree].rows, D[degree + 1].cols)

ranks = []
for degree, M in enumerate(D, start=1):
    diag = smith_normal_form(M, domain=ZZ)
    nonzero = [abs(diag[i, i]) for i in range(min(diag.shape))
               if diag[i, i] != 0]
    assert set(nonzero) == {1}
    ranks.append(len(nonzero))
    print('Boundary degree', degree, 'rank', len(nonzero),
          'nonzero Smith factors', dict(Counter(nonzero)))
assert ranks == [8, 25, 24]
assert [len(orbits[i]) - (ranks[i - 1] if i else 0)
        - (ranks[i] if i < 3 else 0) for i in range(4)] == [1, 0, 0, 1]
print('Integral homology: H0 = Z, H1 = 0, H2 = 0, H3 = Z')

# Fundamental-group presentation: quotient edges modulo a spanning tree,
# and one oriented boundary relator per quotient triangle.
vertices = orbits[0]
edges = list(orbits[1])
triangles = list(orbits[2])
endpoints = [tuple(vertices[canonical((f,))] for f in edge) for edge in edges]
parent = list(range(len(vertices)))

def root(v):
    while parent[v] != v:
        v = parent[v]
    return v


tree_edges = set()
for index, (u, v) in enumerate(endpoints):
    a, b = root(u), root(v)
    if a != b:
        tree_edges.add(index)
        parent[a] = b
assert len(tree_edges) == 8
free_generators = {i: k + 1 for k, i in
                   enumerate(i for i in range(len(edges)) if i not in tree_edges)}
assert len(free_generators) == 25


def freely_reduce(word):
    result = []
    for letter in word:
        if result and result[-1] == -letter:
            result.pop()
        else:
            result.append(letter)
    return result


def inverse(word):
    return [-x for x in reversed(word)]


relators = []
for a, b, c in triangles:
    eab = orbits[1][canonical((a, b))]
    ebc = orbits[1][canonical((b, c))]
    eac = orbits[1][canonical((a, c))]
    boundary_word = [free_generators.get(eab, 0),
                     free_generators.get(ebc, 0),
                     -free_generators.get(eac, 0)]
    relators.append(freely_reduce([x for x in boundary_word if x]))
assert len(relators) == 49

remaining_generators = set(free_generators.values())
eliminations = 0
while True:
    relators = [freely_reduce(r) for r in relators]
    found = None
    for i, r in enumerate(relators):
        for pos, symbol in enumerate(r):
            if sum(abs(t) == abs(symbol) for t in r) == 1:
                rest = r[pos + 1:] + r[:pos]
                replacement = inverse(rest) if symbol > 0 else rest
                found = (i, abs(symbol), replacement)
                break
        if found is not None:
            break
    if found is None:
        break
    relation_index, generator, replacement = found
    updated = []
    for i, r in enumerate(relators):
        if i == relation_index:
            continue
        substituted = []
        for letter in r:
            if letter == generator:
                substituted.extend(replacement)
            elif letter == -generator:
                substituted.extend(inverse(replacement))
            else:
                substituted.append(letter)
        updated.append(freely_reduce(substituted))
    relators = updated
    remaining_generators.remove(generator)
    eliminations += 1
assert eliminations == 25
assert len(remaining_generators) == 0
assert len(relators) == 24 and all(not r for r in relators)
print('Tietze eliminations:', eliminations)
print('Remaining generators: 0; remaining relators: 24 trivial words')
print('Fundamental group: trivial')
print('Conclusion: the quotient is homotopy equivalent to S^3.')

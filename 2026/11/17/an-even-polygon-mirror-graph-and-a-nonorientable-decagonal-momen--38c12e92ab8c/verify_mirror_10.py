"""Exact finite verification of the decagonal real moment-angle dihedral quotient.

Standard library only. Binary words use bit i for the sign at coordinate i;
0 means -1, 1 means +1. Coordinates of cubical faces use 0 for free.
"""
from collections import Counter, defaultdict, deque
from itertools import product
from math import prod

N = 10
PERMS = [tuple((i+k) % N for i in range(N)) for k in range(N)] + [tuple((k-i) % N for i in range(N)) for k in range(N)]
REFLECTIONS = PERMS[N:]


def permute_mask(mask, p):
    return sum(1 << p[i] for i in range(N) if mask & (1 << i))


def mirror_graph():
    parent = {}
    def root(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = root(parent[x])
        return parent[x]
    def join(a, b):
        a, b = root(a), root(b)
        if a != b:
            parent[b] = a

    # Every mirror is a union of four-edge circuits whose two varying
    # coordinates are the reflection's two distinguished index orbits.
    for p in REFLECTIONS:
        remain = set(range(N))
        orbits = []
        while remain:
            i = min(remain)
            j = p[i]
            remain.discard(i)
            remain.discard(j)
            orbits.append((i,) if i == j else (i, j))
        exceptional = [o for o in orbits if len(o) == 1 or ((o[0]-o[1]) % N in (1, N-1))]
        assert len(exceptional) == 2
        ordinary = [o for o in orbits if o not in exceptional]
        ex = [sum(1 << i for i in o) for o in exceptional]
        for z in range(1 << len(ordinary)):
            base = sum(sum(1 << i for i in o) for k, o in enumerate(ordinary) if z & (1 << k))
            corners = [base ^ (ex[0] if q & 1 else 0) ^ (ex[1] if q & 2 else 0) for q in range(4)]
            for c in corners[1:]:
                join(corners[0], c)
    # Passing from the union of all mirrors to its ordinary D_10 quotient.
    for mask in list(parent):
        for p in PERMS:
            join(mask, permute_mask(mask, p))
    components = defaultdict(list)
    for mask in parent:
        components[root(mask)].append(mask)
    signature = sorted((min(v), len(v)) for v in components.values())
    assert len(parent) == 424
    assert signature == [(0, 56), (5, 40), (9, 40), (17, 40), (27, 40),
                         (51, 40), (85, 32), (119, 40), (165, 56), (347, 40)]
    return signature


def permute_face(face, p):
    out = [0] * N
    for i, j in enumerate(p):
        out[j] = face[i]
    return tuple(out)


def quotient_triangles():
    # Face-poset barycentric subdivision. Every 2-simplex has a 0<1<2 flag.
    faces = [[], [], []]
    candidates = [()] + [(i,) for i in range(N)] + [(i, (i+1)%N) for i in range(N)]
    for active in candidates:
        active = set(active)
        for sign in product((-1, 1), repeat=N-len(active)):
            it = iter(sign)
            faces[len(active)].append(tuple(0 if i in active else next(it) for i in range(N)))
    allfaces = [x for ff in faces for x in ff]
    can = {face: min(permute_face(face, p) for p in PERMS) for face in allfaces}
    orbitcells = [sorted({can[x] for x in ff}) for ff in faces]
    label = {f: (d, j) for d, ff in enumerate(orbitcells) for j, f in enumerate(ff)}
    qlabel = {f: label[can[f]] for f in can}
    triangles = set()
    original_flags = 0
    for square in faces[2]:
        a, b = [i for i, x in enumerate(square) if x == 0]
        for fixed, other in ((a, b), (b, a)):
            for u in (-1, 1):
                edge = list(square)
                edge[fixed] = u
                edge = tuple(edge)
                for v in (-1, 1):
                    vertex = list(edge)
                    vertex[other] = v
                    vertex = tuple(vertex)
                    triangles.add((qlabel[vertex], qlabel[edge], qlabel[square]))
                    original_flags += 1
    assert original_flags == 20480
    assert len(triangles) == original_flags // (2*N) == 1024
    return triangles, [len(x) for x in orbitcells]


def quotient_surface():
    tris, cubical_orbits = quotient_triangles()
    triangles = sorted(tris)
    edge_to_triangle = defaultdict(list)
    for idx, (a, b, c) in enumerate(triangles):
        for edge, induced_sign in [((a, b), 1), ((b, c), 1), ((a, c), -1)]:
            edge_to_triangle[edge].append((idx, induced_sign))
    assert set(map(len, edge_to_triangle.values())) <= {1, 2}
    boundary = [edge for edge, incidences in edge_to_triangle.items() if len(incidences) == 1]
    vertices = {v for t in triangles for v in t}
    V, E, F = len(vertices), len(edge_to_triangle), len(triangles)
    assert cubical_orbits == [78, 272, 136]
    assert (V, E, F) == (486, 1584, 1024)
    assert Counter(map(len, edge_to_triangle.values())) == {2: 1488, 1: 96}
    assert V-E+F == -74
    # Boundary is a disjoint union of circles in a surface: its graph has degree 2.
    bg = defaultdict(set)
    for a, b in boundary:
        bg[a].add(b)
        bg[b].add(a)
    assert set(map(len, bg.values())) == {2}
    seen = set()
    lengths = []
    for v in bg:
        if v in seen:
            continue
        q = [v]
        seen.add(v)
        k = 0
        while q:
            k += 1
            for w in bg[q.pop()]:
                if w not in seen:
                    seen.add(w)
                    q.append(w)
        lengths.append(k)
    assert len(lengths) == 10 and sum(lengths) == 96

    # A local orientation changes by -sign(T,e)*sign(U,e) across edge e.
    adjacency = defaultdict(list)
    for edge, incidences in edge_to_triangle.items():
        if len(incidences) == 2:
            (a, sa), (b, sb) = incidences
            trans = -sa*sb
            adjacency[a].append((b, trans))
            adjacency[b].append((a, trans))
    orientation, par = {}, {}
    conflict = None
    for start in range(F):
        if start in orientation:
            continue
        orientation[start] = 1
        par[start] = None
        queue = deque([start])
        while queue and conflict is None:
            a = queue.popleft()
            for b, trans in adjacency[a]:
                if b not in orientation:
                    orientation[b] = orientation[a]*trans
                    par[b] = a
                    queue.append(b)
                elif orientation[b] != orientation[a]*trans:
                    conflict = (a, b)
                    break
        if conflict is not None:
            break
    assert conflict is not None
    a, b = conflict
    ancestors_a, ancestors_b = [], []
    x = a
    while x is not None:
        ancestors_a.append(x)
        x = par[x]
    x = b
    while x is not None:
        ancestors_b.append(x)
        x = par[x]
    common = next(x for x in ancestors_a if x in set(ancestors_b))
    cycle = ancestors_a[:ancestors_a.index(common)+1] + list(reversed(ancestors_b[:ancestors_b.index(common)]))
    assert cycle == [58,57,51,15,14,13,12,3,4,5,22,24,53,55,56]
    factors = []
    for a, b in zip(cycle, cycle[1:]+cycle[:1]):
        factors.extend([t for v, t in adjacency[a] if v == b][:1])
    assert len(factors) == 15 and prod(factors) == -1
    assert len(boundary) == 96
    return (V,E,F),sorted(lengths),cycle


def main():
    components = mirror_graph()
    cells, boundary_lengths, cycle = quotient_surface()
    print('mirror graph: 424 binary sign vertices, 10 components')
    print('component (least bitmask, number of sign vertices):', components)
    print('quotient triangles (vertices,edges,faces):',cells,'Euler characteristic = -74')
    print('boundary cycle lengths (barycentric edges):', boundary_lengths)
    print('orientation-obstruction triangle cycle:',cycle)
    print('nonorientable genus = 2 - 10 - (-74) = 66')
    print('EXACT_DECAGONAL_MIRROR_AND_SURFACE_CHECK_PASS')

if __name__ == '__main__':
    main()

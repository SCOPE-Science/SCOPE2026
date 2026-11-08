#!/usr/bin/env python3
"""Exact standalone finite certificate for the rhombic-dodecahedral graph Čech nerve.

Usage: python3 verify_rhombic_cech.py collapse_pairs.tsv
Only the Python standard library is required.
"""
from __future__ import annotations
import itertools
import pathlib
import sys
from collections import Counter, deque

N = 14
VERTICES = tuple(range(N))
CORNERS = tuple(range(8))
CENTERS = tuple(range(8, 14))


def graph():
    # Corner i has coordinate bit b_j=(i>>j)&1, and is incident to face (j,b_j).
    edges = set()
    for i in CORNERS:
        for j in range(3):
            edges.add(tuple(sorted((i, 8 + 2*j + ((i >> j) & 1)))))
    assert len(edges) == 24
    return tuple(sorted(edges))


def bfs_distances(edges):
    adj = [set() for _ in VERTICES]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    ans = []
    for source in VERTICES:
        d = [-1]*N; d[source] = 0
        q = deque([source])
        while q:
            v = q.popleft()
            for u in adj[v]:
                if d[u] < 0:
                    d[u] = d[v] + 1
                    q.append(u)
        assert all(t >= 0 for t in d)
        ans.append(d)
    assert max(map(max,ans)) == 4
    return adj, ans


def generating_masks(edges, distances, scale):
    candidates = []
    # Witnesses at vertices or midpoints. At integer scale only the
    # parity-relevant witnesses can be maximal.
    if scale % 2 == 0:
        radius = scale//2
        for a in VERTICES:
            candidates.append(sum(1 << v for v in VERTICES
                                  if distances[a][v] <= radius))
    else:
        radius = (scale-1)//2
        for a,b in edges:
            candidates.append(sum(1 << v for v in VERTICES
                                  if min(distances[a][v],distances[b][v]) <= radius))
    return tuple(sorted(set(candidates)))


def expand(generators):
    f = {0}
    for facet in generators:
        sub = facet
        while sub:
            f.add(sub)
            sub = (sub-1)&facet
    return f


def octahedron():
    # Each facet has one of the two centers for every coordinate.
    generators = []
    for bits in itertools.product((0,1), repeat=3):
        generators.append(sum(1 << (8 + 2*j + bits[j]) for j in range(3)))
    return expand(generators)


def check_collapse_certificate(faces, target, path):
    sequence = []
    for line in pathlib.Path(path).read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#'):
            continue
        fields = line.split('\t')
        assert len(fields) == 2, fields
        sequence.append(tuple(map(int, fields)))
    remain = set(faces)
    for k, (lower, upper) in enumerate(sequence,1):
        assert lower and lower not in target and upper not in target
        assert lower in remain and upper in remain
        assert (lower & upper) == lower and (upper ^ lower).bit_count() == 1
        all_immediate = [lower | (1 << v) for v in VERTICES
                         if not (lower >> v)&1 and (lower | (1<<v)) in remain]
        assert all_immediate == [upper], (k, lower, upper, all_immediate)
        # A unique codimension-one coface implies a unique maximal coface.
        remain.remove(lower); remain.remove(upper)
    assert remain == target
    assert len(sequence) == 626
    return len(sequence)


def morse_vertex_sweep(faces, order):
    remain = set(faces) - {0}
    matches = set()
    for v in order:
        bit = 1 << v
        for low in sorted(remain):
            high = low | bit
            if not low & bit and high in remain:
                remain.remove(low); remain.remove(high)
                matches.add((low,high))
    return matches, remain


def assert_acyclic(faces,matches):
    nonempty = set(faces)-{0}
    outgoing = {f:[] for f in nonempty}
    indeg = {f:0 for f in nonempty}
    incidences = 0
    for upper in nonempty:
        for v in VERTICES:
            if (upper>>v)&1:
                lower = upper & ~(1<<v)
                if lower:
                    assert lower in nonempty
                    if (lower,upper) in matches:
                        start,end = lower,upper
                    else:
                        start,end = upper,lower
                    outgoing[start].append(end)
                    indeg[end] += 1
                    incidences += 1
    queue = deque(f for f,d in indeg.items() if d == 0)
    removed = 0
    while queue:
        f = queue.popleft(); removed += 1
        for v in outgoing[f]:
            indeg[v] -= 1
            if indeg[v] == 0: queue.append(v)
    assert removed == len(nonempty), (removed,len(nonempty))
    return incidences


def rank_mod2(columns):
    pivots = {}
    for c in columns:
        while c:
            high = c.bit_length()-1
            if high in pivots: c ^= pivots[high]
            else:
                pivots[high] = c
                break
    return len(pivots)


def boundary_ranks(faces):
    cells = {k:sorted(f for f in faces if f.bit_count() == k+1)
             for k in range(5)}
    ranks = []
    for dim in range(1,5):
        previous = {face:i for i,face in enumerate(cells[dim-1])}
        columns=[]
        for f in cells[dim]:
            column=0
            for j in VERTICES:
                if (f>>j)&1:
                    column ^= 1 << previous[f ^ (1<<j)]
            columns.append(column)
        ranks.append(rank_mod2(columns))
    return ranks


def sign_perm(sequence):
    parity = 1
    for i in range(len(sequence)):
        for j in range(i+1,len(sequence)):
            if sequence[i] > sequence[j]:parity = -parity
    return parity


def symmetry_action(edges, o_faces):
    edge_set = set(edges)
    octa_triangles = [f for f in o_faces if f.bit_count()==3]
    assert len(octa_triangles)==8
    fundamental={}
    for bits in itertools.product((0,1), repeat=3):
        f=sum(1 << (8+2*j+bits[j]) for j in range(3))
        fundamental[f]=(-1)**sum(bits)
    assert set(fundamental)==set(octa_triangles)
    count=0;negative=0;positive=0
    for perm in itertools.permutations(range(3)):
        for bits in itertools.product((0,1),repeat=3):
            mapping = {}
            for v in CORNERS:
                new = 0
                for j in range(3):
                    new |= (((v>>j)&1) ^ bits[perm[j]]) << perm[j]
                mapping[v]=new
            for j in range(3):
                for s in (0,1):mapping[8+2*j+s]=8+2*perm[j]+(s^bits[perm[j]])
            assert len(set(mapping.values()))==N
            assert {tuple(sorted((mapping[u],mapping[v]))) for u,v in edges}==edge_set
            predicted=sign_perm(perm)*(-1)**sum(bits)
            mapped={}
            for f,c in fundamental.items():
                original=[v for v in VERTICES if (f>>v)&1]
                permuted=[mapping[v] for v in original]
                mapped_face=sum(1<<v for v in permuted)
                coeff=c*sign_perm(permuted)
                mapped[mapped_face]=mapped.get(mapped_face,0)+coeff
            assert mapped=={f:predicted*c for f,c in fundamental.items()}
            if predicted==1:positive+=1
            else:negative+=1
            count+=1
    # Any automorphism permutes the six degree-four centers and preserves
    # the three pairs of centers with no common cube corner. The action
    # on the six centers determines the action on all eight corners,
    # hence |Aut(R)| <= 2^3*3! = 48.
    assert count==48 and positive==negative==24
    return count, positive, negative


def run(certificate):
    edges=graph();adj,D=bfs_distances(edges)
    assert [len(adj[i]) for i in CORNERS] == [3]*8
    assert [len(adj[i]) for i in CENTERS] == [4]*6
    facets2=generating_masks(edges,D,2)
    facets3=generating_masks(edges,D,3)
    assert len(facets2)==14 and len(facets3)==24
    f2=expand(facets2);f3=expand(facets3)
    o=octahedron()
    assert len(o)==27 and o <= f2 and f2 <= f3
    hist2=[sum(f.bit_count()==d+1 for f in f2) for d in range(5)]
    hist3=[sum(f.bit_count()==d+1 for f in f3) for d in range(7)]
    assert hist2==[14,60,92,38,6],hist2
    assert hist3==[14,84,260,410,342,144,24],hist3
    assert len(f2)==211 and len(f3)==1279
    collapsed=check_collapse_certificate(f3,o,certificate)
    incidences=[]
    for order in (list(VERTICES),list(reversed(VERTICES))):
        pairs,critical=morse_vertex_sweep(f2,order)
        assert len(pairs)==98
        assert Counter(f.bit_count()-1 for f in critical)=={0:1,2:13}
        incidences.append(assert_acyclic(f2,pairs))
    assert incidences==[sum(1 for f in f2-{0} for v in VERTICES
                            if f>>v&1 and f^(1<<v) in f2-{0})]*2
    ranks=boundary_ranks(f2)
    assert ranks==[13,47,32,6],ranks  # independently checked binary boundaries
    # Betti 2 = 92-rank(boundary_2)-rank(boundary_3) = 13.
    assert 92-ranks[1]-ranks[2]==13
    a,p,n=symmetry_action(edges,o)
    print('RHOMBIC_CECH_CERTIFIED')
    print('graph_vertices=14 graph_edges=24 graph_diameter=4 automorphisms=%d'%a)
    print('scale2_facets=14 scale2_faces_including_empty=%d scale2_fvector=%s'%(len(f2),hist2))
    print('scale2_discrete_morse_pairs=98 critical_cells={0:1,2:13} hasse_incidences=%d'%incidences[0])
    print('scale2_mod2_boundary_ranks=%s'%ranks)
    print('scale3_facets=24 scale3_faces_including_empty=%d scale3_fvector=%s'%(len(f3),hist3))
    print('scale3_collapse_pairs=%d preserved_octahedral_faces=%d'%(collapsed,len(o)))
    print('octahedral_sphere_facets=8 symmetry_orientation_positive=%d negative=%d'%(p,n))
    print('integral_homotopy=scale2_wedge_13_S2;scale3_collapse_to_octahedron_S2')
    print('inclusion_H2_Z13_to_Z_is_split_surjective_kernel_Z12')
    print('VERIFICATION_OK')

if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python3 verify_rhombic_cech.py collapse_pairs.tsv')
    run(sys.argv[1])

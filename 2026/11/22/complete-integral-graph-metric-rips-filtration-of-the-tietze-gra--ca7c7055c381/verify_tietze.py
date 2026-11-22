"""Self-contained check of a finite CW-collapse certificate for the Tietze graph.

Usage: python3 verify_tietze.py collapse_certificate.json
No external packages or data are needed.
"""
import collections
import itertools
import json
import sys

N = 12

def bits(mask):
    return [i for i in range(N) if mask >> i & 1]

def read_graph(edge_list):
    assert len(edge_list) == 18
    assert len({tuple(sorted(e)) for e in edge_list}) == 18
    adj = {i: set() for i in range(N)}
    for a, b in edge_list:
        assert 0 <= a < b < N
        adj[a].add(b)
        adj[b].add(a)
    assert all(len(neighbors) == 3 for neighbors in adj.values())
    assert sum(1 for a,b,c in itertools.combinations(range(N), 3)
               if b in adj[a] and c in adj[a] and c in adj[b]) == 1
    return adj

def distances(adj):
    D = {}
    for v in range(N):
        distances = {v: 0}
        queue = [v]
        for x in queue:
            for y in sorted(adj[x]):
                if y not in distances:
                    distances[y] = distances[x] + 1
                    queue.append(y)
        assert len(distances) == N
        D[v] = distances
    assert max(max(d.values()) for d in D.values()) == 3
    return D

def rips_faces(D, radius):
    return {m for m in range(1, 1 << N)
            if all(D[i][j] <= radius for i,j in itertools.combinations(bits(m),2))}

def dimensions(faces):
    counts = collections.Counter(mask.bit_count() - 1 for mask in faces)
    return [counts[k] for k in range(max(counts)+1)]

def boundary_ranks_mod2(faces):
    bydim = collections.defaultdict(list)
    for mask in sorted(faces):
        bydim[mask.bit_count()-1].append(mask)
    ranks = {}
    for k in range(1, max(bydim)+1):
        index = {mask:i for i,mask in enumerate(bydim[k-1])}
        pivots = {}
        for mask in bydim[k]:
            column = 0
            for j in bits(mask):
                column ^= 1 << index[mask ^ (1<<j)]
            while column:
                pivot = column.bit_length()-1
                if pivot in pivots:
                    column ^= pivots[pivot]
                else:
                    pivots[pivot] = column
                    break
        ranks[k] = len(pivots)
    ranks[0] = 0
    return [len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0)-(1 if k==0 else 0)
            for k in range(max(bydim)+1)]

def verify(certificate):
    adjacency = read_graph(certificate['graph_edges'])
    D = distances(adjacency)
    X1 = rips_faces(D, 1)
    X2 = rips_faces(D, 2)
    X3 = rips_faces(D, 3)
    assert dimensions(X1) == [12,18,1]
    assert dimensions(X2) == certificate['expected']['initial_face_counts_by_dimension']
    assert len(X3) == (1 << N)-1
    assert boundary_ranks_mod2(X1) == [0,6,0]
    assert boundary_ranks_mod2(X2) == [0,0,4,0,0,0,0]
    faces = set(X2)
    for a,b in certificate['elementary_collapse_pairs']:
        assert a in faces and b in faces
        assert (a & b) == a and (b ^ a).bit_count() == 1
        codimension_one_cofaces = [a | 1 << i for i in range(N)
                if not (a >> i & 1) and (a | 1 << i) in faces]
        assert codimension_one_cofaces == [b], (a,b,codimension_one_cofaces)
        faces.remove(a)
        faces.remove(b)
    assert len(certificate['elementary_collapse_pairs']) == 119
    assert dimensions(faces) == [12,38,31]
    assert all(mask.bit_count() <= 3 for mask in faces)
    edges = sorted(tuple(bits(x)) for x in faces if x.bit_count() == 2)
    triangles = sorted(tuple(bits(x)) for x in faces if x.bit_count() == 3)
    tree = set(tuple(e) for e in certificate['spanning_tree_edges'])
    assert len(tree) == 11 and tree.issubset(edges)
    parent = list(range(N))
    def root(x):
        while x != parent[x]:
            x = parent[x]
        return x
    for a,b in sorted(tree):
        ra,rb = root(a),root(b)
        assert ra != rb  # no cycles
        parent[ra] = rb
    assert len({root(i) for i in range(N)}) == 1  # spanning tree
    other_edges = sorted(set(edges)-tree)
    assert len(other_edges) == 27
    index = {edge:i+1 for i,edge in enumerate(other_edges)}
    relations = []
    for a,b,c in triangles:
        word = []
        for x,y in [(a,b),(b,c),(c,a)]:
            e = tuple(sorted((x,y)))
            if e not in tree:
                word.append(index[e] if x < y else -index[e])
        relations.append(word)
    pending = set(index.values())
    for e in certificate['loop_cancellation_edges']:
        name = index[tuple(e)]
        assert name in pending
        # A relator with boundary word consisting solely of this generator
        # permits a one-cell/two-cell CW cancellation.
        i = next((i for i,w in enumerate(relations)
                  if len(w) == 1 and abs(w[0]) == name), None)
        assert i is not None, (name,relations)
        relations.pop(i)
        pending.remove(name)
        relations = [[v for v in word if abs(v) != name] for word in relations]
    assert len(certificate['loop_cancellation_edges']) == 27
    assert not pending
    assert len(relations) == 4 and all(not w for w in relations)
    # Contracting the tree preserves homotopy type; cancellations give
    # one 0-cell and four trivially attached 2-cells, a wedge of four S^2.
    print('PASS: Tietze cubic graph, 12 vertices, 18 edges, diameter 3')
    print('PASS: radii 1,2,3: 31,319,4095 nonempty faces')
    print('PASS: radius-two 119 elementary simplicial collapses')
    print('PASS: residual cell counts (vertices,edges,triangles): (12,38,31)')
    print('PASS: spanning tree 11 edges; 27 elementary CW cancellations')
    print('PASS: final CW model one 0-cell and four 2-cells')
    print('PASS: integral homotopy at radius 2 is wedge of four 2-spheres')
    print('PASS: reduced barcode: 11*[0,1) H0, 6*[1,2) H1, 4*[2,3) H2')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python3 verify_tietze.py collapse_certificate.json')
    with open(sys.argv[1], encoding='utf-8') as f:
        certificate = json.load(f)
    verify(certificate)

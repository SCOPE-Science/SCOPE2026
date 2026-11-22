#!/usr/bin/env python3
"""Exact finite simplicial-collapse and fundamental-group certificate.

Uses only Python standard library.  Run: python3 verify.py
"""
from itertools import combinations
from collections import Counter

LATIN = (
    (0, 1, 2, 3, 4),
    (1, 0, 3, 4, 2),
    (2, 3, 4, 0, 1),
    (3, 4, 1, 2, 0),
    (4, 2, 0, 1, 3),
)
N = 5
VERTICES = tuple(range(N*N))
assert all(set(row) == set(range(N)) for row in LATIN)
assert all({LATIN[i][j] for i in range(N)} == set(range(N)) for j in range(N))

def adjacent(a, b):
    if a == b:
        return False
    i, j = divmod(a, N)
    k, ell = divmod(b, N)
    return i == k or j == ell or LATIN[i][j] == LATIN[k][ell]

EDGES = tuple((a,b) for a,b in combinations(VERTICES,2) if adjacent(a,b))
EDGESET = set(EDGES)

def all_cliques():
    cliques = {()}
    layers = [(x,) for x in VERTICES]
    cliques.update(layers)
    while layers:
        new = []
        for face in layers:
            for v in range(face[-1]+1,N*N):
                if all((u,v) in EDGESET for u in face):
                    x = face + (v,)
                    new.append(x)
                    cliques.add(x)
        layers = new
    cliques.remove(())
    return cliques

def intercalates():
    found = []
    for i,k in combinations(range(N),2):
        for j,ell in combinations(range(N),2):
            a,b,c,d = LATIN[i][j],LATIN[i][ell],LATIN[k][j],LATIN[k][ell]
            if a == d and b == c:
                found.append((i,k,j,ell))
    return found

faces = all_cliques()
fv = Counter(map(len,faces))
assert fv == {1:25,2:150,3:250,4:79,5:15}, f'initial face vector {fv}'
assert len(intercalates()) == 4, intercalates()

removed = []
# At each dimension, all higher-dimensional faces have already disappeared.
for size in range(max(fv),3,-1):
    while True:
        candidates = sorted(face for face in faces if len(face)==size)
        if not candidates:
            break
        used = False
        for high in candidates:
            for low in combinations(high,size-1):
                containing = [f for f in faces if len(f)>len(low) and set(low).issubset(f)]
                if containing == [high] or (len(containing)==1 and containing[0]==high):
                    # Explicit elementary free-face collapse.
                    assert low in faces and high in faces
                    assert len(containing)==1
                    faces.remove(low)
                    faces.remove(high)
                    removed.append((low,high))
                    used = True
                    break
            if used:
                break
        assert used, f'no free pair at size {size}'
assert len(removed)==79
assert not any(len(f)>3 for f in faces)
assert Counter(map(len,faces)) == {1:25,2:150,3:186}
assert sum((-1)**(len(f)-1) for f in faces)==61
# Closure under taking nonempty faces: critical sanity check.
for f in faces:
    for j in range(1,len(f)):
        for sub in combinations(f,j):
            assert sub in faces

# Deterministic spanning tree by lexicographic Kruskal order.
parent=list(range(N*N))
def find(i):
    while parent[i]!=i:
        i=parent[i]
    return i

tree=set()
for a,b in EDGES:
    aa,bb=find(a),find(b)
    if aa!=bb:
        parent[aa]=bb
        tree.add((a,b))
assert len(tree)==N*N-1

# Elementary triangle relator eliminations.  Once two boundary edges
# have become trivial in the edge generators modulo the tree, the third
# edge becomes trivial.  If all non-tree edges are eliminated,
# van Kampen proves that the fundamental group is trivial.
triangles=tuple(sorted(f for f in faces if len(f)==3))
known=set(tree)
triangle_cert=[]
while True:
    start=len(known)
    for tri in triangles:
        sides=tuple(combinations(tri,2))
        missing=[edge for edge in sides if edge not in known]
        if len(missing)==1:
            known.add(missing[0])
            triangle_cert.append((tri,missing[0]))
    if len(known)==start:
        break
assert known==EDGESET, f'{len(known)} of {len(EDGESET)} edges reached'
assert len(triangle_cert)==len(EDGESET)-(N*N-1)==126

# Independent incidence-count sanity check: row, column, and symbol
# cliques contribute all 5-element maximal simplices, while each
# intercalate contributes an additional 4-element maximal simplex.
five=[f for f in all_cliques() if len(f)==5]
assert len(five)==3*N
for f in five:
    r={v//N for v in f};c={v%N for v in f};s={LATIN[v//N][v%N] for v in f}
    assert len(r)==1 or len(c)==1 or len(s)==1

print('LATIN5_NONCYCLIC_CLIQUE_PASS')
print('intercalates=4')
print('initial_faces=25,150,250,79,15')
print('free_collapse_pairs=79')
print('two_dimensional_spine_faces=25,150,186')
print('spanning_tree_edges=24')
print('triangular_relator_eliminations=126')
print('uneliminated_edges=0')
print('Euler_characteristic=61')
print('integral_homotopy_type=wedge_of_60_two_spheres')

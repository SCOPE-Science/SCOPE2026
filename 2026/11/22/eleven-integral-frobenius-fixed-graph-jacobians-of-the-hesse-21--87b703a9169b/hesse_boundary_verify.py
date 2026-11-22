#!/usr/bin/env python3
"""Exact verification of affine symmetry fixed graph-Jacobian groups of the
21-curve Hesse rational elliptic surface boundary.

Requires Python 3.10+ and SymPy 1.11+; run: python hesse_boundary_verify.py
All matrices and symmetry actions are constructed from explicit definitions.
"""
from itertools import product, combinations
from collections import Counter
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

F3 = range(3)
POINTS = list(product(F3, repeat=2))
NORMALS = ((1, 0), (0, 1), (1, 1), (1, 2))
LINES = [(j, c) for j in range(4) for c in F3]
VERTICES = [('P', p) for p in POINTS] + [('L', x) for x in LINES]
INDEX = {v: i for i, v in enumerate(VERTICES)}
assert len(VERTICES) == len(INDEX) == 21
EDGES = []
for p in POINTS:
    for j, (a, b) in enumerate(NORMALS):
        EDGES.append((INDEX[('P', p)], INDEX[('L', (j, (a*p[0]+b*p[1]) % 3))]))
for j in range(4):
    for c, d in combinations(F3, 2):
        EDGES.append((INDEX[('L', (j,c))], INDEX[('L', (j,d))]))
assert len(EDGES) == 48
assert len(set(map(frozenset, EDGES))) == 48
L = sp.zeros(21)
for i, j in EDGES:
    L[i, i] += 1; L[j, j] += 1; L[i, j] -= 1; L[j, i] -= 1
assert list(L.diagonal()) == [4]*9 + [5]*12
assert list(L * sp.ones(21, 1)) == [0]*21
B = L[1:, 1:]
assert B.det() == 3**10 * 7**8
assert all(x.q == 1 for x in 21 * B.inv())

def smith_nonunits(M):
    return tuple(abs(int(d)) for d in smith_normal_form(M, domain=ZZ).diagonal() if abs(d) > 1)

assert smith_nonunits(B) == (3, 3) + (21,)*8

def affine_permutation(m, t):
    a, b, c, d = m
    def image_point(p):
        return ((a*p[0]+b*p[1]+t[0]) % 3, (c*p[0]+d*p[1]+t[1]) % 3)
    images = {p: image_point(p) for p in POINTS}
    perm = [INDEX[('P', images[p])] for p in POINTS]
    for j, (x, y) in enumerate(NORMALS):
        for level in F3:
            target = [images[p] for p in POINTS if (x*p[0]+y*p[1]) % 3 == level]
            matches = [(k, next(iter(values))) for k, (u, v) in enumerate(NORMALS)
                       if len(values := {(u*z[0]+v*z[1]) % 3 for z in target}) == 1]
            assert len(matches) == 1
            perm.append(INDEX[('L', matches[0])])
    assert set(perm) == set(range(21))
    assert {frozenset((perm[i],perm[j])) for i,j in EDGES} == {frozenset(e) for e in EDGES}
    return tuple(perm)

ACTIONS = {}
for matrix in product(F3, repeat=4):
    a,b,c,d = matrix
    det = (a*d-b*c) % 3
    if det:
        for t in POINTS:
            p = affine_permutation(matrix, t)
            assert p not in ACTIONS
            ACTIONS[p] = (matrix, t, det)
assert len(ACTIONS) == 432
GROUP = list(ACTIONS)
PERM_INDEX = {p:i for i,p in enumerate(GROUP)}
INVERSES = []
for p in GROUP:
    q=[-1]*21
    for i, k in enumerate(p): q[k] = i
    INVERSES.append(tuple(q))

def compose(p, q):
    return tuple(p[q[i]] for i in range(21))

CLASSES=[]
unseen=set(range(432))
while unseen:
    representative=GROUP[min(unseen)]
    members={PERM_INDEX[compose(compose(h, representative), hinverse)]
             for h, hinverse in zip(GROUP, INVERSES)}
    assert members <= unseen
    CLASSES.append((representative, members))
    unseen -= members
assert len(CLASSES) == 11
assert sum(len(members) for _, members in CLASSES) == 432
assert sorted(len(members) for _,members in CLASSES) == [1,8,9,24,36,48,54,54,54,72,72]

def image_matrix(perm, sink=0):
    other=[i for i in range(21) if i != sink]
    pos={v:i for i,v in enumerate(other)}
    P=sp.zeros(20)
    for j,v in enumerate(other):
        if perm[v] != sink: P[pos[perm[v]],j] += 1
        if perm[sink] != sink: P[pos[perm[sink]],j] -= 1
    return P

def mod_rank(matrix, p):
    """Independent modular Gaussian elimination, not using Smith routines."""
    a = [[int(x) % p for x in matrix.row(i)] for i in range(matrix.rows)]
    k=0
    for j in range(matrix.cols):
        pivot=next((i for i in range(k,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[pivot],a[k]=a[k],a[pivot]
        inverse=pow(a[k][j],-1,p)
        a[k]=[(z*inverse)%p for z in a[k]]
        for i in range(k+1,len(a)):
            if a[i][j]:
                v=a[i][j]
                a[i]=[(a[i][h]-v*a[k][h])%p for h in range(matrix.cols)]
        k+=1
        if k==len(a):break
    return k

def coinvariant_matrix(perm,sink=0):
    other=[i for i in range(21) if i!=sink]
    reduced=L.extract(other,other)
    return reduced.row_join(image_matrix(perm,sink)-sp.eye(20))

def group_from_ranks(r3,r7):
    # exponent divides 21, hence each primary component is elementary abelian
    return tuple([3]*(r3-min(r3,r7)) + [7]*(r7-min(r3,r7)) + [21]*min(r3,r7))

# Class rows: (size, determinant, group-element order, 3-rank, 7-rank).
EXPECTED = [(36,2,2,6,5),(72,2,6,2,1),(54,2,8,0,1),
            (54,2,8,0,1),(54,1,4,2,2),(72,1,6,2,2),
            (24,1,3,4,4),(48,1,3,4,2),(1,1,1,10,8),
            (8,1,3,4,2),(9,1,2,6,4)]

def cycle_type(perm):
    unseen=set(range(len(perm))); lengths=[]
    while unseen:
        start=min(unseen); i=start; length=0
        while i in unseen:
            unseen.remove(i);length+=1;i=perm[i]
        assert i==start
        lengths.append(length)
    return tuple(sorted(lengths))

EDGE_INDEX={frozenset(pair):i for i,pair in enumerate(EDGES)}

def edge_perm(perm):
    return tuple(EDGE_INDEX[frozenset((perm[i],perm[j]))] for i,j in EDGES)

REPORT=[]
for i,(p,members) in enumerate(CLASSES):
    matrix,t,det=ACTIONS[p]
    size,edet,order,r3,r7=EXPECTED[i]
    assert (len(members),det) == (size,edet)
    assert sp.ilcm(*cycle_type(p)) == order
    # Independently: rational inverse confirms the induced action respects im L.
    assert all(x.q == 1 for x in B.inv()*image_matrix(p)*B)
    M=coinvariant_matrix(p)
    f=smith_nonunits(M)
    assert f==group_from_ranks(r3,r7)
    assert (20-mod_rank(M,3),20-mod_rank(M,7)) == (r3,r7)
    # Different deleted vertex: a separate exact integral presentation.
    assert smith_nonunits(coinvariant_matrix(p,10)) == f
    assert (20-mod_rank(coinvariant_matrix(p,10),3),
            20-mod_rank(coinvariant_matrix(p,10),7)) == (r3,r7)
    for member in members:
        q=GROUP[member]
        # All 432 transformations checked independently, not just one per class.
        N=coinvariant_matrix(q)
        assert (20-mod_rank(N,3),20-mod_rank(N,7)) == (r3,r7)
    REPORT.append((i,size,det,order,matrix,t,cycle_type(p),cycle_type(edge_perm(p)),f))

# The 216-element determinant-one Hessian subgroup is generated by two
# independent translations and two elementary matrices in SL_2(F_3).
def lookup(m,t):
    return next(p for p,(mat,tr,_) in ACTIONS.items() if mat==m and tr==t)
translations=[lookup((1,0,0,1),(1,0)),lookup((1,0,0,1),(0,1))]
S=lookup((1,1,0,1),(0,0))
T=lookup((1,0,1,1),(0,0))
W=lookup((0,1,1,0),(0,0))
for name,gens,expected in [('translation',translations,(3,3,3)),
                           ('hessian',translations+[S,T],()),
                           ('full_affine',translations+[S,T,W],())]:
    M=B
    for gen in gens:
        M=M.row_join(image_matrix(gen)-sp.eye(20))
    assert smith_nonunits(M)==expected

print('HESSE_21_CURVE_BOUNDARY_ALL_432_AFFINE_ACTIONS_VERIFIED')
print('vertices=21 edges=48 genus=28; nonequivariant_group=(3,3,21^8)')
print('class_id size determinant order matrix translation vertex_cycles node_cycles fixed_invariants')
for row in REPORT:
    print(*row)
print('HESSIAN_216_INVARIANTS_TRIVIAL; FULL_AFFINE_432_INVARIANTS_TRIVIAL')

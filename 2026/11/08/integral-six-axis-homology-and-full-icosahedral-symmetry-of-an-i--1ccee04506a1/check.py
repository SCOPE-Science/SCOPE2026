"""Reproduce structural and equivariant integral homology of the icosahedral independence complex.
Dependencies: Python >=3.10, networkx >=2.8, sympy >=1.10.
No internet and no input files required.
"""
from itertools import combinations
from collections import Counter, defaultdict
from math import factorial
import networkx as nx
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

N = 12
ADJ = [
(1,5,7,8,11), (0,2,5,6,8), (1,3,6,8,9),
(2,4,6,9,10), (3,5,6,10,11), (0,1,4,6,11),
(1,2,3,4,5), (0,8,9,10,11), (0,1,2,7,9),
(2,3,7,8,10), (3,4,7,9,11), (0,4,5,7,10)]
G = nx.Graph()
G.add_nodes_from(range(N))
G.add_edges_from((i,j) for i in range(N) for j in ADJ[i] if i<j)
assert len(G.edges()) == 30 and all(G.degree(v)==5 for v in G)
assert [tuple(sorted(G.neighbors(v))) for v in range(N)] == ADJ
D=dict(nx.all_pairs_shortest_path_length(G))
assert nx.diameter(G)==3
ANTI=[next(j for j in range(N) if D[i][j]==3) for i in range(N)]
assert all(ANTI[ANTI[i]]==i and ANTI[i]!=i for i in range(N))
axes=sorted(set(tuple(sorted((i,ANTI[i]))) for i in range(N)))
assert len(axes)==6
assert all(sum(D[i][j]==2 for j in range(N))==5 for i in range(N))

simplices={q:[c for c in combinations(range(N),q+1) if all(D[a][b]>=2 for a,b in combinations(c,2))] for q in range(3)}
assert [len(simplices[i]) for i in range(3)]==[12,36,20]
assert all(not all(D[a][b]>=2 for a,b in combinations(c,2)) for c in combinations(range(N),4))
triangle_edges=Counter(e for t in simplices[2] for e in combinations(t,2))
E2={tuple(sorted((a,b))) for a,b in combinations(range(N),2) if D[a][b]==2}
assert set(triangle_edges)==E2 and all(c==2 for c in triangle_edges.values())
assert set(simplices[1])==E2|set(axes)
# The triangle subcomplex S is a closed connected two-manifold:
S=nx.Graph();S.add_nodes_from(range(N));S.add_edges_from(E2)
assert nx.is_connected(S)
for v in range(N):
    link=nx.Graph()
    link.add_nodes_from(S.neighbors(v))
    link.add_edges_from(tuple(sorted(set(t)-{v})) for t in simplices[2] if v in t)
    assert len(link)==5 and len(link.edges())==5 and nx.is_connected(link)
    assert all(link.degree(u)==2 for u in link)
assert len(S.edges())==30 and 12-30+20==2
# Connected closed combinatorial surface of Euler characteristic 2 is a sphere.
# The six remaining edges are attached along their endpoints, and no triangle uses them.

# Exact integral boundary computation including all simplices.
def boundary(k):
    idx={s:i for i,s in enumerate(simplices[k-1])}
    M=sp.zeros(len(simplices[k-1]),len(simplices[k]))
    for j,s in enumerate(simplices[k]):
        for u in range(len(s)):
            f=s[:u]+s[u+1:]
            M[idx[f],j]=(-1)**u
    return M
B1=boundary(1); B2=boundary(2)
assert B1*B2 == sp.zeros(12,20)
assert B1.rank()==11 and B2.rank()==19
smith=smith_normal_form(B2,domain=ZZ)
assert [int(smith[i,i]) for i in range(19)] == [1]*19
assert smith[19,19]==0
cycle=list(B2.nullspace()[0]);assert all(abs(t)==1 for t in cycle)

# Signed simplicial chain traces and induced orientations.
def parity(values):
    return (-1)**sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))
def chaintrace(s,p):
    z=0
    for face in simplices[s]:
        image=[p[v] for v in face]
        if set(image)==set(face): z+=parity(image)
    return z

def porder(p):
    q=list(range(N))
    for k in range(1,13):
        q=[p[q[i]] for i in range(N)]
        if q==list(range(N)): return k
    raise AssertionError('bad order')

aut=[tuple(m[i] for i in range(N)) for m in nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter()]
assert len(aut)==120 and len(set(aut))==120
center=tuple(ANTI)
assert center in aut and porder(center)==2
assert all(tuple(center[p[i]] for i in range(N))==tuple(p[center[i]] for i in range(N)) for p in aut)

# Each automorphism acts by +/-1 on the unique oriented sphere 2-cycle.
face_to_index={s:i for i,s in enumerate(simplices[2])}
allchars={}
for p in aut:
    image=[p[u] for u in simplices[2][0]]
    k=face_to_index[tuple(sorted(image))]
    chi2=int(cycle[0]*cycle[k])*parity(image)
    assert chi2 in (1,-1)
    for i,face in enumerate(simplices[2]):
        image=[p[u] for u in face]
        j=face_to_index[tuple(sorted(image))]
        assert int(cycle[i])*parity(image)==chi2*int(cycle[j])
    chi1=chi2-(chaintrace(0,p)-chaintrace(1,p)+chaintrace(2,p)-1)
    # Relative H_1(X,S) is the signed six-axis permutation lattice.
    signed_axes=0
    for a,b in axes:
        aa,bb=p[a],p[b]
        if {aa,bb}=={a,b}:signed_axes += 1 if (aa,bb)==(a,b) else -1
    assert chi1==signed_axes
    allchars[p]=(chi1,chi2)
assert allchars[center]==(-6,-1)
assert sum(x[0] for x in allchars.values())==0
assert sum(x[1] for x in allchars.values())==0

# Exhaustively reconstruct conjugacy classes, independently of class names.
def compose(p,q):
    return tuple(p[q[i]] for i in range(N))
def inverse(p):
    ans=[0]*N
    for i,j in enumerate(p):ans[j]=i
    return tuple(ans)
unseen=set(aut)
classes=[]
while unseen:
    p=min(unseen)
    class_set={compose(compose(h,p),inverse(h)) for h in aut}
    assert class_set<=unseen
    assert len({allchars[x] for x in class_set})==1
    classes.append(class_set)
    unseen-=class_set
assert len(classes)==10 and sum(map(len,classes))==120
class_data=Counter()
for cl in classes:
    p=min(cl)
    coset='A5' if allchars[p][1]==1 else 'inversion*A5'
    rot_factor=p if coset=='A5' else compose(center,p)
    class_data[(coset,porder(rot_factor),len(cl),allchars[p][0],allchars[p][1])]+=1
assert class_data==Counter({
    ('A5',1,1,6,1):1,('A5',2,15,-2,1):1,('A5',3,20,0,1):1,
    ('A5',5,12,1,1):2,
    ('inversion*A5',1,1,-6,-1):1,('inversion*A5',2,15,2,-1):1,
    ('inversion*A5',3,20,0,-1):1,('inversion*A5',5,12,-1,-1):2})

# Geometrically: SO(3) rotation subgroup has size 60, inversion coset has size 60.
rot=[p for p,v in allchars.items() if v[1]==1]
assert len(rot)==60 and len(aut)-len(rot)==60
rot_counts=Counter((porder(p),allchars[p][0]) for p in rot)
assert rot_counts=={(1,6):1,(2,-2):15,(3,0):20,(5,1):24}
# Rational A_5 character (6,-2,0,1,1) is the sum of the Galois-conjugate
# complex 3-dimensional icosahedral characters; it is Q-irreducible.
# For each coset, 5A and 5B each have size 12, and share the computed trace.
print('VERTICES_EDGES_FACES 12 36 20')
print('SPHERE_TRIANGULATION 12 30 20 LINK_5_CYCLES_12')
print('EXTRA_ANTIPODAL_EDGES',axes)
print('BOUNDARY_RANKS 11 19; SMITH_B2 1x19 0x1')
print('REDUCED_HOMOLOGY H1=Z^6 H2=Z; OTHERS=0')
print('AUT_ORDER 120; ROTATION_ORDER 60; TEN_CONJUGACY_CLASSES 10; INVERSION_CHARS (-6,-1)')
print('TABLE: coset order size H1 H2')
for coset in ('A5','inversion*A5'):
    sign=1 if coset=='A5' else -1
    for order, size, h1 in [(1,1,6),(2,15,-2),(3,20,0),(5,12,1),(5,12,1)]:
        print(coset, order, size,sign*h1,sign)
print('CHECK_ALL_120_AUTOMORPHISMS_PASS')

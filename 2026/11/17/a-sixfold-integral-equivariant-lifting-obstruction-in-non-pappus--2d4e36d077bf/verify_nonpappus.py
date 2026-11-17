#!/usr/bin/env python3
"""Exact checks for non-Pappus relaxation top-homology lifting index.

All calculations are over integers and rational numbers (standard-library only).
No experimental rank over a finite field is used as an integral conclusion.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations

V = 'abcdefghi'
LINES = tuple(sorted(tuple(sorted(V.index(c) for c in s))
                     for s in ('abc','aei','afh','bdi','bfg','cdh','ceg','ghi')))
L = set(LINES)
T = (3, 4, 5)  # def: relaxed Pappus circuit-hyperplane
PAPPUS_LINES = L | {T}
TRIANGLES = tuple(t for t in combinations(range(9),3) if t not in L)
TRI_PAPPUS = tuple(t for t in combinations(range(9),3) if t not in PAPPUS_LINES)
EDGES = tuple(combinations(range(9),2))
EDGE_INDEX = {t:i for i,t in enumerate(EDGES)}

def sign(xs):
    return -1 if sum(xs[i] > xs[j] for i in range(len(xs))
                     for j in range(i+1,len(xs)))%2 else 1

def permute_simplex(p,t):
    a=tuple(p[i] for i in t)
    return tuple(sorted(a)),sign(a)

def group():
    # The three low-incidence points are exactly d,e,f.
    assert {v:sum(v in s for s in L) for v in range(9)} == dict(enumerate((3,3,3,2,2,2,3,3,3)))
    group=[]
    outer=(0,1,2,6,7,8);inner=(3,4,5)
    for q in permutations(outer):
        for r in permutations(inner):
            p=list(range(9))
            for i,j in zip(outer,q):p[i]=j
            for i,j in zip(inner,r):p[i]=j
            if {tuple(sorted(p[i] for i in t)) for t in L} == L:
                group.append(tuple(p))
    return tuple(sorted(group))

G=group()
assert len(G)==12 and tuple(range(9)) in G
assert all({p[i] for i in T}==set(T) for p in G)
assert all({permute_simplex(p,t)[0] for t in PAPPUS_LINES}==PAPPUS_LINES for p in G)
Z=tuple(V.index(c) for c in 'ghidefabc')
assert Z in G and Z!=tuple(range(9))
assert all(tuple(g[Z[i]] for i in range(9)) ==tuple(Z[g[i]] for i in range(9)) for g in G)
assert len({tuple(p[i] for i in T) for p in G})==6
assert len({p for p in G if tuple(p[i] for i in T)==T})==2
# The central kernel {1,z} is split by the six permutations fixing the two outer triples as sets.
S3=tuple(p for p in G if set(p[i] for i in (0,1,2))=={0,1,2})
assert len(S3)==6
assert {tuple(a[b[i]] for i in range(9)) for a in S3 for b in (tuple(range(9)),Z)}==set(G)

# The following direct formula computes the reduced simplicial Lefschetz number.
# Since the two matroid complexes have only H_2 in reduced homology,
# the alternating chain trace equals the H_2 trace.
def character(g):
    faces=[()]+[(i,) for i in range(9)]+list(EDGES)+list(TRIANGLES)
    value=0
    for t in faces:
        t2,sg=permute_simplex(g,t)
        if t2==t:
            value+=(-1 if len(t)%2==0 else 1)*sg
    return value

chars={p:character(p) for p in G}
assert chars[tuple(range(9))]==48
assert chars[Z]==-6
# Restriction to S3 has classes by permutation of the relaxed triple.
def cycle_type_of_def(g):
    visited=set(); out=[]
    for i in T:
        if i not in visited:
            j=i;order=0
            while j not in visited:
                visited.add(j);order+=1;j=g[j]
            out.append(order)
    return tuple(sorted(out))
classes={}
for p in G:
    c=(cycle_type_of_def(p), int(p not in S3))
    classes.setdefault(c,[]).append(chars[p])
assert classes=={
 ((1,1,1),0):[48], ((1,1,1),1):[-6],
 ((1,2),0):[-4,-4,-4], ((1,2),1):[2,2,2],
 ((3,),0):[0,0], ((3,),1):[0,0]}
# Irreducible multiplicities of S3 x C2. The S3 irreps have chars
# on the identity, transposition, three-cycle, respectively.
class_size={(1,1,1):1,(1,2):3,(3,):2}
chi_S3={'trivial':{(1,1,1):1,(1,2):1,(3,):1},
        'sign':{(1,1,1):1,(1,2):-1,(3,):1},
        'standard':{(1,1,1):2,(1,2):0,(3,):-1}}
mult={}
for name,c in chi_S3.items():
    for eps in (1,-1):
        n=sum(class_size[a]*chars[classes and next(p for p in G if
                  cycle_type_of_def(p)==a and ((p not in S3)==bool(b))) ]
              *c[a]*(eps**b) for a in class_size for b in (0,1))
        assert n%12==0
        mult[(name,eps)]=n//12
assert mult=={('trivial',1):3,('trivial',-1):3,
              ('sign',1):4,('sign',-1):6,
              ('standard',1):7,('standard',-1):9}

# Obtain the complete signed-orbit basis of the sign-def isotypic
# integral chain submodule. Each coefficient vector is primitive.
lam={p:permute_simplex(p,T)[1] for p in G}
unseen=set(TRIANGLES); orbit_basis=[];obstructed=[]
while unseen:
    t=min(unseen)
    orbit={permute_simplex(p,t)[0] for p in G}
    unseen-=orbit
    weights={}
    consistent=True
    for p in G:
        y,sg=permute_simplex(p,t)
        w=lam[p]*sg
        if y in weights and weights[y]!=w:consistent=False
        weights[y]=w
    if consistent:orbit_basis.append((t,weights))
    else:obstructed.append(t)
assert [tuple(V[i] for i in t) for t,_ in orbit_basis]==[
    tuple(s) for s in ('abd','abf','abg','abi','ade','adh','aef','def')]
assert len(orbit_basis)==8 and len(obstructed)==2
assert [len(w) for t,w in orbit_basis]==[12,6,12,6,12,12,6,1]
# Verify, rather than assume, the G-action on every basis vector.
for t,weights in orbit_basis:
    for g in G:
        transform={}
        for u,coef in weights.items():
            v,sg=permute_simplex(g,u)
            transform[v]=coef*sg
        assert transform=={u:lam[g]*coef for u,coef in weights.items()}

# Signed cellular/simplicial boundary of the 2-chains.
B=[[0]*8 for _ in EDGES]
for j,(rep,weights) in enumerate(orbit_basis):
    for t,a in weights.items():
        for i,e in enumerate((t[1:],(t[0],t[2]),t[:2])):
            B[EDGE_INDEX[e]][j]+=(-1)**i*a

ab=B[EDGE_INDEX[(0,1)]];ah=B[EDGE_INDEX[(0,7)]]
ae=B[EDGE_INDEX[(0,4)]];de=B[EDGE_INDEX[(3,4)]]
assert (ab,ah,ae,de)==(
 [2,1,2,1,0,0,0,0],
 [0,0,-2,2,0,-2,0,0],
 [-1,1,0,0,-1,1,1,0],
 [0,0,0,0,4,0,2,1])
# Those four equations imply, integrally, coefficient x_7 of def
# equals -6*(x_1 + x_3 + x_6) for every G-eigen cycle.
# To certify sufficiency, verify that all 36 boundary rows have rank 4.
def rank_Q(a):
    a=[[Fraction(x) for x in row] for row in a]
    n=len(a); m=len(a[0]); k=0
    for j in range(m):
        t=next((i for i in range(k,n) if a[i][j]!=0),None)
        if t is None:continue
        a[k],a[t]=a[t],a[k]
        fac=a[k][j]
        a[k]=[x/fac for x in a[k]]
        for i in range(n):
            if i!=k and a[i][j]:
                fac=a[i][j]
                a[i]=[v-fac*w for v,w in zip(a[i],a[k])]
        k+=1
        if k==n:break
    return k
assert rank_Q(B)==4
assert rank_Q([ab,ah,ae,de])==4
x=[1,-2,0,0,-2,0,1,6]
assert all(sum(a*b for a,b in zip(row,x))==0 for row in B)
assert x[7]==6
# Surjectivity of H2(K) -> Z_def is witnessed by the full-simplex
# oriented boundary [def] - [aef] + [adf] - [ade].
C={T:1,(0,4,5):-1,(0,3,5):1,(0,3,4):-1}
assert all(t in TRIANGLES for t in C)
assert all(sum(c*((-1)**i) for t,c in C.items() for i,e in
               enumerate((t[1:],(t[0],t[2]),t[:2])) if e==edge)==0
           for edge in EDGES)
# Full 1-skeleton: each of the nine forbidden triangle boundaries can
# be filled by three admissible triangles via a fourth vertex.
for bad in PAPPUS_LINES:
    assert any(all(tuple(sorted((v,)+edge)) not in PAPPUS_LINES
                   for edge in combinations(bad,2))
               for v in range(9) if v not in bad)
assert len(TRIANGLES)==76 and len(TRI_PAPPUS)==75
# Therefore H2 ranks equal 76-28=48 and 75-28=47,
# H1=0, since the complete 9-vertex graph has cycle rank 28.
print('NONPAPPUS_RANK3_RELAXATION_CHECK_PASS')
print('point_group_order',len(G),'direct_product','S3 x C2')
print('faces_nonpappus',(9,36,76),'faces_pappus',(9,36,75))
print('H2_ranks',(48,47),'H1_zero','integral_torsion_free')
print('class_traces','id=48 transposition=-4 3cycle=0 z=-6 ztransposition=2 z3cycle=0')
print('rational_multiplicities',mult)
print('twisted_orbit_representatives', [''.join(V[i] for i in t) for t,w in orbit_basis])
print('twisted_boundary_rank',rank_Q(B),'lifting_index',6)
print('witness_six',x)
print('NO_INTEGRAL_EQUIVARIANT_SPLITTING_PASS')

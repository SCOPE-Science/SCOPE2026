#!/usr/bin/env python3
"""Reproducible exact certificate for Franklin graph independence homology.

Requires Python 3, networkx, sympy. No external files are read.
"""
import itertools
import collections
import hashlib
import math
import networkx as nx
from sympy import SparseMatrix, Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 12
# The standard [5,-5]^6 LCF representation of the Franklin graph.
g = nx.cycle_graph(N)
for i in range(N):
    g.add_edge(i,(i+(5 if i%2 == 0 else -5)) % N)
assert g.number_of_edges() == 18
assert all(d==3 for _, d in g.degree())
adj=[sum(1<<j for j in g.neighbors(i)) for i in range(N)]
faces=[[] for _ in range(N+1)]
def independent_search(mask, options, k):
    if mask:faces[k].append(mask)
    while options:
        b=options&-options; options-=b
        independent_search(mask|b, options&~adj[b.bit_length()-1], k+1)
independent_search(0, (1<<N)-1, 0)
assert [len(faces[k]) for k in range(1,7)] == [12,48,76,45,12,2]
assert not any(faces[7:])
F={m for a in faces for m in a}
assert len(F)==195
assert all(not any((adj[i]&m) for i in range(N) if m>>i&1) for m in F)

# A complete acyclic matching of the nonempty face poset.
order=[1,2,8,5,11,10,4,0,6,7,3,9]
free=set(F); matched=[]
for v in order:
    t=1<<v
    lower=[s for s in sorted(free) if not s&t and (s|t) in free]
    for s in lower:
        assert s in free and (s|t) in free
        free.remove(s);free.remove(s|t)
        matched.append((s,s|t))
assert len(matched)==95
assert len(free)==5
assert collections.Counter(s.bit_count()-1 for s in free)=={0:1,2:4}
assert len(set(z for pair in matched for z in pair))==190
match_up=set(matched)
D=nx.DiGraph();D.add_nodes_from(F)
incidence=0
for k in range(2,7):
    for high in faces[k]:
        for i in range(N):
            if not (high>>i&1):continue
            low=high^(1<<i);incidence+=1
            if (low,high) in match_up:D.add_edge(low,high)
            else:D.add_edge(high,low)
assert nx.is_directed_acyclic_graph(D)
print('FACES',*(len(faces[k]) for k in range(1,7)), 'TOTAL',len(F))
print('MORSE_PAIRS',len(matched),'INCIDENCES',incidence,'CRITICAL',sorted((s.bit_count()-1,s) for s in free),'ACYCLIC',True)
# A pointed Morse CW model with one 0-cell and four 2-cells is a wedge of four 2-spheres.

# Integral simplicial boundary maps, degree k-1 uses faces with k vertices.
def boundary(k):
    row={s:i for i,s in enumerate(faces[k-1])}
    out={}
    for j,s in enumerate(faces[k]):
        b=[i for i in range(N) if s>>i&1]
        for t,i in enumerate(b):out[(row[s^(1<<i)],j)]=(-1)**t
    return SparseMatrix(len(faces[k-1]),len(faces[k]),out)
B2=boundary(3) # C_2 -> C_1, 48x76
B3=boundary(4) # C_3 -> C_2, 76x45
assert B2*B3==SparseMatrix(48,45,{})
assert B2.rank()==37
assert B3.rank()==35

# Induced 3-matchings give embedded octahedral boundaries S^0*S^0*S^0=S^2.
E=list(g.edges()); triples=[]
for tri in itertools.combinations(E,3):
    vertices={v for e in tri for v in e}
    if len(vertices)!=6:continue
    if sum(1 for a,b in E if a in vertices and b in vertices)==3:
        triples.append(tuple(tuple(sorted(e)) for e in tri))
assert len(triples)==20
idx2={s:i for i,s in enumerate(faces[3])}
C=SparseMatrix(76,20,{})
for j,tri in enumerate(triples):
    for flags in itertools.product((0,1),repeat=3):
        picked=[tri[k][flags[k]] for k in range(3)]
        sign=(-1)**(sum(flags)+sum(picked[a]>picked[b] for a in range(3) for b in range(a+1,3)))
        s=sum(1<<v for v in picked)
        C[idx2[s],j]=sign
assert B2*C==SparseMatrix(48,20,{})
assert C.rank()==17
BC=B3.row_join(C)
assert BC.rank()==39
smith=smith_normal_form(BC,domain=ZZ)
inv=[abs(int(smith[i,i])) for i in range(min(smith.shape)) if smith[i,i]!=0]
assert inv == [1]*39
# BC lies in the saturated rank-39 kernel of B2, so equality as Z-lattices.
# Four explicit embedded spheres form an integral basis, not just a spanning orbit.
basis_indices=[5,6,8,11]
assert [triples[j] for j in basis_indices] == [
    ((0,11),(2,7),(4,9)),
    ((0,11),(3,4),(7,8)),
    ((0,5),(2,7),(9,10)),
    ((1,2),(4,9),(6,11))]
Bbasis=B3.row_join(C[:,basis_indices])
assert Bbasis.rank()==39
sb=smith_normal_form(Bbasis,domain=ZZ)
assert [abs(int(sb[i,i])) for i in range(min(sb.shape)) if sb[i,i]!=0]==[1]*39
print('INTEGRAL_OCTAHEDRAL_BASIS',basis_indices)
print('OCTAHEDRAL_SPHERES',len(triples),'CYCLE_RANK',C.rank(),'B3_RANK',B3.rank(),'B3_PLUS_C_RANK',BC.rank())
print('B3_PLUS_C_SMITH',collections.Counter(inv),'INTEGRAL_H2_GENERATED',True)

# Exact group enumeration and signed fixed-simplex Lefschetz traces.
perms=sorted(tuple(a[i] for i in range(N)) for a in nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter())
assert len(perms)==48 and len(set(perms))==48
I=tuple(range(N))
assert I in perms
P=set(perms)
def compose(p,q):return tuple(p[q[i]] for i in range(N))
def inverse(p):return tuple(p.index(i) for i in range(N))
assert all(compose(p,q) in P for p in perms for q in perms)
central=[p for p in perms if all(compose(p,q)==compose(q,p) for q in perms)]
assert len(central)==2
z=next(p for p in central if p!=I)
assert compose(z,z)==I
# Signed trace on reduced simplicial chains; only H2 survives.
def character(p):
    out=-1 # empty simplex in reduced chain complex
    for k in range(1,7):
        for s in faces[k]:
            b=[i for i in range(N) if s>>i&1]
            pb=[p[i] for i in b]
            if set(pb)!=set(b):continue
            inversions=sum(pb[a]>pb[b] for a in range(k) for b in range(a+1,k))
            out+=(-1)**(k-1+inversions)
    return out
chi={p:character(p) for p in perms}
assert chi[I]==4 and chi[z]==-2
assert sum(chi.values())==48 # one invariant line
assert sum(v*v for v in chi.values())==96 # trivial+absolute irreducible
assert collections.Counter(chi.values())=={1:16,2:15,0:15,4:1,-2:1}
# Verify that the induced geometric spheres are sent to signed geometric spheres.
triple_set={tuple(sorted(e for e in tri)) for tri in triples}
for p in perms:
    for tri in triples:
        image=tuple(sorted(tuple(sorted((p[a],p[b]))) for a,b in tri))
        assert image in triple_set
# Exactly two orbits; the orbit of eight octahedral spheres already gives an
# integral generating set. The orbit of twelve has rank three modulo boundaries.
T={tuple(sorted(e for e in tri)):j for j,tri in enumerate(triples)}
remaining=set(T);orbit_indices=[]
while remaining:
    a=min(remaining)
    orb={tuple(sorted(tuple(sorted((p[x],p[y]))) for x,y in a)) for p in perms}
    assert orb <= remaining
    orbit_indices.append(sorted(T[o] for o in orb))
    remaining-=orb
assert sorted(len(o) for o in orbit_indices)==[8,12]
for orbit in orbit_indices:
    M=B3.row_join(C[:,orbit])
    d=smith_normal_form(M,domain=ZZ)
    iv=[abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]!=0]
    assert len(iv)==(39 if len(orbit)==8 else 38)
    assert all(t==1 for t in iv)
    print('OCTAHEDRAL_ORBIT',len(orbit),'INTEGRAL_SMITH',collections.Counter(iv),'MOD_BOUNDARY_RANK',len(iv)-35)

# Class table: classify by actual conjugacy, not just by cycle type.
remaining=set(perms); classes=[]
while remaining:
    rep=min(remaining)
    cls={compose(compose(q,rep),inverse(q)) for q in perms}
    assert len(cls.intersection(remaining))==len(cls)
    assert len({chi[p] for p in cls})==1
    classes.append((rep,cls,chi[rep]))
    remaining-=cls
assert len(classes)==10

def cycles(p):
    visited=set();out=[]
    for i in range(N):
        if i in visited:continue
        cyc=[];j=i
        while j not in visited:
            visited.add(j);cyc.append(j);j=p[j]
        if len(cyc)>1:out.append('('+' '.join(str(t) for t in cyc)+')')
    return ''.join(out) or '()'
classes.sort(key=lambda x:(-len(x[1]),x[2],x[0]))
print('AUT_ORDER',len(perms),'CENTER',cycles(z),'CENTER_CHARACTER',chi[z])
print('CHARACTER_NORM',sum(v*v for v in chi.values()),'FULL_INVARIANT_DIM',sum(chi.values())//48)
print('CONJUGACY_CLASSES',len(classes))
for j,(r,cls,v) in enumerate(classes,1):
    print('CLASS',j,'SIZE',len(cls),'CHI',v,'REP',cycles(r))
# Independent verification of the FULL INTEGRAL action on the four displayed sphere cycles:
# solve against an integer basis of 3-boundaries together with the four cycles.
from sympy import Matrix
pivot_cols=B3.rref()[1]
assert len(pivot_cols)==35
M=B3[:,list(pivot_cols)].row_join(C[:,basis_indices])
pivot_rows=M.T.rref()[1]
assert len(pivot_rows)==39
MI=M[list(pivot_rows),:].inv()
def simplex_action(p,vector):
    image=SparseMatrix(76,1,{})
    for i in range(76):
        val=vector[i]
        if val==0:continue
        b=[x for x in range(N) if faces[3][i]>>x&1]
        pb=[p[x] for x in b]
        sign=(-1)**sum(pb[a]>pb[c] for a in range(3) for c in range(a+1,3))
        image[idx2[sum(1<<x for x in pb)]]+=sign*val
    return image
actions={}
for p in perms:
    columns=[]
    for j in basis_indices:
        y=simplex_action(p,C[:,j])
        sol=MI*y[list(pivot_rows),:]
        assert M*sol==y
        assert all(t.q==1 for t in sol)
        columns.append(sol[35:39,:])
    mat=Matrix.hstack(*columns)
    assert mat.det() in (-1,1)
    assert mat.trace()==chi[p]
    actions[p]=mat
assert all(actions[compose(p,q)]==actions[p]*actions[q] for p in perms for q in perms)
generators=[
    (2,3,4,5,6,7,8,9,10,11,0,1),
    (1,0,5,4,9,8,7,6,11,10,3,2),
    (0,1,2,3,10,11,6,7,8,9,4,5),
]
assert all(p in actions for p in generators)
closure={I};front=[I]
while front:
    h=front.pop()
    for p in generators:
        j=compose(h,p)
        if j not in closure:
            closure.add(j);front.append(j)
assert closure==P
v=Matrix([1,1,1,1])
assert all(actions[p]*v==v for p in perms)
assert actions[z].trace()==-2
for j,p in enumerate(generators,1):
    print('GENERATOR',j,'PERM',p,'MATRIX_ROWS',actions[p].tolist())
print('INVARIANT_PRIMITIVE_BASIS_VECTOR',[1,1,1,1])
# Recover the symmetric-four factor without assuming its identification.
# The central half-turn pairs the eight octahedral matchings into four pairs.
eight=next(o for o in orbit_indices if len(o)==8)
eight_set={tuple(sorted(e for e in triples[j])) for j in eight}
def map_matching(p,m):
    return tuple(sorted(tuple(sorted((p[x],p[y]))) for x,y in m))
pair_set={frozenset((m,map_matching(z,m))) for m in eight_set}
assert len(pair_set)==4 and all(map_matching(z,m)!=m for m in eight_set)
pairs=sorted(pair_set,key=lambda t:tuple(sorted(t)))
action4={p:tuple(pairs.index(frozenset(map_matching(p,m) for m in a)) for a in pairs) for p in perms}
assert len(set(action4.values()))==24
assert {p for p in perms if action4[p]==(0,1,2,3)}=={I,z}
# A character valued in Z/2 gives an index-two complement not containing z.
phi={I:0};pending=[I]
while pending:
    h=pending.pop()
    for gen,bit in zip(generators,(1,0,1)):
        w=compose(h,gen);candidate=phi[h]^bit
        if w in phi:assert phi[w]==candidate
        else:phi[w]=candidate;pending.append(w)
assert len(phi)==48 and phi[z]==1
H=[p for p in perms if phi[p]==0]
assert len(H)==24
assert {p for p in H if action4[p]==(0,1,2,3)}=={I}
# Thus H -> S4 is an isomorphism and G=H x <z>.
standard=lambda p:sum(i==action4[p][i] for i in range(4))-1
assert all(chi[p]-1==standard(p) for p in H)
assert all(chi[p]-1==(-1)**phi[p]*standard(p) for p in perms)
print('GROUP_SPLIT_S4_C2_PASS','PAIR_PERMUTATION_IMAGE',len(set(action4.values())),'H_ORDER',len(H))
print('RATIONAL_MODULE_TRIVIAL_PLUS_STANDARD_TWIST_PASS')
print('INTEGRAL_ACTION_VERIFIED',len(actions),'GROUP_GENERATED',len(closure))
print('FRANKLIN_INDEPENDENCE_OCTAHEDRAL_CHARACTER_PASS')

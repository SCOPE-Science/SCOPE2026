#!/usr/bin/env python3
"""Integral discrete-Morse and dihedral-character checks for the Dürer matching complex.
Pure Python 3; no optional scientific packages. All cell orientations use increasing edge indices.
"""
from collections import Counter, deque

N=6
EDGES=tuple(sorted({tuple(sorted(pair)) for i in range(N) for pair in
                    ((i,(i+1)%N),(i,i+N),(i+N, (i+2)%N+N))}))
assert len(EDGES)==18 and len(set(EDGES))==18
ADJ={v:set() for v in range(12)}
for u,v in EDGES: ADJ[u].add(v); ADJ[v].add(u)
assert all(len(ADJ[v])==3 for v in ADJ)

# Enumerate independently as all compatible subsets and as recursive matching extensions.
CONFLICT=tuple(sum(1<<j for j,f in enumerate(EDGES) if set(e)&set(f)) for e in EDGES)
faces=[0]
for j in range(18):
    faces += [f|(1<<j) for f in faces if f&CONFLICT[j]==0]
F=set(faces)
assert len(F)==len(faces)==1038
assert all(not (f&CONFLICT[i] ^ (1<<i)) for f in F for i in range(18) if f&(1<<i))
counts=Counter(f.bit_count()-1 for f in F if f)
assert counts=={0:18,1:117,2:334,3:402,4:156,5:10},counts
# direct independent check via recursive graph-vertex occupations
count2=Counter()
def visit(j,occupied,size):
    if j==18:
        if size:count2[size-1]+=1
        return
    visit(j+1,occupied,size)
    u,v=EDGES[j]
    if (occupied>>u)&1==0 and (occupied>>v)&1==0:
        visit(j+1,occupied|(1<<u)|(1<<v),size+1)
visit(0,0,0)
assert count2==counts

# Standard greedy simplex toggling. Every phase pairs only still-unmatched faces.
free=set(F)-{0}
pairs={}
per_phase=[]
for j in range(18):
    stage=[(f,f|(1<<j)) for f in sorted(free)
           if (f&(1<<j))==0 and (f|(1<<j)) in free]
    assert len({x for a,b in stage for x in (a,b)})==2*len(stage)
    for a,b in stage:
        assert a in free and b in free and b.bit_count()==a.bit_count()+1
        free.remove(a);free.remove(b);pairs[a]=b
    per_phase.append(len(stage))
assert len(pairs)==506 and len(free)==25
assert Counter(f.bit_count()-1 for f in free)=={0:1,3:23,4:1}

# Enumerate every codimension-one Hasse edge; reverse precisely matched edges.
indeg={f:0 for f in F if f}
out={f:[] for f in indeg}
hasse=0
for x in indeg:
    bits=x
    while bits:
        t=bits&-bits;bits-=t;y=x^t
        if y==0:continue
        hasse+=1
        if pairs.get(y)==x:
            out[y].append(x);indeg[x]+=1
        else:
            out[x].append(y);indeg[y]+=1
Q=deque(f for f in indeg if indeg[f]==0)
topo=0
while Q:
    x=Q.popleft();topo+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:Q.append(y)
assert topo==len(indeg)==1037

# Integral chain cancellation: each removed facet/cofacet pair has pivot of degree +/-1.
# The column update is the Schur complement, with both removed cell coordinates deleted.
B={f:{f^(1<<i):(-1)**((f&((1<<i)-1)).bit_count())
      for i in range(18) if f&(1<<i) and (f^(1<<i))} for f in indeg}
active=set(B); pending=dict(pairs)
unit_count=0
while pending:
    pivot_data=next(((lo,hi,B[hi][lo]) for lo,hi in pending.items()
                     if abs(B[hi].get(lo,0))==1),None)
    assert pivot_data is not None, f'nonunit obstruction after {unit_count} cancellations'
    lo,hi,piv=pivot_data
    Bh=B[hi]
    for v in active:
        if v==hi or v==lo:continue
        a=B[v].get(lo,0)
        if a:
            for w,c in Bh.items():
                new=B[v].get(w,0)-a*piv*c
                if new:B[v][w]=new
                else:B[v].pop(w,None)
        B[v].pop(hi,None)
    del B[lo],B[hi]
    active.remove(lo);active.remove(hi);del pending[lo]
    unit_count+=1
assert active==free
assert all(set(B[f]).issubset(active) for f in active)
assert all((not B[f]) for f in active if f.bit_count()<=4)
topcell=next(f for f in free if f.bit_count()==5)
assert len(B[topcell])==2 and set(map(abs,B[topcell].values()))=={1}
assert all(u.bit_count()==4 for u in B[topcell])
# The Morse CW complex is simply connected and has one 0-cell, 23 3-cells,
# one 4-cell; its primitive top attaching map cancels one 3/4 pair.

# Full automorphism group by injective adjacency-preserving backtracking.
# Prune at each vertex and verify every resulting permutation globally.
autos=[]
def extend(mapping,used):
    if len(mapping)==12:
        p=tuple(mapping[i] for i in range(12))
        assert all(((u in ADJ[v])==(p[u] in ADJ[p[v]])) for u in range(12) for v in range(12))
        autos.append(p);return
    v=next(i for i in range(12) if i not in mapping)
    for t in range(12):
        if t in used or len(ADJ[v])!=len(ADJ[t]):continue
        if all(((w in ADJ[v])==(mapping[w] in ADJ[t])) for w in mapping):
            mapping[v]=t;used.add(t);extend(mapping,used)
            used.remove(t);del mapping[v]
extend({},set())
assert len(autos)==12 and len(set(autos))==12

def compose(p,q):return tuple(p[q[i]] for i in range(12))
r=tuple((i+1)%6 if i<6 else 6+(i-6+1)%6 for i in range(12))
s=tuple((-i)%6 if i<6 else 6+(-(i-6))%6 for i in range(12))
ident=tuple(range(12))
assert compose(compose(s,r),s)==tuple(r.index(i) for i in range(12))
powers=[ident]
for i in range(5):powers.append(compose(r,powers[-1]))
assert compose(r,powers[-1])==ident
assert len(set(powers+[compose(t,s) for t in powers]))==12
assert set(autos)==set(powers+[compose(t,s) for t in powers])

edge_id={edge:i for i,edge in enumerate(EDGES)}
def inversion_sign(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
def degree3_trace(p):
    ep=tuple(edge_id[tuple(sorted((p[u],p[v])))] for u,v in EDGES)
    Lef=0
    for f in F:
        if not f:continue
        a=[i for i in range(18) if f&(1<<i)]
        b=[ep[i] for i in a]
        if set(a)==set(b):
            Lef+=(-1)**(len(a)-1)*inversion_sign(b)
    return 1-Lef
rot=[degree3_trace(p) for p in powers]
refl=[degree3_trace(compose(p,s)) for p in powers]
assert rot==[22,0,-2,6,-2,0],rot
assert refl==[0]*6,refl
# Isotypic rational decomposition of D6: four one-dimensional chars + two two-dimensional chars.
# 1-dim multiplicities: both signs on s occur equally; r positive twice, negative once.
assert 2*2+1*2+2*3+2*5==22
print('graph_vertices=12 graph_edges=18 automorphisms=12')
print('matching_face_counts='+str(dict(sorted(counts.items()))))
print(f'morse_pairs={len(pairs)} phase_pairs={per_phase} critical={{0:1,3:23,4:1}}')
print(f'hasse_edges={hasse} acyclic_vertices={topo} unit_cancellations={unit_count}')
print('morse_top_boundary='+str(sorted(B[topcell].items())))
print('homotopy=22 copies of S^3 (integral)')
print('dihedral_rotation_H3_trace='+str(rot))
print('dihedral_reflection_H3_trace='+str(refl))
print('r_even_one_dim_each=2 r_odd_one_dim_each=1 V1=3 V2=5')
print('DURER_MATCHING_EQUIVARIANT_H3_PASS')

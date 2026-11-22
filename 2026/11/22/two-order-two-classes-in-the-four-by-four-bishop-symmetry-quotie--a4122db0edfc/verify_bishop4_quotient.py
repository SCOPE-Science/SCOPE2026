#!/usr/bin/env python3
"""Exact integral cellular computation for a square-board bishop orbit space.

Requires only Python 3 standard library. All cells, group elements and boundaries
are reconstructed from the coordinate definition; no saved certificate is trusted.
"""
from collections import Counter, defaultdict
from heapq import heappop, heappush

N=4
squares=[(r,c) for r in range(N) for c in range(N)]
attack=[]
for r,c in squares:
    attack.append(sum(1<<j for j,(u,v) in enumerate(squares)
                      if (u,v)!=(r,c) and abs(u-r)==abs(v-c)))

def enumerate_faces():
    out=[]
    def visit(face, available):
        if face:out.append(face)
        while available:
            bit=available & -available
            v=bit.bit_length()-1
            available-=bit
            visit(face | bit, available & ~attack[v])
    visit(0,(1<<(N*N))-1)
    return sorted(out,key=lambda x:(x.bit_count(),x))
# The two board colors have connected nonattacking-pair one-skeleta.
# Bishop attacks preserve color, so the full complex is their join;
# a join of two path-connected spaces is simply connected.
for parity in (0,1):
    vertices={i for i,(r,c) in enumerate(squares) if (r+c)%2==parity}
    assert len(vertices)==8
    reached={min(vertices)}
    while True:
        more={j for i in reached for j in vertices
              if j!=i and not ((attack[i]>>j)&1)}
        new=reached|more
        if new==reached:break
        reached=new
    assert reached==vertices, (parity,reached)
# The diagonal reflection fixes singleton (0,0); the horizontal
# reflection fixes the barycenter of {(0,0),(3,0)}, an allowed edge.
# Together these reflections generate the square dihedral group.
assert ((attack[0]>>12)&1)==0
faces=enumerate_faces()
assert len(faces)==728
assert [sum(f.bit_count()==k for f in faces) for k in range(1,7)]==[16,92,232,260,112,16]
face_set=set(faces)

# All eight distinct rigid symmetries of the square.
perms=[]
for turn in range(4):
    for mirror in (False,True):
        trans=[]
        for r,c in squares:
            if mirror:c=N-1-c
            for _ in range(turn):r,c=c,N-1-r
            trans.append(squares.index((r,c)))
        perms.append(tuple(trans))
assert len(set(perms))==8
for perm in perms:
    for i in range(16):
        for j in range(16):
            assert bool((attack[i]>>j)&1)==bool((attack[perm[i]]>>perm[j])&1)
# precompute group maps for all simplices (no unverified action on faces)
images=[{face:sum(1<<p[i] for i in range(16) if (face>>i)&1)
         for face in faces} for p in perms]
assert all(set(M.values())==face_set for M in images)
def canon(flag):return min(tuple(M[s] for s in flag) for M in images)

# Every nonempty chain of distinct nested simplices represents a simplex
# in the barycentric subdivision. Group orbits give quotient simplices.
ends={}
orbits=defaultdict(set)
flag_total=0
for top in faces:
    chains=[(top,)]
    sub=(top-1)&top
    while sub:
        chains.extend(chain+(top,) for chain in ends[sub])
        sub=(sub-1)&top
    ends[top]=chains
    flag_total+=len(chains)
    for flag in chains:orbits[len(flag)-1].add(canon(flag))
assert flag_total==158328
fvec=tuple(len(orbits[k]) for k in range(6))
assert fvec==(100,1210,4530,7260,5280,1440),fvec
# Independent Burnside count: for each group element, count invariant
# nested simplex chains by dynamic recurrence over its invariant faces.
fixed_by_dim=[Counter() for _ in range(8)]
for g,M in enumerate(images):
    ends_counts={}
    for top in faces:
        if M[top]!=top:continue
        ct=Counter({1:1})
        sub=(top-1)&top
        while sub:
            if sub in ends_counts:
                for k,n in ends_counts[sub].items():ct[k+1]+=n
            sub=(sub-1)&top
        ends_counts[top]=ct
        fixed_by_dim[g].update(ct)
assert tuple(sum(C[k+1] for C in fixed_by_dim)//8 for k in range(6))==fvec
assert all(sum(C[k+1] for C in fixed_by_dim)%8==0 for k in range(6))

cells=[flag for k in range(6) for flag in sorted(orbits[k])]
index={flag:i for i,flag in enumerate(cells)}
assert len(index)==19820
facets=[[] for _ in cells]
cofaces=[[] for _ in cells]
for u,flag in enumerate(cells):
    if len(flag)==1:continue
    for j in range(len(flag)):
        v=index[canon(flag[:j]+flag[j+1:])]
        assert len(cells[v])+1==len(flag)
        assert v not in facets[u]
        facets[u].append(v)
        cofaces[v].append(u)
# Face lattice of quotient is a regular cell complex: a group element
# stabilizing a strict flag fixes each differently ranked face, hence
# fixes the barycentric simplex pointwise. All its facets are distinct.
assert sum((-1)**k * fvec[k] for k in range(6))==0

# Genuine elementary collapses in the quotient, not chain-level Morse
# reductions. Each upper cell is maximal and its facet is in precisely
# one active upper cell. This yields an explicit strong deformation retract.
active=[True]*len(cells)
upper_count=[len(x) for x in cofaces]
queue=[]
collapses=[]
def potential(u):
    if not active[u] or upper_count[u]:return
    for v in facets[u]:
        if active[v] and upper_count[v]==1:
            heappush(queue,(-(len(cells[u])-1),u,v))
for u in range(len(cells)):potential(u)
while queue:
    _,u,v=heappop(queue)
    if not(active[u] and active[v]) or upper_count[u]!=0 or upper_count[v]!=1:continue
    assert len(cells[u])==len(cells[v])+1 and v in facets[u]
    assert [w for w in cofaces[v] if active[w]]==[u]
    active[u]=active[v]=False
    collapses.append((u,v))
    for z in (u,v):
        for f in facets[z]:
            if active[f]:
                upper_count[f]-=1
                assert upper_count[f]>=0
                if upper_count[f]==1:
                    for t in cofaces[f]:potential(t)
                elif upper_count[f]==0:potential(f)
assert len(collapses)==9064,len(collapses)
remvec=tuple(sum(active[u] and len(flag)==k+1 for u,flag in enumerate(cells)) for k in range(6))
assert remvec==(60,419,786,427,0,0),remvec
assert all(not active[u] or all(active[v] for v in facets[u]) for u in range(len(cells)))

C={k:set(u for u,flag in enumerate(cells) if active[u] and len(flag)==k+1) for k in range(4)}
D={k:{} for k in (1,2,3)}
for u in C[1]|C[2]|C[3]:
    D[len(cells[u])-1][u]={v:(-1 if j%2 else 1)
                            for j,v in enumerate(facets[u])}

def verify_chain():
    for k in (1,2):
        for u,col in D[k+1].items():
            comp=Counter()
            for v,b in col.items():
                for w,a in D[k][v].items():comp[w]+=a*b
            assert all(a==0 for a in comp.values()),(k,u,comp)
verify_chain()

def mod_rank(cols,p):
    basis={}
    for vec in cols.values():
        x={r:v%p for r,v in vec.items() if v%p}
        while x:
            r=min(x)
            if r not in basis:
                inv=pow(x[r],-1,p)
                basis[r]={t:(z*inv)%p for t,z in x.items()}
                break
            factor=x[r]
            for t,z in basis[r].items():
                a=(x.get(t,0)-factor*z)%p
                if a:x[t]=a
                else:x.pop(t,None)
    return len(basis)

# Independent field-rank checks on the cell structure after topological
# collapses, before any integral pivot transformation.
field_ranks={p:tuple(mod_rank(D[k],p) for k in (1,2,3)) for p in (2,3,5)}
assert field_ranks=={2:(59,360,424),3:(59,360,426),5:(59,360,426)},field_ranks

# Integral unimodular chain cancellation. For a unit coefficient a in
# the row v and column u of d_k, use a unimodular basis transformation:
#   d_k(w) <- d_k(w) - [d_k(w)]_v/a * d_k(u),  w != u;
# then delete basis cells u and v. Chain identity d_{k-1}d_k=0 implies
# the induced restrictions on neighbouring differentials are exact.
unit_pivots=Counter()
for k in (1,2,3):
    incid=defaultdict(set)
    for u,col in D[k].items():
        for v,a in col.items():incid[v].add(u)
    while True:
        best=None
        for u,col in D[k].items():
            for v,a in col.items():
                if abs(a)!=1:continue
                cost=(len(col)-1)*(len(incid[v])-1)
                if best is None or cost<best[0]:best=(cost,u,v,a)
                if cost==0:break
            if best is not None and best[0]==0:break
        if best is None:break
        _,u,v,a=best
        old=D[k][u]
        for w in list(incid[v]):
            if w==u:continue
            col=D[k][w]
            b=col[v]//a
            for r,t in old.items():
                z=col.get(r,0)-b*t
                if z:col[r]=z;incid[r].add(w)
                else:
                    col.pop(r,None);incid[r].discard(w)
        for r in old:incid[r].discard(u)
        del D[k][u]
        C[k].remove(u);C[k-1].remove(v)
        if k>1:del D[k-1][v]
        if k<3:
            for col in D[k+1].values():col.pop(u,None)
        unit_pivots[k]+=1
    verify_chain()
assert unit_pivots=={1:59,2:360,3:424},unit_pivots
assert tuple(len(C[k]) for k in range(4))==(1,0,2,3)
assert all(not col for col in D[2].values())
nonzero=[col for col in D[3].values() if col]
assert len(nonzero)==2
single=next(col for col in nonzero if len(col)==1 and abs(next(iter(col.values())))==2)
other=next(col for col in nonzero if col is not single)
r,a=next(iter(single.items()))
assert r in other and other[r]%a==0
mult=other[r]//a
reduced={v:z-mult*single.get(v,0) for v,z in other.items()}
reduced={v:z for v,z in reduced.items() if z}
assert len(reduced)==1 and abs(next(iter(reduced.values())))==2, (single,other,reduced)
assert next(iter(reduced))!=r
# Thus the residual integral chain complex is diag(2,2,0) in d_3,
# no d_1 or d_2. The operations preserve integral homology.
print('BISHOP4_D4_INTEGRAL_QUOTIENT_OK')
print('simplex_face_counts=(16,92,232,260,112,16)')
print('nonempty_flags=',flag_total,'quotient_f_vector=',fvec)
print('topological_elementary_collapses=',len(collapses),'remaining=',remvec)
print('field_boundary_ranks=',field_ranks)
print('integer_unit_pivots=',dict(unit_pivots))
print('residual_d3=diag(2,2,0); H_2=(Z/2)^2, H_3=Z')

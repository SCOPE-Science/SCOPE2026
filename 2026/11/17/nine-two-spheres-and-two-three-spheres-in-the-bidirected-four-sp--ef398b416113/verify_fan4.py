"""Exact simplicial and equivariant check for the bidirected four-spoke fan.
The undirected graph is K_1 join P_4, with hub vertex 4. A face is an
arc set whose selected arrows form disjoint directed simple paths.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache

EDGES = sorted({tuple(sorted(p)) for p in ([(i,i+1) for i in range(3)] + [(i,4) for i in range(4)])})
ARCS = [a for u,v in EDGES for a in ((u,v),(v,u))]
N=len(ARCS)
assert N==14

def is_multipath(mask):
    successor={};predecessor={}
    for i,(u,v) in enumerate(ARCS):
        if mask & (1<<i):
            if u in successor or v in predecessor:return False
            successor[u]=v;predecessor[v]=u
    for s in successor:
        path=set();v=s
        while v in successor:
            if v in path:return False
            path.add(v);v=successor[v]
    return True

ALL = [s for s in range(1<<N) if is_multipath(s)]
FACES=set(ALL)-{0}
assert len(FACES)==160,(len(FACES))
assert Counter(s.bit_count()-1 for s in FACES)=={0:14,1:56,2:70,3:20}
for s in FACES:
    for i in range(N):
        if (s>>i)&1:assert (s^(1<<i)) in ALL

def staged_match(order):
    R=FACES.copy();lower={};upper={}
    for j in order:
        for low in sorted(R):
            if low&(1<<j):continue
            high=low|(1<<j)
            if high in R:
                R.remove(low);R.remove(high)
                lower[low]=high;upper[high]=low
    return R,lower,upper

# Published finite certificate: successive elementary face-poset toggles.
ORDER = [13, 6, 10, 0, 8, 4, 3, 11, 1, 9, 2, 5, 7, 12]
assert sorted(ORDER)==list(range(N))
CRITICAL,LOWER,UPPER=staged_match(ORDER)
assert len(LOWER)==74 and len(CRITICAL)==12
assert Counter(s.bit_count()-1 for s in CRITICAL)=={0:1,2:9,3:2}

# Full directed face-incidence graph, orient upwards on matched pairs.
indegree={s:0 for s in FACES};outgoing=defaultdict(list);incidences=0
for upper in FACES:
    for j in range(N):
        if not upper&(1<<j):continue
        lower=upper^(1<<j)
        if lower==0:continue
        a,b=((lower,upper) if LOWER.get(lower)==upper else (upper,lower))
        outgoing[a].append(b);indegree[b]+=1;incidences+=1
q=deque(s for s,d in indegree.items() if d==0);visited=0
while q:
    a=q.popleft();visited+=1
    for b in outgoing[a]:
        indegree[b]-=1
        if indegree[b]==0:q.append(b)
assert visited==len(FACES), 'The proposed matching is not acyclic'

def incidence(face, bit):
    return -1 if ((face&((1<<bit)-1)).bit_count()%2) else 1

@lru_cache(None)
def project(face):
    if face in UPPER:return {}
    if face not in LOWER:return {face:1}
    above=LOWER[face]
    added=(above^face).bit_length()-1
    coeff=incidence(above,added)
    v=defaultdict(int)
    for bit in range(N):
        if not above&(1<<bit) or bit==added:continue
        neighbor=above^(1<<bit)
        for c,weight in project(neighbor).items():
            v[c]-=coeff*incidence(above,bit)*weight
    return {c:w for c,w in v.items() if w}

def reduced_boundary(s):
    v=defaultdict(int)
    for i in range(N):
        if not s&(1<<i):continue
        for c,w in project(s^(1<<i)).items():
            v[c]+=incidence(s,i)*w
    return {c:w for c,w in v.items() if w}
assert all(reduced_boundary(s)=={} for s in CRITICAL if s.bit_count()==4)
assert all(reduced_boundary(s)=={} for s in CRITICAL if s.bit_count()==3)

# Independent unsigned mod-two boundary-rank cross-check.
def binary_rank(columns):
    pivots={}
    for col in columns:
        while col:
            k=col.bit_length()-1
            if k in pivots:col^=pivots[k]
            else:
                pivots[k]=col
                break
    return len(pivots)

all_dims={d:sorted(s for s in FACES if s.bit_count()==d+1) for d in range(4)}
MOD2_RANKS={}
for d in range(1,4):
    target_index={s:i for i,s in enumerate(all_dims[d-1])}
    cols=[]
    for f in all_dims[d]:
        col=0
        for j in range(N):
            if f&(1<<j):col^=1<<target_index[f^(1<<j)]
        cols.append(col)
    MOD2_RANKS[d]=binary_rank(cols)
assert MOD2_RANKS=={1:13,2:43,3:18},MOD2_RANKS

# Independent integral homology sanity check by exact rational rank.
TRI=sorted(s for s in FACES if s.bit_count()==3)
TET=sorted(s for s in FACES if s.bit_count()==4)
index_tri={s:j for j,s in enumerate(TRI)}
index_tet={s:j for j,s in enumerate(TET)}
A=[[Fraction(0) for _ in TET] for _ in TRI]
for col,tetra in enumerate(TET):
    for j in range(N):
        if tetra&(1<<j):A[index_tri[tetra^(1<<j)]][col]=Fraction(incidence(tetra,j))
B=[x[:] for x in A]; piv=[];rank=0
for col in range(len(TET)):
    k=next((z for z in range(rank,len(TRI)) if B[z][col]),None)
    if k is None:continue
    B[rank],B[k]=B[k],B[rank]
    lead=B[rank][col];B[rank]=[v/lead for v in B[rank]]
    for z in range(len(TRI)):
        if z==rank or B[z][col]==0:continue
        f=B[z][col];B[z]=[x-f*y for x,y in zip(B[z],B[rank])]
    piv.append(col);rank+=1
free=[j for j in range(len(TET)) if j not in piv]
assert rank==18 and len(free)==2,(rank,free)
kernel=[]
for f in free:
    vector=[Fraction(0)]*len(TET);vector[f]=1
    for k,c in enumerate(piv):vector[c]=-B[k][f]
    assert all(sum(x*y for x,y in zip(row,vector))==0 for row in A)
    kernel.append(vector)

arci={a:i for i,a in enumerate(ARCS)}
def moved_face(mask,g):
    moved=[arci[(g[ARCS[j][0]],g[ARCS[j][1]])] for j in range(N) if mask&(1<<j)]
    odd=sum(moved[i]>moved[j] for i in range(len(moved)) for j in range(i+1,len(moved)))%2
    return sum(1<<j for j in moved),(-1 if odd else 1)

def trace_chain(g,dim):
    return sum(sign for f in FACES if f.bit_count()==dim+1
        for image,sign in [moved_face(f,g)] if image==f)

CHARS={}
for name,g in [('identity',{i:i for i in range(5)}),('reflection',{**{i:3-i for i in range(4)},4:4})]:
    tr3=Fraction(0)
    for idx_f,f in enumerate(free):
        vec=kernel[idx_f]
        for i,c in enumerate(vec):
            if c:
                target,sgn=moved_face(TET[i],g)
                if index_tet[target]==f:tr3+=sgn*c
    lefschetz=sum((-1)**d*trace_chain(g,d) for d in range(4))-1
    tr2=lefschetz+tr3
    assert tr2.denominator==1 and tr3.denominator==1
    CHARS[name]=(int(tr2),int(tr3))
assert CHARS['identity']==(9,2)
assert all((a+b)%2==0 for a,b in zip(*CHARS.values()))

print('FAN4_EXACT_HOMOTOPY_AND_REFLECTION_OK')
print('undirected_edges=',EDGES)
print('arcs=',ARCS)
print('all_faces=',len(FACES),'f_vector=',dict(sorted(Counter(s.bit_count()-1 for s in FACES).items())))
print('matching_toggle_order=',ORDER)
print('matching_pairs=',len(LOWER),'critical_by_dimension=',dict(sorted(Counter(s.bit_count()-1 for s in CRITICAL).items())))
print('hasse_incidences=',incidences,'visited=',visited)
print('morse_3_to_2_boundary=zero; sphere_wedge=S2^9+S3^2')
print('mod2_boundary_ranks=',MOD2_RANKS)
print('top_boundary_rank=',rank,'top_kernel_rank=',len(kernel))
print('reflection_characters_H2_H3=',CHARS)
print('reflection_plus_minus_H2=',((9+CHARS['reflection'][0])//2,(9-CHARS['reflection'][0])//2))
print('reflection_plus_minus_H3=',((2+CHARS['reflection'][1])//2,(2-CHARS['reflection'][1])//2))

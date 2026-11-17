#!/usr/bin/env python3
"""Exhaustive integer-face and signed Lefschetz verifier for an icosahedral graph complex.
Python 3.9+; no third-party packages are needed.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 12
EDGES = (
 (0,1),(0,5),(0,7),(0,8),(0,11),
 (1,2),(1,5),(1,6),(1,8),
 (2,3),(2,6),(2,8),(2,9),
 (3,4),(3,6),(3,9),(3,10),
 (4,5),(4,6),(4,10),(4,11),
 (5,6),(5,11), (7,8),(7,9),(7,10),(7,11),
 (8,9),(9,10),(10,11)
)
FULL=(1<<N)-1
ADJ=[0]*N
for u,v in EDGES:
    assert 0<=u<v<N and not (ADJ[u]>>v&1)
    ADJ[u] |= 1<<v; ADJ[v] |= 1<<u
assert len(EDGES)==30 and all(a.bit_count()==5 for a in ADJ)

def forest_union(s):
    par=list(range(N))
    def root(x):
        while par[x]!=x:
            x=par[x]
        return x
    for u,v in EDGES:
        if s>>u&1 and s>>v&1:
            a,b=root(u),root(v)
            if a==b:return False
            par[a]=b
    return True

def forest_euler(s):
    unseen=s
    nc=0
    while unseen:
        start=unseen&-unseen; unseen ^= start; todo=start; nc+=1
        while todo:
            x=todo&-todo; todo ^= x
            v=x.bit_length()-1
            new=ADJ[v]&unseen
            unseen ^= new; todo |= new
    e=sum((ADJ[v]&s).bit_count() for v in range(N) if s>>v&1)//2
    return e==s.bit_count()-nc

F=set()
for s in range(1<<N):
    assert forest_union(s)==forest_euler(s), f'face disagreement {s}'
    if forest_union(s):F.add(s)
counts=Counter(s.bit_count()-1 for s in F)
assert len(F)==984 and [counts[d] for d in range(-1,6)]==[1,12,66,200,345,300,60]
print('GRAPH: 12 vertices, 30 edges; degree 5; 20 triangles')
assert sum(all((ADJ[a]>>b)&1 for a,b in combinations(x,2)) for x in combinations(range(N),3))==20
print('FOREST_FACES: 984 including empty; dimension counts', dict(sorted(counts.items())))
facets=[s for s in F if all(s|(1<<i) not in F for i in range(N) if not (s>>i)&1)]
facets_by_dimension=Counter(s.bit_count()-1 for s in facets)
assert facets_by_dimension==Counter({4:60,5:60})
print('FACETS: 60 of dimension 4, 60 of dimension 5')

# Matching on NONEMPTY faces, ordered-pivot toggling. The pairs are recomputed
# among still-unmatched cells at each pivot (0,...,11).
unmatched=F-{0};pairs=[]
for v in range(N):
    bit=1<<v
    stage=[(s,s|bit) for s in sorted(unmatched) if not s&bit and s|bit in unmatched]
    for a,b in stage:
        assert a in unmatched and b in unmatched and (a^b)==bit
        unmatched.remove(a);unmatched.remove(b)
    pairs.extend(stage)
crit=Counter(s.bit_count()-1 for s in unmatched)
assert len(pairs)==471 and crit==Counter({0:1,4:40}),crit
print('MATCHING: pairs 471, critical faces 41, critical dimensions',dict(crit))
print('CRITICAL_VERTEX:', [s.bit_length()-1 for s in unmatched if s.bit_count()==1])
print('CRITICAL_4_CELLS:',sorted(s for s in unmatched if s.bit_count()==5))
# All (d-1)-to-d relations between nonempty faces are oriented high->low
# unless in matching, when low->high. Acyclicity of this entire digraph,
# rather than just gradient paths, is checked by topological sort.
matched=set(pairs)
succ=defaultdict(list); indeg={s:0 for s in F if s!=0}; incidence=0
for high in sorted(F-{0}):
    if high.bit_count()<2:continue
    for i in range(N):
        if high>>i&1:
            low=high^(1<<i)
            if (low,high) in matched:
                src,dst=low,high
            else:
                src,dst=high,low
            succ[src].append(dst); indeg[dst]+=1;incidence+=1
queue=deque(k for k,d in indeg.items() if d==0)
removed=0
while queue:
    a=queue.popleft();removed+=1
    for b in succ[a]:
        indeg[b]-=1
        if not indeg[b]:queue.append(b)
assert removed==len(F)-1, ('cycle in matching',removed,len(F)-1)
print('ACYCLIC: all',incidence,'nonempty face-poset cover relations,',removed,'vertices ordered')

# The independent mod-2 simplicial boundary calculation is used as a
# secondary check, not as a substitute for integral Forman theory.
def rank_f2(column_masks):
    piv={}
    for x in column_masks:
        while x:
            k=x.bit_length()-1
            if k in piv:x^=piv[k]
            else:piv[k]=x;break
    return len(piv)
faces_by_k={k:sorted(s for s in F if s.bit_count()==k) for k in range(1,7)}
ranks={0:0}
for k in range(2,7):
    low={s:j for j,s in enumerate(faces_by_k[k-1])}
    columns=[]
    for s in faces_by_k[k]:
        col=0
        for i in range(N):
            if s>>i&1:col^=1<<low[s^(1<<i)]
        columns.append(col)
    ranks[k-1]=rank_f2(columns)
ranks[6]=0
betti={k-1:len(faces_by_k[k])-ranks[k-1]-ranks[k] for k in range(1,7)}
assert betti=={0:1,1:0,2:0,3:0,4:40,5:0},betti
print('MOD2_CHAIN: boundary ranks',ranks,'ordinary Betti numbers',betti)

# Enumerate automorphisms by incremental adjacency constraints.
# Picking the unmapped vertex with the most already-mapped neighbors
# prunes immediately; this is independent of any installed graph package.
ALL=[]
def enumerate_auto(partial,available):
    if len(partial)==N:
        p=tuple(partial[v] for v in range(N))
        assert all((ADJ[p[u]]>>p[v])&1 for u,v in EDGES)
        ALL.append(p);return
    remaining=[v for v in range(N) if v not in partial]
    u=max(remaining,key=lambda v:((ADJ[v]&sum(1<<w for w in partial)).bit_count(),-v))
    for w in range(N):
        if not available>>w&1:continue
        if all(bool(ADJ[u]>>v&1)==bool(ADJ[w]>>wv&1) for v,wv in partial.items()):
            partial[u]=w
            enumerate_auto(partial,available^(1<<w))
            del partial[u]
enumerate_auto({},FULL)
assert len(ALL)==120 and len(set(ALL))==120
I=tuple(range(N));P=set(ALL)
def compose(p,q):return tuple(p[q[i]] for i in range(N))
def inverse(p):return tuple(p.index(i) for i in range(N))
assert I in P and all(inverse(p) in P for p in P)
assert all(compose(p,q) in P for p in P for q in P)

def sign(images):
    return -1 if sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))%2 else 1

def signed_trace(p):
    z=-1 # empty simplex in augmented/reduced Lefschetz number
    for s in F-{0}:
        verts=[i for i in range(N) if s>>i&1]
        images=[p[i] for i in verts]
        if sum(1<<j for j in images)==s:
            z+=((-1)**(len(verts)-1))*sign(images)
    return z
def trace_via_orbits(p):
    cycles=[];unused=set(range(N))
    while unused:
        i=min(unused);v=i;cyc=0
        while v in unused:
            unused.remove(v);cyc|=1<<v;v=p[v]
        assert v==i
        cycles.append(cyc)
    val=0
    for bits in range(1<<len(cycles)):
        union=0
        for j,c in enumerate(cycles):
            if bits>>j&1:union|=c
        if union in F:val+=(-1)**bits.bit_count()
    return -val
T={p:signed_trace(p) for p in ALL}
assert all(T[p]==trace_via_orbits(p) for p in ALL)
print('CHARACTER_SECOND_METHOD: all 120 signed traces agree with orbit-subset formula')
assert T[I]==40
summary=Counter(T.values())
assert summary==Counter({0:48,-1:20,1:20,2:15,-4:15,40:1,-10:1}),summary
assert sum(T.values())==0 and sum(z*z for z in T.values())==120*17
central=[p for p in ALL if all(compose(p,q)==compose(q,p) for q in ALL)]
assert len(central)==2
c=next(p for p in central if p!=I)
assert T[c]==-10
# Commutator subgroup generated by all [p,q] is order-60 rotational A5.
comm={compose(compose(compose(p,q),inverse(p)),inverse(q)) for p in ALL for q in ALL}
assert len(comm)==60 and I in comm
assert all(compose(p,q) in comm for p in comm for q in comm)
assert c not in comm

def order(p):
    power=I
    for o in range(1,121):
        power=compose(power,p)
        if power==I:return o
    raise AssertionError('order >120')
rot_summary=Counter((order(p),T[p]) for p in comm)
assert rot_summary==Counter({(1,40):1,(2,-4):15,(3,1):20,(5,0):24}),rot_summary
for p in comm:
    o=order(p)
    assert T[compose(c,p)]=={1:-10,2:2,3:-1,5:0}[o]
    plus=(T[p]+T[compose(c,p)])//2
    minus=(T[p]-T[compose(c,p)])//2
    assert (plus,minus)=={1:(15,25),2:(-1,-3),3:(0,1),5:(0,0)}[o]
classes=[];remaining=set(P)
while remaining:
    p=min(remaining)
    cls={compose(compose(q,p),inverse(q)) for q in P}
    assert cls<=remaining
    remaining-=cls
    classes.append((order(p),len(cls),'rotation' if p in comm else 'inversion*rotation',T[p]))
assert len(classes)==10
print('AUTOMORPHISMS: 120; center order 2; derived rotation subgroup order 60')
print('CONJUGACY_CLASSES:',sorted(classes))
print('CHARACTER_TRACES:',dict(sorted(summary.items())))
print('AVERAGE_TRACE: 0; CHARACTER_INNER_PRODUCT: 17')
print('A5xC2_IRRED_SPLIT: plus (3)+(3prime)+(4)+(5); minus 2*(3)+2*(3prime)+2*(4)+(5)')
print('ICOSAHEDRAL_FOREST_FULL_CERTIFICATE_PASS')

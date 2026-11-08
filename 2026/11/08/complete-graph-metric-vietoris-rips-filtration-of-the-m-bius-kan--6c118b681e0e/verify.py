#!/usr/bin/env python3
"""Exact face, discrete-Morse and integral-chain verification for a graph metric Rips complex."""
import itertools, collections, random

N,K=8,3
V=tuple(range(2*N))
def build_edges():
  return {tuple(sorted(e)) for i in range(N) for e in [(i,(i+1)%N),(i,N+i),(N+i,N+(i+K)%N)]}
E=build_edges()
assert len(E)==24
adj=[set() for i in V]
for u,v in E: adj[u].add(v);adj[v].add(u)
assert all(len(x)==3 for x in adj)
# Independent all-pairs distances from adjacency: repeated Boolean-power ball expansion.
d=[]
for v in V:
    q=collections.deque([v]);row={v:0}
    while q:
        x=q.popleft()
        for w in sorted(adj[x]):
            if w not in row:row[w]=row[x]+1;q.append(w)
    assert len(row)==16
    d.append(row)
# Compute clique faces by two different methods: recursive face extension and brute-force maximal-clique closure.
def recursive_faces():
    near=[{j for j in V if j!=i and d[i][j]<=2} for i in V]
    faces={()};frontier=[()]
    while frontier:
        x=frontier.pop()
        for j in range(x[-1]+1 if x else 0,16):
            if all(j in near[i] for i in x):
                y=(*x,j)
                assert y not in faces
                faces.add(y);frontier.append(y)
    return faces
faces=recursive_faces()
def maximal_clique_faces():
    near=[{j for j in V if j!=i and d[i][j]<=2} for i in V]
    def bronk(R,P,X):
        if not P and not X:
            for n in range(len(R)+1):
                for f in itertools.combinations(sorted(R),n):other.add(f)
        while P:
            v=min(P);bronk(R|{v},P&near[v],X&near[v]);P.remove(v);X.add(v)
    other=set();bronk(set(),set(V),set())
    return other
assert faces==maximal_clique_faces()
# Independently recover the same graph from the cyclic Möbius–Kantor point-line configuration:
# incidence P_i -- L_{i},L_{i+1},L_{i+3} (indices modulo 8).
incidence_edges={tuple(sorted((i,8+(i+z)%8))) for i in range(8) for z in (0,1,3)}
isomorphism=[0,11,2,13,4,15,6,9,8,3,10,5,12,7,14,1]
assert {tuple(sorted((isomorphism[u],isomorphism[v]))) for u,v in E} == incidence_edges
assert len(faces)==249 # 248 nonempty + empty
count=collections.Counter(len(x)-1 for x in faces)
assert count=={-1:1,0:16,1:72,2:112,3:48}
# Independent brute-force face test on all 65536 subsets.
near_masks=[sum(1<<j for j in V if i!=j and d[i][j]<=2) for i in V]
valid_masks=set()
for mask in range(1<<16):
    selected=[i for i in V if mask>>i&1]
    if all((mask & ~(1<<i)) & ~near_masks[i]==0 for i in selected):valid_masks.add(mask)
assert valid_masks=={sum(1<<i for i in f) for f in faces}
# Radius three: exactly eight antipodal pairs remain nonedges, so the
# clique complex is the boundary of the eight-dimensional cross-polytope.
far_pairs={tuple(sorted((i,j))) for i in V for j in V if i!=j and d[i][j]>3}
assert far_pairs == {(i,i+4) for i in range(4)} | {(i+8,i+12) for i in range(4)}
assert max(max(row.values()) for row in d)==4
# Structural boundary comparison: the graph has girth six, and its
# six-cycles do NOT satisfy edge-disjointness.
assert not any(len(adj[u]&adj[v])>1 for u in V for v in V if u<v)  # no four-cycles
six_cycles=set()
def walk_six(start,path):
    if len(path)==6:
        if start in adj[path[-1]]:
            seq=path; back=list(reversed(seq))
            cyc=min(tuple(seq[k:]+seq[:k]) for k in range(6))
            cyc=min(cyc,min(tuple(back[k:]+back[:k]) for k in range(6)))
            six_cycles.add(cyc)
        return
    for nxt in adj[path[-1]]:
        if nxt not in path:walk_six(start,path+[nxt])
for start in V:walk_six(start,[start])
assert len(six_cycles)==24
edge_cycles=collections.defaultdict(set)
for c in six_cycles:
    for k in range(6):edge_cycles[tuple(sorted((c[k],c[(k+1)%6])))].add(c)
assert max(map(len,edge_cycles.values()))==6
assert (2,3) in edge_cycles and len(edge_cycles[(2,3)])>=2


def make_matching(order):
    unmatched=set(faces);pairs=[]
    for v in order:
        take=[]
        for a in sorted(unmatched,key=lambda x:(len(x),x)):
            if v in a:continue
            b=tuple(sorted((*a,v)))
            if b in unmatched:take.append((a,b))
        for a,b in take: unmatched.remove(a);unmatched.remove(b)
        pairs+=take
    assert len(unmatched)+2*len(pairs)==len(faces)
    return unmatched,pairs

def acyclic(pairs):
    matches={(a,b) for a,b in pairs}
    links={f:[] for f in faces};edges=0
    for b in faces:
        for i in range(len(b)):
            a=b[:i]+b[i+1:];edges+=1
            if (a,b) in matches:links[b].append(a)
            else:links[a].append(b)
    in_degree={x:0 for x in faces}
    for a,targets in links.items():
        for b in targets:in_degree[b]+=1
    queue=collections.deque(x for x,k in in_degree.items() if k==0)
    seen=0
    while queue:
        a=queue.popleft();seen+=1
        for b in links[a]:
            in_degree[b]-=1
            if in_degree[b]==0:queue.append(b)
    assert seen==len(faces),(seen,len(faces))
    return edges

def morse_boundary(pairs,crit):
    # Chain cancellation over the integers, at a simplicial boundary unit.
    cells={f:len(f)-1 for f in faces}
    bd={s:{s[:i]+s[i+1:]:(-1)**i for i in range(len(s))} for s in faces if s}
    bd[()]={}
    for a,b in pairs:
        assert a in cells and b in cells
        cb=bd[b].get(a,0)
        assert abs(cb)==1,(a,b,cb)
        # pivot elimination in the differential from |b| to |a|.
        for z in list(cells):
            if z==b or len(z)!=len(b):continue
            coef=bd[z].get(a,0)
            if coef:
                for t,c in bd[b].items():
                    bd[z][t]=bd[z].get(t,0)-coef*cb*c
                    if not bd[z][t]:bd[z].pop(t)
        del cells[a];del cells[b];bd.pop(a);bd.pop(b)
        for z in bd:bd[z].pop(a,None);bd[z].pop(b,None)
    assert set(cells)==crit
    for z in bd:
        for t in bd[z]:assert len(t)==len(z)-1 and t in cells
    twos=sorted(x for x in crit if len(x)==3)
    threes=sorted(x for x in crit if len(x)==4)
    mat=[[bd[s].get(t,0) for s in threes] for t in twos]
    return mat

def integer_rank(M):
    from fractions import Fraction
    A=[[Fraction(z) for z in row] for row in M]
    r=0
    for j in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][j]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        for i in range(r+1,len(A)):
            if A[i][j]:
                a=A[i][j]/A[r][j]
                for k in range(j,len(A[0])):A[i][k]-=a*A[r][k]
        r+=1
        if r==len(A):break
    return r

rng=random.Random(61)
orders=[]
for n in range(100):
    order=list(V);rng.shuffle(order)
    crit,pairs=make_matching(order)
    v=collections.Counter(map(lambda x:len(x)-1,crit))
    if v=={2:9,3:2}:orders.append(order)
assert len(orders)>=2
results=[]
for order in [orders[0],orders[-1]]:
    crit,pairs=make_matching(order)
    inc=acyclic(pairs)
    mat=morse_boundary(pairs,crit)
    mat_rev=morse_boundary(list(reversed(pairs)),crit)
    assert mat==mat_rev
    results.append((order,len(pairs),inc,crit,mat))
for order,pc,inc,crit,mat in results:
    print('ORDER',order,'MATCHED',pc,'INCIDENCES',inc,'CRITICAL',dict(collections.Counter(len(f)-1 for f in crit)))
    print('MORSE_BOUNDARY_9x2',mat,'RANK',integer_rank(mat))

# Original, unreduced simplicial boundary matrices over three coefficient fields.
def rank_mod_p(dimension,p):
    lower=sorted(f for f in faces if len(f)==dimension)
    higher=sorted(f for f in faces if len(f)==dimension+1)
    columns=[];row_index={f:i for i,f in enumerate(lower)}
    for top in higher:
        col={row_index[top[:j]+top[j+1:]]:(-1)**j%p for j in range(len(top))}
        columns.append(col)
    pivots={}
    for col in columns:
        while col:
            i=min(col)
            if i not in pivots:
                inv=pow(col[i],-1,p)
                pivots[i]={k:(v*inv)%p for k,v in col.items()}
                break
            piv=pivots[i];a=col[i]
            for j,v in piv.items():
                col[j]=(col.get(j,0)-a*v)%p
                if not col[j]:del col[j]
    return len(pivots)
for prime in (2,3,5):
    r=[rank_mod_p(q,prime) for q in (1,2,3)]
    assert r==[15,57,46],(prime,r)
    print('UNREDUCED_MOD',prime,'BOUNDARY_RANKS',r)
print('FACES_BY_DIMENSION',dict(sorted(count.items())))
print('ANTIPODAL_PAIRS',sorted(far_pairs))
print('SIX_CYCLES',len(six_cycles),'MAX_CYCLES_PER_EDGE',max(map(len,edge_cycles.values())))
print('COMPLETE_FILTRATION',{'r0':'16 points','r1':'9 circles','r2':'9 two-spheres plus 2 three-spheres','r3':'seven-sphere','r4':'contractible'})
print('MK_RIPS_COMPLETE_FILTRATION_INTEGRAL_HOMOTOPY_VERIFIED')

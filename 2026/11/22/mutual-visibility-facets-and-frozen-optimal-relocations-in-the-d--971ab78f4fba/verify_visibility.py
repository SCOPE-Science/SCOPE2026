"""Reproducible exact mutual-visibility census and exchange geometry of H(5,2).
Uses only the Python standard library. Run: python verify_desargues_visibility.py
"""
from collections import Counter, deque
from itertools import combinations, permutations

BASE=range(5)
U=list(combinations(BASE,2))
W=list(combinations(BASE,3))
V=U+W
N=len(V)
assert N==20
pos={v:i for i,v in enumerate(V)}
adj=[0]*N
for i,u in enumerate(U):
    for j,w in enumerate(W,10):
        if set(u).issubset(w):
            adj[i]|=1<<j
            adj[j]|=1<<i
assert all(mask.bit_count()==3 for mask in adj)

def distance(s):
    dist=[-1]*N;dist[s]=0;queue=deque([s])
    while queue:
        a=queue.popleft()
        for b in range(N):
            if adj[a]>>b&1 and dist[b]<0:
                dist[b]=dist[a]+1
                queue.append(b)
    return dist

dist=[distance(v) for v in range(N)]
assert max(max(d) for d in dist)==5

# Each interior mask represents exactly one geodesic; its endpoints are excluded.
interiors={}
for u,v in combinations(range(N),2):
    ims=[]
    def extend(w,mask):
        if w==v:
            ims.append(mask)
            return
        for t in range(N):
            if adj[w]>>t&1 and dist[u][t]==dist[u][w]+1 and dist[u][t]+dist[t][v]==dist[u][v]:
                extend(t,mask if t==v else mask|1<<t)
    extend(u,0)
    interiors[u,v]=tuple(ims)
assert Counter(map(len,interiors.values()))=={1:90,2:60,4:30,12:10}

def admissible(mask):
    selected=[i for i in range(N) if mask>>i&1]
    return all(any((p&mask)==0 for p in interiors[u,v])
               for u,v in combinations(selected,2))

# Exhaust every face exactly once in increasing vertex order. The property
# is hereditary, so no invalid set can have any valid extension.
layers=[[0]]
for k in range(1,N+1):
    nxt=[]
    for old in layers[-1]:
        for new_vertex in range(old.bit_length(),N):
            candidate=old|1<<new_vertex
            if admissible(candidate):
                nxt.append(candidate)
    layers.append(nxt)
    if not nxt:
        break
expected=[1,20,190,1080,3925,8944,11300,5840,150,0]
assert [len(x) for x in layers]==expected
all_faces=set(s for layer in layers for s in layer)
assert len(all_faces)==31450
maximal=[s for s in all_faces if all((s|1<<v) not in all_faces for v in range(N) if not(s>>v&1))]
assert Counter(s.bit_count() for s in maximal)=={6:60,7:4700,8:150}
optimal=layers[8]

# Explicit graph automorphisms: all permutations of the five labels and
# 2-set <-> complementary 3-set duality, precisely 240 maps.
autos=[]
for perm in permutations(BASE):
    for dual in (False,True):
        p=[]
        for x in V:
            y=tuple(sorted(perm[i] for i in x))
            if dual:
                y=tuple(i for i in BASE if i not in y)
            p.append(pos[y])
        assert all(((adj[i]>>j)&1)==((adj[p[i]]>>p[j])&1) for i in range(N) for j in range(N))
        autos.append(tuple(p))
assert len(set(autos))==240

def act(mask,p):
    return sum(1<<p[i] for i in range(N) if mask>>i&1)

unseen=set(optimal)
orbits=[]
while unseen:
    representative=min(unseen)
    orbit={act(representative,p) for p in autos}
    assert orbit<=set(optimal)
    orbits.append((representative,orbit))
    unseen-=orbit
assert sorted(len(o) for _,o in orbits)==[30,120]

# Distinct induced-subgraph types: 30 independent; 120 have 3 disjoint
# edges and two isolated vertices. Both types are single symmetry orbits.
for s in optimal:
    degrees=sorted((adj[i]&s).bit_count() for i in range(N) if s>>i&1)
    assert degrees in ([0]*8, [0,0]+[1]*6)
    assert (degrees==[0]*8)==(s>>10==0 or s&((1<<10)-1)==0)

# Natural edge model of the Petersen graph: its vertices are 2-subsets,
# two are adjacent exactly when disjoint. On each side of H(5,2), the 15
# pure configurations are all shore-minus-two sets indexed by these edges.
def petersen_edge(s):
    if s>>10==0:
        omitted=[U[i] for i in range(10) if not(s>>i&1)]
        side=0
    else:
        assert s&((1<<10)-1)==0
        omitted=[tuple(i for i in BASE if i not in W[j])
                 for j in range(10) if not(s>>(10+j)&1)]
        side=1
    assert len(omitted)==2 and set(omitted[0]).isdisjoint(omitted[1])
    return side,frozenset(omitted)

pure=[s for s in optimal if s>>10==0 or s&((1<<10)-1)==0]
assert len(pure)==30
assert Counter(petersen_edge(s)[0] for s in pure)=={0:15,1:15}
for side in (0,1):
    assert {petersen_edge(s)[1] for s in pure if petersen_edge(s)[0]==side}=={
        frozenset((a,b)) for a,b in combinations(U,2) if set(a).isdisjoint(b)}

# Build exact single-token exchange and adjacent-token-slide edge sets.
R={s:set() for s in optimal}
T={s:set() for s in optimal}
for s,t in combinations(optimal,2):
    if (s^t).bit_count()!=2:
        continue
    R[s].add(t);R[t].add(s)
    v=(s&~t).bit_length()-1
    w=(t&~s).bit_length()-1
    if adj[v]>>w&1:
        T[s].add(t);T[t].add(s)
assert sum(map(len,R.values()))//2==60
assert all(not links for links in T.values())
assert Counter(map(len,R.values()))=={0:120,4:30}

# Check adjacency EXACTLY realizes two separate line graphs of Petersen.
for s,t in combinations(optimal,2):
    expected_adj=False
    if s in pure and t in pure:
        side_s,e_s=petersen_edge(s);side_t,e_t=petersen_edge(t)
        expected_adj=(side_s==side_t and len(e_s&e_t)==1)
    assert (t in R[s])==expected_adj

# Verify connected components have precisely 15,15, and 120 singleton states.
remaining=set(optimal)
component_sizes=[]
while remaining:
    start=min(remaining);queue=[start];visited={start}
    for v in queue:
        for w in R[v]:
            if w not in visited:
                visited.add(w);queue.append(w)
    remaining-=visited
    component_sizes.append(len(visited))
assert sorted(component_sizes,reverse=True)==[15,15]+[1]*120
print('visibility_face_counts',expected)
print('facet_counts',sorted(Counter(x.bit_count() for x in maximal).items()))
print('maximal_orbit_sizes',sorted(len(o) for _,o in orbits))
print('optimal_jump_graph','2 L(Petersen) + 120 isolated vertices')
print('optimal_slide_graph','150 isolated vertices')
print('VERIFY_OK')

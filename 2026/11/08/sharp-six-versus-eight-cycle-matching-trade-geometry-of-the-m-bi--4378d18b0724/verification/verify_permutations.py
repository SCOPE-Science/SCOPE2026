"""Independent bipartite-permutation census for GP(8,3) dimers.
Run: python3 verify_permutations.py. Requires Python 3.9+, standard library only.
"""
from itertools import permutations,combinations
from collections import Counter,deque

N=16
B=[[0]*N for _ in range(N)]
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
        B[a][b]=B[b][a]=1
L=tuple(v for v in range(N) if (v<8 and v%2==0) or (v>=8 and v%2==1))
R=tuple(v for v in range(N) if v not in L)
assert len(L)==len(R)==8 and all(sum(B[v])==3 for v in range(N))
assert all(not B[a][b] for a,b in combinations(L,2))
assert all(not B[a][b] for a,b in combinations(R,2))

# Alternative enumeration: exhaust the 8! possible bijections L -> R.
perms=[p for p in permutations(range(8)) if all(B[L[i]][R[p[i]]] for i in range(8))]
assert len(perms)==33

def changed_cycle_length(p,q):
    # Relative permutation on left-side labels: i -> inverse_p[q[i]].
    inv=[0]*8
    for j,r in enumerate(p):inv[r]=j
    rel=[inv[q[i]] for i in range(8)]
    support={i for i in range(8) if rel[i]!=i}
    if not support:return 0
    # The single-cycle test excludes a symmetric difference with two cycles.
    seed=min(support);visited={seed};j=rel[seed]
    while j not in visited:
        visited.add(j);j=rel[j]
    if j!=seed or visited!=support:return -1
    return len(support)

S=[set() for _ in perms];O=[set() for _ in perms]
for a,b in combinations(range(len(perms)),2):
    k=changed_cycle_length(perms[a],perms[b])
    if k==3:S[a].add(b);S[b].add(a)
    if k==4:O[a].add(b);O[b].add(a)
assert sum(map(len,S))//2==96 and sum(map(len,O))//2==36

# This census uses permutation differences, rather than explicit cycle lists.
def metrics(adj):
    parts=[];left=set(range(len(adj)));pairs=Counter();ecc=Counter()
    while left:
        root=min(left);seen={root};todo=[root]
        while todo:
            x=todo.pop()
            for y in adj[x]-seen:seen.add(y);todo.append(y)
        parts.append(len(seen));left-=seen
        if len(seen)==1:continue
        for s in seen:
            dist={s:0};q=deque([s])
            while q:
                x=q.popleft()
                for y in adj[x]:
                    if y not in dist:dist[y]=dist[x]+1;q.append(y)
            assert set(dist)==seen
            ecc[max(dist.values())]+=1
            for t,d in dist.items():
                if s<t:pairs[d]+=1
    return tuple(sorted(parts)),pairs,ecc

T=[S[i]|O[i] for i in range(33)]
assert metrics(S)==((1,1,1,30),Counter({1:96,2:216,3:120,4:3}),Counter({3:24,4:6}))
assert metrics(O)==((33,),Counter({1:36,2:198,3:54,4:240}),Counter({3:3,4:30}))
assert metrics(T)==((33,),Counter({1:132,2:342,3:54}),Counter({3:33}))
assert Counter((len(S[i]),len(O[i])) for i in range(33))=={(0,12):3,(8,2):6,(6,1):24}

# Check bipartite 2-factor structure using an independent permutation model.
def two_factor_type(p):
    match={tuple(sorted((L[i],R[p[i]]))) for i in range(8)}
    edges=[(a,b) for a in range(16) for b in range(a+1,16) if B[a][b] and (a,b) not in match]
    adj=[set() for i in range(16)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    assert all(len(s)==2 for s in adj)
    rest=set(range(16)); lengths=[]
    while rest:
        origin=min(rest);stack=[origin];comp={origin}
        while stack:
            for y in adj[stack.pop()]-comp:comp.add(y);stack.append(y)
        lengths.append(len(comp));rest-=comp
    return tuple(sorted(lengths))
assert Counter(two_factor_type(p) for p in perms)=={(8,8):3,(16,):6,(6,10):24}
for i,p in enumerate(perms):
    assert (len(S[i]),len(O[i]))=={(8,8):(0,12),(16,):(8,2),(6,10):(6,1)}[two_factor_type(p)]

hubs={i for i in range(33) if len(O[i])==12}
mids={i for i in range(33) if len(O[i])==2}
leaves={i for i in range(33) if len(O[i])==1}
assert len(hubs)==3 and len(mids)==6 and len(leaves)==24
assert all(O[i]<=hubs for i in mids|leaves)
assert all(len(O[h]&leaves)==8 for h in hubs)
assert Counter(frozenset(O[i]) for i in mids)=={frozenset(p):2 for p in combinations(sorted(hubs),2)}
print('PASS_BIPARTITE_8_FACTORIAL_33_MATCHINGS')
print('PASS_RELATIVE_PERMUTATION_SINGLE_3_OR_4_CYCLE_TRADES')
print('PASS_THREE_COMPONENTS_HEXAGON_ONLY_AND_CONNECTED_OCTAGON_ONLY')
print('PASS_STRUCTURAL_OCTAGON_GRAPH_AND_ALL_33_COMPLEMENT_2_FACTOR_TYPES')
print('PASS_EXACT_RADIUS_DIAMETER_ECCENTRICITY_ALL_THREE_MOVE_RULES')

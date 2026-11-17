"""Independent adjacency-based majority checker; standard library only.
No dependence on the transfer or orbit-enumeration implementation.
"""
from itertools import combinations, permutations
from collections import Counter, deque

E = list(combinations((1,2,3,4,5,6),2))
edge_index={e:i for i,e in enumerate(E)}
match=[];seen=set()
for p in permutations((1,2,3,4,5,6)):
    m=tuple(sorted(tuple(sorted((p[j],p[j+1]))) for j in (0,2,4)))
    if m not in seen:
        seen.add(m);match.append(m)
match.sort()
assert len(match)==15 and len(E)==15
adj=[[] for _ in range(30)]
for i,e in enumerate(E):
    for j,m in enumerate(match):
        if e in m:
            adj[i].append(j+15)
            adj[j+15].append(i)
assert all(len(n)==3 for n in adj)
assert sum(map(len,adj))//2 == 45

# Independently confirm shortest cycle length eight by BFS from every vertex.
girth=30
for v in range(30):
    queue=deque([v]); depth={v:0}; parent={v:-1}
    while queue:
        u=queue.popleft()
        for z in adj[u]:
            if z not in depth:
                depth[z]=depth[u]+1;parent[z]=u;queue.append(z)
            elif parent[u]!=z:
                girth=min(girth,depth[z]+depth[u]+1)
assert girth==8

# Build shore update using actual graph-neighbor indices and independent
# bitwise tally. This proves the factorization for ALL 2^30 inputs, without
# attempting to scan a billion states.
def majority_on_subset(mask, source_shore, target_shore):
    result=0
    for j in range(15):
        v=target_shore*15+j
        votes=0
        for nb in adj[v]:
            assert nb//15==source_shore
            votes += (mask >> (nb%15))&1
        result |= (votes>=2)<<j
    return result

N=1<<15
forward=[majority_on_subset(x,0,1) for x in range(N)]
backward=[majority_on_subset(x,1,0) for x in range(N)]
# Construct the two opposite-shore-step operators independently.
second_edges=[backward[forward[x]] for x in range(N)]
second_match=[forward[backward[x]] for x in range(N)]
ref_edges=[x for x in range(N) if second_edges[x]==x]
ref_match=[x for x in range(N) if second_match[x]==x]
assert len(ref_edges)==len(ref_match)==2386
assert all(second_edges[second_edges[second_edges[x]]]
           == second_edges[second_edges[x]] for x in range(N))
assert all(second_match[second_match[second_match[x]]]
           == second_match[second_match[x]] for x in range(N))
assert any(second_edges[x]!=second_edges[second_edges[x]] for x in range(N))

# Derive the first entrance on each shore from its direct 1-step neighbor map.
# Pairs of independently chosen shores yield 2^30 initial states.
p_edges=[];p_match=[]
path_edges=list(range(N));path_match=list(range(N))
for time in range(5):
    target_edges=set(ref_edges if time%2==0 else ref_match)
    target_match=set(ref_match if time%2==0 else ref_edges)
    p_edges.append(sum(mask in target_edges for mask in path_edges))
    p_match.append(sum(mask in target_match for mask in path_match))
    path_edges=[(forward if time%2==0 else backward)[mask] for mask in path_edges]
    path_match=[(backward if time%2==0 else forward)[mask] for mask in path_match]
assert p_edges==p_match==[2386,16808,25208,28568,32768]
assert [(p_edges[t]*p_match[t]-(p_edges[t-1]*p_match[t-1] if t else 0))
        for t in range(5)]==[5692996,276815868,352934400,180687360,257611200]

# Group predecessors by their destination under the stabilized two-step map,
# then enforce phase equality to count eventual fixed points exactly.
dest_edge=[second_edges[second_edges[s]] for s in range(N)]
dest_match=[second_match[second_match[s]] for s in range(N)]
runE=list(range(N));runM=list(range(N))
fixed_layer=[]
for time in range(5):
    allowedE=set(ref_edges if time%2==0 else ref_match)
    allowedM=set(ref_match if time%2==0 else ref_edges)
    x_count=Counter(dest_edge[u] for u in range(N) if runE[u] in allowedE)
    y_count=Counter(dest_match[u] for u in range(N) if runM[u] in allowedM)
    fixed_layer.append(sum(x_count[u]*y_count[forward[u]] for u in ref_edges))
    runE=[(forward if time%2==0 else backward)[v] for v in runE]
    runM=[(backward if time%2==0 else forward)[v] for v in runM]
assert fixed_layer==[2386,264032,1372112,11129552,39202352]
first_f=[fixed_layer[0]]+[fixed_layer[t]-fixed_layer[t-1] for t in range(1,5)]
first_all=[p_edges[t]*p_match[t]-(p_edges[t-1]*p_match[t-1] if t else 0)
           for t in range(5)]
first_two=[u-v for u,v in zip(first_all,first_f)]
assert first_f==[2386,261646,1108080,9757440,28072800]
assert first_two==[5690610,276554222,351826320,170929920,229538400]

# Completely independent global 30-bit transition for a stratified sample.
def raw_next(x):
    y=0
    for v,neighbors in enumerate(adj):
        if sum((x>>u)&1 for u in neighbors)>=2:
            y|=1<<v
    return y

def factored_next(x):
    a=x&((1<<15)-1)
    b=x>>15
    return backward[b] | (forward[a]<<15)

# Deliberate deterministic samples include both monochromatic states, all
# singleton states and 12,000 uniformly dispersed configurations. This is a
# cross-check, NOT the source of the all-state proof.
tests=[0,(1<<30)-1]+[1<<j for j in range(30)]
seed=314159265
for _ in range(12000):
    seed=(1664525*seed+1013904223)&((1<<32)-1)
    tests.append(seed&((1<<30)-1))
for x in tests:
    assert raw_next(x)==factored_next(x)
    y=x
    for _ in range(4):y=raw_next(y)
    assert raw_next(raw_next(y))==y
print('graph vertices=30 edges=45 girth=8, bipartite 15+15')
print('direct shore fixed counts:',len(ref_edges),len(ref_match))
print('both shore depth-two projection identities: verified 32768+32768 inputs')
print('one-shore eligibility:',p_edges)
print('first entry:',first_all)
print('first entry, eventual period one:',first_f)
print('first entry, eventual period two:',first_two)
print('direct 30-bit graph-update cross-checks:',len(tests))
print('all independent checks passed')

"""Independent standard-library GP(5,2) check of edge-partition enumeration.
Run: python3 check_gp.py
"""
from collections import Counter, deque
from itertools import permutations

N=10
adj=[set() for _ in range(N)]
def edge(u,v):
    adj[u].add(v)
    adj[v].add(u)
for i in range(5):
    edge(i,(i+1)%5)
    edge(i,i+5)
    edge(i+5,5+(i+2)%5)
E=[(u,v) for u in range(N) for v in sorted(adj[u]) if u<v]
assert len(E)==15 and all(len(a)==3 for a in adj)
D=[]
for start in range(N):
    dist=[-1]*N; dist[start]=0
    todo=deque([start])
    while todo:
        u=todo.popleft()
        for v in adj[u]:
            if dist[v]<0:
                dist[v]=dist[u]+1;todo.append(v)
    D.append(dist)
assert max(max(x) for x in D)==2
ed=[[min(D[v][u],D[v][w]) for v in range(N)] for u,w in E]
counts=Counter(); shapes=Counter(); optimum=[]
precheck=Counter()
words=[0]*N

def verify(block_count):
    blocks=[[] for _ in range(block_count)]
    for v,c in enumerate(words): blocks[c].append(v)
    if block_count==3:
        precheck['all']+=1
        crossings=[(words[u],words[v]) for u,v in E if words[u]!=words[v]]
        if len(crossings)<=6:
            precheck['few_crossings']+=1
            bypair=Counter(tuple(sorted(x)) for x in crossings)
            if max(bypair.values())<=2:
                precheck['few_each_pair']+=1
                singles=[b[0] for b in blocks if len(b)==1]
                if len(singles)==2 and singles[1] in adj[singles[0]]:
                    precheck['adjacent_singletons']+=1
    profiles=[tuple(min((row[v] for v in b)) for b in blocks) for row in ed]
    if len(set(profiles))!=len(E): return
    counts[block_count]+=1
    if block_count==4:
        shapes[tuple(sorted(map(len,blocks)))]+=1
        optimum.append(frozenset(frozenset(b) for b in blocks))

def generate(i,k):
    if i==N:
        verify(k);return
    for c in range(k+1):
        words[i]=c
        generate(i+1,max(k,c+1))
generate(1,1)
assert [counts[k] for k in range(1,11)] == [0,0,0,40,11965,14877,5045,720,45,1]
assert precheck==Counter({'all':9330,'few_crossings':105,'few_each_pair':15,'adjacent_singletons':15})
assert shapes==Counter({(1,3,3,3):40})
assert len(set(optimum))==40
# Independently confirm the orbit under the complete graph automorphism group.
perms=[]
for image in permutations(range(N)):
    if all((image[v] in adj[image[u]]) == (v in adj[u]) for u in range(N) for v in range(u+1,N)):
        perms.append(image)
assert len(perms)==120
rep=optimum[0]
orbit={frozenset(frozenset(p[v] for v in block) for block in rep) for p in perms}
assert orbit==set(optimum)
print('edge_partition_counts', [counts[k] for k in range(1,11)])
print('three_block_precheck', dict(precheck))
print('four_block_shapes', dict(shapes), 'automorphisms',len(perms), 'orbit',len(orbit))
print('GP_CHECK_OK')

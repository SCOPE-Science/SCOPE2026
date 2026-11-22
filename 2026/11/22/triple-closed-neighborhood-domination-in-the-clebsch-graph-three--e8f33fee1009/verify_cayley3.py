"""Exact triple closed-neighborhood domination and optimum exchange, 16-vertex folded cube."""
from collections import Counter, deque
from itertools import combinations, permutations
import json

V = tuple(range(16))
G = (1, 2, 4, 8, 15)
N = [sum(1 << (v ^ g) for g in (0,) + G) for v in V]
assert len(set(N)) == 16
assert all(n.bit_count() == 6 for n in N)
counts = Counter()
opt = []
for mask in range(1 << 16):
    if all((mask & nb).bit_count() >= 3 for nb in N):
        k = mask.bit_count()
        counts[k] += 1
        if k == 10: opt.append(mask)
assert counts == {10:312,11:1872,12:1580,13:560,14:120,15:16,16:1}
assert len(opt) == 312

def deleted_shape(mask):
    deleted = ((1 << 16) - 1) ^ mask
    deg = [sum(bool(N[v] & (1 << w)) for w in V if w != v and (deleted >> w) & 1)
           for v in V if (deleted >> v) & 1]
    return tuple(sorted(deg))
shapes = Counter(deleted_shape(m) for m in opt)
assert shapes == {(1,1,1,1,1,1):40,(0,2,2,2,2,2):192,(2,2,2,2,2,2):80}

def getgraph(t):
    adj=[[] for _ in opt]
    for a,b in combinations(range(len(opt)),2):
        if (opt[a] & opt[b]).bit_count() >= 10-t:
            adj[a].append(b);adj[b].append(a)
    unseen = set(range(len(opt))); components=[]
    while unseen:
        st=[unseen.pop()]; comp=1
        while st:
            for j in adj[st.pop()]:
                if j in unseen: unseen.remove(j);st.append(j);comp+=1
        components.append(comp)
    result={'edges':sum(map(len,adj))//2,'degrees':dict(sorted(Counter(map(len,adj)).items())),
            'components':dict(sorted(Counter(components).items()))}
    if len(components)==1:
        ec=Counter()
        for a in range(len(opt)):
            dist={a:0};q=deque([a])
            while q:
                i=q.popleft()
                for j in adj[i]:
                    if j not in dist:dist[j]=dist[i]+1;q.append(j)
            assert len(dist)==len(opt)
            ec[max(dist.values())]+=1
        result['eccentricities']=dict(sorted(ec.items()))
    return result
result={'graph':'folded five-cube 5-regular','triple_domination_polynomial':dict(sorted(counts.items())),
        'minimum':10,'optima':len(opt),'deleted_induced_degree_sequences':{str(k):v for k,v in sorted(shapes.items())},
        'one_exchange':getgraph(1),'two_exchange':getgraph(2),'three_exchange':getgraph(3)}
print(json.dumps(result,sort_keys=True))

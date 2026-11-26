#!/usr/bin/env python3
"""Exact finite certificate checker: perfect-matching cycle flips of GP(12,5).
Only the Python standard library is needed.
"""
from collections import Counter, deque
from itertools import combinations
import json

N=12
E=sorted({tuple(sorted(e)) for i in range(N) for e in
    ((i,(i+1)%N),(i,12+i),(12+i,12+(i+5)%N))})
assert len(E)==36
edges={e:j for j,e in enumerate(E)}
adj=[[] for _ in range(24)]
for j,(a,b) in enumerate(E): adj[a].append((b,j));adj[b].append((a,j))
assert all(len(a)==3 for a in adj)
# Exhaustive recursive matching enumeration by the least unpaired vertex.
M=[]
def rec(unpaired, mask):
    if not unpaired:
        M.append(mask);return
    v=min(unpaired)
    for w,j in adj[v]:
        if w in unpaired:rec(unpaired-{v,w},mask|(1<<j))
rec(set(range(24)),0)
M=sorted(M); assert len(M)==120 and len(set(M))==120
ID={m:i for i,m in enumerate(M)}
# Enumerate undirected simple cycles by least vertex; represent as edge masks.
def cycle_masks(k):
    found=set()
    def ext(path):
        if len(path)==k:
            v=path[-1]
            for w,j in adj[v]:
                if w==path[0]:
                    ed=[edges[tuple(sorted((path[t],path[(t+1)%k])))] for t in range(k)]
                    found.add(sum(1<<x for x in ed))
            return
        for w,j in adj[path[-1]]:
            if w>path[0] and w not in path:ext(path+[w])
    for v in range(24): ext([v])
    return sorted(found)
cy6=cycle_masks(6);cy8=cycle_masks(8)
assert cycle_masks(4)==[] and len(cy6)==12

def toggles(cycles):
    A=[set() for _ in M]
    for i,m in enumerate(M):
        for c in cycles:
            if (m&c).bit_count()*2!=c.bit_count():continue
            j=ID.get(m^c)
            if j is not None and i!=j:A[i].add(j)
    assert all(i in A[j] for j in range(len(M)) for i in A[j])
    return A

def stats(A):
    seen=set();components=[];eccs=Counter()
    for s in range(len(A)):
        if s in seen:continue
        cc=[];stack=[s];seen.add(s)
        while stack:
            v=stack.pop();cc.append(v)
            for w in A[v]:
                if w not in seen:seen.add(w);stack.append(w)
        components.append(cc)
    detail=[]
    for comp in sorted(components,key=lambda c:(-len(c),min(c))):
        radii=[]
        for s in comp:
            dist={s:0};q=deque([s])
            while q:
                v=q.popleft()
                for w in A[v]:
                    if w not in dist:dist[w]=dist[v]+1;q.append(w)
            assert len(dist)==len(comp)
            radii.append(max(dist.values()))
        detail.append({'size':len(comp),'radius':min(radii),'diameter':max(radii),
          'eccentricities':dict(sorted(Counter(radii).items())),
          'degrees':dict(sorted(Counter(len(A[i]) for i in comp).items()))})
        eccs.update(radii)
    return {'vertices':len(M),'edges':sum(map(len,A))//2,
      'component_sizes':sorted((len(c) for c in components),reverse=True),
      'degree_distribution':dict(sorted(Counter(map(len,A)).items())),
      'radius':min(eccs) if len(components)==1 else None,
      'diameter':max(eccs) if len(components)==1 else None,
      'eccentricities':dict(sorted(eccs.items())) if len(components)==1 else None,
      'component_profiles':detail}
A6=toggles(cy6);A68=toggles(cy6+cy8)
S6=stats(A6);S68=stats(A68)
assert S6['component_sizes']==[57,18,18,18]+[1]*9
assert S6['edges']==192
assert S68['component_sizes']==[120]
assert S68['edges']==606 and S68['radius']==4 and S68['diameter']==6
assert S68['eccentricities']=={4:96,5:18,6:6}
assert S6['degree_distribution']=={0:9,2:48,4:36,5:24,8:3}
# Crosscheck pairwise: adjacency iff symmetric difference forms ONE simple cycle of allowed length.
def single_cycle(d):
    ix=[j for j in range(len(E)) if (d>>j)&1]
    if len(ix) not in (6,8):return False
    sub=[[] for _ in range(24)]
    for j in ix:
        a,b=E[j];sub[a].append(b);sub[b].append(a)
    active=[v for v in range(24) if sub[v]]
    if any(len(sub[v])!=2 for v in active):return False
    seen={active[0]};todo=[active[0]]
    while todo:
        for w in sub[todo.pop()]:
            if w not in seen:seen.add(w);todo.append(w)
    return len(seen)==len(ix)
for i,j in combinations(range(len(M)),2):
    ok=single_cycle(M[i]^M[j])
    assert ok==(j in A68[i]),(i,j)
cert={'graph':'GP(12,5)','edge_index':[list(e) for e in E],
      'perfect_matching_masks_hex':[format(m,'09x') for m in M],
      'hexagonal_cycle_masks_hex':[format(c,'09x') for c in cy6],
      'octagonal_cycle_masks_hex':[format(c,'09x') for c in cy8],
      'flip_edges_6':[[i,j] for i in range(len(M)) for j in sorted(A6[i]) if i<j],
      'flip_edges_8':[[i,j] for i in range(len(M)) for j in sorted(A68[i]-A6[i]) if i<j],
      'stats6':S6,'stats68':S68}
with open('nauru_certificate.json','w',encoding='utf8') as f:
    json.dump(cert,f,sort_keys=True,separators=(',',':'));f.write('\n')
print('graph_vertices=24 graph_edges=36')
print('perfect_matchings=',len(M),'simple_6_cycles=',len(cy6),'simple_8_cycles=',len(cy8))
for name,S in [('6',S6),('6_or_8',S68)]:
    print('flip_type=',name,'edges=',S['edges'],'components=',S['component_sizes'])
    print('degree_distribution=',S['degree_distribution'],'radius=',S['radius'],'diameter=',S['diameter'],'ecc=',S['eccentricities'])
print('pairwise_symdiff_crosscheck=PASSED')

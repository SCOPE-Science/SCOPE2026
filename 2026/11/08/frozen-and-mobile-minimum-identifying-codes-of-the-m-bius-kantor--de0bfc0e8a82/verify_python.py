#!/usr/bin/env python3
"""Exact independent Python enumeration of minimum identifying-code reconfigurations."""
from collections import Counter,deque
from itertools import combinations
from hashlib import sha256
from pathlib import Path

N=16
E=set()
def add(x,y): E.add(tuple(sorted((x,y))))
for i in range(8):
    add(i,(i+1)%8);add(i,8+i);add(8+i,8+(i+3)%8)
assert len(E)==24
NBR=[{v} for v in range(N)]
for x,y in E:
    NBR[x].add(y);NBR[y].add(x)

def is_code(T):
    sig=[frozenset(T.intersection(NBR[v])) for v in range(N)]
    return all(sig) and len(set(sig))==N

by_size=[0]*17
codes=[]
for k in range(N+1):
    for tuple_s in combinations(range(N),k):
        T=set(tuple_s)
        if is_code(T):
            by_size[k]+=1
            if k==8:codes.append(sum(1<<v for v in T))
assert all(x==0 for x in by_size[:8])
assert by_size[8]==584
assert len(codes)==584
codes.sort()
code_set=set(codes)

def edges_of(slide):
    edges=[]
    for mask in codes:
        in_s=[v for v in range(N) if mask & (1<<v)]
        out_s=[v for v in range(N) if not(mask & (1<<v))]
        for u in in_s:
            for v in out_s:
                if slide and (min(u,v),max(u,v)) not in E:continue
                dst=mask^(1<<u)^(1<<v)
                if dst in code_set and mask<dst: edges.append((mask,dst))
    return sorted(edges)

def profile(edges):
    adj={m:set() for m in codes}
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    components=[];seen=set()
    for s in codes:
        if s in seen:continue
        todo=[s];seen.add(s);c=[]
        while todo:
            v=todo.pop();c.append(v)
            for w in adj[v]:
                if w not in seen:seen.add(w);todo.append(w)
        components.append(c)
    eccentricity=Counter()
    for comp in components:
        if len(comp)==1:
            eccentricity[0]+=1;continue
        for s in comp:
            Q=deque([s]);dist={s:0}
            while Q:
                u=Q.popleft()
                for v in adj[u]:
                    if v not in dist:dist[v]=dist[u]+1;Q.append(v)
            assert len(dist)==len(comp)
            eccentricity[max(dist.values())]+=1
    return Counter(map(len,components)), Counter(map(len,adj.values())),eccentricity

T=edges_of(False);S=edges_of(True)
assert len(T)==2496 and len(S)==864
assert set(S)<=set(T)
assert profile(T)==(Counter({584:1}), Counter({9:192,10:144,4:96,6:48,8:48,12:48,24:8}), Counter({8:344,7:240}))
assert profile(S)==(Counter({488:1,1:96}), Counter({0:96,2:240,4:168,6:48,8:30,24:2}),Counter({0:96,8:104,9:192,10:192}))
degree_S=Counter()
for a,b in S:degree_S[a]+=1;degree_S[b]+=1
isolates=[m for m in codes if not degree_S[m]]
assert len(isolates)==96
assert Counter(sum((m>>a&1) and (m>>b&1) for a,b in E) for m in isolates)==Counter({5:48,7:48})
root=Path(__file__).resolve().parent
(root/'codes.txt').write_text(''.join(str(x)+'\n' for x in codes),encoding='utf8')
(root/'slides.txt').write_text(''.join(f'{a} {b}\n' for a,b in S),encoding='utf8')
(root/'jumps.txt').write_text(''.join(f'{a} {b}\n' for a,b in T),encoding='utf8')
print('PYTHON_VERIFY_OK', 'gamma_id=8','min_code_count=584','TJ_vertices=584','TJ_edges=2496','TJ_connected=1','TJ_radius=7','TJ_diameter=8','TS_vertices=584','TS_edges=864','TS_components=97','TS_giant=488','TS_isolates=96','TS_radius_giant=8','TS_diameter_giant=10')
for f in ['codes.txt','slides.txt','jumps.txt']:
    data=(root/f).read_bytes()
    print(f,len(data),sha256(data).hexdigest())

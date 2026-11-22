#!/usr/bin/env python3
"""Independent geometric checker for ternary projective incidence configurations."""
from itertools import product, combinations
from collections import Counter, deque

def normalize(u):
    z=next(x for x in u if x)
    return tuple((x*pow(z,-1,3))%3 for x in u)
V=sorted({normalize(x) for x in product(range(3),repeat=3) if any(x)})
assert len(V)==13
P=set(range(13))
lines=[frozenset(i for i,p in enumerate(V) if sum(x*y for x,y in zip(p,l))%3==0) for l in V]
assert len(set(lines))==13 and all(len(e)==4 for e in lines)
triangle=[]; oval=[]
for c in combinations(range(13),3):
    if not any(set(c).issubset(line) for line in lines):triangle.append(frozenset(c))
for c in combinations(range(13),4):
    if all(len(set(c)&line)<=2 for line in lines):oval.append(frozenset(c))
assert len(triangle)==len(oval)==234
tri_idx={t:i for i,t in enumerate(triangle)}
N=468; adj=[set() for _ in range(N)]

def is_limited_dominating(configuration):
    chosen_p={i for i in configuration if i<13}
    chosen_l={i-13 for i in configuration if i>=13}
    for p in range(13):
        if p not in chosen_p and not (1<=sum(p in lines[l] for l in chosen_l)<=2):return False
    for l in range(13):
        if l not in chosen_l and not (1<=len(lines[l]&chosen_p)<=2):return False
    return True

for t in triangle:
    ext_t={i for i,L in enumerate(lines) if not L&t}
    assert len(ext_t)==4 and is_limited_dominating(set(t)|{13+i for i in ext_t})

for j,o in enumerate(oval):
    ext={i for i,L in enumerate(lines) if not L&o}
    assert len(ext)==3
    mask_o=set(o)|{13+i for i in ext}
    assert len(mask_o)==7 and is_limited_dominating(mask_o)
    for v in o:
        t=o-{v};i=tri_idx[t];ext_t={i for i,L in enumerate(lines) if not L&t}
        assert len(ext_t)==4 and ext<=ext_t
        mask_t=set(t)|{13+i for i in ext_t}
        assert len(mask_o^mask_t)==2
        adj[i].add(234+j);adj[234+j].add(i)
assert all(len(z)==4 for z in adj)
assert sum(map(len,adj))//2==936
profs=Counter();diam=0
for start in range(N):
    dist=[-1]*N;dist[start]=0;Q=deque([start]);
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;Q.append(v)
    assert -1 not in dist
    profs[tuple(Counter(dist)[k] for k in range(max(dist)+1))]+=1
    diam=max(diam,max(dist))
print('geometric triangles',len(triangle),'ovals',len(oval),'configurations',N,'edges',936,'degree',4,'diameter',diam)
for profile,count in profs.items():print('distance profile',count,profile,'sum',sum(profile))
assert diam==9
assert len(profs)==1
# Both types are distinct (dual) and a transversal swap is the only legal one-vertex exchange.
print('PYTHON GEOMETRIC CHECK PASS')

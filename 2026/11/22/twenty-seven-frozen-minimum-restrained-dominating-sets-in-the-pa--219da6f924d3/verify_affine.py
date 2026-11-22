#!/usr/bin/env python3
"""Exact restrained-domination and reconfiguration census for a (9_3) incidence graph.
Python 3 standard library only. Run: python3 verify_affine.py
"""
from collections import Counter, deque
from itertools import product

P = list(product(range(3),repeat=2))  # point labels (x,y), lexicographically
L = [('x',a) for a in range(3)] + [('y',a) for a in range(3)] + [('s',a) for a in range(3)]
N = 18; FULL=(1<<N)-1
adj=[0]*N
for i,(x,y) in enumerate(P):
    for j,(d,a) in enumerate(L):
        hit=(x if d=='x' else y if d=='y' else (x+y)%3)==a
        if hit: adj[i]|=1<<(9+j); adj[9+j]|=1<<i
assert all(a.bit_count()==3 for a in adj)

def ordinary(s):
    return all(adj[v]&s for v in range(N) if not(s>>v&1))
def rd(s):
    out=FULL^s
    return all(adj[v]&s and adj[v]&out for v in range(N) if out>>v&1)

def act(s,p):
    return sum(1<<p[i] for i in range(N) if s>>i&1)

def group():
    triples={frozenset(i for i in range(9) if adj[i]&(1<<(9+j))):j for j in range(9)}
    g=[]
    for a,b,c,d,e,f in product(range(3),repeat=6):
        if (a*d-b*c)%3==0:continue
        p=[P.index(((a*x+b*y+e)%3,(c*x+d*y+f)%3)) for x,y in P]
        ims=[frozenset(p[i] for i in t) for t in triples]
        if not all(t in triples for t in ims):continue
        line_images=[None]*9
        for pre,j in triples.items():line_images[j]=9+triples[frozenset(p[i] for i in pre)]
        g.append(tuple(p+line_images))
    assert len(set(g))==108
    dual=(9,12,15,16,11,14,13,17,10,0,8,4,1,6,5,2,3,7)
    ret=set(g)|{tuple(dual[gi] for gi in p) for p in g}
    assert len(ret)==216
    assert all({p[j] for j in range(N) if adj[i]>>j&1} == {j for j in range(N) if adj[p[i]]>>j&1} for p in ret for i in range(N))
    return ret

ordc=Counter(); rdcounts=Counter(); opt=[]
for s in range(1<<N):
    k=s.bit_count()
    if ordinary(s):ordc[k]+=1
    if rd(s):
        rdcounts[k]+=1
        if k==6:opt.append(s)
assert ordc[5]==18 and not any(ordc[k] for k in range(5))
assert len(opt)==207 and not any(rdcounts[k] for k in range(6))
assert sum(rdcounts.values())==sum(rd(s) for s in range(1<<N))

G=group()
seen=set(); orbit=[]
for s in opt:
    if s in seen:continue
    o={act(s,p) for p in G}; assert o<=set(opt)
    seen|=o
    in_e=sum((adj[i]&s).bit_count() for i in range(N) if s>>i&1)//2
    orbit.append((len(o),s,in_e))
assert seen==set(opt)
assert sorted(x[0] for x in orbit)==[9,18,18,54,108]

def exchange(slide):
    feasible=set(opt); graph={s:set() for s in opt}
    for s in opt:
        for u in range(N):
            if not s>>u&1:continue
            for v in range(N):
                if s>>v&1 or (slide and not adj[u]>>v&1):continue
                t=s^(1<<u)^(1<<v)
                if t in feasible:graph[s].add(t)
    assert all(s in graph[t] for t in graph for s in graph[t])
    degrees=Counter(len(v) for v in graph.values())
    comps=[]; unvisited=set(opt)
    while unvisited:
        q=[unvisited.pop()]; comp=set(q)
        while q:
            for t in graph[q.pop()]:
                if t not in comp:comp.add(t);unvisited.remove(t);q.append(t)
        comps.append(comp)
    ecc=Counter()
    for s in opt:
        d={s:0};q=deque([s])
        while q:
            x=q.popleft()
            for t in graph[x]:
                if t not in d:d[t]=d[x]+1;q.append(t)
        ecc[max(d.values())]+=1
    return len(set(opt)),sum(len(v) for v in graph.values())//2,sorted((len(c) for c in comps)),dict(sorted(degrees.items())),dict(sorted(ecc.items()))

# no extra frontier work beyond the once-per-root BFS
assert exchange(False)==(207,432,[1]*27+[180],{0:27,4:108,6:72},{0:27,6:180})
assert exchange(True)==(207,324,[1]*27+[180],{0:27,2:108,6:72},{0:27,8:180})
print('ordinary size 5:',ordc[5],'; restrained minimum: 6; optimal sets:',len(opt))
print('all restrained cardinalities:',sorted(rdcounts.items()))
print('minimum orbits (size, integer bit mask, induced edges):',sorted(orbit))
print('token jumping:',exchange(False))
print('token sliding:',exchange(True))
print('PASS')

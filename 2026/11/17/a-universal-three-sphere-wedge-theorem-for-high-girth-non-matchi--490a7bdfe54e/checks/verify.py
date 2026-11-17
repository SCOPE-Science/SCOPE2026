#!/usr/bin/env python3
"""Finite independent checks for the high-girth three-nonmatching theorem.
Python 3, standard library only. A finite test does not replace the general proof.
"""
from itertools import combinations
from collections import defaultdict, deque

def cycle(n): return [(i, (i+1)%n) for i in range(n)]
def theta3():
    return [(u,v) for j in range(3) for u,v in [(0,2+2*j),(2+2*j,3+2*j),(3+2*j,1)]]
def bouquet():
    return cycle(6)+[(0,6),(6,7),(7,8),(8,9),(9,10),(10,0)]
def linked():
    return cycle(6)+[(6,7),(7,8),(8,9),(9,10),(10,11),(11,6),(0,6)]
def normal(edges):return sorted(set(tuple(sorted(e)) for e in edges))

def maximum_matching_under3(edges):
    if any(len(set(x for j in triple for x in edges[j]))==6 for triple in combinations(range(len(edges)),3)): return False
    return True

def faces(edges):
    m=len(edges)
    forbidden=[sum(1<<i for i in a) for a in combinations(range(m),3) if len(set(x for j in a for x in edges[j]))==6]
    return {s for s in range(1<<m) if not any((s&f)==f for f in forbidden)}

def cover2(F,edges,vs):
    if not F:return True
    for a in vs:
        for b in vs:
            if a>b:continue
            if all(a in edges[i] or b in edges[i] for i in F):return True
    return False

def girth6(edges):
    vertices=sorted(set(z for e in edges for z in e))
    adj={v:set() for v in vertices}
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    for a,b in edges:
        seen={a};q=deque([(a,0)])
        while q:
            v,d=q.popleft()
            if v==b:
                if d<5:return False
                break
            for w in adj[v]:
                if {v,w}=={a,b}: continue
                if w not in seen:seen.add(w);q.append((w,d+1))
    return True

def mod2_betti(F,m):
    bydim=defaultdict(list)
    for s in F:
        if s:bydim[s.bit_count()-1].append(s)
    ranks={}
    for d in range(1,max(bydim)+1):
        lower={s:i for i,s in enumerate(bydim[d-1])}
        piv={}
        for s in bydim[d]:
            col=0
            for i in range(m):
                if s>>i&1:col^=1<<lower[s^(1<<i)]
            while col:
                j=col.bit_length()-1
                if j in piv:col^=piv[j]
                else:piv[j]=col;break
        ranks[d]=len(piv)
    betti={d:len(ss)-ranks.get(d,0)-ranks.get(d+1,0) for d,ss in bydim.items()}
    betti[0]-=1
    return {d:v for d,v in betti.items() if v}

def tree_and_chords(edges):
    vs=sorted(set(x for e in edges for x in e));adj={v:[] for v in vs}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    reached={vs[0]};q=deque([vs[0]]);T=[]
    while q:
        a=q.popleft()
        for b in sorted(adj[a]):
            if b not in reached:reached.add(b);T.append(tuple(sorted((a,b))));q.append(b)
    assert len(T)==len(vs)-1
    return normal(T),[e for e in edges if e not in T]

def check_link(H,e):
    a,b=e;E=normal(H);m=len(E);vs=sorted(set(x for z in E+[e] for x in z))
    F=faces(E)
    A={i for i,(x,y) in enumerate(E) if a in (x,y)}
    B={i for i,(x,y) in enumerate(E) if b in (x,y)}
    assert A and B and A.isdisjoint(B)
    link=set();Ka=set();Kb=set();N2=set();delta=set()
    for s in F:
        I=[i for i in range(m) if s>>i&1]
        pairwise=all(not set(E[i]).isdisjoint(E[j]) for i,j in combinations(I,2))
        if pairwise:N2.add(s)
        if set(I).issubset(A|B):delta.add(s)
        if any(cover2(I,E,[a,w]) for w in vs):Ka.add(s)
        if any(cover2(I,E,[b,w]) for w in vs):Kb.add(s)
        if maximum_matching_under3([E[i] for i in I]+[e]):link.add(s)
    assert link==Ka|Kb,(e,'link cover mismatch')
    assert Ka & Kb == N2 |delta,(e,'intersection mismatch')
    return len(F),len(link),len(Ka & Kb)

def check(name,edges):
    E=normal(edges);vs=sorted(set(x for e in E for x in e));m=len(E);b=m-len(vs)+1
    assert girth6(E),name
    F=faces(E)
    for s in F:
        I=[i for i in range(m) if s>>i&1]
        assert cover2(I,E,vs),name
    for s in range(1<<m):
        I=[i for i in range(m) if s>>i&1]
        if cover2(I,E,vs):assert s in F,name
    hom=mod2_betti(F,m)
    predicted={3:b*(b+1)//2} if b else {}
    assert hom==predicted,(name,hom,predicted)
    T,add=tree_and_chords(E)
    checks=[check_link(T+add[:i], e) for i,e in enumerate(add)]
    print(f'{name}: V={len(vs)} E={m} b={b} faces={len(F)} beta={hom} chord_link_checks={len(checks)}')

if __name__=='__main__':
    graphs=[('path8',[(i,i+1) for i in range(7)]),('cycle6',cycle(6)),('cycle7',cycle(7)),('cycle8',cycle(8)),('cycle9',cycle(9)),('cycle6_leaf',cycle(6)+[(0,6)]),('theta_3_3_3',theta3()),('bouquet_two_hexagons',bouquet()),('two_hexagons_bridge',linked())]
    for name,E in graphs:check(name,E)
    print('VERIFY_OK cases=%d'%len(graphs))

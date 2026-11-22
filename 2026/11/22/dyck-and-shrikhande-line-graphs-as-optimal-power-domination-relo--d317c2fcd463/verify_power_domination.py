#!/usr/bin/env python3
"""Exhaustive verification of the Shrikhande sensor relocation theorem.

Python >= 3.9, standard library only. Run alongside dyck_isomorphism.json.
"""
import json
from collections import Counter, deque
from itertools import combinations
from pathlib import Path

N=16
ALL=(1<<N)-1
S={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
C={(1,2),(3,2),(2,1),(2,3),(1,3),(3,1)}

def g_neighbors(kind):
    rows=[]
    for u in range(N):
        x,y=divmod(u,4)
        if kind=='shrikhande':
            rows.append(sum(1<<(4*((x+i)%4)+((y+j)%4)) for i,j in S))
        else:
            rows.append(sum(1<<(4*x+j) for j in range(4) if j!=y)+sum(1<<(4*i+y) for i in range(4) if i!=x))
    return rows

def observed(initial,A):
    seen=initial
    for u in range(N):
        if initial>>u&1: seen |= A[u]
    while True:
        update=seen
        for u in range(N):
            if seen>>u&1:
                unseen=A[u]&~seen
                if unseen!=0 and (unseen&(unseen-1))==0:
                    update|=unseen
        if update==seen:return seen
        seen=update

def distances(adj):
    spectrum=Counter()
    eccentricities=[]
    vertices=sorted(adj)
    for k,start in enumerate(vertices):
        q=deque([start]); ds={start:0}
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in ds:
                    ds[w]=ds[v]+1;q.append(w)
        assert len(ds)==len(adj)
        eccentricities.append(max(ds.values()))
        for w,d in ds.items():
            if start<w:spectrum[d]+=1
    return dict(sorted(spectrum.items())),min(eccentricities),max(eccentricities)

def make_adj(states,A,slide):
    good=set(states)
    adj={s:set() for s in states}
    for s in states:
        for u in range(N):
            if not (s>>u)&1:continue
            for v in range(N):
                if (s>>v)&1 or (slide and not (A[u]>>v)&1):continue
                t=s^(1<<u)^(1<<v)
                if t in good:adj[s].add(t)
    assert all(s in adj[t] for t in adj for s in adj[t])
    return adj

def dyck_lcf():
    E=set()
    for i in range(32):
        for j in ((i+1)%32,(i+[-13,5,-5,13][i%4])%32):
            E.add(tuple(sorted((i,j))))
    assert len(E)==48
    return E

def faces(A,pairs):
    result={};local={}
    good=set(pairs)
    for u in range(N):
        nbrs=[v for v in range(N) if (1<<u)|(1<<v) in good]
        assert len(nbrs)==6
        triangles=[]
        for c in combinations(nbrs,3):
            if all(A[x]>>y&1 for x,y in combinations(c,2)):
                triangles.append(c)
        triangles.sort()
        assert len(triangles)==2 and set(triangles[0]).isdisjoint(triangles[1])
        for j,tri in enumerate(triangles):
            result[(u,j)]=tri
            for v in tri:local[(u,v)]=(u,j)
    assert len(result)==32
    edges={frozenset((local[(u,v)],local[(v,u)])) for u,v in combinations(range(N),2) if ((1<<u)|(1<<v)) in good}
    assert len(edges)==48
    return result,edges,local

def main():
    A=g_neighbors('shrikhande');B=g_neighbors('rook')
    for M in (A,B):
        assert all(row.bit_count()==6 for row in M)
        assert all((M[u]&M[v]).bit_count()==2 for u in range(N) for v in range(u+1,N))
    assert all(observed(1<<u,A)!=ALL for u in range(N))
    pairs=[]
    for u,v in combinations(range(N),2):
        mask=(1<<u)|(1<<v)
        dx=((v//4)-(u//4))%4;dy=((v%4)-(u%4))%4
        yes=observed(mask,A)==ALL
        assert yes==((dx,dy) in C)
        if yes:pairs.append(mask)
    assert len(pairs)==48
    assert all(observed(1<<u,B)!=ALL for u in range(N))
    assert all(observed((1<<u)|(1<<v),B)!=ALL for u,v in combinations(range(N),2))
    rook3=sum(observed(sum(1<<u for u in c),B)==ALL for c in combinations(range(N),3))
    assert rook3==416
    jump=make_adj(pairs,A,slide=False)
    slide=make_adj(pairs,A,slide=True)
    assert set(map(len,jump.values()))=={10}
    assert set(map(len,slide.values()))=={4}
    assert sum(map(len,jump.values()))//2==240
    assert sum(map(len,slide.values()))//2==96
    jhist,jrad,jdiam=distances(jump)
    shist,srad,sdiam=distances(slide)
    assert (jhist,jrad,jdiam)==({1:240,2:696,3:192},3,3)
    assert (shist,srad,sdiam)==({1:96,2:192,3:336,4:384,5:120},5,5)
    f,E,local=faces(A,pairs)
    assert all(sum(x in edge for edge in E)==3 for x in f)
    # Each sensor state corresponds to the edge between its two local triangles.
    inverse={frozenset((local[(u,v)],local[(v,u)])):(1<<u)|(1<<v) for u,v in combinations(range(N),2) if ((1<<u)|(1<<v)) in set(pairs)}
    assert len(inverse)==48
    for s in pairs:
        for t in pairs:
            if s==t:continue
            e1=next(e for e,v in inverse.items() if v==s)
            e2=next(e for e,v in inverse.items() if v==t)
            assert (t in slide[s])==(len(e1&e2)==1)
    mapping=json.loads((Path(__file__).parent/'dyck_isomorphism.json').read_text(encoding='utf-8'))
    lookup={(r['u'],r['face_index']):r['dyck_index'] for r in mapping}
    assert len(lookup)==32 and set(lookup)==set(f) and set(lookup.values())==set(range(32))
    converted={tuple(sorted((lookup[x] for x in edge))) for edge in E}
    assert converted==dyck_lcf()
    print(json.dumps({'shrikhande_power_domination':2,'shrikhande_optimal_pairs':48,'rook_power_domination':3,'rook_optimal_triples':416,'shrikhande_jump':{'edges':240,'radius':jrad,'diameter':jdiam,'distance_pairs':jhist},'shrikhande_slide':{'edges':96,'radius':srad,'diameter':sdiam,'distance_pairs':shist},'dyck_isomorphism':'verified','local_triangle_vertices':32,'dyck_edges':48},sort_keys=True))
if __name__=='__main__':main()

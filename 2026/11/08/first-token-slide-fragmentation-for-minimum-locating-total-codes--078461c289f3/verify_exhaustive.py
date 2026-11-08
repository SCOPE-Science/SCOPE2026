#!/usr/bin/env python3
"""Exhaustive locating-total domination and exchange checker (standard library)."""
from itertools import combinations
from collections import Counter, deque
import json
from pathlib import Path

def adjacency(n):
    V = range(3*n)
    return [frozenset(w for w in V if w != v and (
        (w//3 == v//3) or (w%3 == v%3 and ((w//3-v//3)%n in (1,n-1)))))
        for v in V]

def valid(n, comb, neigh):
    S=set(comb)
    signatures=[neigh[v]&S for v in range(3*n)]
    return all(signatures) and len(set(map(frozenset,
        (signatures[v] for v in range(3*n) if v not in S))))==3*n-len(S)

def states(n, neigh):
    for k in range(3*n+1):
        ans=[sum(1<<v for v in tup) for tup in combinations(range(3*n),k)
            if valid(n,tup,neigh)]
        if ans:return k,ans
    raise RuntimeError('No total locating domination')

def edges(n, words, neigh, slide):
    st=set(words)
    E=set()
    for s in st:
        for a in range(3*n):
            if not (s>>a)&1:continue
            for b in range(3*n):
                if (s>>b)&1:continue
                if slide and b not in neigh[a]:continue
                t=s^(1<<a)^(1<<b)
                if t in st:E.add((min(s,t),max(s,t)))
    return sorted(E)

def components(words, E):
    adj={s:set() for s in words}
    for a,b in E:adj[a].add(b);adj[b].add(a)
    unseen=set(words);out=[]
    while unseen:
        root=min(unseen);todo=[root];unseen.remove(root);c=[]
        while todo:
            v=todo.pop();c.append(v)
            for w in adj[v]&unseen:unseen.remove(w);todo.append(w)
        out.append(sorted(c))
    return out,adj

def dist_stats(C,adj):
    if len(C)==1:return 0,0
    ecc=[]
    for start in C:
        Q=deque([start]);distance={start:0}
        while Q:
            a=Q.popleft()
            for b in adj[a]:
                if b not in distance:distance[b]=distance[a]+1;Q.append(b)
        assert len(distance)==len(C)
        ecc.append(max(distance.values()))
    return min(ecc),max(ecc)

def check_witness(n,states,es,cert):
    assert n==4
    verts=set(states)
    assert sorted(map(int,cert))==sorted(verts)
    mapped=[]
    for s in sorted(verts):
        obj=cert[str(s)]
        mapped.append((s,tuple(obj['coord']),obj['component'],obj['type']))
    for a,b in es:
        aa=cert[str(a)]; bb=cert[str(b)]
        assert aa['component']==bb['component']
        i,j=aa['coord'],bb['coord']
        if aa['type']=='C8':
            assert aa['type']==bb['type'] and (i[0]-j[0])%8 in (1,7)
        else:
            assert aa['type']==bb['type']=='C3xC6'
            assert (i[0]==j[0] and (i[1]-j[1])%6 in (1,5)) or (i[1]==j[1] and (i[0]-j[0])%3 in (1,2))
    groups={}
    for s in states:
        rec=cert[str(s)];groups.setdefault(rec['component'],[]).append(tuple(rec['coord']))
    for group,coord in groups.items():
        typ=cert[str(next(int(s) for s in cert if cert[s]['component']==group))]['type']
        if typ=='C8':assert len(coord)==8 and set(coord)=={(i,) for i in range(8)}
        else:assert len(coord)==18 and set(coord)=={(i,j) for i in range(3) for j in range(6)}
    assert len(es)==4*18*4//2+6*8*2//2
    print('coordinate_certificate: all 120 vertices and 192 slide edges matched')

if __name__=='__main__':
    for n in (3,4):
        nei=adjacency(n); k,ss=states(n,nei)
        E=edges(n,ss,nei,True);J=edges(n,ss,nei,False)
        co,adj=components(ss,E);cj,adj_j=components(ss,J)
        counts=Counter(map(len,co));types=Counter((len(c),len([e for e in E if e[0] in c]),*dist_stats(c,adj)) for c in co)
        print(f'n={n}, gamma={k}, states={len(ss)}, slide_edges={len(E)}, slide_component_sizes={sorted(counts.items())}, slide_component_types={sorted(types.items())}')
        print(f'n={n}, jump_edges={len(J)}, jump_components={len(cj)}, jump_radius_diameter={dist_stats(cj[0],adj_j) if len(cj)==1 else "disconnected"}')
        if n==3:
            assert (k,len(ss),len(E),len(co),len(J))==(4,81,198,1,522)
        else:
            assert (k,len(ss),len(E),len(J),sorted(counts.items()),len(cj))==(5,120,192,468,[(8,6),(18,4)],1)
            assert sorted(types.items())==[((8,8,4,4),6),((18,36,4,4),4)]
            cert=json.loads(Path(__file__).with_name('isomorphism_certificate.json').read_text())
            check_witness(n,ss,E,cert)
    print('ALL EXHAUSTIVE CHECKS PASS')

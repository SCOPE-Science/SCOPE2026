#!/usr/bin/env python3
"""Finite certificates for avalanche complexes on two directed pentagons.
Standard library only. Run: python verify.py
"""
from itertools import combinations
from collections import defaultdict, deque

N = 9
ARCS = {0: (1, 5), 1: (2,), 2: (3,), 3: (4,), 4: (0,),
        5: (6,), 6: (7,), 7: (8,), 8: (0,)}
# Tenacity of the exceptional 2-cell matching (0-based maximal-facet nerve indices).
EDGE_TRIANGLE = [
    ((5,6),(2,5,6)), ((0,7),(0,3,7)), ((1,4),(1,4,7)),
    ((2,7),(2,5,7)), ((6,7),(2,6,7)), ((1,5),(1,5,7)),
    ((1,6),(1,5,6)), ((3,6),(3,5,6)), ((3,5),(3,5,7)),
    ((0,6),(0,6,7)), ((4,7),(4,6,7)),
]

def firing_trace(h):
    assert 0 <= h <= 3
    c = [0] + [1]*8
    c[1] = 0
    c[5+h] = 0
    seen, firing = {}, []
    while tuple(c) not in seen:
        seen[tuple(c)] = len(firing)
        U = frozenset(v for v in range(N) if len(ARCS[v]) <= c[v])
        firing.append(U)
        nxt = c[:]
        for v in U:
            nxt[v] -= len(ARCS[v])
            for w in ARCS[v]:
                nxt[w] += 1
        assert sum(nxt) == 6 and min(nxt) >= 0
        c = nxt
        assert len(firing) <= 40, 'unexpected non-repetition'
    start = seen[tuple(c)]
    facets = sorted((tuple(sorted(s)) for s in set(firing) if s and
                     not any(s < t for t in firing)), key=lambda s: (len(s), s))
    # Chronological facet indexing is used for the exact Morse certificate.
    facets = [tuple(sorted(s)) for s in dict.fromkeys(firing) if s and not any(s < t for t in firing)]
    return start, len(firing), facets

def simplicial_faces(facets):
    return {tuple(comb) for facet in facets for k in range(1,len(facet)+1)
            for comb in combinations(facet,k)}

def nerve(facets):
    m=len(facets)
    return {q for k in range(1,m+1) for q in combinations(range(m),k)
            if set.intersection(*(set(facets[i]) for i in q))}

def free_collapse(faces):
    faces = set(faces); pairs = []
    while True:
        immediate = defaultdict(list)
        for f in faces:
            if len(f) <= 1: continue
            for j in range(len(f)):
                sub = f[:j] + f[j+1:]
                if sub in faces: immediate[sub].append(f)
        possibilities = [(co[0],sub) for sub,co in immediate.items() if len(co)==1]
        if not possibilities: break
        possibilities.sort(key=lambda z:(-len(z[0]),z[1],z[0]))
        high, low = possibilities[0]
        assert low in faces and high in faces
        faces.remove(low); faces.remove(high); pairs.append((low,high))
    return faces, pairs

def dag_on_hasse(faces,pairs):
    faces=set(faces); edges=set()
    for f in faces:
        for j in range(len(f)):
            sub=f[:j]+f[j+1:]
            if sub in faces: edges.add((f,sub))
    for low, high in pairs:
        assert low in faces and high in faces and (high,low) in edges
        edges.remove((high,low));edges.add((low,high))
    outgoing=defaultdict(list); indeg={f:0 for f in faces}
    for u,v in edges: outgoing[u].append(v);indeg[v]+=1
    todo=deque(sorted(f for f in faces if indeg[f]==0));n=0
    while todo:
        u=todo.popleft();n+=1
        for v in outgoing[u]:
            indeg[v]-=1
            if not indeg[v]:todo.append(v)
    return n==len(faces)

def reduced_mod2_betti(faces):
    groups={k: sorted(f for f in faces if len(f)==k+1) for k in range(0,max(map(len,faces)))}
    ranks={}
    for d in range(1,len(groups)):
        lower={f:i for i,f in enumerate(groups[d-1])}
        basis={}
        for f in groups[d]:
            col=0
            for j in range(len(f)):
                col ^= 1 << lower[f[:j]+f[j+1:]]
            while col:
                pivot=col.bit_length()-1
                if pivot not in basis:
                    basis[pivot]=col;break
                col ^= basis[pivot]
        ranks[d]=len(basis)
    return {d:len(arr)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)
            for d,arr in groups.items() if len(arr)-ranks.get(d,0)-ranks.get(d+1,0)-(d==0)}

def exceptional_morse(rem):
    edges={f for f in rem if len(f)==2}
    triangles={f for f in rem if len(f)==3}
    assert len(rem)==39 and len(edges)==18 and len(triangles)==13
    assert len(EDGE_TRIANGLE)==11
    assert len({e for e,t in EDGE_TRIANGLE})==11
    assert len({t for e,t in EDGE_TRIANGLE})==11
    assert all(e in edges and t in triangles and set(e)<set(t) for e,t in EDGE_TRIANGLE)
    tree=edges-{e for e,t in EDGE_TRIANGLE}
    assert len(tree)==7
    adj={v:[] for v in range(8)}
    for a,b in tree: adj[a].append(b);adj[b].append(a)
    parent={0:None};queue=deque([0])
    while queue:
        v=queue.popleft()
        for w in adj[v]:
            if w not in parent:
                parent[w]=v;queue.append(w)
    assert len(parent)==8
    vertex_pairs=[((v,), tuple(sorted((v,parent[v])))) for v in range(1,8)]
    pairs=EDGE_TRIANGLE+vertex_pairs
    assert dag_on_hasse(rem,pairs)
    critical=set(rem)-{x for p in pairs for x in p}
    assert len(critical)==3 and sorted(map(len,critical))==[1,3,3]
    return sorted(critical,key=lambda x:(len(x),x))

def main():
    expected={0:({1:1},5,20,7),1:({2:2},8,129,45),
              2:({},7,75,37),3:({},6,39,19)}
    for h in range(4):
        onset,T,facets=firing_trace(h)
        K=simplicial_faces(facets)
        Nrv=nerve(facets)
        rem,pairs=free_collapse(Nrv)
        b1=reduced_mod2_betti(K);b2=reduced_mod2_betti(Nrv)
        want,m,facecount,paircount=expected[h]
        assert b1==b2==want
        assert len(facets)==m and len(Nrv)==facecount and len(pairs)==paircount
        assert len(Nrv)==len(rem)+2*len(pairs)
        assert 2*len(pairs)+len(rem)==facecount
        if h==0:
            assert len(rem)==6 and reduced_mod2_betti(rem)=={1:1}
        elif h==1:
            critical=exceptional_morse(rem)
            assert len(critical)==3
        else:
            assert len(rem)==1
        print(f'shift={h} onset={onset} steps={T} facets={m} nerve_faces={facecount} '
              f'free_pairs={paircount} mod2_betti={b1} '
              f'remaining_faces={len(rem)}')
    print('PENTAGON_ROSE_PHASE_CLASSIFICATION_PASS')

if __name__=='__main__': main()

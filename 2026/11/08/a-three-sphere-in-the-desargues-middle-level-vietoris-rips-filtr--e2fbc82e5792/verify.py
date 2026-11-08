#!/usr/bin/env python3
"""Standalone exact combinatorial certificate for Desargues graph Rips complexes.
No external packages. Python >=3.9; execution: python verify_desargues.py
"""
from collections import Counter, deque
from itertools import combinations

N=20
edges=set()
for i in range(10):
    edges.add(tuple(sorted((i,(i+1)%10))))
    edges.add((i,i+10))
    edges.add(tuple(sorted((10+i,10+(i+3)%10))))
assert len(edges)==30
neighbors=[set() for _ in range(N)]
for a,b in edges:neighbors[a].add(b);neighbors[b].add(a)
assert all(len(a)==3 for a in neighbors)
D=[]
for x in range(N):
    d=[-1]*N;d[x]=0;todo=deque([x])
    while todo:
        a=todo.popleft()
        for b in neighbors[a]:
            if d[b]<0:d[b]=d[a]+1;todo.append(b)
    D.append(d)
assert all(D[i][j]==D[j][i] and D[i][i]==0 for i in range(N) for j in range(N))
shells=Counter(D[i][j] for i in range(N) for j in range(i+1,N))
assert shells=={1:30,2:60,3:60,4:30,5:10},shells
assert {i for i in range(N) for j in range(i+1,N) if D[i][j]==5 for i in (i,j)}==set(range(N))
assert all(sum(D[i][j]==5 for j in range(N))==1 for i in range(N))
# Independent exact metric model: the two middle ranks of the Boolean 5-cube.
LABELS = [
 (1,2),(1,2,3),(2,3),(2,3,4),(3,4),(3,4,5),
 (4,5),(1,4,5),(1,5),(1,2,5),(1,2,4),(1,3),
 (2,3,5),(2,4),(1,3,4),(3,5),(2,4,5),(1,4),
 (1,3,5),(2,5),
]
assert len(LABELS)==N and len(set(LABELS))==N
assert all(len(x) in (2,3) and set(x)<=set(range(1,6)) for x in LABELS)
assert all(D[i][j]==len(set(LABELS[i])^set(LABELS[j]))
           for i in range(N) for j in range(N))

def all_cliques(radius):
    faces=set()
    def visit(cur,options):
        if cur:faces.add(cur)
        for idx,v in enumerate(options):
            visit(cur+(v,),[w for w in options[idx+1:] if D[v][w]<=radius])
    visit((),list(range(N)))
    return faces

ORDER=[x for i in range(10) for x in (i,i+10)]
assert sorted(ORDER)==list(range(N))

def matching(faces):
    left=set(faces);pairs=[]
    for vertex in ORDER:
        take=[]
        for sigma in left:
            if vertex not in sigma:
                tau=tuple(sorted(sigma+(vertex,)))
                if tau in left:take.append((sigma,tau))
        for low,high in take:
            assert low in left and high in left and len(high)==len(low)+1
            assert set(high)-set(low)=={vertex}
            left.remove(low);left.remove(high)
        pairs.extend(take)
    assert len(faces)==len(left)+2*len(pairs)
    # Exhaustively certify the directed Hasse graph is acyclic.
    # Unmatched cover relations point high -> low, matched relations low -> high.
    reverse={pair for pair in pairs}
    adj={f:[] for f in faces}; indeg={f:0 for f in faces}
    for high in faces:
        if len(high)<2:continue
        for idx in range(len(high)):
            low=high[:idx]+high[idx+1:]
            if (low,high) in reverse:src,dst=low,high
            else:src,dst=high,low
            adj[src].append(dst);indeg[dst]+=1
    Q=deque(f for f in faces if indeg[f]==0);seen=0
    while Q:
        f=Q.popleft();seen+=1
        for nxt in adj[f]:
            indeg[nxt]-=1
            if indeg[nxt]==0:Q.append(nxt)
    assert seen==len(faces),(seen,len(faces))
    return left,pairs

for r,expected_counts,expected_critical in (
    (2,[20,90,120,30],{0:1,2:19}),
    (3,[20,150,540,1000,960,450,80],{0:1,3:1}),
):
    faces=all_cliques(r)
    fc=Counter(len(s)-1 for s in faces)
    assert [fc[i] for i in range(len(expected_counts))]==expected_counts
    assert len(faces)==sum(expected_counts)
    crit,pairs=matching(faces)
    cc=Counter(len(s)-1 for s in crit)
    assert cc==expected_critical,(r,cc)
    assert len([x for x in crit if len(x)==1])==1
    assert sum(-1 if len(s)%2==0 else 1 for s in faces)==sum(-1 if len(s)%2==0 else 1 for s in crit)
    print(f'r={r}: faces={len(faces)} f={expected_counts} matched_pairs={len(pairs)} critical={dict(cc)} Hasse_DAG=PASS')
print('distance_shells=',sorted(shells.items()))
print('scale_4: ten disjoint missing edges -> tenfold join of S^0 -> S^9')
print('scale_5: full simplex')
print('VERIFY_OK')

"""Reproduce integral homology of the geodesic general-position complex of G(8,3).

Run as: python check.py
Requires only Python >=3.9 and the adjacent collapses.json.
The finite proof checks a complete face enumeration, 227 actual elementary
collapses, signed chain-boundary identities and unimodular pivot ranks.
"""
import json
from collections import Counter, deque
from itertools import combinations
from pathlib import Path

N = 8
V = 2*N
edges = set()

def edge(a,b):
    assert a!=b
    edges.add(tuple(sorted((a,b))))

for i in range(N):
    edge(i, (i+1)%N)       # outer cycle
    edge(i, N+i)           # spoke
    edge(N+i, N+(i+3)%N)   # inner star
assert len(edges)==24
adj = [set() for _ in range(V)]
for a,b in edges:
    adj[a].add(b)
    adj[b].add(a)
assert all(len(x)==3 for x in adj)

def bfs(start):
    d = [V+1]*V
    d[start]=0
    q=deque([start])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if d[b]==V+1:
                d[b]=d[a]+1
                q.append(b)
    return d

dist = [bfs(x) for x in range(V)]
# Independent all-pairs shortest-path calculation, including every pair.
fw = [[0 if i==j else 1 if j in adj[i] else V+1 for j in range(V)] for i in range(V)]
for k in range(V):
    for i in range(V):
        for j in range(V):
            fw[i][j] = min(fw[i][j], fw[i][k]+fw[k][j])
assert fw == dist
assert max(max(x) for x in dist)==4

forbidden = set()
for a,b,c in combinations(range(V),3):
    if (dist[a][b]+dist[b][c]==dist[a][c]
        or dist[a][c]+dist[c][b]==dist[a][b]
        or dist[b][a]+dist[a][c]==dist[b][c]):
        forbidden.add((1<<a)|(1<<b)|(1<<c))
assert len(forbidden)==336
faces = {x for x in range(1,1<<V) if all(x&t != t for t in forbidden)}
assert Counter(x.bit_count() for x in faces) == {1:16,2:120,3:224,4:220,5:80}
# Independent admissibility test on every enumerated face.
for x in faces:
    vertices=[a for a in range(V) if x>>a&1]
    assert all(not (dist[a][b]+dist[b][c]==dist[a][c]
                    or dist[a][c]+dist[c][b]==dist[a][b]
                    or dist[b][a]+dist[a][c]==dist[b][c])
               for a,b,c in combinations(vertices,3))

cert=json.loads(Path(__file__).with_name('collapses.json').read_text(encoding='utf-8'))
assert cert['format']=='codimension-one-free-face-collapse-sequence'
assert cert['vertex_order']=='u0..u7,v0..v7'
pairs=cert['pairs']
assert len(pairs)==227
pair_count=Counter()
for x,y in pairs:
    assert x in faces and y in faces and x!=y
    assert y.bit_count()==x.bit_count()+1
    assert y&x==x
    # A free face has exactly one immediate coface in a downward-closed complex.
    cofaces=[x|(1<<j) for j in range(V) if not (x>>j)&1 and (x|(1<<j)) in faces]
    assert cofaces==[y]
    pair_count[x.bit_count()-1]+=1
    faces.remove(x)
    faces.remove(y)
assert pair_count=={1:35,2:112,3:80}
assert Counter(x.bit_count() for x in faces)=={1:16,2:85,3:77,4:28}
# Check remaining set is indeed an abstract simplicial complex.
for x in faces:
    for j in range(V):
        if x>>j&1:
            assert x^(1<<j) in faces or x.bit_count()==1

bydim={d:sorted(x for x in faces if x.bit_count()==d+1) for d in range(4)}

def boundary(dim):
    index={x:i for i,x in enumerate(bydim[dim-1])}
    out=[[0]*len(bydim[dim]) for _ in index]
    for j,x in enumerate(bydim[dim]):
        for place,v in enumerate(k for k in range(V) if x>>k&1):
            out[index[x^(1<<v)]][j] = -1 if place%2 else 1
    return out

D={d:boundary(d) for d in (1,2,3)}
for d in (2,3):
    A,B=D[d-1],D[d]
    for i in range(len(A)):
        for j in range(len(B[0])):
            assert sum(A[i][k]*B[k][j] for k in range(len(B)))==0

def unit_smith_rank(A):
    """Unimodular row/column operations using unit (±1) pivots only.
    If the leftover block is zero, every nonzero Smith invariant factor is one.
    """
    a=[list(row) for row in A]
    nr,nc=len(a),len(a[0]) if a else 0
    rank=0
    while rank<min(nr,nc):
        p=next(((i,j) for i in range(rank,nr)
                for j in range(rank,nc) if abs(a[i][j])==1),None)
        if p is None:
            assert all(a[i][j]==0 for i in range(rank,nr) for j in range(rank,nc)), 'nonunit remainder'
            break
        i,j=p
        a[rank],a[i]=a[i],a[rank]
        for row in a:
            row[rank],row[j]=row[j],row[rank]
        pivot=a[rank][rank]
        assert abs(pivot)==1
        for i in range(rank+1,nr):
            v=a[i][rank]
            if v:
                for j in range(rank,nc):
                    a[i][j]-=v*pivot*a[rank][j]
        for j in range(rank+1,nc):
            v=a[rank][j]
            if v:
                for i in range(rank,nr):
                    a[i][j]-=v*pivot*a[i][rank]
        rank+=1
    return rank

ranks={d:unit_smith_rank(D[d]) for d in (1,2,3)}
assert ranks=={1:15,2:46,3:27}
betti={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in range(4)}
assert betti=={0:0,1:24,2:4,3:1}
assert sum((-1)**d*len(bydim[d]) for d in range(4))==-20
print('PASS: forbidden triples 336, face vector (16,120,224,220,80)')
print('PASS: 227 genuine free-face collapses; remaining vector (16,85,77,28)')
print('PASS: signed boundary squared zero; unimodular ranks (15,46,27)')
print('PASS: all nonzero integral Smith factors equal 1; reduced Betti ranks (0,24,4,1)')

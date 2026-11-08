"""Reconstruct and check the graph-metric radius-two Desargues complex.
Requires Python 3.9+ standard library only.  No external data files.
"""
from collections import deque
from itertools import combinations

V=range(20)
edges=set()
def edge(u,v):
    if u==v: raise AssertionError('loop')
    edges.add(tuple(sorted((u,v))))
for j in range(10):
    edge(j,(j+1)%10)
    edge(j,j+10)
    edge(j+10,10+(j+3)%10)
assert len(edges)==30
N=[set() for _ in V]
for u,v in edges:N[u].add(v);N[v].add(u)
assert all(len(n)==3 for n in N)
d=[]
for start in V:
    dist={start:0};q=deque([start])
    while q:
        u=q.popleft()
        for v in N[u]:
            if v not in dist:dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==20
    d.append(dist)
assert min(d[i][j] for i in V for j in V if i!=j and (i,j) not in edges and (j,i) not in edges)==2
R={tuple(sorted((u,v))) for u,v in combinations(V,2) if d[u][v]<=2}
assert len(R)==90
simplices={ (v,) for v in V }
simplices.update(R)
tris={x for x in combinations(V,3) if all(tuple(sorted(p)) in R for p in combinations(x,2))}
simplices.update(tris)
tetras={x for x in combinations(V,4) if all(tuple(sorted(p)) in R for p in combinations(x,2))}
simplices.update(tetras)
assert not any(all(tuple(sorted(p)) in R for p in combinations(x,2)) for x in combinations(V,5))
assert tuple(sum(len(f)==k for f in simplices) for k in range(1,5))==(20,90,120,30)
# Greedy elementary collapses of every tetrahedron along a free triangular face.
pairs=[]
while any(len(f)==4 for f in simplices):
    uppers=sorted(f for f in simplices if len(f)==4)
    incidence={}
    for f in uppers:
        for t in combinations(f,3):incidence.setdefault(t,[]).append(f)
    free=sorted((t,fs[0]) for t,fs in incidence.items() if t in simplices and len(fs)==1)
    assert free,'missing free face'
    t,f=free[0]
    # Verify face is not contained in any other simplex of greater dimension.
    assert sum(set(t).issubset(g) for g in simplices if len(g)>len(t))==1
    simplices.remove(t);simplices.remove(f);pairs.append((t,f))
assert len(pairs)==30
assert tuple(sum(len(f)==k for f in simplices) for k in range(1,5))==(20,90,90,0)
# Independent integral Euler characteristic and mod-two chain calculation.
assert sum((-1)**(len(f)-1) for f in simplices)==20

def gf2_rank(cols):
    basis={}
    for col in cols:
        t=col
        while t:
            h=t.bit_length()-1
            if h not in basis:basis[h]=t;break
            t ^= basis[h]
    return len(basis)
verts=sorted(f for f in simplices if len(f)==1)
verts_idx={f:i for i,f in enumerate(verts)}
edges2=sorted(f for f in simplices if len(f)==2)
edges_idx={f:i for i,f in enumerate(edges2)}
tri2=sorted(f for f in simplices if len(f)==3)
rank1=gf2_rank([(1<<verts_idx[(a,)])^(1<<verts_idx[(b,)]) for a,b in edges2])
rank2=gf2_rank([sum((1<<edges_idx[e]) for e in combinations(t,2)) for t in tri2])
assert (rank1,rank2)==(19,71)
assert (len(edges2)-rank1-rank2,len(tri2)-rank2)==(0,19)
# Spanning tree of the residual one-skeleton. All triangles yield a presentation
# of its fundamental group with one generator for each non-tree edge.
parent=list(V)
def root(v):
    while parent[v]!=v:
        parent[v]=parent[parent[v]];v=parent[v]
    return v
T=set()
for a,b in edges2:
    ra,rb=root(a),root(b)
    if ra!=rb:parent[ra]=rb;T.add((a,b))
assert len(T)==19
non_tree=[e for e in edges2 if e not in T]
generator={e:i+1 for i,e in enumerate(non_tree)}
assert len(generator)==71

def reduce_word(word):
    stack=[]
    for x in word:
        if stack and stack[-1]==-x:stack.pop()
        else:stack.append(x)
    while len(stack)>1 and stack[0]==-stack[-1]:stack=stack[1:-1]
    return tuple(stack)
def letter(a,b):
    e=tuple(sorted((a,b)))
    k=generator.get(e,0)
    return (k if a<b else -k,) if k else ()
relators=[reduce_word(letter(a,b)+letter(b,c)+letter(c,a)) for a,b,c in tri2]
relators=[w for w in relators if w]
assert len(relators)==90

# Exact elementary Tietze eliminations: for a relation g^sign w=1 with g
# appearing exactly once, replace g by w^-1 or w, and delete that relation.
# Every substitution is a genuine presentation equivalence (not abelianization).
alive=set(generator.values())
eliminations=[]
while alive:
    possible=[]
    for j,w in enumerate(relators):
        counts={abs(a):sum(abs(b)==abs(a) for b in w) for a in w}
        for i,a in enumerate(w):
            if counts[abs(a)]==1:possible.append((len(w),j,i,a))
    assert possible,'cannot eliminate all fundamental-group generators'
    _,j,i,a=min(possible)
    w=relators[j];tail=w[i+1:]+w[:i]
    replacement=tuple(-x for x in reversed(tail)) if a>0 else tail
    k=abs(a)
    assert k in alive and all(abs(x)!=k for x in replacement)
    inv=tuple(-x for x in reversed(replacement))
    def substitute(w):
        out=[]
        for x in w:out.extend(replacement if x==k else inv if x==-k else (x,))
        return reduce_word(out)
    relators=[substitute(t) for m,t in enumerate(relators) if m!=j]
    relators=[t for t in relators if t]
    alive.remove(k);eliminations.append((k,a,w,replacement))
assert len(eliminations)==71 and len(relators)==0
# Since the 2-dimensional residual complex is simply connected and has free
# H_2 of rank 19, the standard 2-complex classification gives wedge^19 S^2.
print('DESARGUES_GRAPH_RIPS2_VERIFIED')
print('graph: 20 vertices 30 edges; Rips face vector (20,90,120,30)')
print('elementary collapse pairs:',len(pairs))
print('residual face vector: (20,90,90)')
print('boundary ranks mod 2:',rank1,rank2,'reduced Betti_1,Betti_2 = 0,19')
print('fundamental group: 71 exact Tietze eliminations; zero generators/relators remain')
print('Euler characteristic: 20; homotopy type: wedge of 19 two-spheres')

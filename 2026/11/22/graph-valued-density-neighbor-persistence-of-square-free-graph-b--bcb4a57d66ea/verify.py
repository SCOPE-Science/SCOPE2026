#!/usr/bin/env python3
"""Independent finite comparison for multineighbor filtrations of square-free graph blowups.
Uses only the Python standard library. Does not implement or assume the nerve proof.
"""
from itertools import combinations

def gf2_rank(vectors):
    piv={}
    for v in vectors:
        while v:
            k=v.bit_length()-1
            if k in piv:v^=piv[k]
            else:piv[k]=v;break
    return len(piv)

def complex_betti(facets):
    if not facets:return (0,0,0)
    faces={}
    for f in facets:
        for k in range(1,len(f)+1):
            faces.setdefault(k,set()).update(combinations(sorted(f),k))
    ranks={1:0}
    for k in range(2,max(faces)+1):
        rows={f:i for i,f in enumerate(sorted(faces.get(k-1,[])))}
        columns=[]
        for f in sorted(faces.get(k,[])):
            mask=0
            for j in range(k):mask^=(1<<rows[f[:j]+f[j+1:]])
            columns.append(mask)
        ranks[k]=gf2_rank(columns)
    out=[]
    for k in range(1,max(faces)+1):
        out.append(len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0))
    out[0]-=1
    return tuple((out+[0,0,0])[:3])

def independent_facets(adj,weights,m):
    n=len(adj); fibers=[]; N=sum(weights)
    s=0
    for w in weights:
        fibers.append(tuple(range(s,s+w)));s+=w
    neighbor_masks=[]
    for i in range(n):
        mask=sum((1<<z) for j in adj[i] for z in fibers[j])
        neighbor_masks.extend([mask]*weights[i])
    candidates=[]
    for mask in range(1,1<<N):
        if sum((mask&nm)==mask for nm in neighbor_masks)>=m:
            candidates.append(mask)
    # descending-cardinality maximality test, independent from proposed cover.
    facets=[]
    for mask in sorted(candidates,key=int.bit_count,reverse=True):
        if not any(mask&f==mask for f in facets):
            facets.append(mask)
    return [tuple(i for i in range(N) if f>>i&1) for f in facets]

def graph_betti(adj,weights,m):
    n=len(adj); s=[sum(weights[i] for i in adj[j]) for j in range(n)]
    verts=[('v',j) for j in range(n) if s[j]>=m]+[('e',i) for i in range(n) if weights[i]>=m and adj[i]]
    edges=[]
    for i in range(n):
        if weights[i]>=m:
            for j in adj[i]:
                assert s[j]>=m
                edges.append((('e',i),('v',j)))
    parent={a:a for a in verts}
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for a,b in edges:
        pa,pb=find(a),find(b)
        parent[pa]=pb
    c=len({find(x) for x in verts})
    return (max(c-1,0),len(edges)-len(verts)+c,0)

def square_free(adj):
    return all(len(adj[i]&adj[j])<2 for i in range(len(adj)) for j in range(i+1,len(adj)))

def connected(adj):
    seen={0}; frontier=[0]
    while frontier:
        a=frontier.pop()
        for b in adj[a]-seen:seen.add(b);frontier.append(b)
    return len(seen)==len(adj)

def adj_from_edges(n,edges):
    a=[set() for _ in range(n)]
    for i,j in edges:a[i].add(j);a[j].add(i)
    return a

def cycle(n):return adj_from_edges(n,[(i,(i+1)%n) for i in range(n)])

def petersen():
    return adj_from_edges(10,[(i,(i+1)%5) for i in range(5)]+[(i,i+5) for i in range(5)]+[(i+5,(i+2)%5+5) for i in range(5)])

def heawood():
    return adj_from_edges(14,[(i,7+((i+t)%7)) for i in range(7) for t in (0,1,3)])

n_cases=0;n_graphs=0

def check(adj,weights):
    global n_cases
    assert square_free(adj)
    for m in range(1,max(sum(weights[i] for i in adj[j]) for j in range(len(adj)))+2):
        b1=complex_betti(independent_facets(adj,weights,m))
        b2=graph_betti(adj,weights,m)
        assert b1==b2,(adj,weights,m,b1,b2)
        n_cases+=1

# All connected four-cycle-free labeled graphs up to five vertices.
for n in range(2,6):
    pairs=list(combinations(range(n),2))
    for b in range(1,1<<len(pairs)):
        A=adj_from_edges(n,[edge for k,edge in enumerate(pairs) if b>>k&1])
        if not connected(A) or not square_free(A):continue
        n_graphs+=1
        check(A,[1]*n)
        # Moderate heterogeneous weights, deterministic small test subset.
        if b%7==0:check(A,[1+i%2 for i in range(n)])
# Structural examples with nontrivial cycle rank and higher order.
for a,w in [(cycle(5),[1,2,1,2,2]),(cycle(6),[2,1,1,2,1,1]),(petersen(),[1]*10),(heawood(),[1]*14)]:
    check(a,w);n_graphs+=1
# Four-cycle obstruction: K_2,2 has two contractible N_1 components,
# whereas its bipartite double cover has two circle components.
C4=cycle(4)
assert complex_betti(independent_facets(C4,[1]*4,1))==(1,0,0)
assert graph_betti(C4,[1]*4,1)==(1,2,0)
print('PASS: graph instances =',n_graphs,'; independently enumerated filtered stages =',n_cases)
print('PASS: C4 counterexample: actual (H0~,H1)=(1,0), double cover gives (1,2)')

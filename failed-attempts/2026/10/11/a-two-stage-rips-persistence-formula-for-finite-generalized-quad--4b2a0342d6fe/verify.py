#!/usr/bin/env python3
"""Exact small-prime checks for metric Rips complexes of symplectic generalized quadrangles.

Independent finite corroboration of an all-order combinatorial proof.
Requires only Python's standard library.  Checks q=2 and q=3.
"""
from itertools import product,combinations
from collections import deque,Counter

def points(q):
    def norm(v):
        j=next(i for i,x in enumerate(v) if x)
        inv=pow(v[j],-1,q)
        return tuple(x*inv%q for x in v)
    return sorted({norm(v) for v in product(range(q),repeat=4) if any(v)})

def pair(a,b,q):
    return (a[0]*b[2]-a[2]*b[0]+a[1]*b[3]-a[3]*b[1])%q

def build(q):
    ps=points(q); pind={p:i for i,p in enumerate(ps)}
    ls=set()
    for i,j in combinations(range(len(ps)),2):
        u,v=ps[i],ps[j]
        if pair(u,v,q): continue
        members=[]
        for x in range(q):
            for y in range(q):
                if x==y==0:continue
                w=tuple((x*u[k]+y*v[k])%q for k in range(4))
                nidx=next(k for k,z in enumerate(w) if z)
                inv=pow(w[nidx],-1,q)
                members.append(pind[tuple(z*inv%q for z in w)])
        ls.add(tuple(sorted(set(members))))
    lines=sorted(ls)
    n=len(ps);m=len(lines)
    adj=[set() for _ in range(n+m)]
    for j,l in enumerate(lines):
        for i in l:
            adj[i].add(n+j);adj[n+j].add(i)
    return ps,lines,adj

def all_dist(adj):
    ds=[]
    for st in range(len(adj)):
        dist=[-1]*len(adj);dist[st]=0;todo=deque([st])
        while todo:
            x=todo.popleft()
            for y in adj[x]:
                if dist[y]<0: dist[y]=dist[x]+1;todo.append(y)
        assert min(dist)>=0
        ds.append(dist)
    return ds

def maximal_cliques(adj):
    out=[]
    def bk(R,P,X):
        if not P and not X:
            out.append(frozenset(R));return
        if P or X:
            pivot=max(P|X,key=lambda u:len(P&adj[u]))
            todo=sorted(P-adj[pivot])
        else:todo=[]
        for v in todo:
            bk(R|{v},P&adj[v],X&adj[v]);P.remove(v);X.add(v)
    bk(set(),set(range(len(adj))),set())
    return set(out)

def gf_rank(columns):
    piv={}
    for z in columns:
        while z:
            bit=z.bit_length()-1
            if bit in piv:z^=piv[bit]
            else:piv[bit]=z;break
    return len(piv)

def simplices(facets):
    layers={}
    for facet in facets:
        for k in range(1,len(facet)+1):
            layers.setdefault(k-1,set()).update(combinations(sorted(facet),k))
    return {k:sorted(v) for k,v in layers.items()}

def reduced_betti(facets):
    layers=simplices(facets); ranks={-1:1}
    for k in range(1,max(layers)+1):
        lower={f:i for i,f in enumerate(layers[k-1])}
        cols=[]
        for f in layers[k]:
            z=0
            for j in range(k+1):z^=1<<lower[f[:j]+f[j+1:]]
            cols.append(z)
        ranks[k-1]=gf_rank(cols)
    ranks[max(layers)]=0
    return {k:len(v)-ranks[k-1]-ranks[k] for k,v in layers.items()}, {k:len(v) for k,v in layers.items()}

def collapse_complex_to_graph(centers,adj,dist):
    n=len(adj)
    # Produce all simplices from proposed maximal closed stars and compare
    # against an independent Bron-Kerbosch clique enumeration of squared graph.
    stars={frozenset({v}|adj[v]) for v in centers}
    squared=[{j for j in range(n) if j!=i and dist[i][j]<=2} for i in range(n)]
    actual=maximal_cliques(squared)
    assert actual==stars,(len(actual),len(stars),actual-stars)
    faces=set()
    for s in stars:
        t=sorted(s)
        for k in range(1,len(t)+1):faces.update(frozenset(x) for x in combinations(t,k))
    steps=0
    for c in centers:
        for k in range(len(adj[c]),1,-1):
            for t in combinations(sorted(adj[c]),k):
                low=frozenset(t);high=low|{c}
                assert low in faces and high in faces
                # a free face has exactly one immediate coface
                cofaces=[x for x in range(n) if x not in low and (low|{x}) in faces]
                assert cofaces==[c],(c,t,cofaces)
                faces.remove(low);faces.remove(high);steps+=1
    remaining={frozenset({i}) for i in range(n)}|{frozenset({i,j}) for i in range(n) for j in adj[i] if i<j}
    assert faces==remaining,(len(faces),len(remaining))
    return steps

def verify(q):
    ps,lines,adj=build(q); n=len(ps);m=len(lines)
    assert n==m==(q+1)*(q*q+1)
    assert len(adj)==2*n
    assert all(len(A)==q+1 for A in adj)
    D=all_dist(adj)
    assert max(max(row) for row in D)==4
    assert all((D[i][j]%2==0)==((i<n)==(j<n)) for i in range(2*n) for j in range(2*n))
    assert all(D[i][j] in (1,3) for i in range(n) for j in range(n,2*n))
    assert all(D[i][j] in (2,4) for i,j in combinations(range(n),2))
    assert all(D[i][j] in (2,4) for i,j in combinations(range(n,2*n),2))
    # Independent clique-facet check for both homogeneous sides at scale 3.
    p_adj=[{j for j in range(n) if i!=j and D[i][j]==2} for i in range(n)]
    l_adj=[{j for j in range(n) if i!=j and D[n+i][n+j]==2} for i in range(n)]
    point_cliques=maximal_cliques(p_adj)
    line_cliques=maximal_cliques(l_adj)
    assert point_cliques=={frozenset(x) for x in lines}
    per_point={frozenset(j for j,L in enumerate(lines) if i in L) for i in range(n)}
    assert line_cliques==per_point
    bp, fp=reduced_betti(point_cliques)
    bl, fl=reduced_betti(line_cliques)
    b=(q*q)**2
    assert bp=={k:(b if k==1 else 0) for k in bp},bp
    assert bl==bp
    assert sum(len(x) for x in adj)//2 -(2*n)+1==b
    # VR2 exact simplicial collapse onto the incidence graph.
    steps=collapse_complex_to_graph(range(2*n),adj,D)
    # Scale 3 exactly a join, as its cross edges are complete and same-side
    # edges are precisely those in point/line collinearity graphs.
    for i in range(2*n):
        for j in range(i+1,2*n):
            expect = (i<n)!=(j<n) or (j in p_adj[i] if i<n else (j-n in l_adj[i-n]))
            assert (D[i][j]<=3)==expect
    print(f'order=({q},{q}) points={n} lines={m} incidence_edges={len(adj)*(q+1)//2} beta1={b} predicted_beta3={b*b} scale2_collapse_pairs={steps} point_faces={fp} point_betti={bp} line_betti={bl}')

if __name__=='__main__':
    for q in (2,3): verify(q)
    print('VERIFY_OK primes=2,3 scale2_relative_collapses=yes scale3_join=yes')

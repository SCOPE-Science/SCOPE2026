#!/usr/bin/env python3
"""Finite exact tests for scale-two Rips complexes of hexagonal torus graphs."""
from itertools import combinations
from collections import deque
from math import comb

def torus_graph(L):
    # two colors, black B(i,j)=2*(i*L+j), white W(i,j)=2*(i*L+j)+1
    edges=set()
    for i in range(L):
      for j in range(L):
        b=2*(i*L+j)
        for u,v in ((i,j),((i-1)%L,j),(i,(j-1)%L)):
          w=2*(u*L+v)+1
          edges.add(tuple(sorted((b,w))))
    V=2*L*L
    adj=[set() for _ in range(V)]
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    return adj,edges

def rips(L):
    adj, orig=torus_graph(L)
    V=len(adj)
    d2=[set(x) for x in adj]
    for v in range(V):
      for y in adj[v]:d2[v].update(adj[y])
      d2[v].discard(v)
    e2=set((i,j) for i in range(V) for j in d2[i] if j>i)
    tris=set()
    for a,b in e2:
      for c in d2[a]&d2[b]:
        if c>b:tris.add((a,b,c))
    tetras=set()
    for a,b,c in tris:
      for d in d2[a]&d2[b]&d2[c]:
        if d>c:tetras.add((a,b,c,d))
    return adj, orig, e2, tris, tetras

def rank_mod2(cols):
    pivots={}
    for x in cols:
      while x:
        k=x.bit_length()-1
        if k not in pivots:
          pivots[k]=x;break
        x ^= pivots[k]
    return len(pivots)

def check(L):
    adj, orig, edges, tris, tetras=rips(L)
    v=len(adj)
    assert len(orig)==3*L*L and all(len(x)==3 for x in adj)
    # local tetrahedra and two extra triangles for each hexagonal face
    stars={tuple(sorted([c,*adj[c]])) for c in range(v)}
    assert tetras==stars
    star_tris={tuple(sorted(t)) for s in stars for t in combinations(s,3)}
    extra=tris-star_tris
    assert len(extra)==2*L*L and len(tris)==10*L*L
    assert all(all(u%2==s[0]%2 for u in s) for s in extra)
    assert len(edges)==9*L*L
    # enumerate hexagonal face boundaries as nonstar triples: alternate triangles in either color
    faces={}
    for tri in extra:
      between=[next(iter(adj[u]&adj[w])) for u,w in ((tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0]))]
      assert len(set(between))==3
      hexa=tuple(sorted((*tri,*between)))
      faces.setdefault(hexa, []).append(tri)
    assert len(faces)==L*L and all(len(x)==2 for x in faces.values())
    # Every graph edge borders precisely two six-cycle face boundaries,
    # so the edge-disjoint-hexagons classification does NOT apply.
    border={e:0 for e in orig}
    for hexa,alternating in faces.items():
      hexa_set=set(hexa)
      edge_face={e for e in orig if e[0] in hexa_set and e[1] in hexa_set}
      assert len(edge_face)==6,(L,hexa,len(edge_face))
      for e in edge_face:border[e]+=1
    assert all(x==2 for x in border.values())
    # all fundamental six-cycles are face boundaries (local-geometric check)
    # check that all pairwise distance-two tris not in stars are exactly these triangles
    assert len(tris)==4*v+2*L*L
    # exact chain ranks mod 2
    edge_idx={e:i for i,e in enumerate(sorted(edges))}
    tri_idx={t:i for i,t in enumerate(sorted(tris))}
    d2=[]
    for t in sorted(tris):
      d2.append(sum(1 << edge_idx[p] for p in combinations(t,2)))
    d3=[]
    for q in sorted(tetras):
      d3.append(sum(1 << tri_idx[p] for p in combinations(q,3)))
    r2=rank_mod2(d2); r3=rank_mod2(d3)
    b1=len(edges)-(v-1)-r2
    b2=len(tris)-r2-r3
    b3=len(tetras)-r3
    assert (r2,r3)==(len(edges)-v-1,len(tetras)),(L,r2,r3)
    assert (b1,b2,b3)==(2,L*L+1,0),(L,b1,b2,b3)
    # signed alternating Euler check
    assert v-len(edges)+len(tris)-len(tetras)==L*L
    print(f'L={L} f=({v},{len(edges)},{len(tris)},{len(tetras)}) face={len(faces)} extra={len(extra)} mod2_b1={b1} mod2_b2={b2} mod2_b3={b3}')

if __name__=='__main__':
    for L in (5,6,7,8):check(L)
    print('HONEYCOMB_TORUS_RIPS2_FINITE_CHECKS_OK')

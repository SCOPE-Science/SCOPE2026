#!/usr/bin/env python3
"""Verify an explicit finite contact coloring; relies on standard Python only.
Run: python verify_torus_coloring.py certificate_5x5.json
The cited general edge-coloring theorems, not this finite program, prove all-order claims.
"""
import json, sys, collections

def check(data):
    m, n = data['m'], data['n']
    assert (m,n)==(5,5) and data['directions']==[[1,0],[0,1],[1,-1]]
    assert len(data['pairs'])==m*n
    P=[(i,j) for i in range(m) for j in range(n)]
    shift=lambda p,d:((p[0]+d[0])%m,(p[1]+d[1])%n)
    # Original triangular-lattice edges and their colored incident cells.
    edges, col=[], []
    for k,p in enumerate(P):
        assert len(data['pairs'][k])==3
        for idx,d in enumerate(data['directions']):
            q=shift(p,d); e=frozenset((p,q))
            assert len(e)==2
            a,b=data['pairs'][k][idx]
            assert isinstance(a,int) and isinstance(b,int) and 0<=a<13 and 0<=b<13 and a!=b
            edges.append(e); col.append((a,b))
    assert len(edges)==3*m*n and len(set(edges))==3*m*n
    # Each original vertex has 12 incident small triangles. No two may share color.
    for p in P:
        seen=[]
        for e,c in zip(edges,col):
            if p in e: seen.extend(c)
        assert len(seen)==12 and len(set(seen))==12,(p,seen)
    # List all equilateral triangular faces, including across the torus seam.
    faces=[]
    for p in P:
        i,j=p
        faces += [frozenset([p,shift(p,(1,0)),shift(p,(0,1))]),
                  frozenset([shift(p,(1,0)),shift(p,(0,1)),shift(p,(1,1))])]
    assert len(faces)==2*m*n and len(set(faces))==2*m*n
    tiles=[[] for _ in faces]
    for e,c in zip(edges,col):
        adjacent=[t for t,f in enumerate(faces) if e.issubset(f)]
        assert len(adjacent)==2, (e,adjacent)
        for color,t in zip(c,adjacent):tiles[t].append((e,color))
    assert all(len(t)==3 and len({k for _,k in t})==3 for t in tiles)
    alltiles=[]
    for f,t in zip(faces,tiles):
        for edge,color in t:
            alltiles.append((edge,f,color))
    assert len(alltiles)==6*m*n
    # Two distinct cells touch iff a shared old vertex or a shared face-center.
    deg=collections.Counter()
    for i,(e,f,c) in enumerate(alltiles):
        for j,(e2,f2,c2) in enumerate(alltiles[:i]):
            if e.intersection(e2) or f==f2:
                assert c!=c2, (i,j,c,e,f,c2,e2,f2)
                deg[i]+=1;deg[j]+=1
    assert len(deg)==6*m*n and set(deg.values())=={21},collections.Counter(deg.values())
    assert sum(deg.values())//2 == 1575
    counts=collections.Counter(c for _,_,c in alltiles)
    assert set(counts)==set(range(13)) and sum(counts.values())==150
    print('PASS: 25 original vertices, 75 edges, 50 faces, 150 small triangles, 13 colors, all 21 contacts per triangle properly colored')
    print('Color-class sizes: '+str(sorted(counts.values())))
    print('PASS: odd-order lower bound: each of 12 alleged classes would cover 25 original vertices in pairs, impossible')

if __name__=='__main__':
    p=sys.argv[1] if len(sys.argv)>1 else 'certificate_5x5.json'
    check(json.load(open(p,encoding='utf-8')))

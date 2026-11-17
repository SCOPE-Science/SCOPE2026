#!/usr/bin/env python3
"""Independent finite verification for a scale-three Hamming Rips fixed-point theorem.

No external packages required. The infinite-dimensional theorem uses the separate
mathematical proof; these computations corroborate its finite orbit model.
"""
from itertools import combinations
import json

def cube_squares(m):
    for i, j in combinations(range(m), 2):
        for base in range(1 << m):
            if base & ((1 << i) | (1 << j)):
                continue
            yield (base, base ^ (1 << i), base ^ (1 << j), base ^ (1 << i) ^ (1 << j))

def orbit_graph(m):
    # Two orbits above each base cube vertex, represented by a first-two-bit
    # parity label a=0 or a=1. An orbit is { (a,0,y), (a^1,1,y) }.
    n=m+2
    vertices=[(a,y) for a in range(2) for y in range(1 << m)]
    idx={z:i for i,z in enumerate(vertices)}
    def elements(a,y):
        return ((a<<1)|y<<2, ((a^1)<<1)|1|(y<<2))
    edges=set()
    for z,w in combinations(vertices,2):
        actual=all((u^v).bit_count() <= 3 for u in elements(*z) for v in elements(*w))
        a,x=z; b,y=w; d=(x^y).bit_count()
        predicted=(d<=1 if a==b else d<=2)
        assert actual==predicted,(n,z,w,actual,predicted)
        if actual:edges.add(tuple(sorted((idx[z],idx[w]))))
    return vertices,edges

def flag_faces(vcount,edges):
    adjacency=[set() for _ in range(vcount)]
    for a,b in edges:
        adjacency[a].add(b);adjacency[b].add(a)
    faces={}
    def grow(prefix,candidates):
        if prefix: faces[prefix]=len(prefix)
        for x in sorted(candidates):
            grow(prefix+(x,), {y for y in candidates if y>x and y in adjacency[x]})
    grow((),set(range(vcount)))
    return faces

def square_faces(m):
    f={}
    if m<2:return f
    for square in cube_squares(m):
        for av in range(3):
            for bv in range(3):
                if av+bv == 0:continue
                for aa in combinations(square,av):
                    if av==2 and (aa[0]^aa[1]).bit_count()!=1:continue
                    for bb in combinations(square,bv):
                        if bv==2 and (bb[0]^bb[1]).bit_count()!=1:continue
                        # A vertices 0..2^m-1, B vertices 2^m..2^(m+1)-1.
                        f[tuple(sorted(aa+tuple(x+(1<<m) for x in bb)))]=av+bv
    return f

def rank_mod2(cols):
    pivots={}
    for col in cols:
        while col:
            k=col.bit_length()-1
            if k not in pivots:
                pivots[k]=col
                break
            col^=pivots[k]
    return len(pivots)

def betti_mod2(faces):
    by={j:[] for j in range(1,max(faces.values(),default=0)+1)}
    for s,k in faces.items():by[k].append(s)
    ranks={0:0,1:0}
    for k in sorted(by)[1:]:
        rowmap={s:i for i,s in enumerate(by[k-1])}
        columns=[]
        for s in by[k]:
            column=0
            for j in range(k):column^=1<<rowmap[s[:j]+s[j+1:]]
            columns.append(column)
        ranks[k]=rank_mod2(columns)
    return [len(by[k])-ranks[k]-ranks.get(k+1,0)-(1 if k==1 else 0) for k in sorted(by)], {k:len(v) for k,v in by.items()}

def expected(m):
    if m<=1:return [0,0,0,0]
    return [0,0,(2**(m-3)*(m*m-5*m+8)-1 if m>=3 else 0),m*(m-1)//2 * 2**(m-2)]

def main():
    results=[]
    for m in range(7):
        vertices,edges=orbit_graph(m)
        faces=flag_faces(len(vertices),edges)
        if m>=2:
            sf=square_faces(m)
            assert faces==sf,(m,len(faces),len(sf),len(faces.keys()-sf.keys()),len(sf.keys()-faces.keys()))
        betti,counts=betti_mod2(faces)
        exp=expected(m)
        assert betti==exp[:len(betti)],(m,betti,exp)
        if m>=2:
            fs={1:1<<(m+1), 2:(1<<m)*(m+1)*(m+2)//2,
                3:(1<<m)*2*m*m,4:m*(3*m-2)*(1<<(m-1))}
            assert counts==fs,(m,counts,fs)
        results.append({'n':m+2,'m':m,'orbit_vertices':len(vertices),
                        'compatible_pairs':len(edges),'faces':sum(counts.values()),
                        'face_counts':counts,'reduced_mod2_betti':betti,
                        'predicted_rank_H2':exp[2],'predicted_rank_H3':exp[3]})
    print(json.dumps({'status':'WEIGHT_TWO_FIXED_SPACE_CHECKS_OK',
                      'method':'complete direct pair orbit checks, independent clique enumeration, square block enumeration, exact GF(2) boundary ranks',
                      'parameters':results},ensure_ascii=False,indent=2))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Exact integral certificate for disjoint-cycle three-tori on GP(10,2).
Requires only Python 3 standard library. Run: python3 verify.py
"""
from itertools import combinations, product
from collections import Counter, defaultdict
from fractions import Fraction


def graph():
    es=set()
    for i in range(10):
        es.add(tuple(sorted((i,(i+1)%10))))
        es.add(tuple(sorted((i,10+i))))
        es.add(tuple(sorted((10+i,10+(i+2)%10))))
    edges=sorted(es)
    adj={v:set() for v in range(20)}
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    assert len(edges)==30 and all(len(x)==3 for x in adj.values())
    return edges,{v:sorted(s) for v,s in adj.items()}


def cycles_of(adj):
    # Unoriented simple cycles, each recorded from its least vertex,
    # with smaller second than last vertex; exhaustiveness by DFS.
    cycles=[]
    def explore(root,path,seen):
        for w in adj[path[-1]]:
            if w==root and len(path)>=3:
                if path[1]<path[-1]:cycles.append(tuple(path))
            elif w>root and w not in seen:
                explore(root,path+[w],seen|{w})
    for root in sorted(adj):explore(root,[root],{root})
    return cycles


def torus_vector(t,cycles,loc,index3):
    d=defaultdict(int)
    for choices in product(*(loc[i].items() for i in t)):
        vertices=[v for v,_ in choices]
        order=sorted(range(3),key=lambda k:vertices[k])
        inversions=sum(order[i]>order[j] for i in range(3) for j in range(i+1,3))
        sign=-1 if inversions%2 else 1
        ordered_vertices=tuple(sorted(vertices))
        for local_terms in product(*(x for _,x in choices)):
            g=[term[0] for term in local_terms]
            coeff=sign
            for _,a in local_terms:coeff*=a
            bits=4*g[order[0]]+2*g[order[1]]+g[order[2]]
            d[index3[(ordered_vertices,bits)]]+=coeff
    return {r:a for r,a in d.items() if a}


def rank2_and_rows(vectors):
    basis={}
    accepted=[]
    for i,vec in enumerate(vectors):
        z=0
        for r,c in vec.items():
            if c%2:z^=1<<r
        while z:
            r=(z&-z).bit_length()-1
            if r not in basis:
                basis[r]=z
                accepted.append(i)
                break
            z^=basis[r]
    return sorted(basis),accepted


def determinant(matrix):
    # Fraction-free Bareiss elimination, with exact divisions.
    n=len(matrix)
    a=[list(map(int,row)) for row in matrix]
    if n==0:return 1
    last=1;sign=1
    for k in range(n-1):
        if a[k][k]==0:
            next_row=next((i for i in range(k+1,n) if a[i][k]),None)
            if next_row is None:return 0
            a[k],a[next_row]=a[next_row],a[k]
            sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%last==0
                a[i][j]=num//last
            a[i][k]=0
        last=pivot
    return sign*a[-1][-1]


def inverse(matrix):
    n=len(matrix)
    a=[[Fraction(v) for v in row]+[Fraction(int(i==j)) for j in range(n)]
       for i,row in enumerate(matrix)]
    for j in range(n):
        i=next(i for i in range(j,n) if a[i][j])
        a[j],a[i]=a[i],a[j]
        p=a[j][j]
        a[j]=[v/p for v in a[j]]
        for i in range(n):
            if i==j:continue
            q=a[i][j]
            if q:a[i]=[v-q*w for v,w in zip(a[i],a[j])]
    return [row[n:] for row in a]


def main():
    edges,adj=graph()
    ei={e:i for i,e in enumerate(edges)}
    incident={v:sorted(ei[tuple(sorted((v,w)))] for w in adj[v]) for v in adj}
    base={v:incident[v][0] for v in adj}
    other={v:incident[v][1:] for v in adj}
    cycles=cycles_of(adj)
    assert len(cycles)==1168
    assert Counter(map(len,cycles))=={5:12,8:30,9:20,10:36,11:120,12:100,
                                      13:60,14:180,15:180,16:90,17:180,18:130,20:30}
    masks=[sum(1<<v for v in c) for c in cycles]
    triples=[]
    for i in range(len(cycles)):
        for j in range(i+1,len(cycles)):
            if masks[i]&masks[j]:continue
            both=masks[i]|masks[j]
            for k in range(j+1,len(cycles)):
                if not masks[k]&both:triples.append((i,j,k))
    assert len(triples)==56
    assert Counter(max(len(cycles[i]) for i in t) for t in triples)=={5:20,8:30,10:6}
    vertex_triples=list(combinations(range(20),3))
    index3={(t,b):8*i+b for i,t in enumerate(vertex_triples) for b in range(8)}
    rev3=[(t,b) for t in vertex_triples for b in range(8)]
    loc=[]
    for c in cycles:
        d={}
        for k,v in enumerate(c):
            ein=ei[tuple(sorted((c[k-1],v)))]
            eout=ei[tuple(sorted((v,c[(k+1)%len(c)])))]
            d[v]=[(j,int(eout==e)-int(ein==e))
                  for j,e in enumerate(other[v]) if e in (ein,eout)]
            assert d[v]
        loc.append(d)
    tori=[torus_vector(t,cycles,loc,index3) for t in triples]
    pair_index={t:i for i,t in enumerate(combinations(range(20),2))}

    def boundary(v):
        out=defaultdict(int)
        for r,coef in v.items():
            triple,bits=rev3[r]
            bits3=[bits>>2&1,bits>>1&1,bits&1]
            for j,vx in enumerate(triple):
                rest=tuple(triple[k] for k in range(3) if k!=j)
                rem=[bits3[k] for k in range(3) if k!=j]
                off=(pair_index[rest]*4+rem[0]*2+rem[1])*30
                s=coef*(1 if j%2==0 else -1)
                out[off+other[vx][bits3[j]]]+=s
                out[off+base[vx]]-=s
        return {r:a for r,a in out.items() if a}

    for z in tori:assert not boundary(z)
    # Only degree-three differential needed: weight-three complex C4=0.
    # Matrix has 9,120 columns and 22,800 rows; F2 rank gives
    # a characteristic-zero rank lower bound.
    d3=[]
    for triple,bits in rev3:
        bs=[bits>>2&1,bits>>1&1,bits&1]
        z=0
        for j,vx in enumerate(triple):
            rest=tuple(triple[k] for k in range(3) if k!=j)
            rem=[bs[k] for k in range(3) if k!=j]
            off=(pair_index[rest]*4+rem[0]*2+rem[1])*30
            z^=1<<(off+base[vx])
            z^=1<<(off+other[vx][bs[j]])
        d3.append(z)
    pivots={}
    for z in d3:
        while z:
            b=(z&-z).bit_length()-1
            if b not in pivots:
                pivots[b]=z;break
            z^=pivots[b]
    assert len(pivots)==9094

    kinds=[max(len(cycles[i]) for i in t) for t in triples]
    face=[i for i,x in enumerate(kinds) if x==5]
    octo=[i for i,x in enumerate(kinds) if x==8]
    ten=[i for i,x in enumerate(kinds) if x==10]
    face_rows,face_accepted=rank2_and_rows([tori[i] for i in face])
    assert len(face_accepted)==20
    mface=[[tori[j].get(r,0) for j in face] for r in face_rows]
    assert abs(determinant(mface))==1
    inv=inverse(mface)
    relations=[]
    for i in octo:
        rhs=[tori[i].get(r,0) for r in face_rows]
        cf=[sum(inv[j][k]*rhs[k] for k in range(20)) for j in range(20)]
        assert all(x.denominator==1 for x in cf)
        combined=defaultdict(int)
        for a,j in zip(cf,face):
            if a:
                for r,val in tori[j].items():combined[r]+=int(a)*val
        assert {r:v for r,v in combined.items() if v}==tori[i]
        relations.append([int(c) for c in cf])
    natural=face+ten
    full_rows,full_accept=rank2_and_rows([tori[i] for i in natural])
    assert len(full_accept)==26
    mfull=[[tori[j].get(r,0) for j in natural] for r in full_rows]
    assert abs(determinant(mfull))==1
    # A unit minor makes each selected lattice primitive in C3.
    # rank_F2(d3)=9094 and 26 independent tori show rank_Z ker(d3)=26;
    # thus the primitive 26-torus lattice equals the complete kernel.
    # The primitive 20-face lattice leaves a torsion-free rank-six quotient.
    import json
    print('DODECA_THREE_TORI_LENGTH_TEN_OK')
    print('graph=GP(10,2), cycles=1168, triples=56, split=(20,30,6)')
    print('C3=9120, C2=22800, rank_F2_d3=9094, H3_rank=26')
    print('face_minor='+str(determinant(mface))+', full_minor='+str(determinant(mfull)))
    print('octagon_relations=30 verified, nonzero coefficients per relation='+str(Counter(sum(x!=0 for x in row) for row in relations)))
    print('face_torus_indexes='+json.dumps(face))
    print('ten_torus_indexes='+json.dumps(ten))
    print('face_minor_rows='+json.dumps(face_rows))
    print('full_minor_rows='+json.dumps(full_rows))
    print('face_torus_cycles='+json.dumps([triples[i] for i in face]))
    print('ten_torus_cycles='+json.dumps([triples[i] for i in ten]))
    print('octagon_relations='+json.dumps(relations))

if __name__=='__main__':main()

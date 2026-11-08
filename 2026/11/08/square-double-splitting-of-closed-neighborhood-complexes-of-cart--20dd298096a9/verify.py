#!/usr/bin/env python3
"""Finite face-poset verification of a Cartesian-graph closed-neighborhood collapse."""
from itertools import combinations
from collections import defaultdict


def path(n):
    return n, {(i,i+1) for i in range(n-1)}


def cycle(n):
    return n, {tuple(sorted((i,(i+1)%n))) for i in range(n)}


def star(n):
    return n+1, {(0,i) for i in range(1,n+1)}


def product(H,J):
    a,ea=H; b,eb=J
    ea={tuple(sorted(e)) for e in ea}; eb={tuple(sorted(e)) for e in eb}
    E={tuple(sorted((x*b+y,xx*b+y))) for x,xx in ea for y in range(b)}
    E|={tuple(sorted((x*b+y,x*b+yy))) for y,yy in eb for x in range(a)}
    return a*b,E


def raw_complex(G):
    n,edges=G
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    faces={frozenset()}
    for v in range(n):
        ball=tuple(sorted(adj[v]|{v}))
        for k in range(1,len(ball)+1):
            for sub in combinations(ball,k):faces.add(frozenset(sub))
    return faces, adj


def elementary_collapse(faces,free_face,coface):
    assert free_face in faces and coface in faces
    assert len(coface)==len(free_face)+1 and free_face<=coface
    assert not any(free_face<z and z!=coface for z in faces), (free_face,coface)
    faces.remove(free_face);faces.remove(coface)


def expected_complex(H,J):
    na,ea=H; nb,eb=J
    G=product(H,J)
    faces={frozenset()}
    for v in range(na*nb):faces.add(frozenset((v,)))
    for e in G[1]:faces.add(frozenset(e))
    for a,b in ea:
        for c,d in eb:
            # Four corners of the product square. Two independent diagonal triangulations.
            x=a*nb+c; y=b*nb+c; z=a*nb+d; w=b*nb+d
            for diag in ((x,w),(y,z)):
                t,u=diag
                other=tuple(set((x,y,z,w))-{t,u})
                faces.add(frozenset((t,u)))
                faces.add(frozenset((t,u,other[0])))
                faces.add(frozenset((t,u,other[1])))
    return faces


def check(H,J,betti=True):
    G=product(H,J); n,edges=G
    faces,adj=raw_complex(G)
    raw=len(faces)-1
    stage1=stage2=0
    # Each face on >=3 distinct neighbors is unique to the associated ball.
    for v in range(n):
        neigh=sorted(adj[v])
        for k in range(len(neigh),2,-1):
            for sub in combinations(neigh,k):
                f=frozenset(sub); c=f|{v}
                elementary_collapse(faces,f,c)
                stage1+=1
    # Pairs at distance two having a unique midpoint are free edges.
    for u in range(n):
        for w in range(u+1,n):
            if w in adj[u]:continue
            commons=adj[u]&adj[w]
            if len(commons)==1:
                v=next(iter(commons))
                elementary_collapse(faces,frozenset((u,w)),frozenset((u,v,w)))
                stage2+=1
            else:
                assert len(commons)<=2, (u,w,commons)
    expected=expected_complex(H,J)
    assert faces==expected, (len(faces-expected),len(expected-faces))
    v=len([f for f in faces if len(f)==1]); e=len([f for f in faces if len(f)==2]); t=len([f for f in faces if len(f)==3])
    assert len(faces)==1+v+e+t
    b1=(len(H[1])-H[0]+1)+(len(J[1])-J[0]+1)
    b2=(len(H[1])-H[0]+1)*(len(J[1])-J[0]+1)+len(H[1])*len(J[1])
    assert v-e+t==1-b1+b2
    if betti:
        # Independent mod-2 chain ranks of the fully collapsed two-complex.
        vert=sorted(f for f in faces if len(f)==1)
        edge=sorted((tuple(sorted(f)) for f in faces if len(f)==2))
        edge_index={z:i for i,z in enumerate(edge)}
        tri=[tuple(sorted(f)) for f in faces if len(f)==3]
        basis={}
        for x in tri:
            bits=0
            for z in combinations(x,2):bits^=1<<edge_index[z]
            while bits:
                pivot=bits.bit_length()-1
                if pivot not in basis:
                    basis[pivot]=bits;break
                bits^=basis[pivot]
        rank2=len(basis)
        rank1=v-1
        got1=e-rank1-rank2
        got2=t-rank2
        assert (got1,got2)==(b1,b2),(got1,got2,b1,b2)
    return {'vertices':n,'raw_faces':raw,'collapses':stage1+stage2,'stage1':stage1,'stage2':stage2,'residual_f':(v,e,t),'betti':(b1,b2)}


def main():
    cases=[('edge-edge',path(2),path(2)),('edge-path4',path(2),path(4)),
           ('path3-path3',path(3),path(3)),('path4-path4',path(4),path(4)),
           ('star4-edge',star(4),path(2)),('star3-path3',star(3),path(3)),
           ('pentagon-edge',cycle(5),path(2)),('pentagon-path3',cycle(5),path(3)),
           ('pentagon-pentagon',cycle(5),cycle(5)),('pentagon-hexagon',cycle(5),cycle(6))]
    for name,H,J in cases:
        z=check(H,J)
        print('CASE_OK',name,z)
    print('ALL_VERIFY_OK',len(cases),'Cartesian graph products, all collapses and exact residual simplices, independent mod-2 chain ranks')

if __name__=='__main__':main()

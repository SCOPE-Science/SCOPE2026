#!/usr/bin/env python3
"""Reproducible exhaustive checks of cyclic-power flag-complex edge-fault collapses.

Only finite examples are checked here; the unbounded theorem uses the accompanying proof.
"""
from itertools import combinations

def graph(n,p):
    return {frozenset((a,b)) for a in range(n) for b in range(a+1,n) if min(b-a,n-b+a)<=p}

def flag_faces(n,edges):
    faces = {frozenset()}
    for v in range(n):
        old = tuple(faces)
        faces.update(f|{v} for f in old if all(frozenset((u,v)) in edges for u in f))
    return faces

def link_vertices(n,p,d):
    E=graph(n,p)
    return {v for v in range(n) if v not in (0,d) and frozenset((v,0)) in E and frozenset((v,d)) in E}

def interval_positions(n,p,d):
    return list(range(d-p,0))+list(range(1,d))+list(range(d+1,p+1))

def verify_interval_link(n,p,d):
    vertices = interval_positions(n,p,d)
    assert len({v%n for v in vertices})==len(vertices)
    assert {v%n for v in vertices}==link_vertices(n,p,d)
    E=graph(n,p)
    for a,b in combinations(vertices,2):
        assert (frozenset((a%n,b%n)) in E)==(abs(a-b)<=p)
    if p>=3:
        S=set(vertices)
        while len(S)>1:
            v=min(S)
            w=sorted(S)[1]
            assert w-v<=p
            assert all(u==w or abs(u-w)<=p for u in S if u==v or abs(u-v)<=p)
            S.remove(v)
    else:
        assert (d!=1) or len(vertices)==2

def check_relative_collapses(n,p,d):
    E=graph(n,p)
    edge=frozenset((0,d))
    assert edge in E
    X=flag_faces(n,E)
    Y=flag_faces(n,E-{edge})
    R=X-Y
    if p==2 and d==1:
        assert len(R)==3 # edge and 2 triangles
        return len(R),0
    initial=len(R)
    pairs=0
    while R:
        choice=None
        for s in sorted(R,key=lambda a:(-len(a),tuple(sorted(a)))):
            cofaces=[t for t in R if len(t)==len(s)+1 and s.issubset(t)]
            if len(cofaces)==1 and not any(len(u)==len(cofaces[0])+1 and cofaces[0].issubset(u) for u in R):
                choice=(s,cofaces[0]);break
        assert choice is not None,(n,p,d,len(R))
        R.remove(choice[0]);R.remove(choice[1]);pairs+=1
    assert 2*pairs==initial
    assert Y == X - (X-Y)
    return initial,pairs

def triangle_collapse(n):
    E=graph(n,2)
    lost=frozenset((0,1))
    F=flag_faces(n,E-{lost})
    for i in range(n):
        edge=frozenset((i,(i+2)%n))
        tri=frozenset((i,(i+1)%n,(i+2)%n))
        if lost.issubset(tri):
            continue
        assert edge in F and tri in F
        assert not any(len(t)>len(tri) and tri.issubset(t) for t in F)
        assert [t for t in F if len(t)==3 and edge.issubset(t)]==[tri]
        F.remove(tri);F.remove(edge)
    assert all(len(f)<=2 for f in F)
    verts={next(iter(f)) for f in F if len(f)==1}
    e2=[f for f in F if len(f)==2]
    assert len(verts)==n and len(e2)==n+1
    seen={0}
    while True:
        new=seen|{next(iter(f-{v})) for f in e2 for v in f if v in seen}
        if new==seen:break
        seen=new
    assert len(seen)==n
    return len(e2)-n+1

def run():
    checks=[]
    for p in range(2,7):
        for n in range(4*p+2,4*p+5):
            for d in range(1,p+1):
                verify_interval_link(n,p,d)
                # Complete explicit elementary-collapse replay on selected moderate orders.
                if p<=4 or (p==5 and n==4*p+2):
                    a,b=check_relative_collapses(n,p,d)
                    checks.append((n,p,d,a,b))
    assert triangle_collapse(10)==2
    # Check full unperturbed flag complexes collapse by the distance-p edge cells.
    for p in range(2,7):
        n=4*p+2
        F=flag_faces(n,graph(n,p))
        for q in range(p,1,-1):
            for i in range(n):
                e=frozenset((i,(i+q)%n))
                incident=[f for f in F if e.issubset(f)]
                assert incident
                top=max(incident,key=len)
                assert all(f.issubset(top) for f in incident)
                F.difference_update(incident)
        assert F==flag_faces(n,graph(n,1))
    print('PASS: exact ordered-link equivalences and domination, p=2..6, n=4p+2..4p+4.')
    print('PASS: complete relative elementary-collapse replay',sum(r[4]>0 for r in checks),'nonexceptional single-edge instances; 3 exceptional link/face checks.')
    print('PASS: intact flag-complex elementary-collapse certificates for p=2..6.')
    print('PASS: p=2 nearest-neighbor fault has graph cycle rank two.')
    print('Sample relative face-pair counts:',checks[:12])
if __name__=='__main__':run()

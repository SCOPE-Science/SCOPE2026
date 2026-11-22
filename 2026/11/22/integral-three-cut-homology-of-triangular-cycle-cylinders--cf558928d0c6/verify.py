"""Independent finite checks of triangular-cylinder three-cut duals.
Run: python verify.py. No external packages are needed.
"""
from itertools import combinations
from collections import Counter
from math import comb

def run(n):
    assert n >= 5
    V = tuple(range(3*n))
    v = lambda i,a: 3*(i%n)+a
    def adjacent(x,y):
        i,a=divmod(x,3);j,b=divmod(y,3)
        return (i==j and a!=b) or (a==b and ((i-j)%n in (1,n-1)))
    edges=set(combinations(V,2))
    tri={t for t in combinations(V,3) if sum(adjacent(x,y) for x,y in combinations(t,2))>=2}
    tets={t for t in combinations(V,4) if all(z in tri for z in combinations(t,3))}
    quints={t for t in combinations(V,5) if all(z in tets for z in combinations(t,4))}
    assert len(tri)==16*n and len(tets)==3*n and len(quints)==0
    assert len({t for t in combinations(V,2) if adjacent(*t)})==6*n
    F={1:{(x,) for x in V},2:edges,3:tri.copy(),4:tets.copy()}
    collapse_count=0
    def collapse(face,coface):
        nonlocal collapse_count
        face=tuple(sorted(face));coface=tuple(sorted(coface))
        k=len(face)
        assert len(coface)==k+1 and face in F[k] and coface in F[k+1],(n,face,coface)
        assert [x for x in F[k+1] if set(face)<=set(x)]==[coface],(n,face,coface)
        assert all(not set(face)<=set(x) for d in range(k+2,5) for x in F[d]),(n,face,coface)
        F[k].remove(face);F[k+1].remove(coface)
        collapse_count+=1
    for i in range(n):
        for a,b in combinations(range(3),2):
            x,y,z,w=v(i,a),v(i,b),v(i+1,a),v(i+1,b)
            collapse((x,y,z),(x,y,z,w))
            collapse((y,z),(y,z,w))
    for i in range(n):
        for a in range(3):
            collapse((v(i-1,a),v(i+1,a)),(v(i-1,a),v(i,a),v(i+1,a)))
    assert collapse_count==9*n
    assert len(F[4])==0 and len(F[3])==7*n and len(F[2])==comb(3*n,2)-6*n
    # Exactly n vertical triangles plus two per adjacent-column rectangle.
    want={tuple(sorted(v(i,a) for a in range(3))) for i in range(n)}
    for i in range(n):
        for a,b in combinations(range(3),2):
            x,y,z,w=v(i,a),v(i,b),v(i+1,a),v(i+1,b)
            want.update([tuple(sorted((x,y,w))),tuple(sorted((x,z,w)))])
    assert F[3]==want
    geometric_edges=set()
    for t in F[3]:geometric_edges.update(combinations(t,2))
    assert len(geometric_edges)==9*n
    long_edges=F[2]-geometric_edges
    assert len(long_edges)==comb(3*n,2)-15*n
    # The n triangular-prism boundary spheres have 2D faces
    # (their bases and their rectangular side triangulations).
    # Consecutive prisms share one entire triangular base.
    assert len(F[3])==7*n
    # Compute modular ranks on the original dual without any collapse.
    def rank_gf2(columns):
        basis={}
        for c in columns:
            while c:
                i=c.bit_length()-1
                if i in basis:c^=basis[i]
                else:basis[i]=c;break
        return len(basis)
    original_edges=list(combinations(V,2));ed={e:i for i,e in enumerate(original_edges)}
    original_tris=sorted(tri);td={t:i for i,t in enumerate(original_tris)}
    d2=[]
    for t in original_tris:
        z=0
        for e in combinations(t,2):z^=1<<ed[e]
        d2.append(z)
    d3=[]
    for t in tets:
        z=0
        for e in combinations(t,3):z^=1<<td[e]
        d3.append(z)
    r2=rank_gf2(d2);r3=rank_gf2(d3)
    expected_long=comb(3*n,2)-15*n
    assert r3==3*n and r2==12*n
    assert comb(3*n,2)-(3*n-1)-r2==expected_long+1
    assert 16*n-r2-r3==n
    print(f'n={n} V={3*n} triangles={16*n} tetrahedra={3*n} elementary_collapses={collapse_count} long_edges={expected_long} dual_b1={expected_long+1} dual_b2={n} ranks_F2=({r2},{r3}): PASS')

if __name__=='__main__':
    for n in range(5,11):run(n)
    print('Six finite sizes, all face sets, acyclic free-face cancellations, and GF(2) boundary ranks: PASS')

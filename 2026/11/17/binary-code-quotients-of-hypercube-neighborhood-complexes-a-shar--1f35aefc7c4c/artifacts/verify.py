#!/usr/bin/env python3
"""Independent finite CW-chain checks for neighborhood-complex translation quotients."""
from itertools import combinations
from math import comb

def span(basis):
    v={0}
    for b in basis:
        v |= {a^b for a in tuple(v)}
    return tuple(sorted(v))

def rank_mod2(columns):
    basis={}
    for col in columns:
        t=col
        while t:
            pivot=t.bit_length()-1
            if pivot not in basis:
                basis[pivot]=t
                break
            t ^= basis[pivot]
    return len(basis)

def check(d, basis):
    group=span(basis)
    assert all(c.bit_count()%2==0 and c.bit_count()!=2 for c in group)
    verts=list(range(0,1<<d)); verts=[x for x in verts if x.bit_count()%2==0]
    generators=[1^(1<<j) for j in range(1,d)]
    edges=set()
    for x in verts:
        for i,j in combinations(range(d),2):
            edges.add(tuple(sorted((x,x^(1<<i)^(1<<j)))))
    triangles=set()
    for x in verts:
        for i,j in combinations(generators,2):
            triangles.add(tuple(sorted((x,x^i,x^j))))
    assert len(edges)==2**(d-2)*comb(d,2)
    assert len(triangles)==2**(d-1)*comb(d-1,2)
    def orbit(simplex):
        return min(tuple(sorted(x^g for x in simplex)) for g in group)
    cosets={orbit((x,)) for x in verts}
    eo={orbit(e) for e in edges}
    to={orbit(t) for t in triangles}
    assert len(cosets)==len(verts)//len(group)
    assert len(eo)==len(edges)//len(group)
    assert len(to)==len(triangles)//len(group)
    v_idx={e:i for i,e in enumerate(sorted(cosets))}
    e_idx={e:i for i,e in enumerate(sorted(eo))}
    def col_incidence(faces, indexer):
        x=0
        for face in faces:
            x ^= 1<<indexer[orbit(face)]
        return x
    b1=[]
    for u,v in sorted(eo):
        b1.append(col_incidence([(u,),(v,)], v_idx))
    b2=[]
    for u,v,w in sorted(to):
        b2.append(col_incidence([(u,v),(u,w),(v,w)], e_idx))
    for col in b2:
        low=0
        for i, boundary in enumerate(b1):
            if (col >> i) & 1:
                low ^= boundary
        assert low == 0, "cellular boundary does not square to zero"
    for f in tuple(triangles) + tuple(edges):
        assert all(tuple(sorted(x^g for x in f)) != f for g in group if g), "nonfree face action"
    rank1=rank_mod2(b1)
    rank2=rank_mod2(b2)
    b0=len(cosets)-rank1
    b1dim=len(eo)-rank1-rank2
    b2dim=len(to)-rank2
    expected_b2=(1+2**(d-3)*(d*d-5*d+8)-1)//len(group)-1
    assert b0==1 and b1dim==len(basis) and b2dim==expected_b2+len(basis), (d,basis,(b0,b1dim,b2dim),expected_b2)
    print(f'd={d} rank={len(basis)} |E|={len(group)} cells=({len(cosets)},{len(eo)},{len(to)}) mod2_Betti=({b0},{b1dim},{b2dim}) integral_H1=(Z/2)^{len(basis)} integral_H2=Z^{expected_b2} (mod2_H2_includes_Tor_H1)')

if __name__=='__main__':
    check(4,[0b1111])
    check(5,[0b11110])
    check(6,[0b001111,0b111100])
    check(7,[sum(1<<(i-1) for i in range(1,8) if i & (1<<bit)) for bit in range(3)])
    print('CODE_QUOTIENT_NEIGHBORHOOD_CHAIN_CHECKS_PASS')

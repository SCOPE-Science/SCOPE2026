#!/usr/bin/env python3
"""Exact finite check of maximal-abelian-coset nerves for Dic_n, 2 <= n <= 7."""
from itertools import combinations
from math import comb

def exact(n):
    G=[(a,b) for b in range(2) for a in range(2*n)]
    E=(0,0)
    mul=lambda u,v:((u[0]+(-1 if u[1] else 1)*v[0]+n*u[1]*v[1])%(2*n),u[1]^v[1])
    A=frozenset((a,0) for a in range(2*n))
    Bs=[frozenset((E,(n,0),(i,1),((i+n)%(2*n),1))) for i in range(n)]
    out=[]
    for k,H in enumerate([A]+Bs):
        cosetmap={frozenset(mul(g,h) for h in H) for g in G}
        for C in sorted(cosetmap,key=lambda C:sorted(C)):
            out.append((k,C))
    assert len(out)==2+n*n
    assert len({c for k,c in out})==2+n*n  # all distinct even if equal subgroup order
    z=frozenset((E,(n,0)))
    pairs=[frozenset((g,mul(g,(n,0)))) for g in G]
    pairs=set(pairs)
    assert len(pairs)==2*n
    facets=[]
    for pair in pairs:
        F=frozenset(i for i,(_,C) in enumerate(out) if pair <= C)
        assert len(F)==n+1
        facets.append(F)
    assert len(set(facets))==2*n
    # Exhaustively match every nonempty intersection among maximal cosets to a central-pair facet.
    # A subset of the cosets has nonempty total intersection iff its indices sit in a facet.
    faces=set()
    for facet in facets:
        ids=sorted(facet)
        for k in range(1,len(ids)+1):
            faces.update(combinations(ids,k))
    bydim=[sum(len(face)==d+1 for face in faces) for d in range(n+1)]
    expected=[2+n*n]+[2*n*comb(n+1,d+1) for d in range(1,n+1)]
    assert bydim==expected,(n,bydim,expected)
    # For each pair of maximal cosets, its set intersection is empty or a central pair.
    for i in range(len(out)):
        for j in range(i+1,len(out)):
            M=out[i][1]&out[j][1]
            assert not M or frozenset(M) in pairs
    # The two A cosets give two disjoint contractible subnerves; intersection exactly n^2 vertices.
    iA=[i for i,(k,_) in enumerate(out) if k==0]
    assert len(iA)==2
    L,R=sorted(iA)
    lverts={i for i,(_,C) in enumerate(out) if C & out[L][1]}
    rverts={i for i,(_,C) in enumerate(out) if C & out[R][1]}
    assert lverts&rverts==set(range(len(out)))-{L,R}
    LF={f for f in faces if set(f)<=lverts and any(set(f)<=set(F) for F in facets if L in F)}
    RF={f for f in faces if set(f)<=rverts and any(set(f)<=set(F) for F in facets if R in F)}
    assert LF|RF==faces
    assert LF&RF=={(i,) for i in range(len(out)) if i not in (L,R)}
    # Independently check the signed augmentation character from actual left multiplication.
    index={(k,C):i for i,(k,C) in enumerate(out)}
    Eids=[i for i,(k,C) in enumerate(out) if k>0]
    Aids=[i for i,(k,C) in enumerate(out) if k==0]
    assert len(Eids)==n*n
    for g in G:
        action=[index[k, frozenset(mul(g,h) for h in C)] for k,C in out]
        assert sorted(action)==list(range(len(out)))
        assert {action[i] for i in Aids}==set(Aids)
        fixedE=sum(action[i]==i for i in Eids)
        expected=(n*n if g in ((0,0),(n,0)) else (0 if g[1]==0 else n))
        assert fixedE==expected,(n,g,fixedE,expected)
        observed_character=(-1 if g[1] else 1)*(fixedE-1)
        target=(n*n-1 if g in ((0,0),(n,0)) else (-1 if g[1]==0 else 1-n))
        assert observed_character==target
    # Each distinguished order-four subgroup gives one orbit of n E-vertices,
    # and its stabilizer exchanges the two A-coset vertices, so the graph quotient is a tree.
    for k in range(1,n+1):
        vals=[i for i,(j,C) in enumerate(out) if j==k]
        assert len(vals)==n
        representative=out[vals[0]][1]
        orbit={index[k,frozenset(mul(g,h) for h in representative)] for g in G}
        assert orbit==set(vals)
    assert set(Aids)=={index[0, frozenset(mul((0,1),h) for h in out[Aids[0]][1])], Aids[0]}
    chi=sum((-1)**d*val for d,val in enumerate(bydim))
    assert chi==2-n*n
    return f'n={n} |G|={4*n} |maxcosets|={len(out)} f={bydim} chi={chi} H1_rank={n*n-1}'

if __name__=='__main__':
    for n in range(2,8):print(exact(n))
    print('ALL_EXACT_DICYCLIC_ABELIAN_COSET_NERVE_CHECKS_PASS')

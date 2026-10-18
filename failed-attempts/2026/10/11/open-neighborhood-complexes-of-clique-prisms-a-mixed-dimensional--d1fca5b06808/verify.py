#!/usr/bin/env python3
"""Standalone finite checks for the open-neighborhood complex of K_m box K_2.
Only graph/simplicial definitions and linear algebra over F_2 are used.
"""
from itertools import combinations

def facets(m):
    # Independent graph construction: K_m in each layer, with matching rungs.
    adjacency = [set() for _ in range(2*m)]
    for i in range(m):
        for j in range(i+1,m):
            for layer in (0,1):
                u,v=i+layer*m,j+layer*m
                adjacency[u].add(v)
                adjacency[v].add(u)
        adjacency[i].add(m+i)
        adjacency[m+i].add(i)
    assert all(len(x)==m for x in adjacency)
    return list(map(frozenset,adjacency))

def faces(fs):
    ff={frozenset()}
    for f in fs:
        v=sorted(f)
        for k in range(1,len(v)+1):
            ff.update(map(frozenset,combinations(v,k)))
    return ff

def gf2rank(columns):
    pivots={}; rank=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x;rank+=1;break
            x^=pivots[p]
    return rank

def betti(ff):
    bydim={}
    for face in ff:
        if face: bydim.setdefault(len(face)-1,[]).append(face)
    for d in bydim: bydim[d].sort(key=lambda s:tuple(sorted(s)))
    ranks={}
    for d in sorted(bydim):
        if d<1: ranks[d]=0;continue
        rows={f:i for i,f in enumerate(bydim[d-1])}
        cols=[]
        for f in bydim[d]:
            a=0
            for v in f: a^=1<<rows[f-{v}]
            cols.append(a)
        ranks[d]=gf2rank(cols)
    result={d:len(bydim[d])-ranks[d]-ranks.get(d+1,0) for d in bydim}
    result[0]-=1  # reduced homology for connected complexes
    return result

def check(m):
    full=facets(m); a=faces(full[:m]); b=faces(full[m:]); universe=faces(full)
    assert universe==a|b
    common=a&b
    cross={frozenset((i,m+j)) for i in range(m) for j in range(m) if i!=j}
    assert common == {frozenset()}|{frozenset((i,)) for i in range(2*m)}|cross
    assert len(cross)==m*(m-1)
    assert len(a|b)==len(universe)
    h=betti(universe)
    expected={d:0 for d in h}
    expected[2]=m*m-3*m+1+(2 if m==4 else 0)
    if m>4: expected[m-2]=2
    assert h==expected,(m,h,expected)
    Euler=sum((-1)**(len(f)-1) for f in universe if f)-1
    expEuler=(m*m-3*m+1)+2*((-1)**(m-2))
    assert Euler==expEuler,(m,Euler,expEuler)
    print('m=%d nonempty_faces=%d intersection_edges=%d betti_F2=%s reduced_Euler=%d'%(m,len(universe)-1,len(cross),h,Euler))

if __name__=='__main__':
    for m in range(4,9): check(m)
    print('VERIFY_OK')

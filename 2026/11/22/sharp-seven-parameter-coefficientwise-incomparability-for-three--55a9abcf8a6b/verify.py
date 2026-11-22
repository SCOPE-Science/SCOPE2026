#!/usr/bin/env python3
"""Self-contained check of three-triangle Henson-graph type spectra.

No external dependencies. Every possible triangle triple on <=9 vertices is
covered by relabeling one distinguished triangle to vertices 0,1,2.
"""
from itertools import combinations
from math import comb
from collections import defaultdict


def triangles(n):
    return [sum(1 << v for v in T) for T in combinations(range(n), 3)]


def present_triangles(n, triple):
    edge_set=set()
    for t in triple:
        vs=[v for v in range(n) if (t >> v) & 1]
        edge_set.update(combinations(vs,2))
    return tuple(t for t in triangles(n) if all(e in edge_set for e in combinations([v for v in range(n) if (t >> v)&1],2)))


def poly_direct(n, triple):
    a=[0]*(n+1)
    for subset in range(1<<n):
        if all((subset & t) != t for t in triple):
            a[subset.bit_count()]+=1
    return tuple(a)


def poly_ie(n,triple):
    # Inclusion-exclusion for three forbidden triangles
    out=[0]*(n+1)
    for mask in range(8):
        union=0
        for j in range(3):
            if mask>>j & 1: union |= triple[j]
        sz=union.bit_count()
        sign=(-1)**mask.bit_count()
        for j in range(n-sz+1):out[sz+j]+=sign*comb(n-sz,j)
    return tuple(out)


def spectrum(n):
    tri=triangles(n)
    if n<3:return set(),0
    first=sum(1<<i for i in (0,1,2))
    others=[t for t in tri if t!=first]
    polys=set();valid=0
    for b,c in combinations(others,2):
        triple=tuple(sorted([first,b,c]))
        if set(present_triangles(n,triple))!=set(triple):continue
        p=poly_ie(n,triple)
        assert p==poly_direct(n,triple),(n,triple,p,poly_direct(n,triple))
        polys.add(p);valid+=1
    return polys, valid


def incomparable(a,b):
    return any(x>y for x,y in zip(a,b)) and any(x<y for x,y in zip(a,b))


def check():
    counts={}
    for n in range(3,10):
        ps,valid=spectrum(n)
        bad=sum(1 for a,b in combinations(sorted(ps),2) if incomparable(a,b))
        counts[n]=(len(ps),bad,valid)
        print('n=',n,'spectra=',len(ps),'incomparable_pairs=',bad,'normalized_realizations=',valid)
    assert [counts[n][0] for n in (5,6,7,8,9)]==[2,4,7,8,9]
    assert all(counts[n][1]==0 for n in range(3,7))
    assert counts[7][1]==2
    assert len(spectrum(9)[0])==9
    A=tuple(sum(1<<i for i in T) for T in ((0,1,2),(0,3,4),(0,5,6)))
    B=tuple(sum(1<<i for i in T) for T in ((0,1,2),(0,1,3),(4,5,6)))
    a=poly_direct(7,A); b=poly_direct(7,B)
    assert set(present_triangles(7,A))==set(A)
    assert set(present_triangles(7,B))==set(B)
    assert a==(1,7,21,32,23,6,1,0), a
    assert b==(1,7,21,32,24,6,0,0), b
    assert incomparable(a,b)
    print('A:',a, 'B:',b,'A-B:',tuple(x-y for x,y in zip(a,b)))
    print('all nine n=9 spectra:')
    for p in sorted(spectrum(9)[0]):print(' '.join(map(str,p)))
    print('VERIFY_OK')
if __name__=='__main__':check()

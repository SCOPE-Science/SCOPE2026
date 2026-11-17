"""Reproducible finite checks for rim-edge-deleted Möbius-ladder perfect matching complexes.

The infinite-width theorem is established by the accompanying structural proof;
this program is an independent finite combinatorial consistency check.
"""
from collections import Counter
from functools import lru_cache


def graph_edges(n):
    assert n >= 2
    V = 2*n
    return sorted({tuple(sorted((v,(v+1)%V))) for v in range(V)} |
                  {(v,v+n) for v in range(n)})


def perfect_matchings(n, edges):
    incidence=[[] for _ in range(2*n)]
    for j,(a,b) in enumerate(edges):
        incidence[a].append((b,j));incidence[b].append((a,j))
    @lru_cache(None)
    def solve(rest):
        if rest == 0: return (0,)
        v = (rest & -rest).bit_length()-1
        ans=[]
        for w,j in incidence[v]:
            if (rest >> w)&1:
                ans.extend((1 << j) | m for m in solve(rest ^ (1<<v) ^ (1<<w)))
        return tuple(ans)
    return solve((1 << (2*n))-1)


def all_faces(facets):
    faces={0}
    for f in facets:
        sub=f
        while sub:
            faces.add(sub)
            sub=(sub-1)&f
    return faces


def critical_cells(faces, edge_count):
    remaining=set(faces)
    for j in range(edge_count):
        b=1<<j
        lower={f for f in remaining if f and not (f&b) and (f|b) in remaining}
        remaining.difference_update(lower)
        remaining.difference_update(f|b for f in lower)
    return Counter(f.bit_count()-1 for f in remaining)


def target_degree(n):
    if n%2==0: return n//2-1
    if n%6==5: return None
    if n%6==1: return (n-1)//3
    return (n-3)//3+1


def verify(n):
    E=graph_edges(n)
    removed=(0,2*n-1)
    cross=(n-1,n)
    defective=[e for e in E if e!=removed]
    open_edges=[e for e in defective if e!=cross]
    full_fac=perfect_matchings(n,defective)
    open_fac=perfect_matchings(n,open_edges)
    cross_bit=1<<defective.index(cross)
    extra_fac=[f for f in full_fac if f & cross_bit]
    assert len(extra_fac)==(n%2), (n,len(extra_fac))
    assert len(full_fac)==len(open_fac)+len(extra_fac)
    if n%2:
        F=extra_fac[0]
        remaining=[e for j,e in enumerate(defective) if (F>>j)&1 and e!=cross]
        pos={}
        for e in remaining:
            a,b=e
            assert b==a+1
            i=a+1 if a<n else a-n+1
            assert i not in pos
            pos[i]=open_edges.index(e)
        assert set(pos)==set(range(1,n))
        for S in range(1 << (n-1)):
            subset=sum(1<<pos[i+1] for i in range(n-1) if S>>i & 1)
            extendible=any((subset & f)==subset for f in open_fac)
            independent=not (S & (S<<1))
            assert extendible==independent,(n,S)
    if n<=12:
        faces=all_faces(full_fac)
        critical=critical_cells(faces,len(defective))
        expected=Counter({-1:1,0:1})
        deg=target_degree(n)
        if deg is not None:
            expected[deg]+=1
        # For n=2, degree zero: two critical 0-simplices.
        assert critical==expected,(n,critical,expected)
        return n,len(open_fac),len(extra_fac),len(faces),dict(sorted(critical.items()))
    return n,len(open_fac),len(extra_fac),'uncomputed','intersection checked'


if __name__=='__main__':
    for n in range(2,14):
        print('n, open_facets, extra_facets, faces, critical:',verify(n))
    print('MOBIUS_RIM_DELETION_FINITE_CHECK_PASS')

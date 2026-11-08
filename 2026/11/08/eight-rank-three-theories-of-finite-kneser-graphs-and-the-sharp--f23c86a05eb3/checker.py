"""Reproducible finite checks for rank-three signatures of finite Kneser graphs.

Runs independently of any external data. Standard library only.
Finite enumeration corroborates, rather than proves, the all-parameter theorem.
"""
from itertools import combinations
from math import comb

BITPATTERNS = ((0,0),(0,1),(1,0),(1,1))
P0 = ((0,0),(0,1),(1,0))
P1 = BITPATTERNS

def graph(n, k):
    assert 1 <= k <= n
    verts = [frozenset(s) for s in combinations(range(n), k)]
    return verts

def actual_profile(n,k):
    """All pair-extension masks, using representative ordered pairs for every intersection t.
    An arbitrary pair has the same profile by the symmetric-group action.
    """
    vertices = graph(n,k)
    a = vertices[0]
    vals = {}
    for t in range(k):
        if k-t > n-k:
            continue
        b = frozenset(list(range(t)) + list(range(k,k+(k-t))))
        assert len(b)==k and len(a & b)==t
        edge = int(a.isdisjoint(b))
        patt = tuple(sorted(set((int(a.isdisjoint(z)),int(b.isdisjoint(z)))
                         for z in vertices if z != a and z != b)))
        vals.setdefault(edge,set()).add(patt)
    return tuple((e, tuple(sorted(v))) for e,v in sorted(vals.items()))

def theoretical_profile(n,k):
    count = comb(n,k)
    if count==1: return ()
    if k==1:
        return ((1,((),)),) if n==2 else ((1,(((1,1),),)),)
    if n<2*k:
        return ((0,(((0,0),),)),)
    if n==2*k:
        return ((0,(((0,0),(0,1),(1,0)),)),(1,(((0,0),),)))
    e = P1 if n>=3*k else P0
    ne = {P1 if n>=3*k-t else P0 for t in range(1,k)}
    return ((0,tuple(sorted(ne))),(1,(e,)))

def expected_class(n,k):
    if k==n:return 'singleton'
    if k==1:return 'complete2' if n==2 else 'complete3plus'
    if n<2*k:return 'independent3plus'
    if n==2*k:return 'matching3plus'
    if n>=3*k:return 'full2extension'
    if n==3*k-1:return 'trianglefree_full_nonedge'
    return 'mixed_nonedge'

def representative_pairwise_signature(n,k):
    vertices = graph(n,k)
    A = vertices[0]
    out = {}
    for B in vertices:
        if A==B:continue
        bit = int(A.isdisjoint(B))
        pats=set()
        for C in vertices:
            if C in (A,B):continue
            pats.add((int(A.isdisjoint(C)),int(B.isdisjoint(C))))
        out.setdefault(bit,set()).add(tuple(sorted(pats)))
    return tuple((e,tuple(sorted(v))) for e,v in sorted(out.items()))

def main():
    tested=0
    for n in range(1,18):
        for k in range(1,n+1):
            if comb(n,k)>6000:continue
            actual=actual_profile(n,k)
            theoretical=theoretical_profile(n,k)
            assert actual==theoretical,(n,k,actual,theoretical)
            tested+=1
    reps={'singleton':(1,1),'complete2':(2,1),'complete3plus':(3,1),
          'independent3plus':(3,2),'matching3plus':(4,2),
          'trianglefree_full_nonedge':(5,2),'full2extension':(6,2),
          'mixed_nonedge':(7,3)}
    sigs={c:theoretical_profile(*v) for c,v in reps.items()}
    assert len(sigs)==len(set(sigs.values()))==8
    # A second route uses every ordered-pair orbit representative in each small graph.
    for c,(n,k) in reps.items():
        assert representative_pairwise_signature(n,k)==sigs[c]
    # The three canonical nontrivial thresholds are attained at distinct models.
    for k in range(2,7):
        assert expected_class(3*k-1,k)=='trianglefree_full_nonedge'
        assert expected_class(3*k,k)=='full2extension'
    for k in range(3,7):
        assert expected_class(2*k+1,k)=='mixed_nonedge'
    print('KNESER_RANK3_ALL_FINITE_CHECKS_OK cases=',tested,'classes=',len(sigs),
          'largest_bruteforce_vertices=', max(comb(n,k) for n in range(1,18)
                                                 for k in range(1,n+1) if comb(n,k)<=6000))
if __name__=='__main__': main()

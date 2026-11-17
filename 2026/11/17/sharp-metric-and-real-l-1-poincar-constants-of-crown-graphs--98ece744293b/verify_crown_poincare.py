#!/usr/bin/env python3
"""Finite exact-arithmetic diagnostics for crown-graph metric Poincare bounds.

All universally quantified claims require the separate analytical proof.
"""
from fractions import Fraction
from collections import deque
from itertools import product


def expected_l1(n):
    return Fraction(n-1,n-2) if n%2 == 0 else Fraction(n,n-1)


def check_cuts(n):
    best = Fraction(0)
    maximizers = set()
    cut_count = 0
    for mask in range(1,1<<(2*n)):
        if mask == (1<<(2*n))-1:
            continue
        # Avoid counting complementary cuts twice.
        if not mask&1:
            continue
        size = mask.bit_count()
        boundary = sum(((mask>>i)&1) != ((mask>>(n+j))&1)
                       for i in range(n) for j in range(n) if i != j)
        ratio = Fraction((n-1)*size*(2*n-size),2*n*boundary)
        if ratio > best:
            best = ratio
            maximizers = {mask}
        elif ratio == best:
            maximizers.add(mask)
        cut_count += 1
    assert best == expected_l1(n), (n, best)
    for mask in maximizers:
        ka = sum((mask>>i)&1 for i in range(n))
        kb = sum((mask>>(n+i))&1 for i in range(n))
        assert ka+kb == n
        assert abs(ka-kb) <= 1
        assert all(bool((mask>>i)&1) != bool((mask>>(n+i))&1) for i in range(n))
    expected_count = 0
    # Every index-pair contributes exactly one vertex, so 2^n orientations.
    from math import comb
    expected_count = (2*comb(n,n//2) if n%2 else comb(n,n//2))//2
    assert len(maximizers) == expected_count,(n,len(maximizers),expected_count)
    return cut_count,len(maximizers)


def check_shortest_path_metric(n):
    vertices=2*n
    neigh=[[] for _ in range(vertices)]
    for i in range(n):
        for j in range(n):
            if i != j:
                neigh[i].append(n+j)
                neigh[n+j].append(i)
    dist=[]
    for u in range(vertices):
        d=[-1]*vertices
        d[u]=0
        q=deque([u])
        while q:
            x=q.popleft()
            for y in neigh[x]:
                if d[y]<0:
                    d[y]=d[x]+1
                    q.append(y)
        assert all(v>=0 for v in d)
        for v in range(vertices):
            expected = 0 if u==v else (2 if (u<n)==(v<n) else (3 if u%n==v%n else 1))
            assert d[v]==expected,(n,u,v,d[v],expected)
        dist.append(d)
    pair_average=Fraction(sum(sum(row) for row in dist),vertices*vertices)
    edge_average=Fraction(1)
    assert pair_average/edge_average == Fraction(3,2), (n,pair_average)
    return vertices*vertices


def main():
    assertions=0
    for n in range(3,9):
        cuts,norming=check_cuts(n)
        checked_distances=check_shortest_path_metric(n)
        assertions+=cuts+checked_distances
        print('n=%d: cuts=%d, norming cuts with vertex A_0 in S=%d, geodesic distances=%d, L1=%s' %
              (n,cuts,norming,checked_distances,expected_l1(n)))
    for n in range(9,40):
        assertions+=check_shortest_path_metric(n)
    print('CROWN_POINCARE_DIAGNOSTICS_OK',assertions)

if __name__=='__main__':
    main()

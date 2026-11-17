#!/usr/bin/env python3
"""Exact finite cut certificates for graph heat variation contractivity.

Run: python3 verify_graph_bv_heat.py
No third-party packages are required.  Exhaustive loops cover all finite
attachment patterns used to close the small-cycle classification.
"""
from itertools import combinations


def graph(n, edges):
    edges = tuple(sorted({tuple(sorted((u, v))) for u, v in edges}))
    assert all(0 <= u < v < n for u, v in edges)
    nbrs = [set() for _ in range(n)]
    for u, v in edges:
        nbrs[u].add(v)
        nbrs[v].add(u)
    assert all(nbrs) or n == 1
    return tuple(tuple(sorted(z)) for z in nbrs), edges


def cycle_pendants(k, attached):
    attached = tuple(sorted(attached))
    edges = [(i, (i+1) % k) for i in range(k)]
    edges += [(v, k+j) for j, v in enumerate(attached)]
    return graph(k+len(attached), edges)


def cut_slope(g, mask):
    neighbors, edges = g
    n = len(neighbors)
    assert 0 < mask < 2**n-1
    membership = [bool((mask >> v) & 1) for v in range(n)]
    c = [sum(membership[v] != membership[u] for u in neighbors[v])
         for v in range(n)]
    first = -sum(z*z for z in c)
    second = sum(abs(c[u]-c[v]) for u, v in edges
                 if membership[u] == membership[v])
    return first+second


def direct_first_variation(g, mask):
    """Independently differentiate the absolute edge-differences at time 0+."""
    neighbors, edges = g
    x = [int((mask >> i) & 1) for i in range(len(neighbors))]
    lap = [sum(x[i]-x[j] for j in neighbors[i]) for i in range(len(x))]
    slope = 0
    for u, v in edges:
        a, b = x[u]-x[v], -lap[u]+lap[v]
        slope += b*(1 if a>0 else -1) if a != 0 else abs(b)
    return slope


def max_slope(g):
    n = len(g[0])
    return max(cut_slope(g, mask) for mask in range(1, 2**n-1))


def subset_masks(k, num):
    for a in combinations(range(k), num):
        yield a


def verify_small_cases():
    expected = {(3, 0):-6, (4, 0):-4, (5, 0):-2}
    by_size = {(3,3):8, (4,4):16, (5,2):16}
    cases = 0; cuts = 0
    for k in (3,4,5):
        for ell in range(k+1 if k<5 else 3):
            maxval=-10**9
            for A in subset_masks(k, ell):
                g=cycle_pendants(k, A)
                n=len(g[0]); val=max_slope(g)
                assert val <= 0, (k,A,val)
                maxval=max(maxval,val)
                cases+=1
                for mask in range(1,2**n-1):
                    assert cut_slope(g,mask)==direct_first_variation(g,mask)
                    cuts+=1
            assert maxval == expected.get((k,ell),0), (k,ell,maxval)
    assert cases == 40, cases  # 8 triangle, 16 square, 16 pentagon
    print('ALL_SMALL_CYCLE_ATTACHMENT_PATTERNS_VERIFIED',cases)
    print('EXACT_CUT_SLOPE_VS_INDEPENDENT_FIRST_VARIATION_VERIFIED',cuts)
    print('SMALL_CYCLE_MAXIMUM_TABLE_VERIFIED')


def attached_mask(k,A,cycle_selected):
    S=set(cycle_selected)
    for j,v in enumerate(sorted(A)):
        if v in S:S.add(k+j)
    return sum(1<<v for v in S)


def verify_large_cycle_witnesses():
    cases=0
    for k in range(6,18):
        for A in ((0,), (0,1), tuple(range(k)), (0,)+tuple(range(2,k,2))):
            g=cycle_pendants(k,A)
            S={1,2,3}
            mask=attached_mask(k,A,S)
            K=cut_slope(g,mask)
            assert K >= 1, (k,A,K)
            cases+=1
    print('ALL_LONG_CYCLE_PENDANT_WITNESSES_VERIFIED',cases)


def verify_five_cycle_three_pendants():
    count=0
    for ell in range(3,6):
        for A in subset_masks(5,ell):
            omitted=next(v for v in range(5) if v not in A) if ell<5 else None
            # For all five marked, any omitted cycle vertex is still marked;
            # all other four marked already suffice for positivity.
            if omitted is None:omitted=0
            S={(omitted+2)%5,(omitted+3)%5}
            g=cycle_pendants(5,A)
            mask=attached_mask(5,A,S)
            K=cut_slope(g,mask)
            assert K>0,(A,omitted,K)
            count+=1
    assert count == 16
    print('ALL_FIVE_CYCLE_THREE_PLUS_PENDANTS_WITNESSES_VERIFIED',count)


def verify_bridge_identity():
    cases=0
    for n in range(2,12):
        # Every graph tested is a tree; all its edges are bridges.
        for edges in [ [(i,i+1) for i in range(n-1)],
                       [(0,i) for i in range(1,n)],
                       [(i, (i-1)//2) for i in range(1,n)]]:
            g=graph(n,edges)
            nbr,edges=g
            for u,v in edges:
                reachable={u}
                while True:
                    more={z for x in reachable for z in nbr[x] if (min(x,z),max(x,z)) != (u,v)}
                    if more<=reachable:break
                    reachable |= more
                mask=sum(1<<i for i in reachable)
                assert 0<mask<2**n-1
                val=cut_slope(g,mask)
                assert val == len(nbr[u])+len(nbr[v])-4,(n,u,v,val)
                cases+=1
    print('BRIDGE_DEGREE_SUM_IDENTITY_VERIFIED',cases)


def verify_lipschitz_separation():
    g=cycle_pendants(5,(0,1))
    f=(1,0,0,1,2,2,-1)
    nbr,edges=g
    assert max(abs(f[u]-f[v]) for u,v in edges)==1
    lap=[sum(f[i]-f[j] for j in nbr[i]) for i in range(len(f))]
    assert f[0]-f[1]==1 and -lap[0]+lap[1]==1
    assert max_slope(g)==0
    print('FIVE_CYCLE_BV_VERSUS_LIPSCHITZ_CONTRACTION_SEPARATION_VERIFIED')


def main():
    verify_small_cases()
    verify_large_cycle_witnesses()
    verify_five_cycle_three_pendants()
    verify_bridge_identity()
    verify_lipschitz_separation()
    print('ALL_GRAPH_BV_HEAT_CERTIFICATES_PASSED')

if __name__=='__main__':main()

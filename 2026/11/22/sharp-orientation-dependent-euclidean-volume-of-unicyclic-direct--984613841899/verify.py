#!/usr/bin/env python3
"""Independent integer-Gram checks for oriented unicyclic root polytopes.
Requires only Python's standard library. Run: python verify.py
"""
from itertools import product, combinations
from fractions import Fraction
from math import factorial, comb


def bareiss_det(A):
    n = len(A)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in A]
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            row = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if row is None:
                return 0
            a[k], a[row] = a[row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                val = a[i][j]*pivot - a[i][k]*a[k][j]
                assert val % previous == 0
                a[i][j] = val // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def gram_det(points):
    """Squared factorial-scaled intrinsic simplex volume of given points."""
    diffs = [[x-y for x, y in zip(p, points[-1])] for p in points[:-1]]
    gram = [[sum(x*y for x, y in zip(a,b)) for b in diffs] for a in diffs]
    return bareiss_det(gram)


def heights(n, edges, signs):
    adj = [[] for _ in range(n)]
    for (u, v), s in zip(edges, signs):
        adj[u].append((v, s))
        adj[v].append((u, -s))
    h = [None]*n
    h[0] = 0
    queue = [0]
    for u in queue:
        for v,d in adj[u]:
            if h[v] is None:
                h[v] = h[u]+d
                queue.append(v)
            else:
                assert h[v] == h[u]+d
    assert all(x is not None for x in h)
    return h


def check_graph(n, cycle_len, leaves):
    # 'leaves' lists (old vertex, new vertex) oriented in the listed order.
    assert n == cycle_len + len(leaves)
    edges = [(i,(i+1)%cycle_len) for i in range(cycle_len)] + leaves
    assert len(edges) == n
    checks = 0
    for signs in product((-1,1), repeat=n):
        P = []
        for (u,v),s in zip(edges,signs):
            x = [0]*n
            x[u] = -s
            x[v] = s
            P.append(x)
        imbalance = sum(signs[:cycle_len])
        if imbalance:
            # An n-vertex simplex of dimension n-1.
            actual = gram_det(P)
            expected = n*imbalance**2
            assert actual == expected, (edges,signs,'nonbalanced',actual,expected)
        else:
            h = heights(n,edges,signs)
            potential_energy = n*sum(t*t for t in h) - sum(h)**2
            assert potential_energy > 0
            # For every possible spanning-tree deletion, directly evaluate
            # the intrinsic squared simplex volume from its Euclidean Gram.
            for deleted in range(cycle_len):
                actual = gram_det(P[:deleted]+P[deleted+1:])
                assert actual == potential_energy, (edges,signs,'balanced',deleted,actual,potential_energy)
            # The area of the convex hull is (cycle_len/2) congruent-volume
            # spanning-tree simplices, as justified by its circuit triangulation.
        checks += 1
    return checks


def main():
    cases = [
        (3,3,[]), (4,4,[]), (5,4,[(0,4)]),
        (6,4,[(0,4),(4,5)]), (6,4,[(0,4),(2,5)]),
        (6,6,[]), (7,6,[(1,6)]),
        (8,6,[(0,6),(6,7)]), (8,6,[(0,6),(3,7)]),
        (8,8,[]),
    ]
    total = sum(check_graph(n,l,leaves) for n,l,leaves in cases)
    # Exact special-case comparison, one fixed graph and two leaf orientations:
    edges = [(0,1),(1,2),(2,3),(3,0),(0,4)]
    vals=[]
    for leaf_sign in (1,-1):
        h=heights(5,edges,[1,1,-1,-1,leaf_sign])
        vals.append(5*sum(t*t for t in h)-sum(h)**2)
    assert vals == [10,26], vals
    # General two-block / alternating energies by direct exact sums.
    for n in range(4,42,2):
        signs_alt=[1,-1]*(n//2)
        signs_block=[1]*(n//2)+[-1]*(n//2)
        for signs, target_48 in ((signs_alt,12*n), (signs_block,n*(n*n+8))):
            h=[0]
            for s in signs[:-1]:h.append(h[-1]+s)
            energy_48=48*(n*sum(t*t for t in h)-sum(h)**2)
            # 48*n*variance = 48*(n sum h²-(sum h)²).
            assert energy_48 == target_48*n, (n,energy_48,target_48*n)
    # Average centered potential norm over all equally balanced cycle orientations.
    for n in (4, 6, 8, 10):
        energies = []
        for pos in combinations(range(n),n//2):
            ss = [1 if i in pos else -1 for i in range(n)]
            h = [0]
            for sign in ss[:-1]:h.append(h[-1]+sign)
            energies.append(Fraction(n*sum(t*t for t in h)-sum(h)**2,n))
        mean = sum(energies, Fraction(0))/len(energies)
        assert mean == Fraction(n*(n+1),12), (n,mean)
    # Four-cycle with any number of leaves attached at vertex zero.
    for t in range(1,16):
        n=t+4
        energies=[]
        edges=[(0,1),(1,2),(2,3),(3,0)]+[(0,4+j) for j in range(t)]
        for a in range(t+1):
            signs=[1,1,-1,-1]+[1]*a+[-1]*(t-a)
            h=heights(n,edges,signs)
            H=n*sum(v*v for v in h)-sum(h)**2
            formula=n*(t+6)-(4+2*a-t)**2
            assert H==formula,(t,a,H,formula)
            energies.append(H)
        delta= min(abs(4+2*a-t) for a in range(t+1))
        assert min(energies)==2*n
        assert max(energies)==n*(n+2)-delta**2
    print(f'UNICYCLIC_DIRECTED_ROOT_METRIC_PASS orientations={total} graphs={len(cases)} special_energy=[10,26] balanced_means=4,6,8,10 leaf_extrema_t=1..15')

if __name__ == '__main__':
    main()

"""Exact edge-conditioned degree-law checks for uniform bipartite spanning trees.

Run: python verify_edge_degree.py
Uses only Python's standard library. All probability comparisons are rational.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from math import comb


def is_tree(vertex_count, edge_subset):
    parent = list(range(vertex_count))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j in edge_subset:
        u, v = find(i), find(j)
        if u == v:
            return False
        parent[u] = v
    return len({find(i) for i in range(vertex_count)}) == 1


def binomial_pmf(k, number, denom):
    if not (0 <= k <= number):
        return Fraction(0)
    return Fraction(comb(number, k) * (denom-1)**(number-k), denom**number)


def expected_distribution(a,b,condition):
    # The marked pair is (left vertex 0, right vertex a).
    out = Counter()
    for i in range(1,b+1):
        for j in range(1,a+1):
            if condition:
                p = Fraction(0)
                for x,y,w in ((1,0,b-1),(0,1,a-1),(1,1,1)):
                    p += Fraction(w,a+b-1)*binomial_pmf(i-1-x,b-2,a)*binomial_pmf(j-1-y,a-2,b)
            else:
                p = binomial_pmf(i-1,b-2,a)*binomial_pmf(j-1,a-2,b)
            if p:
                out[(i,j)] = p
    return out


def check(a,b):
    edges = [(i,a+j) for i in range(a) for j in range(b)]
    dists={False:Counter(),True:Counter()}
    for idxs in combinations(range(a*b), a+b-1):
        tree=[edges[k] for k in idxs]
        if not is_tree(a+b,tree):
            continue
        d_u=sum(0 in edge for edge in tree)
        d_v=sum(a in edge for edge in tree)
        present=(0,a) in tree
        dists[present][(d_u,d_v)]+=1
    total=sum(sum(d.values()) for d in dists.values())
    assert total == a**(b-1)*b**(a-1), (a,b,total)
    assert Fraction(sum(dists[True].values()),total)==Fraction(a+b-1,a*b)
    for present in (False,True):
        c=sum(dists[present].values())
        actual={k:Fraction(v,c) for k,v in dists[present].items()}
        expected=dict(expected_distribution(a,b,present))
        assert actual==expected,(a,b,present,actual,expected)
        eu=sum(Fraction(i)*p for (i,j),p in actual.items())
        ev=sum(Fraction(j)*p for (i,j),p in actual.items())
        euv=sum(Fraction(i*j)*p for (i,j),p in actual.items())
        cov=euv-eu*ev
        assert cov == (Fraction(-(a-1)*(b-1),(a+b-1)**2) if present else 0)
    return total

if __name__=='__main__':
    total=0
    for a in range(2,5):
        for b in range(2,5):
            v=check(a,b)
            total+=v
            print(f'EXACT_PASS K_{{{a},{b}}} {v} spanning trees')
    print('VERIFY_OK',total, 'labeled spanning trees in nine parameter pairs')

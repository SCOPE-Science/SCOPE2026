"""Exact small-case verification of commuting graphs in cubic-nilpotent semigroups.

Uses only Python's standard library. Exhaustively enumerates all product maps
and confirms the conditional graph law and maximum commuting subsemigroup size.
"""
from itertools import product
from collections import Counter
from math import comb


def graph_mask(table, r):
    edge = 0
    idx = 0
    for u in range(r):
        for v in range(u + 1, r):
            if table[u*r+v] == table[v*r+u]:
                edge |= 1 << idx
            idx += 1
    return edge


def clique_number(mask, r):
    edges = {}
    idx = 0
    for u in range(r):
        for v in range(u+1,r):
            edges[(u,v)] = bool(mask & (1<<idx))
            idx += 1
    best=0
    for subset in range(1<<r):
        vs=[i for i in range(r) if (subset>>i)&1]
        if all(edges[(u,v)] for u in vs for v in vs if u < v):
            best=max(best,len(vs))
    return best


def formula(r,b,k):
    m=comb(r,2)
    return sum((-1)**j*comb(b-1,j)*(b-j)**(r+k)*((b-j)*(b-j-1))**(m-k)
               for j in range(b))


def denominator(r,b):
    return sum((-1)**j*comb(b-1,j)*(b-j)**(r*r) for j in range(b))


def verify(r,b):
    m=comb(r,2)
    histogram=Counter()
    total=0
    maxsize_hist=Counter()
    for table in product(range(b),repeat=r*r):
        if not set(range(1,b)).issubset(table):
            continue
        mask=graph_mask(table,r)
        histogram[mask]+=1
        total+=1
        maxsize_hist[b+clique_number(mask,r)]+=1
    assert total == denominator(r,b), (r,b,'denominator')
    for mask in range(1<<m):
        assert histogram[mask] == formula(r,b,mask.bit_count()),(r,b,mask)
    assert sum(maxsize_hist.values()) == total
    # Each graph class is exchangeable under relabeling of its edges.
    for k in range(m+1):
        assert len({histogram[mask] for mask in range(1<<m)
                    if mask.bit_count() == k}) == 1
    print(f'PASS r={r} b={b} maps={total} graphs={1<<m} max-commuting-sizes={dict(sorted(maxsize_hist.items()))}')


if __name__=='__main__':
    for r,b in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)]:
        verify(r,b)
    print('ALL EXACT TESTS PASS')

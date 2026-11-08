"""Finite checks for rank-three first-order profiles of Hamming and Johnson graphs.

This is a finite regression test, not a substitute for the uniform proof.
Run: python3 checker.py
"""
from itertools import combinations, product
from math import comb


def mask_of_counts(c):
    return sum(1 << j for j, count in enumerate(c) if count > 0)


def h_analytic(d, q):
    if q == 1:
        return ()
    v, r = q ** d, d * (q - 1)
    ans = set()
    for h in range(1, d + 1):
        if h == 1:
            common, exclusive = q - 2, (d - 1) * (q - 1)
        elif h == 2:
            common, exclusive = 2, r - 2
        else:
            common, exclusive = 0, r
        neither = v - 2 - common - 2 * exclusive
        assert min(common, exclusive, neither) >= 0, (d, q, h)
        ans.add((int(h == 1), mask_of_counts((neither, exclusive, exclusive, common))))
    return tuple(sorted(ans))


def j_analytic(n, k):
    k = min(k, n-k)
    if k == 0: return ()
    v, r = comb(n,k), k * (n-k)
    ans = set()
    for h in range(1, k+1):
        if h == 1:
            common, exclusive = n-2, r-n+1
        elif h == 2:
            common, exclusive = 4, r-4
        else:
            common, exclusive = 0, r
        neither = v-2-common-2*exclusive
        assert min(common, exclusive, neither) >= 0, (n,k,h)
        ans.add((int(h == 1), mask_of_counts((neither, exclusive, exclusive, common))))
    return tuple(sorted(ans))


def graph_signature(vertices, neighbours):
    v = len(vertices)
    assert v > 0
    full = (1 << v) - 1
    root = 0
    assert all(0 <= x < v for neighbourhood in neighbours for x in neighbourhood)
    neigh = [sum(1 << j for j in a) for a in neighbours]
    assert all(not (neigh[i] & (1 << i)) for i in range(v))
    assert all(bool(neigh[i] & (1 << j)) == bool(neigh[j] & (1 << i)) for i in range(v) for j in neighbours[i])
    seen = set()
    for j in range(1, v):
        e = int(bool(neigh[root] & (1 << j)))
        third = full ^ (1 << root) ^ (1 << j)
        n11 = (neigh[root] & neigh[j] & third).bit_count()
        n10 = (neigh[root] & ~neigh[j] & third).bit_count()
        n01 = (~neigh[root] & neigh[j] & third).bit_count()
        n00 = (third & ~(neigh[root] | neigh[j])).bit_count()
        assert n00+n01+n10+n11 == v-2
        seen.add((e, mask_of_counts((n00, n01, n10, n11))))
    return tuple(sorted(seen))


def h_direct(d,q):
    verts = list(product(range(q),repeat=d))
    index = {v:i for i,v in enumerate(verts)}
    adj=[]
    for v in verts:
        row=set()
        for a in range(d):
            for b in range(q):
                if b != v[a]:
                    w = v[:a]+(b,)+v[a+1:]
                    row.add(index[w])
        adj.append(row)
    return graph_signature(verts,adj)


def j_direct(n,k):
    verts = list(combinations(range(n),k))
    idx = {v:i for i,v in enumerate(verts)}
    adj=[]
    for v in verts:
        sv=set(v);row=set()
        for a in v:
            for b in range(n):
                if b not in sv:
                    w=tuple(sorted(sv-{a}|{b}))
                    row.add(idx[w])
        adj.append(row)
    return graph_signature(verts,adj)


def h_class(d,q):
    if q==1: return 'singleton'
    if d==1:
        return 'K2' if q==2 else 'K>=3'
    if (d,q)==(2,2):return 'square'
    if q==2:
        return 'cube3' if d==3 else 'hypercube>=4'
    return 'rook2,q>=3' if d==2 else 'generic d>=3,q>=3'


def main():
    seen={}
    checks=0
    for d in range(1,9):
        for q in range(1,9):
            sig=h_analytic(d,q)
            klass=h_class(d,q)
            if klass in seen:assert seen[klass]==sig,(d,q,klass,sig,seen[klass])
            else:seen[klass]=sig
            if q**d<=800:
                assert h_direct(d,q)==sig,(d,q,h_direct(d,q),sig)
                checks+=1
    assert len(seen)==8, seen
    assert len(set(seen.values()))==8, seen
    for n in range(1,12):
        for k in range(n+1):
            sig = j_analytic(n,k)
            if comb(n,k)<=800:
                assert j_direct(n,k)==sig,(n,k,sig,j_direct(n,k))
                checks+=1
    assert h_analytic(2,3)==j_analytic(6,2)
    assert h_analytic(3,3)==j_analytic(7,3)
    assert h_analytic(3,2)!=h_analytic(4,2)
    assert h_analytic(2,3)!=h_analytic(3,3)
    assert h_analytic(3,3)!=h_analytic(4,2)
    assert all(h_analytic(d,q)==h_analytic(3,3) for d in range(3,11) for q in range(3,11))
    assert all(h_analytic(d,2)==h_analytic(4,2) for d in range(4,11))
    print('RANK_THREE_HAMMING_CHECKS_OK', 'direct_graph_checks=',checks,'classes=',len(seen))
    for key,sig in seen.items():print('  ',key,':',sig)

if __name__=='__main__':main()

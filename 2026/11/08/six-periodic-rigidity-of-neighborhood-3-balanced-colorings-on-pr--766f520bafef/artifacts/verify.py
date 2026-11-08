#!/usr/bin/env python3
"""Exact finite checks of 3-balanced ladder colouring formulas.
Python 3 standard library; no external scientific or network dependencies.
The unrestricted theorem is proved separately from these checks.
"""
from itertools import product

COLORS = range(3)
COLS = tuple(product(COLORS, repeat=2))
PAIRS = tuple(product(COLS, repeat=2))
INDEX = {s: i for i, s in enumerate(PAIRS)}


def graph(n, twisted):
    """Rows r=0,1, columns i=0,...,n-1."""
    assert n >= 3
    adj = [set() for _ in range(2*n)]
    def edge(u, v):
        assert u != v
        adj[u].add(v); adj[v].add(u)
    for i in range(n):
        edge(i, n+i)
    for r in (0, 1):
        for i in range(n-1):
            edge(r*n+i, r*n+i+1)
        edge(r*n+n-1, ((1-r) if twisted else r)*n)
    assert all(len(s) == 3 for s in adj)
    return adj


def balanced(labels, adj):
    return all({labels[u] for u in nbrs} == {0, 1, 2} for nbrs in adj)


def formula(n, twisted):
    if n % 3:
        return 0
    if n % 6 == 3:
        return 36 if twisted else 6
    return 6 if twisted else 36


def patterns():
    seqs = []
    for aa in product(COLORS, repeat=4):
        if aa[0] == aa[2] or aa[1] == aa[3]:
            continue
        a = list(aa)
        a += [(-a[0]-a[2])%3, (-a[1]-a[3])%3]
        seq = tuple((a[i],a[(i+3)%6]) for i in range(6))
        seqs.append(seq)
    assert len(seqs) == 36 and len(set(seqs)) == 36
    return seqs


def count_patterns(n, twisted):
    adj = graph(n, twisted)
    count=0
    for seq in patterns():
        if twisted:
            if not all(seq[(i+n)%6] == seq[i][::-1] for i in range(6)):
                continue
        elif not all(seq[(i+n)%6] == seq[i] for i in range(6)):
            continue
        labels = tuple(seq[i % 6][0] for i in range(n)) + tuple(seq[i % 6][1] for i in range(n))
        assert balanced(labels, adj)
        count += 1
    return count


def transfer_counts(nmax=72):
    """Independent 81-state local-neighbour transfer, ordinary & twisted trace."""
    T = [INDEX[(p[::-1], q[::-1])] for p,q in PAIRS]
    neighbors = []
    for p,q in PAIRS:
        row = []
        for r in COLS:
            if len({p[0], r[0], q[1]}) == 3 and len({p[1], r[1], q[0]}) == 3:
                row.append(INDEX[(q,r)])
        neighbors.append(row)
    rows = [{i: 1} for i in range(len(PAIRS))]  # A^0
    for n in range(1,nmax+1):
        new=[]
        for row in rows:
            d={}
            for j,val in row.items():
                for k in neighbors[j]:
                    d[k] = d.get(k,0)+val
            new.append(d)
        rows=new
        if n >= 3:
            cyl = sum(row.get(i,0) for i,row in enumerate(rows))
            mob = sum(row.get(T[i],0) for i,row in enumerate(rows))
            assert cyl == formula(n,False), (n,cyl)
            assert mob == formula(n,True), (n,mob)
    return nmax


def brute(n, twisted):
    adj=graph(n,twisted)
    return sum(balanced(labels,adj) for labels in product(COLORS,repeat=2*n))


def main():
    # Full vertex-label enumeration, entirely independent of pattern/transfer code.
    for n in range(3,7):
        for twisted in (False,True):
            x = brute(n,twisted)
            assert x == formula(n,twisted), (n,twisted,x)
            print('DIRECT_ALL_VERTEX_LABELS_OK',n,'twisted='+str(twisted),x)
    assert transfer_counts(72)==72
    print('INDEPENDENT_81_STATE_TRACE_AND_TWISTED_TRACE_OK n=3..72')
    for n in range(3,121):
        for twisted in (False,True):
            assert count_patterns(n,twisted)==formula(n,twisted)
    print('EXPLICIT_PERIOD_SIX_PATTERNS_AND_GRAPH_NEIGHBORHOODS_OK n=3..120')
    print('VERIFY_OK')

if __name__ == '__main__':main()

"""Standalone exact checker for the pattern 10100... on graphs of degree at most four."""
from itertools import combinations
from random import Random

def rank_consistent(rows, rhs, n):
    a = [rows[i] | (rhs[i] << n) for i in range(len(rows))]
    r = 0
    for j in range(n):
        pivot = next((i for i in range(r, len(a)) if (a[i] >> j) & 1), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for i in range(len(a)):
            if i != r and (a[i] >> j) & 1:
                a[i] ^= a[r]
        r += 1
    return r, all((a[i] & ((1 << n) - 1)) or not ((a[i] >> n) & 1) for i in range(r, len(a)))

def rank_count(edges, n, pinned1=0, pinned0=0, exceptional=0):
    adj = [0]*n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    rows = [adj[i] | (1 << i) for i in range(n)]
    rhs = [1 ^ ((exceptional >> i)&1) for i in range(n)]
    for i in range(n):
        if pinned1 >> i & 1:
            rows.append(1 << i)
            rhs.append(1)
        if pinned0 >> i & 1:
            rows.append(1 << i)
            rhs.append(0)
    r, ok = rank_consistent(rows, rhs, n)
    return (1 << (n-r)) if ok else 0

def ie_count(edges, n):
    adj = [0]*n
    for u,v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    heavy = [v for v in range(n) if adj[v].bit_count() == 4]
    total = 0
    for b in range(1 << len(heavy)):
        B = [heavy[j] for j in range(len(heavy)) if b >> j & 1]
        R = [v for v in heavy if v not in B]
        for j in range(1 << len(R)):
            J = [R[i] for i in range(len(R)) if j >> i & 1]
            pinned1 = 0
            for v in B + J:
                pinned1 |= adj[v]
            pinned0 = sum(1 << v for v in B)
            total += (-1 if j.bit_count() & 1 else 1) * rank_count(edges,n,pinned1,pinned0,pinned0)
    return total

def direct_count(edges, n):
    adj = [0]*n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return sum(all(bool(s >> v & 1) == (((s & adj[v]).bit_count()) in (0, 2))
                   for v in range(n)) for s in range(1 << n))

def run():
    tests = 0
    for n in range(1, 6):
        pairs = list(combinations(range(n), 2))
        for g in range(1 << len(pairs)):
            edges=[e for j,e in enumerate(pairs) if g >> j & 1]
            assert ie_count(edges,n) == direct_count(edges,n), (n,g,'IE')
            assert direct_count(edges,n) >= 1, (n,g,'small-n')
            tests += 1
    rng=Random(0x5EED)
    for n in (6,7,8):
        pairs=list(combinations(range(n),2))
        for _ in range(700):
            edges=[e for e in pairs if rng.randrange(4)==0]
            if max((sum(v in e for e in edges) for v in range(n)),default=0)>4: continue
            assert ie_count(edges,n)==direct_count(edges,n),(n,edges)
            tests += 1
    w=[(0,1),(0,2),(0,4),(0,5),(1,2),(2,3),(2,5),(3,4)]
    assert direct_count(w,6)==ie_count(w,6)==0
    assert rank_count(w,6)==1
    print('VERIFY_OK', 'graphs=',tests,'witness_edges=',len(w))

if __name__=='__main__':
    run()

"""Standalone finite sanity checks for the cograph adjacency-trace theorem.

Run: python verify.py. Uses only Python's standard library. These finite checks
supplement, but do not replace, the all-size cotree induction.
"""
import itertools


def edges_from_mask(n, mask):
    pairs = list(itertools.combinations(range(n), 2))
    adj = [0] * n
    for k, (u, v) in enumerate(pairs):
        if (mask >> k) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return adj


def is_cograph(adj):
    for vs in itertools.combinations(range(len(adj)), 4):
        degrees = [sum((adj[x] >> y) & 1 for y in vs if x != y) for x in vs]
        if sorted(degrees) == [1, 1, 2, 2]:
            return False
    return True


def traces(adj, A):
    return {tuple((row >> a) & 1 for a in A) for row in adj}


def threshold_witness(m):
    # m clique vertices and m independent vertices with prefix neighborhoods.
    # Their sizes are 0,1,...,m-2,m (and for m=1, just 1).
    lengths = list(range(max(0, m - 1))) + [m]
    assert len(lengths) == m
    n = 2 * m
    adj = [0] * n
    for i in range(m):
        for j in range(i+1, m):
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    for b, length in enumerate(lengths, m):
        for i in range(length):
            adj[b] |= 1 << i
            adj[i] |= 1 << b
    return adj


def graph_with_trace_count(m, k):
    if k == 1:
        return [0] * m
    if k == 2:
        if m == 1:
            return [2, 1]
        n=m; adj=[0] * n
        for j in range(1, n):
            adj[0] |= 1 << j
            adj[j] |= 1
        return adj
    if k <= m:
        adj=[0] * m
        for i in range(k-1):
            for j in range(i+1, k-1):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
        return adj
    # Start from clique A and add k-m independent witnesses with new traces.
    lengths = list(range(max(0, m-1))) + [m]
    lengths = lengths[:k-m]
    n=m+len(lengths); adj=[0]*n
    for i in range(m):
        for j in range(i+1,m):
            adj[i] |= 1<<j; adj[j] |= 1<<i
    for b, length in enumerate(lengths,m):
        for i in range(length):
            adj[b] |= 1<<i; adj[i] |= 1<<b
    return adj


def run():
    graphs=sets=0
    for n in range(1,7):
        max_mask=1 << (n*(n-1)//2)
        for mask in range(max_mask):
            adj=edges_from_mask(n,mask)
            if not is_cograph(adj):
                continue
            graphs += 1
            for amask in range(1,1<<n):
                A=[v for v in range(n) if (amask>>v)&1]
                assert len(traces(adj,A))<=2*len(A)
                sets+=1
    for m in range(1,15):
        adj=threshold_witness(m)
        assert is_cograph(adj)
        assert len(traces(adj,range(m)))==2*m
    spectra=0
    for m in range(1,12):
        for k in range(1,2*m+1):
            adj=graph_with_trace_count(m,k)
            assert is_cograph(adj),(m,k)
            assert len(traces(adj,range(m)))==k,(m,k,len(traces(adj,range(m))))
            spectra+=1
    print(f'VERIFY_OK exhaustive_cographs={graphs} exhaustive_parameter_sets={sets} extremal_sizes=14 spectra={spectra}')

if __name__=='__main__':
    run()

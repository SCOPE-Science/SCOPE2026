"""Independent binary-growth encoding of optimal cycle cutwidth orders.

Run: python verification/flux_graph.py
No permutation enumeration or graph-library dependencies are used.
"""
from collections import Counter, deque
from math import comb


def build(n):
    m = n-2
    width = 1 << m
    verts = n*width
    adj = [[] for _ in range(verts)]
    for u in range(verts):
        root, bits = divmod(u, width)
        # Exchange first two ordered vertices: one particle at left boundary.
        direction = 1 if (bits & 1) else -1
        adj[u].append(((root+direction) % n)*width + (bits ^ 1))
        # Exchange last two ordered vertices: toggle right-boundary bit.
        adj[u].append(root*width + (bits ^ (1 << (m-1))))
        # Interior exchanges swap consecutive opposite growth decisions.
        for j in range(m-1):
            if ((bits >> j) & 1) != ((bits >> (j+1)) & 1):
                adj[u].append(root*width + (bits ^ (3 << j)))
    return adj


def distances(adj, seed):
    d = [-1]*len(adj)
    d[seed] = 0
    queue = deque([seed])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                queue.append(v)
    return d


def check(n):
    adj = build(n)
    m = n - 2
    width = 1 << m
    assert len(adj) == n*(2**m)
    degree = Counter(map(len, adj))
    assert degree == Counter({2+j: 2*n*comb(n-3,j) for j in range(n-2)})
    assert sum(map(len,adj))//2 == n*(n+1)*2**(n-4)
    for u, neighbors in enumerate(adj):
        assert len(neighbors) == len(set(neighbors))
        for v in neighbors:
            assert u in adj[v]
    # Every root rotation of the all-clockwise order has exact transport cost.
    b = width-1
    d = distances(adj, b)
    assert -1 not in d
    for k in range(n):
        assert d[k*width+b] == (n-1)*min(k,n-k)
    return n, len(adj), sum(map(len,adj))//2, max(d)


if __name__ == '__main__':
    for n in range(3, 15):
        print('FLUX_OK', *check(n))

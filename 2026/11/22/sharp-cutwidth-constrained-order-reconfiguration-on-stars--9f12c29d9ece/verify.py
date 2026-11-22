"""Independent finite checks for cutwidth-constrained star order graphs.

Requires Python 3 standard library. Execute: python verify.py
"""
from itertools import permutations
from collections import deque, Counter
from math import factorial, comb


def cutwidth_star(order, r):
    hub = r
    maximum = 0
    prefix = set()
    for v in order:
        prefix.add(v)
        maximum = max(maximum,
                      sum((hub in prefix) != (leaf in prefix)
                          for leaf in range(r)))
    return maximum


def kendall(p, q):
    ranks = {v: i for i, v in enumerate(q)}
    return sum(ranks[p[i]] > ranks[p[j]]
               for i in range(len(p)) for j in range(i+1, len(p)))


def make_graph(r, k):
    # Construct independently from the graph and its cutwidth, not the formula.
    n = r + 1
    vertices = [p for p in permutations(range(n)) if cutwidth_star(p, r) <= k]
    pos = {p: i for i, p in enumerate(vertices)}
    adjacency = [[] for _ in vertices]
    for i, p in enumerate(vertices):
        for a in range(r):
            q = list(p)
            q[a], q[a+1] = q[a+1], q[a]
            j = pos.get(tuple(q))
            if j is not None:
                adjacency[i].append(j)
    return vertices, pos, adjacency


def bfs(adjacency, start):
    dist = {start: 0}
    todo = deque([start])
    while todo:
        u = todo.popleft()
        for v in adjacency[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                todo.append(v)
    return dist


def verify(r, k):
    vertices, pos, adj = make_graph(r, k)
    if k < (r + 1) // 2:
        assert not vertices
        return (r, k, 0, 0)
    L, U = r-k, k
    h = U - L + 1
    assert len(vertices) == h * factorial(r)
    assert all(L <= p.index(r) <= U for p in vertices)
    if h == 1:
        c = L
        expected_comps = comb(r, c)
        component_size = factorial(c) * factorial(r-c)
        exp_diam = comb(c, 2) + comb(r-c, 2)
        assert len(vertices) == expected_comps * component_size
        seen = set()
        count = 0
        for i, p in enumerate(vertices):
            if i in seen:
                continue
            d = bfs(adj, i)
            assert len(d) == component_size
            assert max(d.values()) == exp_diam
            assert all({x for x in vertices[j][:c]} == set(p[:c])
                       for j in d)
            assert all(d[j] == kendall(p, vertices[j]) for j in d)
            seen.update(d)
            count += 1
        assert count == expected_comps
    else:
        # Leaf-label relabelling is a graph automorphism; one representative
        # for each possible hub position checks every ordered vertex pair.
        for c in range(L, U+1):
            p = tuple(list(range(c)) + [r] + list(range(c, r)))
            d = bfs(adj, pos[p])
            assert len(d) == len(vertices)
            assert all(d[i] == kendall(p, q) for i, q in enumerate(vertices))
            assert max(d.values()) == comb(r+1, 2)
        assert all(tuple(reversed(p)) in pos for p in vertices)
    expected_edges = (h * (r-2) * factorial(r) // 2 +
                      (h-1) * factorial(r)) if k < r else (r * factorial(r+1) // 2)
    assert sum(map(len, adj)) // 2 == expected_edges
    return (r, k, len(vertices), expected_edges)


def main():
    checked = []
    for r in range(2, 8):
        for k in range(r+1):
            checked.append(verify(r, k))
    for r,k in ((8,4),(8,5)):
        checked.append(verify(r,k))
    for r,k,v,e in checked:
        print(f'r={r}, k={k}, vertices={v}, edges={e}')
    print('PASS: exact direct cutwidth, adjacency, connectivity, all pair distances via')
    print('leaf-relabeling orbits, component diameters, total diameters, edge counts.')
    print(f'Checked {len(checked)} parameter pairs, including r=8, k=5.')

if __name__=='__main__':
    main()

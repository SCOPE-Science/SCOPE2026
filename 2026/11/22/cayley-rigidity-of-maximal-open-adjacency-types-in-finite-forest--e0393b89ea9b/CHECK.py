"""Reproducible finite checks for adjacency traces of finite forests.

Run: python3 CHECK.py
Only the Python standard library is required. This program checks finite cases;
all-size statements are established by the proof, not by this enumeration.
"""
from itertools import combinations, product


def is_forest(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        a, b = find(u), find(v)
        if a == b:
            return False
        parent[a] = b
    return True


def family(n, edges, A):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    marked = set(A)
    return frozenset(frozenset(adj[v] & marked) for v in range(n))


def nontrivial_marked_components(n, edges, A):
    A = set(A)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, v in edges:
        if u in A and v in A:
            parent[find(u)] = find(v)
    comps = {}
    for v in A:
        r = find(v)
        comps[r] = comps.get(r, 0) + 1
    return sum(size >= 2 for size in comps.values())


def prufer_tree(code, n):
    if n == 1:
        return []
    if n == 2:
        return [(0, 1)]
    deg = [1] * n
    for v in code:
        deg[v] += 1
    out = []
    for v in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        out.append((leaf, v))
        deg[leaf] -= 1
        deg[v] -= 1
    u, v = [i for i in range(n) if deg[i] == 1]
    out.append((u, v))
    return out


def witness(m, tree_edges):
    edges = []
    next_vertex = m
    for u, v in tree_edges:
        edges.extend(((u, next_vertex), (v, next_vertex)))
        next_vertex += 1
    for u in range(m):
        edges.append((u, next_vertex))
        next_vertex += 1
    return next_vertex, edges


def verify():
    checked = 0
    maximizers = 0
    for n in range(1, 7):
        possible = list(combinations(range(n), 2))
        for bits in range(1 << len(possible)):
            edges = [e for j, e in enumerate(possible) if (bits >> j) & 1]
            if not is_forest(n, edges):
                continue
            for m in range(1, n + 1):
                for A in combinations(range(n), m):
                    checked += 1
                    traces = family(n, edges, A)
                    t = nontrivial_marked_components(n, edges, A)
                    assert len(traces) <= 2*m - t
                    if len(traces) == 2*m:
                        maximizers += 1
                        assert t == 0
                        remaining = traces - {frozenset()} - {frozenset((a,)) for a in A}
                        assert len(remaining) == m-1
                        assert all(len(B) == 2 for B in remaining)
                        # The nontrivial traces are exactly edges of a tree on A.
                        index = {a:i for i,a in enumerate(A)}
                        assert is_forest(m, [(index[u],index[v]) for B in remaining for u,v in [tuple(B)]])
                        assert n >= 3*m - 1
    print('EXHAUSTIVE_FOREST_PASS', checked, 'MAXIMIZERS', maximizers)
    for m in range(1, 18):
        edges = [(i, i+1) for i in range(m-1)]
        n, E = witness(m, edges)
        assert n == 3*m-1 and is_forest(n, E)
        assert family(n,E,range(m)) == frozenset([frozenset()] + [frozenset((i,)) for i in range(m)] + [frozenset(e) for e in edges])
    print('ALL_ORDER_PATH_WITNESSES_PASS',17)
    for m in range(2, 6):
        got = set()
        for code in product(range(m), repeat=m-2):
            T = prufer_tree(code,m)
            n,E=witness(m,T)
            fam = family(n,E,range(m))
            assert len(fam)==2*m
            got.add(fam)
        assert len(got) == m**(m-2)
        print('CAYLEY_EXTREMAL_FAMILIES_PASS', m, len(got))
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    verify()

"""Direct finite-field verification of retraction commutation graphs.

Uses generator-image enumeration and full bracket/linear-map checks; it does
not construct candidates from the claimed graph decomposition.
"""
from itertools import product
from collections import Counter, deque


def bracket(a, b, q, kind):
    n = len(a)
    out = [0] * n
    if kind == 'filiform':
        for j in range(1, n-1):
            out[j+1] = (a[0]*b[j] - a[j]*b[0]) % q
    elif kind == 'free3':
        assert n == 5
        out[2] = (a[0]*b[1] - a[1]*b[0]) % q
        out[3] = (a[0]*b[2] - a[2]*b[0]) % q
        out[4] = (a[1]*b[2] - a[2]*b[1]) % q
    else:
        raise ValueError(kind)
    return tuple(out)


def apply(columns, vector, q):
    n = len(vector)
    return tuple(sum(vector[j]*columns[j][i] for j in range(n)) % q
                 for i in range(n))


def build_map(u, v, q, kind):
    n = len(u)
    cols = [u, v]
    z = bracket(u, v, q, kind)
    cols.append(z)
    if kind == 'filiform':
        while len(cols) < n:
            cols.append(bracket(u, cols[-1], q, kind))
    else:
        cols.append(bracket(u, z, q, kind))
        cols.append(bracket(v, z, q, kind))
    basis = [tuple(int(i == j) for i in range(n)) for j in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            left = apply(cols, bracket(basis[i], basis[j], q, kind), q)
            right = bracket(cols[i], cols[j], q, kind)
            if left != right:
                return None
    return tuple(cols)


def compose(f, g, q):
    return tuple(apply(f, v, q) for v in g)


def verify(n, q, kind):
    if kind == 'free3' and n != 5:
        return
    Z = tuple((0,)*n for _ in range(n))
    I = tuple(tuple(int(i == j) for i in range(n)) for j in range(n))
    vecs = list(product(range(q), repeat=n))
    E = []
    endos = 0
    for u in vecs:
        for v in vecs:
            f = build_map(u, v, q, kind)
            if f is None:
                continue
            endos += 1
            if compose(f, f, q) == f:
                E.append(f)
    assert len(set(E)) == len(E), 'Nonunique generator images'
    expected = q * (q+1) * q**(n-2) + 2
    assert len(E) == expected, (kind, n, q, len(E), expected)
    R = [f for f in E if f not in (Z, I)]
    adj = {i: set() for i in range(len(R))}
    for i in range(len(R)):
        for j in range(i+1, len(R)):
            if compose(R[i], R[j], q) == compose(R[j], R[i], q):
                adj[i].add(j)
                adj[j].add(i)
                assert compose(R[i], R[j], q) == Z
    target_degree = q**(n-2)
    assert all(len(neigh) == target_degree for neigh in adj.values())
    seen = set()
    comp_sizes = []
    for k in adj:
        if k in seen:
            continue
        stack = [k]
        seen.add(k)
        component = []
        while stack:
            v = stack.pop()
            component.append(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        comp_sizes.append(len(component))
        assert len(component) == 2*target_degree
        assert all(len(adj[v].intersection(component)) == target_degree for v in component)
        # A regular bipartite graph of 2d vertices with d vertices on each
        # side and every vertex of degree d must be K_(d,d).
        left = {component[0]} | set(adj[component[0]])
        a = adj[component[0]]
        b = set(component)-a
        assert len(a)==len(b)==target_degree
        assert all(adj[v] == b for v in a)
        assert all(adj[v] == a for v in b)
    expected_components = q*(q+1)//2
    assert len(comp_sizes) == expected_components
    print(f'{kind} n={n} q={q}: endomorphisms={endos}, retractions={len(E)}, graph_components={len(comp_sizes)}, edges={sum(map(len,adj.values()))//2}')


if __name__ == '__main__':
    for params in [
        (3,2,'filiform'), (3,3,'filiform'), (4,2,'filiform'),
        (4,3,'filiform'), (5,2,'filiform'), (5,3,'filiform'),
        (5,2,'free3'), (5,3,'free3')
    ]:
        verify(*params)
    print('TWO_GENERATOR_LIE_RETRACTION_GRAPH_VERIFIED')

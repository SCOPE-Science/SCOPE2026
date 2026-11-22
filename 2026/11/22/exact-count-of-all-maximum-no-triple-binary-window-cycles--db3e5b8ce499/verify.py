"""Exact enumerator for optimal binary no-triple universal cycles.

Run: python3 verify.py (Python 3 standard library only).
"""
from itertools import product
from collections import Counter, defaultdict, deque
from math import factorial


def allowed(w):
    return all(not (w[i] == w[i + 1] == w[i + 2]) for i in range(len(w) - 2))


def edges(n):
    return ["".join(z) for z in product("01", repeat=n)
            if allowed(z) and not (z[0] == z[1] and z[-1] == z[-2])]


def graph(n):
    E = edges(n)
    V = sorted(set(e[:-1] for e in E) | set(e[1:] for e in E))
    out = defaultdict(list)
    indeg = Counter()
    for w in E:
        out[w[:-1]].append((w[1:], w))
        indeg[w[1:]] += 1
    assert all(len(out[v]) == indeg[v] in (1,2) for v in V)
    return V, E, out


def bareiss_det(M):
    """Exact fraction-free integer determinant, with row pivoting."""
    N = len(M)
    if N == 0:
        return 1
    A = [list(row) for row in M]
    prev, sign = 1, 1
    for k in range(N - 1):
        if A[k][k] == 0:
            j = next((j for j in range(k + 1, N) if A[j][k]), None)
            if j is None:
                return 0
            A[k], A[j] = A[j], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, N):
            old = A[i][k]
            for j in range(k + 1, N):
                num = pivot * A[i][j] - old * A[k][j]
                assert num % prev == 0
                A[i][j] = num // prev
            A[i][k] = 0
        prev = pivot
    return sign * A[-1][-1]


def cofactor_tree_count(V, arcs, root):
    index = {v:i for i,v in enumerate(V)}
    L = [[0] * len(V) for _ in V]
    for a,b in arcs:
        L[index[a]][index[a]] += 1
        L[index[a]][index[b]] -= 1
    keep = [i for i,v in enumerate(V) if v != root]
    return bareiss_det([[L[i][j] for j in keep] for i in keep])


def compressed(n):
    V, E, out = graph(n)
    B = sorted(v for v in V if len(out[v]) == 2)
    assert B == sorted(v for v in V if v[0] != v[1] and v[-2] != v[-1])
    root = ''.join('01'[i % 2] for i in range(n-1))
    assert root in B
    corridors = []
    for b in B:
        for cur, w in out[b]:
            path = [w]
            while cur not in B:
                assert len(out[cur]) == 1 and len(path) <= n
                cur, w2 = out[cur][0]
                path.append(w2)
            corridors.append((b, cur, tuple(path)))
    assert len(corridors) == 2 * len(B)
    return B, root, corridors


def count_by_traversal(n):
    V, E, out = graph(n)
    index = {e:i for i,e in enumerate(E)}
    root = next(v for v in V if len(out[v]) == 2)
    first = out[root][0]
    target_mask = (1 << len(E)) - 1
    count = 0
    def explore(v,mask):
        nonlocal count
        if mask == target_mask:
            count += (v == root)
            return
        for next_v,e in out[v]:
            t = 1 << index[e]
            if not mask & t:
                explore(next_v,mask | t)
    explore(first[0],1 << index[first[1]])
    return count


def test(n, extra=False):
    V, E, out = graph(n)
    B, root, H = compressed(n)
    seen = {root}
    queue = deque([root]); adj=defaultdict(list)
    for u,v,_ in H: adj[u].append(v)
    while queue:
        v=queue.popleft()
        for w in adj[v]:
            if w not in seen: seen.add(w);queue.append(w)
    assert len(seen)==len(B)
    C = cofactor_tree_count(B,[(u,v) for u,v,_ in H],root)
    assert C > 0
    if extra:
        D = cofactor_tree_count(V,[(w[:-1],w[1:]) for w in E],root)
        assert C == D,(n,C,D)
    if n <= 7:
        T=count_by_traversal(n)
        assert C==T,(n,C,T)
    return n,len(E),len(V),len(B),C

if __name__ == '__main__':
    print('n  windows  vertices  branches  cycles')
    expected = {4:1,5:5,6:12,7:44,8:6720,9:1832544,10:48681971200}
    for n in range(4,12):
        result=test(n, extra=(n <= 9))
        if n in expected: assert result[-1]==expected[n]
        print(*result, flush=True)
    print('PASS: full/branch Laplacian and direct Euler circuits agree in checked ranges')

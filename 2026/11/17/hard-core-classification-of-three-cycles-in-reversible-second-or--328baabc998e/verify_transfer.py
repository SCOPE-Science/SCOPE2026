"""Independent 64-vertex temporal-column graph check for Rule 54."""


def wolfram54(a, b, c):
    return (54 >> (4 * a + 2 * b + c)) & 1


def allowed_triple(A, B, C):
    for t in range(3):
        previous = (B >> ((t + 2) % 3)) & 1
        next_value = (B >> ((t + 1) % 3)) & 1
        here = (B >> t) & 1
        left = (A >> t) & 1
        right = (C >> t) & 1
        if next_value != (previous ^ wolfram54(left, here, right)):
            return False
    return True


def graph():
    V = [(a, b) for a in range(8) for b in range(8)]
    adj = {v: [] for v in V}
    for A in range(8):
        for B in range(8):
            for C in range(8):
                if allowed_triple(A, B, C):
                    adj[(A,B)].append((B,C))
    return adj


def strongly_connected_components(adj):
    # Pure-standard-library Tarjan algorithm.
    index = 0
    stack = []
    active = set()
    stamp = {}
    low = {}
    components = []

    def visit(v):
        nonlocal index
        stamp[v] = low[v] = index
        index += 1
        stack.append(v)
        active.add(v)
        for w in adj[v]:
            if w not in stamp:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in active:
                low[v] = min(low[v], stamp[w])
        if low[v] == stamp[v]:
            comp = set()
            while True:
                w = stack.pop()
                active.remove(w)
                comp.add(w)
                if w == v:
                    break
            components.append(comp)
    for v in adj:
        if v not in stamp:
            visit(v)
    return components


def trace(adjacency, n):
    total = 0
    for start in adjacency:
        counts = {start: 1}
        for _ in range(n):
            nxt = {}
            for a, multiplicity in counts.items():
                for b in adjacency[a]:
                    nxt[b] = nxt.get(b, 0) + multiplicity
            counts = nxt
        total += counts.get(start, 0)
    return total


def lucas3(m):
    u, v = 2, 1
    if m == 0:
        return u
    for _ in range(1, m):
        u, v = v, v + 3 * u
    return v


if __name__ == '__main__':
    adj = graph()
    assert sum(len(v) for v in adj.values()) == 112
    comps = strongly_connected_components(adj)
    cyclic = [c for c in comps if len(c)>1 or any(v in adj[v] for v in c)]
    assert sorted(map(len, cyclic)) == [1, 16]
    singleton = next(c for c in cyclic if len(c) == 1)
    large = next(c for c in cyclic if len(c) == 16)
    assert singleton == {(0,0)}
    assert large == {(a,b) for a in (1,2,4,7) for b in (1,2,4,7)}
    for a,b in large:
        core_successors = {v for v in adj[(a,b)] if v in large}
        expected = {(b,c) for c in ((1,2,4,7) if a == 7 else (7,))}
        assert core_successors == expected
    for n in range(1, 25):
        answer = trace(adj,n)
        expected = 1 + (lucas3(n) if n%2 else lucas3(n//2)**2)
        assert answer == expected, (n,answer,expected)
        print(f'n={n}: graph_trace={answer}')
    print('TEMPORAL_GRAPH_PASS 64 vertices, 112 edges, cyclic SCC sizes 1 and 16')

from collections import deque
from itertools import product


def build_graph(a, b, c, d, xy):
    core = []
    for label, count in (("A", a), ("B", b), ("C", c), ("D", d)):
        core.extend((label, i) for i in range(count))
    x = ("x", 0)
    y = ("y", 0)
    vertices = core + [x, y]
    adj = {v: set() for v in vertices}

    def add(u, v):
        adj[u].add(v)
        adj[v].add(u)

    for i, u in enumerate(core):
        for v in core[i + 1:]:
            add(u, v)
    if xy:
        add(x, y)
    for u in core:
        if u[0] in ("A", "C"):
            add(x, u)
        if u[0] in ("B", "C"):
            add(y, u)
    return vertices, adj


def distances(vertices, adj):
    out = {}
    for s in vertices:
        out[s] = {s: 0}
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in out[s]:
                    out[s][v] = out[s][u] + 1
                    q.append(v)
        if len(out[s]) != len(vertices):
            return None
    return out


def direct_gap(a, b, c, d, xy):
    vertices, adj = build_graph(a, b, c, d, xy)
    dist = distances(vertices, adj)
    if dist is None:
        return None
    wiener = 0
    for i, u in enumerate(vertices):
        for v in vertices[i + 1:]:
            wiener += dist[u][v]
    szeged = 0
    for u in vertices:
        for v in adj[u]:
            if repr(u) >= repr(v):
                continue
            nu = sum(dist[z][u] < dist[z][v] for z in vertices)
            nv = sum(dist[z][v] < dist[z][u] for z in vertices)
            szeged += nu * nv
    return szeged - wiener


def formula_gap(a, b, c, d, xy):
    if xy:
        return 8*a*b + 2*a*c + 3*a*d + 2*b*c + 3*b*d + 4*c*d - 4*d
    if c:
        return (5*a*b + 2*a*c + 2*a*d - 2*a + 2*b*c + 2*b*d - 2*b
                + 4*c*d + 2*c - 4*d - 2)
    return 5*a*b + 2*a*d - a + 2*b*d - b - 4*d - 3


def is_two_connected_profile(a, b, c, xy):
    if xy:
        return a + c >= 1 and b + c >= 1 and a + b + c >= 2
    return a + c >= 2 and b + c >= 2


def classified_equality(a, b, c, d, xy):
    if not xy:
        return False
    if a == b == 1 and c == 0 and d >= 6:
        return True
    if c == 1 and d == 6 and sorted((a, b)) == [0, 1]:
        return True
    return False

# Directly verify the closed forms on a broad finite parameter box.
checked = 0
for a, b, c, d, xy in product(range(5), range(5), range(5), range(5), (0, 1)):
    if a + b + c + d == 0:
        continue
    if xy:
        connected = (a + c >= 1 and b + c >= 1)
    elif c:
        connected = (a + c >= 1 and b + c >= 1)
    else:
        connected = (a >= 1 and b >= 1)
    if not connected:
        continue
    direct = direct_gap(a, b, c, d, xy)
    if direct is None:
        continue
    claimed = formula_gap(a, b, c, d, xy)
    assert direct == claimed, (a, b, c, d, xy, direct, claimed)
    checked += 1
print(f"closed forms: {checked} connected parameter profiles checked")

# Exhaustively verify the equality classification through order 18.
profiles = 0
equalities = []
for n in range(10, 19):
    q = n - 2
    for a in range(q + 1):
        for b in range(q - a + 1):
            for c in range(q - a - b + 1):
                d = q - a - b - c
                for xy in (0, 1):
                    if not is_two_connected_profile(a, b, c, xy):
                        continue
                    direct = direct_gap(a, b, c, d, xy)
                    assert direct is not None
                    predicted = formula_gap(a, b, c, d, xy)
                    assert direct == predicted
                    eq = (direct == 2*n)
                    assert eq == classified_equality(a, b, c, d, xy), (
                        n, a, b, c, d, xy, direct
                    )
                    profiles += 1
                    if eq:
                        equalities.append((n, a, b, c, d, xy))
print(f"equality classification: {profiles} two-connected profiles checked for 10 <= n <= 18")
print("equality profiles (x,y symmetry not quotiented):")
for row in equalities:
    print(row)

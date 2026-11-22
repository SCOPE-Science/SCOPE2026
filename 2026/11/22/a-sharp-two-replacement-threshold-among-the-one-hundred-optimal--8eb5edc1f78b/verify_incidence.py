"""Independent direct exhaustive incidence check of semitotal domination and exchange.
Python 3 standard library only. Run: python3 verify_incidence.py
"""
from itertools import combinations, permutations
from collections import Counter, deque

U = tuple(range(5))
X = list(combinations(U, 2))
Y = list(combinations(U, 3))
objects = X + Y
idx = {v: i for i, v in enumerate(objects)}
n = len(objects)
assert n == 20
adj = [set() for _ in range(n)]
for a, x in enumerate(X):
    for b, y in enumerate(Y, start=10):
        if set(x) <= set(y):
            adj[a].add(b)
            adj[b].add(a)
assert all(len(s) == 3 for s in adj)

# Verify a fixed explicit graph isomorphism to GP(10,3); does not use its
# domination test or enumerator.
map_gp = [0, 10, 4, 16, 7, 19, 9, 15, 3, 12, 11, 1, 17, 5, 13, 8, 18, 2, 14, 6]
assert len(set(map_gp)) == 20
G = [set() for _ in range(20)]
for i in range(10):
    for v, w in ((i, (i + 1) % 10), (i, 10 + i), (10 + i, 10 + (i + 3) % 10)):
        G[v].add(w)
        G[w].add(v)
assert all({map_gp[w] for w in G[v]} == adj[map_gp[v]] for v in range(20))

dist = []
for source in range(n):
    d = [-1] * n
    d[source] = 0
    q = deque([source])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] == -1:
                d[w] = d[v] + 1
                q.append(w)
    assert -1 not in d
    dist.append(d)

# A smaller semitotal set would extend to a dominating five-set.
# Exhaustively check the latter, making the minimum bound independent of literature.
for c in combinations(range(n), 5):
    assert len(set(c) | set().union(*(adj[u] for u in c))) < 20

optimal, ordinary = [], 0
for c in combinations(range(n), 6):
    chosen = set(c)
    dominated = chosen | set().union(*(adj[u] for u in c))
    if len(dominated) != 20:
        continue
    ordinary += 1
    if all(any(v != u and dist[u][v] <= 2 for v in c) for u in c):
        optimal.append(frozenset(c))
assert ordinary == 130 and len(optimal) == 100
assert all(len(s & set(range(10))) == 3 for s in optimal)
assert sum(sum(v in adj[u] for u in s for v in s) // 2 == 1 for s in optimal) == 30

# Every one-token optimum exchange is forbidden; exactly 570 two-token ones.
graph = {s: [] for s in optimal}
for i, s in enumerate(optimal):
    for t in optimal[i + 1:]:
        d = 6 - len(s & t)
        assert d >= 2
        if d == 2:
            graph[s].append(t)
            graph[t].append(s)
assert sum(map(len, graph.values())) // 2 == 570
assert Counter(map(len, graph.values())) == Counter({8: 30, 12: 10, 13: 60})
profiles = Counter()
for s in optimal:
    distances = {s: 0}
    q = deque([s])
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in distances:
                distances[w] = distances[v] + 1
                q.append(w)
    assert len(distances) == 100 and max(distances.values()) == 4
    shell = Counter(distances.values())
    profiles[tuple(shell[i] for i in range(5))] += 1
assert profiles == Counter({(1, 13, 44, 40, 2): 60,
                            (1, 8, 46, 44, 1): 30,
                            (1, 12, 42, 42, 3): 10})

# Independently derive the three symmetry orbits from all 120 relabelings
# and the two-shore duality (complement of a 2- or 3-subset).
def act(s, p, dual):
    new = set()
    for i in s:
        val = tuple(sorted(p[j] for j in objects[i]))
        if dual:
            val = tuple(j for j in U if j not in val)
        new.add(idx[val])
    return frozenset(new)

unseen = set(optimal)
orbits = []
while unseen:
    rep = min(unseen, key=lambda a: sum(1 << i for i in a))
    orb = {act(rep, p, dual) for p in permutations(U) for dual in (False, True)}
    assert orb <= unseen
    orbits.append((rep, len(orb)))
    unseen -= orb
assert Counter(size for _, size in orbits) == Counter({10: 1, 30: 1, 60: 1})
induced_edges = Counter(sum(1 for u in rep for v in rep if v in adj[u]) // 2 for rep, _ in orbits)
assert induced_edges == Counter({0: 2, 1: 1})
print("Incidence H(5,2): ordinary_6=130 semitotal_6=100 one_jump_edges=0 "
      "two_jump_edges=570 diameter=4 orbits=10,30,60 ", end="")
print("VERIFY_OK")

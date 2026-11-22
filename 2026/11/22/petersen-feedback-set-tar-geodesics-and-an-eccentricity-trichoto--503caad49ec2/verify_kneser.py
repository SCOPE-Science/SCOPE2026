"""Exhaustive certificate for the Petersen feedback-deletion TAR theorem.

Vertices of Petersen are 2-element subsets of {0,...,4}, adjacent when disjoint.
Only standard Python 3 libraries are required.
"""
from itertools import combinations
from collections import Counter, deque

E = tuple(combinations(range(5), 2))
V = frozenset(range(10))
adj = tuple(frozenset(j for j, f in enumerate(E) if i != j and set(e).isdisjoint(f)) for i, e in enumerate(E))


def forest(S):
    """Union-find acyclicity on all edges of the *remaining* induced graph."""
    keep = V.difference(S)
    p = {v: v for v in keep}

    def root(x):
        while p[x] != x:
            x = p[x]
        return x

    for v in sorted(keep):
        for w in sorted(adj[v] & keep):
            if v < w:
                a, b = root(v), root(w)
                if a == b:
                    return False
                p[a] = b
    return True


def star3(S):
    return len(S) == 3 and len(set.intersection(*(set(E[x]) for x in S))) == 1


def square4(S):
    if len(S) != 4:
        return False
    deg = Counter(t for v in S for t in E[v])
    return sorted(deg.values()) == [2, 2, 2, 2]


valid = {k: [frozenset(c) for c in combinations(range(10), k) if forest(c)] for k in range(6)}
assert [len(valid[k]) for k in range(6)] == [0, 0, 0, 20, 140, 240]
assert all(star3(S) for S in valid[3])
assert all(any(star3(frozenset(U)) for U in combinations(S, 3)) or square4(S) for S in valid[4])
assert sum(square4(S) for S in valid[4]) == 15
assert all(any(star3(frozenset(U)) for U in combinations(S, 3)) for S in valid[5])


def graph(cap):
    states = [s for k in range(3, cap + 1) for s in valid[k]]
    lookup = {s: i for i, s in enumerate(states)}
    neighbors = [set() for _ in states]
    for i, s in enumerate(states):
        for v in V.difference(s):
            j = lookup.get(s | {v})
            if j is not None:
                neighbors[i].add(j)
                neighbors[j].add(i)
    return states, neighbors


def distances(neighbors, start):
    d = {start: 0}
    q = deque([start])
    while q:
        x = q.popleft()
        for y in neighbors[x]:
            if y not in d:
                d[y] = d[x] + 1
                q.append(y)
    return d

for cap, n, edges, sizes in [(3, 20, 0, Counter({1: 20})), (4, 160, 140, Counter({29: 5, 1: 15})), (5, 400, 980, Counter({400: 1}))]:
    states, nb = graph(cap)
    seen = set()
    comps = Counter()
    for i in range(len(states)):
        if i not in seen:
            component = distances(nb, i)
            seen.update(component)
            comps[len(component)] += 1
    assert (len(states), sum(map(len, nb)) // 2, comps) == (n, edges, sizes)
    print(f'cap={cap} states={n} edges={edges} component_sizes={dict(comps)}')

states, nb = graph(5)
minimum = [i for i, s in enumerate(states) if len(s) == 3]
opt_distance = Counter()
all_pair_dist = Counter()
ecc = Counter()
for i, s in enumerate(states):
    d = distances(nb, i)
    assert len(d) == 400
    ecc[(len(s), max(d.values()))] += 1
    for j in range(i + 1, 400):
        all_pair_dist[d[j]] += 1
for ix, i in enumerate(minimum):
    for j in minimum[ix + 1:]:
        assert distances(nb, i)[j] == len(states[i] ^ states[j])
        opt_distance[len(states[i] ^ states[j])] += 1
assert opt_distance == Counter({2: 30, 4: 90, 6: 70})
assert ecc == Counter({(3, 8): 20, (4, 9): 140, (5, 10): 240})
assert all_pair_dist[10] == 120
print('minimum_pair_distances=', dict(sorted(opt_distance.items())))
print('eccentricity_by_size=', dict(sorted(ecc.items())))
print('full_graph_diameter_pairs=', all_pair_dist[10])
print('PASS exhaustive Kneser realization, all states and full graph distances')

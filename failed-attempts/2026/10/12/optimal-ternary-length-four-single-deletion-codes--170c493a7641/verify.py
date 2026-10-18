#!/usr/bin/env python3
from itertools import product, combinations, permutations
from collections import Counter

Q = (0,1,2)
WORDS = tuple(product(Q, repeat=4))
INDEX = {w:i for i,w in enumerate(WORDS)}
N = len(WORDS)


def descendants_delete(w):
    return frozenset(w[:i] + w[i+1:] for i in range(4))


def descendants_survivors(w):
    return frozenset(tuple(w[j] for j in js) for js in combinations(range(4), 3))

D = []
for w in WORDS:
    a = descendants_delete(w)
    b = descendants_survivors(w)
    assert a == b
    D.append(a)

adj = [0]*N
edge_count = 0
for i in range(N):
    for j in range(i+1,N):
        if D[i].isdisjoint(D[j]):
            adj[i] |= 1 << j
            adj[j] |= 1 << i
            edge_count += 1
assert edge_count == 2370

# Exact maximal-clique enumeration using Bron-Kerbosch with pivoting.
maximal_hist = Counter()
maximal_maxima = []
node_visits = 0


def choose_pivot(P, X):
    U = P | X
    if not U:
        return -1
    best = -1
    best_score = -1
    u = U
    while u:
        lb = u & -u
        v = lb.bit_length()-1
        score = (P & adj[v]).bit_count()
        if score > best_score:
            best_score = score
            best = v
        u ^= lb
    return best


def bronk(R, P, X):
    global node_visits
    node_visits += 1
    if P == 0 and X == 0:
        s = len(R)
        maximal_hist[s] += 1
        if s == 11:
            maximal_maxima.append(tuple(R))
        return
    u = choose_pivot(P,X)
    cand = P if u < 0 else P & ~adj[u]
    while cand:
        lb = cand & -cand
        v = lb.bit_length()-1
        bronk(R+(v,), P & adj[v], X & adj[v])
        P ^= lb
        X |= lb
        cand ^= lb

bronk(tuple(), (1<<N)-1, 0)
assert max(maximal_hist) == 11
assert maximal_hist[11] == 6
assert len(maximal_maxima) == 6

# Independent exact k-clique counter, using only increasing vertices and no maximality logic.
# Counts all cliques of a specified size.
forward = [adj[i] & ~((1 << (i+1))-1) for i in range(N)]

def count_k(k):
    count = 0
    def rec(candidates, need):
        nonlocal count
        if need == 0:
            count += 1
            return
        if candidates.bit_count() < need:
            return
        while candidates:
            if candidates.bit_count() < need:
                return
            lb = candidates & -candidates
            v = lb.bit_length()-1
            candidates ^= lb
            rec(candidates & forward[v], need-1)
    rec((1<<N)-1, k)
    return count

k11 = count_k(11)
k12 = count_k(12)
assert k11 == 6
assert k12 == 0

maxima = [frozenset(WORDS[i] for i in M) for M in maximal_maxima]
maxima_set = set(maxima)
assert len(maxima_set) == 6
core = set.intersection(*(set(M) for M in maxima))
union = set.union(*(set(M) for M in maxima))
expected_core = {(a,a,b,b) for a in Q for b in Q}
expected_extras = {
    (0,1,2,0),(0,2,1,0),(1,0,2,1),
    (1,2,0,1),(2,0,1,2),(2,1,0,2)
}
assert core == expected_core
assert union == expected_core | expected_extras
assert len(core) == 9 and len(union) == 15

extra_edges = set()
for M in maxima:
    ex = tuple(sorted(set(M)-expected_core))
    assert len(ex) == 2
    extra_edges.add(ex)
assert len(extra_edges) == 6
extra_deg = Counter()
for a,b in extra_edges:
    extra_deg[a] += 1
    extra_deg[b] += 1
assert set(extra_deg) == expected_extras
assert set(extra_deg.values()) == {2}
# Connectedness proves this 2-regular six-vertex graph is a 6-cycle.
seen = set()
stack = [next(iter(expected_extras))]
while stack:
    x = stack.pop()
    if x in seen:
        continue
    seen.add(x)
    for a,b in extra_edges:
        if a == x and b not in seen: stack.append(b)
        if b == x and a not in seen: stack.append(a)
assert seen == expected_extras

# Natural action: symbol permutations and reversal.
def act_word(w, p, rev):
    z = tuple(p[x] for x in w)
    return z[::-1] if rev else z

group = [(p,rev) for p in permutations(Q) for rev in (False,True)]
assert len(group) == 12
M0 = next(iter(maxima_set))
orbit = set()
for p,rev in group:
    orbit.add(frozenset(act_word(w,p,rev) for w in M0))
assert orbit == maxima_set
stabilizer = sum(1 for p,rev in group if frozenset(act_word(w,p,rev) for w in M0) == M0)
assert stabilizer == 2

# All equality cases have the same deletion-shadow profile and are non-perfect.
profiles = set()
covered_counts = set()
for M in maxima:
    hist = Counter(len(D[INDEX[w]]) for w in M)
    profiles.add(tuple(sorted(hist.items())))
    covered = set().union(*(set(D[INDEX[w]]) for w in M))
    covered_counts.add(len(covered))
assert profiles == {((1,3),(2,6),(4,2))}
assert covered_counts == {23}

# Pairwise compatibility and structural family reconstruction are checked directly.
for M in maxima:
    for x,y in combinations(M,2):
        assert D[INDEX[x]].isdisjoint(D[INDEX[y]])
    assert expected_core <= set(M)
    assert tuple(sorted(set(M)-expected_core)) in extra_edges

print(
    "VERIFY_OK "
    f"vertices={N} edges={edge_count} maximal_cliques={sum(maximal_hist.values())} "
    f"maximum=11 labeled_maxima={len(maxima_set)} k11={k11} k12={k12} "
    f"core={len(core)} union={len(union)} extras={len(expected_extras)} extra_cycle=C6 "
    f"natural_group=12 orbits=1 orbit_size=6 stabilizer=2 "
    f"shadow_profile=1x3,2x6,4x2 covered_outputs=23/27"
)

"""Independent exact-bitset verifier of minimum McGee identifying-code mobility."""
from collections import Counter, deque
from itertools import combinations

N = 24
ADJ = [set() for _ in range(N)]
# Build each undirected chord once, separately from the cycle edges.
for u in range(N):
    v = (u + 1) % N
    ADJ[u].add(v)
    ADJ[v].add(u)
for u in range(N):
    delta = (12, 7, -7)[u % 3]
    v = (u + delta) % N
    ADJ[u].add(v)
    ADJ[v].add(u)
assert all(len(a) == 3 for a in ADJ)
assert sum(map(len, ADJ)) == 72

def girth():
    best = N + 1
    for root in range(N):
        distance = [-1] * N
        parent = [-1] * N
        distance[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in ADJ[u]:
                if distance[v] == -1:
                    distance[v] = distance[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v:
                    best = min(best, distance[u] + distance[v] + 1)
    return best
assert girth() == 7

closed = [sum(1 << v for v in a | {u}) for u, a in enumerate(ADJ)]
# A set identifies the graph iff it hits all 24 closed neighborhoods and
# all 276 pairwise symmetric differences of closed neighborhoods.
constraints = list(closed)
constraints += [closed[i] ^ closed[j] for i in range(N) for j in range(i)]
assert len(constraints) == 300 and all(constraints)

def masks(k):
    for points in combinations(range(N), k):
        mask = 0
        for v in points:
            mask |= 1 << v
        yield mask

def admissible(mask):
    return all(mask & requirement for requirement in constraints)

count_ten = sum(admissible(mask) for mask in masks(10))
codes = sorted(mask for mask in masks(11) if admissible(mask))
assert count_ten == 0 and len(codes) == 384
index = {mask: a for a, mask in enumerate(codes)}
J = [set() for _ in codes]
S = [set() for _ in codes]
for a, mask in enumerate(codes):
    on = [v for v in range(N) if (mask >> v) & 1]
    off = [v for v in range(N) if not (mask >> v) & 1]
    for u in on:
        for v in off:
            b = index.get(mask ^ (1 << u) ^ (1 << v))
            if b is not None:
                J[a].add(b)
                if v in ADJ[u]:
                    S[a].add(b)

def components(graph):
    unseen = set(range(len(graph)))
    output = []
    while unseen:
        start = min(unseen)
        seen = {start}
        queue = deque([start])
        unseen.remove(start)
        while queue:
            a = queue.popleft()
            for b in graph[a]:
                if b not in seen:
                    seen.add(b)
                    unseen.remove(b)
                    queue.append(b)
        output.append(seen)
    return output

def statistics(graph):
    CC = components(graph)
    counts = Counter((len(c), sum(len(graph[v]) for v in c) // 2) for c in CC)
    degrees = Counter(map(len, graph))
    return len(CC), sum(map(len, graph)) // 2, counts, degrees, CC

jn, je, jt, jd, jcomponents = statistics(J)
sn, se, st, sd, scomponents = statistics(S)
assert (jn, je) == (208, 272)
assert jt == Counter({(1, 0): 176, (2, 1): 16, (11, 16): 16})
assert jd == Counter({0: 176, 1: 96, 3: 32, 4: 64, 6: 16})
assert (sn, se) == (352, 32)
assert st == Counter({(1, 0): 320, (2, 1): 32})
assert sd == Counter({0: 320, 1: 64})

# Verify the exact 11-vertex component topology without relying on graph-isomorphism libraries.
def is_two_tetrahedra_with_leaves(component):
    core = {v for v in component if len(J[v]) > 1}
    leaves = component - core
    if len(core) != 7 or len(leaves) != 4:
        return False
    cliques = [set(p) for p in combinations(sorted(core), 4)
               if all(b in J[a] for a, b in combinations(p, 2))]
    if len(cliques) != 2 or len(cliques[0] & cliques[1]) != 1 or cliques[0] | cliques[1] != core:
        return False
    center = next(iter(cliques[0] & cliques[1]))
    attachments = [next(iter(J[v])) for v in leaves if len(J[v]) == 1]
    if len(attachments) != 4 or len(set(attachments)) != 4 or center in attachments:
        return False
    if any(len(set(attachments) & c) != 2 for c in cliques):
        return False
    # Count all edges: the two complete graphs and four pendant edges.
    return sum(len(J[v]) for v in component) // 2 == 16

assert all(is_two_tetrahedra_with_leaves(c) for c in jcomponents if len(c) == 11)
assert Counter((len(c), sum(len(S[v]) for v in c) // 2) for c in jcomponents) == Counter({(1,0):176,(2,0):16,(11,2):16})
print('VERIFY_OK minimum=11 codes=384 jump=208-components/272-edges slide=352-components/32-edges H11=two_K4_vertex_join_with_four_leaves')

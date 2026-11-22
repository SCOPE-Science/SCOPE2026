"""Independent finite certificate from the Hamiltonian LCF presentation.
Uses a vertex-coclique / perfect-matching search rather than maximal-matching recursion.
Requires only Python 3 standard library.
"""
from collections import Counter, deque
from itertools import combinations

n = 18
offsets = [5, 7, -7, 7, -7, -5] * 3
E = sorted({tuple(sorted((i, (i+1) % n))) for i in range(n)} |
           {tuple(sorted((i, (i+offsets[i]) % n))) for i in range(n)})
assert len(E) == 27
# Explicit graph-model isomorphism to the affine incidence convention;
# this does not enter the independent matching enumeration below.
phi = (0, 9, 2, 17, 3, 12, 6, 16, 1, 13, 7, 11, 8, 14, 5, 10, 4, 15)
affine_points = [(x,y) for x in range(3) for y in range(3)]
affine_edges = {tuple(sorted((i, 9+3*d+c)))
                for i,(x,y) in enumerate(affine_points)
                for d in range(3) for c in range(3)
                if (x if d==0 else y if d==1 else (y-x)%3)==c}
assert len(set(phi)) == 18 and set(phi) == set(range(18))
assert {tuple(sorted((phi[u],phi[v]))) for u,v in E} == affine_edges
adj = [set() for _ in range(n)]
for u, v in E:
    adj[u].add(v); adj[v].add(u)
assert all(len(x) == 3 for x in adj)
part = {0: 0}; queue = deque([0])
while queue:
    u = queue.popleft()
    for v in adj[u]:
        if v in part: assert part[v] != part[u]
        else: part[v] = 1-part[u]; queue.append(v)
assert len(part) == n
left = [v for v in range(n) if part[v] == 0]
right = [v for v in range(n) if part[v] == 1]
assert len(left) == len(right) == 9
edgeid = {e: j for j, e in enumerate(E)}

def perfect_completions(uncovered):
    remaining_left = [u for u in left if u not in uncovered]
    remaining_right = frozenset(v for v in right if v not in uncovered)
    answers = []
    def solve(i, right_free, chosen):
        if i == len(remaining_left):
            assert not right_free
            answers.append(chosen)
            return
        u = remaining_left[i]
        for v in sorted(adj[u] & right_free):
            key = tuple(sorted((u,v)))
            solve(i+1, right_free-{v}, chosen | (1 << edgeid[key]))
    solve(0,remaining_right,0)
    return answers

# A maximal k-matching leaves (9-k) uncovered vertices on EACH shore;
# these vertices must form a coclique, and the complementary induced graph
# must have a perfect matching. Exhaustive for k <= 6.
for missing in (4,):
    feasible = 0
    for X in combinations(left, missing):
        forbidden = set().union(*(adj[x] for x in X))
        for Y in combinations(right, missing):
            if not forbidden.intersection(Y):
                feasible += 1
    assert feasible == 0, feasible

optimal = []
admissible_cocliques = 0
for X in combinations(left, 3):
    forbidden = set().union(*(adj[x] for x in X))
    for Y in combinations(right, 3):
        if forbidden.intersection(Y): continue
        admissible_cocliques += 1
        optimal.extend(perfect_completions(set(X)|set(Y)))
assert admissible_cocliques == 18
assert len(optimal) == len(set(optimal)) == 36
assert all(m.bit_count() == 6 for m in optimal)

T = sorted(optimal)
G = [set() for _ in T]
for i, a in enumerate(T):
    for j in range(i):
        swaps = (a ^ T[j]).bit_count()//2
        assert swaps >= 3
        if swaps == 3: G[i].add(j); G[j].add(i)
assert sum(map(len,G))//2 == 126
assert all(len(x) == 7 for x in G)
for i in range(len(T)):
    dist = {i:0}; q = deque([i])
    while q:
        u = q.popleft()
        for v in G[u]:
            if v not in dist:
                dist[v] = dist[u]+1; q.append(v)
    assert len(dist) == 36
    assert tuple(Counter(dist.values())[r] for r in range(5)) == (1,7,12,12,4)
print('PAPPUS LCF CERTIFICATE PASS')
print('n=18, edges=27, shores=9+9; no four-four cocliques')
print('18 admissible three-three cocliques, 36 distinct minimum maximal matchings')
print('all pairs require at least 3-edge replacements; three-edge exchange connected')
print('126 exchange edges; degree=7; uniform distance shells 1,7,12,12,4')

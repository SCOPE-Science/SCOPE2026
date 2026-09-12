"""Finite-truncation partial-automorphism test (bounded recovery probe).

Truncates T_{3,inf}: inf-vertices given k neighbours (k=4), 3-vertices degree 3,
explored to depth 3 from a root. Enumerates small partial automorphisms and
tests joint embedding (amalgamation) of pairs. Finite-k results do not lift to
k=infinity; used only as a bounded search for obstructions.
"""
from itertools import permutations

K = 4
DEPTH = 3

# Build truncated biregular tree as adjacency via BFS with degree caps.
adj = {}
def add_edge(a, b):
    adj.setdefault(a, []).append(b)
    adj.setdefault(b, []).append(a)

def deg_cap(v):
    return 3 if v[0] == 'a' else K

nodes = [('a', 0)]
adj[('a', 0)] = []
frontier = [(('a', 0), 0)]
uid = 0
from collections import deque
q = deque([(('a', 0), 0)])
seen = {('a', 0)}
while q:
    v, d = q.popleft()
    if d == DEPTH:
        continue
    side = 'b' if v[0] == 'a' else 'a'
    while len(adj[v]) < deg_cap(v):
        uid += 1
        w = (side, uid)
        seen.add(w)
        add_edge(v, w)
        q.append((w, d + 1))

verts = list(seen)
print(f"truncated tree: n={len(verts)} K={K} depth={DEPTH}")

# Partial automorphisms: sample transpositions of sibling leaves sharing a parent.
leaves = [v for v in verts if len(adj[v]) == 1 and v != ('a', 0)]
from collections import defaultdict
by_parent = defaultdict(list)
for v in leaves:
    by_parent[adj[v][0]].append(v)

partials = []
for p, kids in by_parent.items():
    if len(kids) >= 2:
        a, b = kids[0], kids[1]
        partials.append({a: b, b: a})

print(f"sample partial automorphisms: {len(partials)} sibling swaps")

# Joint embedding test: two disjoint-domain swaps always amalgamate (union is
# still a partial automorphism since domains are disjoint siblings). Count them.
jep_ok = 0
jep_total = 0
for i in range(len(partials)):
    for j in range(i + 1, len(partials)):
        d1, d2 = set(partials[i]), set(partials[j])
        jep_total += 1
        if not (d1 & d2):
            jep_ok += 1
print(f"disjoint-pair amalgamation: {jep_ok}/{jep_total} trivially amalgamate")
print("CONCLUSION: finite-k probe amalgamates; WAP/turbulence at k=inf undecided.")

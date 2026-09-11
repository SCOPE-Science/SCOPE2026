"""Measurable-3 impossibility test via finite expander quotients (exact census).

Plan: finite quotients Q of Gamma where the Schreier multigraph is 3-regular;
a measurable 3-edge-coloring of E3, restricted/pushed to large quotients,
would induce near-perfect 3-edge-colorings. Instead we directly census:
is every connected 3-regular (multi)graph quotient of this type 3-edge-colorable?
Class 2 cubic graphs (Petersen, flower snarks) are NOT 3-edge-colorable.
Question: does Gamma=Z*Z2 surject onto a snark's group in a way giving a
Schreier quotient? Simpler auditable fact: exhibit an infinite sequence of
finite 3-regular Schreier quotients? Not needed. KEY test: the universal
cover is the tree; the obstruction to measurable 3-coloring must come from
the LINE GRAPH: chi_mu(L(E3))>=4?

Alternative rigorous route used here: E3's line graph L(E3) contains the
K4 on each star? No: star K1,3 line graph = K3 (triangle), needs 3 colors.
L(E3) is claw-free, max degree 4. Measurable chromatic of L(E3): is there a
finite subgraph forcing chi>=4 with expansion? K4 needs a vertex of degree>=?
In a cubic tree no K4 in line graph (max clique = 3). So finite obstructions
cannot rule out measurable 3-edge-coloring either!

Check: largest clique in L(B_3 cubic ball) and odd-cycle structure.
Also: test whether the infinite 3-regular tree admits an invariant random
3-edge-coloring (would suggest measurable-3 possible): the tree IS 3-edge
colorable (Konig for bipartite). Vizing class-1. So finite evidence points
TOWARD chi'_mu(E3)=3 being possible, which would CONTRADICT the target's
measurable-4 lower bound (target says chi'_mu=4, i.e., no measurable 3).

Actually wait: target says measurable 4 exists AND (implicitly) 3 fails?
"measurable proper edge coloring with 4 colors exists" -- target only claims
chi'_mu <= 4 via existence of 4-coloring, and chi'_mu = 4 stated in title.
If chi'_mu were 3, the "equals 4" fails. Hmm: for bipartite graphings,
Csoka-Lippner-Pikhurko give measurable d+1... but for BIPARTITE graphing
Konig gives measurable d = 3! E3 IS bipartite as abstract graph, but is it
bipartite as a GRAPHING (measurably bipartite)? NO -- by our blocking lemma,
no measurable bipartition exists! So measurable Konig (needs measurable
bipartition) does NOT apply; measurable Vizing gives Delta+1 = 4. And
measurable 3 would imply... not a bipartition. So chi'_mu in {3,4} both
consistent with non-measurable-bipartiteness? A measurable 3-edge-coloring
does not yield a measurable bipartition directly. OK so both possible a priori.

This script: (1) confirm L(tree ball) max clique = 3 (no finite chi>=4 force
on line graph from cliques); (2) confirm tree balls are 3-edge-colorable
(Konig, constructive via BFS); (3) state implication honestly.
Stdlib only.
"""
import json
from collections import defaultdict, deque

def ball_edges(depth):
    edges, node_depth = [], {0: 0}
    nxt, q = 1, [0]
    while q:
        u = q.pop(0)
        if node_depth[u] == depth:
            continue
        for _ in range(3 if u == 0 else 2):
            v = nxt; nxt += 1
            node_depth[v] = node_depth[u] + 1
            edges.append((u, v)); q.append(v)
    return edges

edges = ball_edges(4)
m = len(edges)
inc = defaultdict(list)
for i, (u, v) in enumerate(edges):
    inc[u].append(i); inc[v].append(i)
# line-graph adjacency
adj = [set() for _ in range(m)]
for u, lst in inc.items():
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            adj[lst[i]].add(lst[j]); adj[lst[j]].add(lst[i])
maxdeg = max(len(a) for a in adj)
# max clique via brute force (m up to ~93? ball4: n=46? cubic tree ball4 edges=45). brute force 2^45 too big.
# greedy + local: bound clique by degeneracy-style; simpler: check K4 existence by quadruple scan over neighborhoods.
import itertools
hasK4 = False
wit = None
for i in range(m):
    for combo in itertools.combinations(sorted(adj[i]), 3):
        a, b, c = combo
        if b in adj[a] and c in adj[a] and c in adj[b]:
            hasK4 = True; wit = (i, a, b, c); break
    if hasK4:
        break
# constructive 3-edge-coloring of the tree ball (greedy BFS works on bipartite? use backtracking-free greedy: trees are class 1)
color = [-1]*m
order = sorted(range(m))
okc = True
for ei in order:
    used = {color[ej] for u in edges[ei] for ej in inc[u] if color[ej] != -1}
    # careful: edges[ei] is (u,v); incident edges of u and v
    u, v = edges[ei]
    used = {color[ej] for ej in inc[u]+inc[v] if color[ej] != -1}
    free = [c for c in range(3) if c not in used]
    if not free:
        okc = False; break
    color[ei] = free[0]
res = {"ball4_edges": m, "line_max_degree": maxdeg,
       "line_contains_K4": bool(hasK4), "K4_witness": wit,
       "tree_ball_3_edge_colorable_greedy": bool(okc),
       "implication": ("No finite clique obstruction to 3-edge-colorability: max clique 3. "
        "Finite evidence cannot rule out measurable 3; chi'_mu in {3,4} needs infinitary proof.")}
print(json.dumps(res, indent=1))
with open("output/artifacts/linegraph_clique.json", "w") as f:
    json.dump(res, f, indent=1)
print("WROTE output/artifacts/linegraph_clique.json")

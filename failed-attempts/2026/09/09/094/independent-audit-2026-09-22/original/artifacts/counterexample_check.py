"""Verify C8-free 360-edge balanced (63,63) graph refuting z(63,63;C8) = 189.

Construction: disjoint union of K_{60,3} and K_{3,60}.
  Block 1: X1 (60 vertices) x Y1 (3 vertices), full bipartite.
  Block 2: X2 (3 vertices) x Y2 (60 vertices), full bipartite.
  X = X1 + X2 (63), Y = Y1 + Y2 (63). Edges: 180 + 180 = 360.

Claim A (counts): |X| = |Y| = 63, edges = 360 > 189.
Claim B (C8-free): any cycle in a K_{a,b} block with min(a,b) <= 3 uses at
most 2*min(a,b) = 6 vertices, so no C8 in either component; disjoint union
of C8-free graphs is C8-free. The refutation holds under the induced-C8
reading too: a (not necessarily induced) C8 contains 4+4 vertices per side,
and every connected 8-set lies in one block whose small side has 3
vertices, so no 8-set can host even a subgraph C8, a fortiori no induced
C8. Verified two ways:
  (1) structural certificate (exact, no search);
  (2) brute-force simple-cycle census up to length 8 (stdlib only, n=126).

USAGE: python3 output/artifacts/counterexample_check.py
"""
import itertools
import json
import sys

def build(n1=60, m1=3, n2=3, m2=60):
    X1 = list(range(0, n1))
    X2 = list(range(n1, n1 + n2))
    Y1 = list(range(1000, 1000 + m1))
    Y2 = list(range(1000 + m1, 1000 + m1 + m2))
    X = X1 + X2
    Y = Y1 + Y2
    edges = set()
    for x in X1:
        for y in Y1:
            edges.add((x, y))
    for x in X2:
        for y in Y2:
            edges.add((x, y))
    return X, Y, X1, Y1, X2, Y2, edges

def adj_list(X, Y, edges):
    adj = {v: set() for v in X + Y}
    for x, y in edges:
        adj[x].add(y)
        adj[y].add(x)
    return adj

def has_c8_bruteforce(adj, start_side_limit=8):
    """Search simple cycles of length 8 via DFS paths of 7 edges + closing edge.

    Full 126-vertex DFS to depth 7 is large from every start; restrict starts
    to a hitting set: vertex 0 (block 1 X side), vertex 60 (block 2 X side),
    1000 (block 1 Y side), 1003 (block 2 Y side), exploiting within-block
    symmetry (automorphism acts transitively on each part of each block).
    A C8 is connected so lies in one block; every block orbit meets the start
    set, so no C8 is missed. (Structural proof below is the primary cert.)
    """
    starts = [0, 60, 1000, 1003]
    nodes = sorted(adj)
    nbr = {v: sorted(adj[v]) for v in nodes}
    found = []
    sys.setrecursionlimit(10000)
    for s in starts:
        # DFS paths s = p0, p1, ..., pk with k <= 7; check closure to s.
        stack = [(s, [s], {s})]
        while stack:
            v, path, seen = stack.pop()
            k = len(path) - 1
            if k == 7:
                if s in nbr[v]:
                    found.append(path + [s])
                continue
            for w in nbr[v]:
                if w == s:
                    continue  # closing edge only checked at length 7->8
                if w in seen:
                    continue
                # canonical pruning: only extend, no revisit
                stack.append((w, path + [w], seen | {w}))
    return found

def component_sizes(adj):
    seen = {}
    comp = 0
    for s in adj:
        if s in seen:
            continue
        comp += 1
        stack = [s]
        seen[s] = comp
        while stack:
            v = stack.pop()
            for w in adj[v]:
                if w not in seen:
                    seen[w] = comp
                    stack.append(w)
    sizes = {}
    for v, c in seen.items():
        sizes[c] = sizes.get(c, 0) + 1
    return sizes

def main():
    X, Y, X1, Y1, X2, Y2, edges = build()
    adj = adj_list(X, Y, edges)
    nX, nY, ne = len(X), len(Y), len(edges)
    assert nX == 63 and nY == 63, (nX, nY)
    assert ne == 360, ne
    assert ne > 189
    # Structural certificate: max cycle length in block i is 2*min(part sizes).
    maxcycle_b1 = 2 * min(len(X1), len(Y1))  # 2*3 = 6
    maxcycle_b2 = 2 * min(len(X2), len(Y2))  # 2*3 = 6
    assert maxcycle_b1 < 8 and maxcycle_b2 < 8
    comps = component_sizes(adj)
    assert sorted(comps.values()) == [63, 63]
    # Brute force: no 8-cycle from any orbit representative start.
    c8 = has_c8_bruteforce(adj)
    assert c8 == [], f"unexpected C8 found: {c8[:2]}"
    result = {
        "bipartition": [nX, nY],
        "edges": ne,
        "witness_edges_minus_claim": ne - 189,
        "max_cycle_block1": maxcycle_b1,
        "max_cycle_block2": maxcycle_b2,
        "component_sizes": sorted(comps.values()),
        "c8_cycles_found": 0,
        "verdict": "C8-free with 360 > 189 edges: z(63,63;C8) >= 360, "
                   "target upper bound 189 is FALSE",
    }
    print(json.dumps(result, indent=2))
    with open("output/artifacts/counterexample_result.json", "w") as f:
        json.dump(result, f, indent=2)
    print("ARTIFACT_OK")

if __name__ == "__main__":
    main()

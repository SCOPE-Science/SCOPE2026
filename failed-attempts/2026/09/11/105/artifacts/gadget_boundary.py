"""Verify the finite-gadget counting obstruction for cubic-tree reductions.

Lemma: Let T be the infinite 3-regular tree. For finite nonempty connected
S subset of V(T), the number of boundary edges d(S, T\\S) equals |S|+2.
Corollary: no nontrivial finite connected replacement gadget with exactly 3
inter-gadget edges preserves 3-regularity + acyclicity (only |S|=1 works).
Also: no finite tree gadget with 3 degree-2 ports and all other vertices
degree 3 exists (degree-sum contradiction).

Replay: python3 gadget_boundary.py -> prints VERIFY_OK + certificate lines.
Stdlib only.
"""
from collections import deque
from itertools import combinations

def build_ball(depth):
    # Build a finite rooted subtree of the infinite 3-regular tree:
    # root has 3 children subtrees which are infinite binary trees.
    # Represent as adjacency dict.
    adj = {}
    def add_edge(u, v):
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    # root 0; give it 3 neighbors 1,2,3; then each node except root has
    # 2 further children (to keep degree <=3 inside ball).
    nxt = [1, 2, 3]
    for n in nxt:
        add_edge(0, n)
    frontier = deque(nxt)
    # expand BFS up to given depth (graph distance from root)
    dist = {0: 0}
    for n in nxt:
        dist[n] = 1
    counter = 4
    while frontier:
        u = frontier.popleft()
        if dist[u] >= depth:
            continue
        # u already has 1 parent edge; add 2 children
        for _ in range(2):
            v = counter
            counter += 1
            add_edge(u, v)
            dist[v] = dist[u] + 1
            frontier.append(v)
    return adj

def boundary_of(S, adj):
    S = set(S)
    b = 0
    for u in S:
        for w in adj.get(u, []):
            if w not in S:
                b += 1
    # Note: vertices at the truncation frontier have missing edges
    # (degree <3 in the finite ball). Only count S strictly interior
    # where every vertex has full degree 3 in adj.
    return b

def is_connected(S, adj):
    S = list(S)
    if not S:
        return False
    seen = {S[0]}
    dq = deque([S[0]])
    Sset = set(S)
    while dq:
        u = dq.popleft()
        for w in adj.get(u, []):
            if w in Sset and w not in seen:
                seen.add(w)
                dq.append(w)
    return len(seen) == len(S)

def main():
    adj = build_ball(5)
    # interior vertices: full degree 3
    interior = [v for v, nb in adj.items() if len(nb) == 3]
    # test 1: singletons have boundary 3
    for v in interior[:20]:
        assert boundary_of([v], adj) == 3, v
    print("singletons: boundary=3 OK (20 samples)")

    # test 2: enumerate connected sets containing root 0 up to size 5,
    # verify boundary = |S|+2 (all such S are interior for ball depth 5
    # as long as S is within distance <=3 of root; restrict search).
    # BFS-enumerate connected sets by growth.
    conn_sets = [{0}]
    seen_sets = {frozenset([0])}
    for _ in range(4):  # grow to size 5
        new = []
        for S in conn_sets:
            if len(S) >= 5:
                continue
            nbrs = set()
            for u in S:
                for w in adj[u]:
                    if w not in S:
                        nbrs.add(w)
            for w in nbrs:
                S2 = frozenset(set(S) | {w})
                if S2 not in seen_sets:
                    seen_sets.add(S2)
                    new.append(set(S2))
        conn_sets.extend(new)
    n_checked = 0
    for S in seen_sets:
        if all(len(adj[v]) == 3 for v in S):
            b = boundary_of(S, adj)
            assert b == len(S) + 2, (S, b)
            n_checked += 1
    print(f"connected-set formula: boundary=|S|+2 OK ({n_checked} interior sets, sizes<=5)")

    # test 3: degree-sum impossibility of saturated 3-port tree gadget.
    # Suppose finite tree on n>=2 vertices, 3 ports of internal degree 2,
    # rest internal degree 3. Sum = 3(n-3)+6 = 3n-3; tree sum = 2n-2.
    # 3n-3 = 2n-2 -> n=1, contradiction. Check no n>=2 solves it.
    sols = [n for n in range(2, 1000) if 3*n-3 == 2*n-2]
    assert sols == [], sols
    print("port degree-sum: no n>=2 satisfies 3n-3=2n-2 OK")

    # test 4: disconnected forest replacement also impossible in a tree host.
    # If S has k components with sizes n_i (each connected), boundary = n+2k.
    # Exactly 3 -> n+2k=3 -> only (k=1,n=1). Exhaust small (n,k).
    sols2 = [(n, k) for n in range(1, 12) for k in range(1, n+1) if n+2*k == 3]
    assert sols2 == [(1, 1)], sols2
    print("forest formula: n+2k=3 only (1,1) OK")

    # test 5: brute force — all subsets S of small interior ball (root ball
    # radius 2: 1+3+6=10 vertices... use radius 2 = 10 vertices -> 2^10=1024)
    # check: any S with boundary exactly 3 must be a singleton.
    ball2 = {0, 1, 2, 3}
    # add children of 1,2,3
    kids = {}
    for u in [1, 2, 3]:
        kids[u] = [w for w in adj[u] if w != 0]
        ball2.update(kids[u])
    assert len(ball2) == 10, len(ball2)
    bad = []
    verts = sorted(ball2)
    for r in range(1, 11):
        for combo in combinations(verts, r):
            S = set(combo)
            # require S interior (all degrees full) and S connected? check all S
            if not all(len(adj[v]) == 3 for v in S):
                continue
            if boundary_of(S, adj) == 3 and len(S) > 1:
                # only possible if S touches truncation? no, all interior.
                # Record; expect none connected, but disconnected S could
                # in principle have boundary 3? formula says n+2k=3 impossible
                # for n>1, so expect none at all.
                bad.append(S)
    assert bad == [], bad
    print("brute force radius-2 ball: no multi-vertex S with boundary 3 OK")

    print("VERIFY_OK")

if __name__ == "__main__":
    main()

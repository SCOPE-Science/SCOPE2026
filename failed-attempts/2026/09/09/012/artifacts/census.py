#!/usr/bin/env python3
"""Exhaustive connected cubic graph census for even n in {4,6,8} (+ attempt 10).

Method (complete by construction):
  * Fix vertex 0 with neighbours {1,2,3} WLOG (any cubic graph relabels to this).
  * Recursive backtracking: always complete the lowest-index vertex with remaining
    degree deficit, trying every eligible partner. Every labeled completion is
    visited exactly once.
  * Keep completions that are connected (BFS); dedup into isomorphism classes via
    cheap invariant buckets + exact VF2-lite backtracking isomorphism test.
  * Assert class counts against OEIS A002851 (1,2,5 for n=4,6,8; 19 for n=10).

Output: graphs.json artifact {n: [edge lists]} plus counts printed to stdout.
Pure stdlib. No networkx/nauty needed.
"""
import json, sys, time

sys.setrecursionlimit(100000)

def popcount(x):
    return x.bit_count()

# ---------------- exact backtracking iso test (VF2-lite) ----------------
def are_iso(g, h, n):
    """g,h: lists of n int adjacency bitmasks. Exact isomorphism decision."""
    map_g2h = [-1] * n
    mapped_h_mask = 0
    # order: handled dynamically inside recursion
    def rec(done):
        nonlocal mapped_h_mask
        if done == n:
            return True
        # pick unmapped u with most mapped neighbours (deterministic tie-break)
        best_u, best_c = -1, -1
        for u in range(n):
            if map_g2h[u] < 0:
                c = 0
                gu = g[u]
                m = 0
                for w in range(n):
                    if map_g2h[w] >= 0 and (gu >> w) & 1:
                        c += 1
                if c > best_c:
                    best_c, best_u = c, u
        u = best_u
        gu = g[u]
        for v in range(n):
            if (mapped_h_mask >> v) & 1:
                continue
            hv = h[v]
            ok = True
            for w in range(n):
                mw = map_g2h[w]
                if mw >= 0:
                    au = (gu >> w) & 1
                    av = (hv >> mw) & 1
                    if au != av:
                        ok = False
                        break
            if ok:
                map_g2h[u] = v
                mapped_h_mask |= (1 << v)
                if rec(done + 1):
                    return True
                map_g2h[u] = -1
                mapped_h_mask &= ~(1 << v)
        return False
    return rec(0)

# ---------------- invariants ----------------
def invariant_key(adj, n):
    """Cheap integer invariant bucket: (tri_total, sorted tri-vector, sq_total, bip)."""
    tri = [0] * n
    for v in range(n):
        m = adj[v]
        # pairs of neighbours
        nbs = [u for u in range(n) if (m >> u) & 1]
        c = 0
        for i in range(len(nbs)):
            for j in range(i + 1, len(nbs)):
                if (adj[nbs[i]] >> nbs[j]) & 1:
                    c += 1
        tri[v] = c
    tri_total = sum(tri) // 3
    # squares: sum over unordered pairs of common neighbours C(cnt,2), /2 per square... each
    # 4-cycle has 2 opposite pairs, so sq_total = sum_{u<v} C(cn,2) / 2
    s = 0
    for u in range(n):
        for v in range(u + 1, n):
            cn = popcount(adj[u] & adj[v])
            s += cn * (cn - 1) // 2
    sq_total = s // 2
    # bipartite via BFS
    col = [-1] * n
    col[0] = 0
    stack = [0]
    bip = True
    while stack:
        u = stack.pop()
        for w in range(n):
            if (adj[u] >> w) & 1:
                if col[w] < 0:
                    col[w] = col[u] ^ 1
                    stack.append(w)
                elif col[w] == col[u]:
                    bip = False
                    stack = []
                    break
    return (tri_total, tuple(sorted(tri)), sq_total, bip)

def connected(adj, n):
    seen = 1  # bitmask
    stack = [0]
    while stack:
        u = stack.pop()
        m = adj[u]
        w = 0
        while m:
            if m & 1:
                if not (seen >> w) & 1:
                    seen |= (1 << w)
                    stack.append(w)
            w += 1
            m >>= 1
    return seen == (1 << n) - 1

# ---------------- generator ----------------
def gen_connected_cubic(n, time_cap=600):
    assert n % 2 == 0
    t0 = time.time()
    adj = [0] * n
    rem = [3] * n
    # fix N(0) = {1,2,3}
    for w in (1, 2, 3):
        adj[0] |= (1 << w)
        adj[w] |= (1 << 0)
        rem[0] -= 1
        rem[w] -= 1
    reps = []       # adjacency lists
    rep_keys = []
    stats = {"leaf": 0, "conn": 0, "iso_tests": 0}
    timed_out = {"v": False}

    # candidate partners tried in increasing order
    def rec():
        if time.time() - t0 > time_cap:
            timed_out["v"] = True
            return
        # find first vertex with deficit
        u = -1
        for i in range(n):
            if rem[i] > 0:
                u = i
                break
        if u < 0:
            stats["leaf"] += 1
            if connected(adj, n):
                stats["conn"] += 1
                key = invariant_key(adj, n)
                new = True
                for k, r in enumerate(reps):
                    if rep_keys[k] == key:
                        stats["iso_tests"] += 1
                        if are_iso(adj, r, n):
                            new = False
                            break
                if new:
                    reps.append(list(adj))
                    rep_keys.append(key)
            return
        for v in range(u + 1, n):
            if rem[v] > 0 and not (adj[u] >> v) & 1:
                adj[u] |= (1 << v)
                adj[v] |= (1 << u)
                rem[u] -= 1
                rem[v] -= 1
                rec()
                rem[u] += 1
                rem[v] += 1
                adj[u] &= ~(1 << v)
                adj[v] &= ~(1 << u)
                if timed_out["v"]:
                    return

    rec()
    elapsed = time.time() - t0
    return reps, stats, elapsed, timed_out["v"]

def edges_of(adj, n):
    e = []
    for u in range(n):
        for v in range(u + 1, n):
            if (adj[u] >> v) & 1:
                e.append([u, v])
    return e

def main():
    orders = [int(a) for a in sys.argv[1:]] or [4, 6, 8]
    out = {}
    for n in orders:
        reps, stats, el, to = gen_connected_cubic(n)
        out[str(n)] = [edges_of(r, n) for r in reps]
        print(f"n={n}: classes={len(reps)} leaf={stats['leaf']} conn={stats['conn']} "
              f"iso_tests={stats['iso_tests']} time={el:.1f}s timeout={to}", flush=True)
    expected = {"4": 1, "6": 2, "8": 5, "10": 19}
    for n in orders:
        assert len(out[str(n)]) == expected[str(n)], \
            f"n={n}: got {len(out[str(n)])}, expected {expected[str(n)]} (A002851)"
    print("COUNTS_OK vs OEIS A002851 (1,2,5[,19])", flush=True)
    with open("graphs.json", "w") as f:
        json.dump(out, f)
    print("wrote graphs.json", flush=True)

if __name__ == "__main__":
    main()

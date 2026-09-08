"""Graph kit: labeled connected-cubic generation, girth, alpha, bridges, canonical hash.
Pure stdlib.
"""
import itertools
import sys
from collections import defaultdict

# ---------------- labeled generation: N(0) = {1,2,3} fixed ----------------
def gen_labeled_cubic(n):
    """Yield (adj, connected) for every labeled cubic graph with N(0)={1,2,3}.
    Each such labeled graph appears EXACTLY once (unique forward-choice path).
    Completeness: every iso class has a member with N(0)={1,2,3} (relabel any
    vertex to 0 and its neighbors to 1,2,3)."""
    assert n % 2 == 0
    adj = [set() for _ in range(n)]
    for v in (1, 2, 3):
        adj[0].add(v); adj[v].add(0)

    def rec(i):
        if i >= n:
            if all(len(adj[v]) == 3 for v in range(n)):
                # connectedness
                seen = {0}; stack = [0]
                while stack:
                    v = stack.pop()
                    for u in adj[v]:
                        if u not in seen:
                            seen.add(u); stack.append(u)
                yield ([sorted(adj[v]) for v in range(n)], len(seen) == n)
            return
        back = sum(1 for u in adj[i] if u < i)
        f = 3 - back
        if f < 0:
            return
        if f == 0:
            yield from rec(i + 1)
            return
        cands = [j for j in range(i + 1, n) if len(adj[j]) < 3 and j not in adj[i]]
        forced = None
        if i + 1 < n and not any(u < i + 1 for u in adj[i + 1]):
            if (i + 1) not in adj[i]:
                if (i + 1) not in cands:
                    return
                forced = i + 1
        if f > len(cands):
            return
        combos = ([c for c in itertools.combinations(cands, f) if forced in c]
                  if forced is not None else itertools.combinations(cands, f))
        for c in combos:
            for j in c:
                adj[i].add(j); adj[j].add(i)
            ok = True
            for j in range(i + 1, n):
                bd = sum(1 for u in adj[j] if u < j)
                if bd > 3 or (3 - bd) > (j - 1 - i) + (n - 1 - j):
                    ok = False; break
                need = j - n + 4
                if need > 0 and bd + (j - 1 - i) < need:
                    ok = False; break
            if ok:
                yield from rec(i + 1)
            for j in c:
                adj[i].discard(j); adj[j].discard(i)

    yield from rec(1)

# ---------------- girth (BFS, exact) ----------------
def girth(adj):
    n = len(adj)
    best = n + 1
    for s in range(n):
        dist = [-1] * n; par = [-1] * n
        dist[s] = 0
        q = [s]
        for v in q:
            for u in adj[v]:
                if dist[u] == -1:
                    dist[u] = dist[v] + 1; par[u] = v; q.append(u)
                elif u != par[v] and par[u] != v:
                    cyc = dist[v] + dist[u] + 1
                    if cyc < best:
                        best = cyc
                        if best == 3:
                            return 3
        # note: standard BFS girth needs care; use safer per-edge check below
    # Safer exact method: shortest cycle through each start via BFS tree non-tree edges
    best = n + 1
    for s in range(n):
        dist = [-1] * n; par = [-1] * n
        dist[s] = 0; q = [s]
        for v in q:
            for u in adj[v]:
                if dist[u] == -1:
                    dist[u] = dist[v] + 1; par[u] = v; q.append(u)
        for v in range(n):
            for u in adj[v]:
                if v < u and u != par[v] and v != par[u]:
                    cyc = dist[v] + dist[u] + 1
                    if cyc < best:
                        best = cyc
        if best == 3:
            return 3
    return best

# ---------------- independence number (bitmask B&B, exact) ----------------
def alpha(adj):
    n = len(adj)
    N = []
    for v in range(n):
        m = 0
        for u in adj[v] + [v]:
            m |= (1 << u)
        N.append(m)
    full = (1 << n) - 1
    # greedy lower bound
    def greedy(R):
        s = 0; r = R
        while r:
            v = (r & -r).bit_length() - 1
            s |= (1 << v); r &= ~N[v]
        return s
    best_set = greedy(full)
    best = bin(best_set).count("1")
    # order: static max-degree-first not needed; branch dynamically
    sys.setrecursionlimit(10000)
    def bound_ub(R):
        return bin(R).count("1")
    def rec(R, cur):
        nonlocal best, best_set
        if R == 0:
            if cur > best:
                best = cur
            return
        if cur + bound_ub(R) <= best:
            return
        # pick vertex of max degree within R
        v = -1; vd = -1
        r = R
        while r:
            b = r & -r; i = b.bit_length() - 1
            d = bin(N[i] & R).count("1")
            if d > vd:
                vd = d; v = i
            r ^= b
        # branch include v
        rec(R & ~N[v], cur + 1)
        # branch exclude v
        rec(R & ~(1 << v), cur)
    rec(full, 0)
    # recover one witness set
    R = full; S = []
    # simple recovery: greedy from best via re-run storing choices is complex;
    # instead brute-force recover small witness by checking subsets of size best
    return best

def alpha_with_set(adj):
    a = alpha(adj)
    n = len(adj)
    N = [set(adj[v]) | {v} for v in range(n)]
    for S in itertools.combinations(range(n), a):
        Ss = set(S)
        if all((Ss - {v} - set(adj[v])) == (Ss - {v}) or True for v in S):
            ok = True
            for v in S:
                if any(u in Ss for u in adj[v]):
                    ok = False; break
            if ok:
                return a, list(S)
    raise AssertionError("no witness")

def alpha_bruteforce(adj):
    """Independent slow exact alpha (subset enumeration). Used as cross-check."""
    n = len(adj)
    E = [(v, u) for v in range(n) for u in adj[v] if v < u]
    for k in range(n, -1, -1):
        for S in itertools.combinations(range(n), k):
            Ss = set(S)
            if all(v not in Ss or u not in Ss for v, u in E):
                return k, list(S)

# ---------------- bridges (Tarjan) ----------------
def bridges(adj):
    n = len(adj)
    disc = [-1] * n; low = [0] * n; t = [0]; out = []
    sys.setrecursionlimit(10000)
    def dfs(v, p):
        disc[v] = low[v] = t[0]; t[0] += 1
        for u in adj[v]:
            if disc[u] == -1:
                dfs(u, v)
                low[v] = min(low[v], low[u])
                if low[u] > disc[v]:
                    out.append((v, u))
            elif u != p:
                low[v] = min(low[v], disc[u])
    dfs(0, -1)
    return out

def is_bridgeless(adj):
    return bridges(adj) == []

# ---------------- canonical hash (individualization-refinement, complete) ----------------
def canonical_form(adj):
    n = len(adj)

    def refine(colors):
        while True:
            sig = {}
            new = []
            for v in range(n):
                key = (colors[v], tuple(sorted(colors[u] for u in adj[v])))
                if key not in sig:
                    sig[key] = len(sig)
                new.append(sig[key])
            same = True
            for a in range(n):
                for b in range(a + 1, n):
                    if (new[a] == new[b]) != (colors[a] == colors[b]):
                        same = False; break
                if not same:
                    break
            if same:
                return new
            colors = new

    def adj_string(order):
        pos = [0] * n
        for i, v in enumerate(order):
            pos[v] = i
        edges = []
        for v in range(n):
            for u in adj[v]:
                if v < u:
                    a, b = pos[v], pos[u]
                    edges.append((a, b) if a < b else (b, a))
        return tuple(sorted(edges))

    base = refine([0] * n)
    best = [None]

    def search(colors):
        d = defaultdict(list)
        for v in range(n):
            d[colors[v]].append(v)
        if len(d) == n:
            order = sorted(range(n), key=lambda v: colors[v])
            s = adj_string(order)
            if best[0] is None or s < best[0]:
                best[0] = s
            return
        cell = min((c for c in d.values() if len(c) > 1),
                   key=lambda c: (len(c), colors[c[0]]))
        fresh = max(colors) + 1
        for v in cell:
            nc = list(colors); nc[v] = fresh
            search(refine(nc))

    search(base)
    return best[0]

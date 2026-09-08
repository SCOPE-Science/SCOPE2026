"""Stdlib-only toolkit v2 for cubic-snark certificates (lane-212)."""
import itertools, math, sys
from collections import deque
from fractions import Fraction

# ---------- basics ----------
def edge_list(adj):
    E = []
    for u in range(len(adj)):
        for v in adj[u]:
            if u < v:
                E.append((u, v))
    return E

def is_cubic(adj):
    return all(len(nbrs) == 3 for nbrs in adj)

def bridges(adj):
    n = len(adj); disc = [-1]*n; low = [0]*n; t = [0]; out = []
    sys.setrecursionlimit(100000)
    def dfs(u, pe):
        disc[u] = low[u] = t[0]; t[0] += 1
        for v in adj[u]:
            if v == pe: continue
            if disc[v] == -1:
                dfs(v, u); low[u] = min(low[u], low[v])
                if low[v] > disc[u]: out.append((u, v))
            elif disc[v] < disc[u]:
                low[u] = min(low[u], disc[v])
    for s in range(n):
        if disc[s] == -1: dfs(s, -1)
    return out

def girth(adj):
    n = len(adj); best = 10**9
    for s in range(n):
        dist = [-1]*n; par = [-1]*n
        dist[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u]+1; par[v] = u; q.append(v)
                elif par[u] != v and par[v] != u:
                    c = dist[u]+dist[v]+1
                    if c < best: best = c
        if best == 3: return 3
    return best

# ---------- perfect matchings ----------
def perfect_matchings(adj, limit=200000):
    n = len(adj); used = [False]*n; mate = [-1]*n; out = []
    nbrs = [list(adj[i]) for i in range(n)]
    def bt():
        if len(out) >= limit: return True
        u = -1
        for i in range(n):
            if not used[i]: u = i; break
        if u == -1:
            pm = tuple((i, mate[i]) for i in range(n) if i < mate[i])
            out.append(pm); return False
        for v in nbrs[u]:
            if not used[v]:
                used[u] = used[v] = True; mate[u] = v; mate[v] = u
                if bt(): return True
                used[u] = used[v] = False; mate[u] = mate[v] = -1
        return False
    bt()
    return out

def pm_masks(adj, E, eindex, limit=200000):
    PMs = perfect_matchings(adj, limit=limit)
    masks = []
    for pm in PMs:
        mk = 0
        for (u, v) in pm:
            a, b = (u, v) if u < v else (v, u)
            mk |= (1 << eindex[(a, b)])
        masks.append(mk)
    return PMs, masks

def is_3_edge_colourable(adj, limit=200000):
    """Exact: cubic G 3-edge-colourable iff E partitions into 3 PMs."""
    n = len(adj); E = edge_list(adj); m = len(E)
    assert m == 3*n//2
    eindex = {e: i for i, e in enumerate(E)}
    PMs, masks = pm_masks(adj, E, eindex, limit=limit)
    full = (1 << m) - 1
    S = set(masks)
    for i, m1 in enumerate(masks):
        for m2 in masks[i:]:
            if m1 & m2: continue
            if (full ^ (m1 | m2)) in S:
                return True, (m1, m2, full ^ (m1 | m2)), len(PMs)
    return False, None, len(PMs)

def min_cover_depth(adj, E, eindex, masks, maxdepth, time_budget_nodes=3000000):
    """Exact bounded set-cover: can `maxdepth` PMs cover E? Branch on uncovered edge."""
    m = len(E); full = (1 << m) - 1
    by_edge = [[] for _ in range(m)]
    for mk in masks:
        mm = mk; e = 0
        while mm:
            if mm & 1: by_edge[e].append(mk)
            e += 1; mm >>= 1
    nodes = [0]
    from functools import lru_cache
    # order: use tuple memo
    memo = {}
    def bt(unc, d):
        nodes[0] += 1
        if unc == 0: return []
        if d == 0: return None
        key = (unc, d)
        if key in memo: return memo[key]
        e = (unc & (-unc)).bit_length() - 1  # index of lowest set bit
        # lsb index: bit_length-1 of (unc & -unc) gives position
        for mk in by_edge[e]:
            r = bt(unc & (~mk), d-1)
            if r is not None:
                memo[key] = [mk] + r; return memo[key]
        memo[key] = None
        if nodes[0] > time_budget_nodes: raise TimeoutError
        return None
    try:
        r = bt(full, maxdepth)
    except TimeoutError:
        return None
    return r

def exact_pi_small(adj, maxdepth=5):
    """Returns (pi or None, info). Exact for small graphs."""
    col, _, npm = is_3_edge_colourable(adj)
    if col: return 3, {"npm": npm}
    E = edge_list(adj); eindex = {e: i for i, e in enumerate(E)}
    _, masks = pm_masks(adj, E, eindex)
    for d in (4, 5):
        r = min_cover_depth(adj, E, eindex, masks, d)
        if r is not None: return d, {"npm": len(masks)}
    return None, {"npm": len(masks), "note": "pi>5 or search capped"}

# ---------- cyclic connectivity ----------
class DSU:
    __slots__ = ("p", "r")
    def __init__(self, n):
        self.p = list(range(n)); self.r = [0]*n
    def f(self, x):
        p = self.p
        while p[x] != x: p[x] = p[p[x]]; x = p[x]
        return x
    def u(self, a, b):
        a = self.f(a); b = self.f(b)
        if a == b: return
        if self.r[a] < self.r[b]: a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]: self.r[a] += 1

def cut_is_cycle_separating(adj, E, cut_idx):
    n = len(adj)
    cut = set(cut_idx)
    d = DSU(n)
    for i, (u, v) in enumerate(E):
        if i not in cut: d.u(u, v)
    comp = {}
    for x in range(n):
        r = d.f(x)
        comp.setdefault(r, []).append(x)
    if len(comp) < 2: return False
    cutset = set(E[i] for i in cut_idx)
    ckey = set((min(u,v), max(u,v)) for (u, v) in cutset)
    ncyc = 0
    for verts in comp.values():
        s = set(verts); m = 0
        for u in verts:
            for v in adj[u]:
                if v in s and (min(u,v), max(u,v)) not in ckey: m += 1
        m //= 2
        if m >= len(verts): ncyc += 1
    return ncyc >= 2

def cyclic_scan(adj, kmax=4):
    """Exhaustive serial search for cycle-separating cuts of size<=kmax.
    Returns dict size->(found, witness_or_None, combos_scanned). Stops at first size with a witness."""
    E = edge_list(adj); m = len(E)
    res = {}
    for sz in range(1, kmax+1):
        found = None; scanned = 0
        for cut in itertools.combinations(range(m), sz):
            scanned += 1
            if cut_is_cycle_separating(adj, E, cut):
                found = tuple(E[i] for i in cut); break
        res[sz] = (found is not None, found, scanned)
        if found is not None:
            break
    return res

# ---------- modular circular-flow certificate ----------
def verify_circular_flow(adj, E, orient, fval, p, q):
    """orient: dict (u,v)->(tail,head); fval: dict edge->int in 1..p-1.
    Check allowed range [q,p-q] and Kirchhoff mod p."""
    n = len(adj)
    for e in E:
        a = fval[e]
        if not (q <= a <= p - q):
            return False, f"edge {e} value {a} outside [{q},{p-q}]"
    for v in range(n):
        tot = 0
        for e in E:
            if v not in e: continue
            t, h = orient[e]
            if v == h: tot += fval[e]
            else: tot -= fval[e]
        if tot % p != 0:
            return False, f"Kirchhoff fail at {v}: {tot} mod {p}"
    return True, "ok"

def sa_circular_flow(adj, E, p, q, iters=60000, restarts=6, seed=0):
    import random
    rng = random.Random(seed)
    allowed = list(range(q, p - q + 1))
    orient = {e: e for e in E}  # tail=u head=v with u<v
    incid = [[] for _ in range(len(adj))]
    for e in E:
        incid[e[0]].append((e, -1)); incid[e[1]].append((e, +1))
    best = None
    for rs in range(restarts):
        T0, T1 = 2.0, 0.02
        f = {e: rng.choice(allowed) for e in E}
        bal = [0]*len(adj)
        for v in range(len(adj)):
            s = 0
            for (e, sgn) in incid[v]: s += sgn * f[e]
            bal[v] = s % p
        cost = sum(1 for b in bal if b != 0)
        if cost == 0: return f, orient
        for it in range(iters):
            T = T0 * (T1/T0) ** (it/iters)
            e = E[rng.randrange(len(E))]
            old = f[e]; new = rng.choice(allowed)
            if new == old: continue
            u, v = e
            # delta effect: bal[u] -= (new-old), bal[v] += (new-old)
            d = new - old
            bu0 = bal[u]; bv0 = bal[v]
            bu1 = (bu0 - d) % p; bv1 = (bv0 + d) % p
            dc = (bu1 != 0) + (bv1 != 0) - (bu0 != 0) - (bv0 != 0)
            if dc <= 0 or rng.random() < math.exp(-dc / max(T, 1e-9)):
                f[e] = new; bal[u] = bu1; bal[v] = bv1; cost += dc
                if cost == 0: return f, orient
        if best is None or cost < best[0]: best = (cost, dict(f))
    f = best[1]
    # final cost
    bal = [0]*len(adj)
    for v in range(len(adj)):
        s = 0
        for (e, sgn) in incid[v]: s += sgn * f[e]
        bal[v] = s % p
    cost = sum(1 for b in bal if b != 0)
    return (f, orient) if cost == 0 else (None, None)

# ---------- builders ----------
def _mk(n, elist):
    adj = [[] for _ in range(n)]
    for u, v in elist:
        adj[u].append(v); adj[v].append(u)
    return adj

def petersen():
    E = [(i, (i+1) % 5) for i in range(5)] + [(i, i+5) for i in range(5)] + \
        [(5+i, 5+((i+2) % 5)) for i in range(5)]
    return _mk(10, E)

def flower(k):
    assert k % 2 == 1 and k >= 5
    A = lambda i: i % k; B = lambda i: k + (i % k)
    C = lambda i: 2*k + (i % k); D = lambda i: 3*k + (i % k)
    E = []
    for i in range(k):
        E += [(B(i), A(i)), (B(i), C(i)), (B(i), D(i)), (A(i), A(i+1))]
    for i in range(k-1):
        E += [(C(i), C(i+1)), (D(i), D(i+1))]
    E += [(C(k-1), D(0)), (D(k-1), C(0))]
    return _mk(4*k, E)

def goldberg_chain(k, twist=False):
    """Petersen-minus-{0,1} blocks chained. local idx: 0..7 <-> labels 2..9 minus {0,1}."""
    assert k % 2 == 1 and k >= 5
    loc = {2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7}
    internal = [(2,3),(3,4),(2,7),(3,8),(4,9),(5,7),(7,9),(9,6),(6,8),(8,5)]
    n = 8*k; E = []
    for i in range(k):
        for (a, b) in internal:
            E.append((i*8+loc[a], i*8+loc[b]))
    # Wire as (2,2)-pole chain: in-stubs {local0 (node2), local3 (node5)},
    # out-stubs {local2 (node4), local4 (node6)}; junction i->j uses 2 edges.
    for i in range(k):
        j = (i+1) % k
        if twist and j == 0:
            E.append((i*8+2, j*8+3)); E.append((i*8+4, j*8+0))
        else:
            E.append((i*8+2, j*8+0)); E.append((i*8+4, j*8+3))
    return _mk(n, E)

def generalized_petersen(n, k):
    E = []
    for i in range(n):
        E.append((i, (i+1) % n))
        E.append((i, i+n))
        E.append((n+i, n+((i+k) % n)))
    return _mk(2*n, E)


def dot_petersen_pairing(pairing):
    """Dot product of two Petersens -> 18 vertices. pairing: tuple of 4 H-stubs matched to (a,b,c,d)."""
    P = petersen(); E1 = edge_list(P)
    # G1: remove independent edges (0,1) outer and (7,9) inner? check independent: vertices {0,1,7,9} distinct -> independent.
    e1 = (0,1); e2 = (7,9) if 7 in P[9] else None
    assert e2 is not None
    stubsG = [0,1,7,9]
    # H: remove adjacent vertices 0,1 -> stubs at 4,5 (from 0) and 2,6 (from 1)
    stubsH = [4,5,2,6]  # H-local
    n = 18
    E = []
    for (u, v) in E1:
        if (min(u,v),max(u,v)) in [(0,1),(7,9)]: continue
        E.append((u, v))
    # H part offset by 10; drop vertices 0,1; remap v->v+8 (so 2..9 -> 10..17)
    for (u, v) in E1:
        if u in (0,1) or v in (0,1): continue
        E.append((u+8, v+8))
    # join stubs: stubsG[i] <-> stubsH[pairing[i]]+8
    for i, h in enumerate(pairing):
        E.append((stubsG[i], stubsH[h]+8))
    return _mk(n, E)

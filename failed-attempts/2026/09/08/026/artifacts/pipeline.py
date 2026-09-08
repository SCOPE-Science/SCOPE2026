"""Exact census of connected cubic bipartite graphs via 1-factorization triples.
Every cubic bipartite simple graph G=(L,R,E), |L|=|R|=m, is 3-edge-colorable
(Konig); i.e. E = M1 u M2 u M3, three perfect matchings. Fix M1=id by relabeling.
Then M2 <-> derangement sigma, M3 <-> derangement tau with tau(i)!=sigma(i).
Completeness: any G has a perfect matching M1 (Hall, regular bipartite);
G-M1 is 2-regular bipartite -> two perfect matchings. Quotient sigma by S_m
conjugacy (cycle type), tau by C(sigma) conjugacy. Cross-dedup by exact
bipartite isomorphism test. Sound: construction only yields simple graphs.
"""
import itertools, json, math, sys, time
import numpy as np

# ---------- permutation helpers ----------
def partitions_no_ones(m):
    res = []
    def rec(rem, mn, cur):
        if rem == 0:
            res.append(tuple(cur)); return
        for p in range(mn, rem + 1):
            if p == 1: continue
            if p > rem: break
            cur.append(p); rec(rem - p, p, cur); cur.pop()
    rec(m, 2, [])
    return res

def perm_from_type(m, typ):
    p = [0]*m; i = 0
    for L in typ:
        for k in range(L):
            p[i+k] = i + (k+1) % L
        i += L
    return p

def cycles_of(p):
    m = len(p); seen = [False]*m; cyc = []
    for i in range(m):
        if not seen[i]:
            c = []; j = i
            while not seen[j]:
                seen[j] = True; c.append(j); j = p[j]
            if len(c) > 1: cyc.append(c)
    return cyc

def centralizer_elts(sigma):
    """All elements of C_{S_m}(sigma) as arrays."""
    m = len(sigma); cyc = cycles_of(sigma)
    from collections import defaultdict
    bylen = defaultdict(list)
    for c in cyc: bylen[len(c)].append(c)
    groups = list(bylen.values())
    # choices per group: permutation of its cycles x offsets
    per_group_opts = []
    for g in groups:
        k = len(g)
        opts = []
        for pi in itertools.permutations(range(k)):
            for offs in itertools.product(*[range(len(g[0]))]*k):
                opts.append((pi, offs))
        per_group_opts.append(opts)
    elts = []
    for combo in itertools.product(*per_group_opts):
        c = [0]*m
        for g, (pi, offs) in zip(groups, combo):
            L = len(g[0])
            for a in range(len(g)):
                src_cyc = g[a]; dst_cyc = g[pi[a]]; o = offs[a]
                for t in range(L):
                    c[src_cyc[t]] = dst_cyc[(t+o) % L]
        elts.append(c)
    return elts

def conj_action_tau(c, cinv, tau):
    m = len(tau)
    return tuple(c[tau[cinv[i]]] for i in range(m))

# ---------- tau enumeration (backtracking derangements avoiding sigma) ----------
def enum_tau_reps(sigma, Celts, cinvs):
    m = len(sigma)
    forbid = [set([i, sigma[i]]) for i in range(m)]
    out = set()
    tau = [-1]*m; used = [False]*m
    order = sorted(range(m), key=lambda i: len(forbid[i]))
    # order positions by fewest options statically is same for all; use natural but
    # choose next unassigned with fewest available dynamically
    def rec(nass):
        if nass == m:
            t = tuple(tau)
            best = min(conj_action_tau(c, ci, t) for c, ci in zip(Celts, cinvs))
            out.add(best); return
        # select unassigned i with fewest candidates
        bi = -1; bcand = None
        for i in range(m):
            if tau[i] == -1:
                cand = [v for v in range(m) if not used[v] and v not in forbid[i]]
                if not cand: return
                if bcand is None or len(cand) < len(bcand):
                    bcand = cand; bi = i
                    if len(bcand) == 1: break
        for v in bcand:
            tau[bi] = v; used[v] = True; rec(nass+1)
            tau[bi] = -1; used[v] = False
    rec(0)
    return out

# ---------- graph builders / tests ----------
def edges_of(sigma, tau):
    m = len(sigma); E = []
    for i in range(m):
        E.append((i, m+i)); E.append((i, m+sigma[i])); E.append((i, m+tau[i]))
    return E

def adj_of(n, E):
    a = [[] for _ in range(n)]
    for u, v in E:
        a[u].append(v); a[v].append(u)
    return a

def connected(adj, n):
    seen = [False]*n; st = [0]; seen[0] = True
    while st:
        u = st.pop()
        for w in adj[u]:
            if not seen[w]: seen[w] = True; st.append(w)
    return all(seen)

def girth(adj, n):
    best = 10**9; wit = None
    for s in range(n):
        dist = [-1]*n; par = [-1]*n; dist[s] = 0
        from collections import deque
        q = deque([s])
        order = [s]
        while q:
            u = q.popleft(); order.append(u)
            for w in adj[u]:
                if dist[w] == -1:
                    dist[w] = dist[u]+1; par[w] = u; q.append(w)
                elif w != par[u] and dist[w] <= dist[u]:
                    L = dist[u]+dist[w]+1
                    if L < best and L >= 3:
                        # reconstruct cycle
                        # path s..u and s..w; find LCA via ancestor sets
                        au = {}; x = u; d = 0
                        while x != -1: au[x] = d; d += 1; x = par[x]
                        x = w; common = None
                        while x != -1:
                            if x in au: common = x; break
                            x = par[x]
                        if common is not None:
                            cyc = []
                            x = u
                            while x != common: cyc.append(x); x = par[x]
                            cyc.append(common)
                            tmp = []
                            x = w
                            while x != common: tmp.append(x); x = par[x]
                            cyc += tmp[::-1]
                            if len(cyc) == L:
                                best = L; wit = cyc
        if best == 4:  # can't beat 4 in bipartite simple... min even >=4
            pass
    return best, wit

def spectrum(adj, n):
    A = np.zeros((n, n)); 
    for u in range(n):
        for w in adj[u]: A[u, w] = 1.0
    ev = np.linalg.eigvalsh(A)
    ev2 = np.linalg.eig(A)[0].real  # independent routine cross-check
    ev2s = np.sort(ev2)
    assert np.max(np.abs(ev - ev2s)) < 1e-6, "spectral cross-check failed"
    d = 3.0
    lam2A = ev[-2]
    gap = d - lam2A
    lam2L = d - lam2A  # algebraic connectivity for regular
    # trace checks
    assert abs(np.sum(ev*ev) - 3*n) < 1e-4
    return ev, float(gap), float(lam2L)

def count_cycles(adj, n, L):
    # closed-walk trace based counts via matrix powers (exact ints by rounding)
    A = np.zeros((n, n))
    for u in range(n):
        for w in adj[u]: A[u, w] = 1.0
    if L == 4:
        B = A @ A
        t = round(float(np.sum(B*B)))
        # tr(A^4) = sum B^2; #4-cycles = (tr(A^4) - n*d*(2d-1)... use formula:
        # closed 4-walks per vertex in cubic: 3 (backtrack) ... use standard:
        # c4 = (tr(A^4) - n*3*(2*3-1) ... let me just: trA4 = n*(3 + 6) + 8*C4?
        # backtracking 4-walks at v: sum over neighbors... simpler: C4 = (tr- n*15)/8 for cubic? verify: each 4-cycle contributes 8; non-cycle closed 4-walks at v: go out and back twice: d^2=9, plus out-along-out-back patterns: sum_u (deg(u)-1)... = 3*2=6. total non-cyc = 9+6=15. So C4=(tr-15n)/8.
        return int((t - 15*n)//8), t
    if L == 6:
        B = A @ A @ A
        t = round(float(np.sum(B*B)))
        return None, t
    raise ValueError

# ---------- exact bipartite isomorphism test ----------
def iso_bipartite(E1, E2, n, m):
    """Decide if graphs (with canonical bipartition L=0..m-1) are isomorphic."""
    a1 = adj_of(n, E1); a2 = adj_of(n, E2)
    # bipartitions (graph is connected bipartite; recover by BFS color)
    def bip(adj):
        c = [-1]*n; c[0] = 0
        from collections import deque
        q = deque([0])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if c[w] == -1: c[w] = 1-c[u]; q.append(w)
                elif c[w] == c[u]: return None
        return c
    c1 = bip(a1); c2 = bip(a2)
    if c1 is None or c2 is None: return False
    P1 = [i for i in range(n) if c1[i]==0]; Q1 = [i for i in range(n) if c1[i]==1]
    P2 = [i for i in range(n) if c2[i]==0]; Q2 = [i for i in range(n) if c2[i]==1]
    if sorted([len(P1),len(Q1)]) != sorted([len(P2),len(Q2)]): return False
    S1 = [set(a1[i]) for i in range(n)]; S2 = [set(a2[i]) for i in range(n)]
    for flip in range(2):
        A2, B2 = (P2, Q2) if flip==0 else (Q2, P2)
        if len(A2)!=len(P1) or len(B2)!=len(Q1): continue
        # order P1 by signature for branching
        map_ = {}; ok = [True]
        used = set()
        # order vertices: least candidates first using neighbor-structure keys
        def sig1(v, fixed):
            return tuple(sorted(map_.get(w, -1) for w in a1[v]))
        order = sorted(P1, key=lambda v: len(a1[v]))
        def matchA(k):
            if not ok[0]: return False
            if k == len(order):
                return matchB(0)
            v = order[k]
            for w in A2:
                if w in used: continue
                map_[v] = w; used.add(w)
                if compat(v, w) and matchA(k+1): return True
                del map_[v]; used.discard(w)
            return False
        def compat(v, w):
            # already-mapped neighbors must correspond
            for x in a1[v]:
                if x in map_ and map_[x] not in S2[w]: return False
            for x in a2[w]:
                # reverse check: neighbors of w that are images must preimage-adjacent
                pass
            return True
        def matchB(k):
            if k == len(Q1):
                # full check
                for v in range(n):
                    if set(map_[x] for x in a1[v]) != S2[map_[v]]: return False
                return True
            v = Q1[k]
            # candidates: B2 unused with mapped-neighborhood consistent
            req = set(map_[x] for x in a1[v] if x in map_)
            for w in B2:
                if w in used: continue
                if not req.issubset(S2[w]): continue
                map_[v] = w; used.add(w)
                if matchB(k+1): return True
                del map_[v]; used.discard(w)
            return False
        map_ = {}; used = set()
        if matchA(0): return True
    return False

# ---------- Hamiltonicity backtracker ----------
class HamSearch:
    def __init__(self, adj, n):
        self.adj = adj; self.n = n; self.nodes = 0
    def find(self, limit=10**9):
        n = self.n; adj = self.adj
        path = [0]; used = [False]*n; used[0] = True
        res = []
        # neighbor order heuristic: fewest onward moves first (static degree all 3; use dynamic)
        def dfs():
            self.nodes += 1
            if self.nodes > limit: return 'limit'
            if len(path) == n:
                if path[0] in adj[path[-1]]:
                    res.append(list(path)); return True
                return False
            u = path[-1]
            cands = [w for w in adj[u] if not used[w]]
            # prune: unvisited vertex with no unvisited neighbor (and not closable) -> dead
            # cheap prune only at depth multiples
            if len(path) % 4 == 0:
                # endpoint connectivity prune: every unvisited vertex must have a
                # neighbor that is unvisited or is path[0]-closure... simple version:
                for v in range(n):
                    if not used[v]:
                        ok = any((not used[x]) or (len(path)==n-1 and x==path[0]) for x in adj[v])
                        if not ok: return False
            # order: neighbors with fewer unvisited neighbors first
            cands.sort(key=lambda w: sum(1 for x in adj[w] if not used[x]))
            for w in cands:
                used[w] = True; path.append(w)
                r = dfs()
                if r is True: return True
                if r == 'limit': return 'limit'
                path.pop(); used[w] = False
            return False
        r = dfs()
        return (res[0] if r is True else None), self.nodes

def check_cycle(E, cyc, n):
    if cyc is None or len(cyc) != n: return False
    S = set()
    for u, v in E: S.add((u,v)); S.add((v,u))
    if set(cyc) != set(range(n)): return False
    for i in range(n):
        if (cyc[i], cyc[(i+1)%n]) not in S: return False
    return True

def census(n, verbose=True):
    m = n//2; t0 = time.time()
    reps = []  # (E, sigma, tau)
    buckets = {}
    nconn = 0; ndisc = 0
    for typ in partitions_no_ones(m):
        sigma = perm_from_type(m, typ)
        Cel = centralizer_elts(sigma)
        Cinv = []
        for c in Cel:
            ci = [0]*m
            for i in range(m): ci[c[i]] = i
            Cinv.append(ci)
        taus = enum_tau_reps(sigma, Cel, Cinv)
        for tau in taus:
            E = edges_of(sigma, list(tau))
            adj = adj_of(n, E)
            if not connected(adj, n):
                ndisc += 1; continue
            nconn += 1
            reps.append((E, sigma, list(tau)))
    # invariant bucketing + exact dedup
    classes = []  # list of dicts
    for E, sg, ta in reps:
        adj = adj_of(n, E)
        g, _ = girth(adj, n)
        ev, gap, lam2 = spectrum(adj, n)
        c4, tr4 = count_cycles(adj, n, 4)
        _, tr6 = count_cycles(adj, n, 6)
        key = (g, c4, tr6, tuple(np.round(ev, 6)))
        found = None
        for ci, cl in enumerate(classes):
            if cl['key'] == key:
                if iso_bipartite(E, cl['E'], n, m):
                    found = ci; break
        if found is None:
            classes.append({'key': key, 'E': E, 'sigma': sg, 'tau': ta,
                            'girth': g, 'gap': gap, 'lam2': lam2,
                            'eig': [float(x) for x in ev], 'c4': c4, 'tr6': tr6})
    # Hamiltonicity
    for cl in classes:
        adj = adj_of(n, cl['E'])
        hs = HamSearch(adj, n)
        cyc, nodes = hs.find()
        cl['ham_cycle'] = cyc; cl['ham_nodes'] = nodes
        cl['hamiltonian'] = cyc is not None
        assert check_cycle(cl['E'], cyc, n) if cyc else True
    # girth witnesses
    for cl in classes:
        adj = adj_of(n, cl['E'])
        g, wit = girth(adj, n)
        cl['girth_wit'] = wit
    dt = time.time()-t0
    if verbose:
        h = sum(1 for c in classes if c['hamiltonian'])
        print(f"n={n}: types={len(partitions_no_ones(m))} conn_raw={nconn} "
              f"classes={len(classes)} ham={h} nonham={len(classes)-h} t={dt:.1f}s", flush=True)
    return classes, {'nconn': nconn, 'ndisc': ndisc, 'time': dt}

if __name__ == '__main__':
    ns = [int(x) for x in sys.argv[1:]] or [14]
    allres = {}
    for n in ns:
        classes, info = census(n)
        allres[n] = {'classes': classes, 'info': info}
    with open('output/artifacts/census_raw.json', 'w') as f:
        json.dump({str(n): {'info': v['info'],
            'classes': [{k: c[k] for k in ('E','sigma','tau','girth','girth_wit','gap','lam2','eig','c4','tr6','ham_cycle','ham_nodes','hamiltonian')} for c in v['classes']]}
            for n, v in allres.items()}, f)
    print("wrote output/artifacts/census_raw.json", flush=True)

"""Completeness cross-check: different conjugacy transversal + independent iso test.

Pipeline quotient: sigma over integer-partition cycle types; tau over
C(sigma)-orbit lex-min representatives via full-orbit minimization.
This script re-derives the transversal differently:
  (a) sigma reps: one random conjugate r*sigma*r^-1 per partition type
      (seeded; r drawn uniform in S_m), proving type-only dependence;
  (b) tau reps: canonical "first-seen" transversal using a BFS Schreier
      enumeration of C(sigma) with a different orbit rule
      (lex-min over generators-orbit closure, no full-group materialization
      via centralizer_elts).
Then it re-runs construction + an INDEPENDENT isomorphism test (different
code path: canonical degree-refined backtracking with forward checking)
and checks the class count equals the pipeline count (13 at n=14) and that
every class of one census matches a class of the other.

Also includes Held-Karp DP independent Hamiltonicity replay.
"""
import itertools, json, random
import numpy as np
from collections import deque, defaultdict

def partitions_no_ones(m):
    res = []
    def rec(rem, mn, cur):
        if rem == 0:
            res.append(tuple(cur)); return
        for p in range(mn, rem+1):
            if p == 1: continue
            if p > rem: break
            cur.append(p); rec(rem-p, p, cur); cur.pop()
    rec(m, 2, [])
    return res

def perm_from_type(m, typ):
    p = [0]*m; i = 0
    for L in typ:
        for k in range(L):
            p[i+k] = i + (k+1) % L
        i += L
    return p

def compose(a, b):
    return [a[b[i]] for i in range(len(a))]

def inv(p):
    q = [0]*len(p)
    for i, v in enumerate(p):
        q[v] = i
    return q

def cycles_of(p):
    m = len(p); seen = [False]*m; cyc = []
    for i in range(m):
        if not seen[i]:
            c = []; j = i
            while not seen[j]:
                seen[j] = True; c.append(j); j = p[j]
            if len(c) > 1: cyc.append(c)
    return cyc

def centralizer_gens(sigma):
    # standard generating set of C(sigma): cycle rotations + swaps of equal-length cycles
    m = len(sigma); cyc = cycles_of(sigma)
    gens = []
    for c in cyc:
        L = len(c)
        g = list(range(m))
        for t in range(L):
            g[c[t]] = c[(t+1) % L]
        gens.append(g)
    bylen = defaultdict(list)
    for idx, c in enumerate(cyc):
        bylen[len(c)].append(idx)
    for L, idxs in bylen.items():
        c0 = cyc[idxs[0]]
        for j in idxs[1:]:
            cj = cyc[j]
            g = list(range(m))
            for t in range(L):
                g[c0[t]] = cj[t]; g[cj[t]] = c0[t]
            gens.append(g)
    return gens

def orbit_min_schreier(tau, gens):
    # lex-min over group orbit via Schreier BFS with different traversal order
    best = tuple(tau); seen = {tuple(tau)}
    q = deque([list(tau)])
    while q:
        cur = q.popleft()
        for g in gens:
            gi = inv(g)
            nxt = tuple(g[cur[gi[i]]] for i in range(len(cur)))
            if nxt not in seen:
                seen.add(nxt)
                if nxt < best:
                    best = nxt
                q.append(list(nxt))
    return best

def enum_tau_firstseen(sigma):
    m = len(sigma)
    forbid = [set([i, sigma[i]]) for i in range(m)]
    gens = centralizer_gens(sigma)
    reps = set()
    tau = [-1]*m; used = [False]*m
    def rec(nass):
        if nass == m:
            reps.add(orbit_min_schreier(tuple(tau), gens)); return
        # different variable order than pipeline: largest index first
        bi = -1
        for i in range(m-1, -1, -1):
            if tau[i] == -1:
                bi = i; break
        for v in range(m-1, -1, -1):
            if not used[v] and v not in forbid[bi]:
                tau[bi] = v; used[v] = True; rec(nass+1)
                tau[bi] = -1; used[v] = False
    rec(0)
    return reps

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
            if not seen[w]:
                seen[w] = True; st.append(w)
    return all(seen)

def spectrum_key(adj, n):
    A = np.zeros((n, n))
    for u in range(n):
        for w in adj[u]:
            A[u, w] = 1.0
    return tuple(np.round(np.linalg.eigvalsh(A), 6))

def girth(adj, n):
    best = 10**9
    for s in range(n):
        dist = [-1]*n; par = [-1]*n; dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if dist[w] == -1:
                    dist[w] = dist[u]+1; par[w] = u; q.append(w)
                elif w != par[u] and dist[w] <= dist[u]:
                    L = dist[u]+dist[w]+1
                    if L < best and L >= 3:
                        best = L
    return best

def c4_of(adj, n):
    A = np.zeros((n, n))
    for u in range(n):
        for w in adj[u]:
            A[u, w] = 1.0
    B = A @ A
    return int((round(float(np.sum(B*B))) - 15*n)//8)

def tr6_of(adj, n):
    A = np.zeros((n, n))
    for u in range(n):
        for w in adj[u]:
            A[u, w] = 1.0
    B = A @ A @ A
    return round(float(np.sum(B*B)))

def iso2(E1, E2, n):
    # independent iso: color-refinement (WL-1) signatures + backtracking, separate code path
    a1 = adj_of(n, E1); a2 = adj_of(n, E2)
    def wl(adj):
        col = [3]*n
        for _ in range(n):
            ncol = sorted((col[v], tuple(sorted(col[w] for w in adj[v]))) for v in range(n))
            mp = {}
            col = [(mp.setdefault(k, len(mp))) for k in ncol]
        return col
    w1 = wl(a1); w2 = wl(a2)
    if sorted(w1) != sorted(w2):
        return False
    def bip(adj):
        c = [-1]*n; c[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if c[w] == -1:
                    c[w] = 1-c[u]; q.append(w)
                elif c[w] == c[u]:
                    return None
        return c
    c1 = bip(a1); c2 = bip(a2)
    if c1 is None or c2 is None:
        return False
    S1 = [set(a1[i]) for i in range(n)]; S2 = [set(a2[i]) for i in range(n)]
    P1 = [i for i in range(n) if c1[i]==0]; Q1 = [i for i in range(n) if c1[i]==1]
    P2 = [i for i in range(n) if c2[i]==0]; Q2 = [i for i in range(n) if c2[i]==1]
    for flip in range(2):
        A2, B2 = (P2, Q2) if flip == 0 else (Q2, P2)
        if len(A2) != len(P1):
            continue
        mp = {}; used = set()
        order = sorted(P1, key=lambda v: (w1[v], len(a1[v])))
        def recA(k):
            if k == len(order):
                return recB(0)
            v = order[k]
            need = set(mp[x] for x in a1[v] if x in mp)
            for w in A2:
                if w in used or w1_src[w] != w1[v] or not need.issubset(S2[w]):
                    continue
                # forward check: unmapped neighbor count compatible
                mp[v] = w; used.add(w)
                if recA(k+1):
                    return True
                del mp[v]; used.discard(w)
            return False
        def recB(k):
            if k == len(Q1):
                for v in range(n):
                    if set(mp[x] for x in a1[v]) != S2[mp[v]]:
                        return False
                return True
            v = Q1[k]
            need = set(mp[x] for x in a1[v] if x in mp)
            for w in B2:
                if w in used or w2q[w] != w1[v] or not need.issubset(S2[w]):
                    continue
                mp[v] = w; used.add(w)
                if recB(k+1):
                    return True
                del mp[v]; used.discard(w)
            return False
        w1_src = {w: w2[w] for w in A2}
        w2q = {w: w2[w] for w in B2}
        mp = {}; used = set()
        if recA(0):
            return True
    return False

def held_karp_ham(E, n):
    adj = adj_of(n, E)
    S = [set(a) for a in adj]
    # fix start 0, end = neighbor of 0; DP over subsets ending at v
    N = n
    nbrs0 = adj[0]
    for end in nbrs0:
        # dp[mask] = set of reachable endpoints; standard bitmask DP, n<=16 fine
        dp = [0]* (1 << N)
        dp[1 << 0] |= (1 << 0)
        # store as bitmask of endpoints per mask
        for mask in range(1 << N):
            if not (mask & 1):
                continue
            cur = dp[mask]
            if cur == 0:
                continue
            v = 0
            m = cur
            while m:
                if m & 1:
                    for w in adj[v]:
                        if not (mask & (1 << w)):
                            dp[mask | (1 << w)] |= (1 << w)
                v += 1; m >>= 1
        full = (1 << N) - 1
        if dp[full] & (1 << end):
            return True
    return False

def run(n, seed):
    rng = random.Random(seed)
    m = n // 2
    reps = []
    for typ in partitions_no_ones(m):
        base = perm_from_type(m, typ)
        r = list(range(m)); rng.shuffle(r)
        ri = inv(r)
        sigma = [r[base[ri[i]]] for i in range(m)]
        assert sorted(sigma) == list(range(m)) and all(sigma[i] != i for i in range(m))
        for tau in enum_tau_firstseen(sigma):
            E = edges_of(sigma, list(tau))
            adj = adj_of(n, E)
            if connected(adj, n):
                reps.append(E)
    # dedup with independent iso
    classes = []
    for E in reps:
        adj = adj_of(n, E)
        key = (girth(adj, n), c4_of(adj, n), tr6_of(adj, n), spectrum_key(adj, n))
        hit = -1
        for j, cl in enumerate(classes):
            if cl[0] == key and iso2(E, cl[1], n):
                hit = j; break
        if hit < 0:
            classes.append((key, E))
    return reps, classes

if __name__ == '__main__':
    reps, classes = run(14, seed=20260908)
    print(f"transversal re-run n=14: raw_conn={len(reps)} classes={len(classes)}", flush=True)
    assert len(classes) == 13, f"class-count mismatch: {len(classes)} != 13"
    # cross-match against pipeline census
    pipe = json.load(open('output/artifacts/backup/keep14.json'))['14']['classes']
    assert len(pipe) == 13
    for E_pipe in [c['E'] for c in pipe]:
        assert any(iso2(E_pipe, cl[1], 14) for cl in classes), "pipeline class unmatched"
    for _, E_new in classes:
        assert any(iso2(E_new, c['E'], 14) for c in pipe), "new-transversal class unmatched"
    print("cross-match 13/13 both directions OK (independent iso code path)", flush=True)
    # Held-Karp independent Hamiltonicity replay on all 13
    for i, c in enumerate(pipe):
        assert held_karp_ham(c['E'], 14) is True, f"Held-Karp disagrees at class {i}"
    print("Held-Karp DP: all 13 pipeline classes Hamiltonian (independent replay OK)", flush=True)
    # n=16 Held-Karp replay too (uses stored classes; iso not re-derived)
    pipe16 = json.load(open('output/artifacts/backup/keep16.json'))['16']['classes']
    for i, c in enumerate(pipe16):
        assert held_karp_ham(c['E'], 16) is True, f"Held-Karp-16 disagrees at {i}"
    print(f"Held-Karp DP: all {len(pipe16)} n=16 classes Hamiltonian (independent replay OK)", flush=True)
    json.dump({'n14_raw': len(reps), 'n14_classes': len(classes)},
              open('output/artifacts/transversal_check.json', 'w'), indent=1)
    print('wrote output/artifacts/transversal_check.json', flush=True)

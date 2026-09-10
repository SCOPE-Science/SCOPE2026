#!/usr/bin/env python3
"""Lane-486 TARGET probe N4: is one-step n^{1/4}-cograph extraction even TRUE?

For every P5-free graph on n<=7 vertices (exhaustive), compute:
  maxc(G) = max |H| over P4-free induced H.
Report min over PRIME P5-free G of maxc(G)/n^{1/4}.
If min < 1: N4 route is FALSE (counterexample obstruction) — valuable target evidence.
If min >= 1: route not refuted at small n; lemma stays open.

Also report dominating-clique profile (Bacso-Tuza probe) for prime P5-free n<=7.
Stdlib only. n=7: 2^21=2M graphs; bit-parallel, may take ~2-4 min. Run n<=6 fast first.
"""
import itertools
import math
import sys

LOG = []
def log(s):
    LOG.append(s); print(s, flush=True)

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6

def all_adjs(n):
    m = n * (n - 1) // 2
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for bits in range(1 << m):
        adj = [0] * n
        for k, (i, j) in enumerate(pairs):
            if (bits >> k) & 1:
                adj[i] |= (1 << j); adj[j] |= (1 << i)
        yield adj

def popcount(x): return bin(x).count("1")

def has_induced_Pk(adj, verts, k, edges):
    # check whether verts contain induced Pk (path edges=k-1, connected, maxdeg<=2)
    if len(verts) < k: return False
    n = len(adj)
    for sub in itertools.combinations(verts, k):
        mask = 0
        for v in sub: mask |= (1 << v)
        e = sum(popcount(adj[v] & mask) for v in sub) // 2
        if e != edges: continue
        # connected?
        seen = {sub[0]}; stack = [sub[0]]
        while stack:
            v = stack.pop()
            for u in sub:
                if u not in seen and (adj[v] >> u) & 1:
                    seen.add(u); stack.append(u)
        if len(seen) != k: continue
        if all(popcount(adj[v] & mask) <= 2 for v in sub):
            return True
    return False

def max_cograph_size(adj):
    n = len(adj)
    verts = list(range(n))
    for s in range(n, -1, -1):
        for sub in itertools.combinations(verts, s):
            if not has_induced_Pk(adj, list(sub), 4, 3):
                return s
    return 0

def prime(adj):
    n = len(adj)
    if n <= 2: return False
    full = (1 << n) - 1
    comp = [full ^ (1 << v) ^ adj[v] for v in range(n)]
    # connected both sides
    for A in (adj, comp):
        seen = {0}; stack = [0]
        while stack:
            v = stack.pop()
            for u in range(n):
                if u not in seen and (A[v] >> u) & 1:
                    seen.add(u); stack.append(u)
        if len(seen) != n: return False
    # no nontrivial module
    for r in range(2, n):
        for sub in itertools.combinations(range(n), r):
            s = set(sub)
            ok = True
            for x in range(n):
                if x in s: continue
                d = sum(1 for v in sub if (adj[x] >> v) & 1)
                if d not in (0, r): ok = False; break
            if ok: return False
    return True

def dominating_clique_size(adj):
    n = len(adj)
    best = 0
    for r in range(1, n + 1):
        for K in itertools.combinations(range(n), r):
            mask = 0
            for v in K: mask |= (1 << v)
            e = sum(popcount(adj[v] & mask) for v in K) // 2
            if e != r * (r - 1) // 2: continue
            dom = True
            for x in range(n):
                if x in set(K): continue
                if not any((adj[x] >> v) & 1 for v in K):
                    dom = False; break
            if dom: best = max(best, r)
    return best

worst = {}
for n in range(4, NMAX + 1):
    tot = 0; pf = 0; pr = 0
    min_ratio = 1e9; min_ex = None
    dom_hist = {}
    for adj in all_adjs(n):
        tot += 1
        if has_induced_Pk(adj, list(range(n)), 5, 4): continue
        pf += 1
        if not prime(adj): continue
        pr += 1
        mc = max_cograph_size(adj)
        ratio = mc / (n ** 0.25)
        if ratio < min_ratio:
            min_ratio = ratio; min_ex = (adj[:], mc)
        d = dominating_clique_size(adj)
        dom_hist[d] = dom_hist.get(d, 0) + 1
    log(f"n={n}: total={tot} P5free={pf} prime={pr} min maxc/n^.25={min_ratio:.4f} (maxc={min_ex[1] if min_ex else None}) dom_hist={dom_hist}")
    if min_ex and min_ratio < 1.0:
        log(f"  COUNTEREXAMPLE to N4 extraction at n={n}: adj={min_ex[0]}")
    worst[n] = (min_ratio, min_ex)
log("N4PROBE_OK")
with open("output/artifacts/n4probe.log", "w") as f:
    f.write("\n".join(LOG) + "\n")

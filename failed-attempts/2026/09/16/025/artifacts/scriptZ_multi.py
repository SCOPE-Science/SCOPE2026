"""Script Z: multi-center / deep-block iteration of the W-star.
Script Y: two centers sharing the SAME W -> C7. Alternatives for MORE surplus:
 (i) disjoint W's per center: partition W-top? W has size ~0.235n; per-center disjoint
     subsets give sum C(k_i,2) maximized at single block (convexity) — no gain.
 (ii) iterate at deeper levels: apply W-star inside H[V2] recursively! Surplus at level1:
     C(|W|,2); level2: C(|W2|,2) with W2 = top of V2^(1)-remainder... total = Theta(n^2)
     with BIGGER constant (geometric series across levels). Verify C7-freeness of
     2-level starred family at n=26,36 exactly/heuristic.
 (iii) star at EVERY x in X on disjoint... same as (i), convexity says concentrate.
Test (ii): build B_rec + W-star at level0 AND level1 (x0' in V1^(1), W'=V1^(2))."""
import random, sys, itertools
from math import comb
from collections import defaultdict
sys.setrecursionlimit(10000)

def brec_dp(N):
    b = [0]*(N+1); ch = [None]*(N+1)
    for n in range(3, N+1):
        best = -1; ba = 0
        for a in range(n+1):
            v = comb(a, 2)*(n-a) + b[n-a]
            if v > best: best = v; ba = a
        b[n] = best; ch[n] = ba
    return b, ch
B, CH = brec_dp(120)

def build_brec(n):
    edges = set(); depth = {}
    blocks_by_depth = {}
    def rec(verts, d):
        m = len(verts)
        if m <= 2:
            for v in verts: depth[v] = d
            blocks_by_depth.setdefault(f"tail{d}", []).extend(verts)
            return
        a = CH[m]
        V1 = verts[:a]; V2 = verts[a:]
        for v in V1: depth[v] = d
        blocks_by_depth[d] = list(V1)
        for i in range(len(V1)):
            for j in range(i+1, len(V1)):
                for w in V2:
                    edges.add(tuple(sorted((V1[i], V1[j], w))))
        rec(V2, d+1)
    rec(list(range(n)), 0)
    return edges, depth, blocks_by_depth

def make_link(E):
    L = defaultdict(set)
    for (x, y, z) in E:
        L[(x, y)].add(z); L[(x, z)].add(y); L[(y, x)].add(z)
        L[(y, z)].add(x); L[(z, x)].add(y); L[(z, y)].add(x)
    return L

def has_C7(E, n, cap=1):
    L = make_link(E); found = []
    def bt(path, used):
        if len(found) >= cap: return True
        k = len(path)
        if k == 7:
            if tuple(sorted((path[5], path[6], path[0]))) not in E: return False
            if tuple(sorted((path[6], path[0], path[1]))) not in E: return False
            found.append(tuple(path)); return True
        if k <= 1:
            for v in range(n):
                if v in used: continue
                path.append(v); used.add(v)
                if bt(path, used) and len(found) >= cap: return True
                path.pop(); used.discard(v)
            return False
        for v in L.get((path[-2], path[-1]), ()):
            if v in used: continue
            path.append(v); used.add(v)
            if bt(path, used) and len(found) >= cap: return True
            path.pop(); used.discard(v)
        return False
    for v0 in range(n):
        if bt([v0], {v0}) and len(found) >= cap: break
    return found

def heuristic(E, n, trials=150000, seed=0):
    import random as R
    rng = R.Random(seed)
    for _ in range(trials):
        S = rng.sample(range(n), 7); rng.shuffle(S)
        if all(tuple(sorted((S[i], S[(i+1)%7], S[(i+2)%7]))) in E for i in range(7)):
            return tuple(S)
    return None

for n in [26, 36, 45]:
    E0, depth, blks = build_brec(n)
    adds = set()
    info = []
    for d in sorted(k for k in blks if isinstance(k, int)):
        V1d = blks[d]
        # W for level d = top block of remainder = blks[d+1] if exists
        if (d+1) in blks:
            W = blks[d+1]
            x0 = V1d[0]
            s = {tuple(sorted((x0, W[i], W[j]))) for i in range(len(W)) for j in range(i+1, len(W))} - E0 - adds
            adds |= s
            info.append(f"L{d}: x0 in V1^({d}), |W|={len(W)}, +{len(s)}")
    E1 = E0 | adds
    r = heuristic(E1, n, trials=150000, seed=n)
    print(f"n={n} brec={len(E0)} multilevel-star +{len(adds)} C7={r}", flush=True)
    for i in info: print("   ", i, flush=True)

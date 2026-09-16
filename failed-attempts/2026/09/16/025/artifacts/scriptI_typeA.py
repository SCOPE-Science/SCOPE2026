"""Script I: sharpness hunt v2 — can we add Theta(n^2) 'inV1=1' triples (1 in V1, 2 in V2)?
Structure: B[V1,V2] has {x,y in V1; w in V2}. Candidate extra: {x in V1; w1,w2 in V2}.
Danger: C7 templates. Heuristic search at n=15..30: random subsets of candidate extras,
C7-tested with fast detector; maximize safe count. Also try 'star at one x' and
'complete bipartite-pair' patterns."""
import random, sys, itertools
sys.path.insert(0, 'output/artifacts')
import importlib.util
spec = importlib.util.spec_from_file_location("e2", "output/artifacts/scriptE2_fast.py")
# scriptE2_fast runs experiments on import; instead reimplement minimal builder+detector here.
from math import comb

def brec_dp(N):
    b = [0]*(N+1); ch = [None]*(N+1)
    for n in range(3, N+1):
        best = -1; ba = 0
        for a in range(n+1):
            v = comb(a, 2)*(n-a) + b[n-a]
            if v > best: best = v; ba = a
        b[n] = best; ch[n] = ba
    return b, ch
B, CH = brec_dp(80)

def build_brec(n):
    edges = set(); depth = {}
    def rec(verts, d):
        m = len(verts)
        if m <= 2:
            for v in verts: depth[v] = d
            return
        a = CH[m]
        V1 = verts[:a]; V2 = verts[a:]
        for v in V1: depth[v] = d
        for i in range(len(V1)):
            for j in range(i+1, len(V1)):
                for w in V2:
                    edges.add(tuple(sorted((V1[i], V1[j], w))))
        rec(V2, d+1)
    rec(list(range(n)), 0)
    blocks = {}
    for v, d in depth.items(): blocks.setdefault(d, []).append(v)
    return edges, depth, blocks

def make_link(E):
    from collections import defaultdict
    L = defaultdict(set)
    for (x, y, z) in E:
        L[(x, y)].add(z); L[(x, z)].add(y); L[(y, x)].add(z)
        L[(y, z)].add(x); L[(z, x)].add(y); L[(z, y)].add(x)
    return L

def has_C7(E, n, cap=1, max_expand=60):
    L = make_link(E); found = []
    sys.setrecursionlimit(10000)
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
        nbrs = L.get((path[-2], path[-1]), ())
        if len(nbrs) > max_expand:
            nbrs = list(nbrs)[:max_expand]
        for v in nbrs:
            if v in used: continue
            path.append(v); used.add(v)
            if bt(path, used) and len(found) >= cap: return True
            path.pop(); used.discard(v)
        return False
    for v0 in range(n):
        if bt([v0], {v0}) and len(found) >= cap: break
    return found

def greedy_extra(E0, n, cands, seed=0, order_shuffle=True):
    rng = random.Random(seed)
    if order_shuffle: rng.shuffle(cands)
    cur = set(E0)
    for t in cands:
        cur.add(t)
        if has_C7(cur, n, cap=1):
            cur.discard(t)
    return cur

for n in [12, 15, 18]:
    E0, depth, blocks = build_brec(n)
    V1 = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(V1))
    # candidate extras type A: {x in V1, w1<w2 in V2}
    candsA = [tuple(sorted((x, w1, w2))) for x in V1 for i, w1 in enumerate(V2) for w2 in V2[i+1:]]
    candsA = [t for t in candsA if t not in E0]
    print(f"n={n} |V1|={len(V1)} |V2|={len(V2)} brec={len(E0)} typeA-cands={len(candsA)}", flush=True)
    cur = greedy_extra(E0, n, list(candsA), seed=3)
    print(f"  greedy typeA safe: +{len(cur)-len(E0)} extras (total {len(cur)})", flush=True)
    # type S: star at single x0: all {x0,w1,w2}
    x0 = V1[0]
    candsS = [tuple(sorted((x0, w1, w2))) for i, w1 in enumerate(V2) for w2 in V2[i+1:]]
    candsS = [t for t in candsS if t not in E0]
    E1 = set(E0) | set(candsS)
    print(f"  full star at x0: +{len(candsS)} C7={bool(has_C7(E1, n))}", flush=True)

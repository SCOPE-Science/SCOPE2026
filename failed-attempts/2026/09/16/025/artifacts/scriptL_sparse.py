"""Script L: sparser star families.
Idea L1: star pairs restricted to a subset W of V2 with W contained in ONE deep block
  (e.g. W = deepest block). Then star edges {x0,w1,w2}, w1,w2 in W.
Idea L2: pairs forming a matching/star-forest inside V2 (linear count — fallback probe).
Idea L3: W = V2^(1) top-of-V2 block only.
Test each for C7 at n=18..45 via heuristic + exact small check."""
import random, sys
from math import comb
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

def heuristic(E, n, trials=150000, seed=0):
    rng = random.Random(seed)
    for _ in range(trials):
        S = rng.sample(range(n), 7); rng.shuffle(S)
        if all(tuple(sorted((S[i], S[(i+1)%7], S[(i+2)%7]))) in E for i in range(7)):
            return tuple(S)
    return None

def test_family(n, W, tag):
    E0, depth, blocks = build_brec(n)
    V1 = sorted(blocks[0])
    x0 = V1[0]
    star = set()
    W = sorted(W)
    for i in range(len(W)):
        for j in range(i+1, len(W)):
            t = tuple(sorted((x0, W[i], W[j])))
            if t not in E0: star.add(t)
    E1 = E0 | star
    r = heuristic(E1, n, trials=150000, seed=n*7+len(W))
    print(f"n={n} {tag}: |W|={len(W)} +{len(star)} heur-C7={r}", flush=True)

for n in [18, 26, 36, 45]:
    E0, depth, blocks = build_brec(n)
    V1 = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(V1))
    deeps = sorted(set(depth.values()))
    for d in deeps[1:]:
        W = [v for v in V2 if depth[v] == d]
        if len(W) >= 3:
            test_family(n, W, f"deepblock d={d}")
    # W = top-of-V2 block (depth 1)
    W1 = [v for v in V2 if depth[v] == 1]
    test_family(n, W1, "V2-top-block")

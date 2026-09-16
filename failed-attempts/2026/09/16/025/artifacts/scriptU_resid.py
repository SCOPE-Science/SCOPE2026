"""Script U: link-graph approach to cover lemma.
For C7-free H and candidate X: nonB triples = {x1,x2 in X... no wait nonB = E\B(X,Y):
types: (3 in X), (1 in X 2 in Y), (0 in X, 3 in Y... but those are H[Y] handled by induction).
Hmm: nonB includes H[Y] triples (0 in X)! Restructure: e(H) = |H cap B| + |H[X] (3 in X)|
+ |crossing type (1,2)| + |H[Y]|. Induction handles H[Y]. So need BOUND on H[X] + crossing(1,2).
Probe at scale: take B_rec + W-star extremal-ish graphs, compute for best partition the
two pieces. Also random C7-free graphs (greedy) at n=12..20: measure min over X (|X|>=n/2)
of (|H[X]| + |crossing(1,2)|)/n^2. If bounded by small K at scale -> strong evidence."""
import random, sys, itertools
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

def heuristic(E, n, trials=40000, seed=0):
    rng = random.Random(seed)
    for _ in range(trials):
        S = rng.sample(range(n), 7); rng.shuffle(S)
        if all(tuple(sorted((S[i], S[(i+1)%7], S[(i+2)%7]))) in E for i in range(7)):
            return tuple(S)
    return None

def greedy_random(E0, n, seed):
    all3 = [t for t in itertools.combinations(range(n), 3) if t not in E0]
    rng = random.Random(seed)
    rng.shuffle(all3)
    cur = set(E0)
    for t in all3:
        cur.add(t)
        if heuristic(cur, n, trials=3000, seed=0):
            cur.discard(t)
    return cur

def min_residual(E, n, c=0.5, nsamp=400, seed=0):
    """min over sampled X (|X|>=cn) of (|H[X]|+|crossing(1,2)|)/n^2; always include B_rec top-X."""
    rng = random.Random(seed)
    best = (1e18, None)
    Eset = set(E)
    cands = []
    # include structured candidates: top blocks
    E0, depth, blocks = build_brec(n)
    cands.append(set(blocks[0]))
    for _ in range(nsamp):
        X = set(v for v in range(n) if rng.random() < 0.6)
        if len(X) < c*n: continue
        cands.append(X)
    for X in cands:
        Y = set(range(n)) - X
        r = 0
        for t in Eset:
            s = sum(1 for v in t if v in X)
            if s == 3 or s == 1:
                r += 1
        if r < best[0]: best = (r, sorted(X))
    return best[0]/n**2, best[1]

for n in [12, 16, 20]:
    E0, depth, blocks = build_brec(n)
    V1 = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(V1))
    x0 = V1[0]
    W = sorted(v for v in V2 if depth[v] == 1)
    star = {tuple(sorted((x0, W[i], W[j]))) for i in range(len(W)) for j in range(i+1, len(W))} - E0
    EF = E0 | star
    print(f"n={n} brec={len(E0)} +star={len(star)}", flush=True)
    for tag, E in [("B_rec", E0), ("B_rec+Wstar", EF)]:
        k, X = min_residual(E, n, nsamp=300, seed=n)
        print(f"  {tag}: min-residual/n^2={k:.4f} |X|={len(X)}", flush=True)
    G = greedy_random(E0, n, seed=n)
    k, X = min_residual(G, n, nsamp=300, seed=n+1)
    print(f"  greedy |E|={len(G)}: min-residual/n^2={k:.4f} |X|={len(X)}", flush=True)

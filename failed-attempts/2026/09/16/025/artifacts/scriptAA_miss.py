"""Script AA: miss-control probe. For C7-free H, choose X maximizing B-mass |H cap B(X,Y)|.
Measure (miss, nonB-split, |X|/n) for: B_rec, B_rec+Wstar, exact-greedy maximal, and
'perturbed' graphs (B_rec minus random p of B-edges + greedy refill): does the maximizing
X stay linear with small residual? n=10..14 (exact detector affordable at n<=12)."""
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
B, CH = brec_dp(60)

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

def best_partition_profile(E, n):
    Es = set(E); best = None
    for mask in range(1 << (n-1)):
        X = {0} | {i+1 for i in range(n-1) if mask & (1 << i)}
        Y = set(range(n)) - X
        Xs = sorted(X)
        Bm = sum(1 for i in range(len(Xs)) for j in range(i+1, len(Xs)) for w in Y
                 if tuple(sorted((Xs[i], Xs[j], w))) in Es)
        if best is None or Bm > best[0]:
            # residual split
            hX = sum(1 for t in Es if all(v in X for v in t))
            c12 = sum(1 for t in Es if sum(1 for v in t if v in X) == 1)
            hY = sum(1 for t in Es if sum(1 for v in t if v in X) == 0)
            Bsz = len(Xs)*(len(Xs)-1)//2*len(Y)
            best = (Bm, len(X), Bsz - Bm, hX, c12, hY, sorted(X))
    return best

n = 10
E0, depth, blocks = build_brec(n)
V1 = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(V1))
x0 = V1[0]
W = sorted(v for v in V2 if depth[v] == 1)
star = {tuple(sorted((x0, W[i], W[j]))) for i in range(len(W)) for j in range(i+1, len(W))} - E0
tests = [("B_rec", E0), ("B_rec+Wstar", E0 | star)]
# exact greedy maximal
all3 = [t for t in itertools.combinations(range(n), 3) if t not in E0]
rng = random.Random(5); rng.shuffle(all3)
G = set(E0)
for t in all3:
    G.add(t)
    if has_C7(G, n): G.discard(t)
tests.append(("greedy-max", G))
for tag, E in tests:
    Bm, a, miss, hX, c12, hY, X = best_partition_profile(E, n)
    print(f"{tag}: |E|={len(E)} bestX={X} a/n={a/n:.2f} Bmass={Bm} miss={miss} H[X]={hX} cross12={c12} H[Y]={hY}", flush=True)

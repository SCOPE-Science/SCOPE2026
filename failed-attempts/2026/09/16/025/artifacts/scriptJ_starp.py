"""Script J: single-vertex star S(x0) = B_rec + all {x0,w1,w2} (w1,w2 in V2).
Scale test n=15..45: is S(x0) C7-free? Count extras=C(|V2|,2)=Theta(n^2) if yes.
If yes at scale -> sharpness HALF (Omega(n^2) lower construction). Characterize threshold."""
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

def make_link(E):
    from collections import defaultdict
    L = defaultdict(set)
    for (x, y, z) in E:
        L[(x, y)].add(z); L[(x, z)].add(y); L[(y, x)].add(z)
        L[(y, z)].add(x); L[(z, x)].add(y); L[(z, y)].add(x)
    return L

def has_C7(E, n, cap=1, seed_first=True):
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

def heuristic(E, n, trials=60000, seed=0):
    rng = random.Random(seed)
    for _ in range(trials):
        S = rng.sample(range(n), 7); rng.shuffle(S)
        if all(tuple(sorted((S[i], S[(i+1)%7], S[(i+2)%7]))) in E for i in range(7)):
            return tuple(S)
    return None

for n in [12, 15, 18, 22, 26, 30, 36, 45]:
    E0, depth, blocks = build_brec(n)
    V1 = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(V1))
    x0 = V1[0]
    star = set()
    for i in range(len(V2)):
        for j in range(i+1, len(V2)):
            star.add(tuple(sorted((x0, V2[i], V2[j]))))
    star = {t for t in star if t not in E0}
    E1 = E0 | star
    r_fast = heuristic(E1, n, trials=120000, seed=n)
    print(f"n={n} |V1|={len(V1)} |V2|={len(V2)} brec={len(E0)} +star={len(star)} heur-C7={r_fast}", flush=True)

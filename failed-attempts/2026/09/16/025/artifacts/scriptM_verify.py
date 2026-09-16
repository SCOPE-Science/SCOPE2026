"""Script M: verify W=V2-top-block star family EXACTLY (backtracking, no heuristic doubt)
at n=18,26 + confirm counts scale as Theta(n^2): |W|~c*n? Also verify the added edges
are genuinely new (not already in B) and count total surplus fraction."""
import sys
sys.setrecursionlimit(10000)
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
B, CH = brec_dp(200)

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

def has_C7_exact(E, n, cap=1):
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

for n in [12, 15, 18, 22, 26]:
    E0, depth, blocks = build_brec(n)
    V1 = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(V1))
    x0 = V1[0]
    W = sorted(v for v in V2 if depth[v] == 1)
    star = set()
    for i in range(len(W)):
        for j in range(i+1, len(W)):
            t = tuple(sorted((x0, W[i], W[j])))
            if t not in E0: star.add(t)
    E1 = E0 | star
    print(f"n={n} |V1|={len(V1)} |V2|={len(V2)} |W|={len(W)} brec={len(E0)} +star={len(star)}", flush=True)
    r = has_C7_exact(E1, n)
    print(f"   EXACT C7: {r if r else None}", flush=True)

print("scaling |W|/n:", flush=True)
for n in [30, 50, 80, 120, 200]:
    E0, depth, blocks = build_brec(n)
    V2 = sorted(set(range(n)) - set(blocks[0]))
    W = [v for v in V2 if depth[v] == 1]
    print(f"  n={n} |V2|={len(V2)} |W|={len(W)} |W|/n={len(W)/n:.3f} C(|W|,2)/n^2={comb(len(W),2)/n**2:.4f}", flush=True)

"""Script V: exact link-lemma check. If H[X] (triples inside X) has max degree Delta,
then... Actually the cleanest theoretical path: H[X] must be 'locally sparse' because
a dense H[X] + B-structure creates C7. Direct probe: for greedy C7-free G at n=12..16,
compute H[X] max pair-degree and total |H[X]|; test whether |H[X]| = O(n^2) with small
constant, and crossing(1,2) similarly. Use EXACT C7 detector (backtracking) for n<=12
to make greedy truly C7-free; for n>12 use strong heuristic."""
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

n = 12
E0, depth, blocks = build_brec(n)
X0 = set(blocks[0])
all3 = [t for t in itertools.combinations(range(n), 3) if t not in E0]
rng = random.Random(11)
rng.shuffle(all3)
G = set(E0)
for t in all3:
    G.add(t)
    if has_C7_exact(G, n, cap=1):
        G.discard(t)
print(f"n={n} exact-greedy C7-free |G|={len(G)} brec={len(E0)} gap={len(G)-len(E0)}", flush=True)
# residual decomposition at X0
HX = [t for t in G if all(v in X0 for v in t)]
C12 = [t for t in G if sum(1 for v in t if v in X0) == 1]
HY = [t for t in G if sum(1 for v in t if v in X0) == 0]
BB = [t for t in G if sum(1 for v in t if v in X0) == 2]
print(f"|H[X]|={len(HX)} |cross12|={len(C12)} |H[Y]|={len(HY)} |B-part|={len(BB)} n^2={n*n}", flush=True)
print("H[X]:", sorted(HX), flush=True)
print("cross12:", sorted(C12), flush=True)
# pair-degree profile of H[X]
pd = defaultdict(int)
for (x, y, z) in HX:
    for pr in [(x, y), (x, z), (y, z)]:
        pd[tuple(sorted(pr))] += 1
print("H[X] pair-degrees:", dict(pd), flush=True)

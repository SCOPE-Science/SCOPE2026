"""Script Y: crossing-number bound probe.
For C7-free H with full B-part on (X,Y): crossing triples T={x,w1,w2} (x in X, w's in Y).
Fix x; consider graph G_x on Y with edges {w1,w2}: {x,w1,w2} in H. What does C7-free imply
for G_x? Probe: B_rec+Wstar extremal: G_x0 = complete graph on W (clique!), empty elsewhere.
So G_x CAN be a clique on W (~0.235n). Union over x: total crossing <= sum_x C(d_x...)...?
If each G_x is a disjoint-clique-type (cluster graph), total = O(n^2)? Test structure of
G_x in greedy C7-free graphs: is G_x always a 'cluster' (disjoint union of cliques)?
Also test: what FORBIDDEN pattern in G_x creates C7? Try adding to G_x0 an edge from W to
D (deep): does C7 appear? I.e. is 'clique-on-W + nothing else' maximal?"""
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

n = 18
E0, depth, blocks = build_brec(n)
X = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(X))
x0 = X[0]
W = sorted(v for v in V2 if depth[v] == 1)
D = sorted(v for v in V2 if depth[v] > 1)
star = {tuple(sorted((x0, W[i], W[j]))) for i in range(len(W)) for j in range(i+1, len(W))} - E0
EF = E0 | star
print(f"W={W} D={D}", flush=True)
print("Wstar C7:", has_C7(EF, n), flush=True)
# probe: add W-D edges one by one: which create C7?
print("adding {x0,w,d} (w in W, d in D):", flush=True)
for w in W[:2]:
    for d in D:
        t = tuple(sorted((x0, w, d)))
        r = has_C7(EF | {t}, n)
        print(f"  {t}: C7={r[0] if r else None}", flush=True)
# probe: add D-D edge
if len(D) >= 2:
    t = tuple(sorted((x0, D[0], D[1])))
    r = has_C7(EF | {t}, n)
    print(f"  D-D {t}: C7={r[0] if r else None}", flush=True)
# probe: second center x1: clique on W at x1 too?
x1 = X[1]
star2 = {tuple(sorted((x1, W[i], W[j]))) for i in range(len(W)) for j in range(i+1, len(W))} - EF
E2 = EF | star2
print(f"two-center (+{len(star2)}): C7={has_C7(E2, n)}", flush=True)

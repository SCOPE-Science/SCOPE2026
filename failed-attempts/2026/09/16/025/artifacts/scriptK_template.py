"""Script K: analyze the failing C7 template for star S(x0).
Claim pattern: (0,15,18,20,16,17,19): windows? Determine which windows use star edges.
Goal: find a SPARSE sub-star (e.g. star over an independent/tested subset of V2, or
bounded-degree pairs) that stays C7-free with Theta(n^2) edges — e.g. take all pairs
within a C7-free-selected subset W of V2? But pairs inside V2 interact with H[V2]=B_rec:
need pairs {w1,w2} whose link structure avoids closing a C7 with x0."""
import sys, itertools
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

def all_C7(E, n, cap=200):
    L = make_link(E); found = []
    import sys
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
V1 = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(V1))
x0 = V1[0]
star = set()
for i in range(len(V2)):
    for j in range(i+1, len(V2)):
        t = tuple(sorted((x0, V2[i], V2[j])))
        if t not in E0: star.add(t)
E1 = E0 | star
cycs = all_C7(E1, n, cap=40)
print(f"n={n} star cycles found: {len(cycs)}")
for c in cycs[:8]:
    wins = [tuple(sorted((c[i], c[(i+1)%7], c[(i+2)%7]))) for i in range(7)]
    marks = ['S' if (w in star) else ('B' if w in E0 else '?') for w in wins]
    print("  ", c, marks)
# which star-pairs appear in C7s?
from collections import Counter
pc = Counter()
for c in cycs:
    for i in range(7):
        w = tuple(sorted((c[i], c[(i+1)%7], c[(i+2)%7])))
        if w in star:
            pr = tuple(sorted(set(w) - {x0}))
            pc[pr] += 1
print("star-pair usage:", dict(pc))
print("V2 =", V2, "depths:", {v: depth[v] for v in V2})

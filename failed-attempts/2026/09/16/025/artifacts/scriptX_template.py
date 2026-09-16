"""Script X: threshold refinement — even single triples always kill (census said 100%).
So H[X] inside top-X must be EMPTY in any C7-free superset of B_rec. The cover lemma's
H[X] part: for the STRUCTURAL partition, H[X]=0 exactly. Crossing (1,2) part: star analysis
says restricted. Remains: (a) prove single-extra rigidity in general (any triple in X
+ full B-part => C7): finite pattern? triple {a,b,c} in X: need C7 using it + B-edges.
Try to construct EXPLICIT C7 template: cycle (a,b,c,y1,y2,y3,y4)? windows: abc (extra),
bcy1, cy1y2, y1y2y3, y2y3y4, y3y4a, y4ab. Need y's making all B-edges. Since B pairs in X
link to all of V2: choose y1 in V2? window bcy1: {b,c,y1} with b,c in X: B-edge (pair in X,
third deeper). y1y2y3: need B-edge among y's: y1,y2 in W (V2-top) + y3 deeper: B. etc.
So explicit template exists when |V2| large enough to pick distinct y's with right depths.
(b) crossing triples {x,w1,w2}: also constrained; but W-star shows Theta(n^2) possible,
so crossing part contributes the SHARPNESS, consistent with O(n^2) (not o(n^2)).
Conclusion: upper bound = rigidity (H[X]=0 for good X) + crossing O(n^2) + induction.
Test (a) constructively: for triple {a,b,c} in X at n=12, find C7 with abc-window explicitly."""
import sys, itertools
from collections import defaultdict
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

n = 12
E0, depth, blocks = build_brec(n)
X = sorted(blocks[0]); V2 = sorted(set(range(n)) - set(X))
print("X =", X, "V2 =", V2, flush=True)
# explicit template attempt: (a,b,c, y1,y2,y3,y4) with y's from V2/W/deep
cyc = has_C7(E0 | {tuple(X[:3])}, n)[0]
print("C7 using triple X[:3]:", cyc, flush=True)
if cyc:
    E1 = E0 | {tuple(X[:3])}
    wins = [tuple(sorted((cyc[i], cyc[(i+1)%7], cyc[(i+2)%7]))) for i in range(7)]
    print("windows:", wins, flush=True)
    print("in-B0:", [w in E0 for w in wins], flush=True)
    print("depths:", [depth[v] for v in cyc], flush=True)

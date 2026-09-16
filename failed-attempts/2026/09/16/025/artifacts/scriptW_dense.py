"""Script W: prove the cover lemma's core — H[X] classification.
Conjecture (Single-extra rigidity): adding ANY single triple inside top V1^(0) of B_rec
creates a C7 (verified n=8..12 census: 100%). If H[X]=B-part+C7-free extras with X=V1^(0):
H[X] must be EMPTY... but wait script F showed greedy extras of type inV1=1 (crossing),
and H[X] (3 in X) stays 0. So the REAL lemma: H[X] is EMPTY for the natural partition?
No — H[X] empty only if X is exactly a B_rec top block AND H contains full B-part.
General cover lemma must CONSTRUCT X. Practical approach used in literature (stability):
choose X to MAXIMIZE B-part (minimize miss+nonB jointly)? For the upper bound we only
need existence with residual O(n^2).
Alternative pragmatic route: pick X = argmax over sets of [B-edges present - penalty]?
Try MAX-CUT-like: X maximizing |H cap B(X,Y)| (B-mass captured). Then residual = e(H) -
Bmass; compare with brec: e(H) = Bmass + resid <= C(a,2)b + resid. Same as before.
The theoretical question remains: prove resid = O(n^2) for the maximizing X.
Structural insight attempt: suppose |H[X]| = omega(n^2), i.e. positive density inside X.
Then H[X] contains (by supersaturation / Kőnig-type) a tight path on 4 vertices?
A tight 3-path P4 (verts v1..v5? no: tight path with 3 edges: v1..v5, edges v123,v234,v345)?
Then combined with B-links to Y (dense pairs in X link to most of Y?) closes a C7?
Formalize minimal version: if {p,q,r} in H[X] and pair {p,q} has large common B-neighborhood
in Y (i.e. many w with {p,q,w} in H), then C7 arises? Test computationally: in B_rec+extras,
measure pair codegrees.
Simpler decisive experiment: random 3-graphs with positive density inside X + full B-part:
do they ALWAYS contain C7 at moderate n? If yes with threshold well below extremal density,
cover lemma plausible via 'dense H[X] forces C7'. Test: X size 8, add random p-fraction of
C(8,3) triples inside X to B_rec(12); measure C7 rate vs p."""
import random, sys, itertools
from math import comb
sys.setrecursionlimit(10000)
from collections import defaultdict

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
X = sorted(blocks[0])
inside = [t for t in itertools.combinations(X, 3)]
print(f"n={n} |X|={len(X)} C(|X|,3)={len(inside)}", flush=True)
for p in [0.05, 0.1, 0.2, 0.3, 0.5]:
    hits = 0; T = 12
    for t in range(T):
        rng = random.Random(1000 + int(p*100) + t)
        add = {e for e in inside if rng.random() < p}
        E1 = E0 | add
        if has_C7(E1, n): hits += 1
    print(f"  p={p}: C7 rate {hits}/{T}", flush=True)

"""Script E2: fast backtracking C7 detector; single-extra safety census; greedy max augmentation."""
import random, itertools, sys
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

def make_link(E, n):
    from collections import defaultdict
    L = defaultdict(set)
    for (x, y, z) in E:
        L[(x, y)].add(z); L[(x, z)].add(y); L[(y, x)].add(z)
        L[(y, z)].add(x); L[(z, x)].add(y); L[(z, y)].add(x)
    return L

def has_C7_bt(E, n, cap=1, seed=0):
    L = make_link(E, n)
    found = []
    # order starts v0<v? break symmetry: fix v0 = min of cycle? Simple: try all v0,v1, backtrack
    sys.setrecursionlimit(10000)
    def bt(path, used):
        if found and len(found) >= cap: return True
        k = len(path)
        if k == 7:
            # check closing windows: (v5,v6,v0),(v6,v0,v1) in E
            a, b, c = path[5], path[6], path[0]
            if tuple(sorted((a, b, c))) not in E: return False
            a, b, c = path[6], path[0], path[1]
            if tuple(sorted((a, b, c))) not in E: return False
            found.append(tuple(path)); return True
        if k <= 1:
            cands = range(n) if k == 0 else [v for v in range(n) if v not in used]
            for v in cands:
                if k == 0 and v > n - 1: break
                path.append(v); used.add(v)
                if bt(path, used) and len(found) >= cap:
                    return True
                path.pop(); used.discard(v)
            return False
        # k>=2: next vertex must be in L(path[-2],path[-1])
        for v in L.get((path[-2], path[-1]), ()):
            if v in used: continue
            # prune: for k>=2 also window (path[-1],v,?) unknown yet; but check triple present by construction
            path.append(v); used.add(v)
            if bt(path, used) and len(found) >= cap:
                return True
            path.pop(); used.discard(v)
        return False
    # fix v0 over all n but break rotation: fine for small n
    for v0 in range(n):
        if bt([v0], {v0}) and len(found) >= cap: break
    return found

# validate detector on known cases
E, depth, blocks = build_brec(7)
print("n=7 B_rec C7:", has_C7_bt(E, 7), flush=True)
V1 = sorted(blocks[0]); x = V1[0]; rest = [v for v in V1 if v != x]
add = set()
for i in range(len(rest)):
    for j in range(i+1, len(rest)):
        add.add(tuple(sorted((x, rest[i], rest[j]))))
print("n=7 B_rec+star C7:", has_C7_bt(E | add, 7), flush=True)

print("== E1: single extra triple inside top V1 ==", flush=True)
for n in [8, 9, 10, 12]:
    E, depth, blocks = build_brec(n)
    V1 = sorted(blocks[0])
    total = 0; bad = 0; good = []
    for t in itertools.combinations(V1, 3):
        total += 1
        r = has_C7_bt(E | {t}, n, cap=1)
        if r: bad += 1
        else: good.append(t)
    print(f"n={n} |V1|={len(V1)} triples={total} bad={bad} safe={len(good)} e.g.{good[:3]}", flush=True)

print("== E3: greedy maximal augmentation n<=8 ==", flush=True)
for n in range(5, 9):
    E, depth, blocks = build_brec(n)
    all3 = [t for t in itertools.combinations(range(n), 3) if t not in E]
    rng = random.Random(7)
    bestsize = len(E)
    trials = 200 if n <= 7 else 40
    for _ in range(trials):
        rng.shuffle(all3)
        cur = set(E)
        for t in all3:
            cur.add(t)
            if has_C7_bt(cur, n, cap=1):
                cur.discard(t)
        bestsize = max(bestsize, len(cur))
    print(f"n={n} brec={len(E)} C(n,3)={comb(n,3)} greedy-max={bestsize} gap={bestsize-len(E)}", flush=True)

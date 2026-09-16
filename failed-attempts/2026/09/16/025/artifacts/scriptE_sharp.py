"""Script E: sharpness hunt v2 — random sparse extras inside top V1 + extras in deep V2-core.
Also: exact small-n brute force upper bounds (ex(n,C7) vs brec) for n<=8 via ILP-free
branching? Instead: greedy + random C7-free augmentation to estimate ex-brec gap."""
import random, itertools
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

def find_C7cap(E, verts, cap=1):
    """Search C7 over ordered 7-tuples from verts (verts small) or heuristic if large."""
    found = []
    if len(verts) <= 10:
        for tup in itertools.permutations(verts, 7):
            if all(tuple(sorted((tup[i], tup[(i+1)%7], tup[(i+2)%7]))) in E for i in range(7)):
                found.append(tup)
                if len(found) >= cap: break
    else:
        rng = random.Random(42)
        for _ in range(200000):
            S = rng.sample(verts, 7); rng.shuffle(S)
            if all(tuple(sorted((S[i], S[(i+1)%7], S[(i+2)%7]))) in E for i in range(7)):
                found.append(tuple(S))
                if len(found) >= cap: break
    return found

print("== E1: single extra triple inside top V1 — how many create a C7? ==")
for n in [8, 9, 10, 12, 15]:
    E, depth, blocks = build_brec(n)
    V1 = blocks[0]
    total = 0; bad = 0; good_ex = []
    for t in itertools.combinations(sorted(V1), 3):
        total += 1
        E2 = E | {t}
        cyc = find_C7cap(E2, list(range(n)), cap=1)
        if cyc: bad += 1
        else: good_ex.append(t)
    print(f"n={n} |V1|={len(V1)} triples={total} creating-C7={bad} safe={len(good_ex)} e.g.{good_ex[:3]}")

print("== E2: pairs of extra triples inside top V1 (n=8): max safe set size? ==")
n = 8
E, depth, blocks = build_brec(n)
V1 = sorted(blocks[0])
cands = list(itertools.combinations(V1, 3))
rng = random.Random(1)
best = []
for _ in range(4000):
    rng.shuffle(cands)
    cur = set()
    for t in cands:
        E2 = E | cur | {t}
        if not find_C7cap(E2, list(range(n)), cap=1):
            cur.add(t)
    if len(cur) > len(best): best = list(cur)
print(f"n=8 greedy max safe extras inside V1: {len(best)} of {len(cands)} : {best}")

print("== E3: exact small-n ex(n,C7) upper estimate via greedy maximal augmentation (n<=8) ==")
for n in range(5, 9):
    E, depth, blocks = build_brec(n)
    all3 = [t for t in itertools.combinations(range(n), 3) if t not in E]
    rng = random.Random(7)
    bestsize = len(E)
    for _ in range(3000):
        rng.shuffle(all3)
        cur = set(E)
        for t in all3:
            cur.add(t)
            if find_C7cap(cur, list(range(n)), cap=1):
                cur.discard(t)
        bestsize = max(bestsize, len(cur))
    print(f"n={n} brec={len(E)} C(n,3)={comb(n,3)} greedy-max-C7free={bestsize} gap={bestsize-len(E)}")

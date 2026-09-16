"""Script D: structural test of C7's in B_rec itself and link-graph intuition.
Q1: is B_rec C_7-free at larger n (random-order heuristic search for C7)?
Q2: what does the C7 template (0,1,2,*,3,4,*) tell us? Try to PROVE B_rec is C7-free
    via depth-profile; and find minimal C7-free-violating additions."""
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

B, CH = brec_dp(100)

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
    return edges, depth

def edge_present(E, x, y, z):
    return tuple(sorted((x, y, z))) in E

def heuristic_C7_search(E, n, trials=60000, seed=0):
    """Random-permutation + local window check; also random 7-sets with random orders."""
    rng = random.Random(seed)
    verts = list(range(n))
    for _ in range(trials):
        S = rng.sample(verts, 7)
        rng.shuffle(S)
        ok = True
        for i in range(7):
            if tuple(sorted((S[i], S[(i+1)%7], S[(i+2)%7]))) not in E:
                ok = False; break
        if ok: return tuple(S)
    return None

for n in [15, 25, 40, 60]:
    E, depth = build_brec(n)
    assert len(E) == B[n], (n, len(E), B[n])
    cyc = heuristic_C7_search(E, n, trials=80000, seed=n)
    print(f"n={n} |E|={len(E)} heuristic C7: {cyc}")

print()
print("== depth-profile analysis of a C7 in B_rec ==")
print("Edge rule: {x,y,z} in B iff min-depth pair shares depth d<max depth vertex,")
print("i.e. exactly two vertices in same block V1^(d), third strictly deeper.")
print("Question: can 7 cyclic windows each have exactly-2-in-same-block?")
print("Window-sum computation (script A): the ONLY {0,2}-word is 0^7.")
print("So along ANY single block indicator, a C7 would need all-0: all 7 outside block.")
print("Levels nest: block membership at depth 0,1,2,... Each level needs all-7-outside??")

def check_allzero_impossibility():
    # If every window must avoid sum-1 (claim: sum-1 impossible in B) then:
    # indicator of V1^(0): sum in {0,2,3}, sum-3 impossible inside V1 (empty), so {0,2}.
    # Only 0^7 survives => C subset of V2. Recurse: C subset of V2^(1) subset ... infinite descent.
    # The crux: is window-sum-1 REALLY absent in B_rec? Check by brute force on small B_rec.
    for n in [8, 9, 10, 12]:
        E, depth = build_brec(n)
        blocks = {}
        for v, d in depth.items(): blocks.setdefault(d, []).append(v)
        V1 = set(blocks[0])
        # enumerate all triples, classify indicator sums
        from collections import Counter
        c = Counter()
        for t in itertools.combinations(range(n), 3):
            s = sum(1 for v in t if v in V1)
            present = t in E
            c[(s, present)] += 1
        print(f"n={n} (sum_in_V1, present)->count: {dict(c)}")
check_allzero_impossibility()

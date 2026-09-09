"""Lane-403 attack v7: correct finite-level orbit-density test (target phase).

For candidate phi (given by coherent patterns sig3 on 8 atoms, sig2 on 4):
  Reach(P2) = { level-2 pattern tau of g.phi.g^{-1} : g in S_8 (all 40320),
                defined only when the conjugate preserves mod-4 blocks }.
Density-in-M shadow at level 2: Reach(P2) should = all single 4-cycles (6).
Also level-3 reach with g sampled from S_16? (too big: sample 20000 random
level-4 perms, record level-3 patterns preserving mod-8 blocks).

Candidates:
  B = pure binary odometer.
  T = twisted universal-type at 2-6 tower? (levels incompatible with 8-atom
      g; test separately at 6 atoms with g in S_6=720: reach on mod-2 blocks
      and on 3-class partition a%3.)
"""
import json, os, random, itertools

ART = os.path.dirname(os.path.abspath(__file__))
random.seed(40307)
res = {}

def compose(p, q):
    return [p[q[i]] for i in range(len(q))]

def odo(N):
    return [(a + 1) % N for a in range(N)]

def single(p):
    n = len(p)
    seen = [False] * n
    x, c = 0, 0
    while not seen[x]:
        seen[x] = True
        x = p[x]
        c += 1
    return c == n

def invert(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return q

def conj(g, s):
    return compose(compose(g, s), invert(g))

def pattern_on_blocks(psi, N, M):
    """level-2 pattern of atom-perm psi: blocks a%M; None if not preserving."""
    t = []
    for b in range(M):
        imgs = {psi[a] % M for a in range(N) if a % M == b}
        if len(imgs) != 1:
            return None
        t.append(next(iter(imgs)))
    return tuple(t)

# ---- binary odometer, full S_8 ----
sig3 = odo(8)
sig2 = odo(4)
reach2 = set()
n_pres = 0
for g in itertools.permutations(range(8)):
    gl = list(g)
    psi = conj(gl, sig3)
    t = pattern_on_blocks(psi, 8, 4)
    if t is not None:
        n_pres += 1
        reach2.add(t)
four_cycles = [t for t in itertools.permutations(range(4)) if single(list(t))]
res["binary_level2"] = {
    "g_count": 40320,
    "n_preserving_P2": n_pres,
    "reach": sorted(list(reach2)),
    "n_reach": len(reach2),
    "all_4cycles": len(four_cycles),
    "hits_all_4cycles": set(reach2) == set(tuple(t) for t in four_cycles),
}

# ---- binary odometer, sampled S_16 -> level-3 patterns ----
sig4 = odo(16)
reach3 = set()
n3 = 0
Gs = set()
while len(Gs) < 20000:
    g = list(range(16))
    random.shuffle(g)
    Gs.add(tuple(g))
for g in Gs:
    psi = conj(list(g), sig4)
    t = pattern_on_blocks(psi, 16, 8)
    if t is not None:
        n3 += 1
        reach3.add(t)
res["binary_level3_sampled"] = {
    "g_sampled": len(Gs),
    "n_preserving_P3": n3,
    "n_distinct_patterns": len(reach3),
    "all_single_8cycles": all(single(list(t)) for t in reach3),
    "n_possible_8cycles": 5040,
}

# ---- universal-type twist (2-6 tower), full S_6 ----
h6 = [0, 3, 2, 5, 4, 1]  # parity-preserving, single (from v3 search)
su = compose(h6, odo(6))
reach_mod2 = set()
reach_mod3 = set()
for g in itertools.permutations(range(6)):
    psi = conj(list(g), su)
    t2 = pattern_on_blocks(psi, 6, 2)
    t3 = pattern_on_blocks(psi, 6, 3)
    if t2 is not None:
        reach_mod2.add(t2)
    if t3 is not None:
        reach_mod3.add(t3)
res["twist_level"] = {
    "h6": h6,
    "su_single": single(su),
    "reach_mod2": sorted(list(reach_mod2)),
    "reach_mod3": sorted(list(reach_mod3)),
    "n_mod3": len(reach_mod3),
    "3cycles_possible": [[1, 2, 0], [2, 0, 1]],
    "hits_a_3cycle": any(list(t) in ([1, 2, 0], [2, 0, 1]) for t in reach_mod3),
}

with open(os.path.join(ART, "finite_level_log7.json"), "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))

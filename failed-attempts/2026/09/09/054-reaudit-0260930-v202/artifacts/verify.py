"""Verifier for emergent finding: positive-density window for ex_lin(n,F+).

Checks (stdlib only):
  1. Fano triples form an STS(7) (each of C(7,2) pairs in exactly one triple).
  2. F+ certificate: 7 quads on 14 vertices, linear, pairwise meet exactly once.
  3. Detectors calibrated: find_Fplus(F+) finds witness; count_Fplus(F+) == 1.
  4. Conflict-pair lemma: exact N_conf(n) <= n^6/16 for n = 7..12 (exhaustive).
  5. Constant optimizer identity: a/24 - a^2/16 = 1/144 - (a-1/3)^2/16 (Fraction).
  6. Seeded alteration demo (n=60): greedy sample + repair -> linear, F+-free,
     edges >= n^2/144 - n/12 - 1 (best of seeds, attempts logged).
"""
import itertools
import random
import sys
from fractions import Fraction

sys.path.insert(0, ".")
from fano import fano_triples, build_Fplus, is_linear, find_Fplus
from fcount import count_Fplus

FAILS = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (" | " + str(detail) if detail else ""))
    if not cond:
        FAILS.append(name)


# 1. STS(7)
T = fano_triples()
paircov = {}
for t in T:
    for p in itertools.combinations(sorted(t), 2):
        paircov[p] = paircov.get(p, 0) + 1
check("sts7_ntriples", len(T) == 7, len(T))
check("sts7_pairs", len(paircov) == 21 and set(paircov.values()) == {1},
      (len(paircov), sorted(set(paircov.values()))))

# 2. F+ certificate
F = build_Fplus()
E = [frozenset(e) for e in F]
verts = set().union(*E)
check("Fplus_nedges", len(F) == 7, len(F))
check("Fplus_nverts", len(verts) == 14, len(verts))
check("Fplus_linear", is_linear(F))
ok1 = all(len(E[i] & E[j]) == 1 for i in range(7) for j in range(i + 1, 7))
check("Fplus_pairwise_meet_1", ok1)

# 3. detector calibration
w = find_Fplus(F)
check("detect_planted", w is not None, w)
check("count_planted", count_Fplus(F) == 1, count_Fplus(F))

# 4. conflict-pair lemma: exact N_conf(n) <= n^6/16
for n in range(7, 13):
    quads = list(itertools.combinations(range(n), 4))
    nc = 0
    for i in range(len(quads)):
        si = set(quads[i])
        for j in range(i + 1, len(quads)):
            if len(si & set(quads[j])) >= 2:
                nc += 1
    bound = n ** 6 / 16.0
    check(f"conflict_bound_n{n}", nc <= bound, f"exact={nc} bound={bound:.1f}")

# 5. optimizer identity (exact rational): a/24-a^2/16 == 1/144-(a-1/3)^2/16
for astr in ["1/3", "1/4", "1/2", "1/6"]:
    a = Fraction(astr)
    lhs = a / 24 - a * a / 16
    rhs = Fraction(1, 144) - (a - Fraction(1, 3)) ** 2 / 16
    check(f"optimizer_a={astr}", lhs == rhs, f"{lhs} vs {rhs}")
a = Fraction(1, 3)
check("optimizer_value", a / 24 - a * a / 16 == Fraction(1, 144))


# 6. seeded alteration demo, n=60
def alteration_demo(n, seed):
    rng = random.Random(seed)
    p = 1.0 / (3 * n * n)
    quads = list(itertools.combinations(range(n), 4))
    G = [q for q in quads if rng.random() < p]
    # repair pair conflicts: drop one edge per conflicting pair (greedy by index)
    Gus = [set(q) for q in G]
    dead = set()
    seen = {}
    for i, s in enumerate(Gus):
        for pr in itertools.combinations(sorted(s), 2):
            if pr in seen:
                dead.add(i)  # drop later-index edge
            else:
                seen[pr] = i
    # F+ repair: while a witness exists, drop its last edge
    live = [i for i in range(len(G)) if i not in dead]
    while True:
        sub = [G[i] for i in live]
        wit = find_Fplus(sub)
        if wit is None:
            break
        drop_pos = wit[-1]
        live = [x for k, x in enumerate(live) if k != drop_pos]
    return [G[i] for i in live]


n = 60
floor = n * n / 144.0 - n / 12.0 - 1.0
best = None
tried = 0
for seed in range(40):
    tried += 1
    H = alteration_demo(n, 1000 + seed)
    if best is None or len(H) > len(best):
        best = H
    if len(H) >= floor and is_linear(H) and find_Fplus(H) is None:
        break
check("demo_linear", is_linear(best))
check("demo_Fplus_free", find_Fplus(best) is None)
check("demo_density_floor", len(best) >= floor,
      f"edges={len(best)} floor={floor:.2f} seeds_tried={tried}")
print(f"demo: n={n} edges={len(best)} density={len(best)/n/n:.5f} (1/144={1/144:.5f})")

print("RESULT:", "VERIFY_OK" if not FAILS else f"VERIFY_FAIL {FAILS}")
sys.exit(0 if not FAILS else 1)

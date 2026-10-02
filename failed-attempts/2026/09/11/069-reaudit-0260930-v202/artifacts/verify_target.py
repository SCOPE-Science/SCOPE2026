"""Verify TARGET: tropical independence of explicit triple on mixed-torsion genus-5 chain.

Model:
  Spine x in [0,40]; vertices v_k at x=8k (k=0..5); bridges B_k=[8(k-1),8k], length 8.
  Loop Lambda_k attached at v_k (k=1..5), lengths (1,2,5,7,11) [torsion profile 2,5,7,11 on loops 2..5].
  D = 2(v1)+2(v3)+2(v5).
  Functions: constant on all loops; left-to-right segment slopes on spine nodes
  [v0=0, v1=8, v2=16, m=20, v3=24, v4=32, v5=40] (m = midpoint kink of bridge B3):
    psi0: [0, 0, 0, 2, 1, 1], psi1: [0, 1, 1, 1, 1, 1], psi2: [0, 2, 2, 2, 2, 2];
  psi_i(v0)=0. Bridge-B2 slopes are (0,1,2). Midpoint kink (psi0, valley 0->2,
  ord +2) is the unique interior bend compatible with tight R(D) bounds.
Convention (Baker-Norine): ord_p(f) = sum of OUTGOING slopes; f in R(D) iff D + div(f) >= 0.
  Interior spine vertex v_k: ord = s_k - s_{k-1} (right outgoing +s_k, left outgoing -s_{k-1}; loops 0).
  v0: ord = s_0. v5: ord = -s_4.
Checks:
  (1) R(D) membership of each psi (vertex ord table + effectiveness).
  (2) Distinct slopes (0,1,2) on bridge B2 -> independence theorem premise.
  (3) Numerical envelope sweep over constant grid + random triples: unique-min point on B2 always exists.
"""
import itertools
import random

# Segment nodes: [v0=0, v1=8, v2=16, m=20, v3=24, v4=32, v5=40]; m = midpoint kink on B3.
NODES = [0.0, 8.0, 16.0, 20.0, 24.0, 32.0, 40.0]
L = 8.0  # (kept) standard bridge length; B3 halves are length 4
D = {0: 0, 1: 2, 2: 0, 3: 2, 4: 0, 5: 2}
SLOPES = {
    "psi0": [0, 0, 0, 2, 1, 1],
    "psi1": [0, 1, 1, 1, 1, 1],
    "psi2": [0, 2, 2, 2, 2, 2],
}
NAMES = ["psi0", "psi1", "psi2"]
SEGLEN = [NODES[i + 1] - NODES[i] for i in range(6)]

def values(s):
    a = [0.0]
    for k in range(6):
        a.append(a[-1] + SEGLEN[k] * s[k])
    return a

def ord_at(s, k):
    """ord_{v_k}(psi) with outgoing-slope convention; loops contribute 0."""
    if k == 0:
        return s[0]
    if k == 5:
        return -s[5]
    seg = {1: (0, 1), 2: (1, 2), 3: (3, 4), 4: (4, 5)}[k]
    return s[seg[1]] - s[seg[0]]

def mid_ord(s):
    """ord at midpoint kink m of B3 = right slope - left slope = s3 - s2 (outgoing)."""
    return s[3] - s[2]

print("== vertex values ==")
for name in NAMES:
    print(f"  {name}: slopes={SLOPES[name]} values={values(SLOPES[name])}")

print("== R(D) membership (vertices + midpoint kink m of B3) ==")
membership_ok = True
for name in NAMES:
    s = SLOPES[name]
    parts = []
    for k in range(6):
        o = ord_at(s, k)
        eff = D[k] + o
        parts.append(f"v{k}:ord={o},D+div={eff}")
        if eff < 0:
            membership_ok = False
            print(f"  FAIL {name} at v{k}: ord={o}, D+div={eff}")
    mo = mid_ord(s)
    parts.append(f"m:ord={mo}")
    assert mo >= 0, f"{name}: midpoint kink requires ord>=0, got {mo}"
    print(f"  {name}: " + ", ".join(parts))
assert membership_ok, "R(D) membership failed"
print("  MEMBERSHIP_OK: all D+div effective; loops: psi constant => ord 0, D=0 there.")

print("== nondegeneracy: bends + distinct mod constants ==")
for name in NAMES:
    s = SLOPES[name]
    assert any(s[k] != s[k - 1] for k in range(1, 5)) or s[0] != 0, f"{name} constant"
print("  each psi has a genuine bend (slope change at a named vertex)")
assert len({tuple(s) for s in SLOPES.values()}) == 3
print("  DISTINCT_FUNCTIONS_OK (distinct slope vectors => distinct mod constants)")

print("== bridge-B2 slope pattern ==")
b2 = {n: SLOPES[n][1] for n in NAMES}
print(f"  slopes on B2: {b2}")
assert len(set(b2.values())) == 3, "slopes on B2 must be pairwise distinct"
print("  DISTINCT_SLOPES_OK (0,1,2)")

VALS = {n: values(SLOPES[n]) for n in NAMES}

def unique_min_exists(b, lo=8.0, hi=16.0):
    """Lines L_n(x)=VALS[n][1]+s_n*(x-8)+b[n] on B2; tie set finite => unique-min point exists."""
    s = {n: SLOPES[n][1] for n in NAMES}
    ties = set()
    for i in range(3):
        for j in range(i + 1, 3):
            ni, nj = NAMES[i], NAMES[j]
            denom = s[ni] - s[nj]
            t = ((VALS[nj][1] + b[nj]) - (VALS[ni][1] + b[ni])) / denom
            x = 8.0 + t
            if lo - 1e-12 <= x <= hi + 1e-12:
                ties.add(round(x, 12))
    srt = sorted(set([lo] + sorted(ties) + [hi]))
    cands = [lo + 1e-9, hi - 1e-9]
    for p, q in zip(srt[:-1], srt[1:]):
        if q - p > 1e-9:
            cands.append((p + q) / 2)
    def val(n, x):
        return VALS[n][1] + s[n] * (x - 8.0) + b[n]
    for x in cands:
        vs = sorted(val(n, x) for n in NAMES)
        if vs[0] < vs[1] - 1e-9:
            return True, x
    return False, None

print("== envelope sweep: grid b_i in {-40..40 step 4} (21^3=9261 triples) ==")
grid = list(range(-40, 41, 4))
n = 0
for b0 in grid:
    for b1 in grid:
        for b2 in grid:
            ok, _ = unique_min_exists({"psi0": b0, "psi1": b1, "psi2": b2})
            assert ok, f"no unique-min point for b={(b0, b1, b2)}"
            n += 1
print(f"  GRID_OK: {n} triples, unique minimizer on B2 in every case")

print("== envelope sweep: 20000 random float triples ==")
random.seed(984)
for _ in range(20000):
    b = {"psi0": random.uniform(-100, 100), "psi1": random.uniform(-100, 100),
         "psi2": random.uniform(-100, 100)}
    ok, _ = unique_min_exists(b)
    assert ok, f"no unique-min point for b={b}"
print("  RANDOM_OK: 20000 triples")

print("== longest guaranteed witness interval ==")
print("  B2 length 8 minus <=3 tie points => largest open unique-minimum piece has length >= 2.")
print("VERIFY_OK")

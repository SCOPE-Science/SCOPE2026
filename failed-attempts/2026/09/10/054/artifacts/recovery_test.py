"""Bounded recovery test for TARGET (lane-633).

Tests whether the GPS/Schramm-Steif product-noise + OSSS route can close for
FK q=2 at p_c with only citable constants:
 T1: p_c value check.
 T2: single-edge conditional dependence (FK weight q^{k(w)}) — if the two
     conditional values differ, independent per-edge noise resampling does not
     preserve the FK marginal and product revealment calculus is misspecified.
 T3: exact-enumeration scale check at 256x128 (config count) — infeasible.
 T4: RSW numeric floor present in citable sources? (existence-form only -> absent)
Overall: NEGATIVE (target window not closable from logged constants).
Stdlib only.
"""
import math, itertools

q = 2.0
pc = math.sqrt(2) / (1 + math.sqrt(2))
print(f"T1: p_c(2) = {pc:.15f}")
assert abs(pc - 0.5857864376269051) < 1e-12
print("T1 PASS (value reproduced)")

# T2: FK single-edge conditional on a 2-edge path graph (vertices 0-1-2),
# edges e1=(0,1), e2=(1,2). P(e2=1 | e1=1): endpoints 1,2 disconnected in
# rest={e1} unless... endpoints of e2 are 1,2; rest config {e1=1} does not
# connect 1-2, so conditional = p/(p+q(1-p)). If rest connected them it'd be p.
# General formula check with both values:
p = pc
cond_conn = p
cond_disconn = p / (p + q * (1 - p))
print(f"T2: P(e=1|rest connects endpoints) = {cond_conn:.6f}")
print(f"T2: P(e=1|rest disconnects)        = {cond_disconn:.6f}")
assert abs(cond_conn - cond_disconn) > 0.05, "expected genuine dependence"
# Exact joint check on triangle (single cycle): enumerate 8 configs,
# weight p^o (1-p)^c q^k. Edges e1=(0,1), e2=(1,2), e3=(0,2).
verts = [0, 1, 2]
edges = [(0, 1), (1, 2), (0, 2)]
Z = 0.0
probs = {}
for bits in itertools.product([0, 1], repeat=3):
    parent = list(range(3))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    o = sum(bits)
    for b, e in zip(bits, edges):
        if b:
            union(*e)
    k = len(set(find(v) for v in verts))
    w = (p ** o) * ((1 - p) ** (3 - o)) * (q ** k)
    probs[bits] = w
    Z += w
for bits in probs:
    probs[bits] /= Z
# P(e3=1 | e1=e2=1): endpoints 0,2 connected via path -> should equal p
pe3_both1 = probs[(1, 1, 1)] / (probs[(1, 1, 1)] + probs[(1, 1, 0)])
# P(e3=1 | e1=e2=0): endpoints disconnected -> should equal p/(p+q(1-p))
pe3_both0 = probs[(0, 0, 1)] / (probs[(0, 0, 1)] + probs[(0, 0, 0)])
print(f"T2 exact: P(e3=1|rest connects)={pe3_both1:.6f} (expect {cond_conn:.6f})")
print(f"T2 exact: P(e3=1|rest disconnects)={pe3_both0:.6f} (expect {cond_disconn:.6f})")
assert abs(pe3_both1 - cond_conn) < 1e-9 and abs(pe3_both0 - cond_disconn) < 1e-9
assert abs(pe3_both1 - pe3_both0) > 0.05, "dependence must show exactly"
print("T2 PASS (dependence confirmed; product-noise operator misspecified)")

# T3: enumeration scale at 256x128 free box: ~ (257*128 + 256*129) edges
E = 257 * 128 + 256 * 129
print(f"T3: box edges ~ {E}, configs = 2^{E} (log10 ~ {E * math.log10(2):.0f})")
assert E > 60000
print("T3 PASS (exact enumeration infeasible; MC not a rigorous lower bound)")

# T4: citable numeric RSW floor?
# Chelkak-DC-Hongler gives existence-form c(rho)>0, no 2:1 numeric floor.
print("T4: no citable explicit c_RSW(2:1) numeric floor in fused sources -> ABSENT")

print("RECOVERY_TEST_RESULT: NEGATIVE — no credible route closes Cov->0/BKS from logged constants")

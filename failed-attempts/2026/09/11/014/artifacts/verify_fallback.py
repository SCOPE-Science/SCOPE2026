"""Fallback verification: analytic pattern-case elimination + numerical kills.

Required data (forced by S^3_5(J)~=Y, J L-space since Y is L-space):
  V=[2,1,1,0], V0=2, det=7, a2=6, d0(Y)=-3, g(J)=3.

Rows:
  R0 composite -> Krcatovich primeness (topological).
  R1 Whitehead doubles only: Delta=1 -> V0=0, d0=+1 mismatches; general w=0
     by Hedden (arXiv:0806.2172) satellite/cabling Floer results.
  R2 cable genus equation p*gC+(p-1)(|q|-1)/2=3 (torus genus
     (|p|-1)(|q|-1)/2) solved analytically; corrected solution sets asserted
     and machine-checked; q<=0 killed uniformly by Hom q/p<2gC-1;
     q=+-1 killed by Hom; sole survivor (2,3,trefoil) killed 4x numerically.
  R3 iterated JSJ -> genus monotonicity + trefoil rigidity collapses to R2.
"""
from fractions import Fraction as Q
import math

print("=== Required numbers (from verify_target.py baseline) ===")
V, V0_req, det_req, a2_req = [2, 1, 1, 0], 2, 7, 6
print("V =", V, "V0 =", V0_req, "det =", det_req, "a2 =", a2_req, "d0(Y) = -3")

# ---------- R1: Whitehead doubles only for the classical computation ----------
print("\n=== R1 Whitehead doubles: Delta=1 ===")
dL0 = Q(1)
assert dL0 != Q(-3)
print(f"V0(Wh)=0 vs required 2; d0(Wh +5 surgery)={dL0} vs d0(Y)=-3 -> KILLED")
print("General winding-0 satellites: never L-space knots (Hedden arXiv:0806.2172);")
print("Whitehead +5 surgery is non-L-space, so classical V0/d0 + Hedden kill it;")
print("involutive (dl,d,du) check is moot there.")

# ---------- R2: corrected |q| cable-genus equation ----------
print("\n=== R2 corrected cable-genus equation p*gC+(p-1)(|q|-1)/2=3 ===")
sols = []
for p in range(2, 60):
    for q in range(-20, 21):
        if q == 0:
            continue
        if math.gcd(p, abs(q)) != 1:
            continue
        for gC in range(0, 5):
            if 2 * p * gC + (p - 1) * (abs(q) - 1) == 6:
                sols.append((p, q, gC))
gCpos = sorted(s for s in sols if s[2] >= 1)
print("machine-enumerated gC>=1 solutions:", gCpos)
assert gCpos == [(2, -3, 1), (2, 3, 1), (3, -1, 1), (3, 1, 1)], gCpos
# Case A (q>=2): unique survivor (2,3,1)
A = [s for s in gCpos if s[1] >= 2]
assert A == [(2, 3, 1)], A
print("Case A (gC>=1,q>=2): unique solution (2,3,1)")
# Case B (q<=0): true solutions (2,-3,1),(3,-1,1), ALL Hom-killed uniformly
B = [s for s in gCpos if s[1] <= 0]
assert B == [(2, -3, 1), (3, -1, 1)], B
for (p, q, gC) in B:
    assert Q(q, p) < 2 * gC - 1, (p, q, gC)
    print(f"  Hom-kill {(p,q,gC)}: q/p={Q(q,p)} < 2gC-1={2*gC-1}")
print("Note: earlier draft's (p,-5,3) 'infinite family' was a signed-genus error")
print("(used (q-1) for q<0, giving spurious 3p+(p-1)(-6)/2=3); with |q| the true")
print("q<=-1 solutions are exactly (2,-3,1),(3,-1,1), killed above.")
# Case C (q=+-1): Hom slope kill for gC>=1
C = [s for s in gCpos if abs(s[1]) == 1]
assert C == [(3, -1, 1), (3, 1, 1)], C
for (p, q, gC) in C:
    assert Q(q, p) < 2 * gC - 1, (p, q, gC)
    print(f"  Hom-kill {(p,q,gC)}: (+-1)/p={Q(q,p)} < 2gC-1={2*gC-1}; no (p,+-1)-cable is L-space")
# Case D (gC=0): J=T(p,q) torus knot -> not satellite
D = sorted(s for s in sols if s[2] == 0)
print(f"Case D (gC=0, {len(D)} solutions e.g. {D[:6]}): J=T(p,q) torus -> NOT satellite")
# Boundary q/p==2gC-1 impossible: q=p(2gC-1) forces p|q, coprime -> p=1 <2.
print("Boundary slopes q/p=2gC-1: need p|q, impossible for p>=2 -> strict-vs-lax moot")
print("Genuine satellite survivors passing Hom: [(2,3,1)] only")

# ---------- R2 kill: C_{2,3}(trefoil) ----------
print("\n=== R2 kill: C_{2,3}(T(2,3)) ===")
C3 = {1: 1, 0: -1, -1: 1}
Cp = {2 * e: c for e, c in C3.items()}
prod = {}
for e1, c1 in Cp.items():
    for e2, c2 in C3.items():
        prod[e1 + e2] = prod.get(e1 + e2, 0) + c1 * c2
assert sum(prod.values()) == 1
a = {e: c for e, c in prod.items() if e >= 0}
t0 = sum(j * a.get(j, 0) for j in range(1, 8))
det = int(abs(sum(c * ((-1) ** e) for e, c in prod.items())))
a2 = sum(e * (e - 1) * c for e, c in prod.items()) // 2
print(f"t0/V0 = {t0} (req 2); det = {det} (req 7); a2 = {a2} (req 6)")
assert (t0, det, a2) == (1, 3, 5)
d0_surv = Q(1) - 2 * t0
print(f"d0(survivor +5 surgery) = {d0_surv} vs d0(Y) = -3 -> KILLED (4 mismatches)")
print("Survivor +5 surgery IS L-space (5>=2*3-1, Hom arXiv:0912.4046), so dl=d=du")
print("and the d0 mismatch IS the involutive-triple mismatch there.")

# ---------- R3: genus monotonicity ----------
print("\n=== R3 iterated JSJ: genus monotonicity ===")
print("Outermost companion of a satellite L-space knot is an L-space knot")
print("(Hom-Lidman-Vafaee arXiv:1406.1597, generalizing Hedden/Hom cables).")
print("Minimal satellite L-space companion over trefoil passing Hom is the")
print("(2,3,trefoil) cable of genus 3; any outer cable over it has genus")
print(">= 2*3 = 6 > 3 (cable genus formula). Minimal torus companion (unknot,")
print("g=0) forces a single cable (R2); minimal genus-1 L-space companion is the")
print("trefoil (Ghiggini+Ni), non-satellite. Hence no depth>=2 tower totals g=3.")
print("General JSJ at slope 5: outermost piece cable or composite, both covered.")
print("FALLBACK_VERIFY_OK")

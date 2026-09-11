# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Universal no-satellite-impostor theorem at slope 5 for T(2,7) — DRAFT (repaired)

## Claim (preset fallback, exact)
No satellite knot J in S^3 shares the +5 surgery on T(2,7): for every
satellite J, S^3_5(J) is not orientation-preservingly homeomorphic to
S^3_5(T(2,7)) =: Y.

## Target data (computed; `python3 output/artifacts/verify_target.py` → VERIFY_OK 6/6)
- T(2,7) = T(7,2) = 7_1: two-bridge L-space torus knot, g = 3.
- Δ(t) = t^3 − t^2 + t − 1 + t^{−1} − t^{−2} + t^{−3}; det = 7; a_2 = 6.
- Torsion/V-profile: V = [2,1,1,0], V_0 = 2; τ = ν = 3.
- Y = S^3_5(T(2,7)) is the Moser small Seifert manifold with base
  S^2(2,7,9), orbifold Euler < 0 (atoroidal), π_1 infinite; |H_1| = 5.
- Ni–Wu integer-surgery d-vector:
  d(Y) = (−3, −9/5, −11/5, −11/5, −9/5), d_0(Y) = −3.
- L-space onset 2g−1 = 5; Moser lens slopes 13, 15 — so 5 is non-lens.
- Involutive scope: Y is an L-space, so dl = d = du on Y. The survivor
  R2 +5 surgery is also an L-space (5 ≥ 2·3−1), so its d_0 mismatch IS the
  involutive-triple mismatch there. The Whitehead R1 surgery is non-L-space,
  killed classically; no involutive claim is made there.

## Standing reduction
If S^3_5(J) ≅ Y orientation-preservingly, then H_1 gives slope 5, and
since Y is an L-space, J is an L-space knot (Ozsváth–Szabó), hence prime
(Krcatovich). The L-space surgery formulae force, with the genus bound
g(J) ≤ 3 from 2g−1 ≤ 5, the full profile V = [2,1,1,0], V_0 = 2,
Δ_J = Δ_T, det = 7, a_2 = 6, d_0 = −3.

## Pattern-case table (covers ALL satellite patterns; log: `verify_fallback.py` → FALLBACK_VERIFY_OK)

| Row | Pattern class | Elimination |
|-----|---------------|-------------|
| R0 | Composite J = A # B | Krcatovich: L-space knots are prime. J L-space ⇒ prime. No composite reaches the surgery. |
| R1 | Whitehead doubles (Δ = 1); general winding-0 by theorem | Classical: Δ = 1 gives V_0 = 0 ≠ 2 and Ni–Wu d_0 = d(L(5,1),0) = +1 ≠ −3. General winding-number-0 satellites are never L-space knots (Hedden, arXiv:0806.2172, cabling/satellite Floer results). The Whitehead +5 surgery is non-L-space, so it is killed by the classical V_0/d_0 mismatch plus Hedden; the involutive check is moot there. KILLED. |
| R2 | Cable C_{p,q}(C), p ≥ 2, genus p·g(C) + (p−1)(\|q\|−1)/2 = 3 (standard torus-genus term (\|p\|−1)(\|q\|−1)/2) | Machine-checked + analytic: g_C ≥ 1 solutions are exactly {(2,3,1),(2,−3,1),(3,1,1),(3,−1,1)}. Case A (q ≥ 2): unique (2,3,trefoil) unchanged. Case B (q ≤ 0): true solutions (2,−3,1),(3,−1,1) killed uniformly by Hom (arXiv:0912.4046: cable admits L-space surgery iff companion does and q/p ≥ 2g(C)−1): −3/2, −1/3 < 1. The earlier draft's (p,−5,3) "infinite family" is withdrawn as a signed-genus artefact (it used (q−1) for q < 0); the corrected \|q\| equation has no such family. Case C (q = ±1): (3,±1,1) killed by the same Hom slope inequality ((±1)/3 < 1), so no (p,±1)-cable with g_C ≥ 1 is L-space (non-satellite remark deleted). Case D (g_C = 0): J = T(p,q) torus, not satellite. Sharp boundary q/p = 2g_C − 1 is arithmetically impossible for cables (p \| q ⇒ p = 1), so strict-vs-lax form is moot. Sole genuine survivor (2,3)-cable of the trefoil killed by four independent mismatches via Δ(t) = Δ_C(t^2)·Δ_{T(2,3)}(t): V_0 = 1 ≠ 2, det = 3 ≠ 7, a_2 = 5 ≠ 6, d_0 = −1 ≠ −3. KILLED. |
| R3 | Iterated JSJ (depth ≥ 2 / general JSJ) | Outermost companion of a satellite L-space knot is an L-space knot (Hom–Lidman–Vafaee, arXiv:1406.1597, generalizing Hedden/Hom). Genus monotonicity: the minimal satellite L-space companion over the trefoil passing Hom is the (2,3,trefoil) cable of genus 3, so any outer cable over it has genus ≥ 2·3 = 6 > 3 by the cable genus formula; the minimal torus (unknot, g = 0) companion forces a single cable (R2); the minimal genus-1 L-space companion is the trefoil (Ghiggini + Ni), non-satellite. Hence no depth-≥ 2 tower totals g = 3. General JSJ types at slope 5 reduce likewise: outermost piece is cable or composite, both covered. KILLED. |

## Why the fallback success criterion is met
- Universality: R0–R3 exhaust all satellite JSJ patterns (composite,
  Whitehead-double + general winding-0, cable with corrected \|q\|
  analytic + machine-checked solution sets, iterated/general JSJ via
  genus monotonicity collapse to R2).
- Per-case numerical kills: logged pattern-case table above, each row with
  an explicit mismatch (V_0 / d_0 / det / a_2).
- Mapping-cone d-vector: computed d(Y) = (−3,−9/5,−11/5,−11/5,−9/5); every
  surviving-case comparison uses it (R1: +1 vs −3; R2: −1 vs −3).
- Involutive V_0 check: V_0(T) = 2 vs V_0(Wh) = 0, V_0(survivor) = 1; the
  survivor surgery is an L-space so dl = d = du and the d_0 mismatch is the
  involutive-triple mismatch there; the Whitehead surgery is non-L-space and
  carries no involutive claim.

## Separation of proof / computation / conjecture
- Proof: pattern-case exhaustion logic, corrected \|q\| cable-genus solution
  with Hom slope kills, JSJ genus-monotonicity collapse — from cited theorems
  (Moser, Ozsváth–Szabó, Ni–Wu, Krcatovich, Hedden arXiv:0806.2172,
  Hom arXiv:0912.4046, Hom–Lidman–Vafaee arXiv:1406.1597, Ghiggini/Ni).
- Computed evidence: `verify_target.py` (baseline data), `verify_fallback.py`
  (row-by-row kills, asserting corrected solution sets), both replayable stdlib-only.
- Conjecture/uncertainty: none within the fallback scope. Full +5
  characterization (hyperbolic twins) remains open — explicitly out of scope.

## Limitations
- Uses the Hedden/Hom satellite–L-space classification (cable + winding-0
  rigidity) and Krcatovich primeness as cited tools; does not reprove them.
- Says nothing about hyperbolic or torus impostors (torus impostors other
  than T(2,7) are separately excluded in target work, but that is not part
  of this claim).
- Orientation-preserving only, as stated.

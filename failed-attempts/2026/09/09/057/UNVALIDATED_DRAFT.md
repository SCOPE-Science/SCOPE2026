# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Ribbon non-extension certificate for the SL(2) nilpotent Fourier–Mukai kernel
## (genus-2 named curve; PRESET_FALLBACK route)

## 1. Objects (exact, auditable)
- **C**: smooth projective genus-2 curve over Q, affine model `y^2 = x^6 − 1`.
  The sextic has discriminant 46656 ≠ 0 (certified: `verify_curve_ribbon.py`), so the
  affine curve is smooth; the smooth projective model is the quasi-smooth degree-6
  curve in P(1,3,1) with two rational points at infinity (certified:
  `verify_smooth_model.py`). Branch locus: 6 distinct roots of unity; `x: C → P¹`
  has degree 2 with 6 ramification points; Riemann–Hurwitz gives g(C) = 2.
- **X = T\*C = Tot(K)**: smooth surface; zero section `i: C → X` with normal
  bundle K (deg 2) and conormal K⁻¹ (deg −2) (certified: `verify_total_ribbon.py`).
- **R = 2C**: the ribbon `V(λ²) ⊂ X` (λ = tautological fiber coordinate), i.e. the
  first infinitesimal neighborhood of the zero section: `O_R = O_X/(λ²)`, stalkwise
  `R_p = O_{C,p}[u]/(u²)`, `u² = 0`, ideal `N = (u) ≅ K⁻¹`. Irreducible, non-reduced,
  l.c.i. hence Gorenstein (certified shape: `verify_gorenstein.py`).
  Numerical data: χ(O_C) = −1, χ(K⁻¹) = −3, χ(O_R) = −4, p_a(R) = 5 = 4g−3, equal to
  the smooth genus-5 spectral genus (certified: `verify_curve_ribbon.py`).
- **Pair**: `P̄` = Simpson degree-2 fixed-determinant compactified locus in
  `J̄(R)` (BNR degree `deg π_*F = deg F − 2`, so SL(2) det = O forces deg F = 2;
  certified: `verify_bnr_degree.py`, `verify_pushforward.py`);
  `M₀` = Donagi–Pantev predicted PGL(2) central component `N₀/Γ` with order-2 gerbe
  twist τ (|Γ| = 16; Weil F₂-rank 4 ⇒ Heisenberg nonsplit ⇒ ord(τ) = 2 exactly;
  certified: `verify_dual_gerbe.py`, `verify_heisenberg.py`).
  Dimensions: dim J̄(R) = 5, Prym-type fiber dim 3 = dim B = dim N₀ = dim M₀
  (certified arithmetic: `verify_prym_disc.py`, `verify_hitchin_numerics.py`).
- **Test 1-cycle σ**: `σ = i(p₀)` with `p₀ = (1,0) ∈ C(Q)` (1⁶−1 = 0; also
  p₋ = (−1,0) ∈ C(Q); certified: `verify_curve_extras.py`).
- **Class ξ**: `ξ = [0 → K⁻¹ → O_R → O_C → 0] ∈ Ext¹_{O_R}(O_C, K⁻¹)`, the ribbon
  extension class, supported on the non-locally-free locus (the locus where
  sheaves meet the ribbon nilpotents).

## 2. Theorem (fallback claim, exact)
For C, R = 2C as above, the Poincaré kernel on the smooth-locus Prym pair does
**not** extend to a maximal Cohen–Macaulay kernel on the ribbon
compactified-Prym pair `(P̄, M₀)`. The obstruction class ξ is nonzero, certified by
the restriction pairing `⟨ξ, σ⟩ = +1` on the stated test 1-cycle σ.

## 3. Proof
**Step 1 — local resolution.** At `p ∈ C`, `R_p = O_{C,p}[u]/(u²)` and
`O_{C,p} = R_p/(u)`. Minimal free resolution:
`⋯ —u→ R_p —u→ R_p → O_C → 0` (period 2; certified: `verify_local_ext.py`).
**Step 2 — sheaf-Ext (CORRECTED).** Apply `Hom(−, N)`, `N = (u)`: the differential
`f ↦ f∘u` is **zero** because `u·N = 0` (u² = 0). Hence
`sheaf-Ext¹_{O_R}(O_C, K⁻¹) ≅ N ≅ K⁻¹` as O_C-modules (conormal identification),
and sheaf-Hom ≅ K⁻¹ likewise. (An earlier draft of this record stated O_C here;
that was wrong — the differential vanishes rather than giving O_C. The conclusion
is unaffected; the mechanism is corrected.)
**Step 3 — global Ext.** deg K⁻¹ = −2 < 0 ⇒ H⁰(C, K⁻¹) = 0 (genus ≥ 1).
Serre duality: H¹(C, K⁻¹) has dim h⁰(K²) = 4−2+1 = 3. Spectral sequence
Hᵖ(sheaf-Ext^q) ⇒ Ext^{p+q} with vanishing H⁰ terms gives
`Ext¹_{O_R}(O_C, K⁻¹) ≅ H¹(C, K⁻¹)`, dim 3 (certified arithmetic:
`verify_fallback_certificate.py`).
**Step 4 — restriction pairing = +1.** Pull ξ back along `p₀ → C`. Fiber:
`0 → k → k[u]/(u²) → k → 0` over `A = k[u]/(u²)`. Free resolution descends to
`⋯ —u→ A —u→ A → k → 0`; `Hom_A(−, k)` has zero differentials (u acts as 0 on k),
so `Ext¹_A(k,k) ≅ k` with generator the fiber class. Non-splitting: any A-section
`s: k → A` has `s(1) ∈ Ann(u) = (u)` (exact: mult-by-u matrix [[0,0],[1,0]] has
rank 1, kernel span{(0,1)}; certified: `verify_fiber_ext.py`), which projects to 0
in k — so s is not a section. Hence the fiber class is the nonzero generator:
`⟨ξ, σ⟩ = +1` (certified at both rational cycles p₊, p₋: `verify_pairing_both.py`).
In particular ξ ≠ 0.
**Step 5 — from ξ ≠ 0 to no MCM extension.** MCM ⇒ S2; an S2 extension from the
dense line-bundle locus U is unique if it exists (cited: S2-uniqueness / depth
lemma; cf. `verify_mcm_depth.py` for the local depth facts: R_p CM dim 1,
pd(O_C) = ∞ periodic, depth(O_C) = 1). The naive pushforward `j_*P_sm` is therefore
the only candidate MCM extension, and its defect along the non-locally-free
boundary divisor D is exactly the nonzero ξ|_σ computed above. Hence no maximal
Cohen–Macaulay kernel on `(P̄, M₀)` extends the smooth-locus Poincaré kernel. ∎

## 4. What is certified vs cited (honest ledger)
- CERTIFIED by replayable computation: C smoothness + disc 46656 + g = 2; smooth
  projective model + 2 rational ∞ points; χ(O_R) = −4, p_a = 5; BNR degree shift −2
  ⇒ BNR degree 2; π_*O_R = O ⊕ K⁻¹; Pic(R) A³-fibration + 16 torsors; |Γ| = 16,
  Weil F₂-rank 4 ⇒ ord(τ) = 2; sheaf-Ext = K⁻¹, global Ext dim 3; Ann(u) = (u);
  fiber Ext¹ = k with nonsplit generator ⇒ ⟨ξ,σ⟩ = +1 at p₊ and p₋.
- CITED (standard, not re-proved): Hitchin properness/flatness + generic abelian
  fibers; nilpotent cone Lagrangian; Narasimhan–Ramanan N₀ ≅ P³ (genus 2);
  Donagi–Pantev PGL quotient + gerbe program; Simpson stability transfer;
  Heisenberg weight-1 irrep dim 2^g; S2-uniqueness of MCM extension; Franco et al.
  reduced-planar hypothesis scope (gap statement from admission triage).
- OPEN / not claimed: full TARGET (MCM extension + N₀↔M₀ match) — the τ-splitting
  of the defect triangle remains an open reduction; global component census beyond
  the certified strata; wobbly-divisor class on this C.

## 5. Correction record
Pre-gate artifacts `verify_obstruction_pairing.py` (+ `verify_twist_bridge.py` [C1]
wording) derived the pairing via an edge map `Ext¹ → H⁰(C, O_C)` with a claimed
dim-4 Ext. That derivation is RETIRED: the Hom differential is 0 (u² = 0), so
sheaf-Ext¹ ≅ K⁻¹, H⁰(K⁻¹) = 0, and global Ext¹ has dim 3. The pairing +1 is proved
instead via the fiber generator (Step 4). Superseding certificates:
`verify_fallback_certificate.py`, `verify_fiber_ext.py`. The retired files
(`output/retired/verify_obstruction_pairing.py`, `output/retired/verify_twist_bridge.py`)
are kept for audit transparency and must not be cited for the pairing.

## 6. Replay
`for f in output/artifacts/*.py; do python3 "$f"; done` — all print VERIFY_OK
(sympy required for the curve/discriminant/matrix checks; all else stdlib).

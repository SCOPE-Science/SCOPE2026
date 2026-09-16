# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Elliptic quasimap mirror and genus-one wall-crossing for non-convex CY3 complete intersections in weighted projective stacks
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20463
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Enumerative Geometry
- **Method:** virtual localization and wall-crossing analysis

## Problem

Let X ⊂ P(w) = P(w0,…,wn) be a smooth Calabi–Yau threefold complete intersection defined by a generic section of E = ⊕j O(bj) with Σ bj = Σ wi, as in Janda–Sultani–Zhou §1.1, allowing non-convex E where classical quantum Lefschetz fails (concrete test case: generic X7 ⊂ P(1,1,1,1,3); also X17 ⊂ P(2,2,3,3,7)). Fix the extended GIT presentation X = [We // (C*)^{m+1}] built from degree-2 admissible classes {φi} and its explicit extended I-function I(q0,…,qm,z) of Janda–Sultani–Zhou Theorems 4.3.6/5.2.4. Using torus localization on the 0+-stable quasimap moduli Q^{0+}_{1,0}(X,β), determine in closed form the unpointed genus-1 0+-quasimap generating series ⟨⟩^{0+}_{1,0} := Σ_{β≠0} q^β deg[Q^{0+}_{1,0}(X,β)]^{vir} in terms of Birkhoff-factor data of the (equivariant) extended I-function (orbifold/weighted analogue of Kim–Lho's μ(q), R0(q), Ck(q)), and prove by Yang Zhou's orbifold quasimap wall-crossing that it implies the explicit unpointed genus-1 orbifold Gromov–Witten mirror formula ⟨⟩^{∞}_{1,0} for X, identifying the correct unpointed genus-1 correction term (orbifold analogue of (1/24)χ_top(X) log I0 + (1/24)∫_X (I1/I0) c_{dimX-1}(TX)), in particular evaluating it for X7. The claimed identities are exact equalities of formal q-series (Novikov variables), unconditional on the BCOV mirror conjecture.

## Attempted claim

Let X ⊂ P(w) = P(w0,…,wn) be a smooth Calabi–Yau threefold complete intersection defined by a generic section of E = ⊕j O(bj) with Σ bj = Σ wi, as in Janda–Sultani–Zhou §1.1, allowing non-convex E where classical quantum Lefschetz fails (concrete test case: generic X7 ⊂ P(1,1,1,1,3); also X17 ⊂ P(2,2,3,3,7)). Fix the extended GIT presentation X = [We // (C*)^{m+1}] built from degree-2 admissible classes {φi} and its explicit extended I-function I(q0,…,qm,z) of Janda–Sultani–Zhou Theorems 4.3.6/5.2.4. Using torus localization on the 0+-stable quasimap moduli Q^{0+}_{1,0}(X,β), determine in closed form the unpointed genus-1 0+-quasimap generating series ⟨⟩^{0+}_{1,0} := Σ_{β≠0} q^β deg[Q^{0+}_{1,0}(X,β)]^{vir} in terms of Birkhoff-factor data of the (equivariant) extended I-function (orbifold/weighted analogue of Kim–Lho's μ(q), R0(q), Ck(q)), and prove by Yang Zhou's orbifold quasimap wall-crossing that it implies the explicit unpointed genus-1 orbifold Gromov–Witten mirror formula ⟨⟩^{∞}_{1,0} for X, identifying the correct unpointed genus-1 correction term (orbifold analogue of (1/24)χ_top(X) log I0 + (1/24)∫_X (I1/I0) c_{dimX-1}(TX)), in particular evaluating it for X7. The claimed identities are exact equalities of formal q-series (Novikov variables), unconditional on the BCOV mirror conjecture.

## Research outcome

Emergent twisted-corrected genus-one quasimap wall-crossing identity for non-convex CY3 orbifolds with X7 nonvanishing and verified correction coefficients, after the closed unpointed target proved structurally blocked.

## Why this attempt failed

Failed axes: originality, value.

originality: EMERGENT_FINDING arose from blocked target routes A/B, so route is genuine, but headline is mechanically implied by cited priors. Part (a) is Zhou Cor 1.11.3 specialized to t=0,g=1 for a GIT quotient, which Zhou explicitly states for all targets in all genera including orbifolds. Mu-splitting mu=z(I0-1)+I1+I1' and X7 nonvanishing series plus Lemma 5.2.3 are verbatim in JSZ genus-zero paper. No new localization, vertex reduction, or independent genus-one computation is supplied; concatenation of Zhou wall-crossing with JSZ extended I-function is routine for an expert reader. Prior need not state headline verbatim to cover it. value: No independently retrievable advance beyond restatement plus routine computation. The corrected identity restates Zhou's general formula for the JSZ target class; X7 nonvanishing quotes JSZ printed series; chi/int-c2.H numbers follow from 5-line adjunction c(TX)=prod(1+wH)/prod(1+bH) with intH^3=prod b/prod w, mechanically implied and instantly recomputable (quintic control confirms method is textbook). Preventing pursuit of a false closed unpointed mirror is useful pedagogy but here amounts to reading off that Zhou's mu contains twisted insertions already visible in JSZ, not a new obstruction lemma, benchmark, classification, or exact invariant that is unknown and needed later.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The full closed-loop orbifold A_i-type localization (extended-GIT double-J factorization and twisted genus-one vertex/Hodge reduction) is not proved and is not claimed; no BCOV-type or enumerative consequence beyond the stated identity, nonvanishing, and topological numbers is claimed; extracted equations from PDFs were used with theorem-number citations and a quintic control but without independent visual re-verification of every printed series coefficient.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

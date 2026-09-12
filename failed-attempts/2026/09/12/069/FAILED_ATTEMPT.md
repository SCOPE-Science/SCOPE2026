# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Primitive Bloch invariant for +1 figure-eight surgery
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1229
- **Disposition:** AUDIT_1_REJECT
- **Domain:** hyperbolic geometry and algebraic K-theory
- **Method:** triangulation Bloch relation and Borel regulator computation

## Problem

Let M be the closed oriented 3-manifold obtained by +1 Dehn surgery on the figure-eight knot in S^3 (integral homology sphere, hyperbolic), equipped with a fixed ideal triangulation extending the canonical two-tetrahedron decomposition of the figure-eight complement, and let K_M be its invariant trace field certified by Snap with interval-verified shape parameters, explicitly distinct from Q(sqrt(-3)) which is only the trace field of the cusped complement. Let beta(M) in the Bloch group B(K_M) be its Neumann-Yang invariant with Borel regulator R and geometric normalization complex volume Vol(M) + i 2 pi^2 CS(M) with CS in R/Z. Prove or disprove that beta(M) is nontorsion and primitive (indivisible) in B(K_M) modulo torsion, generating the free rank-one summand, and that R(beta(M)) equals a single explicit nonzero rational multiple q of the full complex volume, pinning volume and Chern-Simons simultaneously with the same q. A complete answer either gives a certified triangulation, machine-checkable Bloch-relation verification, explicit K_M minimal-polynomial certificate, and regulator computation pinning one q for both real and imaginary parts, or gives a certified refutation (torsion/divisibility collapse or real-imaginary q mismatch requiring distinct rationals).

## Attempted claim

Let M be the closed oriented 3-manifold obtained by +1 Dehn surgery on the figure-eight knot in S^3 (integral homology sphere, hyperbolic), equipped with a fixed ideal triangulation extending the canonical two-tetrahedron decomposition of the figure-eight complement, and let K_M be its invariant trace field certified by Snap with interval-verified shape parameters, explicitly distinct from Q(sqrt(-3)) which is only the trace field of the cusped complement. Let beta(M) in the Bloch group B(K_M) be its Neumann-Yang invariant with Borel regulator R and geometric normalization complex volume Vol(M) + i 2 pi^2 CS(M) with CS in R/Z. Prove or disprove that beta(M) is nontorsion and primitive (indivisible) in B(K_M) modulo torsion, generating the free rank-one summand, and that R(beta(M)) equals a single explicit nonzero rational multiple q of the full complex volume, pinning volume and Chern-Simons simultaneously with the same q. A complete answer either gives a certified triangulation, machine-checkable Bloch-relation verification, explicit K_M minimal-polynomial certificate, and regulator computation pinning one q for both real and imaginary parts, or gives a certified refutation (torsion/divisibility collapse or real-imaginary q mismatch requiring distinct rationals).

## Research outcome

+1 surgery on the figure-eight knot is non-hyperbolic (small Seifert fibered), so the target's hyperbolic Bloch invariant premise is refuted with an exact machine-checked knot/homology certificate.

## Why this attempt failed

Failed axes: originality, value.

originality: Originality FAILS: the headline refutation that +1 surgery on the figure-eight knot is non-hyperbolic small Seifert fibered is a classical, long-recorded fact substantively implied by prior work. Thurston/Gordon exceptional-surgery theory, Brittenham/Dean/Miyazaki-Motegi Seifert-surgery literature, and Lackenby-Meyerhoff (arXiv:0808.1176) recording 10 exceptional slopes for the figure-eight exterior already cover +1 as exceptional/non-hyperbolic. Fused retrieval explicitly returned these sources and snippets stating the figure-eight has 10 exceptional slopes and small Seifert-fibered exceptional surgeries. A new machine certificate for the well-known Alexander polynomial and H1=Z/0 does not make the covering theorem new; recomputation is not priority. value: Value FAILS. ADMISSION_DEFECT: the target admitted as hyperbolic a manifold classically known to be non-hyperbolic (closed +1 figure-eight surgery is textbook exceptional small Seifert fibered), so the likely negative resolution was a cheap type/presupposition defect, direct table lookup, and textbook restatement that Admission should have ruled out under STANDARD.md. The submission correctly exposes that defect but does not supply an independently retrievable new theorem, invariant value, census, or downstream use: no new Bloch regulator, no new volume, no new classification boundary. Certification and replayability strengthen evidence but per the shared standard do not create value by themselves.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The final non-hyperbolicity step cites the published Gordon/Thurston/Lackenby-Meyerhoff exceptional-surgery classification and geometrization rather than re-deriving them from the presentation in-lane; the Riley/longitude/filled-representation numerics are heuristic corroboration only and are not claimed as proof. No Snap/interval-verified tetrahedral shapes are provided because the conclusion is that no hyperbolic structure exists to verify.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

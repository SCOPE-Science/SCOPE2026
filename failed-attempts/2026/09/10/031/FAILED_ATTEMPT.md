# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Sharp Elliott-invariant obstruction witness for the Giol-Kerr perforated minimal Cantor crossed product
- **Round:** 2026-09-07-first-light-01
- **Lane:** 585
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Operator Algebras
- **Method:** Elliott-invariant K-theory and traces with Rokhlin-dimension estimates and KK-theoretic classification transfer

## Problem

Decide the Jiang-Su stability cell of the Giol-Kerr perforated minimal Cantor crossed product A_GK = C(X_GK) ⋊_h Z (X_GK the Giol-Kerr minimal subshift with perforated K0): since qualitative non-Z-stability is known, exhibit the sharp Elliott-invariant obstruction — an explicit K0 perforation-witness class with certified trace pairing — and prove a classification-boundary lemma stating that no Z-stable simple unital nuclear C*-algebra shares its K0-trace pairing data.

## Attempted claim

For the Giol-Kerr perforated minimal Cantor crossed product A_GK: exhibit an explicit perforation witness class [w] in K0(A_GK) with certified trace pairing tau_*([w]) = c, and prove a classification-boundary lemma that no unital simple separable nuclear Z-stable C*-algebra has Elliott-invariant K0-trace pairing data matching (K0(A_GK), tau_*), so A_GK is a sharp non-isomorphism witness at the Toms-Winter boundary.

## Research outcome

Sharp Elliott-invariant obstruction witness for the Giol-Kerr perforated minimal crossed product: certified trace pairing c=1 on the K0 perforation witness with n=2 gap and classification-boundary lemma; replayable stdlib certificate VERIFY_OK.

## Why this attempt failed

Failed axes: value.

value: TARGET value fails independently. The only new datum beyond published Giol-Kerr + Rordam corollary is c=1, which is virtual rank 2-1=1: rk(Hopf)=1 definitional, rk(xi^{x2})=1+1=2, minus rk(theta1)=1. Trace-independence is immediate because integrand Tr(P)-Tr(Q) is fiberwise constant 1, so integration against any probability gives 1; any future user would recompute in one line, not retrieve this log. No new obstruction strength: weak perforation already obstructs Z-stability irrespective of whether pairing is 1 or another positive number; trace-blindness ([w] vs [1] share pairing 1 yet differ in order) is generic to any positive-pairing perforation, and boundary lemma's intertwining hypothesis adds nothing because order-unit isomorphism already impossible from perforation alone. Script's 46 lines certify elementary algebra (Pauli identities, K-ring axioms on 4^3 triples, (l,E) census, weight sums) not new mathematics; full K0(A_GK)/K1(A_GK) remain uncomputed per Limitations, so no Elliott-invariant lookup is enabled beyond one rank. Stated radius-of-comparison/Toms-Winter reuse is unsubstantiated - no downstream theorem uses c=1, no criterion requires it. This is textbook restatement (rank arithmetic) + certification alone + tiny unmotivated gain, explicitly rejectable even if correct and new. Exact-invariant eligibility clause requires value not mechanically implied and reasonably needed later; c=1 is mechanically implied by definition of g and not shown to be needed. Defect intrinsic, not a missing citation or motivation fix.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ["Full K0(A_GK)/K1(A_GK) not computed (paper: 'much more complicated than rationals'); only the witness subgroup + PV quotient description is made explicit.", 'Bundle-embedding theorems (Villadsen Lemma 1, Husemoeller 8.1.2), PV sequence, GK Lemma 2.1, Davidson VIII.3 trace correspondence, Rordam/Gong-Jiang-Su implication are cited tools, not new results.', 'Qualitative perforation=>non-Z-stable is a corollary of GK + general theorems (admission-flagged); new content is explicit c=1 certificate…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Explicit needle-localized Mahler stability gap for unconditional bodies in R^4
- **Round:** 2026-09-07-first-light-01
- **Lane:** 759
- **Disposition:** NO_RESULT
- **Domain:** Convex Geometry
- **Method:** needle localization decomposition with functional Santalo inequality and Banach-Mazur stability analysis

## Problem

Establish an explicit Mahler-product stability gap for unconditional centrally symmetric convex bodies in R^4: bound the deficit above the conjectured minimum 32/3 from below by an explicit function of Banach-Mazur distance to the Hanner-polytope class, via needle localization and functional Santalo.

## Attempted claim

There exists an explicitly numerically certified constant c4 > 0, produced by the proof, such that every unconditional centrally symmetric convex body K in R^4 satisfies |K||K*| >= 32/3 + c4 * min{1, d_BM(K,H_4)-1}^2, where K* = {y : <x,y> <= 1 for all x in K}, |.| is Lebesgue volume, H_4 is the class of 4-dimensional Hanner polytopes, and d_BM is Banach-Mazur distance.

## Research outcome

Full-R^4 explicit Mahler stability (target) blocked at global effectivization (explicit uniform gap known only via inexplicit compactness). Revealed S4-window fallback pursued exactly (census reduction CENSUS_OK + ray consistency RAY_CONSISTENT) but remains ATTEMPTED_AND_BLOCKED on the same universal-gap step. No valuable original increment. Clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['No universal explicit stability inequality proved for full R^4 or S4 window; global compactness-effectivization step remains open.', 'S4 census lemma and ell_p ray probe are supporting checks only, not standalone results.', '1D deficit fragment never closed to audit standard; no verified lemma artifact banked.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['No universal explicit stability inequality proved for full R^4 or S4 window; global compactness-effectivization step remains open.', 'S4 census lemma and ell_p ray probe are supporting checks only, not standalone results.', '1D deficit fragment never closed to audit standard; no verified lemma artifact banked.']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

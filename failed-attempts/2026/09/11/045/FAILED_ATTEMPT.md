# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Cap N_{1/5}(18) at 58 via Jacobi forbidden polynomial
- **Round:** 2026-09-07-first-light-01
- **Lane:** 799
- **Disposition:** NO_RESULT
- **Domain:** Algebraic Combinatorics
- **Method:** Jacobi identity for complementary subgraphs plus Seidel characteristic-polynomial integrality

## Problem

Prove at most 58 equiangular lines with angle arccos(1/5) exist in R^18 by forbidding the surviving n=59 characteristic-polynomial family via the Jacobi identity for complementary subgraphs.

## Attempted claim

No system of 59 equiangular lines with common angle arccos(1/5) exists in R^18: every candidate graph on 59 vertices compatible with Seidel interlacing in rank 18 has a characteristic polynomial violating the Jacobi complementary-subgraph identity, so N_{1/5}(18) <= 58.

## Research outcome

Target N_{1/5}(18) <= 58 via Jacobi forbidden-polynomial exclusion is BLOCKED: full n=59 enumeration plus per-family Jacobi kills proved unreachable in-lane. The available bounded alternative (proved forbidden integer-spectrum subfamily, the survey valuable-partial target) was concretely attempted with exact replayable arithmetic and is BLOCKED: 28 weakly-type-2 survivors of 722 remain (logged in output/artifacts/bounded_alt_results.txt), and per-survivor Jacobi kills are unavailable in-lane. No preset fallback was admitted (NOT_PRESET) and no valuable emergent finding exists. Clean exit with attempted-and-blocked alternative.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Lane tooling is stdlib+numpy+sympy only (no Magma/Mathematica/SDP solver); complete totally-real degree-18 enumeration with interlacing/congruence filtering plus per-family Jacobi kills was unreachable. The bounded alternative (integer-subfamily exclusion under the correct weakly-type-2 condition) was concretely attempted: 28 of 722 integer multisets survive, each needing a per-survivor Jacobi kill unavailable in-lane; irrational spectra are uncovered. No emergent alternative can pass Audit.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Lane tooling is stdlib+numpy+sympy only (no Magma/Mathematica/SDP solver); complete totally-real degree-18 enumeration with interlacing/congruence filtering plus per-family Jacobi kills was unreachable. The bounded alternative (integer-subfamily exclusion under the correct weakly-type-2 condition) was concretely attempted: 28 of 722 integer multisets survive, each needing a per-survivor Jacobi kill unavailable in-lane; irrational spectra are uncovered. No emergent alternative can pass Audit.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

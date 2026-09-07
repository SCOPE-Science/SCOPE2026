# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing the BKLC gap at [36,10]: an LP-dual plus residual certificate for nonexistence of a binary [36,10,14] code
- **Round:** 2026-09-07-first-light-01
- **Lane:** 84
- **Disposition:** NO_RESULT
- **Domain:** Coding Theory
- **Method:** Delsarte linear-programming bounds with finite integer search

## Problem

Decide existence of a binary linear [36,10,14] code. Prove that no such code exists (hence d_max(36,10)=13, attaining the known [36,10,13] construction) via an explicit Delsarte-LP dual feasible certificate combined with a finite MacWilliams / residual / shortening case check; or, alternatively, exhibit an explicit generator matrix of a [36,10,14] code. Success closes Grassl BKLC entry [36,10] (currently 13 lower, 14 upper).

## Attempted claim

There is no binary linear [36,10,14] code; consequently the optimal minimum distance at (n,k)=(36,10) is d=13, and the known BE-derived [36,10,13] code is optimal. Evidence is a solver-checkable package: Delsarte (36,14) dual feasible vector + exhaustive MacWilliams/residual integer feasibility log + shortening reduction to the classified vT3 region.

## Research outcome

The [36,10,14] existence question remains OPEN: pure Delsarte, Griesmer, residual, and MacWilliams-LP levels were each pushed to a machine-checkable certificate and each provably fails to close the Grassl [36,10] gap (13 vs 14). Delivered the topic fallback partial certificate: exact Griesmer audit, integer-verified Delsarte-dual bound M<=3193.13, complete LP weight-multiplicity profile (A_14 forced, all weights allowed, even subcase feasible), corrected residual-branch table (all t=14..23 Griesmer-admissible), and shortening-chain non-closure audit - all replayable in minutes via archived numpy-only/stdlib scripts.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Full nonexistence of [36,10,14] NOT proved; gap remains open.', 'Delsarte dual bound (3193) far above 1024: quantified non-closure.', 'LP weight-profile numbers are float solver outputs (tolerance 1e-7..1e-9); only the dual certificate is exact.', 'Residual lemma dimension is proved exactly (kernel = {0,c}) only for the t = d branch; for t > d branches the table uses only the Griesmer-necessary direction (G increasing in k), so no branch is wrongly discharged.', 'Integer DFS datum is support-restricted illustration, not elimination.', 'No MAGMA/heavy ILP/SDP; single-CPU ~2h budget.', 'Grassl snapshot is a live web fetch dated 2026-09-07, not an archived copy.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Full nonexistence of [36,10,14] NOT proved; gap remains open.', 'Delsarte dual bound (3193) far above 1024: quantified non-closure.', 'LP weight-profile numbers are float solver outputs (tolerance 1e-7..1e-9); only the dual certificate is exact.', 'Residual lemma dimension is proved exactly (kernel = {0,c}) only for the t = d branch; for t > d branches the table uses only the Griesmer-necessary direction (G increasing in k), so no branch is wrongly discharged.', 'Integer DFS datum is support-…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

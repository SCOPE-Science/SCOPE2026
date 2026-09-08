# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exact certified W1/W2 cost table with Kantorovich duality on 4x4 and 5x5 Manhattan grids
- **Round:** 2026-09-07-first-light-01
- **Lane:** 235
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Optimal Transport
- **Method:** Kantorovich linear-programming duality with min-cost-flow primal search and complementary-slackness certificate replay

## Problem

Compute and certify exact 1- and 2-Wasserstein costs for a fixed suite of ~12 finitely supported measure pairs (rational masses with denominator 8) on 4x4 (6 pairs) and 5x5 (6 pairs) grids under Manhattan ground cost, each with paired primal/dual optimal solutions and complementary-slackness replay logs.

## Attempted claim

For each of the 12 fixed pairs: W1 cost equals the stated exact rational value witnessed by a feasible min-cost-flow transport plan and a feasible Kantorovich potential with zero duality gap (complementary slackness verified); W2-squared cost likewise exact; including one pair whose every optimal plan necessarily splits mass (non-Monge) and one displacement-interpolation midpoint with certified cost.

## Research outcome

Certified exact 16-pair W1/W2sq table (12 core + strict-splitting P05S + midpoint M1-M3) with zero-gap integer primal/dual certificates and grid Kantorovich potentials, all replayed exactly by stdlib verify.py.

## Why this attempt failed

Failed axes: value.

value: Even taking the strongest headline (P05S strict-splitting witness) separately from the surrounding 12-pair survey, the result is an arbitrary object with certification alone and no independent retrieval value. The 4x4/5x5 denominator-8 suite is author-constructed, not a recognized benchmark suite, census, or extremal class: 6+ entries are trivial unit shifts at 8/8=1 obvious without LP; corners-to-center/ corners-cross entries are direct distance reads; midpoint additivity 16/8=8/8+8/8 follows immediately from translation invariance by 1. No completeness, maximality, classification, or general criterion is proved. The P05S pair was invented to exhibit splitting, not motivated as an object before computation by any cited literature demand for this pair; no source asks for W1/W2 of this specific 8-token configuration. General atom-splitting is textbook (discrete source atoms must split when targets are split); P05S is one more instance with no proved extremality within any defined class (not shown minimal, maximal-gap, or unique), no literature position, and no downstream benchmark that needs this precise pair rather than any canonical splitter. Midpoint triple likewise has no geodesic content beyond W1 additivity of repeated shifts. Future researchers benchmarking Sinkhorn error or Ollivier curvature would compute their own pairs, not retrieve P04=20/8,58/8 or P11=10/8,16/8. This is textbook LP application to hand-picked inputs (parameter substitution) plus unexplained enumeration. Per instructions certification alone does not rescue an arbitrary object, and a narrow datum must have pre-computation motivation and plausible future need; neither holds. Defect is intrinsic arbitrary scope, not a bounded prose fix.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Fixed-suite finite certificate only (denominator-8 masses, Manhattan cost, 4x4/5x5 grids); no general OT theorem claimed. W2 duality is token-level assignment LP; only W1 additionally has grid-level potentials. Optimality is certificate-relative (exact integer replay); pair definitions transcribed in certificates.json. Originality is the archived paired primal/dual/potential artifact with splitting and midpoint witnesses, not the general Kantorovich theory.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

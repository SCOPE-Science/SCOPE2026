# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** No minimal blocking set of size 22 in PG(2,13)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 978
- **Disposition:** NO_RESULT
- **Domain:** Finite Geometry
- **Method:** Redei-polynomial lacunary slope ledger with secant-distribution census

## Problem

Decide whether the Desarguesian projective plane PG(2,13) admits a minimal nontrivial blocking set of exactly 22 points. A blocking set meets every line; it is nontrivial if it contains no full line and minimal if no proper subset still meets every line. The audit criterion is two-sided: a proof must exclude 22-point minimal blockers across all secant-type branches with a Redei-slope ledger, while a disproof must exhibit explicit 22-point coordinates together with a certified 183-line cover table and tangent witnesses at every point.

## Attempted claim

In PG(2,13) there is no minimal nontrivial blocking set with exactly 22 points: every 22-point point set meeting every line of the plane either contains a full line or admits a proper subset that already meets every line.

## Research outcome

Target blocked on both sides after 11 computational routes (C-direct-anneal, H-exact-swap-sweep, N-seeded-repair, J-ruin-recreate, K-grasp, Q-tempering, L-primitivity, O-long-secant, B-Redei-directions, C3-extension-census, theory-secant-census): no minimal nontrivial 22-set found and full exclusion infeasible; clean exit with certified negative statistics.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Search was stochastic and symmetry-unreduced over a C(183,22) space, so the negative statistics (zero minimal-22 across ~500 blocking 22-sets, 60/60 repair walks stuck at redundancy 1, direction floor 12 vs 9) are strong evidence but not a nonexistence proof; the ~3210-branch secant census was enumerated, not closed; verification scripts replay only the certified 21-sets and extension census, not an exclusion theorem.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Search was stochastic and symmetry-unreduced over a C(183,22) space, so the negative statistics (zero minimal-22 across ~500 blocking 22-sets, 60/60 repair walks stuck at redundancy 1, direction floor 12 vs 9) are strong evidence but not a nonexistence proof; the ~3210-branch secant census was enumerated, not closed; verification scripts replay only the certified 21-sets and extension census, not an exclusion theorem.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

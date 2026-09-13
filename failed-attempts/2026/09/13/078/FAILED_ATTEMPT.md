# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Level-3 Sherali-Adams gap persistence at 2 for R||Cmax
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1636
- **Disposition:** NO_RESULT
- **Domain:** lift-and-project hierarchies
- **Method:** Sherali-Adams level-3 lifting of assignment LP

## Problem

For general unrelated-machine makespan minimization R||Cmax (arbitrary finite processing times p_{ij} in [0, infinity], arbitrary eligibility via infinite entries; canonical assignment LP of Lenstra-Shmoys-Tardos at normalized guess T=1, i.e. fractional assignment with per-machine load at most 1 and infeasible machine-job pairs fixed to zero): after exactly 3 rounds of the Sherali-Adams lift-and-project procedure applied to this LP, is the worst-case integrality gap over all instances with arbitrarily many machines and jobs still equal to 2? A complete answer either exhibits one explicit instance with a rigorously verified feasible level-3 Sherali-Adams solution at T=1 whose integral optimum is at least 2 (gap persistence after 3 rounds), or proves with an explicit constant delta > 0 that every level-3 feasible instance admits an integral schedule of makespan at most 2 - delta.

## Attempted claim

For general unrelated-machine makespan minimization R||Cmax (arbitrary finite processing times p_{ij} in [0, infinity], arbitrary eligibility via infinite entries; canonical assignment LP of Lenstra-Shmoys-Tardos at normalized guess T=1, i.e. fractional assignment with per-machine load at most 1 and infeasible machine-job pairs fixed to zero): after exactly 3 rounds of the Sherali-Adams lift-and-project procedure applied to this LP, is the worst-case integrality gap over all instances with arbitrarily many machines and jobs still equal to 2? A complete answer either exhibits one explicit instance with a rigorously verified feasible level-3 Sherali-Adams solution at T=1 whose integral optimum is at least 2 (gap persistence after 3 rounds), or proves with an explicit constant delta > 0 that every level-3 feasible instance admits an integral schedule of makespan at most 2 - delta.

## Research outcome

Target blocked and budget expired: classic gap family provably dies at SA-1, tiny exhaustive cells contain no exact-2 attainer, and neither a gap-persistence instance nor a uniform-delta rounding proof was completed.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No explicit level-3 Sherali-Adams feasible instance with integral optimum at least 2 was constructed or verified, and no uniform delta>0 rounding proof was established. Evidence is limited to exact rational checks: the classic 2-1/m family dies at one conditioning step, plus exhaustive absence of exact-2 attainers in tiny 2x2 and 2x3 cells, which does not decide the target either way.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No explicit level-3 Sherali-Adams feasible instance with integral optimum at least 2 was constructed or verified, and no uniform delta>0 rounding proof was established. Evidence is limited to exact rational checks: the classic 2-1/m family dies at one conditioning step, plus exhaustive absence of exact-2 attainers in tiny 2x2 and 2x3 cells, which does not decide the target either way.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

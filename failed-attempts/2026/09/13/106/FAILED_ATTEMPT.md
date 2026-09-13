# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Komlos 8-column 2.5 versus 2.6 benchmark
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1720
- **Disposition:** NO_RESULT
- **Domain:** matrix discrepancy
- **Method:** entropy-method chaining on 8-column body with exact subset enumeration

## Problem

Let M be any real matrix with exactly 8 columns of Euclidean norm at most 1 (any number of rows), with hereditary discrepancy herdisc(M) = max_{K subset [8]} min_{x in {+-1}^K} max_{row r} |sum_{j in K} M_{r,j} x_j|. Prove or disprove that herdisc(M) <= 2.5 for every such M, by an explicit entropy-method partial-coloring chaining certificate applied to the 8-column body geometry. A complete answer either proves the stated explicit small-dimension benchmark upper bound, or gives a rigorous counterexample in the form of one explicit 8-column unit-norm matrix with a certified column subset attaining herdisc >= 2.6, improving the best known Komlos constant lower bound of 1+sqrt(2).

## Attempted claim

Let M be any real matrix with exactly 8 columns of Euclidean norm at most 1 (any number of rows), with hereditary discrepancy herdisc(M) = max_{K subset [8]} min_{x in {+-1}^K} max_{row r} |sum_{j in K} M_{r,j} x_j|. Prove or disprove that herdisc(M) <= 2.5 for every such M, by an explicit entropy-method partial-coloring chaining certificate applied to the 8-column body geometry. A complete answer either proves the stated explicit small-dimension benchmark upper bound, or gives a rigorous counterexample in the form of one explicit 8-column unit-norm matrix with a certified column subset attaining herdisc >= 2.6, improving the best known Komlos constant lower bound of 1+sqrt(2).

## Research outcome

Target blocked on both horns (envelope B&B UNDECIDED at all needed masses; witness search below 1.2) and the bounded hybrid alternative hits the same wall; clean exit with no claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Only the diffuse-mass regime was closed (Hoeffding-Jensen); concentrated-row certification, chaining completion, and any herdisc>=2.6 witness remain open. Heuristic envelope numbers (4,18,32,64,96,116) are uncertified observations, and witness search covered only hill-climbing plus standard structured families.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Only the diffuse-mass regime was closed (Hoeffding-Jensen); concentrated-row certification, chaining completion, and any herdisc>=2.6 witness remain open. Heuristic envelope numbers (4,18,32,64,96,116) are uncertified observations, and witness search covered only hill-climbing plus standard structured families.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

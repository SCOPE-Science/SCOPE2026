# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Bush-type (100,45,20) with partition-preserving orthogonal polarity
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1709
- **Disposition:** NO_RESULT
- **Domain:** combinatorial design theory
- **Method:** Bush-type tactical decomposition and polarity-constrained Kramer-Mesner

## Problem

For symmetric 2-(100,45,20) Menon designs (v=100, k=45, lambda=20, order n=25): determine whether there exists such a design admitting simultaneously a Bush-type tactical decomposition into 10 point classes and 10 block classes of size 10 (every point in either 0 or 5 blocks of each block class and dually) and an orthogonal polarity preserving that partition. A complete answer either exhibits a 100x100 incidence matrix satisfying the 2-(100,45,20) equations together with the explicit 10x10 class partition, its 10x10 tactical decomposition matrix, and the polarity permutation with verified absolute-point set, or proves by exhaustive Kramer-Mesner enumeration over Bush-type orbit matrices with the polarity symmetry imposed that no such combined structure lifts to a full incidence matrix, with the searched orbit-matrix set and decomposition log as certificate.

## Attempted claim

For symmetric 2-(100,45,20) Menon designs (v=100, k=45, lambda=20, order n=25): determine whether there exists such a design admitting simultaneously a Bush-type tactical decomposition into 10 point classes and 10 block classes of size 10 (every point in either 0 or 5 blocks of each block class and dually) and an orthogonal polarity preserving that partition. A complete answer either exhibits a 100x100 incidence matrix satisfying the 2-(100,45,20) equations together with the explicit 10x10 class partition, its 10x10 tactical decomposition matrix, and the polarity permutation with verified absolute-point set, or proves by exhaustive Kramer-Mesner enumeration over Bush-type orbit matrices with the polarity symmetry imposed that no such combined structure lifts to a full incidence matrix, with the searched orbit-matrix set and decomposition log as certificate.

## Research outcome

Target blocked: tactical/polarity level is exactly feasible (canonical 5-swap pattern verified), but the 100x100 Kramer-Mesner lift stalled at squared defect ~25000 versus 0 across ~1.75M annealing iterations with no structural shortcut found; clean exit with negative evidence logged.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No exhaustive Kramer-Mesner certificate was produced: the ~95-block 100x100 lift space is astronomically large and infeasible to enumerate in-session. Heuristic evidence is bounded (about 1.75M joint annealing iterations across two implementations) and does not constitute proof of nonexistence; a structured construction, for example via regular symmetric Hadamard matrices of order 100 or a refined switching search, may still succeed in future work.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No exhaustive Kramer-Mesner certificate was produced: the ~95-block 100x100 lift space is astronomically large and infeasible to enumerate in-session. Heuristic evidence is bounded (about 1.75M joint annealing iterations across two implementations) and does not constitute proof of nonexistence; a structured construction, for example via regular symmetric Hadamard matrices of order 100 or a refined switching search, may still succeed in future work.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

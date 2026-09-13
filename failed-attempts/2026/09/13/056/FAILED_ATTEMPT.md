# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Two-circuit 2-factor four-circuit cover at 8m/5
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1582
- **Disposition:** NO_RESULT
- **Domain:** cubic cycle covers
- **Method:** two-circuit 2-factor construction

## Problem

Let G be a bridgeless cubic graph with m edges possessing a 2-factor consisting of exactly two circuits, and define a circuit cover as a family of circuits covering E(G) with length the sum of circuit lengths. Prove or disprove that G admits a cycle cover consisting of at most four circuits of total length at most 8m/5. A complete answer is either a proof that every such two-circuit 2-factor G has such a four-circuit cover, exhibiting the construction from the 2-factor, or an explicit such G with a certified proof that every cover by at most four circuits has total length exceeding 8m/5.

## Attempted claim

Let G be a bridgeless cubic graph with m edges possessing a 2-factor consisting of exactly two circuits, and define a circuit cover as a family of circuits covering E(G) with length the sum of circuit lengths. Prove or disprove that G admits a cycle cover consisting of at most four circuits of total length at most 8m/5. A complete answer is either a proof that every such two-circuit 2-factor G has such a four-circuit cover, exhibiting the construction from the 2-factor, or an explicit such G with a certified proof that every cover by at most four circuits has total length exceeding 8m/5.

## Research outcome

Target blocked on both directions: exhaustive search found no counterexample (Petersen optimum 21/15, 230 random instances worst ratio 1.40, structured families at 4m/3) but cannot certify the universal claim, and the constructive proof from the two-circuit 2-factor lacks a length-preserving lemma for the 1.4n residual budget.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Exact min-4-circuit-cover certification scales exponentially (n=24 instance reached 1870 distinct cycles and timed out), so larger graphs could not be certified; the constructive proof attempt lacked a length-preserving two-circuit merging lemma; random and structured search covered only small orders. No universal proof and no counterexample were obtained.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Exact min-4-circuit-cover certification scales exponentially (n=24 instance reached 1870 distinct cycles and timed out), so larger graphs could not be certified; the constructive proof attempt lacked a length-preserving two-circuit merging lemma; random and structured search covered only small orders. No universal proof and no counterexample were obtained.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Cyclically 4-connected cubic cycle cover at 14m/9
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1579
- **Disposition:** NO_RESULT
- **Domain:** cubic cycle covers
- **Method:** ear-decomposition / flow-based cover

## Problem

Let G be a cyclically 4-edge-connected cubic bridgeless graph with m edges, where m=3n/2 for n vertices, and define a cycle cover as a family of even subgraphs whose edge-sets union to E(G) with length the sum of their edge-counts and cc(G) its minimum. Prove or disprove that cc(G) <= 14m/9 for every such G. A complete answer is either a proof of this bound for all such G, exhibiting the ear-decomposition cycle-space construction achieving it, or an explicit such G with a certified proof that every cycle cover has length exceeding 14m/9.

## Attempted claim

Let G be a cyclically 4-edge-connected cubic bridgeless graph with m edges, where m=3n/2 for n vertices, and define a cycle cover as a family of even subgraphs whose edge-sets union to E(G) with length the sum of their edge-counts and cc(G) its minimum. Prove or disprove that cc(G) <= 14m/9 for every such G. A complete answer is either a proof of this bound for all such G, exhibiting the ear-decomposition cycle-space construction achieving it, or an explicit such G with a certified proof that every cycle cover has length exceeding 14m/9.

## Research outcome

No proof and no counterexample for the 14m/9 cycle-cover bound was established: exact ILP optima on ten in-class cyclically 4-edge-connected cubic graphs all lie strictly below 14m/9, and the proof route never materialized, so the lane exits cleanly with no claim.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Exact minimum-cycle-cover ILP requires full simple-cycle enumeration, which explodes beyond about 26 vertices (over ten thousand cycles), so larger graphs could only be bounded above by greedy covers; the universal proof direction was never reduced to lemmas; literature retrieval was unavailable (missing API key), so the study is self-contained computation plus deduction.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Exact minimum-cycle-cover ILP requires full simple-cycle enumeration, which explodes beyond about 26 vertices (over ten thousand cycles), so larger graphs could only be bounded above by greedy covers; the universal proof direction was never reduced to lemmas; literature retrieval was unavailable (missing API key), so the study is self-contained computation plus deduction.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.

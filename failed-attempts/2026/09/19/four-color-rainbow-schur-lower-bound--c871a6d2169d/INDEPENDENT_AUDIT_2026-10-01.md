# Independent scientific audit — SCOPE-20260919-c871a6d2169d

Audited at: 2026-10-01T13:18:12.002998Z

Disposition: **failed**

## Correctness — PASS

The ten-interval coloring and exact area calculation are correct. Independent recomputation of the inclusion-exclusion contributions gives 0, 0, 280, 648, 648, 220, 1086, 922, 1272, 454, summing to 5530 and hence limiting normalized density 553/1000. The Riemann-sum passage is valid because the indicator has discontinuities on finitely many lines.

## Originality — FAIL

A published SCOPE record from 17 September already proves the strictly stronger lower bound 16/27 for the identical four-colour rainbow-Schur extremal quantity. Since 16/27 is approximately 0.59259, it directly implies the assigned 553/1000 approximately 0.553 lower bound. The assigned record therefore cannot be original as a bound, regardless of its different interval construction.

### Equivalent formulations

Both statements concern the same extremal normalized rainbow-Schur density; the earlier one is stronger.

### Broader coverage

The earlier SCOPE lower bound dominates the assigned numerical claim.

### Exact database or table

This is decisive database coverage by a stronger result, not merely an unsuccessful novelty search.

### Claim versus prior implication

The assigned claim is a strict corollary of the stronger prior lower bound.

## Value — FAIL

The exact 553/1000 construction is mathematically correct, but as a lower-bound result it is strictly weaker than an already published 16/27 construction for the same invariant. The particular ten-interval value is not a natural exact invariant and no independent structural reason is supplied for needing this dominated construction.

## Sources inspected

- A 16/27 lower bound for four-colour rainbow Schur triples — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE007. COVERING_STRONGER: Proves liminf Lambda_{n,4} at least 16/27, strictly stronger than 553/1000.
- A somewhat sure note on an un-Schur problem — https://arxiv.org/abs/2609.18474. BACKGROUND: Provides the 10/21 baseline cited by the assigned record; it is not the decisive prior coverage because the earlier SCOPE record is stronger.

## Checked sources

- https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE007
- https://arxiv.org/abs/2609.18474
- https://doi.org/10.37236/13554
- Resultary semantic search

## Residual risks

- No material originality uncertainty remains because the stronger earlier lower bound is explicit and on the identical invariant.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The assigned construction remains valid evidence but is dominated by an earlier stronger lower bound.
- The complete original package must be preserved in the assigned failed-attempt archive.

# Independent mathematical audit — SCOPE-20260919-bedf83d63f82

Final disposition: **FAILED**.

## Correctness
**PASS** — The codimension-one projection-DPP calculation is correct: for a unit null vector z, omission j has probability z_j^2 and oblique loss 1/z_j^2; conditioning after each nested block gives the stated rare-event multiplier, and the nearly rank-d matrix converts this to the same limiting orthogonal CSS loss. The product limit follows by taking successive new-coordinate leverage scores sufficiently small. No finite experiment is needed for the theorem.

## Originality
**FAIL** — A published finding dated September 18, one day earlier, proves the same theorem for every stage partition: supremal factor product_i(k_i+1), actual orthogonal column-projection sharpness, one-shot factor d+1, singleton separation 2^d/(d+1), and the same rare-event mechanism. Its complete RESULT was inspected. The assigned September 19 claim is therefore fully covered, not merely similar.

### Equivalent formulations
The earlier theorem and assigned theorem are equivalent at the claim level despite different construction notation.

### Broader coverage
The earlier result is at least as broad in every scientific dimension relevant to the final claim.

### Exact database or table
The exact database hit is decisive prior coverage.

### Claim versus prior implication
This is direct prior implication, so unsuccessful external searches are irrelevant.

## Value
**FAIL** — The theorem is mathematically useful, but this record contributes no surviving scientific fact beyond the earlier stronger/equivalent published theorem. A different parametrization of the sharp family does not create separate value under the audit bar.

## Source inspections
- **Worst-case sharpness of multistage adaptive randomized pivoting** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-sharp-multistage-arp-error-products--77e11f8220ee): complete RESULT.md Assessment: EXACT_PRIOR_COVERAGE. Evidence: It proves arbitrary-partition product sharpness, orthogonal-CSS sharpness, one-shot d+1, and singleton 2^d/(d+1).
- **Incremental Column Subset Selection via Conditional Determinantal Point Processes** (https://arxiv.org/abs/2609.20556): full-text retrieval attempted through open and authorized routes; no verified PDF was obtained in this run Assessment: ACCESS_LIMITATION_NOT_DECISIVE. Evidence: The originality rejection does not depend on this inaccessible source because exact earlier published coverage is decisive.

## Residual risks
- No correctness defect was found; rejection is scientific duplication.
- The motivating primary paper could not be inspected in full during this run, but that access failure cannot override exact prior coverage.

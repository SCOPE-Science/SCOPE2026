# Independent mathematical audit — SCOPE-20260919-f92b8fbc7023

Final disposition: **FAILED**.

## Correctness
**PASS** — The singleton-stage construction is correct. In the codimension-one projection-DPP model, the final sample omits one coordinate and the omission weights are the squared coordinates of the null vector. The hierarchical Givens choice makes each newly introduced weight negligible relative to every old omission weight, so the conditional inverse-weight expectation gains a factor \(2+o(1)\) at each stage. At final rank, the Schur-complement identity gives normalized orthogonal CSS error \(1/(a_j+\sigma^2 b_j)\); because \(\sigma^2/\min_j a_j	o0\), this is uniformly \(a_j^{-1}(1+o(1))\). Hence the staged expectation tends to \(2^d\), while one-shot projection DPP has omission law \(a_j\) and expectation tending to \(d+1\).

## Originality
**FAIL** — A published September 18 result, 'Worst-case sharpness of multistage adaptive randomized pivoting', was read in full and strictly covers the assigned theorem. It proves sharpness of \(\prod_i(k_i+1)\) for every stage partition, proves the same sharpness for actual orthogonal CSS, and states the singleton-stage corollary \(2^d\) versus \(d+1\) on the same final subspace. The assigned distinct-leading-singular-value refinement removes a basis-degeneracy nuisance but does not change the covered scientific conclusion.

### Equivalent formulations
The formulations are mathematically identical after setting every stage size to one; distinct singular values only choose a unique basis representative.

### Broader coverage
The broader published result dominates every substantive conclusion of the assigned theorem.

### Exact database or table
This is theorem-level prior coverage rather than a finite database value; the exact published hit is decisive.

### Claim versus prior implication
The assigned final claim is a direct corollary of a stronger prior theorem.

## Value
**FAIL** — The mathematical phenomenon is worthwhile, but this September 19 record is a special-case rederivation of a stronger September 18 published theorem. The extra choice of distinct leading singular values is a robustness normalization, not an independently motivated new invariant or boundary. Under the shared bar, the record adds no separate scientific value.

## Source inspections
- **Worst-case sharpness of multistage adaptive randomized pivoting** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-sharp-multistage-arp-error-products--77e11f8220ee): complete RESULT.md. Assessment: STRICTLY_COVERS. Evidence: Theorems 1-2 prove every-stage-partition product sharpness and Section 'Sharpness for the actual orthogonal CSS error' proves the same orthogonal-error result; the singleton corollary is explicit.
- **Incremental Column Subset Selection via Conditional Determinantal Point Processes** (https://arxiv.org/abs/2609.20556): primary abstract / indexed source record. Assessment: SOURCE_CONTEXT. Evidence: The source introduces conditional-DPP incremental CSS and its product-form performance guarantees.

## Residual risks
- No correctness defect is asserted; rejection is exact prior scientific coverage.

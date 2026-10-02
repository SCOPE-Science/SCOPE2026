# Independent mathematical audit — 2026-10-01

## Final claim assessed

Hermite–Hellmann–Feynman extrapolation for constrained eigenvalue penalties

## Correctness — PASS

PASS. The simple constrained eigenvalue yields an analytic branch in inverse penalty by the Schur-complement implicit-function argument. Expanding the effective symmetric matrix gives the stated second coefficient. Hellmann-Feynman supplies derivatives at the penalty nodes, and the standard Hermite remainder gives order two-q from q value/derivative pairs; direct solution of the two-node confluent system gives the displayed fourth-order formula. The inspected numerical witness has a stable nonzero rho-to-the-fourth scaled error, confirming only the finite example and not substituting for the analytic proof.

## Originality — FAIL

FAIL. A published SCOPE record dated 18 September 2026, one day before this record, was inspected in full. It states the same simple-eigenvalue analytic inverse-penalty branch, the same explicit second coefficient, the same general Hermite–Hellmann–Feynman order O(rho^{-2p}) from p penalty levels, and exactly the same two-level formula 5 f(rho)+rho f'(rho)-4 f(2rho)+8 rho f'(2rho). It uses the same Wang–Xia penalty path and the same Schur-complement/Hermite mechanism. This is decisive prior coverage under the required implication-and-special-case standard; differences in example data and wording do not restore originality.

### equivalent_formulations

Searches: Resultary: constrained eigenvalue penalty Hellmann Feynman Hermite extrapolation Richardson derivative; 2026/9/18 SCOPE-hellmann-feynman-hermite-penalty-extrapolation--a3a87ccd7379

Evidence: The 18 September record gives the same analytic branch, second coefficient and derivative-enhanced extrapolation theorem.

Reasoning: The notation differs slightly but the matrix blocks, penalty path, interpolation nodes and asymptotic order are mathematically equivalent.

### broader_coverage

Searches: Full 18 September published RESULT.md; arXiv:2609.18538 Wang Xia

Evidence: The 18 September result covers arbitrary p penalty levels and therefore dominates the present q-level statement. Wang-Xia supplies the first-order penalty/Hellmann-Feynman background.

Reasoning: The earlier SCOPE theorem is at least as broad as the final claim.

### exact_database_or_table

Searches: Resultary semantic search for the exact two-level formula

Evidence: The exact same formula appears in the 18 September record.

Reasoning: This is decisive exact theorem coverage; no numerical database comparison is needed beyond locating the prior published record.

### claim_vs_prior_implication

Searches: 2026/9/18 published SCOPE full result versus assigned RESULT.md

Evidence: Every central claimed implication—analyticity, explicit second coefficient, O(rho^{-2p}) Hermite order, and the rho/2rho fourth-order estimator—is already stated and proved.

Reasoning: The assigned theorem is directly covered, not merely suggested or numerically matched.

## Scientific value — PASS

PASS. Derivative-assisted order doubling on a constrained-eigenvalue penalty path is mathematically useful and can reduce the penalty scale needed for a target scalar error. The record fails because the contribution is already published, not because the theorem lacks value.

## Source inspections

- **Hellmann–Feynman Hermite extrapolation for projected-Hessian penalty paths** — https://github.com/Resultary/2026/blob/main/2026/9/18/SCOPE-hellmann-feynman-hermite-penalty-extrapolation--a3a87ccd7379/RESULT.md. Material read: Complete published RESULT.md. Assessment: DECISIVE_PRIOR_COVERAGE. Evidence: It contains the same analytic branch, second coefficient, general order-doubling theorem and identical two-level fourth-order formula.
- **The Projected Hessian Quantification Theorem: Exact Duality For Constrained Eigenvalues** — https://arxiv.org/abs/2609.18538. Material read: Primary abstract and indexed theorem statement describing exact duality, first-order expansion and Hellmann-Feynman sensitivity. Assessment: BACKGROUND_SOURCE. Evidence: It supplies the underlying penalty path; the decisive coverage comes from the earlier 18 September published result.

## Limitations and residual risks

The theorem is correct only under the stated simple-eigenvalue/asymptotic assumptions and is rejected solely for prior coverage.

- None material to the originality disposition: the earlier published result directly covers the central theorem.

## Disposition

**failed**

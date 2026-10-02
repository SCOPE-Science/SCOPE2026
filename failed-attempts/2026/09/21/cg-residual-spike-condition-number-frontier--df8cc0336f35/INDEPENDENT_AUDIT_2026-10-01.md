# Mathematical audit — 2026-10-01

## Final claim assessed

Sharp condition-number frontier for CG residual spikes

## Correctness — PASS

PASS. The package proof is valid: the CG--Lanczos \(LDL^T\) factorization identifies the relevant residual multiplier in a trailing Schur complement, spectral enclosure is inherited through the inverse principal block, and the sharp two-by-two spectral-interval maximization yields the factor \((\kappa-1)/(2\sqrt{\kappa})\). An independent earlier proof based directly on CG orthogonality plus Kantorovich gives the same bound and equality family. The supplied two-dimensional equality cases and numerical artifact are consistent supporting evidence.

## Originality — FAIL

FAIL. A published 20 September 2026 result, one day earlier, states the same sharp all-step Euclidean residual factor, the same exact universal monotonicity threshold \(3+2\sqrt2\), the same endpoint-eigenspace first-step equality construction, and the same fixed-SPD-preconditioner consequence in the \(M^{-1}\) residual norm. It additionally gives a history-dependent refinement. This is direct prior coverage, not merely a similar parameter computation.


### equivalent_formulations

Searches: Resultary: conjugate gradient residual ratio condition number sharp all-step frontier monotonicity threshold; CG beta coefficient condition-number bound

Evidence: The complete 20 September record gives the identical per-step factor and threshold, using a different but equivalent CG identity/Kantorovich derivation.

Reasoning: Residual-ratio, \(\beta_k\), and condition-number-threshold formulations are equivalent here; the earlier theorem covers all of them.
### broader_coverage

Searches: https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-sharp-condition-threshold-monotone-cg-residuals--828a911cf7d9; Bouyouli--Meurant--Smoch--Sadok 2009

Evidence: The earlier published record is strictly at least as strong on the central frontier and includes a history refinement. The older 2009 result supplies a weaker all-step condition-number bound.

Reasoning: The 20 September result decisively dominates the assigned package's novelty claim.
### exact_database_or_table

Searches: Resultary semantic search for the exact \(3+2\sqrt2\) CG residual threshold

Evidence: The 20 September record is the top matching earlier theorem.

Reasoning: The exact threshold is directly published rather than inferred from a data table.
### claim_vs_prior_implication

Searches: complete 20 September CG threshold RESULT.md; assigned 21 September CG frontier RESULT.md

Evidence: The central boxed formulas and sharpness mechanism coincide.

Reasoning: The assigned result is directly covered and cannot become original through an alternative proof.

## Scientific value — PASS

PASS. The exact residual-spike frontier and threshold are useful structural facts for conjugate gradients. The scientific rejection is originality only.

## Source inspections

- **Sharp condition-number threshold for monotone exact-CG residuals** — https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-sharp-condition-threshold-monotone-cg-residuals--828a911cf7d9. Material read: Complete published RESULT.md. Assessment: DECISIVE_PRIOR_COVERAGE. Evidence: It states the identical all-step factor, universal threshold, equality construction and fixed-preconditioner extension.
- **New results on the convergence of the conjugate gradient method** — https://doi.org/10.1002/nla.618. Material read: Bibliographic/indexed result context as identified in the compared records. Assessment: OLDER_WEAKER_BOUND. Evidence: The prior literature gives a weaker condition-number-only residual ratio bound; it is not needed for the decisive failure because the 20 September result is exact.

## Limitations and residual risks

The theorem is correct in exact arithmetic for finite-dimensional real SPD systems, with the preconditioned statement in the \(M^{-1}\)-residual norm. It is rejected solely because an earlier published result already contains the same sharp all-step frontier and threshold.

- No access limitation affects the originality failure because the earlier published theorem directly states the same final claim.

## Disposition

**failed**

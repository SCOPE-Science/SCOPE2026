# Scientific audit — 2026-09-30

## Final claim assessed

For odd off-diagonally symmetric alternating sign matrices of order five, at parameter r equal to 1, the first-row-one generating polynomial has coefficients 3, 7, 9, 9, 4 on exponents one through five, so no monomial shift makes it reciprocal; order three is reciprocal.

## Correctness — PASS

An independent standard-library backtracking enumeration reproduced ASM counts 1,2,7,42,429; DSASM counts 1,2,5,16,67; OSASM counts 1,1,4,3,32; and the order-five first-row distribution 3,7,9,9,4. Since the support is exactly exponents 1 through 5, any reciprocal shift is forced to 6, which fails at both endpoint coefficient pairs.

## Originality — FAIL

Behrend--Fischer--Koutschan already give a Pfaffian formula for the full three-statistic DSASM generating function and explicitly relate the odd-order OSASM generating function to the coefficient of one diagonal nonzero entry. Their Section 8 states a Pfaffian identity for the full two-parameter OSASM generating function. The order-five polynomial is therefore a direct finite specialization of a stronger published generating-function formula, whether or not its five coefficients are printed as a row.

The comparison explicitly checked equivalent formulations, broader coverage, exact databases or tables, and implication from prior results. Structured searches, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-09-30.json`.

## Scientific value — FAIL

A five-coefficient specialization of an existing all-order Pfaffian generating function, followed by a support-symmetry check, is a routine extraction. The failure of the naive odd reciprocal analogy is mathematically understandable, but this particular n=5 computation is not a new structural lemma or motivated unknown invariant under the stated value bar.

## Disposition

**FAILED**. This assessment records the mathematical status of the claim and does not assert formal verification or external certification.

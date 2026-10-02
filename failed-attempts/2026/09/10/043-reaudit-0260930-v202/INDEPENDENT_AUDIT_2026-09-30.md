# Scientific audit — 2026-09-30

## Final claim assessed

Using the explicit constants in Evra--Kaufman Remark 3.4 at dimension three, together with the universal zero-dimensional coboundary-expansion cap beta at most 2, the resulting certificate has epsilon-bar at most one over 1,536,000 and mu at most the sixteenth power of one over 491,520,000, so that published closed-form route cannot certify a value of 0.08.

## Correctness — PASS

The primary paper states the constants in Remark 3.4. For any pure link with at least two vertices, choose a minimum-weight vertex singleton. The zero-dimensional coboundary denominator is its weight, while its coboundary is contained in the edge container, whose norm is at most twice the singleton norm by Lemma 2.3; hence beta is at most 2. Substitution at dimension three gives C0 equal to one over 960, C1 equal to 160, epsilon-bar equal to one over 1,536,000, and mu equal to the sixteenth power of one over 491,520,000. Independent exact rational arithmetic reproduced all values.

## Originality — FAIL

The claimed cap is mechanically implied by the same Evra--Kaufman paper: Definition 2.12 gives the zero-dimensional coboundary ratio, Lemma 2.3 gives the factor-two container bound, and Remark 3.4 gives the explicit constants. Combining these displayed statements and substituting dimension three is a direct corollary, even though the numerical 0.08 comparison is not written there.

The comparison explicitly checked equivalent formulations, broader coverage, exact databases or tables, and implication from prior results. Structured searches, source inspections, checked sources, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-09-30.json`.

## Scientific value — FAIL

The contribution is a method-specific constant substitution that only says one published, explicitly non-optimized certificate cannot reach an externally chosen threshold. It does not bound the true invariant and does not isolate a new structural obstruction. This is precisely a cheap feasibility check rather than a worthwhile mathematical result.

## Disposition

**FAILED**. This assessment records the mathematical status of the claim and does not assert formal verification or external certification.

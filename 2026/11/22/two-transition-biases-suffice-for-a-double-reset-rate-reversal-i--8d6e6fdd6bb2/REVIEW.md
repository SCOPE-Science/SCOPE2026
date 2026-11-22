# Review of the two-transition-bias resetting theorem

## Correctness

**PASS, self-review.** A renewal argument reduces ultimate exit probability to the ratio of two discounted first-exit generating functions. Tridiagonal cofactors yield the stated two explicit continuants and the rational reset-response formula. Positivity of the finite killed resolvents controls the denominator. Exact expansion and a positive-derivative upper bound establish derivative signs at three points for every bias in the entire asserted open/closed interval. The intermediate-value theorem and analyticity establish at least two strict interior extrema; an exact Sturm count establishes exactly two for the specified rational bias. The homogeneous case is supplied by explicitly cited published theorems with the same model. `CHECK.py` independently confirms the exact finite cofactor data, rational derivative polynomial and Sturm certificate. Its finite checks are supplementary, not substitutions for the continuous-parameter proof.

## Originality

**PASS against inspected evidence, not a claim of exhaustive priority.** The closest work, Newton and Vega Coso's *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting* (arXiv:2611.01756v1, Sections 4–7 and 10.3), proves the homogeneous response is monotone and supplies heterogeneous exact-time reversals, while explicitly leaving multiple interior reset-rate optima open. Existing heterogeneous examples establish that double reset-rate extrema are possible, so **bare existence is not new**. They do not imply the new two-valued complementary transition environment or the theorem valid uniformly over its one-parameter interval. The homogeneous multi-site analysis arXiv:2605.00657v1 and homogeneous critical-invariants analysis arXiv:2603.24803v1 do not cover heterogeneous transition-alphabet minimality. Equivalent-formulation, more-general-coverage and exact-example searches found no covering statement, but cannot rule out an obscure or unpublished equivalent construction.

## Value

**PASS.** The number of distinct sitewise transition probabilities is an intrinsic structural measure of environment complexity. Distinguishing homogeneous monotonicity from **a robust two-bias mechanism supporting two interior turning points** answers a natural, specifically motivated restriction of the published multiply switching-site problem. The claim is not merely a tuning of independent rational rates: all eleven transitions are tied to the same single parameter and its complement. The exact symbolic sign certificate makes the phenomenon reproducible and stable across a nontrivial interval. No stronger all-length extremum bound or minimum state-space threshold is asserted.

## Scope and residual limits

The stated bias interval is a sufficient range, not a maximal range; the all-parameter theorem guarantees at least two extrema and the two-root exact count is certified only for a rational member. Other inhomogeneous birth-death constructions with more extrema are not superseded. Possible unlocated equivalent theorems and independent validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.

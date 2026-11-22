# Scientific review

## Correctness

**PASS — self-review.** The unit-row Kaczmarz progress expansion gives the exact positive quantity \(\beta(2-\beta)r_i^2\). Choosing the least favorable pair of multiplicative residual errors maximizes the odds of sampling the weaker row, giving the displayed rational progress ratio. Its loss logarithmic derivative is strictly decreasing in the residual ratio and changes sign exactly once. The proof of the high-power limit uses fixed-ratio upper bounds and a compactness/subsequence lower bound; it does not replace an infinite argument by finite enumeration. The independent-row assumption realizes arbitrary residual pairs. The packaged standard-library checker returned 18,098 passing assertions, including exact-rational nonorthogonal Kaczmarz examples.

## Originality

**PASS — best-knowledge, qualified.** Full accessible material from Coleman, and full primary results for three strongly related published frozen-snapshot Kaczmarz findings, was compared by implication. Coleman addresses empirically measured selection/read delays but does not give the robust two-row conditional-progress ratio; the three related results accumulate stale corrections rather than use one fresh correction after noisy selection. Steinerberger's primary theorem and proof establish exact fresh-residual selection, while the available Gower et al. summary describes broader current-residual adaptive methods. No exact covering ratio, unique finite-exponent minimizer, or sharp large-power limit was located in the searched literature or mathematical records. This remains subject to an unindexed robust-importance-sampling equivalent or other earlier work. A search failure is not a priority certificate.

## Value

**PASS.** Multiplicative residual accuracy is a natural dimensionless control on noisy or asynchronously maintained row-selection scores. The sharp constant gives a calibrated lower bound on useful one-step progress for every pair of normalized independent equations, without assumptions on their mutual angle; the unique extremal imbalance identifies the genuinely adverse state, and the limiting \(e^{-4\varepsilon}\) factor describes the worst impact of growing aggressiveness. This is a conditional numerical reliability benchmark, not an asynchronous convergence guarantee.

## Closest literature and residual risks

Coleman (2026), arXiv:2607.08313; Steinerberger (2020), arXiv:2007.02910 (theorem and proof inspected); Gower et al. (2019), arXiv:1909.03604; published numerical findings on common-snapshot Kaczmarz collisions (2026). Generic likelihood-ratio perturbation theory and older specialist works not located by the searches might imply overlapping competitive bounds. Only one-step fresh-correction effects are assessed.

Self-review: passed. Independent audit: not yet performed.

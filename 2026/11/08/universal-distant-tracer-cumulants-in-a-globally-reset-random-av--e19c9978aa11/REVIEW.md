# Scientific review

## Correctness — PASS

The claim follows from four explicit steps: a convex-combination backward-ancestor representation for the random average process; an annealed Poisson nearest-neighbor dual with polynomial bounds on moments of every order; an ancestor-exit tail bound that makes widely separated graphical windows jointly independent at a fixed reset-free age; and mixing these products over the one shared exponential last-reset age. The partition formula for connected cumulants then yields the stated all-order coefficient. The bound integrates for every positive resetting rate, so the proof does not silently assume a rate larger than a jump intensity. The finite-time second-order formula independently agrees with Eq. (42) of Santra–Singh. Exact symbolic checks through order ten corroborate the age-cumulant algebra. Numerical tail checks are diagnostics, not convergence proofs.

## Originality — PASS, with publication-priority risk

Santra–Singh (arXiv:2311.04097, Sections IV B and VI) derive the exact two-tracer covariance and acknowledge higher moments as an open problem, but do not state a higher connected spatial cumulant or a conditional product law for interacting RAP tracers. Rajesh–Majumdar (arXiv:cond-mat/0104430) treats reset-free two-point correlations. Biroli et al. (arXiv:2211.00563) obtain a resetting-age mixture of product Brownian laws for independent particles; direct factorization fails for an interacting RAP at fixed age and must be established here using the graphical truncation bound. Primary-literature comparisons and mathematical-result searches did not surface equivalent or stronger coverage. A general theorem on marked Poisson graphical mixing combined with common resetting might subsume this as a corollary, and inaccessible or unindexed literature cannot be ruled out. No assertion of formal priority or independent originality certification is made.

## Mathematical value — PASS

The preceding study identifies a persistent second-order correlation but leaves higher moments open. A single nonzero covariance cannot determine a third- or fourth-order connected correlation, much less all fixed orders. The theorem shows a factorial hierarchy of genuinely long-range, non-Gaussian connected tracer statistics, with exact finite-time age formulas and independence from all higher moments of the random-gap-fraction law. The mechanism distinguishes shared global reset-clock fluctuations from the unknown local many-particle dynamics, making it possible to predict long-distance multi-point responses without solving the one-tracer higher-moment problem. The result is restricted to one insertion per distant tracer, fixed order, and the specified Poisson reset model.

## Closest literature and limitations

The exact second-order plateau and renewal model are prior results, not new contributions. The new proof concerns all higher distinct-tracer cumulants and the full limiting fixed-order mixture law. It does not compute finite-distance correlations or high single-tracer moments, does not supply uniform estimates when order grows, and does not treat non-Poisson or partial resets. Independent publication-priority checking remains advisable.

Self-review: passed. Independent audit: not yet performed.

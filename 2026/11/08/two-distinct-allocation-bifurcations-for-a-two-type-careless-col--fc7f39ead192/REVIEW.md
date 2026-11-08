# Self-review: Two distinct allocation bifurcations for a two-type careless collector

## Correctness — PASS

The finite post-loss transition matrix is explicitly stated and each row sums to one. Stationary marginal equations and the exact three-transient-state hitting linear system give the two rational formulas for the same chain. Parameterization by the sum and product of survival probabilities covers every allocation, including boundary allocations. Two strictly monotone derivative numerators prove global uniqueness and classify all four threshold crossings; the exact budget-half witness follows by rational substitution. A fresh standalone checker solves the actual Markov systems without using those formulas as the solver and passed 20,031 assertions/diagnostics. The finite mesh is not an exhaustive proof; the analytic monotonicity and polynomial-root argument provides that proof.

## Originality — PASS, subject to historical limitations

Cruciani and Dudeja's February 2026 source defines post-loss careless coupon collection only with a common loss rate, and explicitly lists type-dependent rates as future research. Long's May 2026 paper treats the same post-loss transition at common rate, plus an unlike reset-button model. Kleiner's recent fragile collector has hazards only for unseen types and makes discovered coupons permanently safe. The closest indexed coupon rate result concerns heterogeneous sampling for a global reset mechanism, not these loss parameters. The previously established homogeneous stationary specialization cannot imply optimization on the heterogeneity segment. The exact double phase diagram was not found, though broader Markov reliability and cache optimization literature remains a priority risk; this is a best-knowledge search, not an independent novelty certificate.

## Mathematical value — PASS

The two-type instance is the first nontrivial heterogeneous version of a motivated new stochastic process. It answers two different and operationally natural optimization questions completely, finds analytically different phase-transition budgets, and proves that maximizing stationary availability can worsen expected time to first complete collection. The strict rational witness at budget one-half and the full continuum of regimes supply more than a textbook single-point calculation.

## Scope and limitations

Two labels, independent post-draw global losses, uniform acquisitions and total loss budget strictly between zero and one. No general-alphabet optimum or stochastic domination is claimed. Independent mathematical verification and definitive historical-priority assessment are still outstanding. Relevant primary sources are arXiv:2602.20705, arXiv:2605.14511 and doi:10.3390/math14203729.

Self-review: passed. Independent audit: not yet performed.

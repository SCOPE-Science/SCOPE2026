# Scientific review of a drift-controlled hierarchy of collective extremes

## Correctness — PASS

The stationary law follows from coupling at the first common reset and the exact exponential backward-age representation. Conditional Gaussian independence yields the renewal integral for any fixed particle count. Its unique interior saddle is strictly separated from all boundaries, including the large-age Gaussian-nonrare region when logarithmic drift is positive. Uniform Mills estimates and Laplace's method reconstruct the exact polynomial prefactor and exponential rate. Inverting the one-dimensional variance-mean Gaussian mixture yields an independently checkable exact marginal survival function. Algebra establishes the strict rate order and all three iterated size regimes. The supplied numerical checker passed 128 assertions; finite calculations are diagnostics only, and every infinite claim is supported by explicit proof. Risks: the claim is not uniform in particle number or in extreme positive drift, and does not provide finite-threshold error bounds.

## Originality — PASS, qualified

The 2021 reset-geometric-Brownian paper states the univariate stationary Pareto exponent, not correlated simultaneous extremes from a *shared* reset clock. The Opitz elliptical Laplace field and the broader random-scale paper address centered exponential Gaussian scales or independent radial multipliers, rather than an age-dependent Gaussian **mean and variance**. The two closest published shared-reset Brownian records explicitly assume zero drift and cover the neutral-log-drift benchmark, which is excluded from the novelty claim. A literature and semantic-database search found no equivalent nonzero-drift, arbitrary-finite-population sharp prefactor plus drift-sign hierarchy. Novelty is not guaranteed by search absence: broader multivariate asymmetric Laplace theory could imply parts of the result without the same physical language, and independent publication-priority assessment remains necessary.

## Mathematical value — PASS

The precisely motivated invariant is the probability of collective large positive displacements at equal individual quantile levels, an extreme-risk observable not fixed by one-particle Pareto laws. The result gives the sharp full equivalent, not just the marginal rate; the exact drift-sign trichotomy separates saturation, square-root growth and linear growth as particle count increases. Independent versus shared catastrophes have identical marginals yet strictly different joint upper-tail exponents for every fixed number of particles. This provides a structural and physically interpretable collective-fluctuation classification. Limitations include the iterated nature of the size limit, the identical-parameter assumption and lack of correlated-noise or partial-reset coverage.

## Closest literature and remaining risk

Stojkoski et al. (arXiv:2104.01571) provide the marginal reset-geometric-Brownian formulas. Opitz (arXiv:1507.02537) and Engelke et al. (arXiv:1803.04221) develop adjacent general extreme-value frameworks. The closest publicly available Brownian-resetting results treat zero-drift Gaussian positions under partial and shared reset shocks; their stated rate formulas do not incorporate the multiplicative growth drift or the derived polynomial equivalent. An implicit special-case derivation from general multivariate asymmetric Laplace asymptotics remains the leading originality risk.

Self-review: passed. Independent audit: not yet performed.

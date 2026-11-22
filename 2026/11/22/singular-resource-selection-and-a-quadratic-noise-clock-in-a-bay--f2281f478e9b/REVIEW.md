# Scientific review: singular resource selection and a quadratic noise clock

## Correctness — PASS

The claim uses the exact four-phenotype replicator and resource equations, with strictly positive initial phenotypes and an interior resource. The conditioned action-payoff differences give three uniformly positive growth rates for the phenotype \(HL\) relative to competitors. For each finite sensory noise this establishes exponential phenotype selection globally, not merely stability of a listed equilibrium. The truncated Gaussian perception probability is strictly decreasing in resource abundance and crosses the harvest balance once. Uniform exponential phenotype selection and scalar inward comparison imply convergence to the unique interior resource equilibrium for every eligible initial state.

The high-noise Taylor expansion is uniform through one derivative and yields the selected abundance and the leading slow eigenvalue. In the explicit constant-gap payoff slice, exact logistic solutions at infinite noise give the stated logit-memory law. Integrable fast transients and a uniform \(O(\sigma^{-4})\) perception expansion establish the stretched-time cubic limiting dynamics away from the initial time boundary layer. The standalone numerical checker verifies complementary algebra and illustrative parameter values. It is not used as evidence for infinite-dimensional or infinite-time quantifiers.

## Originality — PASS, with historical priority risk

The motivating paper [1] gives the continuous-resource Gaussian-perception equations and stationary cases, including the noise-dependent partially depleted regime and its formal disappearance as noise diverges. The current claim does not relabel those fixed points as new. Its separate contributions are a quantified global-interior convergence statement, the selected high-noise limit \((1+c)/3\), exact noncommuting time/noise limits, and a full slow-time crossover at the paper's own critical feedback balance.

The closest distinct literature consists of noisy information channels in discrete stochastic resource games [2] and replicator feedback with no such channel [3]. They do not supply the identical truncated-Gaussian four-phenotype limit on the inspected material. The novelty conclusion is bounded by accessible sources and explicit statement-level comparisons, not by keyword absence. An equivalent asymptotic calculation elsewhere cannot be categorically ruled out.

## Value — PASS

The initiating model's high-noise phase diagram appears to squeeze the partially depleted state away at one precisely distinguished harvest-balance parameter. The theorem resolves what finite but arbitrarily large noise actually selects, why loss of the partial-resource region at exactly infinite noise is singular, and how the environmental response slows on an explicit quadratic clock. The transient resource memory and deterministic crossover can be tested against numerical implementations using the exact equations. The threshold and noise clock are motivated by the original model's phase boundary, not a gratuitous numerical parameter slice.

## Closest literature and limitations

[1] A. Patra, J. Das Bairagya and S. Chakraborty, *Bayesian eco-evolutionary game dynamics*, Phys. Rev. E **111**, 044401 (2025); https://doi.org/10.1103/PhysRevE.111.044401 ; open full preprint https://arxiv.org/abs/2504.02399. Inspected its model derivation, equilibria, phase diagram, and strong-noise discussion.

[2] S. S. Mondal and S. Chakraborty, *Noisy information channel mediated prevention of the tragedy of the commons* (2024), https://arxiv.org/abs/2408.08744. This concerns a stochastically fluctuating two-state repeated game; the accessible introduction was read, not every appendix.

[3] J. S. Weitz et al., *An oscillating tragedy of the commons in replicator dynamics with game-environment feedback* (2016), https://doi.org/10.1073/pnas.1604096113. The available abstract establishes a different no-channel formulation; it is not a full-text exclusion certificate.

Scope is deterministic, infinite-population, positive initial phenotype support and interior resource abundance. Noncommutation and the crossover are demonstrated in an explicit constant-gap payoff slice with independent initial phenotype coordinates. No empirical calibration, finite-population survival, or non-Gaussian extension is claimed. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.

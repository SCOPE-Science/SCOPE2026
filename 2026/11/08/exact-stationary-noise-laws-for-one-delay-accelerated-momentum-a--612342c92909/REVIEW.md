# Review

## Correctness

**PASS, self-review.** The one-delay cubic coefficients were independently obtained from the literal update, matched to equation (81) of the motivating full text, and the published Proposition 3.19 proves their Schur stability for every positive condition number. Independent Yule--Walker equations yield the stationary rational formula; direct expansion produces the slow-mode \(2q^{-3}\) and fast-mode \(16/(7q)\) factors. The independently optimized delayed-GD comparator and its stationary variance follow from its characteristic quadratic and its separate Yule--Walker equations. The standalone checker passed 450 numerical/simulation and 9 exact-rational assertions. Risk: finite checks do not establish the continuum theorem; its justification is analytic and the stated published root-location result.

## Originality

**PASS, subject to historical priority.** The closest source, Gürbüzbalaban et al., treats exact deterministic spectral rates, not the stationary additive-noise covariance of its optimized one-delay method. The general classical phenomenon (accelerated two-state momentum amplifying noise by a factor of order \(\sqrt\kappa\)) is already known and explicitly credited to Mohammadi et al. That earlier paper uses second-order (two-state, undelayed) updates, not the distinct cubic delayed recurrence or rate-optimized delayed-GD comparison; it does not imply the numerical constants by its stated results. Stich and Karimireddy's delayed SGD bounds concern different stochastic asymptotics, not the exact cubic stationary noise law. Relevant published-finding corpus searches and accessible historical claims found no direct equivalent. Residual risk: a less-indexed source might treat exact constant-parameter delayed three-state covariance; novelty is claimed only for this method-specific exact law and sharp comparison, not for generic noise amplification.

## Value

**PASS.** A current deterministic delay-resistant accelerator claims accelerated condition-number dependence; the exact stationary error law supplies a quantitatively different selection criterion under persistent unbiased gradient noise. The divergence is unbounded with conditioning, and the comparison is normalized by independently rate-optimal *delayed* gradient descent, rather than by a delay-free baseline. The result motivates practical stochastic parameter tuning and separates deterministic rate from a relevant stochastic cost. Its narrow two-mode witness is explicitly stated, not generalized to all stochastic accelerators.

Self-review: passed. Independent audit: not yet performed.

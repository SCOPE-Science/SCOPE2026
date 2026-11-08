# Self-review

## Correctness — PASS

The exact source System I is specified for every integer \(1<M<N\), positive payoff and time-scale parameters, and exactly critical linear feedback. In logit risk coordinates, the binomial factor satisfies the exact logarithmic derivative identity needed to obtain the scalar inhomogeneous equation \(\dot Y=(aY-q\sigma(s))\dot s\); differentiating the integrating-factor formula gives zero without hidden boundary assumptions. A positive-definite Hessian at the sole interior fixed point yields a regular closed annulus, and the purely imaginary Jacobian gives the limiting period. The in-package verifier supplies 75 independent symbolic consistency assertions across 25 integer combinations and a high-accuracy sample trajectory check. Finite testing is corroborative rather than a proof of the general assertion.

## Originality — PASS (best-knowledge)

Closest source: Liu–Chen–Szolnoki, *eLife* 2023 (original preprint 2022-12-20), System I and Appendix 1. The full open-access original and its arXiv version were read. They identify the linear threshold and oscillatory regimes, and Appendix 1 uses an approximately zero negative numerical first Lyapunov coefficient to argue for a supercritical stable cycle. Neither text sets out the exact integrating-factor first integral or its nonisolated annulus consequence. Weitz et al. 2016 develops the broader evolutionary game–environment context but does not contain this exact binomial-payoff formula. The 2025 Zhang–Yang–Han–Xia threshold-public-goods study concerns a related framework, but only its abstract was accessible; an equivalent full-text result is a residual risk. Semantic research searches and historical-claim comparison did not identify a covering statement, which is not a proof of novelty.

## Value — PASS

The distinction between a family of neutral periodic states and an attracting isolated cycle changes the interpretation of the critical cooperation–risk regime: arbitrarily close initial conditions can maintain different oscillation amplitudes, and no cycle there selects a unique amplitude through attraction. The conservation law is exact for all group sizes and parameter choices satisfying the model conditions, and yields a closed small-oscillation time scale. This is a motivated structural classification of the source's highlighted critical regime, not a cosmetic reparametrization of a known conserved energy.

## Scientific and access limitations

The periodic-annulus theorem is local despite the first integral being globally defined on the interior. It does not establish global periodicity, persistence of cycles under off-critical perturbations, or a stochastic-population result. Possible equivalent treatments in inaccessible articles or unindexed literature are not excluded. The original text's numerical coefficient is compared as scientific context, not used as an exact negative certificate.

Self-review: passed. Independent audit: not yet performed.

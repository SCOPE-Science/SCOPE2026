# Scientific review

## Correctness — PASS

The central formula follows from two exact first-order asymptotics: the all-target-corner mixture event has leading coefficient \(\pi_s m^{-1/\theta}\), and the event with one coordinate omitted has leading coefficient \((\pi_s+\pi_{s\oplus e_i})(m-1)^{-1/\theta}\). The negligible off-target events are established using exact bivariate Clayton lower/upper events and bounded bivariate density near the upper corner. The denominator is positive for all permitted parameters. The square/edge conditions are necessary by shared denominators and sufficient by the coordinate-flip path construction; connectivity proves uniqueness. Exact-rational checks corroborate, but do not substitute for, the proof.

## Originality — PASS, qualified

The 19 March 2024 original posting treats bivariate four-rotation mixtures; the 10 February 2025 revision explicitly extends the construction to multivariate \(2^m\) rotations. The multivariate revision introduces the same all-other-extremes conditional coefficient but reports a linear component-mixture expression. This is not valid for the stated conditioning when \(m\ge3\): in the uniform eight-rotation mixture at \(m=3\) and \(\theta=1\), that linear calculation gives \(1/12\), while the actual conditional limit is \(1/3\). The present result supplies the correctly normalized coefficient and an exact intrinsic compatibility and recovery theorem, which the 2025 revision does not supply. The distinction arises because conditioning event probabilities vary with mixture components. General tail correlation matrix realization results use pairwise, not these oriented higher-order conditional, coefficients. The accessible literature and related findings did not reveal dominating prior coverage. Specialized unindexed results could remain; historical priority is not certified.

## Value — PASS

The theorem converts a high-dimensional extremal-dependence model into an explicit, testable population-level identification problem. It proves that the shared dependence parameter and all rotation weights can be recovered from conditional rare-event behavior alone. It also gives sharp algebraic incompatibility constraints: locally plausible edge values can fail globally, as the constructive three-dimensional example shows. This is useful for model validation, tail-based calibration, and identifying observational restrictions before inference. No estimator-rate or finite-sample inference claim is made.

## Closest literature and limits

The nearest source is Pan, Nieto-Barajas and Craiu, arXiv:2403.12789, originally bivariate (2024) and multivariate in its third revision (2025). Pairwise tail-matrix realization results of Fiebig–Strokorb–Schlather and Shyamalkumar–Tao are broader in a different observable and do not imply the particular conditional inverse theorem without additional analysis. Scope is strictly dimension at least three, positive weights, one shared positive Clayton parameter, and the specified equal-width extreme bands. Empirical stability and heterogeneous component parameters remain outside the claim.

Self-review: passed. Independent audit: not yet performed.

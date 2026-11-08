# Scientific review

## Correctness — PASS

The theorem is for exact linear drift and free-diffusion substeps with fresh Gaussian noise and independent global Bernoulli order choices. Every eigenmode contracts with factor \(e^{-h\lambda_i}\), ensuring the unique stationary series and legitimate exchange of expectations. Conditional Gaussian covariance reduces to an almost-surely convergent Bernoulli series. The displayed covariance, minimax, fourth-cumulant and cross-square formulas follow by summing geometric series. Strict monotonicity of \(f\) establishes the unique minimax probability and the exact covariance-calibration condition. Positive fourth cumulant excludes a Gaussian stationary law for every interior probability; endpoint probabilities give Gaussian laws with incorrect covariance. The standalone verifier separately recomputes one- and two-coordinate moment recursions in exact rational arithmetic (including a finite-prefix geometric tail identity). It passed 20,450 assertions. All-domain claims rely on the analytic argument, not the finite grid.

## Originality — PASS, qualified

The closest algorithmic comparison is Li, Wang and Wang (arXiv:2510.07676v1), whose random Lie–Trotter Langevin algorithm fixes the two orderings to equal probability and proves ergodicity and error estimates, not the all-spectrum minimax covariance calibration and non-Gaussian stationary moment identities here. Leimkuhler and Sachs (arXiv:2012.04245v1, sections 2 and 3.2.1) instead study fixed symmetric splitting and exact Gaussian quadratic marginals for a different scheme. Cho, Berry and Hsieh (arXiv:2210.11281v1) randomize product formulas for Hamiltonian quantum simulation, without an invariant Gaussian diffusion law. Generic Gaussian AR(1) moment formulas and the elementary midrange solution to scalar minimax approximation are background tools, not independently claimed discoveries; the combined sampling-design classification and its unavoidable fourth-order dependence are the claimed distinction. Searches for weighted random-order Ornstein–Uhlenbeck covariance calibration, Gaussian-mixture kurtosis and stochastic splitting did not find an exact covering published result, but such a result could exist outside the inspected materials. This is not independent publication-priority certification.

## Value — PASS

A random-order Langevin sampler can have a correct stationary covariance and still fail to sample a Gaussian law. The exact all-spectrum minimax parameter is a concrete, implementable diagnostic for anisotropic Gaussian benchmarks, while the positive cross-mode square dependence reveals a distortion that a covariance-only check would miss. The result completes the natural family of all independent Bernoulli order probabilities for exact subflows and any SPD quadratic target. It neither claims a runtime gain nor optimizes Wasserstein distance or higher-order errors.

## Closest literature and limitations

- Leimkuhler and Sachs, *Efficient Numerical Algorithms for the Generalized Langevin Equation*, arXiv:2012.04245v1 (2020-12-08), https://arxiv.org/html/2012.04245v1 .
- Cho, Berry and Hsieh, *Doubling the order of approximation via the randomized product formula*, arXiv:2210.11281v1 (2022-10-20), https://arxiv.org/abs/2210.11281 .
- Li, Wang and Wang, *Ergodicity and error estimate of laws for a random splitting Langevin Monte Carlo*, arXiv:2510.07676v1 (2025-10-09), https://arxiv.org/abs/2510.07676 .

The formulas assume a common fresh Bernoulli ordering for all eigenmodes, isotropic Brownian noise and exact drift and diffusion subflows; they do not cover state-dependent or correlated choices or arbitrary nonlinear potentials. Independent expert validation and a broader specialist precedence check have not been performed.

Self-review: passed. Independent audit: not yet performed.

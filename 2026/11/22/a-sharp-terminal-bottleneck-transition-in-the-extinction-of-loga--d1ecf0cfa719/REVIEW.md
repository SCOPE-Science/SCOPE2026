# Review of logarithmic Ising-domain extinction theorem

## Correctness

PASS. For each fixed minus domain the initial and intermediate lengths have two permitted end flips, hence independent exponential waiting times of rate two, while the final isolated spin has rate one. The block decomposition and its exact Laplace transform follow by independent Poisson clocks and the strong Markov property. The large-deviation rate is derived from the joint rate \(j(g)+e\), and the constrained minimizer is unique in each regime. Independence and exponential growth in block count yield the extreme-time law. Exponential compactness and a strict rate gap yield the winning block's microscopic mechanism. The optional discrete-update corollary follows from independent Poissonization gaps and an explicit mean-square estimate. The reproducible checker passed 76 finite-state, asymptotic and sampling checks, with no appeal to simulations as an infinite proof.

## Originality

PASS on available evidence, with substantive residual risk. The motivating 2026 kinetic-sector paper supplies the exact finite-block waiting-time transform, two mean absorption-time examples and the related first-step recursion. It does not state the logarithmically growing equal-domain extreme-time transition or the conditional last-domain bottleneck. A separate earlier analysis has the full exact arbitrary-domain absorption CDF, including the gamma-plus-exponential independent factors. That exact CDF is prior work, not a newly asserted result. Its Gumbel and Gaussian laws concern the extreme fastest/slowest initial arrangements, not exponentially many identical logarithmically growing domains; the present new claim is the sharp asymptotic threshold and the conditional erosion-versus-terminal split of the selected last domain. Another prior claim treats Bernoulli-prepared random domains and their Gumbel limit. Targeted indexed searches for the source, aliases, rate function and competing extremes did not identify equivalent coverage. General Cramér and extreme-value principles are not claimed as new. The earlier exact arbitrary-domain formula certainly provides the finite-size input and could imply the present scalar asymptotic after further large-deviation analysis; this is a substantial prior-coverage risk for the scalar consequence. The conditional winning-domain mechanism and its rate-transition proof are not directly covered by the accessible claims, although an unindexed equivalent remains a risk.

## Value

PASS. In the physically natural weak-seeding regime where the gap between permanent nucleation seeds grows logarithmically with system size, the dominant mechanism changes at the explicit constant \(1-\log2\), with a continuously differentiable but not twice differentiable speed law. The result distinguishes a macroscopic single-spin bottleneck from a collective erosion delay, rather than merely calculating a known expectation or reparameterizing an exact finite formula. It identifies when different microscopic interventions should matter for slow ordering. The theorem is restricted to irreversible one-dimensional equal-domain preparations; robustness beyond that class remains open.

## Closest literature and limitations

Cao, Jiang and Zhang, arXiv:2610.36829v1, Section IV.B and Appendix C, is the closest primary paper. Its finite-block generating functions are explicitly credited. General Cramér-type tail theory underpins the proof. Prior coverage is not ruled out by a failed search; priority assessment remains qualified. A self-review is not independent validation.

Self-review: passed. Independent audit: not yet performed.

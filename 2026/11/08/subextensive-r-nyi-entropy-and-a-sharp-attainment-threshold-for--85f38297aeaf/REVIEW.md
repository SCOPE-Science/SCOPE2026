# Scientific review: common-clock quantum renewal purity

## Correctness — PASS
The exact stationary equilibrium-age distribution and the tensor-product overlap lead to the binomial Fourier identity. For arbitrary integrable positive reset times, the age Fourier coefficients are uniformly of order \(1/|k|\). Dominated convergence and Parseval then establish the many-qubit \(N^{-1/2}\) law and its exact prefactor. The sharp fixed-mean attainment boundary uses the equality case of the triangle inequality on the unit circle and an explicitly normalized two-point approximating sequence. The Poisson hyperbolic-cotangent coefficient follows from the classical partial-fraction expansion. The checker verifies 51 finite assertions; it cannot prove the general theorem.

## Originality — PASS, with stated priority risk
Magoni et al., https://arxiv.org/abs/2202.12655, already establish the exact physical global-reset Rabi-spin model and its correlation mechanism. Sevilla and Valdés-Hernández, https://arxiv.org/html/2209.05643v1, already give a more general stationary purity formula: their Eq. (42) implies the displayed finite-\(N\) binomial purity as a specialization. No novelty is claimed for that identity or for basic renewal averaging. Wald et al., https://arxiv.org/html/2410.11497v3, analyze discrete-time resetting and few-qubit resonance. The assessed additions are the quantitative full-register \(\sqrt N\) law, exact clock-phase \(L^2\) coefficient, and mean-budget attainable/unattainable optimizer boundary. An unindexed derivation of these extra consequences remains possible.

## Mathematical value — PASS
A shared reset clock creates classical/quantum-discord correlations without interactions and determines the effective dimension of a many-spin stationary ensemble. A complete, all-mean optimization result shows when perfect period-phase mixing is actually realizable rather than merely approximable. The threshold distinguishes feasible reset schedules from singular limiting protocols, which is relevant when resets have a fixed mean cost.

## Scope and limitations
The stationary equilibrium-renewal ensemble need not be the pointwise-time limit from a synchronized initial state for deterministic/lattice clocks. The lower-mean infimum construction requires arbitrarily short positive intervals. The ensemble is separable; its Rényi entropy measures mixture, not entanglement. The broad spectral-purity formula is prior art; the new contribution is confined to the all-\(N\) asymptotic and fixed-mean classification. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.

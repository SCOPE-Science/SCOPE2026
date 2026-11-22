# Self-review

## Correctness — PASS
The stationary resolvent follows from regenerative Poisson resets; tensorized depolarization gives a single GHZ coherence and symmetric Hamming-weight diagonal populations. The published exact X-state genuine-multipartite concurrence formula, checked against its original proof, yields the stated rational threshold. Strict stochastic monotonicity supplies a unique root, while a uniform Laplace expansion proves the two-term \(n\)-asymptotic. The standalone checker passed exact stationary generator and normalization identities and independent numerical quadrature and roots. Residual risk: the uniform error estimate assumes fixed homogeneous noise and reset rates with the critical rate scaling proportionally to qubit number, as stated.

## Originality — PASS, qualified
The closest primary results separately provide the exact X-state concurrence theorem [1], non-reset depolarizing GHZ scaling [2], and the Poisson reset resolvent for closed quantum evolution [3]. The published amplitude-damping GHZ protocol [4] does not imply the depolarizing reset-age binomial transform or its linear-size threshold. An exact restatement or stronger general theorem was not found after searches for joint GHZ Poisson depolarizing resets, biseparability, and asymptotic thresholds. However, it remains possible that more general open-system reset methods implicitly cover portions; external publication-priority assessment is not implied.

## Mathematical value — PASS
The boundary is an exact, parameter-complete maintenance criterion for a standard multipartite quantum resource, not merely another example of matrix evaluation. The first two large-size coefficients quantify an extensive reset overhead from isotropic local noise and distinguish its behavior from amplitude-damping reset scenarios. This answers a motivated question about how expensive repeated entangled-state restoration becomes as the number of qubits grows. The protocol assumes an entangled global reset resource, so it does not claim creation of entanglement from local separable operations.

## References and limits
[1] https://arxiv.org/abs/1208.2706 — Sections II and VI, exact X-state GM concurrence.
[2] https://arxiv.org/abs/0812.4203 — GHZ entanglement under local decoherence without renewal restoration.
[3] https://arxiv.org/abs/2307.07485 — Section II reset-time Laplace average; closed unitary model.
[4] https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-all-size-entanglement-death-thresholds-for-amplitude-damped-ghz--f0bf2204cc39 — amplitude-damping with partial NOT controls, different channel.

Self-review: passed. Independent audit: not yet performed.

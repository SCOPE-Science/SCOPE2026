# Scientific review: correlated-label inverse-riffle inversion transition

## Correctness

**PASS.** The stable-sort inversion identity is exact, and the stationary Markov-spin correlations recover the mean and zero atom. The triangular-array martingale decomposition has deterministic conditional variance, uniformly bounded normalized jumps when \(n(1-p_n)\to\infty\), and an explicit \(L^2\) remainder of smaller order. The quadratic-spin contribution is negligible by its second-moment bound. Independent Bernoulli switches give both the finite-rate Poisson process limit and the uniform single-switch limit. The standalone exact checker passed 8,284 rational assertions; finite simulations are diagnostics only.

## Originality

**PASS under the documented accessible-source comparison, with historical-priority residual risk.** Jiang's Definition 2.4 specifies the process and his results concern multi-step mixing, not the three one-step inversion regimes. Jonasson–Morris study fixed persistence and mixing rather than the triangular-array inversion limit. Işlak proves a shuffle-inversion CLT for independent marks and therefore includes the special \(p_n=0\) case only; his iid hypotheses do not imply the high-adhesion Poisson/rare regimes. No directly covering statement was found among actual indexed searches or the accessible earlier claim ledger. The earlier Wager dissertation cited by Jonasson–Morris could not be inspected and remains a priority risk; absence of a search match is not proof of first discovery.

## Value

**PASS.** Inversion number measures the macroscopic disorder introduced by one adhesive shuffle. The natural dimensionless parameter \(n(1-p_n)\) is the expected switch-count scale. A change in this parameter causes a genuine qualitative transition: Gaussian behavior, a positive limiting atom and stochastic inversion area, and an asymptotically vanishing event with a nondegenerate conditional shape. This is an interpretable structural classification for the model, rather than an arbitrary finite statistic.

## Closest literature and limitations

The exact inversion-word reduction extends Işlak's independent-label viewpoint to a Markov label chain, and the Markov inverse-riffle construction itself is due to prior work. These facts are acknowledged; no novelty is claimed for either. The result is not a mixing-time theorem or a statement of independent external validation. See RESULT.md and AUDIT.json for exact boundaries and source comparisons.

Self-review: passed. Independent audit: not yet performed.

# Scientific review: unique Poisson-frequency optimum of Gaussian endpoint divergence

## Correctness — PASS

For every real \(0<q<1\), \(k>0\), the no-reset Gaussian covariance is exact, the Jeffreys divergence is \((u_q-q)^2/(2qu_q)\), and exponential renewal averaging yields the stated integral. The second time derivative of the single-cycle divergence changes sign exactly once, and the ratio of positive to negative Laplace derivative contributions is strictly increasing; the endpoint derivative signs therefore give exactly one frequency optimum. A uniform multiplicative bound proves the near-equal-width limit. The narrow-width limit uses an exact alternate transform, dominated convergence, and uniformity on compact scaled-frequency intervals. The numerical verifier independently checks algebra and representative parameters but is not a substitute for the analytic quantifiers.

## Originality — PASS, qualified

The closest 2026 primary publication gives the Gaussian endpoint-divergence expression, and approximate Poisson rates under a teleportation constraint, but does not establish a unique optimum for every finite \(q\) or the two sharp asymptotic laws; its high-frequency extrapolation is explicitly excluded. Earlier entropy-production and erasure-work papers optimize different thermodynamic observables. Related mathematical statements address an optimal renewal waiting distribution *at fixed mean*, a reversal between periodic and Poisson waiting, or multiscale two-peak examples. None of those claims implies uniqueness of the Poisson rate optimizer in one dimension or its sharp asymptotics. Residual risk: an unlocated general variation-diminishing theorem may subsume the uniqueness proof, and unpublished extensions of the closest primary paper may exist. Publication-priority independence is not asserted.

## Value — PASS

Finite reset width is physically unavoidable, and the leading small-width/fast-frequency approximations used in the motivating model do not give an optimum within their stated validity. The result identifies the exact existence and uniqueness of an observable-specific optimal cadence and its divergent inverse-square-root scaling as the finite width approaches zero. The one-scale uniqueness sharply contrasts with known multi-relaxation-scale examples exhibiting multiple local maxima, so it is a structural boundary rather than a routine numerical peak location. The two limiting coefficients are testable and separate peak location from peak height.

## Scope and closest literature

- Farago, *The Resetting Heat Engine* (2026), arXiv:2605.28445, especially the harmonic model, Gaussian endpoint KL, and approximate Poisson formula. These parts are prior work.
- Mori, Olsen and Krishnamurthy, *Entropy production of resetting processes* (2023), DOI:10.1103/PhysRevResearch.5.023103. Its trajectory-entropy and stationary-distribution observables are not identical to the conditional-endpoint rate here.
- Gupta, Olsen and Krishnamurthy, *Thermodynamic Cost of Recurrent Erasure* (2025), DOI:10.1038/s42005-025-02277-w. Its work-cost optimization concerns finite-time trap-control protocols.
- Closely related mathematical claims about fixed-mean renewal envelopes and two peaks for two distinct relaxation scales were compared by exact implication; their results do not settle the stated one-scale Poisson-frequency problem.

The endpoint diagnostic is **not** identified with measured work, heat, or total stochastic entropy production. The theorem does not extend to a non-Gaussian reset law, arbitrary renewal law, multidimensional dynamics, or the singular value \(q=0\).

Self-review: passed. Independent audit: not yet performed.

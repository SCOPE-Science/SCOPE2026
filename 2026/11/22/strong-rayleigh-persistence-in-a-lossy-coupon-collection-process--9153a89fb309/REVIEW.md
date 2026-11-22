# Scientific review: strong Rayleigh persistence in a lossy coupon collection process

## Correctness — PASS
The full claim concerns uniform independently drawn labels, an initially empty set, and independent post-draw losses with an arbitrary deterministic common per-round probability. The count polynomial satisfies the exact identity
\[
F_{t+1}(z)=x_t\left[F_t(x_t)+\frac{1-x_t}{n}F'_t(x_t)\right],\qquad x_t=p_t+(1-p_t)z.
\]
The polar-derivative interlacing argument preserves real nonpositive roots for every \(n\ge1\), including repeated roots and endpoint loss rates. Exchangeability plus the established characterization of symmetric multiaffine stable polynomials proves the strongly Rayleigh property. The Bernoulli-sum factorization follows from roots and normalization. Uniqueness of the fixed-rate invariant distribution and polynomial-limit closure give the stationary corollary. Independent finite-state rational arithmetic checks, including exact symbolic root counting, passed 3,960 assertions using the packaged checker. The proof, not the finite sample of checks, establishes the arbitrary-size theorem.

## Originality — PASS under examined evidence, with priority limitations
Cruciani–Dudeja (2026, arXiv:2602.20705, full text inspected) prove negative association of coupon-indicator variables at each fixed time, but do not state this stronger multivariate strong Rayleigh or Poisson-binomial factorization. Long (2026, arXiv:2605.14511, full text inspected) develops stationary flux and hitting-time results, not arbitrary-time polynomial root preservation. Previously available exact stationary inclusion formulas and stationary fluctuation laws concern the same collector but do not imply the all-time strong Rayleigh assertion without further argument. The group-coupon vacancy theorem concerns never-seen labels **without erasure**; its root preservation is a different update operator and only overlaps with the zero-loss boundary. Borcea–Brändén–Liggett (2009) provide the exchangeable strong Rayleigh equivalence and polarization used in this proof, rather than establishing this particular collector's update. Additional general real-rootedness-preserver or queueing representations might imply this model-specific conclusion; their absence from searches does not establish universal historical novelty.

## Value — PASS
Random erasure after collection induces dependencies across physically retained labels, and the motivating work uses negative association to obtain concentration bounds. Identifying the exact finite-time Poisson-binomial class and joint strong Rayleigh property is a substantive strengthening: it supplies an explicit factorization of the full count law and a stable-polynomial invariant for every time-dependent common deletion schedule, not merely a mean/covariance inequality or a limiting law. It is directly relevant to dynamic cache and unreliable-information retention models. The result does not claim elementary formulas for Bernoulli parameters or extension to heterogeneous per-label deletion.

## Limitations and review status
All public source comparisons are best-knowledge, not proof of exhaustive bibliographic uniqueness. Neither the finite checker nor the model review is an external mathematical validation. The statement is restricted to the exact uniform-label, common-probability independent-thinning model.

Self-review: passed. Independent audit: not yet performed.

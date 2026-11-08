# Scientific review

## Correctness — PASS

The claim uses exact quantifiers (all positive damping, confinement, and covariance decay rates; all finite lags) and excludes additional white noise. The covariance ODE follows from the stable causal convolution, not from assuming Gaussian forcing. The critical exponential/oscillatory amplitude bound is a strict algebraic inequality; spectral-ratio inversion gives a convolution of strictly positive functions below the threshold. Above the threshold the slower oscillatory component forces both signs indefinitely. The first-negative-lag bracket implies the stated singular limit. The standalone symbolic checker validates the critical identities and independent matrix-exponential reconstruction. The 4,509 finite sign samples are diagnostic only, not evidence for an infinite-lag theorem.

## Originality — PASS (qualified)

Caprini and Marconi, *Inertial self-propelled particles* (arXiv:2009.14032v1, full accessible text, Section IV.2 Eq. 33 and Appendix C), already provide the full time-dependent stationary position correlation and say increased persistence can suppress negative correlation. They do **not** explicitly formulate the universal exact boundary \(\lambda=\alpha\), prove all-lag positivity by positive convolution for the whole exponential-covariance class, or derive the diverging first-negative-lag asymptotic constant. This is the closest and potentially dominating prior result: the present theorem is a new global sign analysis of an available exact formula, not a claim of a new pointwise correlator. Related full sections in Nguyen et al. (2021) address inertial harmonic AOUP displacement statistics, and Chaudhuri (2024) covers stationary moments and kurtosis of inertial active Brownian particles, not the stated sign/delay theorem. A prior reader could in principle derive the sign boundary from the 2020 formula; this creates nontrivial implicit-priority risk, acknowledged rather than treated as proof of novelty.

## Mathematical value — PASS

The precise all-lag suppression of negative correlations is a motivated dynamical distinction in inertial active-trap measurements. A finite observational window can mistake an oscillatory system for a non-sign-reversing one just beyond the boundary; the exact singular delay quantifies that risk, without relying on a finite plot. The strict proof applies across physical AOUP and active Brownian orientation models sharing the same two-point function. It neither asserts a larger downstream theorem nor treats algebra alone as value.

## Closest sources and remaining risks

The strongest coverage risk is Eq. (33) of the 2020 primary paper, which fully determines the covariance before the new global sign analysis. The 2021 and 2024 primary sources may contain further implicit equivalent forms of stationary second moments. Alternative experimental noises, rotational inertia, and a thermal bath lie outside the theorem. Independent specialist scrutiny has not occurred.

Self-review: passed. Independent audit: not yet performed.

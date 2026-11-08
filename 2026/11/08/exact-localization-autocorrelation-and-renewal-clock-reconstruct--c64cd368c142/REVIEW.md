# Review: stationary localization autocorrelation and renewal-clock identification

## Correctness — PASS

The observation at the resetting site is exactly the event of no jump since the most recent full reset, because jump sizes are non-atomic. A stationary Poisson reset has independent exponential backward age. The full proof partitions pair events by whether the interval contains any reset; the surviving no-reset term is a reset-tilted waiting-time tail, and the reset-containing term factors with the stationary localization mass. The resulting covariance passes the \(t=0\) variance and \(t\to\infty\) decorrelation boundary checks. The derivative inverse uses the continuity and normalization \(\Psi(0)=1\). Tonelli's theorem and elementary Laplace-integral asymptotics yield each of the five Lomax regimes. The standard-library reproducibility script independently checks exponential and deterministic clocks, numerical Lomax inversion and stationary paired simulations.

## Originality — PASS, with qualified priority risk

The January 2026 motivating article determines a one-time stationary delta mass and spatial distribution; its inspected main article and independent-reset supplement do not develop the two-time localization covariance or joint reconstruction. Earlier continuous-time random-walk resetting literature primarily treats one-time propagators, moments and first-passage observables; accessible abstracts do not establish the new inverse law, although their full texts were not accessible in this review. A related indexed theorem about general stationary alternating-renewal pair-law nonidentifiability has a different model class and does not cover the special full-clock Poisson reset structure or its mass-plus-correlation recovery. The 2025 full-text study of independently reset scaled Brownian particles concerns continuous Gaussian spatial laws and extreme-value/center-of-mass statistics, not a positive-mass site-occupancy time series. The source's known one-time mass does not by itself imply the full correlation curve: the latter depends on the whole tail of the holding-time distribution, not only its Laplace transform at one rate. A general previously published regenerative two-time or renewal inverse theorem could still cover this specialization.

## Value — PASS

A stationary localization mass alone reveals only a single Laplace statistic of the renewal waiting law. The complete binary time series, without measuring displacements or jumps, reconstructs both the physical resetting rate and the entire unknown holding-time survival distribution. The integrated correlation time also exhibits five sharp weak-reset regimes, with both the infinite-mean and infinite-second-moment boundaries visible, furnishing a concrete temporal test for hidden heavy-tailed renewal statistics in a model featuring a macroscopic stationary atom. This is a motivated structural identification and classification rather than merely a numerical increment to a known density table.

## Limits and priority

The claim concerns population correlation, not stable finite-sample estimation. Non-atomic jumps, clock renewal upon every reset, and an exactly known stationary regime are essential. The main source was inspected in full relevant sections; a potentially relevant pair of earlier primary CTRW-reset papers could only be checked from accessible abstracts, leaving explicit publication-priority uncertainty. The checking script is finite evidence and cannot replace the proof.

Self-review: passed. Independent audit: not yet performed.

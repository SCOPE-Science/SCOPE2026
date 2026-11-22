# Review of the critical spherical Poisson-kernel shot-noise law

## Correctness — PASS
The sphere-angle density is \(a_q\sin^{q-1}\theta\), so the close-pair scale \(n^{-2/q}\) has finite nonzero expected collision intensity. The factorial-moment graph argument excludes overlapping edge clusters, proving the limiting Poisson distance measure. Uniform integrable tail bounds justify the noncompact Poisson-kernel integral. Conditional centering removes cross-edge covariances, and the spherical Poisson semigroup gives exact all-bandwidth covariance. Poisson Laplace calculus gives the beta cumulants and the two iterated endpoint regimes. The normalization and all integer \(q\ge1\), fixed positive tuning parameters, and nonsimultaneous limits are specified. The included checker passed 202 numerical and algebraic assertions. Computation corroborates but does not replace the proof.

## Originality — PASS with residual risk
The 2023 Fernández-de-Marcos–García-Portugués paper supplies the spherical Poisson-kernel statistic, exact fixed-parameter moments and chi-squared-series limits. The Ding–Markatou–Saraceno study independently develops its spectral/Karhunen–Loève decomposition and fixed-tuning calibration. The present critical scale changes the limit mechanism to a Poisson shot-noise law, including a shared cross-bandwidth Poisson measure and exact log-scale correlation. The published semigroup and variance formulas imply its covariance asymptotic, but not by themselves the non-Gaussian triangular joint distribution or the boundary laws. Classical close-pair Poisson theorems provide the point-process ingredient and are explicitly acknowledged, not claimed as new. The 2010 Pycke article is related but only its accessible abstract was inspected; an unidentified historical singular-kernel theorem may already cover the exact limit.

## Value — PASS
A published spherical goodness-of-fit statistic may be tuned increasingly close to the nonsmooth kernel boundary as samples grow. Fixed-tuning null calibration then fails to describe the critical rare-pair regime. A complete distributional limit and the explicit \(\operatorname{sech}^{q}\) correlation function give usable multiscale null calibration and sharply distinguish sparse, critical and Gaussian-dilute endpoint behaviors. The substantive gap is not a mere restatement of kernel normalization or of the Poisson limit for unweighted pair counts. No power gain is asserted.

## Scientific limits
Only finitely many fixed bandwidth constants are covered jointly; the dimension remains fixed. Independent historical-priority assessment remains necessary. No machine-assisted finite check proves the asymptotic statements.

Self-review: passed. Independent audit: not yet performed.

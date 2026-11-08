# Scientific assessment

**Correctness — PASS.** The stated integrand prior gives an exact Markov-bridge partition of posterior integral uncertainty. Direct Gaussian conditioning yields the terminal and interior gap functions. Their strict convexity proves the single global optimizer and handles zero-gap and single-node cases. Uniform cubic-gap expansions and a bounded 1-dependent central limit theorem establish asymptotic loss and its fluctuation constant; the independent finite verification program passed 140 checks. Numerical checks are consistency evidence only, not infinite proofs.

**Originality — PASS, qualified.** The 2018 Bayesian quadrature framework and its exponential-covariance example do not state the specific finite-\(n\) global integral-optimal nodes; OU pathwise IMSPE results use a different design objective. An earlier Brownian-kernel benchmark treats a different, nonstationary covariance, for which the OU finite-sample nonlinear terminal spacing does not follow. The 2001 dissertation abstract by Mukherjee separately mentions integral estimation and creates genuine precedence uncertainty because the relevant full text was unavailable. Other equivalent classical specializations cannot be excluded without specialist review.

**Value — PASS.** The global finite-sample design is a motivated exact optimization result for the exponential covariance / Matérn-1/2 quadrature benchmark. Quantifying the jitter penalty and fluctuation law makes the optimality distinction operational; the leading stochastic effects may also be explained by Brownian local scaling, so no broader universality breakthrough is asserted.

**Scientific limits:** Known stationary Gaussian covariance and zero mean; noiseless single-location measurements; one-dimensional interval; integral variance rather than integrated pointwise variance. No unknown hyperparameters, pathwise IMSPE, or noisy observations are treated. No independent verification or comprehensive publication-precedence certification is claimed.

Self-review: passed. Independent audit: not yet performed.

# Scientific review: unique transient kurtosis peak under velocity-only resetting

## Correctness — PASS
The theorem concerns a precisely specified integrated Brownian motion with independent Poisson resets of velocity alone and zero initial velocity. Conditioning on the Poisson interval lengths gives a nondegenerate Gaussian variance mixture, so the excess kurtosis is exactly three times the relative variance of the sum of cubed interval lengths. The two finite-time moment formulas match independently published renewal moments (den Hollander et al., arXiv:1801.09909, Theorem V.1). Reconstructing their derivative produces an explicit entire exponential polynomial. Its first nonzero Taylor coefficients are strictly positive at orders 9--15 and strictly negative at every order at least 16. Normalizing by the fifteenth power gives a strictly decreasing function with opposite endpoint signs, proving a unique critical point over the entire positive axis. The symbolic checker reproduces the renewal transforms and every finite sign in this proof, and confirms the endpoint coefficients and numerical peak. Numeric samples are not used to prove uniqueness.

## Originality — PASS, with priority risk
The original complete finite-time second and fourth moments are already in den Hollander et al. (2018), and reproduced by Smith and Majumdar (2022). The latter also establishes the fourth-cumulant rate and hence the leading large-time \(42/(rt)\) excess-kurtosis coefficient. Olsen and Löwen (2024) explicitly connect velocity-only resetting to the Brownian-area observable. None of these premises is claimed as new. Their complete moment formula does not itself state a global one-critical-point classification. The new mathematical step is the all-orders sign-change proof that its transcendental derivative has exactly one positive zero. Searches of these primary full texts, related publications, and mathematical finding records did not locate that specific theorem. There is residual risk that an unindexed presentation, or an earlier global analysis of the same exact formula, has already established the result.

## Mathematical value — PASS
The normalized fourth cumulant is a natural and dimensionless measure of non-Gaussianity in transport. A global one-peak theorem determines the number, location and size of non-Gaussian transient maxima, not merely the early or late expansion. The parameter-free peak height and the exact time rescaling \(t_*=z_*/r\) distinguish a single characteristic pulse from potentially multiple transient bursts; this is a motivated structural classification of a prominent non-equilibrium model. It does not claim experimental calibration performance or an extension to arbitrary reset protocols.

## Closest literature and limits
- Den Hollander et al., *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909, Section V, Theorem V.1: identical finite-time moments (prior), no reported single-peak theorem.
- Smith and Majumdar, *Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting*, arXiv:2202.03546, Section III: known cumulant coefficients and same moment formulas, no reported transient peak classification.
- Olsen and Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685, Sections 2--3: same physical resetting interpretation and generic moment recursion, no reported exact kurtosis unimodality.

All results require the specifically stated zero-start Gaussian velocity segments and Poisson resets. The peak value is approximate; the uniqueness and global bound are exact.

Self-review: passed. Independent audit: not yet performed.

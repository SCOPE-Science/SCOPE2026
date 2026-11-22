# Self-review

## Correctness — PASS

The claim is a stationary, one-coordinate, two-time stochastic integral theorem with explicit quantification over \(\kappa>0\), \(A>0\), \(D\ge0\), and positive lag. The generator's Lyapunov equation gives the stated Gaussian covariance. The exact semigroup gives two-time Gaussian pair contractions. Crucially, the work noise at an earlier time changes the later positional drift, producing the additional term \(-2D\kappa A e^{-(\kappa+1)t}\). Including it gives the claimed kernel. The sign of a two-exponential kernel has the stated strict one-crossing/no-crossing dichotomy, with a separate correct resonant limit. No heuristic infinite-time inference is made from finite computations. `check.py` passed 1,039 exact-rational and deterministic checks, including the full bivariate exponential polynomial and resonance. The positive zero-lag Dirac term is explicitly distinguished from the negative regular separated-lag covariance.

## Originality — PASS, qualified

The 2021 primary source studies large deviations of active work, including simulations for confinement. The accessible full 2023 preprint is the closest same-model source and analyzes the path-integral and scaled generating function for integrated work and its unusual rate-function tails. Its model, observable, stationary covariance, main analysis and conclusions were materially read; they do not assert the positive-lag work-current covariance law or the thermal- and stiffness-frontier classification. Its integrated second cumulant can constrain only an integral of the lag kernel, not the unique crossing time or sign at every lag. Two materially read published findings concerning harmonic *switching-work across distinct particles* and *equal-time active velocity correlations on graphs* use different observables/dynamics and imply neither statement. Several additional semantic searches of prior mathematical findings for active-work lag covariance, thermal noise, sign change and harmonically trapped Ornstein–Uhlenbeck activity returned no stronger covering claim. This is a claim-level comparison, not a search-based proof of novelty. Residual risks: an unindexed Gaussian additive-functional theorem may imply the result; the earlier 2021 manuscript was not available in full text. No independent publication-priority verification was performed.

## Mathematical value — PASS

Active work is a natural injection and dissipation statistic of persistent self-propulsion. The distinction between a white-noise instantaneous contact, positive short-lag memory, and anticorrelated delayed injection is physically interpretable but invisible in the bulk rate function alone. The explicit thermal threshold \(d_c(\kappa)=(\kappa+2)/(\kappa(\kappa+1)^2)\), unique crossing time, resonance formula, and unique stiffness boundary give an exhaustive, parameter-uniform phase classification for a directly measurable two-time observable. This is more than re-expression of a known first or second integrated cumulant, and can be used to benchmark finite-bandwidth active-work measurements. Generalizing to interacting or nonlinear models is not claimed.

## Closest literature and limitations

- Semeraro et al., *Work Fluctuations in the Active Ornstein-Uhlenbeck Particle Model*, arXiv:2103.11369 (2021): same active-work observable and confinement, but accessible material only title and abstract; possible implicit overlap remains.
- Semeraro et al., *Work Fluctuations for a Harmonically Confined Active Ornstein-Uhlenbeck Particle*, arXiv:2302.12535 (2023): full preprint model, covariance matrix, work functional, generating function and conclusions read; studies integrated-work large deviations, not the assessed positive-lag covariance sign law.
- *A rank-one work-noise law for Brownian particles in a common flashing harmonic trap*, published-finding corpus published 2026-11-02: distinct common flashing-trap switching work across particle species; does not specialize to this single-particle active propulsion work.
- *Graph-matched active forcing: a two-temperature Gaussian law and simultaneous velocity-correlation reversal*, published-finding corpus published 2026-10-26: equal-time velocity correlation in inertial networks, not the present lagged quadratic-work current.
- The 2023 comment arXiv:2311.14724 addresses large-deviation generating-function-domain complications; no assertion is made here about those rare-tail issues.

Self-review: passed. Independent audit: not yet performed.

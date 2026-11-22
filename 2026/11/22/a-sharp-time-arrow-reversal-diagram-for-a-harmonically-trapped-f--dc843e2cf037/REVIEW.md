# Scientific review: finite-tumble position-only time-arrow classification

## Correctness — PASS

The stationary three-state motor dynamics, invariant distribution, independent Gaussian perturbation and fourth-order time-order convention are explicit. Polynomial-generator stationarity gives the five mixed moments needed for a closed five-dimensional resolvent. Direct exact symbolic reduction yields the rational Laplace transform with all poles and normalizations displayed in `RESULT.md`, independently of thermal diffusivity. Inverting gives four- and five-fold positive exponential convolutions. The ratio of these kernels is strictly increasing by log-concavity, with exactly computed endpoint limits; hence the positivity, negativity and unique sign-crossing alternatives follow for every positive parameter value, including resonances and equality boundaries. `verify.py` independently compares the generator semigroup and positive cascade and passed 123 checks. Numerical evidence is supplementary, not the all-parameter proof.

**Risk/limit:** The theorem assumes stationary exponentially distributed running and tumbling intervals, a symmetric relaunch, a linear trap and independent Gaussian thermal forcing. It does not assert entropy-production quantification or statistical identifiability from finite observations.

## Originality — PASS, with publication-priority qualification

The relevant primary 2026 work and its 2024 precursor derive conditional/single-time harmonic-trap distributions and moment calculations, but not the present stationary **two-time position-only quartic asymmetry** and its exact three-way sign classification. The known result on an always-positive time arrow for the same finite-tumble motor combines hidden motor occupancy with position; it is a different statistic and does not dominate this sign-reversing observable. The known full quartic time-arrow result for instantaneous-reorientation run-and-tumble dynamics excludes finite tumble states. The known unconfined three-state fourth-cumulant diagram concerns displacement, not the time-reversed ordering of confined stationary positions. The full relevant public Result.md statements and available primary text were compared on these implications, rather than titles alone.

**Risk/limit:** Earlier general Markov semigroup, diagrammatic moment and convolution techniques could be specialized to obtain the formula; the assessment does not claim those tools are new. Unindexed equivalents or a result hidden in another primary source may change priority; no independent literature audit is claimed.

## Value — PASS

A position-only fourth-order arrow avoids access to a latent motility sensor and can discriminate temporal order even when every ordinary stationary position covariance is time-symmetric. The rest-time parameter creates a sharp, nontrivial switch between fixed-sign and exactly one-lag-reversal regimes. Its exact boundary includes all trap/motor rate resonances and survives arbitrary independent Brownian thermal fluctuations. This identifies a meaningful model-sensitive boundary for time-series irreversibility diagnostics, rather than a narrow numerical example or mere recalculation of stationary moments.

**Risk/limit:** It provides a theoretical observable, not an experimental power analysis or a universal thermodynamic entropy rate.

## Closest literature

- Sun, Ye and Chen, arXiv:2610.24961v1 (2026): same finite-tumble model; conditional stationary distributions and moment methods, no identified position-only temporal sign diagram.
- Sun, Ye and Podgornik, arXiv:2409.00578v1 (2024): exact moments and steady-state law for same model, no identified two-time temporal sign classification.
- *A sharp dimension-seven threshold for the quartic time arrow of trapped run-and-tumble motion* (2026): no finite tumble phase, different model.
- *An exact two-moment inverse fold in a trapped run-and-tumble particle* (2026): same model, one-time inverse moments.
- *A golden-ratio kurtosis boundary for intermittent run-and-rest motion* (2026): same motor, unconfined fourth displacement cumulant, not stationary trapped temporal ordering.
- Previously recorded mixed hidden-motor/position time arrow for the same dynamics: strictly positive but does not determine the position-only statistic.

Self-review: passed. Independent audit: not yet performed.

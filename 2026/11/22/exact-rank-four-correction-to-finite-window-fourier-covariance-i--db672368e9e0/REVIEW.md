# Review of the finite-window telegraph Fourier-covariance theorem

## Correctness — PASS

The joint two-state transcription generator gives the stated stationary promoter–mRNA cross-covariance, mRNA variance and two-exponential (or confluent resonant) time covariance. The identity between a Kac–Murdock–Szegő Toeplitz covariance and its periodization is verified entry-by-entry. The nonresonant rank follows from a four-root Vandermonde system; at equal rates it follows from a two-root confluent Vandermonde system and a four-dimensional coefficient matrix of nonzero determinant. Strict spectral positivity makes the Gaussian-surrogate determinant and inverse identities applicable. A standalone standard-library checker passed exact rational identities and rank tests, and independently summed the nonperiodized finite Fourier covariance for the concrete transcription parameters.

A finite checker does not replace the universal argument. The Gaussian **surrogate** has the exact second-moment covariance but is not asserted to equal the true stochastic-transcription likelihood. The initiating numerical trajectories are nonstationary, while this theorem requires stationary initialization.

## Originality — PASS within inspected literature; residual priority risk

Fang, Sun, Zhang and Khammash (2026), arXiv:2611.07684v1, give the specific telegraph reactions and use a diagonal covariance for a Fourier Gaussian approximation (Algorithm 1). Their inspected full text does not derive this model's exact finite-window off-diagonal covariance, periodization rank, or resonant four-dimensional correction. Geoga (2024), arXiv:2404.16583, treats general finite-DFT covariance and efficient **approximate** diagonal-plus-low-rank correction; the generic existence of nonzero finite-DFT correlations and the low-rank idea are therefore not new. The assessed distinction is a **closed exact biochemical parameterization**, with a sharp rank drop only on the explicitly specified nonresonant surface, a non-dropping confluent rank at equal rates, and exact fixed-rank Fourier Gaussian-surrogate computation. General Kac–Murdock–Szegő kernel algebra is prior mathematics; this claim is not a rediscovery of it as a general theorem.

No equivalent model-specific theorem was located by the documented targeted database and literature searches. This cannot prove uniqueness: unindexed spectral/ARMA or biochemical statistics literature could contain an equivalent. One newer two-state transcription distribution paper was inaccessible in full; its available description concerns skewness/kurtosis rather than the Fourier likelihood, but it remains an access risk.

## Value — PASS

An actual 2026 biochemical-inference algorithm assumes diagonal frequency covariance. In the same model, at precisely the sample rates highlighted by that article, the promoter and degradation relaxation rates coincide: the exact finite-window covariance remains rank four away from a diagonal Fourier matrix, not diagonal or rank two. The correction enables covariance-matched Gaussian calculations in quasilinear time without Monte Carlo estimation of a dense covariance. Its natural purpose is to diagnose and correct finite-window frequency coupling, not merely to restate a standard Toeplitz identity. The all-rate and resonance formulas constitute a reproducible benchmark for future stationary-frequency inference comparisons.

## Closest literature and scientific limitations

- Fang et al., *Accelerating reaction network identification via frequency-domain analysis*, arXiv:2611.07684v1 (2026-11-05), https://arxiv.org/abs/2611.07684
- Geoga, *Fast Machine-Precision Spectral Likelihoods for Stationary Time Series*, arXiv:2404.16583 (2024-04-25), https://arxiv.org/abs/2404.16583
- The scope is stationary, single-promoter linear transcription, complete regular temporal sampling, and exact second moments only. The original experiment's transient initialization, its posterior accuracy, and non-Gaussian likelihood are not proved. Near-resonant evaluation requires stable divided differences or the explicit resonant expression. Historical equivalence remains possible.

Self-review: passed. Independent audit: not yet performed.

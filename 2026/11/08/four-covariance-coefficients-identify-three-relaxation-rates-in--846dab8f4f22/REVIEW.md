# Scientific review

## Correctness

**PASS.** The specified two-dimensional Markov process regenerates at complete Poisson resets and has finite stationary moments. Its generator gives exactly three stationary moment identities, and the closed two-component lag semigroup gives an exact two-exponential/confluent covariance. The right derivative identity recovers the reset rate. If the covariance Prony determinant is nonzero, the characteristic polynomial and the strictly ordered stationary-variance comparison identify the remaining rates. If the determinant is zero, the nonvanishing orientation coefficient forces an exact cancellation of the trap pole, which is recovered by a strictly monotone quadratic. All cases have been examined, and the rational cancellation witness verifies the exceptional branch. The embedded checker passed 1,409 exact-rational and numerical consistency checks, including separately formulated finite-matrix semigroup calculations; the infinite-parameter proof is analytic rather than inferred from those computations.

## Originality

**PASS, with publication-priority uncertainty.** Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap* (arXiv:2409.06920), provides the relevant reset-and-trap model, one-time moments, and orientation correlations, but the inspected text does not report stationary transverse *two-time positional* covariance or prove recovery of all three unknown rates from its first four right derivatives. Caraglio and Franosch (arXiv:2210.04205) calculate position autocorrelations without resetting; Kumar, Sadekar and Basu (arXiv:2008.03294) study complete resetting without a trap. Classical Prony reconstruction of two exponential rates is well known and is not counted as a novel contribution. The distinct contribution under review is model-specific injectivity, exploiting a reset-only cusp slope and strict mode-assignment inequality, including hidden-pole recovery. The forward formulas in the cited literature could facilitate an independent derivation, so a broader unpublished or unindexed inverse-identification theorem remains a residual priority risk. No searched covering statement was found; absence from search is not a novelty proof.

## Mathematical value

**PASS.** The result answers an experimentally motivated structural-identifiability question: whether a single time series transverse to a known reset heading, without orientation measurements, is theoretically sufficient to determine all three unknown relaxation mechanisms. It gives an explicit algebraic reconstruction rather than a numerical least-squares fit, and it treats the exceptional cancellation at which naive two-pole inference breaks. The exact cancellation example demonstrates why the boundary case is substantive rather than a generic restatement of two-exponential fitting. Structural identifiability does not guarantee stable estimation from sampled data, and the result is limited to a fully resetting harmonic model with calibrated propulsion and thermal diffusivity.

## Checked literature and limitations

Relevant inspected primary sources: Shee (https://arxiv.org/abs/2409.06920), including the physical model and sections on moments and orientation correlations; Caraglio and Franosch (https://arxiv.org/abs/2210.04205), especially the unreset positional autocorrelation Eq. (26); and Kumar, Sadekar and Basu (https://arxiv.org/abs/2008.03294), for complete resetting without confinement. Also compared against semantic research-record results for stationary autocorrelation identification, reset dynamics and spectral pole recovery. No independent expert or publication-priority audit has been carried out.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness

**PASS.** The result follows from exact Poisson frequencies of zeros and ones, two nonnegative probability-generating-function remainder bounds, and a conditional convergence argument identifying each reciprocal-Poisson atom and the infinity branch. Fixed-parameter delta-method center and variance were reconstructed independently from the Poisson covariance matrix; the explicit limiting critical boundaries strictly separate the Poisson atoms. The complete proof is in `RESULT.md`, and `verify.py` supplies additional exact-rational and numerical checks rather than an infinite-proof substitute.

## Originality

**PASS (qualified).** Aleksandrov, Weiß and Jentsch (doi:10.1111/stan.12252) introduce the ratio, its fixed-parameter normal calibration and the possible zero-denominator issue. Weiß, Puig and Aleksandrov (doi:10.1002/bimj.202200073) analyze the same exponential weight family and warn about degenerate boundary choices. The second paper's Gaussian CLT/delta method does not apply to the critical triangular array; its warnings do not identify an atom at infinity, the reciprocal-Poisson law or the 36.79% null rejection rate. Mathematical-record and prior-claim comparisons found no directly covering statement. Classical Poisson rare-event and generic reciprocal-ratio results could offer components or historical priority, so absolute novelty is not claimed.

## Value

**PASS.** The exact limiting rejection probability exposes an extreme and precisely quantified failure of a conventional calibration when the expected number of zero observations remains order one. The statistic-specific mechanism distinguishes a Gaussian approximation's nonuniformity from routine small-sample bias. The result neither invalidates the authors' ordinary fixed-parameter assumptions nor evaluates simulation-based alternatives.

## Closest literature and limitations

The original 2021-online study, its 2022-online weight-selection successor, and classical rare-binomial Poisson approximation are the closest identified mathematical sources. The regime requires iid Poisson counts with increasing means and weights approaching zero, and the 36.79% figure is specific to a two-sided 5% normal calibration. No claim is made about finite-sample accuracy, an optimal replacement test, high-dimensional dependence, or fully exhaustive historical priority. The result has no independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.

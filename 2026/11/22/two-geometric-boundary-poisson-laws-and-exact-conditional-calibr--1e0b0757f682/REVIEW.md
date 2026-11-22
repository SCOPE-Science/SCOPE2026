# Self-review

## Correctness — PASS

The one claim is the sharp two-boundary calibration theorem, including the exact conditional finite-sample remedy. Exact algebra gives \(H-K=S^2/(n+S)-D\) with \(D=\sum_i(X_i-1)_+\), and the published variance reduces to \(p(1-p)^2\). The \(p\downarrow0\) endpoint is driven by rare zeros; the opposite endpoint is driven by observations of size at least two, occurring with probability \((1-p)^2\). The Poisson limits follow from binomial Poisson convergence and explicitly controlled higher counts; zero-intensity cases are handled separately. Lyapunov third moments prove the sufficient Gaussian condition uniformly, and subsequences prove necessity. Conditional probabilities are exact weak-composition counts and yield finite-sample superuniform p-values. The standalone checker passed 13,626 assertions. Numerical simulation is supplementary, not a substitute for proof. Risks: no explicit convergence-rate or uniform-tail result, and equality of an atom with a limiting critical value is excluded from the strict size statement.

## Originality — PASS, qualified

Directly inspected the primary freely accessible arXiv full-text sections on the test construction, Proposition 3.1, the geometric subcase, and simulation/limitations; fixed-parameter normality in that article does not imply arbitrary triangular-sequence normality. Its studentizing variance is reused without claiming authorship. The closest broader p.g.f. and count-data comparisons concern different test statistics or families. Targeted mathematical-record and published-literature searches for the zero-count versus fitted-mean statistic, rare-doubleton boundary, parameter aliases, and sharp Gaussian/Poisson thresholds found no direct coverage. The conditional composition count is elementary and explicitly not claimed as combinatorially original. Residual risk: older general triangular-array asymptotic theory or unseen dissertations may implicitly subsume parts of the phase diagram; searches cannot certify absolute priority.

## Value — PASS

For a published, readily implemented goodness-of-fit test, a precise if-and-only-if condition for valid normal calibration is mathematically and practically important. The two critical exponents are different and arise from genuinely different sufficient-statistic cancellations; both yield the same non-Gaussian family. The theorem demonstrates an attainable asymptotic null rejection level approaching 16.18% despite a nominal 5% cutoff, and provides an exact parameter-free conditional calibration that works across both problematic regimes. This addresses real control of false positives, not an arbitrary parameter slice or recomputation of a table. The result does not assert a global maximizer, a power advantage, or superiority of a particular alternative test.

## Closest literature and limitations

Di Noia et al. (2021 preprint, 2022 online journal article), https://arxiv.org/html/2112.11861 and https://doi.org/10.1080/10485252.2022.2137728: fixed-parameter normal theory and the exact definition of this test. *Pgf-based goodness-of-fit tests for binomial counts* (2026), https://doi.org/10.1007/s00184-025-01009-y: broader count-data testing context but bounded-binomial rather than the target geometric parameter-boundary theorem. The 2013 dissertation *The goodness-of-fit tests for geometric models* by Feiyan Chen, https://digitalcommons.njit.edu/dissertations/350/, was checked at its abstract level; the linked full-text download returned HTTP 403 and it remains a general historical priority risk rather than decisive evidence.

Self-review: passed. Independent audit: not yet performed.

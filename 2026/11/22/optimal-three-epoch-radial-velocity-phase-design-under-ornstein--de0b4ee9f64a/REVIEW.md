# Technical review: three-epoch correlated radial-velocity design

## Correctness — PASS

The claim is a global, three-parameter Fisher determinant statement for exactly three scalar measurements in one period. With the covariance model explicitly fixed, the determinant of the design matrix factors into three half-angle sines, while the stationary Ornstein–Uhlenbeck covariance determinant factors into the two consecutive innovation variances. Strict concavity of the gap-wise objective proves that every global optimum is equally spaced, not merely that an equal-gap stationary solution exists. Strict logarithmic concavity of the resulting one-variable objective proves its unique root, the exact range, monotonicity in correlation rate, and both endpoint limits. The proof handles zero-gap and full-period endpoints and excludes the singular infinite-correlation model. The companion checker successfully reproduced symbolic determinants, unconstrained numerical optimizations, and supplementary comparisons.

## Originality — PASS on inspected evidence

The main motivating article (Lam et al., arXiv:2408.16830) studies a general Fisher-information scheduling framework, using quasi-periodic Gaussian-process noise and primarily semi-amplitude precision, but does not give the exact joint three-parameter, three-epoch Ornstein–Uhlenbeck solution. Dette et al. (arXiv:1303.2863) treat approximate-design trigonometric regression with periodic kernels; their uniform design result does not establish a nonperiodic OU optimum whose finite-correlation gap is strictly below one-third period. Dette et al. (PMCID: PMC4914140) study continuous-time and primarily one-parameter regression designs. Baran et al. (arXiv:1704.05719) treat complex two-component OU processes with a different parameter family and information determinant; their equidistance theorem alone does not determine the present frequency-dependent gap. Comparisons with related published mathematical records and accessible earlier research claims did not identify implication-level coverage. General optimal-design theory is acknowledged as prior art. Historical priority remains provisional, particularly for older, difficult-to-index finite harmonic regression literature.

## Value — PASS

Precisely three observations are the saturated minimum for jointly identifying a systemic velocity offset and both phase coefficients at a known frequency. Correlation can change the optimal observation timing even though it does not change the mean sinusoid. The complete global phase law quantifies the admissible shift from \(P/3\) to \(0.2869573P\) and demonstrates a limiting determinant efficiency of only \(0.8726724\) for using white-noise timing with persistent noise. This is a reproducible analytic benchmark for checking finite-visit scheduling algorithms; its target is a motivated physical statistical problem, rather than an arbitrary numerical slice.

## Closest prior work, interpretation, and limitations

This result is not a theorem for eccentric planetary motion, correlated quasi-periodic stellar activity, photon-noise mixtures, unknown period, continuous observing campaigns or the marginal semi-amplitude variance optimized by Lam et al. The result also does not imply empirical feasibility or precision under telescope night constraints. A broader exact finite-sample theorem in uninspected literature could still cover the case. Independent external audit has not occurred.

Self-review: passed. Independent audit: not yet performed.

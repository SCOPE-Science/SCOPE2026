# Review of the drifted-walk rank saturation theorem

## Correctness — PASS
The result concerns independent iid-increment walks with nonzero signed drift, a negative exponential moment after sign orientation, and no ties. Infinite-horizon inversions have exponentially decaying last-lag tails. The stationary ergodic average of squared rank displacements yields the Spearman limit; the classical cyclic-permutation occupation identity supplies the \(\sum k p(k)\) variance. Fixed-lag ergodic discordance averages and exponential long-lag domination yield the Kendall limit. The exact checker tests finite coefficients and rank identities, but does not substitute for the analytical almost-sure proof. The limiting constants are finite and strictly positive when a negative step is possible.

## Originality — PASS against inspected evidence
Piancastelli and Barreto-Souza, *Time Series Analysis of Rankings* (arXiv:2502.05102, 2025), analyze temporally evolving stationary Mallows rankings, not rank concordance of a pair of independent cumulative-sum paths. Ryan et al. (2025) discuss drifted random walks as nonstationary trends, but give no such rates. Xie and Zhu (2026-11-16) study **centered** independent walks with mean-zero assumptions and different Brownian limit behavior. Published permutation-null rank identities and the classical Spitzer occupation formula do not themselves yield the two drifted-walk constants. Unknown earlier equivalent work cannot be conclusively ruled out.

## Value — PASS
The result distinguishes quadratic Spearman and linear Kendall convergence to falsely perfect concordance under process independence. Both leading terms are explicit summable functions of one-walk negative partial-sum probabilities; they are structurally meaningful for rank dependence in nonstationary series. It exposes a difference invisible to first-order saturation alone.

## Limits
The proof does not cover centered walks, heavy negative tails lacking the specified exponential moment, ties or dependent increments across series. No finite-sample calibration or independent mathematical audit is claimed. The 2026 comparison concerns centered walks; the motivating rank-dynamics paper was first posted in February 2025.

Self-review: passed. Independent audit: not yet performed.

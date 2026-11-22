# Scientific review

## Correctness — PASS

For each \(a_i,a_j,D_i,D_j,r>0\), \(0\le q<1\), stability of the contracting jump-diffusion guarantees a unique stationary law with bounded conditional variances. Applying its exact generator to \(x_i^2\), \(x_j^2\), and \(x_i^2x_j^2\) proves the positive equal-time covariance. The semigroup eigenfunction \(x_j^2-m_j\) gives the exact lag covariance; its reverse ordering gives the exponential ratio and one maximizer. The inverse formulas solve an injective algebraic map on the physical domain. Reproducibility checks include independent common-clock sampling, not just substitution into the claim. No numerical assertion is used as an infinite proof.

## Originality — PASS, qualified

The closest directly examined source is Galla (2026), arXiv:2602.21635, whose main multi-particle section and supplementary S2.2 derive the identical-particle squared-position correlation from a Gaussian weak-reset approximation, not exact finite-size shocks with heterogeneous trap strengths or inverse shock identification. Tal-Friedman et al. (2022) and Di Bello et al. (2023) provide single-process partial-reset distributions, which do not imply the heterogeneous fourth-order time arrow without additional coupled dynamics and inference. Published related fourth-order time arrows in different reset-noise or switching-trap models concern different generators and do not supply this formula. General generator-based covariance relations are standard; residual risk remains from unindexed equivalent special cases and general common-jump inference literature.

## Value — PASS

The claim identifies a directly interpretable fourth-order, time-directional signature of synchronized catastrophes that is invisible in the entire positional cross-covariance function. The inverse result is exact at arbitrary shock size and recovers both physically distinct shock controls using only stationary squared energies and their single-lag cross-correlation, without requiring the thermal diffusion constants. This is a meaningful identification of hidden common environmental events, not merely another isolated moment calculation.

## Scope and limitations

The result assumes stationary Gaussian thermal drivers, two distinct or equal positive trap strengths, one shared independent Poisson contraction clock, and a nontrivial contraction factor \(0\le q<1\). It does not solve noisy finite-sample estimation, unsynchronized clocks, or random shock amplitudes. The review establishes neither independent replication nor absolute publication priority.

Self-review: passed. Independent audit: not yet performed.

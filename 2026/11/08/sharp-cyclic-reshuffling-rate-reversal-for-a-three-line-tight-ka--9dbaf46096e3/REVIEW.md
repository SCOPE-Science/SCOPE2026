# Review of the three-line Kaczmarz rate-reversal result

## Correctness (C): PASS

The finite matrix identities, exact Schur discriminant, six-order covariance, independent-sampling gap and nonzero rank-one Jordan identity were reconstructed from the stated row vectors and verified by `verify.py`. The argument covers all real relaxations \(0<\omega<2\) and every integer epoch count. In particular, the `k=1` inequality and `k>=2` induction compare a deterministic worst-case initial error to an isotropic expected error, never conflating an eigenvalue with a singular norm. The symbolic checker and four rational two-epoch enumerations corroborate the proof, but they are not themselves a proof for infinite time.

## Originality (O): PASS, with precedence risk

Han and Xie (2024, arXiv:2410.01140) analyze reshuffling Kaczmarz using general bounds and comparisons in Section 3.3, not an explicit common-overrelaxation three-line exact second moment. Oswald and Zhou (2015, arXiv:1510.04727) give general shuffled-SOR rates and an even-row planar example, not the three-line optimal relaxation and finite-horizon reversal. Ferreira and coauthors (2024) survey randomization and empirical rate comparisons. A prior published two-row optimized cyclic Kaczmarz result shares a Jordan mechanism but does not cover the three-row randomized comparison. The search and implication comparisons are documented in `AUDIT.json`. Overlap in unindexed exact-frame literature remains possible; independent originality validation is not claimed.

## Value (V): PASS

The minimal redundant tight frame isolates an otherwise obscured scheduling issue: independently reshuffling rows offers a strict one-epoch advantage and improves on iid-with-replacement sampling, yet optimizing a fixed cyclic order yields a much smaller asymptotic rate and wins after every \(k\ge2\) epochs. The crossing is proved exactly rather than inferred numerically. This is a meaningful benchmark for row-action solvers, while being intentionally limited to this geometry, consistent systems and fixed common relaxation.

## Scientific limitations and risks

No result is asserted for inconsistent systems, arbitrary frames, per-horizon reoptimized relaxations, or almost-sure randomized exponents. The literature search supports best-knowledge originality only; published specialist work could contain an equivalent formula. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.

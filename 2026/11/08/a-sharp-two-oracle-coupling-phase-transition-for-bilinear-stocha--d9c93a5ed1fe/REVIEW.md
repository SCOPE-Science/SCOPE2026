# Scientific review

## Correctness — PASS

The full theorem follows from a pathwise scalar squared-norm multiplier, a complete parameterization of all uniform-marginal couplings, and two explicit quadratics. The comparison of stable-step ceilings reduces to the polynomial \(r^4-2r^3-2r^2-2r+1\), which has exactly one root above one after the substitution \(u=r+r^{-1}>2\). The global optimal-rate inequality is strictly positive for \(2<u<4\); for \(u\ge4\), antithetic sampling cannot contract at any positive step. Direct exact-rational tests and a standalone checker independently test all finite algebraic identities. Universal ranges are established by the proof, not by the tests.

## Originality — PASS, qualified

Mishchenko et al. (arXiv:1905.11373), Li et al. (arXiv:2107.00464), and Gorbunov et al. (arXiv:2111.08611) establish the importance and analysis of shared versus independent samples. Chae et al. (NeurIPS 2024) study shuffling across iterations, rather than all joint laws with prescribed uniform per-stage marginals. The directly compared statements do not yield the piecewise optimal oracle coupling, its ratio frontier or the sample-reuse versus antithetic stability/rate tradeoff. The identity for the purely same-sample method is background rather than the novelty claim. The inspection and semantic overlap comparisons are recorded in `AUDIT.json`; specialist precedence remains a residual risk.

## Value — PASS

The complete two-client classification resolves a natural design choice at fixed unbiased per-stage oracle costs. It shows that the pairing with the largest safe step need not be the pairing giving the fastest tuned convergence, and provides a rational case where both standard shared-sample and independent sampling diverge while antithetic coupling contracts. These features motivate larger finite-sum and oracle-coupling studies; the result is not claimed to imply any such extension.

## Scientific limitations

Exact only for scalar two-component bilinear games, equal-stage step sizes, no additive noise, and independent iteration-wise draws. The conclusion concerns mean-square geometric factors and not worst-case general monotone variational inequalities. Earlier publications may contain a mathematically equivalent special result not detected by the sources inspected.

Self-review: passed. Independent audit: not yet performed.

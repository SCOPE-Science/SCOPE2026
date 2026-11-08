# Scientific review

## Correctness — PASS

A precise quadratic-oracle model and both sampling laws are stated. Exact fourth spherical moments imply unbiasedness, the one-sample squared Frobenius norm, and the orthonormal-pair curvature covariance. The latter gives a closed formula for the risk difference for every \(d\ge2\) and \(2\le k\le d\), with exact trace-to-norm boundaries in the only two dimensions permitting risk inflation. The symbolic verifier confirms polynomial identities, threshold substitutions, three optimal inflation ratios, planar deterministic quadrature, and selected seeded higher-dimensional sanity tests. Finite tests are supplemental rather than an infinite theorem proof. All source formulas and evaluation costs use the same normalization.

## Originality — PASS (qualified)

Specific source-equivalence checks distinguish the one-frame projector-calibrated directional Hessian estimator from Wang's two-independent-direction estimator and Feng–Wang's two-frame mixed-direction scheme. The 2024 incremental Hessian paper uses a residual-correction recursion rather than this one-step calibrated average; its readable complete public manuscript was examined, including its background, estimator (3), and orthonormal sampling section. No inspected source asserts the trace–anisotropy risk ordering, the two exact low-dimensional reversal boundaries, or the sharp inflation ratios for this estimator. Prior spherical moment identities and generic orthogonal sampling benefits are explicitly not novelty claims. A specialized unpublished or older exact covariance calculation remains possible; this is not a proof of uniqueness.

## Value — PASS

Directional black-box curvature is a natural fixed-cost Hessian access primitive. The analysis resolves a real sampling-design ambiguity: orthonormality may increase, not decrease, mean-square Hessian error for certain indefinite quadratic objectives, yet universally reduces it in higher dimensions and for every positive-semidefinite Hessian. Sharp cutoffs and extremal ratios are directly reusable as finite-query regression tests and benchmarks for derivative-free Hessian estimation. The object and invariant precede computation; this is neither an arbitrary parameter slice nor a mere finite table.

## Closest literature and remaining limits

The detailed mathematical distinction from the 2022 two-direction and two-frame methods and the 2024 incremental method appears in `RESULT.md` and `AUDIT.json`. This result covers noiseless quadratic objectives and the explicitly defined unbiased estimator; it is not a claim about general nonlinear problems or all Hessian estimators. Specialized historical overlap cannot be excluded completely, and no independent scientific validation has been carried out.

Self-review: passed. Independent audit: not yet performed.

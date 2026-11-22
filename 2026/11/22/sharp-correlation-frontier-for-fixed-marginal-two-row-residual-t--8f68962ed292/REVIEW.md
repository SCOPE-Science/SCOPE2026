# Review

## Correctness — PASS

The update uses the unnormalized sum-gradient estimator and cached residuals from before the iteration. Each sample map is specified, and the second-moment operator is derived by averaging all four possibilities. An exact quadratic form has conditional drift equal to twice \(F(h,u)e^2\). The two-by-two energy block is positive throughout the proposed stable interval; at the all-or-none endpoint the omitted tracker-difference direction still decays through the explicit tracker replacement recursion. At and beyond the threshold, the moment operator has an eigenvalue at least one, so uniform mean-square decay for all initial states is impossible. The full covariance map gives deterministic witnesses above the boundary. Exact arithmetic verifies the critical identities; numerical spectral checks do not replace proof.

## Originality — PASS, with priority risk

The source algorithm supplies arbitrary subset sampling but not the sharp correlation-dependent threshold. General arbitrary-sampling SAGA prior theory supplies sufficient complexity bounds. The closest published exact calculations concern exactly one selected row per iteration: nonuniform singleton probabilities on two rows and uniform singleton sampling on any number of rows. Those do not imply a sharp ordering for distributions containing empty and two-row subsets at fixed row marginals. Searches by algorithm names, subset correlation, identical-row specializations, variance/covariance and equivalent SAGA/JacSketch formulations did not reveal the same classification. Unindexed equivalent derivations remain possible; this review does not assert exclusive worldwide priority.

## Value — PASS

The result isolates a materially important design distinction: sampling frequency and expected minibatch cost alone fail to determine robust stochastic stability. The sharp endpoints differ by a factor above 2.5 on a fully coherent, perfectly conditioned least-squares problem. A complete boundary and exact mathematical certificate provide a reproducible stress test for correlation-aware subset-sampling designs, rather than a routine stepsize example.

## Closest literature and limitations

The primary method is Xie–Qi–Han (arXiv:2610.39537v1). Qian–Qu–Richtárik (arXiv:1901.08669) treat arbitrary-sampling SAGA; Gazagnadou–Gower–Salmon (arXiv:1902.00071) treat minibatch SAGA. Published exact singleton frontiers supply the closest specialized comparisons. This is a two-row rank-one robust all-initialization statement; no optimality for arbitrary systems, computational cost, or practical noise is claimed. No independent mathematical audit or exhaustive priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.

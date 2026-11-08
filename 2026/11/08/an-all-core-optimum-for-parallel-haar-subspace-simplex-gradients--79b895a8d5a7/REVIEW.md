# Self-review

## Correctness: PASS

The proof is reconstructed from the log-Gamma quotient, its two-step recurrence and the digamma integral representation. The bound \(L(s)<1/[2(s-1)]\) holds strictly for real \(s>1\), establishing strict decrease of \(H_c(s)\) beyond \(c+2\). Every integer subspace size is partitioned by the ceiling-cost batch. Equality and all boundary cases (one core, two cores, fewer dimensions than cores, and the opportunistic one-dimensional evaluation) are addressed. The separately runnable checker passed 460267 finite comparisons, but the proof is the analytic inequality, not the enumeration.

## Originality: PASS, qualified

The closest paper is Hare, Roberts and Royer, *Expected decrease for derivative-free algorithms using random subspaces*, first posted 2023-08-09 (arXiv:2308.04734), especially Theorem 4.2 and Section 4.2. It already supplies the score formula, cost model, and two-core tie, and reports only finite numerical evidence for the all-core rule. The new contribution is the complete analytic all-integer proof, including partial batches. Roberts and Royer (arXiv:2204.01275) and Kozak et al. (arXiv:2003.02684) have distinct random-subspace objectives and do not imply this precise allocation theorem on inspected content. A complete publisher-hosted journal revision was not accessible; the possibility of a prior stronger formulation remains a nonzero publication-precedence risk. Similarity search alone is not novelty certification.

## Value: PASS

Subspace dimension creates a genuine trade-off between stronger expected linear-model descent and the number of sequential evaluation rounds. This result closes an explicit bounded numerical observation with a sharp all-integer classification and determines precisely when the optimum is nonunique. It is valid for the natural exact Haar model-based score and ideal parallel timing assumption, not a theorem about real machine latency, nonlinear convergence, or arbitrary derivative-free algorithms.

## Limits

All averages are for the cited linearized Haar benchmark; costs assume equal-duration evaluation rounds with a sequential final evaluation. The numerical verifier is supplementary. Publication precedence requires later independent review, particularly of the 2024 journal version.

Self-review: passed. Independent audit: not yet performed.

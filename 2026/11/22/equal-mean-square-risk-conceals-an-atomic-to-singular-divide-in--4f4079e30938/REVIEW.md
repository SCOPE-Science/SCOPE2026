# Review of the minibatch-partition stationary-law separation

## Correctness — PASS

The scalar equal-curvature assumption is essential. The epoch reduction is exactly affine; a fixed random partition has zero conditional noise mean, so holding it for future epochs changes higher-order dependencies but not unconditional epoch-to-epoch covariance. The finite-population identity, Gaussian-moment formula, and balanced four-label partitions were independently reconstructed. The self-similar stationary series converges absolutely for the stated normalized stepsizes. For strictly disjoint three-map images, the Cantor dimensions follow from cylinder contraction and entropy; at the ternary boundary, atypical digit frequencies yield a continuous singular law on a full interval. An exact-rational checker in this package returned `VERIFY_OK 236`. Finite tests guard finite algebra rather than substituting for infinite proofs.

## Originality — PASS (historically qualified)

Kumar (2026, https://optimization-online.org/wp-content/uploads/2026/11/minibatch_rr.pdf) develops a fixed-partition minibatch method, already includes the batch variance identity, and explicitly identifies independent repartitioning across epochs as an unresolved setting. Ying et al. (2018, https://arxiv.org/abs/1803.07964) analyze mean-square reshuffling; neither is credited with this exact fresh/frozen distributional separation. Two close published results classify Bernoulli-convolution supports for respectively two and three **unbatched** components; their explicit assumptions and conclusions do not subsume the four-sample randomly partitioned benchmark. Search comparisons concern equivalent claims and implications, not titles alone. No database absence is interpreted as novelty proof. The full text of Domingo-Enrich (2022) was not available during this comparison, and unindexed equivalent studies remain possible. The finite-population variance formula, fractal-set dimension theorem, and generic IFS method are not claimed new.

## Value — PASS

Equality of every finite-epoch mean-square risk cannot distinguish an exact mass at the minimizer from a purely nonatomic stationary distribution; at the sharp critical step even full interval support coexists with singularity and Gaussian kurtosis. This benchmark addresses an explicitly motivated fresh-partition modeling gap. The small data size is structurally minimal for nontrivial equal-size batching, not an arbitrary numerical slice.

## Scope and limits

Only scalar, equal-curvature, strongly convex quadratic components are covered. Full stationary support classification is for the centered four-data, two-batch construction. The result does not establish general optimization-rate dominance or almost-sure convergence of individual ongoing trajectories. Historical priority and the proof have not been independently audited.

Self-review: passed. Independent audit: not yet performed.

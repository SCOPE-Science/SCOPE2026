# Review: optimal dephasing on a trapped friendship network

## Correctness — PASS

The precise trace-decreasing Lindblad generator, graph and rate conventions are defined in `RESULT.md`. The quantum dissipator has strictly negative spectral real part for every positive dephasing rate by the Hilbert–Schmidt quadratic form and graph connectivity. The eighteen real orbit coordinates are exhaustive under the trap stabilizer; their generator is affine in the number of indistinguishable triangles, allowing an exact rational symbolic solution. The supplied executable code reconstructs the generator and certifies the rational identity, two globally valid coefficientwise positive polynomial lower bounds, critical scaling and derivative. Fifteen full complex-Liouvillian comparisons provide an independent finite-dimensional numerical cross-check. The proof explicitly excludes zero dephasing and arbitrary trap rates from its asymptotic claims.

## Originality — PASS on examined evidence, with residual priority risk

Plenio–Huelga (arXiv:0807.4902) develops the qualitative dephasing-assisted mechanism, while Caruso et al. (arXiv:0901.4454, sections II and Appendix A) give complete fully connected network formulas and demonstrate dark-state effects. Neither paper gives the friendship-graph rate-two peripheral trapping mean or the exact scaling profile and optimal constant. A closely motivated exact star-network calculation has no within-triangle edges and therefore does not imply this topology-specific rational profile. Broad searches for friendship/windmill graphs, local dephasing, and peripheral sinks found no corresponding formula, although incompleteness of the accessible indexed literature remains possible. The comparison is about the mathematical statements, not only differing graph names.

## Mathematical value — PASS

Friendship networks isolate a physically interpretable local motif (triangular coherent interference) while holding the hub-bottleneck architecture fixed. The finding identifies both the exact performance exponent and a nontrivial, unique optimally scaled noise strength. The sharp function and coefficient differ from those of a star, giving a quantitative benchmark for noise engineering and demonstrating that adding triangles changes capture kinetics beyond merely changing the total vertex count. The global lower bounds distinguish an actual all-noise optimum from a chosen scaling limit; this is more than a routine finite enumeration.

## Limitations and closest literature

The proof is only for unit hopping, unit-dephasing convention, trap population-loss rate two and a starting peripheral in a different triangle. It does not describe transient trapping probability or arbitrary dephasing/trap parameters. The full Caruso et al. preprint was examined, including the fully connected model and Appendix A. Plenio–Huelga was inspected for generator and chain results. Lloyd–Mohseni was consulted at abstract level for symmetry-based physical motivation, not treated as full-text negative evidence. A specialized unpublished or unindexed friendship-network calculation may exist. Finite Liouvillian tests are not infinite proofs. Priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.

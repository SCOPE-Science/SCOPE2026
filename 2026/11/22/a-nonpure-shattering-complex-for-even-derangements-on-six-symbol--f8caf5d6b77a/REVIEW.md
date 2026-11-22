# Scientific review of the even-derangement incidence complex

**Correctness: PASS.** The 130 even fixed-point-free permutations are independently enumerated by two parity methods. Every potentially shattered support is a partial matching, so exhaustive enumeration of these supports through size five is complete; absence of five-faces excludes larger faces by heredity. Two independently compiled/interpreted verifiers agree on face counts, all facet sizes, and the exact GF(2) boundary ranks. Python independently checks the simultaneous-relabeling facet orbits. The result is finite; no infinite theorem is inferred from enumeration.

**Originality: PASS within the inspected record.** The closest published record gives shattering for all derangements on six points, not the even-sign subfamily; removing concepts can invalidate shattered supports and change homology. The closest primary graph-derangement paper studies derangement/intersection proportions, rather than Boolean traces, facet orbits or simplicial homology. The current work differs in claims and implications, not merely labels. Bibliographic priority is not certified; older unindexed parity-restricted tables remain possible.

**Value: PASS.** Parity-constrained perfect matchings on the diagonal-deleted board form a canonical algebraic restriction. The full derangement family shatters every four-cell nonattacking rook placement, whereas its even-sign subfamily loses 1575 such faces and gains 360 lower-dimensional maximal faces. The two nonzero homology degrees and five total facet orbits quantify a real structural change missed by the shared VC dimension four. This is a motivated complete finite classification, not a general claim or an arbitrary numerical refinement.

**Remaining limitations:** Only six symbols; mod-two rather than integral homology; priority may be affected by unindexed computations. Both mathematical verifiers are included in the package.

Self-review: passed. Independent audit: not yet performed.

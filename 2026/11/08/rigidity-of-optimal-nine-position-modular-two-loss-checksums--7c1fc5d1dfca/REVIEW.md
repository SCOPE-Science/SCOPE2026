# Scientific review: optimal nine-position two-loss checksums

## Correctness
PASS. The claim is finite and exactly specified: nine distinct residues modulo 56 with all 36 distinct-index pair sums different. The complete increasing-prefix depth-first search checks a necessary and sufficient condition at every extension and thereby enumerates every valid set containing zero exactly once. The standalone checker returns 216 anchored sets in 3,455,863 recursion nodes, independently generates the 1,344-element affine orbit and verifies equality. Incidence double-counting gives 1,344 total sets. An independent C++ search reproduces the anchored count and unique affine orbit. The historical assertion that 56 is the minimum modulus comes from the cited 2004 enumeration, rather than the new finite checker.

## Originality
PASS on available evidence, with a concrete historical risk. Ye et al. (arXiv:2608.08018, Section III-C) state the weak-set checksum framework, but their tabulated finite construction ends at the eight-coordinate two-loss case. Haanpää–Huima–Östergård (2004) establish the nine-element cyclic minimum 56, and Haanpää–Östergård Report A87 reports group maximum sizes and sample sets while explaining equivalence. These facts imply existence and minimality, but do not imply that all optimal sets form exactly one affine orbit or give the counts 216 and 1,344. OEIS A004135 and A260998 repeat size information, not the complete class count. The full 2004 cyclic-journal text was not available for an independent full-text comparison; its potential unpublished orbit enumerations are a priority risk. Meaning-based literature and mathematical-record searches found no statement covering the classification.

## Value
PASS. A previously known small modulus does not tell an encoder designer whether it admits fundamentally distinct nine-position syndrome mappings. The complete affine-rigidity result answers that structural question at the first case outside the 2026 weak-set table. Since affine coefficient changes merely relabel fixed-weight two-loss syndrome outputs, all optimal nine-position checksum sets have the same intrinsic pair-localization pattern. The result is narrower than a general channel theorem but resolves a natural complete classification, with reproducible certificates.

## Scope and residual limitations
Exactly two losses, with known loss count; modulus 56; nine distinct positions. Pairwise distinct-index sums only. No result for multiple erroneous rows or higher-order loss classes. Full historical priority and independent mathematical validation remain unsettled.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness — PASS

The greedy embedding lemma follows by comparing positions of successive letters inside a strictly increasing permutation block; a nonincreasing adjacent transition consumes a new block. For a cyclic query, a cut omits exactly one edge, so the worst rotation of a nonconstant word requires one more block than its cyclic weak-descent count; for constants the correct boundary is instead the length. These two cases produce the precise acceptance criterion. The weighted trace has a direct closed-walk interpretation, and Burnside's fixed rotation formula uses repetition multiplier \(d\); adding the constants precisely when \(h=k\) avoids an off-by-one boundary. Longest-length and near-maximal classification follow from the unique decomposition into strictly increasing arcs. The two-defect argument proves all arc boundary inequalities automatically because a violated boundary would need at least \(q\ge3\) omissions. The finite verifier tests direct embeddings and all cyclic rotations, and checks the Burnside coefficients and defect classification independently. The infinite theorem is proved symbolically, not inferred from these tests.

## Originality — PASS (with residual bibliographic risk)

Three primary preprints were examined at the level of their definitions and substantive relevant theorem sections. Kosche et al. distinguish matching against a rotated host; this theorem requires matching every rotation of the **query** against an unrotated repeated-permutation host. Fleischmann et al. address full scattered-factor universality of a host across all queries, rather than the all-conjugates condition for each query necklace. Hirakawa et al. count Lyndon subsequences, not rotation-complete necklace classes. Published-record searches for rotation-complete scattered subsequences, cyclic weak-descent necklace formulas, and permutation-power all-conjugates conditions found no exact match. Accessible earlier claims about factor Lie complexity, host circular universality, and reverse-complement subsequences do not imply the present statement. The source searches are not a proof of worldwide priority, and an unindexed equivalent or special-case theorem remains possible.

## Mathematical value — PASS

The question asks which *cyclic query patterns* can be recognized in all orientations by a finite, highly structured subsequence host. It is a natural intermediate invariant between ordinary subsequence presence and universal hosts. The result supplies an exact enumeration for every alphabet size, host repeat count and query length, and goes beyond an algorithm by giving a sharp maximum and complete top-three-layer classifications, including nontrivial parity dependence at the second defect. This distinguishes query-rotation closure from the better-studied host-rotation and ordinary Lyndon-counting problems.

## Principal sources and limits

- Fleischmann, Germann and Nowotka, arXiv:2104.09063, definitions and circular/universality results.
- Hirakawa, Nakashima, Inenaga and Takeda, arXiv:2106.01190, introduction and counting results.
- Kosche, Koß, Manea and Pak, arXiv:2207.09201, bounded-range definitions and circular matching results in Section 5.
- Exact formulas are restricted to a fixed linear host consisting of repeated distinct-letter permutation blocks. Reproduction scripts test finite configurations and do not replace the general proof.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

**Claim assessed.** Every labeled maximum four-list code in the ternary unordered-multiset channel with two survivors and source length \(n\ge4\) is one of the two explicitly enumerated families in RESULT.md, and the total number of optimal codebooks is \(12n-36\). The maximum cardinality \(11\) is background, not an originality claim.

## Correctness (C): PASS

For any eleven-codeword family, the total monochromatic parent incidence is at most twelve, while at least \(22-T\) where \(T\) counts one-heavy messages, forcing \(T\ge10\). If \(T=11\), only deleting a three-symbol-support one-heavy word can repair all three initially overloaded mixed received outputs. If \(T=10\), both monos for the two-heavy word are saturated; the two removals must have different heavy labels. Exact inspection of the three mixed outputs forces the three edge alternatives and unique interior alternative. No other word has zero or three heavy coordinates in an optimal code. Each surviving case satisfies all six loads by direct counting. Disjointness and counting give \(3+3(3(n-3)+n-4)=12n-36\). All bounds and quantifiers hold for every integer \(n\ge4\), including empty interior ranges. Source code in checks/brute.py and checks/structural.py independently enumerates 12 and 24 optimal codes at n=4,5 and the full constrained candidate census for n=4..40; their outputs are packaged.

## Originality (O): PASS against accessible primary and indexed evidence

The known high-list result explicitly reports the four-list size eleven as already established; the claimed novelty excludes this size. That result proves the higher-list cardinalities (L at least five) and rigidity only for even L at least six, and contains no codebook classification for four-list equality cases. The general low-list result requires L no greater than the survivor size two. The January 2026 primary paper and March follow-up address principally unique decoding, constructions and deletion-ball geometry; neither gives the four-list codebook census. published-finding corpus semantic queries, specific parameter and alias queries, connected public-result full text, and public web searches found no implication that already yields the two-family classification or the exact count. This is evidence-based priority, not a proof of global novelty; an unindexed optimizer census is the main residual risk.

## Value (V): PASS

For a natural worst-case multiset deletion channel, codebook *capacity* alone leaves the number and structure of extremizers unresolved. The complete optimizer classification describes the equality topology of the three monochromatic and three mixed received-pair loads, exhibits a sharp difference between one-heavy-only and one-replacement optima, and counts all labeled optimal codes at every block length. It can be used to sample or compare extremal decoder designs and quantifies optimal-design diversity. The classification is not an arbitrary tiny computation: it is an infinite all-length exact structural result, and the prior even-list rigidity does not extend verbatim to four-list equality.

## Closest sources and limitations

- A. Kreindel, I. Barouch Essayag and A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Syndrome Constructions, Bounds, and Exact Results*, arXiv:2601.05636, first public 9 January 2026. This determines unique-decoding cases, not four-list optimizer counts.
- Same authors, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322, first public 18 March 2026. Primarily unique decoding and shadow geometry.
- *High-list saturation for ternary two-symbol multiset deletion codes*, public scientific RESULT.md in published-finding corpus/2026. Known four-list cardinality is expressly acknowledged; results for L at least five do not imply the asserted four-list classification.
- *Sharp list-capacity plateau for high-deletion multiset channels*, public scientific RESULT.md in published-finding corpus/2026. Requires list allowance at most survivor size (two), not the present four-list case.

The theorem counts distinct subsets of labeled-alphabet multiset vectors; no orbit count under alphabet permutations is asserted. Finite checkers are supplementary and do not independently establish infinite correctness. Published equivalent work not indexed or accessible remains possible.

Self-review: passed. Independent audit: not yet performed.

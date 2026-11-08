# Scientific review: mixed-alphabet online neighborhood dimensions

## Correctness — PASS
The theorem concerns only the exact *online* Littlestone dimensions. A coordinate-line/two-center common-positive-fiber argument proves the universal online upper bound three for both conventions. For two-row rook graphs a separate negative-fiber argument proves the nontrivial closed online bound two, even when the alphabet of the other factor is unbounded. A positive-fiber cardinality argument proves the open (2,3) exception; explicit shattered supports supply lower bounds where static rank three, and two eight-leaf complete online decision trees supply the strict (3,3) gap. An independent standard-library checker confirms 26 finite concept-family comparisons and both complete adaptive trees. Pre-existing static VC values are shown for comparison, not claimed as new.

## Originality — PASS, subject to priority uncertainty
Earlier mathematics already contains the complete heterogeneous closed-neighborhood **VC** formula, the open rectangular-rook VC polynomial, and equal-alphabet online dimensions for both open and closed neighborhoods. Those prior claims were compared by implication and are explicitly excluded as separate originality assertions. They do not settle the exact **online** dimension of heterogeneous closed rectangles: a class with static VC rank two can have online rank either two or three, as the square ternary rook example demonstrates. Nor do they yield the full mixed-parameter online classification. The original 2020 Hamming article treats static open VC only. Published semantic searches and available prior claim texts revealed no equivalent general online table; unindexed historical coverage remains a risk.

## Mathematical value — PASS
A natural, complete two-invariant adaptive classification for all mixed-alphabet Hamming graphs determines the worst-case realizable online membership-mistake bound without distance-transitivity. The infinite family of two-row rook graphs exhibits a sharp open/closed online divergence: the closed bound stays at two regardless of the other factor's size, whereas the open bound jumps at alphabet four. The contrast between VC and Littlestone rank two versus three shows this online conclusion is not a mechanical consequence of the earlier static formula. The classification sharply determines which full products exhibit a static/adaptive gap.

## Limits
The online formulas assume complete Cartesian products with \(q_i\ge2\), not arbitrary induced subgraphs, other radii or code-restricted hypotheses. All static VC numbers included in the comparative table are prior results, even where their short proofs appear for completeness. Independent proof validation and absolute historical priority have not been established.

Self-review: passed. Independent audit: not yet performed.

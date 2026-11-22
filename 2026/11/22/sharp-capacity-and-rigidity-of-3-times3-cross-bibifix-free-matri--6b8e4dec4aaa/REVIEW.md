# Scientific review

## Correctness — PASS
The definition quantifies over all ordered matrix pairs, including a matrix paired with itself, and both proper square-overlap sizes. Disjoint top-left and bottom-right alphabet sets follow at size one. At size two, equality occurs only between uniquely indexed left/right matrix classes, which form complete bipartite conflict components; this is a direct exhaustive partition of the unrestricted candidates. Their independence numbers, the exact unused-center count, and the unique integer maximizer prove the all-alphabet upper bound and constructions. Binary equality was checked by direct matrix enumeration and by an independent integer program. The proof—not finite experimentation—establishes the all-alphabet result.

## Originality — PASS, with stated priority risk
Blackburn (arXiv:1303.1026, Section 4, Theorem 5) already gives the exact *one-dimensional* three-letter non-overlapping code capacity. Barcucci et al. (arXiv:1502.05275, Section 4) already lift such codes into cross-bibifix-free matrix codes, establishing the matching lower bound but not an upper bound for arbitrary matrix codes. The newly proved conflict-graph decomposition establishes that the lower bound is universally sharp and classifies all equality cases, including binary non-lift optima. Searches for diagonal square overlaps, matrix bibifix codes, and optimum codebooks found no dominating two-dimensional result. The closely named general-translation matrix literature studies a stronger and distinct condition. An inaccessible full text of one such later paper and unindexed equivalent graph formulations remain priority risks.

## Value — PASS
This is a natural first nontrivial square dimension in the two-dimensional synchronization model; it gives sharp capacity over every alphabet and an equality-case rigidity transition, not merely a new construction. It shows that one-dimensional lifts are forced for alphabets of size at least three even though off-diagonal degrees of freedom could potentially avert overlaps, while binary alphabets exhibit 28 genuinely non-lift equality cases. The theorem resolves a basic finite-dimensional optimization and supplies a closed-form design count. It does not purport to solve higher dimensions or stronger translation-overlap models.

Self-review: passed. Independent audit: not yet performed.

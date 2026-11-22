# Self-review

**Final claim.** For the symmetric-edge polytope of each unweighted cycle of order \(n\ge3\), the sharp vertex-generation weight equals \(1/(n-1)\) when \(n\) is odd and \(1/(n-2)\) when \(n\) is even; the corresponding Schneider indices are \(n-2\) and \(n-3\). The single all-order theorem and its two-simplex free-sum lemma are fully specified in `RESULT.md`.

## Correctness — PASS

The polar is the exact zero-sum section of a cube. Its vertices have the claimed parity structure, and the associated facets are either simplices or affinely independent free sums of two centered simplices. The free-sum gauge and the vertex-cover criterion are reconstructed in the proof, with the sharp uncovered boundary witness for every larger weight. General facet inheritance and centrally symmetric boundary lifting are established in Artstein-Avidan–Falah–Slomka, Lemmas 2.2 and 5.1. The code verifies 1,154 polar facets and 4,120 exact rational points for small parameters. Finite tests are not infinite proof. Risk: an algebraic oversight in the all-parameter covering lemma is the critical step; the gauge inequalities and boundary witness were checked symbolically as well as numerically.

## Originality — PASS (provisional historical priority)

The 2018 and 2021 cycle graph literature provides facet combinatorics, and the 2024 vertex-generation article provides general principles; none of the inspected material states the numeric odd/even index or the free-sum gauge formula. Read the full publicly available main results and proofs for cross-polytope skeleta, hypersimplex vertices, demihypercube covering, planar polygon bounds, and product-of-simplices skeleta. Their invariants have the same normalization but apply to different polytopes and do not imply the cycle theorem. Other checked cycle-polytope results concern facet or Euclidean invariants, not this affine convexification coefficient. Exact searches, implication comparisons and source material are catalogued in `AUDIT.json`. Residual risk: an unindexed equivalent result or an inaccessible recent general convexification preprint; historical priority is not definitively certified.

## Mathematical value — PASS

The coefficient is a natural sharp global covering invariant studied in recent convex geometry. The parity dichotomy is determined by a nontrivial change in facet structure, and the proof yields a reusable exact invariant for the free sum of any two centered simplices. The result distinguishes whole-body vertex covering from mere face enumeration and supplies a concrete testing family for convexification theory. It makes no claim to solve the general graph case.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness — PASS

The statement concerns the ordinary geometric quotient by a prime target-color cycle, not source-position permutations or a homotopy orbit space. Every nonidentity prime cycle acts transitively on target colors; because each Hom cell has three nonempty disjoint color blocks, a fixed point would require an impossible triple of invariant subsets. This makes the quotient a regular covering with simply connected total space by Babson–Kozlov [1,2]. Cartan–Leray with rows only in degrees zero and \(p-3\) establishes every claimed lower integral group. Cellular dimension and Euler characteristic prove that top homology is free and fix its exact rank. The cohomological spectral sequence establishes the multiplicative classifying-map isomorphism only below \(p-3\); the exact cup-length follows from one nonzero borderline product in degree \(p-4\) and a dimension/graded-commutativity upper bound. The independent signed-cell verifier found the predicted mod-prime ranks for \(p=5,7\), checked all integer boundary compositions, and found the Smith factor five at \(p=5\). These checks are finite corroboration, not infinite proof.

## Originality — PASS relative to inspected literature

The 1997 ordered-disjoint-block theorem [1] and 2003 Hom-complex classification [2] cover the *unquotiented* connectivity and sphere counts, not integral cohomology of prime target-color cyclic quotients. The two closest public complete-graph Hom results [3,4] were read in full in their substantive `RESULT.md` files: both classify rational target-color characters and rational full/alternating quotient invariants, and explicitly leave integral cyclic torsion and multiplicative products undetermined. Neither of those rational theorems implies integral torsion or the exact mod-prime cup-length. The cyclic chessboard Bockstein [5] is structurally analogous but its covering complex is a rook-placement complex, not the present ordered three-block Hom complex. The exact family-level integral and multiplicative classification was not located in targeted semantic and primary-literature searches. Remaining risk: an unindexed earlier formulation using deleted products, Borel spectral sequences or another group-quotient notation may subsume it; completeness of publication priority is not certified.

## Value — PASS

The natural problem is to understand how cyclic relabeling of colors changes the topology of spaces of multicolorings of a triangle. The known covering spaces have free homology in one high dimension, while the quotient exhibits a full sequence of nonzero *integral* torsion groups and a precise, unbounded mod-prime cup-length. The cup-length is an exact multiplicative invariant, not a rational character or a restatement of the sphere count; it detects product structure missed by rational symmetry methods and supplies an explicit lower bound for Lusternik–Schnirelmann category. The object and invariant are natural across every prime, so this is not an arbitrary finite slice. The proof transparently uses classical connectivity and spectral-sequence tools; those inputs are prior work and their use alone is not a novelty claim.

## Closest literature and boundaries

[1] https://arxiv.org/pdf/math/9704227 (1997-04-29), Sections 1 and 6; ordered-block complex and distinct block-permutation quotients.

[2] https://arxiv.org/abs/math/0310056 (2003-10-05), Sections 1 and 4.3; complete Hom connectivity and sphere-count formulas.

[3] https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-color-permutation-characters-of-complete-graph-hom-complexes--50c1a3944425; full `RESULT.md` inspected, rational target character.

[4] https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-full-two-sided-symmetry-character-of-complete-graph-hom-complexe--ce942485ca98; full `RESULT.md` inspected, rational source/target character.

[5] https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-nontrivial-mod-five-bockstein-cup-product-in-the-cyclic-chessb--19b7184f8768; only indexed summary inspected, distinct chessboard complex.

The general mod-prime ring *above and at* degree \(p-3\), top integral action lattice, and full homotopy classification are unproved. Unindexed equivalent formulations remain an originality risk.

Self-review: passed. Independent audit: not yet performed.

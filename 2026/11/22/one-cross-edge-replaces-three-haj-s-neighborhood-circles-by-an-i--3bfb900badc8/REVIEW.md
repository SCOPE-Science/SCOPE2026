# Review of the cross-edge neighborhood-homology finding

## Correctness — PASS

The proof gives an explicit five-piece cover of the pre-addition complex, exactly two new simplex attachments, their full intersections, and four attaching loops with a saturated rank-three integral boundary matrix. The long exact sequence establishes the stated integral homology and split inclusion maps, without assuming a wedge-of-spheres result for the new space. The standard-library verifier directly reconstructs all nine small sample cases from graph neighborhoods, checks relative attachment identities, and independently computes mod-two boundary ranks. Limitation: finite tests alone do not establish the all-order statement; the uniform combinatorial identities do.

## Originality — PASS with residual bibliographic risk

Braun–Vega, arXiv:1812.07991v1 (Theorem 3.3 and its proof) treats a Hajós merge but not insertion of the additional edge or its induced integral homology map. The publicly indexed result on partially matched clique pairs assumes two *disjoint* cliques joined by matching bridges, not a Hajós identification, and therefore does not imply the new attaching matrix. An indexed block-graph theorem has inapplicable clique-block hypotheses. Queries included the exact graph construction, aliases (Hajós join/sum), one-cross-edge perturbations, neighborhood homology, and stronger possible edge-restoration classifications. The full source text for the closest disjoint-clique record could not be accessed, and any unindexed equivalent work remains a risk.

## Value — PASS

The result sharpens a topology–graph-coloring construction question: one local graph-edge addition can simultaneously annihilate three independent integral first-homology classes and create a new primitive two-class. It gives an exact all-size and all-choice formula plus the maps induced by the change, rather than an isolated facet count. This is a natural minimal cross-link perturbation of the two-clique Hajós construction; no larger general theorem is suggested without evidence.

Self-review: passed. Independent audit: not yet performed.

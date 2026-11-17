# Review of the bounded-slope tree projection finding

## Correctness — PASS

The statement concerns one precise map, Euclidean projection onto the finite tree's symmetric bounded-edge-difference polyhedron, and one two-input graph-total-variation seminorm. The active-set argument establishes that every forest of tight edges occurs with strict complementarity and gives the block-average Jacobian. A one-edge-cut basis computes its exact norm, with an explicit weighted boundary-count formula. Optimizing the components yields the sharp all-tree formula; the degree-sum argument proves a \(3/2\) discontinuity between contractive and noncontractive shapes, and a broom witness attains the full sharp fixed-order envelope. The projection is piecewise affine, so derivative gains give actual ratios of nearby *finite* input pairs. A standalone exact rational checker verifies 1,441 labeled trees, 43,614 active-set faces and distinct primal-dual KKT witnesses; none of the infinite-family claims is inferred from enumeration.

## Originality — PASS, with residual priority risk

Yeganova–Wilbur (2009) address monotone Lipschitz-isotonic regression on the line, and Agarwal–Phillips–Sadri (2009) address monotonicity/unimodality-constrained tree regression algorithms. Kyng–Rao–Sachdeva–Spielman (2015) optimize Lipschitz extensions of fixed labels rather than an all-observations nearest-point projection. The inspected mathematical statements do not imply the exact connected-subtree graph-variation gain, the path-or-claw contractivity classification or the fixed-order extremal envelope. Related published findings about edge-gradient orthoprojectors and descendant averaging concern different operators and likewise do not subsume the claim. Semantic searches under bounded-slope, slab projection, graph variation, connected averaging and equivalent cut formulations identified no decisive coverage. An unindexed publication deriving the same result remains possible, so originality is a best-knowledge scientific conclusion rather than a certificate of priority.

## Mathematical value — PASS

The variation sensitivity of a smoothness-constrained least-squares estimator controls how changes in observations can alter graph-edge roughness. A sharp tree formula is structurally different from the ambient Euclidean nonexpansivity and ordinary norm equivalence. The exact stability class consists of paths and the four-vertex claw, while every other tree has a quantitative gap of at least one half beyond nonexpansivity. The worst attainable amplification grows as \(n-2\sqrt n+1+O(n^{-1/2})\), showing a sharp nearly linear branching effect. Each of these is a natural, fully classified feature of the same estimator, with concrete finite witnesses.

## Closest literature and limitations

The relevant lead works are Yeganova–Wilbur, *Isotonic Regression under Lipschitz Constraint* (first public online 2009-01-07, DOI 10.1007/s10957-008-9477-0); Agarwal–Phillips–Sadri, *Lipschitz Unimodal and Isotonic Regression on Paths and Trees* (arXiv:0912.5182, first version 2009-12-28); and Kyng–Rao–Sachdeva–Spielman, *Algorithms for Lipschitz Learning on Graphs* (arXiv:1505.00290, first version 2015-05-01). The new theorem uses unweighted squared errors, symmetric positive edge caps and unweighted tree variation; general graphs, weighted observation laws and nonuniform variation weights are not treated. The finite reproducibility checks are supplementary, not substitutes for the all-dimensional proof. Historical priority remains provisional pending independent review.

Self-review: passed. Independent audit: not yet performed.

# Scientific review: facet-area condensation in complete-bipartite graphical zonotopes

## Correctness — PASS

The exact domain is the unit-segment graphical zonotope of \(K_{2,q}\), with integer \(q\ge2\), inherited Euclidean metric, and intrinsic area/volume. The central geometric step is the connected-cut facet criterion; the face is an orthogonal product of the induced-subgraph zonotopes. The standard spanning-tree zonotope-volume rule yields each facet area, and a complete cut classification gives precisely the two claimed area families and their multiplicities. The binomial fourth-moment bound proves the surface concentration with its error term. The direct convex-hull checker separately computes each facet area and the total volume for \(q=2,3,4\); its numerical extrapolation is not used as a proof.

## Originality — PASS, subject to residual historical risk

Chapoton–Pilaud (arXiv:2201.06896, pp. 9–12, 18–19 and Appendix A) gives the facet combinatorics of graphical zonotopes and, in particular, complete-bipartite facet counts; it does not give Euclidean areas of the individual facets or their size-biased concentration. Dall–Pfeifle (arXiv:1404.3876) establishes the general matroid-zonotope volume relationship, which supplies an ingredient but does not state the specific two-hub area law. Padrol–Pilaud–Poullot (DOI:10.1007/s00454-023-00586-x) treats deformations, not facet-area distributions. Related geometry of tree graphical zonotopes and Euclidean inballs/covariance of complete-bipartite zonotopes concerns different invariants. The claim is not that the facet-count identity or the spanning-tree volume formula is new. Residual risk: an earlier unindexed application of those general ingredients may already report the same area spectrum or concentration.

## Mathematical value — PASS

The two-hub complete-bipartite graphical zonotopes form the first non-tree complete-bipartite family and a natural shuffle building block. The complete metric facet-area spectrum contrasts exponentially numerous facets with a surface-area measure asymptotically supported on only linearly many facets; the vanishing-uniform-facet-mass versus near-total-area contrast is a precise geometric boundary-concentration phenomenon. The exact leading constant \(2\) and rate \(q^{-3/2}\) are not supplied by the known facet count. The result is a natural structural metric classification, not an arbitrary finite computation or a claim of generality beyond its proven domain.

## Scientific limitations

The statement is limited to the unweighted standard realization and does not infer corresponding laws for general complete bipartite graphs, other generator scalings, or different Euclidean metrics. Earlier equivalent findings outside the compared sources remain possible. Numerical verification was finite.

Self-review: passed. Independent audit: not yet performed.

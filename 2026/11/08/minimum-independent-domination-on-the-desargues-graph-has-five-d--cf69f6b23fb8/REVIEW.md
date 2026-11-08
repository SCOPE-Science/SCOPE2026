# Scientific review

## Correctness

PASS. The lemma \(B=F(A), A=F(B)\) is both necessary and sufficient. Exactly 1024 left masks are checked by the first program, yielding 187 maximal independent sets and exactly 100 minimum six-vertex ones. Independently, the second program checks all \(2^{20}\) vertex subsets of \(GP(10,3)\) up through cardinality six. Separate transition constructions verify exactly 120 moves, 10 isolates and five 18-state components with degree profiles \((4^6,2^{12})\), a doubled six-cycle subdivision, and common eccentricity six. The explicit matching/path/triangle classification is independently generated and checked against the closure list; all source programs and actual outputs are supplied.

## Originality

PASS, with historical-priority risk. No relevant inspected work determines the claimed fixed-host graph. Suzuki, Mouawad and Nishimura (2014, arXiv:1401.5714) treat addition/deletion transitions on nonnecessarily independent dominating sets of varying size, which do not imply the minimum independent-set slide graph. Kazemi (2010) proves bounds on a different generalized Petersen subfamily \(GP(2k+1,k)\), not this \(GP(10,3)\) census. Dorbec and collaborators (2015) study broad bounds for cubic graphs, but only the abstract was accessible, which is a residual uncertainty. Related exact homotopy results for the Desargues independence complex concern a different invariant; a homotopy type does not determine adjacency among minimum maximal independent faces. General jump-versus-slide coincidence for independent domination is elementary and is not attributed as a novel contribution.

## Value

PASS. The Desargues graph is a canonical symmetric cubic incidence graph. Classifying the entire optimal independent-dominating layer shows the coexistence of ten locally frozen optimum configurations and five unexpectedly mobile eighteen-state components, with an exact doubled-hexagon structure and sharp diameter. This provides a natural benchmark for maintaining coverage and pairwise nonadjacency while relocating devices, rather than merely giving another minimum cardinality. The structural fivefold decomposition is not implied by cubic domination bounds or the number of optimal configurations.

## Limitations

The theorem addresses one host graph and one move rule; no wider family result is claimed. Unindexed equivalents are not excluded, and not every broadly related full article was available. Verification is same-source mathematical and programmatic review, not an independent scholarly assessment.

Self-review: passed. Independent audit: not yet performed.

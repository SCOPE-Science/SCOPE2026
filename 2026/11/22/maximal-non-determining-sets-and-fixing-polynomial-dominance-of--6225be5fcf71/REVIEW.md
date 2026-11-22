# Review of the fixing-polynomial comparison

## Correctness — PASS

Pointwise-stabilizer failure is exactly containment in a nonidentity automorphism's fixed set. The root-neighborhood six-cycle bounds Shrikhande automorphisms by 192; twelve explicit connection-preserving matrices and sixteen translations meet this bound. Seven distinct order-four kernels yield precisely 28 maximal cosets. The rook group is the full wreath-type row/column group; its nonidentity fixed sets yield precisely twelve slabs and twenty-four transversals. Exact subset counts follow from finite intersection counting; positive polynomial coefficients yield the entire Bernoulli reliability comparison. An independently written graph-isomorphism-based verifier and a formula-based verifier each check all 65,536 subsets on each graph. No infinite-domain assertion is made.

## Originality — PASS, with historical priority risk

Boutin (2006) establishes the fixing/determining notion and stabilizer methods, and Boutin (2009), Lemma 1, supplies a more general Cartesian-product criterion, explicitly **covering the general rook membership test**. These precedents are credited. An earlier centroidal-locating census on this same graph pair already establishes the twelve failing rook eight-slabs and a stronger nine-sensor rook guarantee, which implies our nine-set fixing claim; these components are explicitly credited as covered. Neither accessible foundational primary text nor the earlier centroidal statement establishes the 28 Shrikhande four-cosets or the exact six-term positive **fixing**-polynomial difference for the canonical strongly regular graph pair. Accessible mathematical-record searches for the fixing polynomial, pointwise bases, cosets, transversals, and graph-pair aliases did not identify a dominating exact statement. A later general fixing-parameter source was only available as an abstract, so an unindexed or inaccessible prior full enumeration remains a real residual risk.

## Value — PASS

The two graphs have identical strongly regular parameters and the fixing-polynomial comparison differentiates every uniform independent detector deployment probability in the open interval. The full classification establishes the exact failure configurations, thresholds for guaranteed success, and all-cardinality counts. This is a natural complete symmetry-recovery classification, not an arbitrary parameter slice, although it has no asserted extension beyond these two graphs.

## Scientific limitations

Reproduction requires Python 3, with NetworkX 2.8+ for the independent adjacency-based script. The historical search does not prove universal novelty. The numerical verifiers independently rederive a finite claim but are not external validation. The general Cartesian-product criterion already contains the abstract rook test.

Self-review: passed. Independent audit: not yet performed.

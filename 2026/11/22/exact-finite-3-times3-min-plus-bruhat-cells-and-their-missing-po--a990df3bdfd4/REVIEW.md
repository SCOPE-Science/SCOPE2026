# Scientific assessment of finite three-by-three min-plus Bruhat membership

## Correctness — PASS

The two possible permutations are forced by the finite entry in position \((3,1)\). All finite factorizations can be normalized to left diagonal zero without changing any target entry. Direct multiplication then yields the exact two displayed parameter maps in RESULT.md. The four necessary nonnegative defects and the fifth conditional defect follow from the min expressions; conversely the case-split explicit factor selections reconstruct every entry. The \(231\) case follows from a separate explicit parameter map. The strict-positive counterexample has defects \((2,3,3,1,-3)\), so it violates the proved necessary condition for the longest cell and violates the required zero for the other cell. Deterministic arithmetic tests and small-box exhaustive reconstructions support, but do not replace, this universal proof.

## Originality — PASS, qualified

Grigoriev, *Min-plus Bruhat decomposition*, arXiv:2611.03896v1, provides cell dimensions, a proposed longest-cell sufficient defect system and generic statements, but not the exact correct all-boundary three-by-three membership test. Its printed sufficient inequalities are strictly weaker than necessary: the explicit concrete counterexample satisfies all four strictly yet has no factorization. Hence the classification is not an application of the printed sufficient criterion. Niv, *Factorization of Tropical Matrices*, arXiv:1202.3615, gives a three-by-three classification for arbitrary elementary-factor products, a different predicate that does not imply membership in a fixed upper-triangular two-sided Bruhat cell. Relevant published results and semantic mathematical-record searches were compared by object, quantifiers and implication rather than title alone. Residual risks include an unknown unindexed equivalent exact characterization and future revisions of the initiating paper.

## Value — PASS

This gives the full first nontrivial finite-matrix image across every permutation cell, exposes a missing **full-dimensional** obstruction rather than an artificial finite slice, reconstructs factors on all admissible boundary wings, and supplies a small counterexample to a published mathematical sufficient condition. The natural problem is exact representability in a recently studied tropical analogue of the classical Bruhat decomposition. No claim is made about the higher-dimensional classification or elementary-factor width.

Self-review: passed. Independent audit: not yet performed.

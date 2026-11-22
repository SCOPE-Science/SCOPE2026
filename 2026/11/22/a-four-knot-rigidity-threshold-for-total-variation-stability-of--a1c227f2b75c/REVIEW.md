# Scientific review

## Correctness — PASS

The exact active-cone Karush–Kuhn–Tucker construction supplies an open input neighborhood on which convex regression is the weighted affine projector. Its step-response variation norm is \(L\max_jc_j\), with strict enlargement exactly when the interior knots cannot all equal the weighted centroid. The three-node projection has only identity and affine branches. The four-node equal-grid case checks all four active-set matrices, giving sharp \(6/5\), and the arbitrary-grid obstruction follows from strict positivity and distinct interior knots. The standalone exact-rational program verifies critical projector, variation and multiplier identities; finite checks do not replace these proofs.

## Originality — PASS, with explicit priority risk

Originality was compared by statement and implication, not by title. Guntuboyina–Sen (2013, arXiv:1305.1648) develop squared-risk bounds and convex projections (including affine projections of concave inputs), not a two-input variation coefficient. Meyer (2008, arXiv:0811.1705) treats shape-restricted regression splines and cone projection computations, but not the mass/mesh rigidity threshold. Yang–Barber (2017, arXiv:1706.01852) treat the distinct isotonic cone. The closest published finite-convex-regression record establishes coordinate maximum-norm constants, not the variation seminorm; the closest variation-rigidity record imposes first-difference isotonic constraints on cycle-shaped orders, not convex second-difference constraints. Dykstra (1983) and Hildreth (1954) have historical priority as algorithms and formulation; their complete original text was not obtained, and an equivalent, unindexed earlier statement remains possible. The checked sources do not currently provide stronger coverage of this precise theorem.

## Mathematical value — PASS

A quadratic convex-regression estimate is known to be stable in the fitting Hilbert norm, which does not answer whether it preserves oscillation magnitude measured by first differences. The classification proves an unavoidable qualitative obstruction for *every* positive mass profile on *every* mesh with at least four knots, gives a precise three-knot exception, and computes the first sharp loss \(6/5\). It supplies realizable arbitrarily small witnesses, not merely a formal operator-norm calculation, and a quantitative uniform-grid lower bound approaching \(3/2\). These conclusions provide a natural stability diagnostic for shape-constrained fitting. The exact coefficient for larger grids remains open.

Self-review: passed. Independent audit: not yet performed.

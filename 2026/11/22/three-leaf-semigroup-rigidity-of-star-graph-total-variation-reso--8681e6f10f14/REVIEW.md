# Scientific review

## Correctness — PASS

The domain is the real \((m+1)\)-dimensional unweighted star with \(m\ge1\); each \(P_t\) has a unique minimizer by strict convexity. For \(m\le3\), the flux optimization yields the minimum-norm subgradient and verifies MINSUB at all tie configurations. Polyhedrality and the reviewed equivalence theorem of Burger et al. then imply the claimed semigroup identity for every input and every nonnegative parameter. For \(m=4,5\), every rational counterexample is certified by primal/dual KKT identities; adding \((-10,10)\) leaf pairs preserves the hub's stationarity for all degrees, with exact rational discrepancy. The standalone checker independently replays the finite certificates using fractions. No part of the all-dimensional conclusion is inferred from enumeration.

## Originality — PASS, with priority qualification

Burger et al. (arXiv:1601.02912) give the existing sufficient MINSUB-to-flow theorem, which also explains the easy positive direction; it does not supply the negative direction for stars. Kirisits et al. (arXiv:1807.10514), Section 5, give an existence counterexample on general graphs and equivalence criteria, but not the complete star threshold and all-degree obstructions. Bungert et al. (arXiv:1901.06979) study related abstract criteria. These were compared by operators, time-composition quantifiers, graph families, and implications rather than by titles. Relevant related results on graph heat variation and fixed-parameter TV-proximal stability do not imply the same property. The residual risk is unindexed equivalent graph-TV semigroup classification or a disguised fused-lasso path theorem; historical priority is not claimed as fully proven.

## Mathematical value — PASS

A sharp obstruction boundary differentiates proximal parameter continuation from the true autonomous TV gradient-flow semigroup on the simplest branching graphs. The first failure at four leaves and the exact rational, parity-complete certificate furnish a structural diagnostic relevant to whether sequential graph-TV denoising equals single-stage denoising at the summed penalty. It is a natural complete classification, not an arbitrary finite parameter exercise or merely a re-expression of the MINSUB sufficient condition.

## Remaining limitations

Unequal edge weights, general trees, other fidelities and worst-case composition-gap sizes remain open here. The external equivalence theorem and exact KKT identities are checked; independent expert validation is not part of this review.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness — PASS

The finite falling-factorial identity follows from exact simultaneous avoidance of prescribed labels in the two coordinatewise coupled Prüfer codes. The exact variance and cross-covariance formulas were reconstructed from one-label and two-label avoidance events. First-order expansions give the stated covariance matrix and the asymptotic variance function. Differentiation proves that its derivative changes sign exactly once. The conditional Gaussian proof reduces the coupled allocation to three independent fixed-size urn streams after conditioning on the number of copied positions, uses the Schur complement for Poisson counts conditioned on stream totals, and finally restores a binomial Gaussian fluctuation. All independence statements and the restrictions on the copying parameter are explicit. The standalone independent weighted-enumeration checker passed 749 finite exact-rational assertions; those finite checks are not substitutes for the infinite-limit argument.

## Originality — PASS, qualified

The closest original sources inspected were Bogachev–Gnedin–Yakubovich (arXiv:math/0609498, §§1–2, 2006) on the variance of occupied boxes in a single infinite-urn model, and Barbour–Gnedin (arXiv:0809.4387, §§1–4, 2008) on counts of boxes of specified occupancy in a single allocation. Neither states this two-code correlated-copy model, its joint leaf-overlap law, or the unique interior maximum of the overlap-count variance. The closest indexed related findings concern shared-ancestry or copied-parent couplings of *recursive/attachment trees*, not positionwise refreshing of independent uniform Prüfer letters, and one previously noted uniform Cayley-tree result counts agreement of the **entire degree** at a vertex for independent trees, not common leaves under partial code copying. These differences are mathematical distinctions, not merely differences of title. A sufficiently general multistream occupancy theorem could yield parts of the present result by specialization; unindexed coverage remains a priority risk, and publication should not be described as independently priority-certified.

## Value — PASS

Common leaves of trees on persistent labels are a natural stability statistic for sampled network structures. The precise intermediate copying fraction at which their uncertainty is largest is a nonmonotonic structural boundary: the two endpoint models are *not* extremal. Exact finite moments support calibration, and the joint limit describes simultaneous sampling uncertainty in the two leaf totals and their intersection. The variance optimum is of direct use when selecting conservative standard errors for a partially refreshed code-based random-tree null model, even without an additional downstream theorem.

## Sources and limitations

- Bogachev, Gnedin and Yakubovich, *On the variance of the number of occupied boxes*, https://arxiv.org/abs/math/0609498 (first preprint 2006-09-18).
- Barbour and Gnedin, *Small counts in the infinite occupancy scheme*, https://arxiv.org/abs/0809.4387 (first preprint 2008-09-25).
- The coupling is specified by Prüfer coordinates, not graph-edge replacements; the Gaussian result is stated for fixed interior copying probability. No Berry–Esseen rate or priority guarantee is asserted.

Self-review: passed. Independent audit: not yet performed.

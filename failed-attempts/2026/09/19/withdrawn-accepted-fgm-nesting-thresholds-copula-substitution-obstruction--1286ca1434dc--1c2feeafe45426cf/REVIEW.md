# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The counterexample is exact. For product inner blocks, repeated differentiation yields
\[
(1+D_u)^{m-1}(1+D_v)^{n-1}c(u,v),
\]
not the simple outer-density-times-inner-density expression. Applying this identity to the FGM density gives
\[
1+\theta(1-2^m u)(1-2^n v).
\]
The extrema of the two affine factors give the stated necessary and sufficient interval for density nonnegativity. Groundedness and uniform one-dimensional margins are immediate from the copula boundary identities, so nonnegative full mixed density is sufficient. At \((m,n,\theta)=(2,1,1)\), exact evaluation gives density \(-35/64\), decisively disproving unrestricted closure.

The entropy curvature follows from the Taylor expansion of \(-(1+\theta h)\log(1+\theta h)\), together with \(\mathbb Eh=0\) and the exact moment identity
\[
\mathbb E(1-2^m\prod_{i=1}^mU_i)^2=(4/3)^m-1.
\]
For \((m,n)=(2,1)\), the quadratic entropy defect relative to the outer FGM copula is \(-2\theta^2/27\). Exact-rational verification reproduces all displayed special-case constants.

## Originality

**PASS, to the best of our knowledge, with a narrow claim.** Lu (arXiv:2609.20512v1) states unrestricted copula closure, a product density rule, and entropy additivity under the substitution at issue, but does not contain the FGM obstruction or threshold formulas above. The older nested-Archimedean literature already demonstrates that meaningful hierarchical copula constructions can require compatibility or nesting conditions, so no originality is claimed for that general principle.

Searches by FGM nesting terminology, the exact threshold values, product-inner substitution, and equivalent hierarchical-copula language did not locate the displayed parameter interval, Euler-operator formula, or entropy-curvature defect. McNeil (2008) and Hofert--Maechler (2011) were inspected through their public article descriptions; the full breadth of older nested-copula literature was not exhaustively inspected. This leaves residual originality risk that an equivalent FGM special case exists under another construction or terminology. The claim is therefore restricted to the explicit formulas and obstruction stated here and is made only to the best of our knowledge.

## Value

**PASS.** The finding directly tests the central closure operation of a new probability/statistics preprint and provides more than a single counterexample: it gives an exact two-parameter family of admissibility thresholds, identifies the missing chain-rule structure, and shows that the entropy theorem also fails even when the substituted object remains a valid smooth copula. The formulas isolate a salvageable parameter region and make the obstruction quantitatively reusable.

## Limitations

- Exact thresholds are for a bivariate FGM outer copula with independence inner blocks.
- No complete criterion is given for arbitrary outer or inner copulas.
- The entropy discrepancy is established locally around independence rather than in closed form on the entire admissible interval.
- Older hierarchical and nested-copula literature is extensive; an equivalent special case under different terminology remains a residual originality risk.
- Independent audit has not been performed.

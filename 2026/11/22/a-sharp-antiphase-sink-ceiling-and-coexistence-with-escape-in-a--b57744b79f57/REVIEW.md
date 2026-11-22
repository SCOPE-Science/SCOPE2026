# Self-review

## Correctness — PASS
On the invariant anti-diagonal the nonzero fixed-point equation is \((1-u)e^{-u}=(1+2b)/a\) with \(u>0\); differentiation gives the complete 0/2/4 census including boundary cases. The full-plane Jacobian diagonalizes along normal/tangent directions, with multipliers \(a e^{-u}(1-5u+2u^2)\) and \(1+2au(u-2)e^{-u}\). Below \(a=e^2\) a neighborhood of the nondegenerate \(u=2\) fold on its inner side has both multipliers strictly within the unit disk. At or above the threshold, the mutually exhaustive regions \(u\in(0,3/20]\), \([3/20,1]\), \([1,2)\), and \([2,\infty)\) give at least one multiplier outside the open disk. The \(b<-1/2\) escaping region follows from a uniform bounded-nonlinearity inequality. The fold square-root coefficient follows from the exact second derivative. The included checker reconstructs the two-by-two Jacobians and checks 102 numerical/branch conditions, not infinitely many cases. No unproved nonlinear classification at neutral multipliers is claimed.

## Originality — PASS within inspected evidence
The original full-text article by Soula et al. (2023, DOI 10.3390/math11061517) describes the map, numerical bifurcations and invariant subspaces without establishing this full antiphase census or sharp necessary-and-sufficient \(a<e^2\) gain ceiling. The closest indexed same-map RESULT.md, *A sharp global boundedness interval and logarithmic critical escape in a coupled Gaussian map* (2026), proves global absorbing/escape bounds but explicitly leaves finite-attractor classification open. Its escape theorem overlaps the coexistence proof's escape half; it does not imply the existence, exact number or stability of antiphase equilibria or the gain ceiling. Other indexed symmetric-coupling stability results concern different response maps, and none checked dominates the present claim. Unindexed exact antiphase calculations and older inaccessible literature are publication-priority risks. Absence of hits is not treated as uniqueness proof.

## Mathematical value — PASS
A sharp, dimensionless gain threshold separates the presence and impossibility of stable antiphase equilibria under any coupling. The continuous fold-to-sink bifurcation at \(a<e^2\) meets a second multiplier boundary at \(a=e^2\), where the critical pair is \((1,-1)\). On a nonempty open coupling interval, two attracting antiphase equilibria coexist with an open set of geometrically escaping trajectories. This is a structural multistability/escape boundary in the same natural coupled-map model, not a parameter substitution or a numerical diagram restatement.

## Closest sources and limits
[1] Y. Soula et al., *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps*, Mathematics 11 (2023), 1517, https://doi.org/10.3390/math11061517. Inspected full openly accessible article including equations, discussions and figures.

[2] *A sharp global boundedness interval and logarithmic critical escape in a coupled Gaussian map* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-sharp-global-boundedness-interval-and-logarithmic-critical-esc--f463338d3c52/RESULT.md. Inspected complete RESULT.md with explicit equations, proof and limitations.

The theorem does not classify off-antidiagonal equilibria, all finite attractors, basin boundaries, or nonlinear neutral behavior. No publication-priority certification or external validation is claimed.

Self-review: passed. Independent audit: not yet performed.

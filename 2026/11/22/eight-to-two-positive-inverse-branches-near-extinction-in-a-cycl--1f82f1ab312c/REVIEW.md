# Self-review

## Correctness — PASS

The formula \(F_i(p)=R p_i(h-(Cp)_i)\) reduces the zero fiber to a complete finite support enumeration. The two-coordinate solutions and the determinant \(D=\bigl((\alpha-1)^2+(\beta-1)^2+(\alpha-\beta)^2\bigr)/2\) establish all admissible zero states and rule out a hidden singular three-coordinate state when the coefficients are not both one. The occupied blocks and missing-coordinate multipliers of \(DF\) give the signs of the unique local inverse branches. Every strictly positive inverse of a positive target satisfies \(p_i<h\), so compactness prevents any unlisted branch from appearing as the target tends to zero. The exceptional equal-interaction case follows from a scalar quadratic. These steps establish exact counts, not merely numerical evidence.

A standalone rational-arithmetic and small-output diagnostic (`CHECK.py`) checks the formulas; numerical iterations are neither used as an infinite proof nor used to infer the uniform positive-target quantifier.

## Originality — PASS within inspected evidence

The 2024 source's full manuscript, especially its three-dimensional model and bifurcation sections, raises the noninvertibility problem but does not classify its one-step inverse sheets. The 2010 general Lotka–Volterra paper supplies the critical-set and inverse-sheet framework but does not state the cyclic-map parameter classification. Its planar examples do not determine the three-dimensional positive-octant counts. A 2001 paper studies a different planar Lotka–Volterra map. Publicly indexed results on the same map treat periodic orbits and stability, not extinction inverse valence. Search absence cannot certify originality; an unindexed broader result in multivariate polynomial inverse dynamics remains the principal publication-priority risk.

## Mathematical value — PASS

This is a complete, parameter-uniform local inverse classification of a natural observation (extinction) highlighted by the founding dynamical study. The change from eight positive inverse sheets under weak competition to two under stronger competition is not a statement about fixed points or linear stability. More unusually, under strong competition the extinction observation itself still possesses eight nonnegative ancestors, so counting inverse images at the boundary does **not** recover the positive inverse multiplicity in any neighborhood. This informs the interpretation of backward reconstruction and noninvertible basin geometry in the specific model, without claiming a global attractor classification.

## Closest literature and limits

The primary source is S. S. Muni, arXiv:2408.15054v1 (2024); the principal nearby inverse-geometry source is G. I. Bischi and F. Tramontana, DOI 10.1016/j.cnsns.2009.10.021 (2010). The classification excludes the two half-lines where precisely one interaction coefficient equals one; all statements are for positive \(R,\alpha,\beta\) and one-step inverse images. Independent review and publication-priority certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.

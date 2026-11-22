# Review of the natural cubic geometric-grading variation theorem

## Correctness — PASS

The exact knot-curvature recurrence is reconstructed from the natural-spline tridiagonal equations, including endpoint conditions and the exceptional forcing at the first interior knot. Both characteristic roots and the boundary normalization are checked; the first cell is strictly monotone and each later cell is a one-excursion cubic because the adjacent curvature ratio lies in \([0,a]\) with \(a<1/2\). The finite formula therefore calculates the **whole** variation, not an upper bound. Geometric dominated convergence proves the subcritical and supercritical limits, while the Lipschitz property of the excursion envelope gives an \(O(1)\) critical remainder. An independently solved tridiagonal system and separately calculated cubic derivative extrema agree with the formula for multiple real grading ratios and mesh lengths. Finite numerical checks are evidence for implementation consistency, not an infinite-case proof.

## Originality — PASS, qualified

The closest indexed natural cubic interpolation finding treats exactly three knots and a positivity defect for variable mesh ratio; it does not imply the exact finite-\(N\) curvature propagation and fixed-\(R\) large-\(N\) growth threshold. The inspected Dermoune–Preda (2014) natural-basis account and a 2012 weighted shape-preserving cubic study concern different endpoints of spline theory and do not state this step-variation law. Classical 1973 and 1986 spline articles were available only in abstract; neither is ruled out at the full-text level. Historical-priority risk remains and independent literature verification is appropriate.

## Mathematical value — PASS

The golden-ratio-squared threshold is a nontrivial structural boundary: holding the ratio of successive knot widths fixed can switch a single-jump natural spline from bounded variation to linear and then exponential variation growth as the number of cells increases. Exact finite-grid variation, asymptotic rate and positive exponential prefactor identify a concrete mechanism and stability limitation of standard natural cubic interpolation. This is not a general operator-norm classification, and that limitation is integral to the claim.

## Limits

The theorem applies only to the named geometric grid, single-jump data and natural boundary conditions; older spline literature without accessible complete texts leaves a residual priority risk. The supplied proof is an analytical argument and the checker is a supplementary reproducibility check.

Self-review: passed. Independent audit: not yet performed.

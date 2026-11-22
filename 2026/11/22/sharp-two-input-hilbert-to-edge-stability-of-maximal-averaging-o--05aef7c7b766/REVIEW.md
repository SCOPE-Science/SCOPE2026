# Review of the star maximal-gradient stability theorem

## Correctness — PASS
The graph-ball formulas are exact on counting-measure stars. The proof handles the hub-global and hub-singleton cells separately and excludes the infeasible all-leaf-singleton hub-singleton cell using the mean constraint. Every remaining affine Jacobian has a nonnegative row Gram matrix entrywise bounded by the \(m-1\)-singleton/one-global Gram matrix; the two-dimensional spectral calculation yields the stated larger root. An open strict-selection region and a right singular vector give true positive-pair attainment. Reduction through \(|f|\) gives complex inputs, and the two-vertex case is checked separately. The standalone exact rational certificate and direct-pair tests agree. Risk: finite tests do not independently certify the universal branch argument.

## Originality — PASS, relative to inspected evidence
The central comparison is not title-based. Liu–Lian–Wang, arXiv:2611.15377v1, and González-Riquelme–Madrid, arXiv:2011.02630v1, solve single-input variation or operator-norm problems. The publicly available two-input star total-variation theorem uses an edge-\(\ell^1\) denominator; its sharp \(2m/(m+1)\) result cannot recover this exact vertex-\(\ell^2\)-to-edge-\(\ell^2\) spectral constant by a norm change. Fractional-star two-input asymptotics for positive fractional exponents do not provide this exact endpoint formula. Stronger or unindexed historical coverage remains possible; the inspection is not a priority guarantee.

## Value — PASS
This is the complete exact sharp Hilbert perturbation invariant for a canonical family of all finite stars, not a single small-graph computation. It quantitatively separates regularity of individual maximal outputs from stability of a nonlinear edge gradient under measurement perturbations, and identifies an attained degree-\(\sqrt m\) amplification with an explicit spectral extremizing mechanism. The precise result is useful for perturbation estimates on graph maximal filters and for comparison to the better-studied one-input variation theorems.

## Scientific limits
The theorem is for unweighted centered stars with vertex Hilbert input and quadratic edge-gradient output. No extension to general weighted graphs, arbitrary graph families, other exponents, or exhaustive equality classification is claimed. The originality assessment is bibliographically bounded and independent assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.

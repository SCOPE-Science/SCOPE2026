# Scientific assessment

## Correctness

PASS. The full order-three kernel is a verified reproducing kernel in the cited primary source. Its nonzero Gaussian factor reduces orthogonality to two squared interpoint distances. The exact anchored-gram determinant is computed for all eleven isomorphism classes of four-point edge colorings; the independent exact quadratic-field checker covers all 64 labeled patterns and all 1024 five-node patterns. A separate combinatorial argument rules out five nodes without any numerical extrapolation. Two explicit four-point configurations realize the two permitted patterns. Minimal enclosing circles are computed from acute and equilateral triangles. For first-order jitter, differentiation of the **normalized** Fock kernel retains the essential Gaussian factor \(e^{-\alpha d^2/2}\); the Hermitian arrowhead Gram derivative and its two-by-two weighted covariance spectrum yield both sharp constants. The checker reconstructs these constants and finite-difference behavior. No infinite asymptotic assertion is inferred from finite experiments.

## Originality

PASS relative to inspected scientific evidence, with an explicit prior-implication boundary. The underlying Laguerre kernel is known from De Bie–De Martino–Diki (arXiv:2510.14639) and earlier work; Harborth–Piepmeyer (1993) already identifies the maximal planar two-distance ratio and its two four-point configurations. Accordingly the mere existence of four orthogonal evaluations and the two planar shapes **are not claimed as independent new geometry**: they follow by combining prior formulas. The proposed distinct contribution is the full, explicitly normalized first-order **Gram-operator jitter optimization**, in which the minimum-aperture design is less robust than the competing geometry. No inspected primary work or indexed result states this sharp Fock-kernel tradeoff. Publication-priority risk remains because the 1993 chapter was available only via its detailed public abstract and specialized quantum measurement literature could use another sensitivity convention.

## Value

PASS. For orthogonal evaluation designs, exact aperture measures the smallest phase-space region accommodating four mutually orthogonal measurement vectors, whereas the first-order operator-norm jitter penalty measures conditioning loss under node misplacement. The two notions pick opposite designs. The Gaussian suppression of long-pair correlations makes this non-obvious from geometry alone. The calculation supplies natural sharp design criteria, not just a negative existence test, an arbitrary finite numerical slice, or a small improvement in a previously known constant.

## Closest literature and limitations

See [1]–[4] in `RESULT.md`. The 2025 paper derives polyanalytic Gaussian kernels, the 2024 paper develops their quantum harmonic analysis, and the 1993 chapter already supplies the two-distance extremizers. The present theorem is limited to full-order-three polyanalytic kernels, four exactly orthogonal nodes in one complex dimension, and **one-node infinitesimal** perturbations. The result must not be read as an independent geometric classification or a global finite-jitter optimization. Independent publication-priority verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness
**PASS.** The normalized full-sphere and equatorial fourth moments yield an exact quadratic form on trace-free symmetric matrices. Five symmetry sectors and an even generalized eigenvalue block account for every dimension. The two-level crossing produces a unique optimal angle and exact condition numbers. The full-matrix test in `check_two_equators.py` independently constructs the Gram matrix through projections rather than applying the sector formulas. Residual limit: tests are finite, and the proof—not their count—justifies arbitrary dimensions.

## Originality
**PASS, provisional.** Direct comparison with the full text of Quellmalz et al. (arXiv:2303.05179) distinguishes scalar Funk integrals from two function-valued equator traces. Michel et al. (arXiv:2103.14650) treat spherical cap localization rather than normalized measures on measure-zero equators. Generic nonorthogonal injectivity and its optimized full spectrum are not implied by the previously studied orthogonal-equator classification. Exact database and terminology searches found no dominating result. Residual priority risk: a classical harmonic restriction calculation might implicitly contain the spectrum.

## Mathematical value
**PASS.** This is a complete natural two-view inverse-geometry classification: for quadratic harmonics, orthogonal views fail while generic oblique views recover uniquely. The theorem supplies the exact optimal two-view angle, every eigenvalue and multiplicity, and a dimension-uniform stability constant, answering a concrete design question not settled by the orthogonal-view case. It does not claim arbitrary degree, sampling, or noise models.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness
**PASS.** The cubic collocation matrix is obtained from the stated clamped knots and Greville sites. The standard B-spline total-nonnegativity and oscillatory-matrix criterion give real simple positive eigenvalues; strict substochasticity bounds them below one. The two parity equations are derived by exact elimination, and both root counts are proved by explicit strictly signed derivatives. The exceptional band-edge solution occurs precisely at eight cells. A simple-root expansion gives the exact exponential splitting. The packaged checker corroborates the identities and finite examples, but is not treated as a proof of the infinite statement.

## Originality
**PASS with historical-priority risk.** The February 2014 Nagler–Cerejeiras–Forster preprint provides broad spectral constraints and explicitly leaves individual spline-operator eigenvalues unknown. The December 2013 Nagler–Kähler paper treats iteration and smoothness, not cubic boundary modes. A later published study of generalized B-spline isogeometric eigenproblems concerns stiffness-collocation matrices rather than this positive Greville averaging matrix. Similar periodic cubic-spline collocation results concern singular values and periodic meshes. The previously computed quadratic case does not imply the cubic outlier transition. An unindexed specialized result may still predate this analysis.

## Value
**PASS.** This is the first degree in which a cubic cardinal band and nontrivial clamped boundary collars coexist, and it supplies a sharp finite-grid threshold, a natural algebraic limit, and quantitative boundary interaction. The eight-cell transition is not a routine rescaling or a single unmotivated numerical invariant; it distinguishes distinct spectral regimes relevant to spline collocation conditioning and boundary-mode analysis.

Self-review: passed. Independent audit: not yet performed.

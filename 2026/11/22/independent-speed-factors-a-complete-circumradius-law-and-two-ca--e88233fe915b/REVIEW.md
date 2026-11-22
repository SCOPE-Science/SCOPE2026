# Mathematical review: random ellipse circumradius law

## Correctness (C) — PASS

The proof begins with independently checked Euclidean identities: the chord length of an ellipse parametrized by eccentric anomaly and the affine image of the cyclic-triangle area. The standard triangle circumradius identity then cancels all three chord-gap factors, leaving exactly three speed functions evaluated at the pairwise angular half-sums. The associated integer torus map has determinant two and is surjective, hence its Haar pushforward has three independent uniform components; it does not assume unproved independence of the original triangle's edge lengths.

The arcsine change of variables yields a normalized explicit single-factor density; its triple logarithmic convolution is the full radius law. The beta/hypergeometric moment representation and Fourier evaluation of the log moments are convergent for every fixed \(a>b>0\). The eight-point Morse critical census supplies precisely four critical values, and the local quadratic Jacobian/coarea calculation supplies both one-sided square-root density coefficients with multiplicity three. The endpoint exponents follow from isolated positive/negative definite quadratic extrema and three-dimensional ball volume. The log-variance dilogarithm is strictly increasing with axis ratio, proving population-level two-statistic recovery. The delivered standard-library checker passed 1,845 numerical diagnostics on the exact geometry, moments, Hessian coefficients and inversion; these checks supplement, rather than replace, the analytic arguments.

Remaining scientific limits: near-circular joint parameter asymptotics, numerical estimation error, and general nonelliptic curves are outside the claim. The cusp remainder statements depend on smooth Morse-coordinate localization; no finite simulation is presented as an infinite proof.

## Originality (O) — PASS, with residual historical-priority risk

**Most closely related published statement.** *The universal astroid law and sharp cusp scaling of random ellipse circumcenters* uses the same three independent eccentric-anomaly samples. Its fully inspected statement and proof give a two-dimensional **circumcenter** marginal and its four cusp laws, not the circumradius or its Mellin distribution. The circumcenter marginal cannot determine the radius: fixing the center at the origin while varying a centered circle's radius through \((b,a)\) produces different circumradii through triples chosen from its four intersections with a noncircular ellipse. The isolated endpoint Morse geometry is related and is not asserted as novelty by itself. Other inspected mathematical results on identical samplers concern acuteness or Delaunay triangulations; neither determines a radius law. Published tangent-chord-product inverse results concern a different geometric observable and source sample.

**Historical comparison.** Garcia (2016, arXiv:1607.00179v1, full accessible text) and Romaskevich (2013, arXiv:1304.7588, full accessible text) describe the deterministically constrained one-parameter family of three-periodic elliptic billiard triangles and their incircle-center loci, not an independent three-point radius distribution. Searches using circumradius, Mellin transform, pairwise half-sum, product of arcsine speeds, caustics and logarithmic moments produced no equal or dominating published claim. The result is therefore original to the accessible comparisons on a best-knowledge basis, not certified globally unique. Unindexed older conic probability or special-function literature remains a genuine priority risk.

## Mathematical value (V) — PASS

A circumradius is an intrinsic elementary invariant of the naturally sampled ellipse-inscribed triangle, and the three-factor independence is a non-obvious exact structural feature created by a degree-two covering of the angular torus. This provides the **complete** distribution, not just a moment or a narrow numerical slice. The geometry of its density is also nontrivial: its only two internal transitions are unequal-coefficient one-sided square-root caustics at the minor and major semiaxes. Finally, two direct statistics of the same natural random radius, the mean and variance of its logarithm, invert both geometric semiaxes without additional observables. These give a motivated and reusable baseline in conic stochastic geometry. No universal inequality, new hypergeometric identity, or downstream theorem is needed to justify the finite-dimensional classification.

## Relevant scientific limitations

The proved law is for independent uniform **eccentric anomalies**, not uniform Euclidean arclength, and for fixed noncircular axes. The archived foundational papers address billiard-orbit families, and later published papers cited in the full report are near comparisons, not proof of global novelty. No external independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.

# Review of Exact Euclidean projection, matching distance law, and parity-dependent deep holes of chainlink polytopes

## Correctness — PASS

The construction of the active-edge set as a matching and the explicit coordinate bounds establish that the proposed orthogonal edge corrections remain feasible even when two nonadjacent active edges flank a third constraint. The residual is a nonnegative combination of active facet normals, giving a global quadratic minimizer certificate. The matched-edge count and equality conditions give exactly the even/odd deep-hole loci. For the random law, inclusive matching events factor over disjoint coordinate pairs and the elementary triangular-depth density gives the precise Laplace transform. The accompanying standalone verifier compared 960 pointwise projections against a general constrained quadratic optimizer; these finite tests supplement, not replace, the proof.

## Originality — PASS (provisional priority)

Kantarcı Oğuz, Özel and Ravichandran (arXiv:2211.08382v1, 2022) introduced the body and already proved its matching volume formula. That known matching geometry is credited. The metric projection normal-cone certificate, sharp odd/even box deep-hole classification and marked squared-distance Laplace law are not stated by that result, nor do they follow solely from its volume trace. Indexed records about chainlink section fluctuations and radial vertex shells do not imply the present metric claim. Related archive full-text access was incomplete and an unindexed equivalent remains possible.

## Mathematical value — PASS

The problem is motivated by the precise metric repair needed to map an arbitrary box point to its nearest feasible chainlink point. A globally coupled constraint system unexpectedly separates into an orthogonal matching for each input. The exact projection gives a linear-time solver and the complete deep-hole geometry; its squared error has a closed transform and sharp expectation. The zero-distance volume formula is old, explicitly separated from the claimed new metric laws.

## Verification and limitations

The claim requires \(s\ge3\), \(0<2\ell\le\min_i a_i\), standard coordinate Euclidean distance and points in the containing box. No assertion is made outside this parameter regime or about independent verification. The `verify.py` tests are finite reproducibility checks; the analytic argument establishes the universal statements.

Self-review: passed. Independent audit: not yet performed.

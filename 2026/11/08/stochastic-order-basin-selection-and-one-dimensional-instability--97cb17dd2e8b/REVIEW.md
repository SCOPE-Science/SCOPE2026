# Scientific review

## Correctness — PASS

The exact cumulative-tail transform converts the mean-field update into a cooperative ODE on the compact order simplex. Its off-diagonal Jacobian signs are checked under the full probability constraints, including the extreme endpoints. Comparison with uniform is strictly positive in all coordinates after positive time for any strictly comparable initial law. The polynomial barriers \(U\pm\varepsilon w\), with \(w_i=i(m+1-i)\), are explicitly admissible and have componentwise outward-pointing derivatives for \(0<\varepsilon<1/[(m+1)(m+2)]\). Monotone bounded barrier trajectories converge to equilibria; the stationary birth-death flux calculation establishes that the only equilibria are the two extremes and uniform. The symmetric tail Jacobian is a negative definite Dirichlet Laplacian plus a rank-one perturbation whose inertia has exactly one positive direction. Rational checker identities for \(k=2,\ldots,16\) and direct ODE witness integrations corroborate but do not certify the infinite family.

## Originality — PASS, with residual risk

Cao and Gong (arXiv:2605.28984v1, 2026-05-27) state the nonlinear model and three equilibria, prove symmetric convergence and far-mean sufficient selection \(M(0)<1\) or \(M(0)>m-1\), and explicitly leave broader nonsymmetric basins as a challenge. The two five-opinion witnesses have means \(19/10\) and \(21/10\), so neither conclusion follows from those far-mean bounds; both witnesses are nonsymmetric. The new ordered-tail transformation, strict barrier construction, and full saddle inertia establish a genuinely different sufficient domain and its local boundary geometry. Search comparisons for stochastic dominance, monotonicity, spectral index and the article identifier did not locate an already covering statement. Classical cooperative-ODE comparison and stable-manifold principles are acknowledged, not claimed as new. Earlier Cao–Reed and Cao–Cortez opinion papers use other interaction rules; their abstracts do not resolve the comparison. An equivalently phrased result in unindexed literature or a more general theorem specialized to this exact vector field remains a residual risk.

## Mathematical value — PASS

Selecting the eventual consensus from nonsymmetric initial probability laws is an explicit open direction in the motivating article. First-order stochastic comparison gives a simple finite list of inequalities for all \(2k+1\) states and applies at moderate mean bias outside previously certified regions. The exact unstable dimension explains why the uniform distribution can attract on a lower-dimensional set while separating opposing outcomes locally. These are structurally motivated criteria, not arbitrary parameter slices or a known-table recomputation. The sufficient criterion is deliberately not presented as a complete global basin classification.

## Sources and remaining limits

Primary: https://arxiv.org/html/2605.28984 and https://arxiv.org/abs/2605.28984 (mathematical formulation, known results and open problems, relevant sections inspected). Related but structurally distinct: https://doi.org/10.1137/24M1700661 and https://doi.org/10.1137/24M1682269 (abstract and bibliographic information checked). Results apply only to the exact deterministic mean-field dynamics; finite stochastic populations, rates and the incomparable-initial-data region remain untreated.

Self-review: passed. Independent audit: not yet performed.

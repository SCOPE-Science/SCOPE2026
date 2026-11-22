# Scientific review

## Correctness: PASS

The claim fixes all quantifiers: integer clique and independent-set sizes at least two, premium clique price greater than one, positive budget and positive finite observation time, unconstrained independent nonnegative conductances. Injectivity of the graph Laplacian in edge weights and a strictly positive matrix-exponential Hessian imply a unique unrestricted optimum. The proof checks every boundary: the cross-only endpoint has the exact threshold derivative, while the clique-only endpoint has strictly positive derivative when price exceeds one. The four explicit eigenspaces give a complete spectrum, and the convex one-parameter minimization proves support classification without relying on numerical search. The reentrant case follows from strict positivity of the second derivative of the exponential denominator, with an exact unique maximum and a derived asymptotic premium window. A standalone standard-library verifier replayed successfully with 10,812 finite checks. Residual correctness risk is ordinary proof/transcription error; those tests cannot prove the infinite quantifiers.

## Originality: PASS on inspected evidence, qualified

The closest published exact result for the same graph and two-price model optimizes the smallest positive Laplacian eigenvalue. Its crossing-only optimum when the independent set is at least as large as the clique does not imply the present full-spectrum reentrant heat-trace optimum: the latter can uniquely fund clique edges at intermediate time. The 2006 primary treatments of continuous-time fastest mixing and convex eigenvalue optimization cover generic methods and a spectral-gap target, but not the exact finite-horizon support law. Query comparisons were performed for aliases involving exponential trace, graph heat semigroup, time-dependent conductance design, support screening and reentrant investment. No directly covering theorem appeared in the inspected records. Remaining risk: equivalent results in specialized optimal experimental-design or network heat-trace literature could be unindexed; novelty is not an assertion of exclusive priority.

## Value: PASS

The support phase is not just a restatement of a convexity test. The canonical clique-plus-independent-set model admits a costly edge class that must be absent at both early and late horizons yet strictly positive in between, despite its never being needed for the best asymptotic spectral gap in the same size regime. The exact condition \(q=p+1\), unique two-switch interval, sharp price ceiling and nonzero \(1/p\)-scale cost window provide meaningful structural boundaries and a reproducible design rule for finite-horizon diffusion networks.

## Scope and limitations

Only a two-price complete split topology with premium clique-edge price is classified; heterogeneous prices and mass-weighted dynamics are not covered. The checker is supplementary finite evidence; no independent audit or full literature guarantee exists.

Self-review: passed. Independent audit: not yet performed.

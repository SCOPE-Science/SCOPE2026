# Scientific review

## Correctness — PASS

The likelihood score is exactly \(-\sqrt n\,B_n(t)/[t(1-t)]\) on every open data-free segment, and continuous likelihood values glue the integrated profile across sample knots. Population expected log likelihood is exactly \(\log2-1\) for every mode. The singular-endpoint truncation error is controlled by the uniform bound \(2\arcsin\sqrt\delta\), so Donsker's theorem gives a genuine full-interval functional limit. Brownian-bridge area regression isolates an independent absolutely continuous Gaussian linear tilt, making the maximizing location unique almost surely by convex-function differentiability. The reflection identity and the nonzero Gaussian derivative at the midpoint give the exact half-versus-half conclusion. Finite checker diagnostics are not treated as proof of infinite claims. Limitations: no explicit argmax density or local-alternative theory.

## Originality — PASS against checked evidence

Hjort (arXiv:2611.01030v1, Section 3.2; full accessible HTML inspected) treats misspecified triangular likelihood only when \(F(\theta)=\theta\) has one interior solution and \(f(\theta)>1\). The uniform case has all solutions and \(f=1\), so its local quadratic normal-limit theorem does not imply the global Brownian-bridge argmax law. Oliver's earlier fact that finite likelihood maxima are sample points is not claimed original. Ferguson (1982; abstract inspected) considers a different triangular-to-uniform one-parameter family with a deterministic inconsistent maximum, not this flat pseudo-true mode manifold. Targeted equivalent-formulation and overlap searches supplied no directly covering statement. Residual risk: unlocated general or early specialized work could already have the same global functional limit; some older model-fitting papers were not inspected in full.

## Mathematical value — PASS

The theorem resolves a concrete excluded boundary of recently developed nonregular likelihood theory: an entire interval of equally good population approximations. Unlike a routine normalization, it identifies a new global stochastic scale, proves uniqueness of an infinite-dimensional random argmax, and shows persistent lack of parameter concentration with an exact symmetry split. This matters for interpreting mode MLEs under severe yet natural misspecification; it is not a claim of general consistency or a universal phenomenon beyond this model.

Self-review: passed. Independent audit: not yet performed.

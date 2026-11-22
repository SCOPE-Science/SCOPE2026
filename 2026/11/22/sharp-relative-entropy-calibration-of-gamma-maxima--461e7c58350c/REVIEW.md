# Scientific review — sharp relative-entropy calibration of gamma maxima

## Correctness (C): PASS

The claim is a forward KL asymptotic for fixed Gamma shape \(\alpha>0\), \(\alpha\ne1\), with exact tail quantile and reciprocal-hazard scaling. The proof supplies: (i) the exact normalized maximum density and the unique global Gumbel KL optimizer via a strictly convex inverse-scale objective; (ii) a differentiable incomplete-gamma survival expansion, producing the first non-Gumbel density perturbation; (iii) a moving-window argument with both complementary KL tails negligible beyond fourth order; and (iv) the exact two-score projection and zeta-value residual coefficient. The perturbation's first-order mass is zero, preventing a spurious second-order KL term. The included numerical checker recomputes the Gram integrals, optimizer coefficients and exact finite-sample gamma KL integrals; it is not used as proof of an infinite limit. The shape-one endpoint, reverse divergence and moving-shape regimes are explicitly excluded.

## Originality (O): PASS, with residual priority risk

**Closest mathematical statements.** Johnson's arXiv:2007.03569 (initial public version 7 July 2020), later *Journal of Applied Probability* 61, provides relative-entropy convergence for Gamma maxima, but no \((\log n)^{-4}\) coefficient or fitted-Gumbel optimum; its closing paragraph raises optimal information-rate questions. Gasull, López-Salcedo and Utzet, *TEST* 24 (2015), study exactly the Gamma maximum and its accurate hazard-based norming constants, Lambert expansions, and CDF convergence; those normalizations and CDF facts are prior work. A separately indexed result treats the best KL Gumbel approximation of **exponential**, not nonexponential, maxima, at order \(n^{-2}\); the new theorem excludes that case. The 2025 Gaussian extreme-rate study concerns a different parent tail. None of the inspected relevant material supplies the global forward-KL optimizer with the universal zeta-value residual for fixed nonexponential Gamma shapes.

The conclusion is based on statement-level implication comparison, not title matching or the absence of search results. It remains vulnerable to obscure or inaccessible earlier KL expansions; no independent priority certification is claimed. The extracted text of the 2015 preprint was available for its substantive sections and comparison, although rendering its PDF image failed.

## Value (V): PASS

The classification resolves a natural quantitative refinement explicitly suggested by relative-entropy extreme-value theory: what information loss remains after both location and scale are optimized? It identifies a strict, positive universal coefficient with \(\zeta(3)\), a unique best affine correction, and a sharp distinction from the exponential endpoint. This addresses the accuracy of Gumbel approximations for chi-square/Gamma maxima relevant to maxima-based detection; it is not an arbitrary one-parameter slice or a reformulation of classical weak convergence.

## Scope and limitations

Only forward divergence is finite for the unbounded Gumbel reference and a finite-sample Gamma maximum. The limit is pointwise in fixed shape, not uniform as \(\alpha\to1\) or \(\alpha\to\infty\). Numerics are finite checks. Publication priority remains subject to specialist review.

Self-review: passed. Independent audit: not yet performed.

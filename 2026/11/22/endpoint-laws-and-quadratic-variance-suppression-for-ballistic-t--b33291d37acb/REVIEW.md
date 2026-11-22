# Scientific review

## Correctness — PASS

The core equality is a pathwise coboundary: for any bounded positional observable, its centered integral over a complete ballistic descent is identically zero, and the primitive is continuous through resets because its values vanish at both spatial endpoints. Under the Gamma-renewal velocity family, length bias changes the shape from \(n-1\) to \(n\), which determines the exact endpoint mixture. The integer-shape Erlang representation supplies a finite-stage Poisson construction and endpoint decorrelation, with the Gamma tails controlling moment convergence. The polynomial coefficients follow from explicit Beta integrals and Gamma moments. The code checks 6,000 sampled one-flight identities and independent stationary/fresh-start simulation, but the analytical proof, not simulation, establishes the limit.

## Originality — PASS, with bounded residual risk

The closest source is Das, Majumdar and Pal, arXiv:2611.16733v1 (November 12, 2026). Its complete accessible article establishes the uniform one-time stationary law, propagator, spatial relaxation freezing and shock fronts; it does not derive the exact endpoint-difference time-average law or the stationary/fresh-start variance ratio. Patch, Nazarathy and Taimre, arXiv:1408.1530, treat general multivariate renewal rewards accumulated at renewal epochs, and standard renewal-reward theory implies the ordinary average, but neither directly supplies the present partial-cycle law and its complete Gamma–uniform limiting distribution. Indexed searches on exact phrases, aliases and threshold-reset time-average fluctuations found nearby results for diffusive threshold resetting and history-resetting particles, rather than this ballistic renewal protocol. Mathematical novelty remains subject to specialist verification, especially against general coboundary or regenerative-process literature.

## Value — PASS

Time-averaged spatial measurements are a natural physical observable in a resetting transport experiment. The result identifies an entire class of observables with an exact, sharp \(t^{-2}\) fluctuation law, considerably faster than the conventional renewal \(t^{-1}\) law, and gives both the non-Gaussian limiting measurement error and a factor-two dependence on whether the measurement begins immediately after resetting or in stationarity. It complements the primary article's unusual spatial relaxation with a distinct and quantitatively testable temporal property. The exact formulas remain meaningful for varying Gamma shape, including shapes on both sides of the article's spatial freezing regimes.

## Limitations and evidence

The theorem applies to position-only observables under noiseless full ballistic traversals and positive integer shape \(n-1\). It does not assert any analogous superconvergence under intra-run speed changes, partial resets, or diffusion. Fresh-start and equilibrium initialization must not be conflated. Simulated estimates are checks rather than mathematical evidence for convergence. The publication-priority risk is that some general regenerative-coboundary framework may imply this particular special law without using the same vocabulary.

Self-review: passed. Independent audit: not yet performed.

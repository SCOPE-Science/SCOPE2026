# Scientific review: bounded diffusivity and first-passage optimization

## Correctness — PASS

The backward equation for the reflected Itô diffusion yields the exact functional \(\int_0^1(1-x)/D(x)\,dx\). Strict convexity of \((1-x)/d+d/c^2\) for almost every \(x\), with a multiplier chosen by the exact mean-budget equation, is a global optimality and uniqueness certificate over **all bounded measurable** admissible profiles. Direct integration gives both exact profile and value branches. The derivative calculation proves \(C^2\), but not \(C^3\), at the cap-activation threshold. A standalone checker verifies the exact branch identities, 16 independently sampled quadratures and 16 numerical constrained optimizations. Numerical checks corroborate, but do not replace, the analytic proof.

## Originality — PASS, qualified

The closest paper, Menon (2026), arXiv:2611.17470v1, supplies the crucial general variational context and the unbounded optimum; it does not derive a simultaneous finite floor-and-ceiling profile, the precise cap-onset budget, the explicit two-bound optimum value, or the jump in the third budget derivative. The 2023 study by Menon, dos Santos and Anteneodo supplies the Itô mean-time integral for arbitrary diffusivity and examples, not the present two-sided constrained optimization. General heterogeneous-diffusion escape work by Tung and Lawley concerns other boundary geometries and observables. Mathematical overlap was compared at the level of what each theorem implies, not matching words. The new result is a constrained-design extension of established convex-variational structure, not an independent invention of the Itô first-passage formula or square-root allocation idea. Related generic bounded-resource optimization and unindexed exact treatments remain priority risks.

## Value — PASS

A nonzero mobility floor and a finite ceiling are motivated by implementability: the unconstrained Itô minimizer from the motivating literature vanishes at the absorbing endpoint, while experimentally tunable diffusivity cannot be arbitrarily small or large. Under two physical bounds, the optimal design has an exactly solvable structural change from one to two saturated layers; the sharp threshold and the \(C^2\)-but-not-\(C^3\) value regularity give a quantitative phase diagram and a useful benchmark for numerical bounded-diffusivity design. Unlike a single special parameter example, the theorem classifies all positive floor, ceiling and mean triples in its domain. It does not claim higher-dimensional, non-Itô, or variance-optimal design results.

## Closest literature, comparisons and limitations

- L. Menon (2026), arXiv:2611.17470v1, §§II–III and Appendix B: fixed-average unconstrained optimum and numerical positivity floor; no analytic simultaneous upper and lower caps.
- L. Menon Jr., M. A. F. dos Santos and C. Anteneodo (2023), arXiv:2311.00818v1, §3.1: arbitrary-coefficient first-passage integral, not a constrained global optimizer.
- H.-R. Tung and S. D. Lawley (2025), arXiv:2512.19646v1, accessible abstract: three-dimensional small-target escape, not an exact bounded-design classification; the uninspected full text is an access-limited priority risk rather than evidence of absence.

This review assesses the specified one-dimensional Itô model and mean first-passage objective only. Complete bibliographic novelty cannot be certified from indexed searches.

Self-review: passed. Independent audit: not yet performed.

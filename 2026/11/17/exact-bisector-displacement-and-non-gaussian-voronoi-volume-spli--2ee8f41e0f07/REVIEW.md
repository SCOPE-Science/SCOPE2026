# Scientific review: exact two-site Voronoi splitting

## Correctness — PASS

For two independent volume-uniform sites, the midpoint–half-difference transformation has Jacobian \(2^d\). Its lens slices directly give the exact signed bisector density and normalization. The conditional cap-volume integral yields the complete cell imbalance law. In dimension three the polynomial density integrates to one and gives the exact imbalance variance \(421/4200\). A unimodal Laplace concentration argument supplies pointwise limiting bisector densities, and the smooth, invertible volume transformation supplies the limiting cell-imbalance densities. Both limits integrate to one, so Scheffé's lemma justifies **total variation**. The packaged checker was executed successfully; finite checks support but do not replace the analytic proof.

## Originality — PASS, provisional historical priority

Published research-record searches for two-site Euclidean-ball Voronoi volume, signed bisector displacement, beta-like offsets, high-dimensional volume imbalance and Laplace limits returned nearby but non-dominating research. The closest published geometry-related entries concern anisotropic Voronoi-cell connectivity, three-site *spherical* cell areas, and a clipped two-site *rectangle* small-cell tail; these do not imply this all-dimensional ball bisector density or the two Laplace limits. Relevant primary full text was read for Devroye et al. (2015), which studies the **large number of sites** regime, and Hoerrmann et al. (2014), which studies **Poisson hyperplane** zero cells. Neither contains the two-uniform-site fixed-ball law. A specialized earlier source not represented in the inspected indices may still establish an equivalent law; the priority claim is limited accordingly.

## Value — PASS

Random two-site partitions are the base case of Voronoi geometry and give a precise model of territorial balance in a bounded domain. The exact finite-dimensional distribution and a rational three-dimensional variance quantify that balance. The sharp choice of fluctuation scales and the limiting **Laplace rather than Gaussian** distribution reveal persistence of exponentially distributed radial-depth differences despite angular concentration. This is a natural complete law for a canonical geometry problem, not a bespoke numerical instance.

## Closest literature and limitations

- Devroye, Györfi, Lugosi and Walk, *On the measure of Voronoi cells*, arXiv:1512.04267v1 (2015); entire theorem statements and relevant proof sections compared. Site-count asymptotics, not a two-site high-dimensional splitting law.
- Hoerrmann, Hug, Reitzner and Thäle, *Poisson polyhedra in high dimensions*, arXiv:1403.8017 (2014); introduction, Poisson-process setup, statements and high-dimensional section compared. Different sampling model and cell functional.
- Schneider and Weil, *Stochastic and Integral Geometry* (2008); background reference, not used as evidence of exact claim exclusion.

No rate of total-variation convergence, more-than-two-site law, or extension to general convex bodies is proved. Exhaustive historical priority and independent validation are not claimed.

Self-review: passed. Independent audit: not yet performed.

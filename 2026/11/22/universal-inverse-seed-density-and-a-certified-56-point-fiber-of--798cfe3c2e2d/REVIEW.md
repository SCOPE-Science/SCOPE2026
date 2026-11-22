# Scientific assessment

## Correctness

**PASS (self-review).** The symmetric-parameter sine map factors through \(G(x,y)=(y(x+1),x(y+1))\). The coordinate change \(u=x-y\), \(v=x+y+1\) globally reduces the inverse to one scalar square root and identifies a two-sheet fold. Both sheets are compact polygons and their images have rectifiable boundaries; grid-cell counting gives a target-uniform \(O(t)\) error. The exact total Jacobian variation is \(13/3\), split into \(25/6\) and \(1/6\). The preimage spatial law follows from translated-lattice Riemann sums. The attached exact rational verifier certifies 43 strict interior and 13 boundary preimages when \(t=10\), with no undecidable comparisons. Analytical arguments, not finite tests, establish the asymptotic claims.

## Originality

**PASS against inspected sources, with priority uncertainty.** Feng et al. (2023), Section 3.1, define the two-dimensional map and treat simulated Lyapunov and encryption properties. The later Mathematics 2024 article reuses the map for image encryption without giving inverse-preimage classifications. Close indexed results address different maps, including a quadratic sine-circle fold and a four-partition planar inverse census; their equations and domains do not imply this map's quadratic fold, universal \(13/(3\pi^2)\) coefficient or 56-point baseline fiber. The area formula and elementary lattice point estimates are standard; their *methods* are not claimed as new. No matching full theorem was found in the sources inspected, but publication priority beyond that evidence remains open.

## Mathematical value

**PASS.** Inverse multiplicity is an intrinsic and motivated invariant for a published map used to generate deterministic sequences: it quantifies how many distinct states share a prescribed successor. The theorem covers every target, explains the exact two-fold phase geometry, identifies the sharp boundary-target halving law and the limiting \(25:1\) distribution between inverse sheets, and provides a complete exact finite certificate at the smallest published symmetric parameter. This is more than a sampled orbit test or an arbitrary parameter substitution.

## Limitations

The result concerns only one-step exact-real inverse fibers on the forward-invariant square, along equal control parameters. The infinite-gain limit continues the defining formula beyond the finite gain window of the original numerical study. It does not imply cryptographic attacks, generic forward ergodicity, entropy, Lyapunov positivity or floating-point behavior. The discrepancy \(O(t)\) may not be optimal, and unindexed equivalent mathematical work is a residual priority risk. Only the finite baseline is independently reproducible by the executable checker; the infinite law is supplied with a written proof.

## Closest literature

- W. Feng et al., *Exploiting Newly Designed Fractional-Order 3D Lorenz Chaotic System and 2D Discrete Polynomial Hyper-Chaotic Map for High-Performance Multi-Image Encryption*, Fractal and Fractional 7 (2023), 887, Section 3.1 and Equation (3), https://doi.org/10.3390/fractalfract7120887.
- *A Novel Multi-Channel Image Encryption Algorithm Leveraging Pixel Reorganization and Hyperchaotic Maps*, Mathematics 12 (2024), 3917, Sections 2.1 and 3.2, https://doi.org/10.3390/math12243917.
- *Area formula*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Area_formula, for the general multiplicity principle used in the proof.

Self-review: passed. Independent audit: not yet performed.

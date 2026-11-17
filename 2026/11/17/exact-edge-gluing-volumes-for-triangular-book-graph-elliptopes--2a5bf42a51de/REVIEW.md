# Mathematical review

## Correctness

**PASS.** The common-edge correlation is fixed before taking volumes. Every projected-elliptope fiber is exactly a product of planar Gram ellipses: an explicit orthogonal-residual construction establishes sufficiency of the independent local PSD conditions. Every cut fiber is exactly a product of triangle-cut parallelograms: a shared symmetric hub distribution and conditionally independent page spins establish sufficiency of the local inequalities. Their correctly normalized fiber areas integrate to the stated beta values, and the gamma ratio yields the sharp asymptotic with the stated first correction. The standalone program completed 2,216 checks, including independent convex-hull and quadrature computations; these are supplementary to the written proof.

## Originality

**PASS, subject to historical-priority risks.** The direct motivating paper [Avis–Devroye–Deza, arXiv:2604.16735, §3] already reports the star-suspension **cut** volume, the triangle example, a product theorem for at most one shared vertex, and a broad cosine parameterization for series-parallel graph elliptopes. None of these states the exact elliptope volume of the triangular book with pages sharing an edge. [Lee–Skipper, arXiv:1703.02444] concerns Boolean-quadric/cut volumes, as does the more recent series-parallel algorithm [Lee, arXiv:2610.00734]; neither evaluated the PSD book-graph elliptope volume in the inspected material. Related published book-graph results treat different convex bodies. The previously obtained volume of the graph without the hub edge is a marginal and does not numerically determine the added-coordinate body. Potential unindexed and differently parameterized prior formulas are acknowledged in AUDIT.json.

## Value

**PASS.** The result evaluates a natural full-dimensional convex body's volume in an infinite family and identifies a sharp exponential relaxation-volume gap with base \(\pi/2\). A contrast with vertex-gluing proves that the geometry of overlapping cliques—not merely the number of triangles—controls volume behavior. The exact beta law and nontrivial first asymptotic correction provide a reusable benchmark for semidefinite-relaxation volume comparisons.

## Limits and closest literature

The closed formula is limited to triangles sharing one edge; no arbitrary chordal-graph classification follows. The formula for the cut volume and the one-triangle PSD case are not new. Prior cosine image theorems remain stronger as *point-set parameterizations* but do not supply this stated numerical volume. The 2026 Jon Lee source was read through an accessible textual rendering rather than its original PDF; see AUDIT.json for all material and risks. The finite verifier is not a substitute for the analytic proof.

Self-review: passed. Independent audit: not yet performed.

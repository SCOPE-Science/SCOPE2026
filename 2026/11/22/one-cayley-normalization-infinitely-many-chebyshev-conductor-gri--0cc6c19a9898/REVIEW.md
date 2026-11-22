# Scientific review: Cayley normalization and Chebyshev conductor grids

## Correctness — PASS

The proof explicitly identifies the integral finite birational extension, verifies its normality by the isolated-nodal hypersurface criterion, and computes the conductor as \((f,u)\) using the module decomposition over \(\mathbb C[y,z]\). Simple roots and endpoint behavior of Chebyshev polynomials exhaust all singular strata. Formal coordinate changes establish every local form, and direct Jacobian ideals prove the single embedded length at every pinch and crossing. The intrinsic singular-component graph yields nonisomorphism of different unordered frequency pairs. The attached exact symbolic checker passes relevant finite samples, but the paper's ring and local arguments are the proofs for all parameters.

## Originality — PASS (best-knowledge, not absolute priority)

The initiating Mascarin article (arXiv:2611.15725v1) already gives the \((3,5)\) equation and states its six singular curves and four isolated points; that information is **not** claimed new. The older Chebyshev Varieties article (arXiv:2401.12140v1), particularly Proposition 5.8, offers general singular supports, and the 2025 Lissajous Varieties article (arXiv:2509.06844v1) supplies Cayley-cubic equations. The checked relevant material did not state the common **normalization**, exact **conductor**, full analytic and Jacobian strata, or the intrinsic **isomorphism classification**. Searches for index-independent Cayley normalization, Chebyshev conductor, pinch/crossing singularities and equivalent parametrizations returned related work on distinct objects, not a dominating theorem. Residual risk: unindexed specialized prior work and inaccessible historical records could contain equivalent calculations.

## Value — PASS

The result answers a motivated global question raised by explicit high-degree Lissajous equations: what changes intrinsically as the two frequencies vary? It shows a nontrivial dichotomy—one common normal surface but infinitely many mutually nonisomorphic nonnormal surfaces—whose information is captured exactly by conductor geometry. It also determines the local scheme, not merely a reduced singularity list. These are natural structural invariants useful for later deformation, desingularization and intersection studies without assuming any unproved downstream theorem.

## Scope and residual risks

Work is confined to affine complex surfaces, with no assertion in positive characteristic, no smooth resolution, and no integral arithmetic statement. Previous research establishes some of the reduced singular loci, and the Cayley cubic is classical. Publication priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.

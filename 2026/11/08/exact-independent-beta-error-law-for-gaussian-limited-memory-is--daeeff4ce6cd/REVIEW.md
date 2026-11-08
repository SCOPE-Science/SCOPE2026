# Scientific review: Independent beta contraction law for limited-memory Gaussian IS-Krylov

## Correctness

**PASS.** On a consistent scaled-isometry the source's sketched gradient is a scalar multiple of a standard Gaussian direction. The retained memory directions form a mutually orthogonal window, and the current error is orthogonal to this window. After orthogonalizing a fresh Gaussian, exact line search removes precisely the projection of the error onto that random direction. The conditional squared-error factor is therefore a beta-distributed complement of a squared spherical coordinate. Its conditional law depends only on the deterministic window size, establishing independence across iterations. Beta integration and the strong law give all stated moment formulas, sharp negative-moment threshold, and pathwise rate. The full-memory zero-ratio boundary follows from a one-dimensional complement. `verify.py` independently checks raw source-style updates and moment consequences. The proof does not rely on the Monte Carlo tests.

## Originality

**PASS, with priority risk.** The closest sources are Sun, Han and Xie (arXiv:2505.20602v1, Sections 3, 4.2 and Remark 3.6), Zeng, Cai, Han and Xie (arXiv:2605.25034v1, Section 2), and Zeng, Han, Su and Xie (arXiv:2305.05482, Sections 4–5). The first explicitly contains the finite-termination result when memory reaches rank, which is **not** asserted as new. Those sources furnish general expected-rate bounds and an adaptive orthogonalization algorithm; the inspected text did not state the exact independent adaptive beta factors, finite-time Mellin product, inverse-error integrability threshold, or almost-sure digamma exponent. Classical one-direction spherical beta laws are known and are used as a lemma, not claimed as original. Generic sketch-and-project theory and published random-projection claims in neighboring settings do not cover the specified sliding-window process or its whole error law. Literature indexing can miss mathematically equivalent older formulations; no claim of exhaustive novelty certification is made.

## Value

**PASS.** The exact product distribution resolves a natural theoretical gap between general expected-rate bounds and full pathwise uncertainty in a memory-controlled, randomized linear solver. It quantifies precisely the improvement from retaining additional orthogonal directions and distinguishes the typical rate from the expected squared-error rate. The sharp negative-moment threshold identifies what relative-error reliability statistics exist, a feature absent from convergence-factor upper bounds. The scaled-isometry case is a meaningful baseline for checking numerical methods even though it is not a general ill-conditioned solver theorem.

## Scientific limitations

Only consistent systems with scaled-orthonormal columns, independent rank-one Gaussian sketches, exact orthogonalization, and exact arithmetic are covered. The classical rank-memory finite-termination fact is acknowledged as prior. The verifier checks finite instances, not proof or priority. The result does not determine behavior under noisy data, anisotropic conditioning, block/structured sketching, or roundoff.

Self-review: passed. Independent audit: not yet performed.

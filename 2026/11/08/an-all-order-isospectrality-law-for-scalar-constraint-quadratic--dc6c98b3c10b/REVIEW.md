# Self-review

**Correctness — PASS.** An explicit determinant-preserving reduction of the ADMM characteristic pencil to a cyclic bidiagonal system establishes the complete polynomial for every block count \(n\ge2\), and strict Schur inequalities establish the stated three-block consequence. The independent standard-library exact-arithmetic checker makes 200 assertions, exhausts 152 finite fixed orders across \(n=2,3,4,5\), and tests 8 larger-size orders. These finite tests are supporting evidence, not the proof.

**Originality — PASS (best-knowledge, with precedence risk).** Direct searches compared the mathematical implication of the result with Mihić–Zhu–Ye's general QP permutation analysis, Cipolla–Gondzio's random multi-block QP analysis, the earlier Sun–Luo–Ye random-order theory, Ke–Ma–Zhang's three-block quadratic analysis, and an existing symmetric three-block ADMM penalty optimizer. General permutation-dependent bounds, a randomized per-sweep process, and an identical-curvature three-block optimizer do not entail the symmetric all-block fixed-order characteristic law. One plausible 2018 source could not be read completely; analogous rank-one Gauss–Seidel results may exist and remain a specialist-precedence risk. Literature searches do not prove priority.

**Value — PASS.** The all-block exact spectral law answers a motivated algorithmic question—whether expensive testing of all fixed cyclic orders can improve asymptotic spectral performance for rank-one-constrained separable quadratic ADMM—and shows that any benefit must lie elsewhere, such as finite-time transients. Its four-block explicit witness demonstrates a large real finite-time difference despite spectral equality. This is a structural classification, not an arbitrary isolated parameter value.

The result does not claim order-independence for per-epoch randomization, general constraint matrices, or uniform convergence for arbitrary numbers of blocks. A standard separate three-block Schur calculation is supplied as supporting scope rather than a separate novelty claim.

Self-review: passed. Independent audit: not yet performed.

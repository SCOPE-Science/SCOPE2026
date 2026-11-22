# Scientific review

## Correctness — PASS

For each \(n\ge3\), \(\mu>0\), and \(1\le k\le n\), the proof equates the Nyström residual to the inverse of the complementary principal precision block. Removing the chosen cycle vertices creates independent screened path blocks. Their continuants \(F_m\) yield a strictly convex trace cost \(F_m'/F_m\) and a strictly concave determinant log-value \(\log F_m\) as functions of the integer block length. Smoothing every gap difference of at least two strictly improves both criteria, establishing all optimizer and equality claims. The exact Wronskian identity yields the sharp runner-up determinant ratio, while a final strict smoothing step proves runner-up optimality. The reproducible source checker passed 8,695 exact-rational assertions. The universal proof does not rely on enumeration.

## Originality — PASS (inspected sources, with residual priority risk)

The closest reviewed Nyström paper by Belabbas–Wolfe (2009; arXiv:0906.4582v1) provides a general Schur-complement trace formulation and determinantal interpretation; its relevant sections do not classify screened-cycle gap optimizers or second-best deficits. Guestrin–Krause–Singh (2005) concerns general Gaussian-process sensor placement. Baz–Alonso–Pérez-Fernández (2023) concerns cycle correlation-matrix construction and asymptotics; the accessible sections do not supply landmark selection optima. Related interval Ornstein–Uhlenbeck designs study different processes and criteria. The accessible abstracts of a more recent periodic-mask study were insufficient for a whole-paper exclusion; this and unindexed equivalences remain risks. The absence of matching search hits is not a proof of first publication.

## Value — PASS

This is a complete natural fixed-budget landmark classification on an infinite structured family of dense inverse kernels, for both matrix approximation trace and information volume, with explicit optimal values and a closed combinatorial census. The second-best determinant loss quantifies a real finite-grid robustness margin. The \(C_6\) example proves that exact optima can be incompatible across successive budgets, which matters for append-only landmark policies.

## Limits and comparisons

This does not address arbitrary circulants or nonuniform coefficients, independent measurement noise, or general Nyström approximation complexity. Earlier Gaussian-process and Nyström frameworks imply the **definitions** and Schur-complement interpretations, not the strict finite-cycle optimizer classification. The most directly comparable interval-process design results concern different covariance geometries and do not provide the finite-cycle second-best loss.

Self-review: passed. Independent audit: not yet performed.

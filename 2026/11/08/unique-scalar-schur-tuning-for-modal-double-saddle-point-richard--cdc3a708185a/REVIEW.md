# Scientific review

## Correctness — PASS

For positive modal couplings and positive scalar preconditioner scale, the saddle matrix is invertible and the stationary error matrix splits exactly into three-dimensional modal blocks. Its characteristic polynomial is a zero root times a quadratic. The largest-coupling modal root product forces a necessary lower bound on the scalar scale at any claimed radius, and evaluating the smallest-coupling polynomial at that radius forces an upper bound. Their compatibility gives the sharp positive root of a strictly increasing quadratic. At the resulting scale, direct real/complex root analysis bounds every intermediate mode, and equality in the necessary inequalities proves unique optimality. The exact rational two-mode example and 9456 numerical checks in the supplied script support, but do not substitute for, the proof.

## Originality — PASS (qualified)

Liang and Huang (arXiv:2609.01031v1) provide this class of block-triangular approximation and general real/complex spectral analysis, but no exact scalar-scale minimax choice for the unit-step stationary iteration in the inspected sections. Bergamaschi, Ferronato and Martínez (arXiv:2505.06043) analyze a different triangular preconditioner and derive eigenvalue circle bounds, not this modal sharp lower bound and unique optimum. Notay (2014) provides general two-block spectral bounds, with 2013 lecture slides available; Pearson and Potschka (2023) treat an SPD factorization and ideal eigenvalue clustering. General two-block Richardson tuning and the 2022 parameterized SPD three-block literature do not supply the claimed formula by direct implication from their accessible statements. Priority remains qualified: unindexed equivalent special-case optimal scaling and inaccessible complete articles may contain related derivations.

## Value — PASS

Restricting the Schur approximation to a common scalar multiple of identity is a natural low-cost design constraint. The exact asymptotic factor of this stationary method is a natural performance quantity, and the theorem supplies the unique global tuning without solving a matrix optimization problem. Its two-extreme-mode balancing is structurally informative: the weakest mode reaches a real eigenvalue at the boundary while the strongest typically reaches a complex pair of the same radius. With two modal strengths 1 and 3 and secondary coupling 4, the sharp rate is 1/2 rather than the 3/5 from the largest-mode Schur scale. The claim does not imply improved finite-step GMRES convergence or general PDE performance.

## Closest literature and limitations

The main sources are arXiv:2609.01031, arXiv:2505.06043, and Y. Notay, *A New Analysis of Block Preconditioners for Saddle Point Problems* (2014, DOI 10.1137/130911962). Pearson–Potschka (2023) and Wang–Li (2022) are important but use different preconditioner classes. This result addresses exact commuting modal saddle matrices, one scalar Schur degree of freedom, and the asymptotic radius of unit-step Richardson; finite-dimensional numerical tests are not a proof for unrestricted matrix systems.

Self-review: passed. Independent audit: not yet performed.

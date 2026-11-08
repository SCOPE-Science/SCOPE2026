# Review: lifted–physical residual separation for scalar affine companion GMRES

## Correctness — PASS
The exact right-preconditioned companion columns form an independent chain. Their codimension-one orthogonal complement gives the finite residual norm for every positive integer Krylov length; the two first residual coordinates yield the recovered physical residual. The special one-step convention is included. Direct exact-rational finite least-squares computations and the symbolic limiting simplification support the proof but are not a replacement for it.

## Originality — PASS (qualified)
The closest primary reference is Gao and Jiang, *Toeplitz Infinite GMRES for Parameterized Linear Systems*, arXiv:2610.01740, especially the source definition of the companion residual and the positive lower bound outside the unit disk. This bound concerns the enlarged residual, whereas the claim relates it exactly to the original scalar-equation residual and exhibits an exact-cancellation locus. Earlier foundational work, Jarlebring and Correnty (arXiv:2102.04082) and Correnty, Jarlebring and Soodhalter (arXiv:2206.05153), describes companion GMRES, preconditioning and residual bounds without the same full scalar identity in the inspected text. Mathematically related published records address other Krylov residual/positivity properties, not this enlarged-versus-physical identity. Unindexed equivalent calculations remain a priority risk; a failed search does not prove novelty.

## Value — PASS
The source's lower bound naturally invites interpretation of the actual solution accuracy. The exact counter-separation shows why a positive lifted residual does not imply a positive physical residual, and locates the exceptional affine parameter curve plus the three convergence regimes. This is directly relevant to deciding which residual a stopping criterion should monitor. It does not prove failure of the underlying algorithm, superiority of a competing algorithm, or analogous cancellation for matrices and nonlinear families.

## Limits of verification
This is self-review with 175 exact-rational finite companion comparisons and one symbolic identity. The infinite statement follows from the written argument, not from sample coverage. Historical priority and floating-point behavior are not certified. Independent mathematical assessment was not conducted.

Self-review: passed. Independent audit: not yet performed.

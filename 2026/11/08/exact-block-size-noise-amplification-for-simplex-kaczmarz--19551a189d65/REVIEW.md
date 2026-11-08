# Scientific review

## Correctness

**PASS.** The Gram spectrum of the unit simplex implies an exactly one-dimensional inconsistent residual. Every selected subset has an invertible equicorrelation Gram matrix; its inverse gives the exact affine forcing vector and its squared norm. The average orthogonal row-span projector equals \((k/d)I\) by permutation symmetry and trace. Orthogonality of the projection residual and shift gives a *conditional equality* for squared error, from which the finite-time formulas follow without Jensen bounds or asymptotic arguments. Permutation isotropy also yields the entire covariance. The accompanying exact rational program exhaustively verifies the subset identities for dimensions two through seven; finite tests are secondary to the proof.

## Originality

**PASS under available evidence, with priority risk.** Gan and Wu (arXiv:2608.22259), especially the general sketch-and-project inequality in Section 5, is the nearest formal ancestor. It bounds the mean-square error but does not state an all-subset simplex equality law, covariance profile, or strict block-size reversal. Needell and Tropp (arXiv:1208.3805) use a fixed block partition and give paving-dependent convergence bounds; Needell, Zhao and Zouzias (arXiv:1403.4192) incorporate a residual-correction process different from this unextended iteration. The exact parameter specialization and asymptotic saturation are close to generic proof techniques, so an older equality case or a derivation embedded in another work remains a real priority risk. Search failure alone is not a novelty proof.

## Value

**PASS.** Regular-simplex rows form a natural, minimally overdetermined unit-norm tight frame, and their entire least-squares inconsistency is a single identifiable common-mode residual. Block size is the method's central cost/contraction parameter. The formula exposes a dimension-unbounded factor between the fastest noiseless-contraction choice and the least noisy steady-state choice, while avoiding any confounding change in the least-squares solution. Exact finite-time covariance permits direct error-budget comparisons. It is not a universal negative theorem for block Kaczmarz.

## Limits

Only uniform independent size-fixed subsets and ordinary, unextended exact block projections are covered. The coefficient/response observations are fixed, not redrawn each iteration. The result does not address partitions, extended corrections, computational cost or general frames. Independent external validation is absent.

Self-review: passed. Independent audit: not yet performed.

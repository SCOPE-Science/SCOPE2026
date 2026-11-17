# Self-review

## Correctness — PASS

The input space is all real or complex \(3\times3\) matrices, with the Ky Fan-two norm equal to the sum of the two largest singular values. A singular-value-cone decomposition reduces every unit-ball input to three classes of partial isometries (rank one, rank two, and full rank) with total coefficient at most one. Rank two is bounded by Frobenius nonexpansivity; the full-rank class is bounded by an explicit unit-circle three-point inequality; rank one has an exact one-variable singular-value expression maximized at overlap squared \(3/8\). An explicit nonnormal real matrix attains the result. Orthogonal/unitary conjugation averaging independently proves the minimum projection claim, including real-linear projections on complex matrices. The self-adjoint comparison is independently proved by scalar extreme-point reduction. Exact symbolic identities and representative numerical matrices were checked using the packaged script. No extrapolation from finite enumeration is made.

## Originality — PASS (qualified)

Foucart, *Computation of Minimal Projections and Extensions*, §4, Theorem 1 and Corollary 4, was read in the open author PDF. Theorem 1 gives norm-minimizing trace-centering, and Corollary 4 gives only a nonsharp intermediate Ky Fan bound of \(4/3\) in the present dimension; neither asserts the exact \(1/2+\sqrt6/4\) constant. The separate self-adjoint result concerns Hermitian matrices, where the constant equals one, and therefore cannot imply this full-matrix formula. Targeted mathematical-record searches for the operator, parameter, radical constant and equivalent traceless/symmetric-gauge formulations produced no exact match. An unindexed older finite-dimensional matrix-norm result remains possible, and this review is not a historical-priority certification.

## Value — PASS

Dimension three is the first size supporting a genuine intermediate Ky Fan norm. The theorem determines the corresponding natural zero-trace minimum-projection constant and locates its extremizer among nonnormal rank-one matrices, despite contraction on the self-adjoint subspace. It also improves the explicit older upper bound \(4/3\) to a sharp achieved value. The distinction matters in applying trace removal to general nonselfadjoint matrices; no general-dimensional theorem is claimed or needed for the precise boundary question.

## Limits

Only matrix dimension three and Ky Fan rank two are resolved. The proof does not classify every extremizer or all minimal projections. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.

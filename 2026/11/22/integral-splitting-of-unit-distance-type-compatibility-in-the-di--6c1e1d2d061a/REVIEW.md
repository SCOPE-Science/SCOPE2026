# Scientific review

## Correctness — PASS

The admissible types are exactly the core \(\{2,3,4\}^n\) and the \(n\) exceptional families with one coordinate equal to one and all other coordinates in \(\{3,4\}\). The four-point metrics determining each matrix entry are governed by the original triangle inequalities. The core unit-distance matrix is the tensor power of the explicit unimodular three-by-three matrix \(T\). The cross-block rows each carry an exceptional vector annihilating every possible cross factor under \(T^{-1}\), proving the integer identity \(HD^{-1}H^{\mathsf T}=0\). The block elimination and its inverse use only integer matrices of determinant one, so the Smith-form and real-inertia conclusions hold for all positive \(n\). `VERIFY.py` reconstructs the matrix independently and checks the integer identity and modular ranks through four parameters. Computation is corroboration rather than an infinite proof.

## Originality — PASS (provisional)

Sauer (arXiv:1010.4212, Sections 2 and 4) proves the underlying Katětov type and possible-orbit-distance criteria; Conant (arXiv:1504.02427, Introduction) establishes the general integral Urysohn framework. The previously published diameter-three Widom–Rowlinson one-type polynomial counts scalar types but does not determine this new matrix. Available historical claims include a diameter-four scalar type count and a diameter-three compatibility Smith form, neither of which implies the integral splitting claimed here. Searches for alternative Katětov, Urysohn, tensor and Smith-form formulations found no decisive covering statement. The standalone number sequence \(3^n+n\) occurs in unrelated databases and is not claimed as a new integer sequence. Residual risk: an equivalent integral principal-submatrix formula might exist under another combinatorial name.

## Mathematical value — PASS

The result gives an exact integral and real-spectral classification of a natural pair-realizability relation, even though its indexing set grows as \(3^n+n2^{n-1}\). The tensor-plus-isotropic-block decomposition explains the growing nullity, why every prime sees the same rank, and the surprising linear signature \(n+1\). This is not an isolated small determinant or a rebranding of an existing type-count formula. Its directly reusable principal-unimodular-core certificate is mathematically more informative than numerical checks alone.

## Scope and risks

The theorem is limited to individually named equilateral distance-four parameter sets, mutual distance one, and the finite distance alphabet \(\{0,1,2,3,4\}\). Relevant older papers supply the logical extension setup but not independent confirmation of this new arithmetic statement. Historical priority is provisional; no independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.

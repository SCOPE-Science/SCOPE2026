# Scientific review

## Correctness — PASS
The statement uses normalized finite-group Fourier coefficients and an exact two-character rank projection. Each quotient character has odd order, so the phase extremizer is everywhere defined. Its discrete Fourier coefficients are obtained by a geometric sum and have exactly two strictly largest moduli; hence the norm of the linear projection is attained under the nonlinear greedy constraint. Equality in the convolution triangle inequality and strict monotonicity of the finite root-of-unity norm classify every extremizer. `verify.py` checks the coefficient identity, strict ranking, sharp evaluation, kernel norm, and quotient example numerically; these tests are supplementary to the general proof.

## Originality — PASS relative to inspected sources
Nielsen's 2026 theorem provides large magnitude-threshold sums on high-dimensional odd cyclic products, rather than the exact coefficient-count-two constant or its equality cases at fixed group order. The closest published two-frequency concentration formula gives the denominator of the projection kernel but optimizes the spatial concentration of equal-coefficient idempotents, not the Fourier-coefficient-ranked input. Consequently it gives the linear projection constant, not the nonlinear equality or the prime-divisor rigidity. The 2018 Chebyshev thresholding paper concerns best approximants and asymptotic rates rather than the raw greedy partial-sum norm. The searches do not exclude unindexed folklore, which is the primary residual bibliographic risk.

## Mathematical value — PASS
Fourier coefficients ordered by magnitude define a nonlinear selector, and its exact amplification is a natural finite-scale invariant behind rearranged Fourier-series stability. The theorem determines this invariant uniformly on every finite odd-order abelian group, locates the precise group-theoretic source of the worst case (smallest prime torsion), proves that optimizing a linear projection is compatible with the nonlinear ordering, and classifies all equality signals. The result is intentionally limited to the first nontrivial coefficient count and does not infer an infinite-group divergence statement.

Self-review: passed. Independent audit: not yet performed.

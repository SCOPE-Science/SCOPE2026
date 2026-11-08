# Self-review

## Correctness — PASS

The spectral-gradient distribution has mean equal to the reciprocal step length. Convexity of the even power gives an endpoint chord at the *same mean*, yielding an exact reduction to two eigenvalues rather than merely a loose worst-case estimate. The displayed two-mode recurrence, strict monotonicity in the condition number, and the threshold crossing are algebraically established. Strict power-mean comparison proves threshold ordering. The asymptotic sandwich controls the whole positive half-line, not only a candidate local optimizer. The standalone checker executed successfully for exact rational samples and supplementary numerical threshold examples. Finite checks are not used as proofs of universal claims.

## Originality — PASS, qualified

The closest primary work studies two-spectrum cyclic steepest descent and long-time convergence; it provides two-eigenvalue formulas that relate to the algebra here, but the all-spectrum fixed-matrix endpoint extremality, dimension-independent safety frontier, its strict cycle-length ordering and logarithmic transition are not directly covered in the material inspected. Older cyclic Barzilai–Borwein literature concerns convergence rates and function-value performance, and published related results about stagewise-safe Richardson or recurrent exact line search use distinct step policies. There is a residual possibility of an unindexed or differently phrased analysis deriving equivalent global gradient-safety conditions. This is not an independent historical-priority certification.

## Value — PASS

Finite-cycle gradient norms are a natural diagnostic for step reuse: repeated steps can improve long-run cost while amplifying a monitored gradient within a cycle. A sharp test that applies in any dimension but is exactly witnessed by two extreme modes gives a usable, algorithm-specific conditioning bound. The decrease of that bound toward \(2\) at logarithmic-over-linear speed shows explicitly how increased reuse can erode gradient-norm safety. This is a structural result, not a renamed isolated two-dimensional computation.

## Scientific limitations

This is a cycle-boundary, exact-arithmetic result for fixed SPD quadratics with a single reused exact Cauchy step. It is not a pointwise objective decrease theorem or an optimal convergence rate theorem. Numerical root locations are illustrative only. Primary-source and indexing coverage cannot rule out unpublished or unindexed equivalents.

Self-review: passed. Independent audit: not yet performed.

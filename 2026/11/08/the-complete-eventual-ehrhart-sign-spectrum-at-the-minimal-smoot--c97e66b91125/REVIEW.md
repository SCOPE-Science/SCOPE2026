# Self-review

## Correctness — PASS

The slice-counting identity and the smoothness/facet statement are Proposition 5.1 of [1]. Expanding the binomial numerator gives exactly two leading twist powers, and the Faulhaber formula gives nonzero even Bernoulli coefficients at every intermediate Ehrhart degree. Odd Bernoulli cancellation at the top twist power is recovered at the next power, so there is no omitted coefficient class. Top and constant degrees are handled separately. For each fixed dimension, the finitely many nonzero coefficient-leading terms establish one simultaneous eventual threshold. Reconstructed symbolic identities agree with 518 exact arithmetic checks performed by the included verifier, but the proof, not enumeration, establishes the infinite range.

## Originality — PASS (historical priority provisional)

The exact same polytope family occurs in [1], but its Theorem 5.2 establishes only negativity of the coefficient in degree \(d-4\), not the complete sign vector or the separate, canceled \(c^{r-1}\) tier. The stronger all-middle-negative construction of [2] has much higher facet counts and does not imply the facet-minimal full classification. The h*-shape questions in [3] are mathematically different. Searches across the mathematical literature and accessible research records found no claim implying the presented all-degree statement. Residual priority risks include an independently derived equivalent Faulhaber classification under an unexpected name. No independent novelty certification is claimed.

## Mathematical value — PASS

The minimal facet count is a sharp geometric constraint, already established in [1]; determining every Ehrhart coefficient's eventual sign under this constraint is a natural structural question. A single-sign counterexample does not answer it. The two-tier Bernoulli cancellation reveals an alternating paired-sign structure and shows that the number of simultaneous negative coefficients increases without bound even at the geometric minimum. This is an all-dimensional classification, not an arbitrary isolated computation. It does not claim to optimize the number of negative coefficients among every minimal-facet polytope.

## Scope and remaining risks

The onset twist is not optimized. Numerical tests cover finitely many dimensions. Historical completeness is uncertain, especially for implicit equivalences of simplex bundles and generalized Hirzebruch polytopes; independent external review remains appropriate.

Self-review: passed. Independent audit: not yet performed.

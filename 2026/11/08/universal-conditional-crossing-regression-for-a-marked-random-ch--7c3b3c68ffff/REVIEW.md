# Scientific assessment

## Correctness — PASS

For each feasible bridge count, the three remaining chord classes have deterministic sizes and exchangeable endpoints. Their pairwise crossing probabilities are exactly \(1/3\), \(1/2\), or zero depending on types, yielding a first-moment formula with cancellation of the quadratic degree term. The precise domain, parity support, and boundary degeneracies have been checked. An independently implemented complete matching enumeration for \(n=3\) through \(7\) passed 291 exact rational assertions, without substituting finite enumeration for proof.

## Originality — PASS (qualified)

The full 2015 Acan paper, especially Section 2 on conditional chord degree, the Flajolet–Noy report on global chord crossing moments, and the Paguyo paper on global crossing limit theorems were compared at the level of their actual statements. They do not give the pointwise conditional mean of remaining crossing pairs given a marked chord's degree, whose slope is independent of the chord's location. A separate conditional covariance or variance formula would not determine a conditional regression at every feasible degree. The closest potential source of implicit coverage is the more general Touchard–Riordan joint and multivariate enumeration literature: neither a universal historical novelty guarantee nor an independence claim is made.

## Mathematical value — PASS

The marked chord degree is the local degree of a distinguished vertex in the random chord intersection graph, and the number of crossings among the others is the remaining graph's edge count. A universal affine conditional mean across all arc imbalances is a natural and non-obvious local-global dependence law: the individual degree distributions vary strongly with marked chord length, but their conditional prediction slope does not. This gives exact finite-size conditional information not recoverable from separate global and local moments, even though it requires no new asymptotic theorem.

## Closest sources and limitations

Acan, arXiv:1501.01489v1, Section 2; Flajolet–Noy, *Analytic Combinatorics of Chord Diagrams*, Sections 1–3; Paguyo, arXiv:2104.01134, Introduction and distributional estimates. The statement determines only the conditional mean, not the conditional distribution or higher moments; historical implicit coverage remains a priority risk.

Self-review: passed. Independent audit: not yet performed.

# Review: exploration–displacement coupling

## Correctness — PASS

Writing the step histogram as a multinomial vector makes exploration the sum of occupied-coordinate indicators and displacement the sum of odd-coordinate indicators. Same-coordinate and different-coordinate covariances yield the exact formula; strict Jensen supplies the sign. Pairwise avoidance and parity transforms give both variances. Uniform expansions at \(t/n\to c\) and \(t/(n\log n)\to\beta\) yield the announced profiles. The original standalone verifier reproduces 28 exact enumeration cases (140 exact moment comparisons), 84 finite positivity checks, and 13 numerical asymptotic spot comparisons. Numerical work does not replace the uniform asymptotic proof.

## Originality — PASS, with historical-priority qualifications

An exact-source/alias search compared the full inspected occupancy studies, the finite hypercube mixing article's accessible abstract and references, the bit-flipping model abstract, and full published-finding corpus files on occupied-indicator precision and richness–single-frequency covariance. **The earlier published-finding corpus exact formula for every frequency implies this candidate's finite numerator covariance by summation over odd frequencies; the numerator is NOT original.** The precise \(t/n\) correlation profile and \(n\log n\) decay instead require the parity-count variance and triangular-array analysis, and are not stated or directly entailed by the older results alone. Earlier normalized-correlation formulas in unavailable sources remain a priority risk. No claim of proven priority is made.

## Value — PASS

The explicit normalized-correlation crossover is the central quantitative finding: individual coordinate flips can cancel displacement but not exploration, yet the two statistics retain a positive dependence for every finite time. The explicit crossover from near-perfect correlation as \(c\downarrow0\) to polynomially small correlation on the \(n\log n\) scale is a natural joint-statistics benchmark not delivered by marginal occupancy variance, parity variance, or hypercube mixing alone. The cross-covariance in isolation is not counted as new or sufficiently valuable.

## Limits

Only uniform independent coordinate choices without holding are treated. The proof does not establish strict monotonicity of the correlation in time, a joint CLT or a mixing theorem. Older full-text access was incomplete for the two classical random-walk / bit-flip references.

Self-review: passed. Independent audit: not yet performed.

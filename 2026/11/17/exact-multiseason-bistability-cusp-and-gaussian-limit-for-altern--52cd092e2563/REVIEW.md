# Mathematical review

## Correctness — PASS
The return is obtained by exact composition: \(A_\alpha^{\circ m}(x)=\alpha^{2^m-1}x^{2^m}\). Fixing \(d=2^m\), roots are precisely intersections of the horizontal line \(p\) with \(R_q(x)=x/[1-q(1-x)^2]^d\). Its derivative has the sign of \(1-q(1-x)[1+(2d-1)x]\); its maximum-factor threshold and two roots give all possible fixed-point counts and folds. Because the return is increasing, monotone-iteration arguments prove global convergence and basin separation. At the unique triple fixed point the third derivative is strictly negative, and reciprocal-square telescoping yields the stated \(n^{-1/2}\) constant. Uniform convergence of logarithmic derivatives establishes the limiting Gaussian map and its cusp. The independent symbolic checker covers finite depths and the explicit three-root witness but is not an infinite-depth proof.

## Originality — PASS within inspected sources
The strongest close analogue is the published exact cusp diagram for the strictly alternating quadratic map of Lawnik–Moysis–Volos (the \(d=2\) case), and it is expressly excluded. The work of Jamilov–Mukhamedov–Mukhamedova–Souissi establishes regularity for individual operators and certain within-class compositions, not coexistence of two attracting cycles under opposing seasonal operators. Actual mathematical database searches for iterated quadratic extinction and a multi-season cusp found the exponent-two analogues, not a theorem for every \(d=2^m\), the explicit \(q_d,p_d\), and Gaussian season limit. General one-variable fold theory is background and does not supply the stated exact formulas. An unindexed equivalent treatment remains a risk; no claim of exhaustive uniqueness is made.

## Value — PASS
Individually regular population maps can exhibit bistability under a natural deterministic schedule, exposing a substantive distinction between autonomous and periodically alternating dynamics. An exact all-season cusp threshold predicts when the competing attracting populations occur. The limiting Gaussian map and explicit critical scaling identify a nontrivial large-season transition, not merely a single arbitrary finite computation.

## Scope and literature boundaries
Only two-species quadratic stochastic maps with one opposite-selection season and \(m\ge2\) identical extinction seasons are classified. Finite checker tests support, but do not replace, the proof. Closest inspected sources are doi:10.1002/mma.10191 and doi:10.3390/sym15071311, together with the published \(d=2\) exact return-cusp analysis. A wider literature search or independent proof audit could change publication-priority assessment.

Self-review: passed. Independent audit: not yet performed.

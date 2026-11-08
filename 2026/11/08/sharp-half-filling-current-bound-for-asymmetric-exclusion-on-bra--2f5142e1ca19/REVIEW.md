# Scientific review

## Correctness

**PASS.** The proof specifies a connected finite graph with periodic backbone, exact half filling, positive tree rates and nonnegative backbone rates with positive clockwise bias. Stationarity is established by per-edge tree detailed balance and the equality of \(10\) and \(01\) counts on each ring configuration. The canonical pair probability follows by elementary-symmetric coefficient extraction. The coefficient identity is verified algebraically from the binomial expansion and has positive coefficients for all permitted indices. Equality occurs when no pair of nonunit activities exists. Particle-hole complementation handles activities below one; the mixed-sign witness is rationally exact. The separately executed `verify.py` passed 334 exact checks, including explicit generator-balance checks.

## Originality

**PASS, qualified.** The primary article arXiv:2603.09694v1 provides a general stationary measure and formulas for two selected tree geometries, but the inspected sections do not state a half-total-filling bound uniform over all rooted tree geometries, its exact positive deficit polynomial, its equality characterization, or the mixed-sign sharpness witness. The broader balance-network source arXiv:1207.3552 gives factorized weights rather than this inequality. The precise implication relationship is that the present result uses the prior stationary distribution as a premise; the nonnegative elementary-symmetric identity supplies the comparison theorem. published-finding corpus searches for the source, half-filling current bound, weighted canonical sampling and elementary-symmetric aliases produced no scientifically covering result among their closest hits. A possible unindexed general coefficient inequality is a residual risk.

## Value

**PASS.** The question addresses a natural transport-design issue posed by the primary literature: whether attaching biased tree networks can increase the flow at a fixed particle budget. The result gives an all-size and all-tree-shape no-enhancement theorem exactly at half-total-filling, an equality rigidity condition, and a minimal opposing-bias counterexample defining the boundary of validity. The positive polynomial is a finite-size quantitative loss certificate, not merely a restatement of the stationary law.

## Closest literature and limitations

The 2026 tree-branch ASEP paper supplies the factorized canonical measure and special-geometry current sums. The 2012 balance-network paper supplies a more general factorization principle. The 2024 transition-decomposition paper establishes broader exact steady-state methods. No stronger directly applicable published half-filling current inequality was located, but unindexed or difficult-to-access treatments may cover the result. There is no assertion for arbitrary mixed-sign branch biases or for non-half-filled systems.

Self-review: passed. Independent audit: not yet performed.

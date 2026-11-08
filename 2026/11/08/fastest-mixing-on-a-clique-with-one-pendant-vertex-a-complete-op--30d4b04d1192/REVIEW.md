# Mathematical assessment

## Correctness — PASS

The centered vector with entries \((2n-1,n-2,-3,\ldots,-3)\) gives a Rayleigh upper bound on the Laplacian spectral gap that directly yields the exact SLEM lower bound and a sharp hub-holding penalty. Equality forces every pendant/hub incident edge probability. The complete three-dimensional quotient has characteristic polynomial \(s(s-(n+1)/(5n-4))(s-3(2n-1)/(5n-4))\); the remaining block is \((1-p)I-L_W\) on the ordinary vertices' constant-orthogonal subspace. Its interval constraint is necessary and sufficient, and uniform internal weights attain the optimum. Symbolic verification checks the algebraic factorization; finite numeric checks are supportive, not the proof.

## Originality — PASS with residual risk

The exact four-state case \(n=3\), including SLEM \(7/11\) and optimizer nonuniqueness, is in Boyd, Diaconis and Xiao (2004), Figure 1(b), Table 1 and their rank-one dual example. It is expressly excluded from the new-range claim. The new statement covers the infinite \(n\ge4\) family, the full set of non-invariant optimizers, and a quantitative holding penalty. The inspected Boyd–Diaconis–Parrilo–Xiao analysis concerns bridges between **equal** cliques, a different graph family. Roch gives general variational bounds, not this closed-form global optimizer face. Search of publicly indexed mathematical records yielded no directly dominating theorem. Unindexed treatments of a single pendant on a clique or general unequal clique bridges remain possible; lack of retrieval does not certify priority.

## Value — PASS

An isolated pendant can dominate convergence even when its adjacent core becomes dense; the exact optimum tends to \(4/5\), unlike the standard degree-normalized walk whose gap tends to zero. The theorem identifies all local probabilities forced by optimality and all remaining design freedom, offering a concrete implementation and robustness check. This is an infinite-family exact classification, not an incremental recomputation of the published four-vertex example.

## Boundaries

The result is for symmetric stochastic matrices and discrete-time SLEM; it does not optimize nonuniform-stationarity or nonreversible chains and does not evaluate all finite-time mixing constants. The theoretical conclusion is analytic; the checker samples only finitely many graphs. The literature overlap risk is not zero.

Self-review: passed. Independent audit: not yet performed.

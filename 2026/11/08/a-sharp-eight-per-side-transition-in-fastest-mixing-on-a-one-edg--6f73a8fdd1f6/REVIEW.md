# Scientific review

## Correctness (PASS)

The graph, allowed symmetric stochastic kernels, holding probabilities, operator-norm objective and quantifiers are stated explicitly. Averaging over all graph automorphisms gives an invariant global optimizer without asserting non-invariant uniqueness. The invariant matrix has two edge orbit variables. Orthogonal decomposition yields exactly \(2n\) eigenvalues with their multiplicities. In the small branch, the odd block norm has universal lower bound \(1/\sqrt n\), with equality forcing the displayed two weights; the remaining eigenvalue meets the bound exactly for integer \(3\le n\le7\). In the large branch, the radical kernel meets all stochastic constraints, has quotient eigenvalues \(\pm r\), and has ordinary difference eigenvalue \(r\). A convex subgradient with a strictly interior one-sided coefficient proves the global lower bound and invariant uniqueness for every integer \(n\ge8\). The pure-Python verifier independently constructs full matrices; its finite checks are supplementary and not substituted for the infinite proof.

## Originality (PASS on inspected evidence)

The graph-specific claim is a closed-form FMMC evaluation for \(K_{n,n}\) with one missing crossing edge, including the sharp change at \(n=8\). The 2004 Boyd–Diaconis–Xiao full text solves the intact biclique and states the general convex program; the 2007 Boyd–Diaconis–Parrilo–Xiao full text develops orbit/block methods and treats the intact biclique, but the inspected sections do not evaluate this single-edge deletion. The 2010 Jafarizadeh full-text sections concern symmetric/semi-symmetric pseudo-distance-regular multipartite patterns, not the single missing crossing edge. The general semidefinite formulation does not itself give the two-orbit radical optimum or its crossover. Published semantic searches and accessible historical claims showed no stronger statement with the same consequence. The closest accessible related record fixes the outgoing mass of one vertex in an **intact** biclique and retains all its crossing edges, so it cannot be substituted to force one specific edge absent. Limits: the literature search is not exhaustive; inaccessible or unindexed equivalent treatments may exist.

## Value (PASS)

One failed edge is the smallest nontrivial asymmetric fault in a dense two-community graph. Its complete optimal symmetric mixing design differs sharply from the intact graph and exhibits two exact regimes separated by the natural integer cutoff \(n=8\). The theorem gives the optimal SLEM and implementable transition probabilities for every size, with all-row feasibility and the uniqueness claim scoped exactly to invariant designs. These are practically interpretable benchmark data for consensus and reversible sampling and are not mere numerical instances or a renaming of the known intact-biclique formula.

## Limits and closest literature

Boyd–Diaconis–Xiao (2004), Sections 1 and 7.1; Boyd–Diaconis–Parrilo–Xiao (arXiv:0709.0955v1), Sections 3.1.2 and 5.3.1; and Jafarizadeh (arXiv:1008.2588v1), Section III. The claim does not classify all non-invariant optimal matrices, varying stationary laws, unequal part sizes or finite-time total-variation optimizers. No independent audit has been done.

Self-review: passed. Independent audit: not yet performed.

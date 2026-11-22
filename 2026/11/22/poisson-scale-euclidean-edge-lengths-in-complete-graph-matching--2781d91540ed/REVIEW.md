# Scientific review: Poisson-scale Euclidean edge lengths in complete-graph matching polytopes

## Correctness — PASS

The claim specifies a complete graph, the full matching polytope, its standard Euclidean edge-indicator embedding, and the distinction between finite enumerators and asymptotics. The established adjacency criterion reduces geometric neighbors to one alternating path or cycle. Four disjoint endpoint classes give the exact coefficients, with reversal divisions checked even for the smallest path lengths. The exact ratio \(A_{k,k-r}/A_{k,k}=1/(2^rr!)\) proves the Poisson limit, while cycle weights are negligible because of their additional \(1/j\) factor. The accompanying verifier exhaustively reconstructs all 34 strata for \(n\le10\) by a different combinatorial computation; the infinite theorem follows from the argument, not the finite tests.

## Originality — PASS, subject to unindexed priority risk

The closest primary exposition is Abreu–Costa–Nascimento–Patuzzi (arXiv:1701.06210), whose degree formula counts alternating paths and cycles without evaluating the complete-graph metric-length polynomial or a near-perfect Poisson limit. Merino–Mütze (arXiv:2304.08567) proves existence of short-exchange Hamilton listings, not the distribution over *all* incident edges. Ito et al. (arXiv:1907.01700) study shortest sequences of perfect-matching flips, not local Euclidean edge lengths. Relevant indexed results concern rectangular bipartite matching polytope degrees, complete-graph matching covariance, or Euclidean inballs, and do not dominate the present assertion. The generic path/cycle characterization is a necessary known premise, not claimed as new. Historical priority remains provisional in the presence of unindexed or inaccessible prior work.

## Mathematical value — PASS

The exact metric edge spectrum refines scalar degree information into a complete stratified local geometric invariant for a classical infinite family. Its asymptotic law identifies an unexpected Poisson *defect from maximal-length exchanges*: the enormous majority of a nearly perfect matching's polytope neighbors differ on all but a tight number of matched pairs, while a Hamilton listing needs only bounded-length exchanges. This quantifies the distinction between typical adjacency geometry and special efficient traversals, a natural issue raised by the cited traversal literature.

## Limitations

Only standard orthonormal edge coordinates of complete graphs are covered; noncomplete graphs, rescaled metrics and global skeleton distances are outside the theorem. The fixed-uncovered-count requirement is essential to the stated limit. Exhaustive computation is finite confirmation, not a proof of asymptotics. Historic equivalence to an unindexed source remains possible; no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.

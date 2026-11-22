# Self-review

## Correctness — PASS

The geodesic reachability order in a Cartesian product of complete graphs has the explicit coordinatewise criterion \(x\preceq_r y\) iff each coordinate of \(x\) equals the root symbol or the corresponding symbol of \(y\). Every rooted geodesic is a chain and every chain embeds in one rooted geodesic. On an endpoint geodesic, two chronological vertices are incomparable exactly when their intervening coordinate updates include a nonroot replacement or both an addition and an erasure. Counting disjoint charged segments gives the upper bound, and ordering alternating erasure/addition pairs followed by replacements attains it. Optimizing the numbers of transitions gives the mixed-factor formula for every root. Small exhaustive computations independently confirm both formulas; finite checks are supporting evidence, not the infinite proof.

## Originality — PASS (qualified)

The closest published works are Chakraborty et al., ISAAC 2022, DOI 10.4230/LIPIcs.ISAAC.2022.12, and Chakraborty et al., MFCS 2023, DOI 10.4230/LIPIcs.MFCS.2023.32 / arXiv:2301.00278. The 2022 work defines the antichain parameter and proves approximation results; the 2023 work defines the rooted-path version and proves equivalence and general bounds. Their inspected texts do not give the fixed-terminal formula or mixed Hamming product law. A prior homogeneous Hamming-graph computation already determines the all-binary and all-nonbinary uniform-alphabet specializations; these are recognized as prior coverage and excluded from the new theorem's claim. Searches for equivalent formulations and mixed-factor coverage found no dominating statement. This is a best-knowledge assessment; absence from indexed sources does not establish absolute priority, and some unindexed work may remain.

## Mathematical value — PASS

The theorem computes a natural distance-based structural parameter on all heterogeneous Hamming products, where binary and larger alphabets interact rather than behave uniformly. The terminal-conditioned refinement is stronger than a scalar formula: it gives the exact extremal cost of covering the vertices of a path between prescribed terminals, and explains both the one-per-replacement and one-per-addition/erasure-pair mechanisms. Mixed products model networks with Boolean and categorical coordinate links; the result supplies sharp certificates for their rooted shortest-path routing complexity. This is not a re-enumeration of the previously known homogeneous case.

## Closest literature and limitations

The original isometric path cover number (covering the entire graph by shortest paths) differs from covering each individual shortest path by paths with a common root. Results about the former do not imply the latter. A relevant later strong-isometric-path-complexity paper concerns broad structural graph classes and operators rather than an exact terminal-conditioned mixed Hamming formula. Independently indexed publication priority cannot be guaranteed. The proof does not classify every maximizing coordinate permutation or extend to Cartesian products with noncomplete factors. Finite tests cannot prove the unrestricted statement.

Self-review: passed. Independent audit: not yet performed.

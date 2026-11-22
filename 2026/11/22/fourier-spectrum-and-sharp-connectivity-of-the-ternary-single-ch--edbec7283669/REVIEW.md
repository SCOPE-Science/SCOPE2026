# Self-review

## Correctness — PASS
The codeword set is exactly the vertex set in the one-hot product-of-simplices embedding. A coordinate face yields a necessary-and-sufficient minimal-zero-sum adjacency criterion, not just a sufficient combinatorial test. There are only three nonzero minimal-zero-sum sequence patterns over \(\mathbb F_3\), giving precisely the stated length-two and length-three generators. Fourier diagonalization on the finite abelian single-checksum subgroup produces the exact cubic-root character identity. Its multiplicity quotient is free, and the minimization of the exact positive form \(F\) is proved uniformly, with all equality cases. Verified finite exhaustive tests and an independent linear-programming midpoint test agree with the statement.

## Originality — PASS (priority provisional)
Rosnes and Helmling's 2015 ternary conference paper and 2017 arXiv paper already treat the **same ternary single-parity codeword polytopes** and provide the complete facet inequalities; neither is claimed as new. Their inspected full 2017 paper (especially Theorem 3, p. 15) establishes a complete facet description but does not evaluate the one-skeleton's complete spectrum or its Fiedler eigenvalue and multiplicity. The earlier 2015 full text was not obtained; its abstract identifies facet/decoder work, so it is retained as a residual priority risk. Frede–Kaibel–Merkert (2024) treats **binary**, not ternary, cyclic transversal polytopes. Existing related checksum Fourier-sampling and binary edge-census results concern distinct operators or fields, and do not imply the evaluated ternary cubic character polynomial without the separate new adjacency analysis. Search absence alone was not used as the novelty argument.

## Mathematical value — PASS
For the full, naturally embedded family of ternary single-check codeword polytopes, the result exactly determines the edge metric census **and the complete graph Laplacian spectrum**, not merely an isolated example. The sharp, all-length connectivity and multiplicity theorem gives an explicit spectral benchmark for a highly symmetric but noncomplete coding polytope graph. The normalized connectivity \(9/[2(n+1)]\) and the exceptional complete-graph case at length three expose structural information beyond known facet representations.

## Limits
The proof concerns the unweighted graph of the all-ones ternary check; no other checks, characteristic, or edge-length-weighted Laplacians are covered. The cited 2015 conference version was compared at abstract level, not inspected in full. A bibliographically unindexed equivalent could exist. All computational checks are finite and do not independently certify the all-length proof.

Self-review: passed. Independent audit: not yet performed.

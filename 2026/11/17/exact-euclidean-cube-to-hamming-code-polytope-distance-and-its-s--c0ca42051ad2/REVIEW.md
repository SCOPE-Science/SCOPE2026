# Scientific review

## Correctness: PASS
The unique projection is exhibited as an explicit convex combination of zero and all weight-three codewords through one coordinate. The weight-three minimum-distance property gives a global exposing inequality with the exact equality face; the Euclidean projection condition and strict convexity prove optimality and uniqueness. Codeword reflection supplies every noncode vertex. A residual-variance identity rules out every nonvertex cube point, and the distance follows exactly. The arbitrary-dimension argument does not depend on finite computation. Scope: unweighted Euclidean metric, binary Hamming check columns, \(m\ge2\).

## Originality: PASS, priority provisional
Kashyap (2006) covers general codeword-polytopes, face symmetries and minimal-codeword connections but not the exact Hamming cube-to-hull distance, exposed nearest-point simplices or full deep-hole classification in its inspected sections. Gensheimer et al. (arXiv:1901.03240, 2019) analyze single parity-check-polytope projection, not projection onto the simultaneous Hamming codeword hull. Coregliano–Jeronimo–Jones (arXiv:2112.09221, 2021) treat LP code-size bounds and associated hierarchies. An equivalent formulation as a Talagrand-style convex distance at binary inputs was searched for explicitly. No stronger encompassing theorem or published exact Hamming-code table was identified in the inspected material and focused published-finding corpus/literature searches, but absence of search matches is not an exhaustive priority certificate. The exact claim remains subject to historical specialist review.

## Mathematical value: PASS
The full Hamming-code family is an infinite, canonical class of high-dimensional binary polytopes. Its exact geometric covering error and complete deep-hole classification relate discrete perfect decoding radius one to convex relaxation radius \(2/\sqrt{n+3}\), an asymptotically vanishing factor. The explicit relatively open simplex faces of dimension \((n-1)/2\) provide structural information about nearest-point geometry, not merely a numerical evaluation.

## Evidence, closest literature and limits
Exact/rational symbolic checks passed for all codewords in lengths 3, 7 and 15, with further sampled conditions in lengths 31, 63 and 127. A separately implemented quadratic-program solve matched lengths 3 and 7. Neither finite test is substituted for the analytical proof. Priority risks include alternative formulations through convex distance, codeword-polytope projections, or coding-theoretic pseudoweight terminology. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.

# Independent mathematical audit

## correctness

PASS

The statistic uses unordered neighboring values of the same permutation, with H on fixed labels. After fixing distinct images a,b at positions i,i+1, the partial injection consists of directed paths and forced closed cycles. Completing the paths uniformly leaves expected cycle count H_{n-2} plus the number of forced cycles (the two possible loops and the possible two-cycle). Summing over oriented realizations of the graph edges adds d_i+d_{i+1}+1_{{i,i+1} in E(H)} at each i. The sum of the degree terms is 4e-d_1-d_n, and subtracting E[K]E[B_H] gives (c+2e/n-d_1-d_n)/[n(n-1)]. The complements, path and relabeled stars follow from the stated edge and endpoint counts. At n=2 the only adjacency is constant and the empty completion has zero cycles.

## originality

FAIL

Féray's exact joint-moment lemma for arbitrary partial permutations under Ewens weighting gives the two-image law at general theta, including loops and forced two-cycles. The uniform cycle covariance is the derivative of the corresponding expectation at theta=1. Summing that prior formula over the graph's ordered edge realizations and taking this derivative gives the audited formula and all sign cases. This is verified coverage by implication; it does not claim Féray explicitly stated the endpoint-degree formula.

## value

FAIL

The endpoint-degree expression is concise and the labeled-star sign reversal illustrates a meaningful difference between graph isomorphism and equality of the joint statistics. Nevertheless the exact invariant is mechanically obtained from the known arbitrary two-image Ewens moments by differentiation and summation; the examples require only substituting graph degrees. It is informative as an application of that prior formula, but does not meet the value standard for an independently unknown exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.

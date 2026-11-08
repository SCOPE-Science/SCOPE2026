# Scientific review: directed reachability on \(K_{2,n}\)

## Correctness: PASS
The four mutually exclusive two-edge orientation types have probabilities \(p(1-p),p(1-p),p^2,(1-p)^2\). Reachability of the second hub is equivalent to occurrence of the first type; this proves the joint PGF. A conditional comparison on the no-type-I event gives an exact signed difference of two binomial laws. Sign threshold, total variation, and sharp exponential rate follow from the explicit coefficients and binomial large-deviation concentration. Mean and covariance follow by differentiation. The independent graph-enumeration checker passed 710 exact assertions for 30 parameter instances. The infinite theorem does not depend on the finite enumeration.

## Originality: PASS (subject to historical priority risk)
F. Bienvenu (2017 preprint, 2019 article) proves general positive association but no explicit distribution for \(K_{2,n}\), and E. Aas (2011) studies a different consecutive-path correlation under a regime in which both part sizes grow. The signed binomial correction, exact one-crossing threshold, total-variation identity and magnitude, and variance surplus are not stated or implied by either inspected theorem without a further family-specific computation. Targeted searches for oriented \(K_{2,n}\) out-component laws and polynomial aliases found no dominating evaluated result. A general directed-cluster counting identity elsewhere could conceivably produce the finite polynomial, and unindexed earlier evaluations remain a risk.

## Value: PASS
The two-hub bipartite family is the first cyclic layer beyond oriented trees and a natural test case for correlation and cluster-size behavior. The result provides the complete finite law for every bias, a signed local comparison and sharp approximation constant/rate, rather than just expectation or qualitative association. The exact variance inflation at fair bias shows how rare, correlated global reachability failures can increase dispersion despite stochastic domination by an independent-vertex benchmark. The precision may serve as a check for oriented-percolation approximation methods on other sparse-core graph families.

## Scope and limitations
The main conclusions apply to independently oriented \(K_{2,n}\), not all graphs. The sharp asymptotic fixes \(0<p<1\) or restricts it to a compact interior interval. Priorities for unindexed older computations are not certified; no independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.

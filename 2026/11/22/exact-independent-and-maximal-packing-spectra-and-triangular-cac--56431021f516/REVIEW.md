# Review of exact packing spectra and optimum exchange for path blob graphs

## Correctness: PASS
The domain is all nonempty intervals of a path with overlapping/adjacent intervals incompatible. Each compatible family maps bijectively to an even-sized subset of \(n+1\) boundaries. This gives every independent-set coefficient and its exact negative simple roots. For maximality, every omitted path vertex must touch a selected interval: equivalently both endpoint gaps are at most one and each internal vacant gap at most two. Enumerating these forced gap types yields the displayed bivariate rational function, with all boundary cases included. For optimal exchange at even order exactly one unit of slack remains; omission of one of \(n+1\) endpoint labels gives the entire exact triangle-chain adjacency relation. A separate graph-based exhaustive enumerator agrees through order twelve; extrapolation is not used as proof.

## Originality: PASS (historical priority qualified)
The open full text of Bonnet et al., arXiv:2602.18317v1 (2026-02-20), Section 4, defines the blob graph and proves optimization reductions and induced-minor transfer, not all-size counts, independence roots, maximal-set profiles, or exchange graphs for path bases. The open full text of Martin et al. (Algorithmica, 2023), Sections 2 and 3, also uses blob graphs algorithmically without the present all-cardinality and optimum-exchange classification. The total number of inclusion-maximal packings at consecutive orders follows the **known** OEIS A000213 tribonacci sequence; that univariate integer sequence is credited and is not a novelty claim. Searches for path blob, connected-interval-packing and optimum-reconfiguration variants found no prior result that implies the joint theorem. A published result on rank-three first-order theories of complete discrete-interval intersection graphs and a published exchange theorem for powers of cycles concern different invariants or graph families; neither implies the present formulas. Unindexed historical interval-scheduling literature remains a material priority risk.

## Value: PASS
The blob-graph transformation is a current graph-algorithmic tool for induced connected packing, and path bases are its most natural test family. The theorem supplies simultaneous exact all-cardinality counting of feasible and maximal packings, complete root location, and a nontrivial *exact optimum exchange graph* that changes from one state at odd orders to a connected chain of triangles of unbounded diameter at even orders. These combine a natural counting problem with the mobility structure of optimal solutions, which cannot be read from the univariate tribonacci count alone. The restriction to path bases and the absence of an independent external review are explicit.

## Sources and remaining limits
- Bonnet et al., arXiv:2602.18317v1, full text Section 4, https://arxiv.org/html/2602.18317v1.
- Martin, Paulusma, Smith, van Leeuwen, Algorithmica 85 (2023), full-text Sections 2 and 3, https://doi.org/10.1007/s00453-023-01109-z.
- OEIS A000213, https://oeis.org/A000213, exact univariate total sequence only.
- Exact standalone Python verification of orders \(1\) through \(12\): 8190 independent packings enumerated and every coefficient, maximality property, optimum and exchange edge set compared.

Self-review: passed. Independent audit: not yet performed.

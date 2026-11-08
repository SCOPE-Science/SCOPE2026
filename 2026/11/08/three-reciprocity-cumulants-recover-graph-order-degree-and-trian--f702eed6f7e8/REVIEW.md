# Scientific review

## Correctness (C): PASS

The event of reciprocal selection on an edge has probability \(d^{-2}\); two events sharing a vertex are incompatible, while events on disjoint edges are independent. This establishes the matching-based generating function. Independent triples in the regular line graph have the explicit inclusion-exclusion count shown in the proof; its triangles are exactly vertex-centered edge triples plus graph triangles. The first three factorial moments yield the asserted ordinary cumulants. Positive degree makes the variance-to-mean ratio invertible, and the triangle-incidence bound proves the complete degree-dependent sign classification. The exact-rational checker independently compares complete outcome enumeration with matching coefficients for 16 hosts (301 assertions). Risk: the checks cover only finite examples, but the all-parameter argument is algebraic and combinatorial.

## Originality (O): PASS, with explicit priority uncertainty

The closest mathematical coverage is the matching partition function in Davies–Jenssen–Perkins (arXiv:2004.06695), whose third-order cluster terms already involve triangles. This is a powerful pre-existing source of the **combinatorial ingredients** but it does not state the one-neighbor reciprocity model, its exact third cumulant, inverse recovery from three population cumulants, or the sign classification. Leckey–Wormald (arXiv:1803.02667) study orbit lengths in a different constrained random mapping model; Wang–Resnick (arXiv:2103.07424) study reciprocal links in preferential attachment, a different sampling mechanism. Exact search phrases covered independent neighbor choices, reciprocal pairs, three cumulants, matching polynomials, and triangle recovery. A historically earlier formulation may exist under random mapping or cluster expansion terminology; novelty here is a model-level inverse theorem, not a new matching identity.

## Value (V): PASS

Reciprocity is an interpretable network statistic of a natural independent-choice directed graph. The first two cumulants deliberately cannot distinguish regular hosts with the same order and degree, but the third extracts precisely their triangle total. As an explicit boundary, \(K_{3,3}\) and the triangular prism have identical mean and variance but different third cumulants. Complete sign information identifies the role of short cycles in fluctuations, beyond the existing mean/variance benchmark. This is a natural inverse identification law rather than a numerical curiosity or arbitrary parameter slice.

## Closest sources and limitations

- Leckey and Wormald, arXiv:1803.02667, 2018: functional graph model with prescribed indegrees, not this local neighbor-choice law.
- Davies, Jenssen and Perkins, arXiv:2004.06695, 2020: low-order matching coefficients and triangle contributions; closest mathematical mechanism and main residual priority risk.
- Wang and Resnick, arXiv:2103.07424, 2021: global and pairwise reciprocity in growing directed networks, not a fixed regular host.

Sampling independence and regularity are essential. No statistical estimation guarantee or graph-isomorphism reconstruction is claimed. The reported novelty remains provisional until independent mathematical and historical review.

Self-review: passed. Independent audit: not yet performed.

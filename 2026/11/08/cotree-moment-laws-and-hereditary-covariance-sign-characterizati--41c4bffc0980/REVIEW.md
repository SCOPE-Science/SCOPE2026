# Scientific review: cotree moment laws and hereditary covariance signs

## Correctness — PASS

The proof identifies graph disjoint unions with Cartesian products of stable-set polytopes and graph joins with convex free sums. Radial cone-volume integration proves the exact factorial volume and rising-factorial moment recursions for all nonnegative multiindices. The normalized mixed-second-moment ratio transforms by an explicit positive factor at joins; induction gives the uniform sharp edge bound and exact nonedge sign partition. Direct rational integration on the induced four-vertex path establishes its negative endpoint covariance, so the hereditary converse follows from the cograph forbidden-path characterization. All quantifiers, coordinate normalization, and base cases are explicit. The checker independently integrates full-dimensional simplices for 564 finite cographs, evaluates 1,120 cubic-moment cases, and rechecks the path obstruction. Finite evidence supports rather than replaces the proof.

## Originality — PASS (historical priority provisional)

The closest primary graph source is Singh's *Cographs and 1-sums*, arXiv:2210.04139, establishing the join/zero-sum and induced-path framework. Aliniaeifard et al., *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, treat the same indicator polytopes but their inspected theorems concern edges, facets and diameter, not uniform-volume correlations. Kohn–Shapiro–Sturmfels, *Moment Varieties of Measures on Polytopes*, arXiv:1807.10258, establish general simplex-moment machinery but no closed cotree moment recursion or hereditary sign boundary. An earlier complete-multipartite moment law is a restricted special case, not broader coverage. Equivalence and implication comparisons under the aliases cograph/P4-free, graph join/0-sum, free sum, independence polytope, and uniform-volume moments found no dominating result. Targeted search cannot establish historical priority conclusively; generic integration and an unlocated alternate formulation remain risks.

## Mathematical value — PASS

The theorem gives an all-degree exact integration method, a sharp edge covariance inequality, full reconstruction of adjacency and connected components from uniform interior covariance, and a clean forbidden-induced-subgraph converse. The P4 obstruction provides a substantive mathematical boundary rather than a numerical anecdote. Arbitrarily nested union/join constructions go beyond the earlier special families. There is no claim for uniform random stable sets or noncanonical affine coordinates.

## Limits and reproducibility

The exact formula applies to finite simple cographs in their standard indicator realization. The hereditary characterization quantifies over every nonempty induced subgraph. A standalone checker uses stable-set vertex enumeration and independent exact-rational simplex integrations, with 564 finite configurations and 1,120 cubic-moment tests, without certifying all dimensions. Independent mathematical assessment and full historical-priority review have not occurred.

Self-review: passed. Independent audit: not yet performed.

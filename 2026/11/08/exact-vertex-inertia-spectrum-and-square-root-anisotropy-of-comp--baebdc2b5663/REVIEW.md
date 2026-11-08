# Self-review

## Correctness — PASS

The claim concerns uniform sampling from all binary matching-incidence vertices of the full-dimensional matching polytope of the complete graph on at least four vertices. Counting one edge and two disjoint edges gives the exact covariance entries. The well-specified orthogonal decomposition of edge space into constants, centered vertex stars and unsigned-incidence kernel yields the three eigenvalues and their multiplicities. The strict inequalities are proved using the two-step telephone recurrence, not inferred from sampled dimensions. The coefficient in the square-root condition-number asymptotic is supported by a quantitative two-step-ratio estimate with its derivative and error bounds explicitly shown. The checker independently enumerates every matching through nine vertices and uses exact rational arithmetic.

## Originality — PASS, with provisional historical priority

Abreu–Costa–Nascimento–Patuzzi (2019, DOI 10.5540/tema.2019.020.01.189) analyze degrees and regularity of the matching polytope's one-skeleton; the inspected eight-page primary full text does not state vertex-uniform second moments or a covariance spectrum. Torres (arXiv:2306.11910, 2023) treats normality of fixed-cardinality bipartite matching polytopes, rather than the all-cardinality complete-graph vertex distribution. Ferrarini–Gualandi (arXiv:2105.09827, 2021) discuss total matchings and facet systems, a different object. Quitmann (arXiv:2309.13632, 2023) proves spatial decay of monomer–dimer correlations for lattice domains, a different setting despite use of dimer–dimer covariance. Published nearby findings concern complete-graph matching-polytope radii and fractional matching-polytope John ellipsoids; their accessible summaries do not imply vertex-uniform covariance formulas, and the corresponding full repository pages were inaccessible. The line-graph/Johnson spectral decomposition is classical; novelty is not attributed to that representation alone but to the explicit all-size covariance classification, strict mode ordering and sharp conditioning. A different formulation under monomer–dimer susceptibility, random involutions or association schemes could predate the result; an expert literature audit is warranted.

## Mathematical value — PASS

The covariance ellipsoid is a natural intrinsic second-moment invariant of a full-dimensional family of 0–1 polytopes. Exact identification of every eigenvalue and eigenspace answers a geometric question not answered by ordinary facet, volume or graph-skeleton data. The nontrivial inequality making the size mode uniquely least variable is all-dimensional, and the precise growth of its condition number as \(2\sqrt n+O(1)\) distinguishes the three fluctuation scales (size, star contrasts and cycle contrasts). This is an exact infinite-family classification, not an arbitrary finite slice or a table lookup.

## Limits and residual risks

No conclusions are made for arbitrary graphs, volume-uniform points, weighted models or fixed-size matching slices. Primary-source inspection covers the cited matching-polytope paper and directly relevant HTML text; the full text of the nearest published-finding corpus geometric findings could not be retrieved. Classical monomer–dimer correlations or association-scheme treatments might contain an equivalent theorem. The finite checker alone is not evidence for infinite-dimensional statements.

Self-review: passed. Independent audit: not yet performed.

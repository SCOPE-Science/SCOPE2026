# Self-review

## Correctness — PASS

For binary block occupancy \(k\), Euclidean projection onto the quota hypersimplex has squared error \(F(k)\) as stated in `RESULT.md`. The two analytic pieces join with zero first derivative at the quota and both have positive second derivative. Therefore fixed-total occupancy maximizers are precisely the packed profiles prescribed by Euclidean division. The strict variance inequality for projection residuals forces a nonvertex deepest point to be a mixture of maximizing vertices with the same residual; the residual is insensitive to the selected coordinates of the sole partial block precisely when its occupancy equals its quota. The full formulas and contact-face classification follow. The embedded standard-library checker independently verifies 75 parameter triples and many projection witnesses, but these computations do not establish the infinite theorem.

## Originality — PASS, with residual priority risk

The closest primary source is Schröter (2017, arXiv:1707.02814), which *defines precisely* partition-matroid products of hypersimplices (Example 16) and locates them as common cells of hypersimplex subdivisions (Proposition 22). The exact Euclidean Hausdorff separation from the ambient hypersimplex is not one of its results. Lasoń–Michałek (2020, arXiv:2005.08359) supplies a direct-sum product rule and classifies Gorenstein/smooth matroids, not Euclidean projections. Torres (2024, arXiv:2407.13125) addresses general Hausdorff distance and best zonotope approximation; its generic vertex reduction is credited, but the present family has different geometry and an explicit arithmetic equality locus. Related published indexed hypersimplex facial-distance work measures another separation. Neither the matched rank-two graphical edge-polytope classification nor the generic results implies arbitrary higher-rank equal-quota partitions. All searches and implication comparisons are recorded in `AUDIT.json`. Historical-priority certainty is not claimed.

## Mathematical value — PASS

The object is a canonical partition-matroid base polytope embedded in the uniform-matroid hypersimplex. The invariant measures maximal Euclidean loss when balanced quota constraints are imposed, a basic natural geometric comparison in a family already central to matroid subdivision theory. In addition to the universal exact radius, the theorem determines **every** maximizing point and reveals an arithmetic transition: isolated worst-case binary vertices become full positive-dimensional coordinate faces exactly when \(q\mid(r-1)c\). The phenomenon persists for infinitely many independent ranks, capacities and block counts. Its equality classification is mathematically informative beyond numerical evaluation of the distance.

The statement applies only to balanced blocks and the standard coordinate Euclidean metric. Priorities may change with examination of additional historical sources; no external review or independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.

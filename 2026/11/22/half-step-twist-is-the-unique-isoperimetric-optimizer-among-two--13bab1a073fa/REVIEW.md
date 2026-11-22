# Self-review — Half-step prismatoid isoperimetry

## Correctness: PASS
For every integer \(n\ge3\), the surface-area and volume formulas follow from the actual lateral triangular facets and mixed-area integration. The one-variable height objective diverges at both ends and has one stationary point, a global minimum; after substituting that optimum, the derivative with respect to increasing twist has the strictly negative sign bounded by \(-3c^2\). This proves the sharp constant and equality cases, including twist endpoints. The independent convex-hull implementation passed 5,582 finite checks; the continuum-wide proof is analytic, not computational.

## Originality: PASS (provisional priority)
The nearest same-object published calculation, [*Exact John–Löwner ellipsoid profile of twisted regular polygonal prismatoids*](https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-john-l-wner-ellipsoid-profile-of-twisted-regular-polygonal--4eb565e76a67), contains the **volume** term already used here, but its claim and complete proof concern extremal ellipsoid volumes, not lateral surface area or a globally optimized isoperimetric quotient. The full results [*Uniform antiprisms uniquely minimize mean planar-silhouette complexity*](https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-uniform-antiprisms-uniquely-minimize-mean-planar-silhouette-comp--b44d8c773553) and [*Equidihedral minimax and volume–angle separation*](https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-equidihedral-minimax-and-volume-angle-separation-in-regular-anti--12f724b4a957) optimize different objectives; their height solutions do not imply the new one. Abrosimov–Vuong arXiv:2110.12265v1 treats spherical antiprism volume, not the Euclidean question. Horváth–Lángi arXiv:1302.6164 treats convex-hull volume under translations/reflections, not surface minimization. Searches for isoperimetric aliases, exact parameters, and broader convex-hull theorems did not identify a dominating result, although absence of search hits does not prove priority. An unindexed Euclidean antiprism treatment and incomplete access to the full 2013 source remain explicit risks.

## Mathematical value: PASS
This is a complete sharp optimization over radius, height, and twist within a canonical family, not a parameter substitution. The strict difference between the optimum and the edge-uniform realization for every \(n\ge4\), plus the optimal-cylinder limit, provide structural geometric information beyond the known polygonal prismatoid volume formula.

## Limitations
Two congruent coaxial regular planar polygonal rings only; no claim for offset, unequal or irregular bases or arbitrary polyhedra. The finite checker is not a formal or infinite-range proof. Independent validation and exhaustive historical priority are not claimed.

Self-review: passed. Independent audit: not yet performed.

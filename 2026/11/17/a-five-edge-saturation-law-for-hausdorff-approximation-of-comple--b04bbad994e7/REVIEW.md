# Self-review

## Correctness — PASS

The claim is in the inherited Euclidean metric on the zero-sum subspace, with the common normalization \(\|e_i-e_j\|^2=2\). The path roots give an injective basis matrix, identifying the path polytope with an \(\ell_1\)-unit ball in coefficient coordinates. Every exact projection is accompanied by a rational feasible point and all necessary and sufficient subgradient inequalities, not just a numerical objective value. The longest-root certificates establish the lower bounds; constructive bounds for every other omitted root prove the global Hausdorff maximum. A convexity/equality argument proves farthest-point uniqueness in the *whole* polytope. For the second vertex level, the potentially tied separation-four cases are excluded using a strict subgradient violation. The attached exact-arithmetic checker tests 10,659 root pairs through order 40 and the 38 independently optimized instances agree within \(3\times10^{-14}\). Finite computation is corroboration, not an infinite proof.

## Originality — PASS, with historical-priority risk

The complete-graph and path symmetric edge polytopes are standard objects, not a new construction. The primary 2019 treatment *Many faces of symmetric edge polytopes* gives the graph-root and finite-metric framework but does not determine Euclidean projection distances between these two bodies. The inspected 2021 facet-subgraph and 2022 gamma-vector papers address different invariants. The closest previously indexed path inball result gives the inradius, circumradius, and incenter family *of the path body itself*, which cannot imply the Hausdorff separation from the complete-root body or the three long-root shells. Indexed results about crown-graph Hausdorff losses involve a different polytope and deletion pattern. Searches included root-polytope aliases, path simple-root coordinates, crosspolytope projections, Hausdorff and nearest-point terminology. No statement with equivalent hypotheses or stronger implication was identified in examined sources. Historical priority remains provisional: a projection-theoretic formulation in the broader literature might not be indexed using these names.

## Mathematical value — PASS

This is an exact, natural geometric comparison between the symmetric edge polytopes of a complete graph and a spanning path, with an initially surprising saturation phenomenon: removing an increasing fraction of root directions nevertheless gives a constant limiting Hausdorff loss. The exact localization shells distinguish internal and boundary roots and yield a complete sharp second-distance vertex level, not just an approximate asymptotic. The structural answer pertains to an infinite family and provides explicit nearest-point certificates. The underlying path inradius calculation is separate, and the result is neither a renaming of a known formula nor merely a finite table.

## Closest literature and limits

D'Alì–Delucchi–Michałek (arXiv:1910.05193), Chen–Davis–Korchevskaia (arXiv:2107.12315), D'Alì–Juhnke-Kubitzke–Köhne–Venturello (arXiv:2201.09835), and the publicly accessible path-inball note were checked for stated implications. No claim extends to weighted trees or to the second-largest distance among all convex-body points. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.

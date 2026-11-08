# Research assessment: weighted-path Gauss positivity

## Correctness — PASS

The domain is every finite positively weighted path of order at least two and every nonnegative step. The proof reconstructs the rational stability map from two-stage fourth-order Gauss--Legendre, obtains its precise large-step expansion, and derives a necessary sign condition on the Moore--Penrose group inverse. The resistance-centering identity yields exact adjacent inequalities. Their three-coordinate irreducible Perron reduction excludes every order at least five, and its equality case fixes the unique four-node conductance ray. The two small cases are explicitly evaluated by exact rational formulas with positive denominators and numerators on the claimed weight ranges; strict positive diagonal entries follow from spectral positivity. The packaged exact symbolic checker replayed successfully. Risks: the theorem is specific to completed steps and the given rational map, and finite checks alone could not prove the all-order statement.

## Originality — PASS on examined sources, with a publication-priority reservation

The closest previous coverage is the weighted-path group-inverse M-matrix literature (Chen--Kirkland--Neumann 1995; Kirkland--Neumann--Shader 1997; Kirkland--Neumann 1998), which addresses the sign obstruction that forms a *necessary* step here, including a four-node example. That necessary classification is not asserted to be new. Lóczi--Ketcheson 2013 studies numerical positivity and absolute-monotonicity radii for rational functions, without supplying a complete all-step parameter classification on these weighted path Laplacians. The claim newly assessed is the *if-and-only-if unconditional nonnegativity of the [2/2] Gauss end-step*, including sufficiency certificates and strict positivity. The previously recorded complete-multipartite scalar-filter theorem already covers the unweighted two-vertex and equal-weight three-vertex subcases and a negative unweighted four-vertex example; these are not separately claimed new. The new classification includes arbitrary positive path conductances, the sharp three-node weight interval, the exceptional four-node ray, and the all-weight exclusion for longer paths. Related cycle and Cartesian-product statements concern different graph families. The full text of the 1995 and 1998 matrix-theory sources was not available for a decisive passage-by-passage check; available abstracts and the detailed 1997 full text indicate that their target is group-inverse structure, not this specific Runge--Kutta map. This is the material residual novelty risk, not a claimed proof of literature uniqueness.

## Value — PASS

A-stable high-order numerical integration need not preserve the positive cone. The exact safe region in the natural space of path conductances is an unexpectedly small, sharply classified set: all two-node paths, a closed parameter interval for three nodes, and one ray at four nodes, with a universal all-weight impossibility from five nodes onward. This has a direct mathematical purpose for graph-heat discretizations and provides a reusable combination of Green-function asymptotics, a Perron obstruction, and finite rational positivity certificates, rather than a computed isolated example.

## Scientific limitations

The result concerns the finished matrix step and symmetric, positive, nearest-neighbor path conductances; no general graph, directed generator or stagewise-positivity theorem is claimed. Some close group-inverse papers were only abstract-accessible; publication priority must be checked by additional specialist reading. Code replay is self-review, not independent audit.

Self-review: passed. Independent audit: not yet performed.

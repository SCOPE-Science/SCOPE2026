# Review of the fractional-cap enclosing-sphere theorem

## Correctness — PASS

The theorem quantifies over every integer \(n\ge3\) and every real \(0<\tau\le n\), including integral caps, the full cube, and the exact mixed-contact boundaries. The proof reconstructs all vertices of the one-hyperplane-truncated cube and shows uniqueness of the minimum-ball center by strict convexity of the max-squared-distance function. Permutation symmetry reduces the optimizer to a diagonal center, whose allowed interval is proved rather than assumed. Two exact quadratic vertex-distance profiles give the median center, radius, and all contacts. The strict-convexity argument excludes nonvertex contacts.

The middle regime has the exact threshold conditions \(s\ge2q/n\) and \(s\le2q/(n-2)\) whenever relevant; the complete general statement uses a median formula so no separate special-case assumptions are required. The exact rational verifier checked 401 parameter cases and 45,451 assertions, including boundary values, and a separate nonsymmetric numerical epigraph optimization agreed in five cases. Neither finite test is presented as an unrestricted proof.

## Originality — PASS (historical priority provisional)

Black–Steiner's fully inspected optimization manuscript investigates combinatorial paths and graph diameters in fractional knapsack polytopes. Gunluk's open 37-page truncated-hypercube manuscript (introduction and main theorems inspected) treats deterministic volume estimation. Neither supplies minimum Euclidean enclosing-sphere radii or contacts. The nearest same-body published record, *Three-phase John ellipsoid of a capped hypercube*, computes a maximal **inscribed-volume** ellipsoid, whereas the present result computes the minimal **enclosing-radius** ball. The nearest published outer-sphere result, *Sharp minimum-sphere bounds for matroid independence polytopes*, covers only the integral rank \(\tau=q\) for this family, with Boolean vertices; its projection identity cannot be applied to fractional cut vertices. The example \(n=5,\tau=8/5\) rigorously distinguishes the two claims.

Searches under truncated cube, fractional hypersimplex, fractional uniform matroid, minimum ball, circumradius, Chebyshev center, contact shell, and dual/enclosing-ellipsoid terminology did not reveal a covering exact theorem. The existing exact uniform-matroid Santaló and rank-convexification computations concern other invariants. Absence from the searched literature is not a proof of global novelty; unindexed equivalent formulations are a residual risk.

## Mathematical value — PASS

A uniformly capped cube is the canonical symmetric representative of the one-linear-cut knapsack bodies featured in current polyhedral work. The calculation does more than supply one radius: it classifies the center and **every equality vertex for the complete real-cap family**. Its nontrivial feature is the persistent radius plateau followed by a mixed-contact interval and a complete contact-orbit exchange, not a change of notation or a fixed-parameter check. The fractional phase invalidates naive extension of the Boolean-vertex projection identity. These sharp metric boundaries provide natural geometry to compare with volume estimates, truncated-cube combinatorics, and ellipsoid geometry; no speculative downstream theorem is asserted.

## Limitations

The asserted novelty concerns this exact symmetric family; it does not settle general unequal knapsack weights or multi-cut bodies. Results are in the inherited standard Euclidean metric. The broader historical literature may contain an equivalent calculation not indexed under the searched terms; independent priority and mathematical audit have not been performed.

Self-review: passed. Independent audit: not yet performed.

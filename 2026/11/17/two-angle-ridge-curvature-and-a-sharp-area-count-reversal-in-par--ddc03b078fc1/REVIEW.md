# Self-review

## Correctness
PASS. The explicit parity halfspace description supplies exactly \(2n\) coordinate and \(2^{n-1}\) simplex facets. Intersections of distinct facets exhaust two ridge orbits for \(n\ge5\): coordinate–coordinate, with \(2n(n-1)\) ridges of \((n-2)\)-volume \(W_{n-2}\) and right exterior angle; and coordinate–simplex, with \(n2^{n-1}\) ridges of \((n-2)\)-volume \(\sqrt{n-1}/(n-2)!\) and exterior angle \(\arccos(1/\sqrt n)\). Distinct simplex facets share at most an edge. Applying the normalized polyhedral Steiner formula gives the exact claimed intrinsic volume and area ratio. The monotonicity proof uses the positive difference \(D_{n+1}-2D_n=(n-3)(n-2)!\); the exception at \(n=4\) is stated separately. Exhaustive finite-dimensional Euclidean convex-hull checks for dimensions four through seven independently confirm the formulas, but do not replace the proof.

## Originality
PASS under available evidence, with residual historical-priority risk. Manecke–Sanyal–So (arXiv:1812.07491), inspected in full, provide facet classification and combinatorial triangulation counts, not the Euclidean ridge measures or the second Steiner coefficient. The closest separately indexed parity-halfcube finding concerns uniform-volume covariance and an isotropic constant, neither of which gives ridge angles. Separate ridge-angle results on other polytope families have noninterchangeable facet incidence geometry. Targeted searches for 'halfcube', 'demihypercube', 'parity polytope', 'Steiner', and angle/area aliases located no established implication covering the full result. The inaccessible full text of a recent same-object covariance item and classical polytope tables remain residual risks; absence of a search hit is not proof of uniqueness.

## Mathematical value
PASS. The theorem determines a complete canonical Euclidean curvature invariant for a classical infinite polytope family, not a selected unmotivated instance. It exposes a sharp geometric dimension threshold between \(n=5\) and \(n=6\): the class with exponentially more ridges loses total intrinsic ridge-area dominance and becomes asymptotically negligible. That structural distinction could not be inferred from a face vector or total volume and is intrinsic to Euclidean boundary geometry.

## Limitations and scope
The standard unit-cube Euclidean realization is essential. The exact full ridge classification assumes \(n\ge5\); the \(n=4\) exception is explicit. Finite checks cover \(4\le n\le7\), while the all-dimensional proof is analytic and combinatorial. Historical priority is provisional and independent auditing has not occurred.

Self-review: passed. Independent audit: not yet performed.

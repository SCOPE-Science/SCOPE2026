# Self-review

## Correctness — PASS

The precise nodes, normal orientation, every triangle area, and the Steiner-centered representative are reconstructed explicitly. The displayed halfspaces all have common offset \(b_n/\sqrt3\), which proves the inscribed ball; their zero-sum spanning normals prove global optimality and center uniqueness. The poles prove the enclosing sphere and its uniqueness for \(n\ge4\). The exact support-function representation of Hausdorff distance, the strict inequality \(b_n>3-\sqrt3\), and the monotone function \(x\cot x\) establish the distance and strict monotonicity for all integers in the claim. The two-pyramid volume formula is exact. The verifier independently rebuilt hulls and moment data in finite dimensions, passing 16,023 assertions. The proof, rather than its finite tests, handles every \(n\ge4\). No infinite-performance or independent-computation claim is made.

## Originality — PASS, with residual historical priority risk

Two components are specifically prior: Bajnok's aligned latitude-ring spherical \(3\)-design construction (Construction 3.3) and An's unique equal-area Minkowski polytope construction plus its asymptotic estimate as spherical design **strength** grows. Neither cited publication establishes the exact regular-bipyramid inradius, circumsphere, fixed-strength Hausdorff distance sequence and the opposed Hausdorff/volume monotonicities. The closest found mathematical records on six-node spherical \(2\)-design polyhedron volume and planar normal-weighted Minkowski polygons concern different configurations. Named searches included exact metric/volume formulas, bipyramid aliases, design-cardinality and design-strength equivalences; no source implying the complete claim was found. This is a bounded-priority assessment, not certification that no precedent exists; an unindexed calculation under another name remains possible.

## Mathematical value — PASS

This is a natural fixed-strength boundary case for recently studied geometric sphericity of equal-area Minkowski realizations of spherical designs. It establishes the unexpected strict worsening of Hausdorff sphericity despite increasing equal-area facet count and increasing volume, supplies exact limiting nonround shape, and clarifies why node count cannot replace design strength in geometric estimates. The object and limit are mathematically motivated rather than an arbitrary isolated numerical slice. The claim is a focused exact classification, not a general optimality theorem among all spherical designs.

## Reproducibility and limitations

The standalone `verify.py` requires NumPy and SciPy. It independently checks the convex hull and all degree-three design moments through dimension-index parameter \(n=40\), plus monotonicity through \(n=300\). The mathematical proof covers all integers \(n\ge4\). The construction of the design is old; only the specified metric/volume and monotonicity classification is proposed as new. The external literature assessment remains provisional and no independent scientific audit has occurred.

Self-review: passed. Independent audit: not yet performed.

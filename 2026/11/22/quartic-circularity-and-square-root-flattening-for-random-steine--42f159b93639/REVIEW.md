# Scientific review

## Correctness — PASS

The claimed eccentricity is the Euclidean eccentricity of the maximum-area Steiner inellipse, not the triangle's incircle or circumcircle. The affine equilateral-triangle parametrization shows that its squared semiaxes are proportional to the eigenvalues of the centered vertex second-moment matrix. The exact chord formula and both local expansions are explicitly derived in `RESULT.md`. At the near-circular endpoint there are exactly two isolated labelled equilateral configurations after quotienting by global rotation; their local quadratic-form sublevel area yields the quartic coefficient. At the flat endpoint a global shortest-chord inequality first localizes *all* exceptional triangles to pair collisions; the uniform local gap derivative and an independent triple-collision bound give the linear axis-ratio coefficient. The eccentricity conversion is exact. The marked total-variation claims follow from convergence of constant-density parameter domains with negligible singular overlap. The included checker independently compares 1000 covariance eigenvalue evaluations with the chord identity and examines numerical endpoint convergence.

Limit: the numerical comparisons are diagnostics only; the infinite assertions follow from the written geometric estimates and dominated localization, not a finite mesh.

## Originality — PASS, with historical-priority risk

Minda–Phelps (2008) and Rohe (2015) derive the known Steiner inellipse and its foci, including its equilateral circle case. Their inspected geometric constructions do not state the random-circle probability endpoint laws or marked rare-shape limits. MathWorld's circle-triangle picking entry treats triangle area rather than the axes of the maximal-area ellipse. Nearby mathematical research records cover random cyclic triangle inradii, near-maximal triangle areas and ellipse-sampled triangle angles, but no retrieved statement supplied either sharp Steiner-inellipse endpoint coefficient or both conditional laws. A result about random points in a disk (rather than on its boundary) is not a theorem for this sampling model. The 2010 Scimemi paper is plausible related deterministic literature; its full text could not be obtained, so this assessment is provisional rather than a historical priority certificate.

## Mathematical value — PASS

The Steiner inellipse is the unique canonical maximum-area ellipse of a triangle; its eccentricity is an intrinsic Euclidean measure of how isotropic that optimal convex figure is. For circle-inscribed random triangles, the two natural extreme shapes are controlled by different geometric singular sets: isolated equilateral configurations and codimension-one pair collisions. Their exact exponents, constants and marked limits distinguish two fundamentally different sources of rare optimal-inellipse shapes. The collision constant being independent of the third vertex's position is a structural feature, rather than a numerical table entry or an arbitrary parameter slice.

## Sources and residual limitations

Primary geometry: D. Minda and S. Phelps (2008), DOI: 10.1080/00029890.2008.11920581; K. Rohe, arXiv:1502.01367 (2015). Relevant but only indexed/abstract-inspected: B. Scimemi, Forum Geometricorum 10 (2010), 55–77. Comparison measures: Wolfram MathWorld, *Circle Triangle Picking*; D. G. Kendall, *Exact distributions for shapes of random triangles in convex sets* (interior-point law). Full historical exhaustiveness and independent validation remain outside this review.

Self-review: passed. Independent audit: not yet performed.

# Self-review: even-cycle outer ellipsoids

## Correctness — PASS
The affine dimension is \(2m-2\), because the unsigned cyclic incidence operator has only one zero Fourier frequency for even order; centering deletes the constant mode. The covariance eigenvalues are exactly \(4\cos^2(\pi k/(2m))/(2m)\) for the remaining modes. Vertex-transitive isotropy makes each Mahalanobis squared length equal to dimension, and a trace–determinant argument proves *global* minimum volume and unique center, including competitors not preserving symmetry. The classical sine-product identity then proves the exact volume fraction. Directly executed numerical checks covered every integer \(m\) from 2 through 20. No step infers an infinite theorem from those checks.

## Originality — PASS (provisional priority)
The first public version of Kálmán–Tóthmérész (2021-05-03, arXiv:2105.00960) was inspected for geometric scope; its treatment centers on shellable dissections and Ehrhart data. The closest published *same family* result establishes incenter radius, support-plane distances and an incenter parity law, not the **minimum-volume enclosing ellipsoid**. Full-text comparisons to the published odd-prism and wheel edge-polytope Löwner results show distinct graph families, dimensions and orbit structure; their exact scalar optimizations do not imply the even-cycle determinant product. General graph Lewis-weight work supplies the classical ellipsoid optimal-design mechanism, credited rather than claimed. The trigonometric volume ratio may occur in unidentified older literature, and full historical priority remains provisional.

## Mathematical value — PASS
This is a naturally defined Euclidean metric invariant of an infinite canonical lattice-polytope family with an exact semiaxis profile. The sharp ratio \(m/2^{m-1}\) shows exponential failure of the smallest circumball as a volume-efficient outer model, while the ratio of ellipsoid semiaxes grows linearly; all vertices are still contacts with both objects. These facts distinguish Euclidean ellipsoidal geometry from merely combinatorial affine equivalence and can serve as a quantitative benchmark for graph-polytope approximation and optimal-design questions. The contribution is not the general isotropic-design theorem but its exact evaluated consequences in this family.

## Limits and risk
No claim is made for other edge weights, odd cycles, other orientations or arbitrary affine normalizations. Closely related papers may contain the same trigonometric product under alternate language or as an unstated special case. The claimed priority is best knowledge after the documented searches, not a uniqueness certificate.

Self-review: passed. Independent audit: not yet performed.

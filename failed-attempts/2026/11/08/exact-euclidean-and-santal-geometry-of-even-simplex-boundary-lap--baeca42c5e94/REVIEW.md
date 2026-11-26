# Independent mathematical audit

## correctness

PASS

With N=2k and the stated face orientations, centering the columns of NI−ssᵀ leaves N(e_i−1_A/k) in one sign block or its counterpart in the other. Their centered (k−1)-spaces are orthogonal. Polar vertices are −(v_i+v_j)/(4k) for opposite-block indices; their common norm gives the inradius, and the vertex norm gives the enclosing radius. The facet normals sum to zero and span, so no larger inball or nonzero equal-radius center is possible. Independent block permutations kill cross terms of invariant quadratic forms, and swapping the blocks equates the two scalar restrictions, proving the ellipsoid assertions by uniqueness. The centroid and the unique Santaló point are fixed by the group. Each of the k² facet cones omits one vertex per block and has the same volume. In the uniform-simplex second moment formula, averaging the sum of vertex outer products retains each vertex with weight 1−1/k; the square of the vertex sum restores weight 1/k, with no cross term. The resulting N² projector divided by (N−1)N gives covariance. The Gram determinant after omitting one vertex per block gives cone volume N^(2k−2)/[k(2k−2)!]; the polar is an orthogonal product of the regular simplex polars, each a reflected rescaling by 1/(4k). These give both volumes, their product and the stated Stirling asymptotic. All claims are intrinsic, for k≥2 and the specific orientation. The supplied checker and verification notes were inspected, not executed. Independent /workspace/branches/38aef4fa-d4fb-46ec-89b1-d61aeb3b04f0/independent_metric_moment_check.py checked radii, hulls, volumes and covariance for k=2,3,4; maximum observed covariance error was 2.22e−16, corroborative only.

## originality

FAIL

The frozen theorem presents the canonical isometric split and the even John/Löwner profile as part of its contribution, but an earlier indexed result states all of that for exactly the same realization, including contacts and uniqueness. Its proof already supplies the actual centered coordinates, facet pairs and symmetries. The product and covariance are not asserted as printed in that source: they are direct standard volume and simplex-moment evaluations of the known realization and its listed facets. The asserted package does not support the submitted originality framing.

## value

FAIL

The body and metric are natural, and the formulas could be useful as reference data. But the submitted structural geometry is already established in the same metric. The remaining volumes, covariance and asymptotic comparison are mechanically obtained by standard volume and simplex moments from that prior exact split and facet list. No additional structural or extremal finding is established beyond those evaluations.

The dated certificate retains the supplied scientific assessment, sources and limitations.

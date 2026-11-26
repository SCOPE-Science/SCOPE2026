# Independent mathematical audit

## correctness

PASS

With U=Σu_i, V=Σv_j, hat integration gives diagonal blocks diag(u_i V/3), diag(v_j U/3) and cross block u vᵀ/6. Block multiplication verifies the inverse: diagonal terms 3/(u_i V) or 3/(v_j U), a same-shore all-ones correction 1/(UV), and cross entries −2/(UV). For U_k of weight w=u_k/U, the dimensionless kernel endpoints (multiply by UV) are (1+3/w,−2) on incident edges and (1,−2) on other edges. Absolute affine integration gives ((3+w)²+4w²)/(6(1+w))+5(1−w)/6=g(w). Interpolation of endpoint kernels strictly lowers the evaluation norm below the larger endpoint bound at interior points because the endpoint kernels have opposite signs on a positive-length segment. Sign inputs attain the vertex evaluation norms, which give the essential supremum by continuity. Symmetry gives the L¹ norm by duality. As g decreases strictly, the optimum for fixed a,b comes from maximizing the smallest factor to 1/max(a,b), with the frozen statement's exact condition on both shores, not necessarily uniformity on the smaller shore. Small positive factors approach the unattained supremum 7/3. Since P1=1 the negative part of each row integrates to (g(w)−1)/2. Three independent rational configurations agree exactly with the matrix and row-integral identities.

## originality

FAIL

The exact vertex law is equivalent, shore by shore, to the already tabulated weighted star leaf law: all copies of each edge have the same kernel at a vertex of the other shore and their measures simply add. The general weighted bipartite deficit also recovers the full endpoint norm and norming points by direct substitution. This comparison is about scientific coverage, not priority inferred from a date.

## value

FAIL

Sharp stability and positivity defects of graph splines are useful, but in this family the vertex norms reduce directly to the known star leaf rows and the global extrema are consequences of the simplex constraints. The frozen record does not establish an independently useful exact invariant beyond this reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

A ball with center x satisfies each linear inequality a·x<=b with inward margin r||a|| in the native Frobenius metric, including valid redundant inequalities. In the coordinates u,v the normal lengths for nonnegativity, first-row differences, column-total differences, first-row cap and total cap are respectively 1, sqrt(2), 2, 1 and sqrt(2). Telescoping from u_m>=r and u_m+v_m>=2r gives sharp upper bounds r<=rho_m and r<=sigma_m(t); the baseline profiles in the record realize both lower margin chains and are feasible whenever those caps allow r. In the lower regime saturation fixes every column sum and both final entries. Nonnegativity and first-row differences then give precisely the displayed ordered z, per-coordinate bounds and z_1 cap. With positive slack the z-region has relative interior in m-1 dimensions (a point for m=1). At equality both margin chains saturate, leaving one point; above equality only the first-row profile is forced, and the remaining v-slacks are exactly the stated order simplex, whose volume is its containing cube's volume divided by m!. At t=0 the z_1 cap equals c(m-1), and reversal and scaling give 0<=Z_1<=...<=Z_(m-1) with Z_k<=k. Each constant run at a vertex is anchored either at zero or at the first index's cap, since an unanchored run can be perturbed. Conversely choosing equality with the previous index or equality to the cap at each index gives full-rank triangular constraints and distinct feasible vertices. For the volume one may sort points in [0,n]^n with n=m-1 and use ceilings on unit cells: the condition on the sorted ceilings is exactly that of n-car parking words. The circular argument gives (n+1)^(n-1) words and sorting divides volume by n!. Scaling each free direction by c and embedding it as (1,-1) gives the extra (sqrt(2)c)^n factor. Finally the original t=0 order polytope has just its binary threshold configurations as vertices (threshold decomposition; each binary point is extremal in the enclosing cube). These checks are analytic, including m=1 and the exact threshold; the supplied finite verifier was inspected, not executed.

## originality

PASS

The variable-second-supply phase transition and the zero-supply identification of the optimal-center locus survive. The all-ones predecessor mechanically gives not just the common radius but the entire t=1 high-regime slice; that slice is credited, rather than counted as an independent discovery. The parking-function volume itself and the defining flow geometry also have prior sources.

## value

PASS

The two competing margin chains give more than an isolated inradius: they explain a dimension collapse of the optimal-center set at a critical supply and different geometries on either side. At zero supply the known parking-function polytope appears in a new metric role, with an intrinsic volume conversion and an exponential center-vertex count against the original polytope's quadratic count. The meaningful content is the family and its full center loci, not the already known fixed all-ones value.

The dated certificate retains the supplied scientific assessment, sources and limitations.

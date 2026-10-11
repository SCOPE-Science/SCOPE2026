# Independent mathematical audit

## correctness

PASS

For unit vertex directions u_i of a centered regular n-simplex, sum_i u_i=0 and sum_i u_i u_i^T=((n+1)/n)I. Since d_i(P)=r+<u_i,p>, summing squared differences gives ((n+1)/n)||P-Q||^2 exactly. The barycentric identity d_i=(n+1)r lambda_i identifies the image and inverse map; setting Q at the center gives the second-moment formulas. Independent random checks in dimensions 2 through 7 reproduced the identities.

## originality

FAIL

Originality fails because the central theorem is implication-covered by standard regular-simplex barycentric geometry. Existing regular-simplex barycentric-coordinate documentation explicitly states that a regular simplex at its canonical scale preserves Euclidean distance in barycentric coordinates. The audited proof itself uses the standard relation d_i=(n+1)r lambda_i. Combining those facts gives the claimed facet-distance scaled isometry by one rescaling; its second-moment and inverse formulas are immediate corollaries.

## value

FAIL

The result is a clean reformulation, but under the required value bar it is a routine consequence of standard barycentric coordinates for a regular simplex and their known Euclidean metric normalization. The inverse and variance identities are immediate algebraic corollaries. It therefore does not fill a sufficiently distinct unknown mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.

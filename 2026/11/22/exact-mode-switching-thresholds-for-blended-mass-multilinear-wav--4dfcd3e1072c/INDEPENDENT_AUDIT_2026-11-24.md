# Independent mathematical audit

## correctness

PASS

For each coordinate, the constant and alternating vectors have consistent masses h/2 and h/6, and stiffnesses 0 and 2/h. Tensor products diagonalize both masses and the stiffness sum. On a Walsh vector with active set S the consistent mass is (V/2^d)3^(-|S|), and the stiffness divided by that mass is 12c^2 times the sum of h_j^(-2) over S. Dividing instead by the blended mass yields the stated spectrum, including zero. At cardinality k the largest numerator selects the k shortest sides up to ties. Cross multiplication of successive positive denominators gives the sign of 3^k(2s_k-r_{k+1})(1-alpha)-r_{k+1}alpha; the switching odds 3^k(2s_k/r_{k+1}-1) increase strictly, because s increases and the next positive r cannot increase. This yields all cardinalities, precisely adjacent ties at switches, the one- and d-coordinate endpoints, and no transition for d=1. The cube switches are 3/4 and 27/28 for d=3. For the positive modal spectrum, 0<lambda*dt^2<4 is exactly the distinct unit-circle-root regime. At equality n(-1)^n grows; above equality a root is outside the unit circle. Excluding the constant mode is necessary. The cube bound follows from k/3^k<=1/3; at alpha=1 the maximum is exactly 12dc^2/h^2. Replay: RESULT.md lines 35–67; CHECK.py and VERIFICATION.md were inspected as finite supporting evidence, not run or used as an all-dimension certificate.

## originality

PASS

The supported distinction is the exact upper envelope and ordered all-cardinality switching diagram for a single scalar Q1 orthotope, not mass blending, Walsh diagonalization, or the generic CFL formula. The closest same-day result shares the entire blended mass but analyzes inverse entries without stiffness. The inspected primary comparisons concern accuracy-optimized quadrature, trimmed or multiscale methods, or standard CFL bounds, not this exact switching theorem.

## value

PASS

Wave stability depends on the largest eigenvalue, and blending can change which spatial mode realizes it. Proving that every cardinality occurs, with exact anisotropic switch points and no hidden nonadjacent ties, provides information not supplied by the standard CFL relation or by endpoint comparison. The cube bound isolates fixed partial lumping from full consistency at growing dimension. These are useful single-cell spectral facts, not claims about assembled meshes, cheap mass inversion or dispersion accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.

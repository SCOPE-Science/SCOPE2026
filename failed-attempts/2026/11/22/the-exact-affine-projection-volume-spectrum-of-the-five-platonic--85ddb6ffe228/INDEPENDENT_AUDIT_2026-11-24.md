# Independent mathematical audit

## correctness

PASS

Cauchy's formula assigns each facet a centered segment with half-vector A_F n_F/2; an antipodal pair combines to one segment with half-vector A_F n_F. The three-dimensional zonotope volume is eight times the absolute triple-determinant sum in these half-vector conventions. An exact independent reconstruction, python3 /workspace/branches/check_platonic.py, starts with the frozen original vertices, enumerates supporting triples and recovers all facets, orders their boundaries, computes outward area vectors and body volumes, and sums all determinant contributions. All signs are computed in Q(sqrt(5)) without floating point. It verifies the five facets counts 6,20,12,8,4 in the order displayed, both antipodal determinant spectra, the golden-body projection volumes 1120+640sqrt(5) and 800sqrt(5), and all five ratios. The strict comparisons reduce to 5·63²>139², 5·12²>26² and 34²>5·15² between positive quantities, followed by 9<18. For example the squared equal-volume circumradius comparison gives (R(I)^3/vol(I))^2−(R(D)^3/vol(D))^2=9(sqrt(5)−2)/80>0, opposite to the ratio order. Affine covariance Π(TK)=|det T|T^(−t)Π(K) is consistent with the squared volume normalization in dimension three. No general projection-volume inequality is being verified.

## originality

FAIL

Both advertised new numbers are mechanically implied by existing volume tables under equivalent zonohedron names. The projection body of the icosahedron is the rhombic enneacontahedron scaled to edge 2sqrt(3), and that of the dodecahedron is the rhombic triacontahedron scaled to edge 2A_D. The basis-direction table and the exact volume formulas were independently inspected. These imply both volumes, ratios and the complete ordering with existing benchmarks. This establishes scientific coverage irrespective of whether a source lists the ratios in this notation or explicitly sorts them.

## value

FAIL

P is a natural affine-invariant benchmark and the five-body comparison is correct, but the frozen claim limits its increment to the two computed ratios and their ranking. They are recoverable by routine normalization and arithmetic from the exact existing tables once the dual normal sets are identified. The minor tables are auxiliary certificates for those evaluations, not an independently motivated surviving theorem in the frozen record. This is a rejection of the proposed incremental result, not of the usefulness of the invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.

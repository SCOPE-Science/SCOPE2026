# Independent mathematical audit

## correctness

PASS

The row-and-column weights in RESULT.md are pairwise distinct, so the projective fixed locus consists exactly of the coordinate lines lying in the variety. For E_ij every northwest rank is 0 except those in the southeast quadrant of (i,j), where it is 1. Monotonicity of the rank bounds makes membership equivalent to r_w(i,j)>0, or i>=m_j. The complex-algebraic torus identity for compactly supported Euler characteristic applies without a smoothness assumption; projectivity identifies this with ordinary topological Euler characteristic. The j-th summand ranges from j to n: equality in all lower bounds forces the first j values to be the j largest for each j, and equality in all upper bounds is equivalent to w(1)=1. This includes n=1 and gives 9 for 132, whose only nonautomatic condition is the northwest 2-by-2 determinant. The frozen artifacts/verify.py checks membership and the extremal statements for n<=7, not the torus identity. The decision rests on the all-n proof, not on executing the uploaded script.

## originality

FAIL

The literal prefix-minimum statement was not located as a separate prior theorem. However, it is a mechanical consequence of the existing projective coordinate fixed-point calculation and the published northwest rank definition; the conversion to prefix minima, extremizers, and example require no intervening structural theorem. This is coverage by implication, not a claim of verbatim prior publication.

## value

FAIL

The object and invariant are natural and the formula is a useful expository example. As a standalone result, however, a standard fixed-point rule and the defining rank conditions reduce the invariant immediately to counting permitted coordinates. The bounds, extremizers and 132 example are elementary evaluations of that count. There is no distinct surviving nonmechanical claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.

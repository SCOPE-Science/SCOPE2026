# Independent mathematical audit

## correctness

PASS

The exact matrix claim and strict/critical classification hold with the frozen definitions. P1=1 and Pe=a1+de give the reducing space span{1,e}; P is symmetric so the perpendicular complement is also invariant and contributes only rP^2 with eigenvalues at most r. The all-ones Rayleigh quotient r[1+(zeta-1)/n] is strictly above r. In the stated orthonormal basis the 2-by-2 block has trace T and determinant r^2 zeta d^2 by direct expansion, including d=0. Subtracting this block from the identity gives a positive diagonal matrix (because |d|<1) minus a rank-one positive update. On conjugating by the inverse square root of the diagonal matrix, only the eigenvalue along the update direction can cross zero. Its sign gives the frozen A-Bd^2 test. For zeta<=1/r the test is strictly subcritical because a=0 is excluded; between 1/r and zeta_c, B is positive at both endpoints and A-B=n(1-r)(1-r zeta)<0. At zeta=zeta_c, the determinant is zero at d=0 and negative otherwise, and above it the all-ones Rayleigh quotient exceeds 1. The physical endpoint a=1/(n-1) is included. The result establishes the conjectured threshold location, not literal strict stability on the preprint's closed interval: true unit-eigenvalue endpoints are critical in the frozen convention. It makes no nonlinear claim at criticality. Replay: RESULT.md lines 11–55; VERIFICATION.md and verify.py inspected, not executed.

## originality

FAIL

Demonstrable full coverage, not a finding about historical priority: distinct indexed Resultary record 3575e4cfa8c0 §5 explicitly treats exactly the uniform-hub class with arbitrary symmetric nonnegative constant-row-sum peripheral block and gives its dominant 2-by-2 block, as a subcase of broader spectral work. Its block is the frozen block in a rotated basis. The numerical eigenvalue formula and the piecewise threshold including equality are direct trace/determinant and sign evaluations of that same block; no independent mathematical remainder is established. The comparison does not infer provenance from dated paths or from inaccessible literature.

## value

PASS

Considered as a mathematical question, invariance of the leading eigenvalue under arbitrary peripheral rewiring subject to the stated symmetry and equal hub coupling is a useful structural conclusion. The classification makes precise the relation to conjectured intervals and distinguishes unit-root endpoints from strict inequalities. That significance does not make the frozen result a distinct contribution when the whole dominant quotient and its hypothesis class are already covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.

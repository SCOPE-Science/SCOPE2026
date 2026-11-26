# Independent mathematical audit

## correctness

PASS

The rank-≤6 locus of projective skew 10-by-10 forms is irreducible of codimension six, smooth away from rank ≤4 (codimension 15). A general P9 avoids the latter, meets the smooth stratum transversely, and cuts no new singularities on the rank-eight stratum. In a rank-six chart, the Pfaffian is an invertible factor times the quadratic Pfaffian of the four-dimensional Schur complement. Its normal Hessian is nondegenerate; hence the restricted Jacobian generators span the conormal of the transverse slice and generate its reduced ideal locally. The kernel incidence is an isomorphism over the rank-six stratum. Determinants, using projectivization of lines, give K_Z=−5g−15h, so 35 hyperplane cuts give −5g+20H. The nondegenerate alternating form on the six-dimensional quotient with values in O(H) trivializes det(Q*)⊗O(3H); g=3H on S and K_S=5H. Checked all four integers independently: on P9×Gr(4,10), the same kernel incidence is the regular zero set of E=(Λ²V*/Λ²Q*)⊗O(1), of rank 30. Integrating c_top(E) times the virtual tangent Chern classes using formal P9 hyperplane degree and 210 Grassmannian fixed points returned (330,−1650,7920,−31350), using exact rationals and Newton identities (python3 /workspace/review-evidence/check_frozen.py, pfaffian). The independent method is not an execution of the frozen 3150-point checker. HRR and Gauss–Bonnet give exactly the asserted polynomial, K³ and Euler characteristics. Only general slices are verified.

## originality

FAIL

No inspected source prints this complete exact table, but the numerical claims are mechanical specializations of published general formulas for projectivized skew rank strata and Euler characteristics of their general linear sections. Generic Pfaffian ring Hilbert series and the Gorenstein property also cover the Hilbert polynomial and the canonical line. The exact computation checks the table; it does not establish a new invariant distinct from those formulas.

## value

FAIL

The singular threefold and its numerical invariants are natural, and the direct computation is sound. But the entire numerical package is mechanically obtainable from explicit skew-rank CSM and general-section formulas, and the canonical line from established Pfaffian graded data. The frozen claim does not isolate a further independently useful invariant not already determined this way.

The dated certificate retains the supplied scientific assessment, sources and limitations.

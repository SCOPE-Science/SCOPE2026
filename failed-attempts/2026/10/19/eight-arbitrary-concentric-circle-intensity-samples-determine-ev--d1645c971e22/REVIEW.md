# Independent mathematical audit

## correctness

PASS

On the first circle the lift is a Laurent polynomial of degree at most two in each direction, hence vanishes identically if it vanishes at five distinct sites. This gives H02=0, H01+H12=0 and trace H=0. At radius R the second harmonic is then absent and three distinct sites kill the remaining Laurent polynomial of degree one, including the off-diagonal term with coefficient R(1-R²). The two diagonal equations have exactly the line spanned by (R²,−1−R²,1) as their kernel. This generator has rank three, excluding a nonzero rank-at-most-two difference of vector lifts, including for zero coefficients. For at most seven measurements the real Hermitian kernel has dimension at least two. If the measurement vectors span, the kernel has no nonzero semidefinite matrix; the odd determinant on a circle in a two-dimensional kernel subspace forces a singular indefinite rank-two difference, proving noninjectivity. If the vectors do not span, a nonzero vector is indistinguishable from zero. Equal radii and repeated nodes fail by the one-circle rank bound and the seven-effective-measurement bound, respectively. For a nonzero rank-at-most-two H and its unit null vector v, the squared distance from D_R to the line of H is at least min(1,R⁴), since (D_R−tH)v=D_Rv. The ratio in the claim is this distance divided by ||D_R||_F². Removing the least absolute eigencomponent gives equality at an indefinite rank-two H. This is a kernel-angle estimate, not a uniform bound on measured output norms.

## originality

FAIL

Pohl–Li–Boche's 2017 author presentation states the arbitrary concentric allocation 2n+1 and 2n−1 for polynomials of degree at most n, giving exactly the frozen five-plus-three sampling theorem. Bandeira–Cahill–Mixon–Nelson's theorems give the already-known eight-measurement necessity and the same nullity/odd-determinant criterion in dimension three. The kernel line is a direct consequence: D_R annihilates evaluations identically on both circles, and known phase injectivity forces nullity at most one. The exact angle, not printed in those passages, is then the standard best rank-two Frobenius approximation error of D_R relative to its norm, attained by deleting one eigencomponent. There is no distinct supported contribution in these specializations.

## value

FAIL

The design is useful, but the central arbitrary 5+3 recovery result and its global minimum are already covered. The explicit obstruction line follows from one diagonal polynomial and the known nullity criterion. The sharp normalized kernel distance then just evaluates a standard rank-truncation identity on that diagonal matrix; it controls neither the angular conditioning nor a distinct sampling phenomenon. There is no genuine surviving value-bearing remainder to repair without adding new mathematics.

The dated certificate retains the supplied scientific assessment, sources and limitations.

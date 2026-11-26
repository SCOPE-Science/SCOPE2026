# Independent mathematical audit

## correctness

PASS

A nonzero normal form is a path pair with common terminal vertex (including length-zero paths and distinct parallel edges), so grade convolution gives T(t)=sum_v P_v(t)^2. Prefix cancellation makes its square nonzero precisely for comparable paths. Equal paths are counted once by P_v(t^2); each strict orientation gives a base path and a nonempty closed suffix, counted by P_v(t^2)(C_v(t)-1). Repetition of the closed suffix or its inverse leaves every power nonzero, whereas an incomparable pair squares to zero. Thus T-Q counts nonzero square-zero elements, not the semigroup zero. The adjacency resolvent gives rationality for all finite graphs. For primitive A, the rank-one spectral projection r l^T gives residues in the (1-rho*t) denominator equal to (sum r)l_v for P_v and r_v l_v for C_v. The total has double-pole coefficient (sum r)^2 sum l_v^2. Since rho>1, P_v(t^2) is analytic in a disk past the dominant point and its value there is P_v(rho^(-2)); the simple-pole coefficient of Q is 2 sum_v P_v(rho^(-2)) r_v l_v. Primitivity excludes other dominant poles. Dividing the leading coefficients of O(rho^n) and (n+1)rho^n, with exponentially smaller remainder for Q and O(rho^n) remainder for T, gives the stated constant and O(n^(-2)) error. Reciprocal rescaling of the two eigenvectors leaves the constant unchanged. The exact formulas do not require primitivity; the probability statement does, and is at exact normal-form length, not arbitrary word length. A separate direct two-letter word-pair check gives Q_0 through Q_6 = 1,4,10,24,52,112,232, T_n=(n+1)2^n and c_E=4. The frozen finite checker was inspected, not rerun; finite cases are corroboration, not a proof of the asymptotics.

## originality

PASS

The supported contribution is the square-predicate refinement of normal-form growth and its explicit Perron survival constant, not the normal form, cancellation criterion, coarse growth or the elementary power dichotomy taken alone. Search and retrieval limits are recorded below.

## value

PASS

Square-zero is intrinsic to the semigroup, while a normal-form generating series is natural for comparing large-degree elements across graphs. The exact rational refinement applies to both finite and infinite cases, and the simple-pole versus double-pole contrast yields a quantitative rare-survival phenomenon with an explicit graph-dependent constant. This is more informative than detecting zero products by the classical prefix test or reporting total growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.

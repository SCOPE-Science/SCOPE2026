# Independent mathematical audit

## correctness

PASS

For normalized circle integration and odd N, the N mutually distinct nodes give an invertible Fourier interpolation system (multiply each interpolant by e^{imx} and use ordinary polynomial unisolvence on the unit circle). At u=0 the weights are uniform. For 0<u<1, sum the two uniform-grid Dirichlet cardinal evaluation identities at the changed sites: the coefficient on the sum of old endpoint values is sin(πu)S_N(u)/N. Solving gives the two identical positive weights, and for the stationary middle site the sum of cardinal evaluations is 2 sin(πu)f(1−u)/N, giving w₁=(1−R_N)/N. At other fixed sites the numerator relative to the moving coefficient is a signed translate of the convex cosecant difference. For N≥5, f(v)−f(v+2(1−u)) strictly decreases in v and the two outermost relevant translates, j=3 and j=N−1, are opposite by reflection; their common absolute value is strictly smaller than S_N. There are no other sites when N=3. Thus the nonmiddle weights stay positive. Independently, putting s=π/N and z=1−u, the product-to-sum identity gives R_N=(sin²s−sin²(sz))/(cos(s)sin²(sz)), strictly increasing from 0 to ∞ in u. The crossing is below 1/2 by R_N(1/2)>2, and the middle weight is zero, not negative, at equality. The exact root is equivalently u_N=1−arcsin(√2 sin(s/2))/s, whose Taylor expansion reproduces the stated N^{-2} correction. Since the weights sum to one and only w₁ can be negative, matching the real error signs gives the exact ℓ∞ norm. Using sin(sz)∼sz in the displayed quotient recovers the fixed-N quadratic coefficient; no claim of quadrature at coincident nodes is made. The submitted check.py and VERIFICATION.md were inspected, not executed; their documented finite Fourier-moment and numerical asymptotic checks can be replayed with Python 3 and do not substitute for the all-N proof.

## originality

PASS

Credit existing degree-one three-node formulas and partial same-day overlap; the distinct supported claim is the exact localized law across odd grids, in particular N≥5, with a single stationary sign change, finite-grid noise norm and sharp triple-collision coefficient. Broad conditioning, worst-grid positivity radii, and different adjacent-site deformations do not establish that law. Historical priority beyond the compared sources is not asserted.

## value

PASS

The two displaced samples and fixed middle sample give a natural test of local crowding distinct from arbitrary global jitter and ordinary adjacent double collision. The exact weight sign transition tells when the quadrature ceases to be positivity preserving; the sharp bounded-error norm and its coefficient quantify exactly what fails as the three sites merge. The across-grid result and the one-weight mechanism beyond degree one are useful even though the isolated N=3 case is covered by earlier gap formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.

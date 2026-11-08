# Strict Santaló-volume monotonicity for the cubic threefold-projection exception

## Finding
Let \(S^2\) be the Euclidean unit sphere and put \(f(u)=u_1u_2u_3\). For real \(\varepsilon\), set \(h_\varepsilon(u)=1+\varepsilon f(u)\). Define \(\varepsilon_c=\sup\{t\ge0:h_t\text{ is the support function of a convex body}\}\). Then \(1/2\le\varepsilon_c\le1\), the admissible interval is precisely \([-\varepsilon_c,\varepsilon_c]\), and every corresponding body \(K_\varepsilon\) is full-dimensional, contains the origin in its interior, and has Santaló point exactly the origin. The endpoint is included; this paper does not require a closed radical expression for \(\varepsilon_c\).

Put \(s=\varepsilon^2\) and \(\kappa_3=4\pi/3\). Throughout the entire admissible interval,
\[
\frac{\operatorname{vol}_3(K_\varepsilon)\operatorname{vol}_3(K_\varepsilon^\circ)}{\kappa_3^2}
=(1-s/7)\;{}_3F_2\!\left(\begin{matrix}1/2,3/2,2\\5/6,7/6\end{matrix};s/27\right).
\]
The right-hand side has expansion
\[
1-\frac{3}{35}s-\frac{181}{35035}s^2-\sum_{j\ge3}c_j s^j,
\qquad c_j>0.
\]
Consequently the Santaló volume product is **strictly decreasing with** \(|\varepsilon|\) on \([0,\varepsilon_c]\), and has its unique maximum at the Euclidean ball. More precisely the sharp global-in-parameter quadratic estimate holds:
\[
\kappa_3^2-\operatorname{vol}_3(K_\varepsilon)\operatorname{vol}_3(K_\varepsilon^\circ)
\ge \frac{3}{35}\,\kappa_3^2\varepsilon^2,
\]
with equality only at \(\varepsilon=0\). The constant \(3/35\) cannot be increased because the normalized quotient tends to \(3/35\) as \(\varepsilon\to0\). This is a statement about the explicit cubic constant-width family, not a general stability theorem for arbitrary convex bodies.

## Assumptions and scope
All volumes are three-dimensional Euclidean Lebesgue volumes. Polarity is about the origin: \(K^\circ=\{y:\langle x,y\rangle\le1\ \forall x\in K\}\). The Santaló point is the unique translation center minimizing the volume of the polar. The hypergeometric function is interpreted by its ordinary power series around zero; here \(0\le s\le1\), strictly within its convergence radius \(27\). For \(\varepsilon=\pm\varepsilon_c\), formulas follow by continuity even if the support curvature loses strict positivity. No assertion about unrestricted nonspherical bodies or all constant-width bodies is made.

The underlying family arises naturally in the exceptional triangular-projection phenomenon: on any great circle the restriction of \(u_1u_2u_3\) has Fourier frequencies only \(1\) and \(3\); translation removes the first frequency, leaving a threefold rotationally symmetric planar projection. The construction and its relevance were established in the motivating 2026 paper [1]. The finding here is the exact polar-volume and Santaló-product profile and its global monotonicity, not that projection-symmetry construction.

## Proof
**Step 1 (admissibility and Santaló center).** The homogeneous cubic \(F(x)=x_1x_2x_3\) restricts to \(f\) on \(S^2\). Its spherical support-curvature perturbation is \(Q=\nabla^2_{S^2}f+fI\) on tangent planes. For unit \(u\) and tangent unit \(v\), homogeneity gives
\[
\langle Qv,v\rangle=D^2F(u)[v,v]-2f(u).
\]
The Euclidean Hessian has squared Frobenius norm \(2\) on \(S^2\); also \(|f(u)|\le1/(3\sqrt3)\). Therefore \(\|Q\|_{\mathrm{op}}\le\sqrt2+2/(3\sqrt3)<2\), so \(I+\varepsilon Q\) is positive definite for \(|\varepsilon|\le1/2\). At \(u=(0,0,1)\), \(Q\) has eigenvalues \(1,-1\), forcing \(|\varepsilon|\le1\) for any convex support function. Since support functions form a closed convex cone in the uniform topology and \(h_{-\varepsilon}(u)=h_\varepsilon(-u)\), the admissible set is the claimed closed symmetric interval. Moreover \(h_\varepsilon(u)\ge1-1/(3\sqrt3)>0\), so the origin is interior throughout it.

Every \(h_\varepsilon\) is invariant under each half-turn changing the signs of two coordinates. These three rotations have only the origin as a common fixed point. The Santaló center is unique and equivariant under Euclidean symmetries, hence it must be the origin. Thus the polar product below is the true Santaló product, not merely a nonoptimal-centered polar product.

**Step 2 (primal volume).** For a \(C^2\) strictly curved support function in three dimensions,
\[
\operatorname{vol}_3(K_\varepsilon)=\frac13\int_{S^2}h_\varepsilon\det(I+\varepsilon Q)\,d\sigma.
\]
The function \(f\) is a degree-three spherical harmonic, so \(\Delta_{S^2}f=-12f\), \(\operatorname{tr}Q=-10f\), and \(\int_{S^2}f^2\,d\sigma=4\pi/105\). By the integrated Bochner identity on the unit two-sphere,
\[
\int_{S^2}\det Q\,d\sigma
=\frac12\int|\nabla f|^2+\int f\Delta f+\int f^2
=(6-12+1)\int f^2=-5\int f^2.
\]
The linear and cubic terms of the volume polynomial vanish by antipodal parity. The quadratic term is \(\frac13(-5-10)\int f^2=-5\int f^2\). Hence
\[
\operatorname{vol}_3(K_\varepsilon)=\frac{4\pi}{3}\left(1-\frac{s}{7}\right).
\]
This formula extends to the curvature-degenerate endpoints by approximating them from within the admissible interval.

**Step 3 (polar volume).** The radial function of \(K_\varepsilon^\circ\) is \(h_\varepsilon^{-1}\), giving
\[
\frac{\operatorname{vol}_3(K_\varepsilon^\circ)}{\kappa_3}
=\frac1{4\pi}\int_{S^2}(1+\varepsilon f)^{-3}\,d\sigma
=\sum_{k=0}^\infty a_k s^k,
\quad
 a_k=\binom{2k+2}{2}\frac{((2k-1)!!)^3}{(6k+1)!!},
\]
where \((-1)!!=1\). This follows by expanding the binomial series and using the exact sphere moment \(\frac1{4\pi}\int f^{2k}\,d\sigma=((2k-1)!!)^3/(6k+1)!!\). It converges uniformly for all admissible \(\varepsilon\), since \(|\varepsilon f|\le1/(3\sqrt3)\). Applying the triplication identity for Pochhammer symbols gives
\[
\sum_{k=0}^\infty a_k s^k={}_3F_2\!\left(\begin{matrix}1/2,3/2,2\\5/6,7/6\end{matrix};s/27\right).
\]

**Step 4 (every nonconstant coefficient is negative).** For integers \(k\ge1\), direct cancellation of the double factorials gives
\[
\frac{a_k}{a_{k-1}}=\frac{(k+1)(2k+1)(2k-1)^2}{k(6k-3)(6k-1)(6k+1)}.
\]
The inequality \(7a_k<a_{k-1}\) is equivalent to positivity of
\[
 k(6k-3)(6k-1)(6k+1)-7(k+1)(2k+1)(2k-1)^2
=(2k-1)(80k^3-28k^2+4k+7)>0.
\]
Thus every coefficient \(b_k=a_k-a_{k-1}/7\) of \((1-s/7)\sum_ja_js^j\) is **strictly negative** for \(k\ge1\). In particular \(b_1=-3/35\) and \(b_2=-181/35035\). Absolute convergence on \(0\le s\le1\) permits termwise comparison and differentiation, proving strict decrease, the global quadratic deficit, uniqueness of equality, and sharpness by the \(s\downarrow0\) expansion. \(\square\)

## Verification
The standalone `verify.py` reproduces the double-factorial and rational coefficient identities, tests the exact inequality \(7a_k<a_{k-1}\) for \(1\le k\le120\), and independently integrates the primal support-volume and polar radial-volume expressions via Gauss–Legendre/spherical quadrature at four parameters. These finite checks support the computations but the all-parameter conclusions follow from the analytic proof and the displayed polynomial positivity, not extrapolation. The numerical comparison tolerance is \(10^{-10}\) in units of \(\kappa_3\).

## Relationship to prior work
Myroshnychenko, Ryabogin and Saroglou [1] introduce the cubic harmonic \(u_1u_2u_3\) as the canonical exceptional class for universal threefold-symmetric planar shadows, proving that small perturbations remain convex. Their main theorem characterizes higher-fold projection symmetry and does not give the Santaló product or its monotonicity.

The classical Blaschke–Santaló inequality [2] bounds the volume product above by that of the ball, with ellipsoidal equality. That global comparison does **not** imply that the product is ordered at two different nonzero parameters or provide the exact coefficient series and sharp in-family quadratic constant.

Related geometric calculations for this same cubic support family concern the support-function convexity threshold and its directional projected-area (brightness) function; these are different invariants and do not directly supply the polar integral or product comparison. Standard support-function and spherical-harmonic identities provide ingredients [1,3], but the displayed exact hypergeometric profile and all-orders coefficient sign are the specific claims established here.

## Limitations
The result is restricted to the one-parameter cubic harmonic family; no minimum among arbitrary constant-width bodies, general sharp Santaló stability modulus, or closed form for the endpoint \(\varepsilon_c\) is claimed. The title uses the name of the threefold-projection exception for geometric motivation, not as a uniqueness assertion for all examples. Literature priority remains provisional, and no independent mathematical audit has been performed. The code is only supporting verification and is not an infinite-proof certificate.

## References
[1] S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192, first submitted 2026-09-23, Sections 1, 3, 5. https://arxiv.org/abs/2609.27192

[2] *Blaschke–Santaló inequality*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Blaschke-Santal%C3%B3_inequality (background on the general volume-product comparison).

[3] R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd edition (standard support-function reference; cited in [1]).

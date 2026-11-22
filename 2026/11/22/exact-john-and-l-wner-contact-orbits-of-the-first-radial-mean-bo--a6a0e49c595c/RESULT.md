# Exact John and Löwner contact orbits of the first radial mean body of a three-cube

## Finding

Let \(Q=[-1,1]^3\) and let \(R_1Q\) be its Gardner–Zhang first radial mean body. The unique maximum-volume ellipsoid inside \(R_1Q\) and the unique minimum-volume ellipsoid containing it are the concentric Euclidean balls
\[
B_2^3\!\left(0,\frac{17\sqrt{17}}{81}\right)
\quad\text{and}\quad B_2^3(0,1),
\]
respectively. All \(24\) contact points with the inner ball are the points
\[
\frac{17\sqrt{17}}{81}\,u,
\qquad u\in\left\{\frac{(\epsilon_1 a_1,\epsilon_2 a_2,\epsilon_3 a_3)}{\sqrt{17}}:
(a_1,a_2,a_3)\text{ permutes }(3,2,2),\ \epsilon_j\in\{-1,1\}\right\}.
\]
All \(6\) contact points with the outer ball are \(\pm e_1,\pm e_2,\pm e_3\). In particular, the shortest radial directions are not the cube axes, face diagonals, or body diagonals: they form an oblique cubic-symmetry orbit with coordinate ratio \(3:2:2\).

For comparison, the known body-diagonal radius is \(\sqrt3/2\); its strict excess above the sharp inner radius is quantified by the exact difference of squared auxiliary values \(27-19652/729=31/729\). Thus sampling only the standard high-symmetry directions fails to detect the true insphere contacts.

## Assumptions and scope

A convex body has nonempty interior; the Euclidean norm is the standard norm on \(\mathbb R^3\). For \(u\in S^2\), write \(\rho_{L}(u)=\sup\{r\ge0:ru\in L\}\). The Gardner–Zhang convention, at the first mean, is
\[
\rho_{R_1Q}(u)=\frac{1}{\operatorname{Vol}(Q)}\int_Q \rho_{Q-x}(u)\,dx
=\int_0^\infty\frac{g_Q(ru)}{\operatorname{Vol}(Q)}\,dr,
\]
where \(g_Q(z)=\operatorname{Vol}(Q\cap(Q+z))\). The final equality follows by Fubini's theorem and uses the usual positive-ray exit length. We use the classical fact that radial mean bodies with positive parameter are convex; in this statement no convexity assertion for negative parameters is needed. All stated ellipsoids are ordinary Euclidean ellipsoids, not a claim about the Banach–Mazur minimizer.

## Proof

**1. Reduce all spatial directions to a two-variable polynomial.** Since
\[
\frac{g_Q(z)}{\operatorname{Vol}(Q)}=\prod_{j=1}^3\left(1-\frac{|z_j|}{2}\right)_+,
\]
reflection and coordinate-permutation symmetries let us write an arbitrary unit direction as a signed permutation of \((1,s,t)/\sqrt{1+s^2+t^2}\), with \(s,t\in[0,1]\). Here \(s,t\) are not required to be ordered. Put
\[
S(s,t)=1+s^2+t^2,\qquad D(s,t)=6-2s-2t+st,
\qquad H(s,t)=\sqrt{S(s,t)}D(s,t).
\]
Substitution of the cube covariogram and the variable \(z=r/(2\sqrt{S})\) gives the exact formula
\[
\rho_{R_1Q}(u)=2\sqrt{S}\int_0^1(1-z)(1-sz)(1-tz)\,dz
=\frac{H(s,t)}6.
\]
The integrand is nonnegative, so the expression is well defined and continuous on the closed parameter square.

**2. Exhaustively classify interior extrema.** For \(0<s,t<1\), the respective numerators of the partial derivatives of \(H\), after multiplication by \(\sqrt S\), are
\[
A=sD-(2-t)S,\qquad B=tD-(2-s)S.
\]
They satisfy the exact identity \(A-B=(s-t)(D-S)\). The function \(D-S=5-2s-2t+st-s^2-t^2\) has strictly negative partial derivatives on \([0,1]^2\), and its minimum, attained only at \((1,1)\), is zero. Thus an interior stationary point must have \(s=t=z\). On this diagonal,
\[
A(z,z)=B(z,z)=(1-z)^2(3z-2),
\]
so the only interior stationary point is \((s,t)=(2/3,2/3)\). There
\[
H^2=\frac{19652}{729},\qquad
\rho_{R_1Q}=\frac{17\sqrt{17}}{81}.
\]

**3. Check every boundary, including its endpoints.** On the edge \(s=0\),
\[
H(0,t)=\sqrt{1+t^2}(6-2t),\qquad
\sqrt{1+t^2}\,\frac{d}{dt}H(0,t)=-2(2t-1)(t-1).
\]
This edge has its unique interior minimum at \(t=1/2\), with \(H=5\sqrt5/2\), and maximum \(H=6\) at \(t=0\). On the edge \(s=1\),
\[
H(1,t)=\sqrt{2+t^2}(4-t),\qquad
\sqrt{2+t^2}\,\frac{d}{dt}H(1,t)=-2(t-1)^2,
\]
so it decreases strictly from \(4\sqrt2\) to \(3\sqrt3\). By symmetry, the edges \(t=0\) and \(t=1\) have the same classifications. The diagonal endpoint obeys \((3\sqrt3)^2=27\), whereas the interior stationary point has squared value \(19652/729<27\), with exact gap \(31/729\). Also \(5\sqrt5/2>3\sqrt3\). It follows from compactness and the exhaustive critical-point and boundary analysis that the **unique reduced global minimum** is \((2/3,2/3)\), and the **unique reduced global maximum** is \((0,0)\). This determines the stated radii and, by restoring all signed coordinate permutations, exactly \(24\) inner and \(6\) outer directions.

**4. Upgrade sharp centered radii to John–Löwner ellipsoids.** The body \(R_1Q\) is origin-symmetric and invariant under all signed coordinate permutations. The unique maximal-volume inscribed ellipsoid (John's ellipsoid) and unique minimal-volume enclosing ellipsoid (Löwner's ellipsoid) must inherit these symmetries. The only invariant positive-definite quadratic forms under this group are scalar multiples of the identity, so both ellipsoids are centered balls. Their radii are precisely the computed minimum and maximum radial values. For completeness, the inball center is unique even within the class of balls: at each of its \(24\) contact points the inner ball's supporting plane, with normal \(u\), also supports the convex body. Any equal-radius inscribed ball centered at \(c\) would therefore require \(u\cdot c\le0\) for every such \(u\). Antipodal contact pairs force equality, and these directions span \(\mathbb R^3\); hence \(c=0\). The \(6\) antipodal outer contacts similarly force the circumcenter to be the origin.

## Verification

The included standard-library program `verify.py` independently integrates the exact three-cube covariogram with composite Simpson quadrature for \(160\) deterministic unit directions, and checks the closed radial formula to absolute tolerance \(2.1\cdot10^{-11}\). Exact rational calculations verify the stationary-point identity, its diagonal factorization, boundary derivative identities, the strict rational gap \(31/729\), and \(289\) rational grid values. The output is `CUBE_R1_EXACT_CONTACT_CHECKS_OK`. These finite checks are reproducibility aids; the all-direction classification rests on the analytic global critical-point proof above, not on numerical enumeration.

## Relationship to prior work

Gardner and Zhang introduced \(R_pK\) and proved its convexity for \(p\ge0\). Langharst's 2026 work extends convexity to \(-1<p<0\); this is background, not a claimed contribution. Langharst, Manui and Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117v2, Proposition 34, already derive the **entire cube covariogram integral** and evaluate axial and body-diagonal radial directions. The integral and those endpoint values are explicitly prior work. The present claim is instead the sharp **global** angular extremization of that known expression for the three-cube at \(p=1\), with its nonstandard oblique \(24\)-point John contact orbit, exact radius, and full six-contact Löwner orbit. A closely related published differentiability classification of radial mean bodies of parallelotopes concerns smoothness and tie strata, not these Euclidean optima; the published planar-square radius classification concerns dimension two and does not imply the three-dimensional optimum.

## Limitations

The theorem fixes the canonical three-dimensional cube and the first radial mean parameter. It does not classify the contact orbits at arbitrary \(p\) or in dimensions at least four, nor optimize anisotropic Banach–Mazur containment ellipsoids beyond the stated John–Löwner characterization. The cube radial integral is known, and the work claims novelty only for its exact three-dimensional global extremizers and ellipsoid contacts. Possible unindexed older computations and unavailable full text of Gardner–Zhang's 1998 original are residual historical-priority risks.

## References

1. D. Langharst, A. Manui, and A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117, first public version 2026-01-27, v2 (2026-06-30), Proposition 34, https://arxiv.org/pdf/2601.20117v2.
2. D. Langharst, *Convexity of Radial Mean Bodies via an Extension of Ball's Bodies*, arXiv:2603.14134, first public version 2026-03-14, https://arxiv.org/html/2603.14134v5.
3. R. J. Gardner and G. Zhang, *Affine inequalities and radial mean bodies*, *American Journal of Mathematics* **120** (1998), 505–528, https://doi.org/10.1353/AJM.1998.0021.
4. J. Haddad, *Planar radial mean bodies are convex*, arXiv:2412.01475, first posted 2024-12-02, https://arxiv.org/abs/2412.01475.

# Coexisting opposite Lyapunov orderings in an equilateral ellipsoidal open billiard

## Finding

Let three ellipsoidal obstacles have their centers at the vertices of an equilateral triangle of side \(1\), with common equation in centered coordinates
\[
 u^2+v^2+\beta^2 z^2\le r^2,\qquad r=\frac1{10},\quad 1<\beta<\frac2{\sqrt3}.
\]
For the open billiard map \(B\) on the compact nonescaping set, denote the positive exponent along the vertical (out-of-plane) unstable direction by \(\chi_\perp(\mu)\), and the positive exponent along the planar unstable direction by \(\chi_\parallel(\mu)\), both normalized per collision. Then there are two periodic invariant probabilities with *opposite* strict orderings:
\[
\chi_\perp(\mu_2)>\chi_\parallel(\mu_2)>0,
\qquad
\chi_\parallel(\mu_3)>\chi_\perp(\mu_3)>0.
\]
The same two strict inequalities hold, respectively, for two distinct **ergodic, full-support Gibbs measures for Hölder potentials** on the same nonescaping set. Thus the geometrically distinguished planar and transverse unstable line bundles cannot have a uniform Lyapunov ordering across all Gibbs measures for these parameters.

The periodic probabilities \(\mu_2\) and \(\mu_3\) are supported on the alternating two-obstacle orbit and an equilateral three-obstacle orbit. Their four exponents are explicit:
\[
\begin{aligned}
\chi_\perp(\mu_2)&=\operatorname{arcosh}\left(1+\frac{\beta^2(1-2r)}r\right),&
\chi_\parallel(\mu_2)&=\operatorname{arcosh}\left(1+\frac{1-2r}r\right),\\
\chi_\perp(\mu_3)&=\operatorname{arcosh}\left(1+\frac{\sqrt3\,\beta^2(1-\sqrt3r)}{2r}\right),&
\chi_\parallel(\mu_3)&=\operatorname{arcosh}\left(1+\frac{2(1-\sqrt3r)}{\sqrt3r}\right).
\end{aligned}
\]
In particular, the crossing of the two exponents on the displayed three-cycle occurs at \(\beta=2/\sqrt3\), while the two-cycle already has a larger transverse exponent at every \(\beta>1\). The stated parameter interval is a certified coexistence range; it is **not** asserted to be maximal for all periodic trajectories.

## Assumptions and scope

Put the obstacle centers at \(O_1=(0,0,0)\), \(O_2=(1,0,0)\), and \(O_3=(1/2,\sqrt3/2,0)\). Every obstacle is the closed ellipsoid \(K_i=\{(x,y,z):(x-X_i)^2+(y-Y_i)^2+\beta^2z^2\le r^2\}\). The ball map records postcollision position and outgoing unit velocity; exponents are counted **per collision**, not per unit flight time. We consider the compact set of bi-infinite nonescaping trajectories, on which coding by successive obstacle labels is conjugate to the two-sided shift on \(\{1,2,3\}\) forbidding equal consecutive labels. This standard coding is valid here because the obstacles are smooth, strictly convex, disjoint, and satisfy no eclipse. Indeed each obstacle lies in the radius-\(r\) ball about its center, the convex hull of two such balls lies in the radius-\(r\) tubular neighborhood of their center segment, and the third center is at distance \(\sqrt3/2>2r\) from that segment.

The ambient plane \(z=0\) is invariant under reflection. As in the standard open-billiard construction for coplanar centers, all trapped trajectories lie in that plane. Reflection symmetry gives two invariant transverse variational blocks, one within the plane and one vertical. On the uniformly hyperbolic trapped set, each supplies one continuous unstable line bundle and a corresponding positive Lyapunov exponent for every ergodic invariant measure.

## Proof

**1. The two explicit periodic rays.** Let \(C=(O_1+O_2+O_3)/3\). The alternating ray between \(O_1\) and \(O_2\) strikes at \(q_1=O_1+r(O_2-O_1)\) and \(q_2=O_2+r(O_1-O_2)\). It retraces the segment and has constant free-flight length \(L_2=1-2r\) and outgoing incidence cosine \(c_2=1\). At the three-cycle use \(q_i=O_i+r(C-O_i)/\lVert C-O_i\rVert\), visiting obstacles in cyclic order. The \(q_i\) form a smaller equilateral triangle: \(L_3=1-\sqrt3r\), with outgoing incidence cosine \(c_3=\sqrt3/2\). Both paths satisfy the specular reflection law, because the outward normal at each \(q_i\) points to the centroid and bisects the angle between outgoing ray and the reversal of the incoming ray. They therefore are genuine primitive periodic trajectories, with no intermediate obstacle crossings.

**2. The physical principal curvatures.** At an equatorial hit, the obstacle defining function is \(F_i=(x-X_i)^2+(y-Y_i)^2+\beta^2z^2-r^2\). Its gradient has norm \(2r\) and its Hessian is \(2\operatorname{diag}(1,1,\beta^2)\). The shape operator therefore has equatorial principal curvatures \(\kappa_\parallel=1/r\) and \(\kappa_\perp=\beta^2/r\). Here \(\beta^2/r\), rather than \(\beta/r\), is the curvature of the *displayed physical ellipsoid equation*; it also follows directly by differentiating the unit normal.

**3. Scalar linearization and exact multipliers.** In adapted Poincaré coordinates \((U,V)\) for displacement and direction variation orthogonal to each flight, free flight followed by an exterior convex reflection has the positive symplectic block
\[
 M(a,L)=\begin{pmatrix}1&L\\a&1+aL\end{pmatrix},
 \qquad\det M=1,\quad\operatorname{tr}M=2+aL.
\]
In the vertical direction projection onto the tangent plane leaves the vector unchanged, so the reflection kick is \(a_\perp=2c\kappa_\perp=2\beta^2 c/r\). In the planar transverse direction the projection/angle factors instead yield \(a_\parallel=2\kappa_\parallel/c=2/(rc)\). This is the standard Jacobi/Poincaré billiard linearization; it can equivalently be checked directly by differentiating the intersection of a ray with the quadratic obstacle and its specular reflection. On either of the symmetric periodic paths \(a\), \(L\), and \(c\) are constant along all collisions. Changes of adapted signed frame may multiply a one-step block by \(-1\), affecting eigenvalue signs but not absolute values. Therefore the unstable expansion per collision is
\[
 \log\rho(M(a,L))
 =\operatorname{arcosh}\left(1+\frac{aL}{2}\right).
\]
Indeed the expanding eigenvalue is \((2+aL+\sqrt{(2+aL)^2-4})/2\), and a \(p\)-step monodromy is (up to sign/conjugacy) the \(p\)-th power of the common scalar block. Substituting \((c,L)=(1,1-2r)\) and \((\sqrt3/2,1-\sqrt3r)\) yields the four exact expressions in the finding. All are positive since \(L>0\).

**4. Opposite orders.** Because \(\operatorname{arcosh}\) is strictly increasing on \((1,\infty)\), at the two-cycle the transverse exponent exceeds the planar exponent exactly when \(\beta^2>1\). At the three-cycle the transverse exponent is smaller exactly when \(\beta^2 c_3<1/c_3\), or \(\beta^2<4/3\). Both hold simultaneously throughout the specified open parameter interval.

**5. Promotion from periodic probabilities to Gibbs probabilities.** Give the symbolic space its standard two-sided metric \(d_\theta\), and for either periodic orbit \(P\subset\Sigma_A\) consider the Hölder potential \(\phi_t(s)=-t\,d_\theta(s,P)\) with \(t>0\). Its unique equilibrium/Gibbs measure \(\nu_t\) is mixing or at least ergodic and assigns positive mass to every nonempty admissible cylinder. For any shift-invariant probability \(\nu\), the variational principle bounds \(h_\nu(\sigma)\) between \(0\) and \(\log2\); comparing the equilibrium pressure against the zero-potential-energy periodic probability gives \(\int d_\theta(s,P)\,d\nu_t\le(\log2)/t\). Therefore every weak-* limit as \(t\to\infty\) is supported on \(P\), and is its unique invariant equidistribution. Thus \(\nu_t\to\mu_P\).

The invariant one-dimensional unstable bundles for the planar and vertical variational blocks vary continuously on the compact trapped set (strict convexity, absence of grazing, and uniform hyperbolicity). Their one-step logarithmic expansion functions are continuous, so each line-bundle Lyapunov exponent equals its integral and depends continuously on the invariant probability. Strict inequalities at the two periodic measures consequently persist for sufficiently large *finite* values of \(t\). Choosing such a finite value for each periodic orbit produces the required two ergodic full-support Gibbs measures. No uniform ordering of these two physical subbundles over all Gibbs measures is possible.

## Verification

The included standalone `check_billiard.py` follows both explicit periodic rays, perturbs initial impact position and direction in each of the two invariant variational planes, and independently computes the four monodromy eigenvalue magnitudes by centered finite differences of exact quadratic ray/ellipsoid intersection and specular reflection. For \(\beta=11/10\), all four numerical per-collision exponents agree with the symbolic formulas to better than \(3\cdot10^{-6}\). The checker additionally tests closure of both rays and their opposite transverse ordering. Execute with `python check_billiard.py` (requires NumPy). Finite differences do not prove any all-parameter result; the curvature, matrix, and monotonicity derivation above does.

## Relationship to prior work

Al Dowais and Stoyanov (October 2, 2026) introduced the planar-centered ellipsoidal open-billiard family, coding, invariant planar/transverse splitting, and a **large-flattening sufficient condition** for positive separation in one orientation under Gibbs measures. Their result does not supply the opposite periodic-order examples for a single small-flattening parameter. Their displayed ellipsoid geometry yields the transverse equatorial curvature \(\beta^2/r\) by direct differentiation; this physical normalization is used throughout. Their earlier ball-obstacle study examines the spherical boundary, whereas here \(\beta>1\) and two spectral orders coexist.

Two previously published related research findings concern a coefficient-level repair of the *large-flattening* gap and a uniform two-term asymptotic for the *large-flattening* transverse top exponent. Neither establishes a small-flattening coexistence region, the explicit two-/three-cycle spectral crossing, or Gibbs measures with opposite planar/vertical ordering. Prior billiard linearization, symbolic coding, and Gibbs concentration principles are used as established tools, not claimed as innovations.

## Limitations

This theorem concerns the specified equilateral three-obstacle geometry and \(1<\beta<2/\sqrt3\), with exponents per collision. It does not classify every invariant measure or the maximal parameter range of mixed ordering. The proven contradiction is to *one uniform physical ordering of the planar versus vertical unstable lines*; no general theorem about every possible abstract dominated splitting is asserted. The periodic measures themselves lack full support, whereas the constructed finite-potential Gibbs measures have full support. Historical priority beyond the checked papers and records remains an acknowledged risk.

## References

1. A. Al Dowais and L. Stoyanov, *Some open billiards with distinct top Lyapunov exponents*, arXiv:2610.03004v1, first published October 2, 2026, https://arxiv.org/html/2610.03004v1; §§1–3 (particularly symbolic coding and Poincaré matrices).
2. A. Al Dowais and L. Stoyanov, *Lyapunov Exponents for Open Billiards in the Exterior of Balls*, arXiv:2306.03611, https://arxiv.org/abs/2306.03611 (scalar Poincaré linearization).
3. *Two-term large-flattening Lyapunov law for planar-trapped ellipsoidal billiards*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-two-term-large-flattening-lyapunov-law-for-planar-trapped-ellips--84cea797c5a4.
4. *A repaired Lyapunov-gap comparison for ellipsoidal open billiards*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-repaired-lyapunov-gap-comparison-for-ellipsoidal-open-billiard--f290e988fe0b.

# A sharp dimension-dependent negative center-mass law for finite spherical metric spaces

## Finding

Let the Euclidean space have dimension \(d\ge2\). Given any \(n\ge3\) distinct points \(V=\{x_1,\dots,x_n\}\subset RS^{d-1}\), where \(R>0\) and \(0\in\operatorname{conv}V\), add the center \(0\) as one more site. Define \(D_{ij}=\|x_i-x_j\|\). There is a unique signed vector \(p\in\mathbb R^n\) and scalar \(c\) with

\[
Dp=c\mathbf 1,\qquad \mathbf 1^\top p=1,
\qquad c=p^\top Dp.
\]

The normalized microscopic weighting of the \(n+1\) sites \(\{0\}\cup V\), in the sense of Roff and Willerton [1], is

\[
\boxed{ w_0=\frac{R-c}{2R-c},\qquad
w_i=\frac{R}{2R-c}p_i \quad (1\le i\le n).}
\]

The sharp dimension-dependent bounds are

\[
\boxed{R<c<C_dR,\qquad
\frac{1-C_d}{2-C_d}<w_0<0,}
\qquad C_d=\frac{2^{d-1}\Gamma(d/2)^2}{\sqrt\pi\,\Gamma(d-\tfrac12)}.
\]

Both endpoints of the interval for \(w_0\) are optimal as infimum and supremum over finite configurations satisfying the hypotheses, but neither is attained. In particular, \(C_2=4/\pi\), \(C_3=4/3\), and \(C_d\to\sqrt2\), so the sharp lower bound on center mass is \((\pi-4)/(2\pi-4)\) in the plane, \(-1/2\) in three-dimensional space, and tends to \(-1/\sqrt2\) with the ambient dimension.

## Assumptions and scope

All distances are ordinary **unsquared Euclidean chord distances** in \(\mathbb R^d\). We allow the rim weighting \(p\) to be signed, as is required by the microscopic-weighting definition. The origin belongs to the ordinary convex hull of the rim sites but need not lie in its interior. No symmetry, general-position, full-dimensionality, or positive-weight hypothesis is made for the rim set. There must be at least three distinct rim points; when the rim consists only of two antipodal points the center mass is zero instead. Microscopic weights are normalized to total mass one.

For a finite set \(Y\) with distance matrix \(D_Y\), a normalized microscopic weighting is the unique vector \(q\) satisfying \(\sum q_i=1\) and \(D_Yq=t\mathbf1\) for some scalar \(t\). It exists uniquely for the Euclidean sets here by strict negative type [1,2]. Equivalently it is the unique maximizer of signed distance energy \(q^\top D_Yq\) on the affine mass-one hyperplane [1].

## Proof

**1. Rim energy and existence.** The Euclidean chord-distance kernel is strictly conditionally negative definite on finitely many distinct sites [1,2]. Thus the energy \(E_V(q)=q^\top Dq\), restricted to \(\sum_iq_i=1\), is strictly concave, coercive along the zero-mass directions, and has a unique maximum \(p\). Its stationary equations give \(Dp=c\mathbf1\), with \(c=E_V(p)\).

**2. Exact center block identity.** The augmented distance matrix is

\[
D_X=\begin{pmatrix}0&R\mathbf1^\top\\R\mathbf1&D\end{pmatrix}.
\]

Seek its mass-one gauging in the form \(w=(a,bp)\), where \(a+b=1\). The center potential is \(Rb\), and every rim potential is \(Ra+bc\). Equality of these potentials gives \(Rb=Ra+bc\), so

\[
a=\frac{R-c}{2R-c},\qquad b=\frac{R}{2R-c}.
\]

The denominator will be shown strictly positive below. Uniqueness of the augmented Euclidean gauging proves these are exactly the microscopic weights. The augmented maximal energy is also \(R^2/(2R-c)\).

**3. Strict lower rim-energy bound.** Since \(0\in\operatorname{conv}V\), choose a convex combination \(q_i\ge0\), \(\sum_iq_i=1\), and \(\sum_iq_ix_i=0\). All pair distances lie between zero and \(2R\); hence \(t\ge t^2/(2R)\) for every pair distance \(t\). Consequently,

\[
E_V(q)\ge\frac1{2R}\sum_{i,j}q_iq_j\|x_i-x_j\|^2
=\frac{2R^2-2\|\sum_iq_ix_i\|^2}{2R}=R.
\]

If a pair of nonantipodal distinct sites has positive \(q_iq_j\), strict inequality holds. Otherwise the support of \(q\) consists of two antipodal sites \(\pm Ru\), each weighted \(1/2\), and \(E_V(q)=R\). Since there is a third site \(z\in V\) different from those endpoints, strict triangle inequality on the sphere gives

\[
\frac{\|z-Ru\|+\|z+Ru\|}{2}>R.
\]

The derivative of \(E_V((1-\varepsilon)q+\varepsilon\delta_z)\) at \(\varepsilon=0\) is therefore positive. In either case the maximum \(c\) is strictly larger than \(R\).

**4. Sharp uniform-sphere upper bound.** Let \(\sigma_R\) be normalized rotation-invariant surface measure on the radius-\(R\) sphere, and let \(\mu=\sum_i p_i\delta_{x_i}\), a signed measure of mass one. The spherical potential of \(\sigma_R\) is constant on the sphere, equal to \(C_dR\). The standard beta integral for \(\|x-y\|\) gives

\[
E(\sigma_R)=C_dR,
\qquad C_d=\frac{2^{d-1}\Gamma(d/2)^2}{\sqrt\pi\,\Gamma(d-\frac12)}.
\]

Put \(\nu=\mu-\sigma_R\), which has total mass zero. Since the cross potential \(\int\|x-y\|\,d\sigma_R(y)\) is constant for \(x\) on the sphere, expanding the energy yields

\[
E(\mu)=C_dR+E(\nu).
\]

For any nonzero finite signed mass-zero measure \(\nu\) supported in a bounded subset of Euclidean space, the strict negative-type identity

\[
E(\nu)=-\kappa_d\int_{\mathbb R^d}
\frac{|\widehat\nu(\xi)|^2}{\|\xi\|^{d+1}}\,d\xi<0,
\qquad\kappa_d>0
\]

follows by integrating the classical Fourier representation of \(\|x-y\|\). Here \(\mu\) is atomic while \(\sigma_R\) is nonatomic for \(d\ge2\), so \(\nu\ne0\). Thus \(c=E(\mu)<C_dR\). The mean-chord constant satisfies \(1<C_d<\sqrt2<2\), by the strict chord-versus-squared-chord inequality and Jensen's inequality. The already-derived block formula now implies \(2R-c>0\) and

\[
\frac{1-C_d}{2-C_d}<\frac{R-c}{2R-c}<0,
\]

because \((R-c)/(2R-c)\) decreases strictly with \(c\).

**5. Sharpness of both endpoints.** Fix \(d\ge2\) and choose distinct unit vectors \(u\) and \(v_\theta\) separated by an angle \(0<\theta<\pi\). For \(V_\theta=\{\pm Ru,\pm Rv_\theta\}\), the four rim points are transitive under isometries, so \(p_i=1/4\). The normalized rim concentration is

\[
\frac{c_\theta}{R}=\frac{2+\|u-v_\theta\|+\|u+v_\theta\|}{4}
=\frac{1+\sin(\theta/2)+\cos(\theta/2)}{2}
\longrightarrow1
\]

as \(\theta\downarrow0\). Therefore \(w_0\to0^-\). Conversely, take a sequence of finite, distinct antipodally symmetric sphere samples whose uniform empirical measures converge weakly to \(\sigma_R\); such samples exist by elementary equidistribution. Their uniform empirical energies tend to \(C_dR\). Their *maximum signed energies* \(c_m\) are at least these empirical energies and strictly less than \(C_dR\), so \(c_m\to C_dR\) and \(w_0\to(1-C_d)/(2-C_d)\). These limits prove both bounds sharp without unattained finite equality.

Finally, concentration of coordinate projections on a high-dimensional unit sphere gives \(C_d\to\sqrt2\) (or use the gamma quotient); substitution yields \((1-C_d)/(2-C_d)\to-1/\sqrt2\). This completes the proof.

## Verification

The standalone `verify.py` solves the mass-one distance gauging equations independently for the rim and its augmented center and checks the exact formulas and sharp bounds. It verifies 52 finite configurations (regular polygons, cross-polytopes, nearly overlapping antipodal pairs, and irregular clouds) and prints the dimension constants. The checker has no nonstandard Python dependencies. Its finite tests do not prove the universal theorem: that conclusion follows from the strict-negative-type, convex-combination, beta-integral, and endpoint arguments above.

Run: `python3 verify.py`.

## Relationship to prior work

Roff and Willerton [1], first publicly posted 6 July 2026, establish existence, uniqueness and signed-distance-energy optimization of the microscopic weighting on any finite Euclidean metric space. Those are the starting principles here, not new claims. Alexander and Stolarsky [2] established the related signed-distance-energy theory and sphere-uniform upper bounds. Their sphere extremal bound, and the classical Stolarsky principle [3], are used and credited; this finding does **not** claim a new solution of the classical sphere-distance-sum problem.

The additional claim proved here is the fully general sphere-plus-center *block gauging*, the strictly negative sign forced solely by a center-in-hull condition, the sharp ambient-dimension-dependent range of the center mass, and the distinct sharpness constructions at both endpoints. Hayden, Lee, Wells and Tarazaga [4] studied block structures for **squared** Euclidean-distance matrices. Their formulas do not directly give the unsquared chord-energy microscopic center weighting considered here. Priority assessment is provisional pending independent literature review.

## Limitations

The assumption \(0\in\operatorname{conv}V\) is essential for the universal negativity conclusion. For a two-site antipodal rim, the center weight is zero, explaining the \(n\ge3\) hypothesis. The theorem controls the center's weight, not the signs of individual rim weights, and does not determine the maximizer \(p\) for every irregular rim. The sharp extrema are approached but never attained by finite configurations. Generalization to non-Euclidean or geodesic sphere metrics, other distance powers, or arbitrary interior added sites is not asserted. No independent mathematical audit has been performed.

## References

1. E. Roff and S. Willerton, *The microscopic weighting on a metric space*, arXiv:2607.05349, first posted 2026-07-06, especially §§4–6. https://arxiv.org/html/2607.05349v2
2. R. Alexander and K. B. Stolarsky, *Extremal problems of distance geometry related to energy integrals*, Trans. Amer. Math. Soc. 193 (1974), 1–31, particularly §§3–4, DOI:10.1090/S0002-9947-1974-0350629-3. https://www.researchgate.net/publication/246156218_Extremal_Problems_of_Distance_Geometry_Related_to_Energy_Integrals
3. K. B. Stolarsky, *Sums of distances between points on a sphere II*, Proc. Amer. Math. Soc. 41 (1973), 575–582, as cited in [2].
4. T. L. Hayden, J. Lee, J. Wells and P. Tarazaga, *Block matrices and multispherical structure of distance matrices*, Linear Algebra Appl. 247 (1996), 203–216, DOI:10.1016/0024-3795(95)00100-X. https://www.academia.edu/109959117/Block_matrices_and_multispherical_structure_of_distance_matrices

# Strict covariance anisotropy and exact interface contributions for coaxial ball intersections

## Finding
Let \(d\ge2\) and let
\[
K=\bigcap_{i=1}^N\{(z,y)\in\mathbb R\times\mathbb R^{d-1}:(z-c_i)^2+\|y\|^2\le R_i^2\}
\]
be a full-dimensional intersection of finitely many Euclidean balls, where \(N\ge1\), every \(R_i>0\), and the centers \(c_i e_1\) are collinear. Neither equal radii nor symmetry of the centers is assumed. For a volume-uniform random point \(X=(Z,Y)\in K\), the covariance matrix has an axial eigenvalue \(v_{\parallel}=\operatorname{Var}(Z)\) and a transverse eigenvalue \(v_{\perp}=\operatorname{Var}(Y_j)\), repeated \(d-1\) times. Then
\[
\boxed{v_{\perp}\ge v_{\parallel},\quad
v_{\perp}=v_{\parallel}\ \Longleftrightarrow\ K\text{ is a Euclidean ball}.}
\]
There is an exact positive decomposition of the difference. Write the successive *effective* ball-center coordinates on the axial interval, from left to right, as \(a_0>a_1>\cdots>a_m\), with transition abscissae \(t_1<\cdots<t_m\). For each \(j\), set
\[
p_j=\Pr(Z\le t_j),\quad
\mu_{-,j}=\mathbb E[Z\mid Z\le t_j],\quad
\mu_{+,j}=\mathbb E[Z\mid Z>t_j].
\]
Then \(0<p_j<1\) and
\[
\boxed{v_{\perp}-v_{\parallel}
=\sum_{j=1}^{m}(a_{j-1}-a_j)p_j(1-p_j)(\mu_{+,j}-\mu_{-,j}).}
\]
Every term is strictly positive. The empty sum, occurring for one effective ball, is zero. In particular, the covariance condition number is \(v_{\perp}/v_{\parallel}>1\) for every nonball intersection.

## Assumptions and scope
The intersection has positive \(d\)-dimensional Lebesgue volume. All centers lie on one fixed Euclidean line, but the finite number of balls, their radii and the center coordinates are otherwise arbitrary. An effective ball is one whose sphere supplies the cross-sectional boundary on a nonempty *open* axial subinterval. Repeated or everywhere-redundant constraints are discarded, as are zero-length ties. When there is just one effective ball, the resulting body is that ball. The eigenvalues above are variances (moments divided by total volume), not moments of inertia about uncentered axes. All quantities and thresholds are real and exact.

The structural mechanism also applies to any disk-section rotational body with squared section radius \(f\), where \(f+z^2\) is concave and \(f\) is absolutely continuous on a compact interval, positive in its interior, and zero at its endpoints. The finite ball-intersection result and its discrete interface formula are the stated theorem.

## Proof
**1. Axial geometry and the lower envelope.** Define
\[
u=\max_i(c_i-R_i),\qquad v=\min_i(c_i+R_i).
\]
Full dimensionality is equivalent to \(u<v\). For \(z\in[u,v]\), the section perpendicular to the first coordinate is exactly the \((d-1)\)-ball of squared radius
\[
f(z)=\min_i\bigl(R_i^2-(z-c_i)^2\bigr)
=-z^2+g(z),\quad
 g(z)=\min_i\bigl(2c_i z+R_i^2-c_i^2\bigr).
\]
Thus \(f\) is continuous, positive on \((u,v)\), and vanishes at \(u,v\). A minimum of finitely many affine functions is concave, so \(g\) is concave and piecewise affine. Let \(C(z)=g'(z)/2\) at all non-breakpoint positions. This function is a nonincreasing step function; on the segment belonging to the ball centered at \(c_i e_1\), it equals \(c_i\), and
\[
f'(z)=2\bigl(C(z)-z\bigr)\quad\text{almost everywhere.}
\]
Hence the consecutive effective center coordinates strictly decrease; any affine pieces with equal slope are merged.

**2. Covariance slices.** Set \(q=(d-1)/2>0\), \(H=\int_u^v f(z)^q\,dz>0\), and \(\mu=H^{-1}\int_u^v z f(z)^q\,dz\). The axial marginal density of \(Z\) is \(f(z)^q/H\), since the omitted unit-ball volume constant cancels. Each uniform transverse \((d-1)\)-ball section has mean zero and coordinate variance \(f(z)/(d+1)\). Rotational symmetry therefore gives
\[
v_{\parallel}=\frac1H\int_u^v(z-\mu)^2f(z)^q\,dz,
\quad v_{\perp}=\frac1{(d+1)H}\int_u^vf(z)^{q+1}\,dz.
\]
All cross-covariances vanish, including the axial–transverse ones. The centroid of \(K\) is \((\mu,0,\ldots,0)\).

**3. Exact covariance identity.** Since \(d+1=2(q+1)\), the piecewise differentiability of \(f\) implies
\[
\frac{d}{dz} f(z)^{q+1}
=(d+1)\bigl(C(z)-z\bigr)f(z)^q
\quad\text{a.e. on }(u,v).
\]
Integrate \((z-\mu)\frac{d}{dz}f^{q+1}\) over all effective pieces. Internal boundary terms cancel by continuity, and both exterior boundary terms vanish because \(f(u)=f(v)=0\). Integration by parts yields
\[
\frac1{d+1}\int_u^v f(z)^{q+1}\,dz
=\int_u^v(z-\mu)\bigl(z-C(z)\bigr)f(z)^q\,dz.
\]
Consequently the exact, all-dimensional identity is
\[
\boxed{v_{\perp}-v_{\parallel}=-\operatorname{Cov}\bigl(Z,C(Z)\bigr).}
\]

**4. Positivity and strict rigidity.** If \(Z'\) is an independent copy of \(Z\),
\[
-2\operatorname{Cov}(Z,C(Z))
=\mathbb E\bigl[(Z-Z')(C(Z')-C(Z))\bigr]\ge0,
\]
because \(C\) is nonincreasing. The marginal density is strictly positive on the whole open interval \((u,v)\). If \(C\) is not constant on that interval almost everywhere, the displayed integrand is strictly positive on a positive-probability set of ordered pairs, so the gap is strict. Otherwise \(g\) is affine on \([u,v]\) and \(f(z)=R^2-(z-c)^2\) for some \(c\) and \(R>0\). Its two zeros are precisely \(u,v\); the sections reconstruct a complete Euclidean ball. Conversely, one ball has equal covariance eigenvalues \(R^2/(d+2)\). This proves the equality classification.

**5. Exact interface decomposition.** The active-center step function can be written, except at the measure-zero transition points,
\[
C(z)=a_0-\sum_{j=1}^m(a_{j-1}-a_j)\mathbf1_{\{z>t_j\}}.
\]
Inserting it in the covariance identity and observing that
\[
\operatorname{Cov}\bigl(Z,\mathbf1_{\{Z>t_j\}}\bigr)
=p_j(1-p_j)(\mu_{+,j}-\mu_{-,j})>0
\]
proves the claimed positive sum. Distinct effective intervals meet only at actual changes of active center, so every listed jump is positive and every conditional mean exists.

**6. A genuinely three-effective-ball example.** In \(\mathbb R^3\), take the centers at \(-1,0,1\) with radii \(2,\sqrt2,2\), respectively. The axial interval is \([-1,1]\), and its squared section radius is
\[
f(z)=\begin{cases}2-z^2,&|z|\le\tfrac12,\\
3-2|z|-z^2,&\tfrac12\le|z|\le1.
\end{cases}
\]
The active center coordinates move \(1\to0\to-1\). Exact polynomial integration gives
\[
\operatorname{vol}_3(K)=\frac{17\pi}{6},\quad
v_{\parallel}=\frac{139}{680},\quad
v_{\perp}=\frac{573}{1360},\quad
\boxed{v_{\perp}-v_{\parallel}=\frac{59}{272}}.
\]
Each of the two interfaces at \(z=\pm\tfrac12\) contributes exactly \(59/544\). This non-lens example witnesses that the decomposition is not confined to two-ball geometry.

## Verification
A standalone `verify.py` checks the exact three-ball volume, two covariance eigenvalues, positive gap, and the sum of its two interface contributions with symbolic rational integration. Independently, the program constructs the lower envelope for one ball, an unequal-radius two-ball lens, the three-ball example, and a four-effective-ball example. For dimensions \(2,3,4,5,7,9\), it integrates the sectional moments and checks both the covariance and interface expressions against them. **138 checks passed** in the supplied run. The universally quantified proof is the analytic lower-envelope and integration-by-parts argument; finite numerical experiments alone would not prove it. Run `python verify.py` with `sympy` and `mpmath` installed.

## Relationship to prior work
Bezdek's 2019 study treats Euclidean intersections of congruent balls and proves sharp volume, inradius and intrinsic-volume comparisons. It motivates the intersection geometry, but no covariance-axis inequality, equality classification, or additive active-interface formula is obtained there. Drach and Tatarko's 2023 study treats reverse isoperimetry and inradius for curvature-constrained bodies and the role of congruent-ball lenses; these valuations are distinct from covariance.

The previously published *Sharp covariance anisotropy law for symmetric Euclidean ball lenses* proves an exact positive gap and strict anisotropy growth for the intersection of **two equal-radius balls symmetrically placed**, in every dimension. That family is an explicit special case of the present statement and is **not claimed as new**. Its conclusions do not extend directly by symmetry to unequal radii or to three or more genuinely active coaxial spheres, where the centroid is generally not the midpoint and the active center is a many-step function. The contribution here is the full unequal-radius finite-intersection inequality, the equality classification and the exact multi-interface positive decomposition.

Diaz, Herrera and Martinez give classical generating-function moment-of-inertia integrals for general solids of revolution. These encompass the slice-integration technique, so slice integrals themselves are not claimed as new. The geometric deduction from a lower envelope of ball profiles to strict axis ordering and positive individual switch contributions is the additional result. Historical priority remains provisional: older mechanics treatments or unindexed results may contain equivalent sign laws.

## Limitations
The centers must be collinear, the balls Euclidean and the density uniform. No assertion is made for arbitrary noncollinear centers, a union or convex hull of balls, nonuniform densities, higher moments, or curvature-constrained bodies without the indicated squared-section-radius concavity. The formula gives an exact covariance gap but does not optimize it at fixed volume or classify bodies with a prescribed anisotropy ratio. The numerical checks are finite and supplemental. Independent mathematical validation has not been performed.

## References
1. Károly Bezdek, *Volumetric bounds for intersections of congruent balls*, arXiv:1912.05118v1, first public date 2019-12-11, especially §§1–2; https://arxiv.org/abs/1912.05118.
2. Kostiantyn Drach and Kateryna Tatarko, *Reverse isoperimetric problems under curvature constraints*, arXiv:2303.02294v1, first public date 2023-03-04; https://arxiv.org/abs/2303.02294.
3. Rodolfo A. Diaz, William J. Herrera and R. Martinez, *Moments of inertia for solids of revolution and variational methods*, arXiv:physics/0507172v1 (2005), and *European Journal of Physics* **27** (2006), 183; DOI:10.1088/0143-0807/27/2/001.
4. *Sharp covariance anisotropy law for symmetric Euclidean ball lenses*, published mathematical result (2026), identifier `dbb6d001c487`, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-covariance-anisotropy-law-for-symmetric-euclidean-ball-len--dbb6d001c487.

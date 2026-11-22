# A tricylinder endpoint law for the inradius of random unit-edge parallelotopes

## Finding
Let \(U_1,U_2,U_3\) be independent, surface-uniform unit vectors on \(S^2\subset\mathbb R^3\), and form the centered parallelotope
\[
P=\left\{\sum_{i=1}^3 t_iU_i:-\tfrac12\le t_i\le\tfrac12\right\}.
\]
Write \(R\) for its Euclidean inradius (the radius of the largest contained Euclidean ball). Then \(R\le1/2\), with equality precisely for an orthonormal generator triple, and
\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon^{-3/2}\Pr\{R>\tfrac12-\varepsilon\}
=\frac{16(2-\sqrt2)}{\pi}.}
\tag{1}
\]
This coefficient is approximately \(2.983385828624452\). Its geometric origin is the three-cylinder Steinmetz solid
\[
\mathcal S=\{(x,y,z)\in\mathbb R^3:x^2+y^2<1,\ x^2+z^2<1,\ y^2+z^2<1\},
\quad \operatorname{vol}(\mathcal S)=8(2-\sqrt2).
\tag{2}
\]
Define the three Gram off-diagonal coordinates
\[
a=U_1\cdot U_2,\qquad b=U_1\cdot U_3,\qquad c=U_2\cdot U_3.
\]
Conditioned on \(E_\varepsilon=\{R>1/2-\varepsilon\}\), the rescaled Gram vector
\[
X_\varepsilon=\frac{(a,b,c)}{2\sqrt\varepsilon}
\]
converges **in total variation** to a point uniformly distributed by three-dimensional Lebesgue volume on \(\mathcal S\). Moreover, the relative deficit \((1/2-R)/\varepsilon\), under the same conditioning, converges in distribution to \(\operatorname{Beta}(3/2,1)\). Each of the three opposite facet pairs is uniquely the closest pair to the center with probability exactly \(1/3\) (ties have probability zero).

The following integral is also an exact expression for the entire upper-tail probability at every \(0<r<1/2\). Put \(\Delta(a,b,c)=1-a^2-b^2-c^2+2abc\) and \(m(a,b,c)=\min(a^2,b^2,c^2)\). Then
\[
\Pr(R>r)=\frac1{4\pi}\int_{[-1,1]^3}
\frac{\mathbf1\{\Delta>4r^2(1-m)\}}{\sqrt\Delta}\,da\,db\,dc,
\tag{3}
\]
where the integrand is defined as zero when \(\Delta\le0\).

## Assumptions and scope
The three directions are independent and Haar-uniform on \(S^2\), not uniform in a ball; their lengths are fixed at one. The parallelotope is almost surely full-dimensional. Distances and balls are Euclidean in \(\mathbb R^3\). The inradius is the radius of a ball allowed to have any center; central symmetry and convexity ensure one of maximal radius can be centered at the origin. Statements involving strict versus weak endpoint inequalities are equivalent because the distribution has no positive atoms near \(1/2\). The parameter \(\varepsilon\) is a **length deficit**, not a relative volume deficit.

## Proof
**1. The exact inradius.** A face orthogonal to \(U_j\times U_k\), with \(\{i,j,k\}=\{1,2,3\}\), is at center-distance
\[
\frac12\frac{|\det(U_1,U_2,U_3)|}{\|U_j\times U_k\|}.
\]
Every contained ball must fit between each opposite face pair. The centered ball with the minimum of these three half-widths fits inside all six defining halfspaces, so equality is attained. As \(\|U_i\|=1\) and the squared Gram determinant is \(\Delta\), we obtain
\[
\boxed{2R=\sqrt{\frac{\Delta}{1-m}}.}\tag{4}
\]
Each altitude is at most one because it is the absolute inner product of a unit generator with a unit normal. Equality of all three altitudes requires each generator to be perpendicular to the other two; this proves the maximum and its complete equality classification.

**2. Exact Gram density.** By rotation invariance fix \(U_1\) at the north pole. Independently, \(a=U_1\cdot U_2\) and \(b=U_1\cdot U_3\) are uniform on \([-1,1]\). Conditional on them, the azimuthal difference \(\phi\) is uniform on \([0,2\pi)\), and
\[
c=ab+\sqrt{(1-a^2)(1-b^2)}\cos\phi.
\]
The two-to-one cosine change of variables gives exactly
\[
\boxed{f(a,b,c)=\frac{\mathbf1\{\Delta>0,\ |a|,|b|,|c|<1\}}{4\pi\sqrt\Delta}.}\tag{5}
\]
This is a normalized probability density by the spherical construction. Substituting (4) proves (3).

**3. Localization and the tangent region.** If \(R>1/2-\varepsilon\), each face altitude exceeds \(1-2\varepsilon\). A generator making absolute normal component at least \(1-2\varepsilon\) has inner product at most \(\sqrt{1-(1-2\varepsilon)^2}\le2\sqrt\varepsilon\) with either unit vector lying in the orthogonal face plane. Applying this to the three faces shows
\[
|a|,|b|,|c|\le 2\sqrt\varepsilon.
\tag{6}
\]
For \(a=2\sqrt\varepsilon x\), \(b=2\sqrt\varepsilon y\), \(c=2\sqrt\varepsilon z\), equation (4) and the exact equivalence \(R>1/2-\varepsilon\iff(2R)^2>(1-2\varepsilon)^2\) imply, uniformly on the bounded region (6),
\[
\frac{1-(2R)^2}{4\varepsilon}
=\max\{x^2+y^2,x^2+z^2,y^2+z^2\}+O(\sqrt\varepsilon).
\tag{7}
\]
The boundary of \(\mathcal S\) has three-dimensional measure zero. After rescaling, the indicators of \(E_\varepsilon\) therefore tend almost everywhere to \(\mathbf1_{\mathcal S}\); (5) tends uniformly to \(1/(4\pi)\) locally, and (6) gives one fixed compact dominating support. The dominated-convergence theorem gives
\[
\Pr(E_\varepsilon)\sim\frac{(2\sqrt\varepsilon)^3}{4\pi}\operatorname{vol}(\mathcal S).
\tag{8}
\]
The conditional rescaled densities converge in \(L^1\) (equivalently total variation) to \(\mathbf1_{\mathcal S}/\operatorname{vol}(\mathcal S)\), by the same domination and normalized convergence.

**4. The exact tangent volume.** There are 48 congruent signed ordered coordinate sectors. On \(x\ge y\ge z\ge0\), the three cylinder inequalities reduce to \(x^2+y^2<1\), \(0\le z\le y\). In polar coordinates \(x=t\cos\theta,y=t\sin\theta\),
\[
\operatorname{vol}(\mathcal S)
=48\int_0^{\pi/4}\int_0^1t^2\sin\theta\,dt\,d\theta
=16\left(1-\frac1{\sqrt2}\right)
=8(2-\sqrt2).
\]
Putting this into (8) yields (1).

**5. Conditional marks.** Equation (7) identifies the limiting rescaled deficit as
\(M(X)=\max\{X_1^2+X_2^2,X_1^2+X_3^2,X_2^2+X_3^2\}\) for \(X\) uniform on \(\mathcal S\). Since \(\{M(x)<t\}=\sqrt t\,\mathcal S\) for \(0\le t\le1\), its CDF is \(t^{3/2}\), establishing the beta law; it also follows immediately by taking the ratio of two instances of (1). The three closest opposite face pairs correspond to the smallest of \(a^2,b^2,c^2\); their labels are equiprobable by exchangeability, and ties have zero probability by (5).

## Verification
The standalone `verify.py` uses only the Python standard library. It computes the tricylinder integral by Simpson quadrature independently of its closed form, numerically compares the direct cross-product facet formula to the Gram-determinant formula on 2,000 spherical triples, and reproduces the tail constant and beta-mark prediction using a seeded 1,500,000-draw spherical-coordinate construction. It returns `ALL_CHECKS_PASSED`. The large-sample checks are diagnostic only; the exact volume integral and the domination argument, not simulation, prove the asymptotic and total-variation statements.

## Relationship to prior work
The archival paper by Alonso-Gutiérrez, Dafnis, Hernández Cifre and Prochno studies *mean outer radii* of many-point convex hulls sampled from isotropic bodies, with primary classification 52A22. Its observables and asymptotic regime do not give the inradius of a three-generator zonotope. The more directly related classical papers by Ruben (1979) and Mathai (1999) study random parallelotope **volume (content)**. The author-uploaded full text of Mathai's paper was inspected at the statement and development of its determinant-based results; it does not evaluate the smallest face altitude or the present inradius endpoint.

Indeed the volume does not even determine the inradius for unit-edge parallelotopes: the Gram triples \((\sqrt{13/125},0,0)\) and \((1/5,1/5,1/5)\) have the same determinant \(112/125\), but their inradii are respectively \(\frac12\sqrt{112/125}\) and \(\frac12\sqrt{14/15}\). Thus a volume distribution is not an equivalent formulation of (1).

The tricylinder itself and its volume are classical, and prior studies address its random **directional widths**. The proposed addition is that the *conditional Gram geometry* of nearly optimally inscribed random parallelotopes converges to this particular nonellipsoidal body, with a sharp normalized probability and beta radial deficit. The published extremal inradius result for degree-two lattice zonotopes concerns an integer-generator class and different length restrictions; it does not imply the unit-generator random law.

## Limitations
The result concerns precisely three independent, uniformly oriented, fixed-length generators in three dimensions. It gives the leading endpoint asymptotic, an exact three-fold integral for the full tail, and conditional limits; it does **not** provide an elementary closed-form CDF at every radius, a second asymptotic coefficient, high-dimensional analogues, or anisotropic sampling results. The full 1979 Ruben paper was not accessible in the available retrieval routes; only its published abstract and bibliographic record were available. A still-unknown older inradius theorem under parallelotope or random-frame terminology could affect historical priority. No independent mathematical audit has been performed.

## References
1. D. Alonso-Gutiérrez, N. Dafnis, M. Á. Hernández Cifre, J. Prochno, *On mean outer radii of random polytopes*, arXiv:1211.2336v1, first public 2012-11-10, primary MSC 52A22; *Indiana University Mathematics Journal* 63 (2014), 579–595.
2. H. Ruben, *The volume of an isotropic random parallelotope*, *Journal of Applied Probability* 16 (1979), 84–94, DOI: 10.2307/3213377 (accessible abstract, original full text not inspected).
3. A. M. Mathai, *Random p-content of a p-parallelotope in Euclidean n-space*, *Advances in Applied Probability* 31 (1999), 343–354, DOI: 10.1239/aap/1029955138 (author-uploaded full text inspected).
4. P. Bourke, *Intersecting cylinders*, discussion and construction of the three-cylinder intersection, March 1992, https://www.paulbourke.org/geometry/cylinders/.
5. *A unique tangential rhombohedron maximizes the inradius of degree-two lattice zonotopes*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-unique-tangential-rhombohedron-maximizes-the-inradius-of-degre--77b0eeb3cc1b (full RESULT text inspected for implications).

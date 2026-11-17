# Two pedal-area moments reconstruct every Euclidean triangle

## Finding

Let \(T\) be any nondegenerate Euclidean triangle of area \(\Delta\), circumcenter \(O\) and circumradius \(R>0\). Draw one point \(P\) uniformly from \(T\) with respect to normalized Euclidean area. Write \(H_1,H_2,H_3\) for the orthogonal projections of \(P\) onto the three **complete supporting lines** of the sides, and let

\[
Q=\frac{\operatorname{Area}(H_1H_2H_3)}{\Delta},\qquad
\mu=\mathbb E Q,\quad\nu=\mathbb E Q^2.
\]

**The exact pair \((\mu,\nu)\) determines the similarity class of \(T\), without any advance knowledge of its angles, size or circumradius. The first moment alone does not.**

Let \(s_1,s_2,s_3\) be the side lengths and define \(a_i=s_i^2/R^2\). Their elementary symmetric functions are

\[
e_1=a_1+a_2+a_3,\quad e_2=a_1a_2+a_2a_3+a_3a_1,\quad e_3=a_1a_2a_3.
\]

The forward and inverse relations are

\[
\boxed{\mu=\frac{e_1}{48},\qquad
\nu=\frac{e_1^2-e_2}{1440},\qquad e_3=4e_2-e_1^2,}
\]

\[
\boxed{e_1=48\mu,\quad e_2=(48\mu)^2-1440\nu,\quad e_3=4e_2-e_1^2.}
\]

The three roots (with multiplicity) of \(z^3-e_1z^2+e_2z-e_3=0\) are exactly the positive numbers \(s_i^2/R^2\). They therefore recover the side ratios and hence the similarity class, even for repeated side lengths.

For a sharp one-moment obstruction, the two nonsimilar isosceles triangles with normalized squared side triples

\[
\left(\frac72,\frac72,\frac74\right),\qquad
\left(\frac52,\frac52,\frac{15}4\right)
\]

both have \(\mu=35/192\), while their second moments differ.

## Assumptions and scope

Uniformity means normalized **area** within a fixed nondegenerate triangle, not a boundary sample or independent samples on its sides. The feet refer to complete straight lines, so feet outside the side segments are retained. Pedal-triangle area is unsigned, parent area \(\Delta>0\), and the observable is dimensionless. Similarity allows reflections and vertex permutation. All statements concern exact population moments. The circumcenter may lie outside an obtuse triangle; no assumption of acuteness is made. Since \(P\) is in the circumdisk, the normalized area \(Q\) is nonnegative (and at most \(1/4\)).

## Proof

**1. The classical area identity.** The classical pedal-area identity [1] states, for a point within the circumdisk,

\[
\frac{\operatorname{Area}(H_1H_2H_3)}{\Delta}
=\frac{R^2-\lVert P-O\rVert^2}{4R^2}.
\]

This also follows directly without invoking any distributional theorem. Every perpendicular projection onto a fixed line is affine-linear in \(P\), hence the oriented pedal area is a quadratic polynomial in the Cartesian coordinates of \(P\). By the Simson-line theorem it vanishes for every \(P\) on the circumcircle. Any real quadratic polynomial vanishing on a circle is a scalar multiple of its defining quadratic; at \(P=O\) the projections are the three side midpoints, whose triangle has area \(\Delta/4\). Therefore the ratio is the displayed polynomial. Its sign is positive in the circumdisk, giving the unsigned formula. This argument is valid even when \(O\) lies outside \(T\).

**2. Barycentric conversion.** Write \(P=\lambda_1v_1+\lambda_2v_2+\lambda_3v_3\), where \(v_i\) are the vertices. For normalized area sampling, \((\lambda_1,\lambda_2,\lambda_3)\sim\operatorname{Dirichlet}(1,1,1)\) on the simplex. Since the vertices satisfy \(\lVert v_i-O\rVert^2=R^2\), direct expansion of the square gives

\[
R^2-\lVert P-O\rVert^2
=\sum_{1\le i<j\le3}\lambda_i\lambda_j\lVert v_i-v_j\rVert^2.
\]

With \(a_1=\lVert v_2-v_3\rVert^2/R^2\) and cyclic indexing, it follows exactly that

\[
Q=\frac14\bigl(a_1\lambda_2\lambda_3+a_2\lambda_3\lambda_1+a_3\lambda_1\lambda_2\bigr).
\]

**3. Exact moment integration.** For nonnegative integers \(j_i\), the Dirichlet monomial rule is

\[
\mathbb E\prod_{i=1}^3\lambda_i^{j_i}
=\frac{2\prod_{i=1}^3j_i!}{(j_1+j_2+j_3+2)!}.
\]

Thus, for distinct indices, \(\mathbb E[\lambda_i\lambda_j]=1/12\), \(\mathbb E[\lambda_i^2\lambda_j^2]=1/90\), and \(\mathbb E[\lambda_i^2\lambda_j\lambda_k]=1/180\). Expanding the displayed expression for \(Q\) once and twice yields

\[
\mu=\frac{a_1+a_2+a_3}{48}=\frac{e_1}{48},
\]

\[
\nu=\frac1{1440}\left(\sum_i a_i^2+\sum_{i<j}a_ia_j\right)
=\frac{e_1^2-e_2}{1440}.
\]

No sampling or asymptotic approximation is involved in these identities.

**4. The circumcircle eliminates the third unknown.** Heron's formula, expressed in the squared side lengths \(s_i^2=R^2a_i\), gives

\[
16\Delta^2=R^4(4e_2-e_1^2).
\]

The elementary circumradius identity \(R=s_1s_2s_3/(4\Delta)\) independently gives \(16\Delta^2=R^4a_1a_2a_3=R^4e_3\). Therefore

\[
\boxed{e_3=4e_2-e_1^2.}
\]

The first two observed moments determine \(e_1,e_2\), and this geometric constraint determines \(e_3\). Vieta's formulas now reconstruct the multiset \(\{a_1,a_2,a_3\}\) as the roots of the stated cubic. Its roots are positive for actual nondegenerate triangles, and the side-side-side criterion reconstructs similarity uniquely. Neither repeated roots nor obtuse angles cause an exception.

**5. One moment cannot suffice.** Let an isosceles triangle have two base angles \(t,t\), with \(0<t<\pi/2\). The law of sines implies that its squared side lengths, normalized by squared circumradius, are

\[
\bigl(4\sin^2t,\ 4\sin^2t,\ 4\sin^2(2t)\bigr).
\]

Taking \(\cos^2t=1/8\) and \(\cos^2t=3/8\) produces the two triples in the Finding section. Both sum to \(35/4\), so both yield \(\mu=35/192\); however their second elementary symmetric functions are respectively \(49/2\) and \(25\), so the second moments differ. The triangles are nonsimilar (their normalized squared side multisets differ), which proves that two is the minimum length of an initial moment sequence sufficient for all triangles.

## Verification

The included standalone standard-library Python script `pedal_moment_check.py` verifies the Dirichlet-integrated first- and second-moment identities over exact rational coefficients. For three rational triangles (acute, right and obtuse), it independently computes circumcenters, circumradii, normalized squared side lengths and projections of four barycentric points onto the supporting side lines; it checks the pedal-area formula and \(e_3=4e_2-e_1^2\) using exact rational arithmetic. It also validates the explicit one-moment collision. Run `python3 pedal_moment_check.py`; successful output ends with `PEDAL_MOMENT_TOMOGRAPHY_CHECKS_OK`. These finite cases test implementations and complement, but do not substitute for, the all-triangle algebraic proof above.

## Relationship to prior work

Steggall [1] explicitly records the classical area ratio depending on squared distance to the circumcenter, and credits earlier geometric arguments. That relation is a **premise**, not claimed as new. Ganchev, Ahmed and Petkova [2] classify points with pedal triangles similar to their reference triangle; Castellano and Manack [3] study dynamical iterations of the pedal construction. Neither deals with the two area moments of one uniformly sampled interior point or their inverse shape information. Huang [4] derives distance-to-circumcenter and pedal-geometry inequalities for interior points, but no random-observation reconstruction theorem. Li and Qiu [5] analyze distance moments from a *vertex* to a random triangle point, not from the circumcenter and not the normalized pedal area.

In related published inverse geometry, *Three centroidal radial moments reconstruct every Euclidean triangle* (research record identifier `77120cadfb6f`, inspected in full) concerns squared distance to the **centroid**, and requires three even radial moments; its formulas do not imply the present two-moment reconstruction about the circumcenter. *Three area moments reconstruct a triangle from perimeter-uniform random inscribed triangles* (record `29f901c45c33`, inspected in full) uses three **boundary samples** and a different area observable. General shape inversion from multivariate moments [6] does not, from the accessible abstract alone, furnish this special two-scalar inverse. The claim here concerns only the two exact dimensionless pedal-area moments and their minimality, not the original pedal-area identity or a general polytope moment method.

## Limitations

The result uses **normalized** area ratios, rather than unnormalized pedal-triangle areas. It reconstructs triangle similarity, not overall scale. It requires a uniform interior point and Euclidean orthogonal projections. No statistical estimation accuracy, noise stability, full probability density, corresponding result for arbitrary convex polygons, or independent mathematical audit is claimed. The reference [1] article was printed in February 1893 (day not established in accessible evidence); its digitally verified public appearance is dated January 20, 2009, while other sources have day-precise dates. Historical priority of the exact two-moment inverse is provisionally assessed, and some general inverse-moment literature was accessible only in abstract.

## References

1. J. E. A. Steggall, *The pedal triangle*, Proceedings of the Edinburgh Mathematical Society 12 (February 1893), 85, DOI:10.1017/S001309150000170X, electronic posting dated 2009-01-20, https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/pedal-triangle/1AD2D7B7E3E9668F91A20EFAC9D3F833.
2. G. Ganchev, G. Ahmed and M. Petkova, *Points, whose pedal triangles are similar to the given triangle*, arXiv:1210.2929v1, first posted 2012-10-09, https://arxiv.org/abs/1210.2929.
3. C. Castellano and C. Manack, *Linear Triangle Dynamics: The Pedal Map and Beyond*, arXiv:1312.0281v1, first posted 2013-12-01, https://arxiv.org/abs/1312.0281.
4. F. Huang, *Two inequalities about the pedal triangle*, Journal of Inequalities and Applications (2018), article 72, DOI:10.1186/s13660-018-1661-7, https://link.springer.com/article/10.1186/s13660-018-1661-7.
5. H. Li and X. Qiu, *Moments of Distance from a Vertex to a Uniformly Distributed Random Point within Arbitrary Triangles*, 2016, DOI:10.1155/2016/8371750, https://onlinelibrary.wiley.com/doi/10.1155/2016/8371750.
6. G. H. Golub, P. Milanfar and J. Varah, *A Stable Numerical Method for Inverting Shape from Moments*, SIAM Journal on Scientific Computing 21 (1999), 1222–1243, DOI:10.1137/S1064827597328315.

# Fourth-order onset and Beta–Dirichlet shape law for four random spherical caps

## Finding

Let \(X_1,X_2,X_3,X_4\) be independent, normalized-area-uniform points on the unit sphere \(S^2\). Write \(p(\omega)\) for the probability that the four closed spherical caps of common angular radius \(\omega\), centered at these points, cover \(S^2\). Put
\[
\omega_0=\arccos(1/3),\qquad \delta=\frac13-\cos\omega.
\]
Then \(p(\omega)=0\) for \(\omega\le\omega_0\), and, as \(\omega\downarrow\omega_0\),
\[
\boxed{p(\omega)=\frac{81\sqrt3}{4\pi}\,\delta^4+o(\delta^4)
=\frac{16\sqrt3}{\pi}(\omega-\omega_0)^4+o((\omega-\omega_0)^4).}
\]
There is also a joint geometric limit for the rare covering event. Let \(h_i\) be the (positive) distance from the origin to the facet plane of the Euclidean tetrahedron \(\operatorname{conv}\{X_1,X_2,X_3,X_4\}\) opposite vertex \(X_i\). For sufficiently small positive \(\delta\), covering implies these four quantities are defined, with \(h_i\ge\cos\omega\). Define
\[
\alpha=\frac{(X_1\!\cdot\!X_2)+(X_3\!\cdot\!X_4)+2/3}{4},\quad
\beta=\frac{(X_1\!\cdot\!X_3)+(X_2\!\cdot\!X_4)+2/3}{4},\quad
Q=\alpha^2+\beta^2+(\alpha+\beta)^2,
\]
and \(y_i=h_i-\cos\omega\). Conditioned on covering, the jointly defined variables
\[
\left(\frac{Q}{2\delta},\ \frac{(y_1,y_2,y_3,y_4)}{y_1+y_2+y_3+y_4}\right)
\]
converge in distribution to independent \(\operatorname{Beta}(1,4)\) and \(\operatorname{Dirichlet}(1,1,1,1)\) random variables. Since the denominator is strictly positive almost surely, the displayed conditional ratio is well defined almost surely.

## Assumptions and scope

Only four independent identically distributed uniform surface points on \(S^2\) and congruent closed geodesic caps are considered. Angles lie in \((0,\pi/2)\) near \(\omega_0\). Degenerate tetrahedra have probability zero. All error estimates concern the limit from above of the optimal covering angle, with no claim of an exact formula for the entire intermediate angular range. The original definition of \(\alpha,\beta\) uses fixed vertex labels. Relabeling changes these coordinates, but their limiting transverse quadratic form has the required tetrahedral permutation symmetry; no exact label-invariance of the finite-deficit \(Q\) is asserted.

## Proof

**1. Coverage and the extremizer.** For \(0<\omega<\pi/2\), each cap is \(\{u\in S^2:X_i\cdot u\ge t\}\), \(t=\cos\omega>0\). The caps cover iff
\[
\min_{u\in S^2}\max_{1\le i\le4}X_i\cdot u\ge t.
\]
This is equivalent to containment of \(tB^3\) in the tetrahedron \(P=\operatorname{conv}\{X_i\}\); the support function comparison is exact for compact convex bodies. In particular, the origin is interior, and the support distances of the four facets are \(h_i\ge t\). Conversely the four facet inequalities imply containment of \(tB^3\). Euler's tetrahedral inradius–circumradius inequality \(r\le R/3\) gives \(\min_i h_i\le1/3\), because \(P\) has circumradius \(R\le1\) and the centered ball is not larger than its inball. Equality requires a regular tetrahedron inscribed in \(S^2\). The set of such ordered tetrahedra has zero probability. Compactness, plus uniqueness of the equality configurations up to rotation and chirality, localizes all covering events as \(t\uparrow1/3\) to neighborhoods of regular tetrahedra.

**2. Five coordinates and exact sampling density.** By rotational invariance take \(X_4=(0,0,1)\) and fix the azimuth of \(X_1\) to zero. Let \(\theta_1,\theta_2,\theta_3\) be the polar angles of \(X_1,X_2,X_3\) and \(\phi_2,\phi_3\) their relative azimuths. Their joint density with respect to five-dimensional Lebesgue measure is
\[
\frac{\sin\theta_1\sin\theta_2\sin\theta_3}{32\pi^2}.
\]
There are two regular tetrahedron configurations in this chart, at \(\theta_i=\arccos(-1/3)\), \((\phi_2,\phi_3)=(2\pi/3,4\pi/3)\) and the exchanged arrangement. In either branch, use the local coordinates
\[
(h_1,h_2,h_3,\alpha,\beta).
\]
For any triple of vertices indexing a face, let \(G\) be its \(3\times3\) Gram matrix. The supporting plane has distance
\[
h=(\boldsymbol1^T G^{-1}\boldsymbol1)^{-1/2}
\]
in the interior-facing neighborhood. At the regular tetrahedron every off-diagonal Gram entry equals \(-1/3\), so differentiation gives
\[
dh_i=\frac13\sum_{\{j,k\}\subset\{1,2,3,4\}\setminus\{i\}}d(X_j\cdot X_k).
\]
Differentiating the five new coordinates with respect to \((\theta_1,\theta_2,\theta_3,\phi_2,\phi_3)\) yields a nonsingular Jacobian of absolute determinant \(64\sqrt2/19683\). This determinant is also computed symbolically in `scripts/check.py`. Since \(\sin\theta_i=2\sqrt2/3\) at the reference configuration, the transformed probability density tends to
\[
J_0=\frac{729}{128\pi^2}
\]
at **each** of the two chirality branches.

**3. Quadratic transverse defect.** Put \(u_i=h_i-1/3\) for \(i=1,2,3\) and \(z=(\alpha,\beta)\). The first derivative of \(\sum_{i=1}^4h_i\) vanishes at regular tetrahedra: since \(\sum_i X_i=0\) there, differentiating \(\lVert\sum_i X_i\rVert^2=4+2\sum_{i<j}X_i\cdot X_j\) gives \(\sum_{i<j}d(X_i\cdot X_j)=0\); summing the four displayed height derivatives gives zero. The null space of the linearized four facet heights is two dimensional, and the above \(z\)-coordinates identify it. To evaluate its Hessian, use the actual disphenoid path with vertices
\[
(a,b,c),\quad(a,-b,-c),\quad(-a,b,-c),\quad(-a,-b,c),
\]
where \(a^2=1/3+\alpha\), \(b^2=1/3+\beta\), \(c^2=1/3-\alpha-\beta\). All four facet heights coincide, each equaling \((a^{-2}+b^{-2}+c^{-2})^{-1/2}\). The Taylor expansion therefore is
\[
h_i=\frac13-\frac12Q+O(|z|^3),\qquad
\sum_{i=1}^4h_i=\frac43-2Q+O(|z|^3)
\]
along this path. Because the gradient of the sum is zero, the same quadratic expression holds on the tangent kernel independently of the chosen path. Smooth Taylor expansion in the nonsingular chart gives
\[
\sum_{i=1}^4h_i=\frac43-2Q
+O(|u|^2+|u|\,|z|+|z|^3). \tag{1}
\]
This error is uniform in sufficiently small fixed neighborhoods of both regular tetrahedra.

**4. Uniform localization and integration.** Coverage is equivalent to \(h_i\ge1/3-\delta\). Hence \(u_i\ge-\delta\) for \(i=1,2,3\) and, by (1),
\[
\sum_{i=1}^3u_i+2Q\le\delta
+O(|u|^2+|u|\,|z|+|z|^3).
\]
Since \(\sum_i u_i\ge-3\delta\) and the coordinate neighborhood can be taken arbitrarily small by compactness, the remainder is bounded by an arbitrarily small multiple of \(|u|+Q\). Combining the preceding inequalities and \(u_i\ge-\delta\) first yields \(|u|\le C(\delta+Q)\), and then \(Q\le C'\delta\) and \(|u|\le C''\delta\) after absorbing the small multiple. It follows that the remainder in (1) is \(o(\delta)\), uniformly throughout the covering region. Therefore the four nonnegative slacks \(y_i=h_i-1/3+\delta\) obey
\[
\sum_{i=1}^4y_i=4\delta-2Q+o(\delta).
\]
Set \(z=\sqrt\delta\,Z\), \(y_i=\delta Y_i\), and apply dominated convergence in the resulting bounded domain. At fixed \(\alpha,\beta\), the leading domain for \((y_1,y_2,y_3)\) is a simplex of volume \((4\delta-2Q)^3/6\) if \(Q<2\delta\). As the matrix of \(Q=2\alpha^2+2\alpha\beta+2\beta^2\) has determinant \(3\), its ellipsoidal polar area element is \(\pi\,dQ/\sqrt3\). Thus the total leading five-dimensional coordinate volume is
\[
\int_{Q<2\delta}\frac{(4\delta-2Q)^3}{6}\,d\alpha\,d\beta
=\frac{\pi}{6\sqrt3}\int_0^{2\delta}(4\delta-2q)^3dq
=\frac{16\pi}{3\sqrt3}\delta^4.
\]
Multiplying by the two local densities gives
\[
2J_0\cdot\frac{16\pi}{3\sqrt3}=\frac{81\sqrt3}{4\pi}.
\]
Since \(\delta=\sin\omega_0(\omega-\omega_0)+O((\omega-\omega_0)^2)\) and \(\sin\omega_0=2\sqrt2/3\), its fourth power converts the constant into \(16\sqrt3/\pi\) in angular units.

**5. Conditional limits.** Normalize \(q=Q/(2\delta)\in[0,1]\). The radial Jacobian in \((\alpha,\beta)\) is constant in \(q\), while the available slack-simplex volume is proportional to \((1-q)^3\), so \(q\) has limiting density \(4(1-q)^3\), i.e. \(\operatorname{Beta}(1,4)\). Conditional on this \(q\), Lebesgue measure is uniform over the 3-simplex of nonnegative \((Y_1,Y_2,Y_3,Y_4)\) with \(\sum_iY_i=4(1-q)\). Normalizing by that sum gives \(\operatorname{Dirichlet}(1,1,1,1)\), independent of \(q\). The exceptional boundary \(q=1\) has measure zero.

## Verification

`python scripts/check.py` symbolically reconstructs the five-dimensional Jacobian determinant and leading constant, evaluates an independent numerical integral for the asymptotic volume, and compares the prediction with independent Haar samples of four sphere points. The Monte Carlo checks corroborate rather than prove the infinite-dimensional-looking limit: the proof is the finite-dimensional local Taylor expansion plus dominated convergence above. An exact pencil-and-paper Jacobian or symbolic differentiation can replace all code.

## Relationship to prior work

Finch's *Covering a Sphere with Four Random Circular Caps* (2015) explicitly asks for the previously unknown exact four-cap coverage probability below \(\pi/2\), and provides nontrivial lower estimates only at considerably larger angles. The present result is a **near-optimal-radius asymptotic**, not an exact expression for all intermediate radii. Bürgisser, Cucker and Lotz (2007/2010) treat the general spherical coverage process and exact probabilities for hemispherical and larger caps, plus bounds below hemisphere size. Brauchart and collaborators (2015) study random spherical covering principally as the point count grows. Euler's tetrahedral inradius–circumradius inequality and the definition of the covering threshold are classical and are not claimed as new.

## Limitations

Only the leading \(\delta^4\) coefficient and the stated conditional limits are proved; neither a finite-radius exact formula nor higher asymptotic coefficients are asserted. The conditional limit relies on fixed labels and the origin-containing tetrahedron, which is automatic on the near-threshold event. Although relevant full-text portions of the principal papers and searchable research records were compared, exhaustive historical priority is not established. Existing general geometric probability machinery may offer an alternative derivation. Independent mathematical review has not been performed.

## References

1. Steven R. Finch, *Covering a Sphere with Four Random Circular Caps*, arXiv:1502.06931v1 (first publicly posted 2015-02-24), https://arxiv.org/abs/1502.06931.
2. Peter Bürgisser, Felipe Cucker, Martin Lotz, *Coverage processes on spheres and condition numbers for linear programming*, arXiv:0712.2816v1 (2007-12-17); *Annals of Probability* 38 (2010), 570–604, https://arxiv.org/abs/0712.2816.
3. Johann S. Brauchart, Alexander B. Reznikov, Edward B. Saff, Ian H. Sloan, Yu Guang Wang, Robert S. Womersley, *Random Point Sets on the Sphere—Hole Radii, Covering, and Separation*, arXiv:1512.07470v1 (2015-12-23), https://arxiv.org/abs/1512.07470.
4. H. Maehara, *A threshold for the size of random caps to cover a sphere*, *Annals of the Institute of Statistical Mathematics* 40 (1988), 665–670, DOI 10.1007/BF00049424 (large-sample threshold, not fixed four-cap endpoint asymptotics).

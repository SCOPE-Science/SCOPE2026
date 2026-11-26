# Triangular joint width–brightness law and directional recovery for triaxial ellipsoids

## Finding

Let \(E\subset\mathbb R^3\) be a solid ellipsoid with pairwise distinct semiaxes \(a_1>a_2>a_3>0\). Choose a unit normal \(U\) uniformly from the Euclidean unit sphere. Let \(W(U)\) be the Euclidean width in direction \(U\), and let \(B(U)\) be the area of its orthogonal projection onto \(U^\perp\). Set
\[
X=(W/2)^2,\qquad Y=(B/\pi)^2,\qquad \lambda_i=a_i^2,\qquad D=\lambda_1\lambda_2\lambda_3.
\]
Write \(v_i=(\lambda_i,D/\lambda_i)\), let \(T=\operatorname{conv}\{v_1,v_2,v_3\}\), and define \(p_i(x,y)\) to be the barycentric coordinates of \((x,y)\) relative to its ordered vertices. Then the full joint law of the two physical measurements has support \(T\), and has the explicit two-dimensional density
\[
\boxed{f_{X,Y}(x,y)=\frac{\mathbf1_{\operatorname{int}T}(x,y)}{2\pi\,|\prod_{i<j}(\lambda_i-\lambda_j)|\sqrt{p_1(x,y)p_2(x,y)p_3(x,y)}}.}
\]
In particular, its density has integrable inverse-square-root divergences along each open edge of \(T\). Its law determines the unordered three semiaxes from the three support vertices. If the ellipsoid is known, one paired measurement at a generic orientation uniquely determines the three squared principal-axis components \(U_i^2\), hence determines exactly eight oriented normals (four unoriented lines), related by the ellipsoid's coordinate reflections.

There is also a strict exact anticorrelation identity for these **squared, normalized** geometric observables:
\[
\boxed{\operatorname{Cov}(X,Y)=-\frac{2D}{45}\sum_{1\le i<j\le3}\frac{(\lambda_i-\lambda_j)^2}{\lambda_i\lambda_j}<0.}
\]
The distinctness assumption is essential for a density with respect to planar Lebesgue measure. If exactly two semiaxes agree, the joint law lies on the segment joining the two distinct points \((\lambda,D/\lambda)\) and is the affine image of a \(\mathrm{Beta}(1/2,1)\) law, with its parameter assigned to the isolated axis. If all three agree, the joint law is a point mass.

## Assumptions and scope

The random normal is Haar-uniform on \(S^2\); the projection is orthogonal and the width and projection area are measured in **the same direction**. The axes are specified up to a rigid rotation, and all lengths and areas retain their physical units. The word *brightness* here means geometric projected area, not a scattering-law-dependent photometric intensity. The density concerns the transformed variables \(X\) and \(Y\); the distribution of the unsquared positive pair follows by the ordinary smooth monotone change of variables. The theorem is exact for every nondegenerate triaxial ellipsoid and contains no high-dimensional or small-eccentricity approximation.

## Proof

**1. Projection geometry.** Rotate to the principal-axis frame and write \(E=\operatorname{diag}(a_1,a_2,a_3)B_2^3\). Its support function is \(h_E(u)=\sqrt{\sum_i\lambda_i u_i^2}\), and central symmetry gives \(W(u)=2h_E(u)\). For an orthonormal \(3\times2\) matrix \(Q\) spanning \(u^\perp\), the projected ellipse has area \(\pi\sqrt{\det(Q^T\operatorname{diag}(\lambda_i)Q)}\). The complementary-minor identity yields
\[
\det(Q^T\operatorname{diag}(\lambda_i)Q)=D\sum_i\frac{u_i^2}{\lambda_i}.
\]
Consequently
\[
X=\sum_i\lambda_i u_i^2,\qquad Y=D\sum_i\lambda_i^{-1}u_i^2.
\]

**2. Exact distribution of squared direction coordinates.** Let \(G_i\) be independent standard real Gaussians and \(U=G/\|G\|\). Then \(P_i=U_i^2\) satisfy \(P_i>0\), \(\sum_i P_i=1\), and \((P_1,P_2,P_3)\sim\mathrm{Dirichlet}(1/2,1/2,1/2)\). Its density with respect to \(dp_1dp_2\) on \(p_1,p_2>0\), \(p_1+p_2<1\), is
\[
\frac{\Gamma(3/2)}{\Gamma(1/2)^3}(p_1p_2p_3)^{-1/2}=\frac1{2\pi\sqrt{p_1p_2p_3}}.
\]

**3. Full joint density and directional inverse.** The map from the open simplex to the two observables is affine:
\[
(X,Y)=p_1v_1+p_2v_2+p_3v_3.
\]
Its signed Jacobian, using \(p_3=1-p_1-p_2\), is
\[
\det(v_1-v_3,v_2-v_3)=-(\lambda_1-\lambda_2)(\lambda_1-\lambda_3)(\lambda_2-\lambda_3).
\]
Since all eigenvalues differ, the determinant is nonzero. The change-of-variables theorem proves the displayed density and normalization immediately. The coordinate functions \(p_i(x,y)\) are the unique affine inverse, which proves recovery of squared principal components; the signs of the three nonzero components are the only ambiguity at an interior point, and all eight sign assignments occur equally often. This also proves all support and singularity statements. The three noncollinear extreme points of the support have first coordinates \(\lambda_i\), so the **joint law** recovers each semiaxis without knowledge of individual viewing directions. The pair of observations carries enough independent information to localize an orientation modulo reflection symmetries.

**4. Exact strict anticorrelation.** Uniform-sphere moments give \(\mathbb E[P_i]=1/3\), \(\mathbb E[P_i^2]=1/5\), and \(\mathbb E[P_iP_j]=1/15\) for distinct indices. Put \(A=\sum_i\lambda_i\) and \(C=\sum_i\lambda_i^{-1}\). The formulas above imply
\[
\mathbb E[X]=A/3,\quad \mathbb E[Y]=DC/3,\quad
\mathbb E[XY]=D(AC+6)/15,
\]
so \(\operatorname{Cov}(X,Y)=-2D(AC-9)/45\). Expanding the product yields the identity
\[
AC-9=\sum_{i<j}\frac{(\lambda_i-\lambda_j)^2}{\lambda_i\lambda_j},
\]
which is positive precisely when the body is not a sphere. This proves the claimed exact strict sign; no assertion is made here about the covariance of the **unsquared** pair \((W,B)\).

**5. Repeated semiaxes.** If \(\lambda_1=\lambda_2=\lambda_\mathrm{rep}\ne\lambda_3=\lambda_\mathrm{solo}\), both observables depend solely on \(P_3=U_3^2\sim\mathrm{Beta}(1/2,1)\). The support is the line segment between the repeated-axis and isolated-axis vertices and the law on it is the corresponding affine beta pushforward. All equal semiaxes give a point mass. Thus the three regimes are exhaustive.

## Verification

The accompanying `check.py` independently constructs the paired observations from Gaussian-uniform spherical normals, inverts every observation back to squared principal coordinates, and compares Monte Carlo covariance with the exact rational identity on three different triaxial spectra. It also symbolically verifies the signed Vandermonde Jacobian and the sum-of-squares identity using SymPy. Those finite tests are diagnostic only: the proof is the analytic projection, Dirichlet pushforward, and finite algebra above.

## Relationship to prior work

The directional support and projected-area formulas for ellipsoids are classical; ellipsoidal brightness and shape recovery were already central to Muinonen and Lumme's 2015 geometric/photometric analysis. The new assertion here is the **two-observable joint distribution in a common Haar direction**, its triangular density, full directional fiber and singular support classification, together with the exact signed squared-observable covariance. Kim, Yaskin and Zvavitch (2015) formulate separate one-dimensional central-section and projection-area distribution functions and compare volumes; their Section 4 treats separate marginals and supplies no joint width–projection-area law. The 2026 published-finding corpus study *Endpoint tomography from paired sections and shadows of triaxial ellipsoids* concerns a **single scalar ratio** of shadow and section areas, equivalently a product of the present two observables; a one-dimensional product law cannot determine their two-dimensional joint law or individual conditional fibers. The 2026 work *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* addresses, as specified in its accessible abstract, polyhedral width/brightness marginals and cosine-transform reconstruction, not the triaxial smooth-body joint density developed here. An inaccessible full text can conceal additional results; historical priority therefore remains provisional.

## Limitations

The claims require exactly matched, perpendicular orthogonal-projection measurements in a common Haar-random direction. They neither cover independent directions nor arbitrary convex bodies. The sign formula concerns squared half-width and squared area normalized by \(\pi\), not unsquared covariance or photometric brightness. The triaxial density becomes singular as semiaxes coalesce; the limiting laws are supported in lower dimension. The theorem does not address sampling errors, finite-sample estimation or numerical stability of inverse support estimation. The originality review is same-model and independent verification has not been performed.

## References

1. K. Muinonen and K. Lumme, *Disk-integrated brightness of a Lommel–Seeliger scattering ellipsoidal asteroid*, Astronomy & Astrophysics 584 (2015), A23, first published online 2015-11-13. DOI: https://doi.org/10.1051/0004-6361/201526456 . Historical geometric ellipsoid formulas and shape-modelling context; photometric brightness is distinguished from geometric projected area.
2. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202 (2026). https://arxiv.org/abs/2609.26202 . Related width/brightness random-direction framework, primarily for polytopes.
3. *Endpoint tomography from paired sections and shadows of triaxial ellipsoids*, published-finding corpus (2026-10-18). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-endpoint-tomography-from-paired-sections-and-shadows-of-triaxial--e3183756e2e2 . Related but weaker one-dimensional ratio observable.
4. J. Kim, V. Yaskin and A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289 (first public 2015-12-22), https://arxiv.org/html/1512.07289v1 . Inspected full HTML text; separate section and projection marginal laws and volume comparison.
5. The Gamma–Dirichlet representation and uniform-sphere fourth moments are standard probability identities, derived or specified fully in the present proof.

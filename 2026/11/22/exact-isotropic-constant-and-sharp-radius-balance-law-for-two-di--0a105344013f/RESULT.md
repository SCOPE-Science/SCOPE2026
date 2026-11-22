# Exact isotropic constant and sharp radius-balance law for two-disc discotopes

## Finding

For two centered, noncoplanar Euclidean disks in \(\mathbb R^3\), the affine-invariant isotropic constant of their Minkowski sum has the exact shape law
\[
L(K)^6=\frac{(49-u^2)(11+u^2)}{110592\pi^2},\qquad u=\frac{a-b}{a+b}.
\]
It does not depend on the angle of the generating planes. Equal radii are the **unique** minimizers (up to common positive scaling), and the supremum is approached only when one radius becomes negligible. The exact deficit is
\[
L(K)^6-\frac{539}{110592\pi^2}=\frac{u^2(38-u^2)}{110592\pi^2}.
\]
In particular, the full sharp range is
\[
\frac{539}{110592\pi^2}\le L(K)^6 <\frac{1}{192\pi^2}.
\]

## Assumptions and scope

A Euclidean circular disk means the full closed two-dimensional ball in its plane. Let \(D_1,D_2\) be centered disks with radii \(a,b>0\), contained in two *distinct* linear planes in \(\mathbb R^3\). Their intersection line determines one common unit direction; the planes' acute angle is in \((0,\pi/2]\). Set \(K=D_1+D_2\), which is three-dimensional. If \(X\) is uniform on \(K\), define its covariance matrix \(\Sigma\). We use the conventional affine-invariant normalization \(L(K)^6=\det\Sigma/\operatorname{vol}_3(K)^2\). At equal radii, the minimum is attained at *every* permitted nonzero angle. The upper bound is a supremum, not an attained maximum among positive radii. Coplanar disks are excluded because the three-dimensional volume vanishes.

## Proof

**1. Reduction to mutually perpendicular disks.** Choose a unit vector \(e\) along the line shared by the two planes and respective unit directions \(v_1,v_2\) perpendicular to \(e\) in each plane. The invertible linear transformation sending the orthonormal triple \((e,e_2,e_3)\) to \((e,v_1,v_2)\) maps the sum of orthogonal disks with radii \(a,b\) to \(K\). Its determinant has absolute value \(\sin\theta>0\). For any invertible linear map \(T\), covariance transforms as \(T\Sigma T^\top\) and volume transforms by \(|\det T|\). Hence \(\det(T\Sigma T^\top)/(\operatorname{vol}(TK))^2=\det\Sigma/\operatorname{vol}(K)^2\). It suffices to compute in the orthogonal model.

**2. Volume and second moments in the orthogonal model.** In Cartesian coordinates put
\[
D_1=\{(x,y,0):x^2+y^2\le a^2\},\qquad D_2=\{(x,0,z):x^2+z^2\le b^2\}.
\]
For \(|y|\le a,\ |z|\le b\), the cross-section parallel to the \(x\)-axis is exactly \([-h(y,z),h(y,z)]\), where
\[
h(y,z)=\sqrt{a^2-y^2}+\sqrt{b^2-z^2}.
\]
Integrating the length \(2h\) gives \(V=2\pi ab(a+b)\). The independent sign symmetries force the centroid to be zero and the off-diagonal moments to vanish. Integrating \(x^2\), \(y^2\), and \(z^2\) in this exact cross-section yields
\[
\Sigma_{xx}=\frac{a^2+b^2}{4}+\frac{5ab}{12},\quad
\Sigma_{yy}=\frac{a^2(3a+4b)}{12(a+b)},\quad
\Sigma_{zz}=\frac{b^2(3b+4a)}{12(a+b)}.
\]
The required one-dimensional integrals are
\[
\int_{-r}^r(r^2-t^2)^{k/2}\,dt
=r^{k+1}\,B\!\left(\frac12,\frac k2+1\right)
\quad(k=0,1,2,3),
\]
and \(\int_{-r}^r t^2\sqrt{r^2-t^2}\,dt=\pi r^4/8\); substituting them into \(\int\!\int (2/3)h^3\,dy\,dz\), \(\int\!\int 2y^2 h\,dy\,dz\), and its \(z\)-analogue proves the displayed moment formulas for every \(a,b>0\).

**3. Affine-invariant quotient and sharp extrema.** By direct multiplication and division by \(V^2\),
\[
L(K)^6=\frac{(3a+4b)(4a+3b)(3a^2+5ab+3b^2)}{6912\pi^2(a+b)^4}
=\frac{(49-u^2)(11+u^2)}{110592\pi^2}.
\]
Writing \(z=u^2\in[0,1)\), the numerator becomes \(539+38z-z^2\), strictly increasing since its derivative is \(38-2z>0\). The minimum occurs precisely when \(u=0\), i.e. \(a=b\). The upper limiting numerator is \(576\) as \(z\to1\), but cannot be achieved at positive radii. Subtracting the minimum gives the exact deficit, completing all quantifiers and both endpoints.

## Verification

The separately supplied `check.py` derives the beta integrals by gamma-function identities, symbolically reconstructs all three covariance entries and the quotient, verifies its derivative, then independently performs four tensor-product Gaussian-quadrature calculations on \(160^2\) grid nodes, and twelve affine-angle determinant checks. Execute `python check.py` with Python, NumPy, and SymPy. The analytic argument, not the finite numerical checks, establishes the theorem for all positive radii and nonzero plane angles.

## Relationship to prior work

Gesmundo and Meroni introduced and analyzed discotopes as Minkowski sums of Euclidean disks and studied their algebraic boundaries and extreme points. Mathis and Meroni's study of fiber convex bodies includes sums of planar disks and computes zonoid/fiber-body information. Those examined results concern algebraic geometry and projections/fiber bodies, rather than the exact uniform-*interior* covariance determinant and its optimized ratio law. Extant indexed mathematical abstracts about extremal ellipsoids of two perpendicular disks concern John/Löwner ellipsoids, which alone do not specify the covariance of uniform interior points. The present statement is consequently a distinct shape invariant and complete radius-ratio classification, subject to the literature-access caveats below.

## Limitations

The formula is specific to exactly two Euclidean disks, not all summands or unequal eccentricities. It gives the affine-invariant isotropic constant, not the angle-dependent Euclidean inertia spectrum. Equal radii minimize only within the stated family. Direct inspection of some relevant indexed mathematical findings was limited to publicly available summaries; possible unindexed or inaccessible prior equivalent formulas remain a priority risk. No independent mathematical audit has yet been performed.

## References

- F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241 (first public posting 2021-11-01), https://arxiv.org/abs/2111.01241; *Le Matematiche* 77 (2022), 143–171, doi:10.4418/2022.77.1.8.
- L. Mathis and C. Meroni, *Fiber Convex Bodies*, *Discrete & Computational Geometry* 70 (2023), 1451–1475, https://doi.org/10.1007/s00454-022-00451-3 (online 2022-11-19).

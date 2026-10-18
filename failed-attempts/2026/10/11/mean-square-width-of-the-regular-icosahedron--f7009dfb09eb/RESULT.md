# Mean square width of the regular icosahedron
## Finding
Let \(I\subset\mathbb R^3\) be a regular icosahedron of edge length \(1\). If \(U\) is uniform on \(S^2\), then
\[
\mathbb E\,w_I(U)^2=\frac{5+\sqrt5}{6}+\frac{10\sqrt3}{3\pi}=3.043774314322605\ldots.
\]
Here \(w_I(u)\) is the distance between the two supporting planes perpendicular to \(u\).

## Assumptions and scope
Use the centered vertices
\[
\frac12(0,\pm1,\pm\phi),\quad \frac12(\pm1,\pm\phi,0),\quad \frac12(\pm\phi,0,\pm1),\qquad \phi=\frac{1+\sqrt5}{2}.
\]
These give edge length \(1\) and circumradius
\[
R^2=\frac{5+\sqrt5}{8}.
\]
Only the second directional-width moment is claimed; no full density or higher moment is evaluated.

## Proof
The icosahedron is centrally symmetric, so \(w_I(u)=2h_I(u)\). The sphere splits into twelve congruent vertex-normal cells. Fix one vertex \(v\), put \(n=v/R\), and let \(C\) be its cell. If \(\theta\) is spherical distance from \(n\), then on \(C\),
\[
h_I(u)=R\cos\theta.
\]
For an adjacent vertex \(v'\), the corresponding side of \(C\) is \((v-v')\cdot u=0\). If \(\delta\) is the spherical distance from \(n\) to this side, then, since \(\lVert v-v'\rVert=1\) and \(v\cdot v'=R^2-1/2\),
\[
\sin\delta=\frac1{2R},\qquad \sin^2\delta=\frac{5-\sqrt5}{10},\qquad \cos^2\delta=\frac{5+\sqrt5}{10}.
\]
The cell is a regular spherical pentagon. Put \(\alpha=\pi/5\). In one of its five congruent sectors, using polar coordinates centered at \(n\), the boundary great circle is
\[
\tan\theta_b(\psi)=\frac{\tan\delta}{\cos\psi},\qquad -\alpha\le\psi\le\alpha.
\]
Therefore
\[
\int_C\cos^2\theta\,d\sigma=\frac53\left(2\alpha-J\right),
\]
where
\[
J=\int_{-\alpha}^{\alpha}\frac{\cos^3\psi}{(\cos^2\psi+\tan^2\delta)^{3/2}}\,d\psi.
\]
With \(x=\sin\psi\) and \(A=\sec^2\delta\), an antiderivative is
\[
\arcsin\left(\frac{x}{\sqrt A}\right)+(1-A)\frac{x}{A\sqrt{A-x^2}}.
\]
Since
\[
\sin^2\alpha=\frac{5-\sqrt5}{8},\qquad \sin\alpha\cos\delta=\frac12,
\]
one obtains
\[
J=\frac\pi3-\frac{2\sin^2\delta}{\sqrt3}
\]
and hence
\[
\int_C\cos^2\theta\,d\sigma=\frac\pi9+\frac{10}{3\sqrt3}\sin^2\delta.
\]
Summing the twelve cells gives
\[
\mathbb E\,w_I(U)^2=\frac{12R^2}{\pi}\int_C\cos^2\theta\,d\sigma
=\frac{4R^2}{3}+\frac{40R^2\sin^2\delta}{\pi\sqrt3}.
\]
Finally \(4R^2\sin^2\delta=1\), which yields
\[
\mathbb E\,w_I(U)^2=\frac{5+\sqrt5}{6}+\frac{10\sqrt3}{3\pi}.
\]

## Verification
The bundled `verify.py` reconstructs the twelve vertices over \(\mathbb Q(\sqrt5)\), verifies the thirty unit edges and degree five at every vertex, checks the exact radius and inradius identities, and independently evaluates the spherical-sector integral by deterministic quadrature. The quadrature is a regression check only; exactness follows from the antiderivative above.

## Relationship to prior work
Finch's 2011 paper *Width Distributions for Convex Regular Polyhedra* computes the same second moment for the regular tetrahedron and cube and explicitly invites analogous computations for other convex bodies; its full text contains no icosahedral calculation. Kabluchko, Litvak, and Zaporozhets later proved a general higher-moment Sudakov formula and gave explicit applications for cubes, simplices, and crosspolytopes; their full text contains no icosahedron or dodecahedron. Targeted searches for the icosahedral mean square width, the equivalent random projection-length moment, the exact radical expression, and its decimal value did not locate a prior evaluation.

## Limitations
Only the second moment is evaluated. A differently phrased or unindexed classical stereological calculation could contain the same value; the inspected regular-polytope literature and exact-constant searches did not reveal one.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, 4 October 2011.
2. Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, 26 November 2015.

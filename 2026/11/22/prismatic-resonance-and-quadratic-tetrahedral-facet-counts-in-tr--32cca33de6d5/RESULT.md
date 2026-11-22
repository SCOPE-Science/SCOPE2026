# Prismatic resonance and quadratic tetrahedral facet counts in triangular containment duals

## Finding
For each integer \(n\ge3\), put \(\zeta=e^{2\pi i/n}\) and \(\omega=e^{2\pi i/3}\), and define
\[
D_n=\operatorname{conv}\bigl\{(\omega^j\zeta^k,\zeta^k):0\le j\le2,\ 0\le k<n\bigr\}\subset\mathbb C^2.
\]
All facets of this four-polytope are tetrahedra or triangular prisms. The exact number of triangular prisms is
\[
N_{\mathrm{prism}}(n)=\begin{cases}2n,&3\mid n,\\ n,&3\nmid n.\end{cases}
\]
The number of tetrahedral facets with two vertices from each of exactly two component regular polygons is
\[
N_{2+2}(n)=3n\left\lfloor\frac{n-1}{3}\right\rfloor.
\]
The polar is, after a positive diagonal rescaling and a linear change of rotation coordinates, the similarity-containment polytope for an equilateral triangle within a regular \(n\)-gon. This is a complete classification of *nonsimplicial facets* and an exact count of the specified quadratic-size tetrahedral family, not a complete face-vector determination.

## Assumptions and scope
The complex plane is identified with the real plane and \(\mathbb C^2\cong\mathbb R^4\), with real-linear support functionals. Set \(P_j=\{(\omega^j\zeta^k,\zeta^k):0\le k<n\}\), for \(j=0,1,2\). Each \(P_j\) is a regular planar \(n\)-gon. Distinct supporting planes of \(P_j\) meet only at the origin and jointly span all four dimensions. Consequently, the origin is interior to \(D_n\). Every point displayed in the construction is an extreme point, since all have equal Euclidean norm and the Euclidean ball is strictly convex. A *facet* is a three-dimensional exposed face. An edge of \(P_j\) consists of two cyclically consecutive vertices.

## Proof
**1. Dual support geometry.** Write a real-linear functional as \(L_{a,b}(z,t)=\operatorname{Re}(az+bt)\), with complex coefficients \(a,b\). Its value on \(P_j\) is \(\operatorname{Re}(w_j\zeta^k)\), where \(w_j=b+a\omega^j\). The triple satisfies
\[
w_0+\omega w_1+\omega^2w_2=0.
\]
Let \(W\) denote the regular \(n\)-gon of circumradius one, with vertices the outward normal coefficients for edges of \(\operatorname{conv}\{\zeta^k\}\). Thus \(W\) has vertices \(u_k=e^{-i(2k+1)\pi/n}\). The support of the source polygon in direction \(w\) is at most \(\cos(\pi/n)\) precisely when \(w\in W\). If an edge is maximized, \(w\) is a positive multiple of one of the \(u_k\); choosing the supporting value to be \(\cos(\pi/n)\) forces \(w=u_k\). For every nonzero facet functional, the maximum is positive because zero is interior. A touched \(P_j\) contributes either one vertex or two adjacent vertices, since the functional cannot vanish identically on \(P_j\) at positive support height. A facet must therefore touch at least one component edge.

**2. Discrete equilateral-apex lemma.** Fix two components, cyclically relabeled \(0\) and \(1\). If their corresponding directions are edge-support vertices \(w_0=u_k\), \(w_1=u_l\), the third direction forced by the linear relation is
\[
w_2=e^{-\pi i/3}w_0+e^{\pi i/3}w_1.
\]
Writing \(m\in\{0,\ldots,n-1\}\) for the directed circular difference of the arguments of \(w_1,w_0\), one has, up to common rotation,
\[
w_2=2\cos\left(\frac{\pi m}{n}+\frac\pi3\right)e^{\pi i m/n}.
\]
This point belongs to \(W\) if and only if \(0\le m\le n/3\). It lies in the *interior* of \(W\) if and only if \(0<m<n/3\), and on the boundary otherwise (where \(m=n/3\) is possible only if \(3\mid n\)). To check the assertion, put \(t=\pi/n\). For \(0<m\le n/6\), the displayed radial coefficient is positive. At angle \(mt\), the radial boundary of \(W\) is either one or \(\cos t\), according to the parity of \(m\); the coefficient is strictly below the appropriate boundary because \(2\cos(\pi/3+mt)<1\), and for odd \(m\), \(2\cos(\pi/3+mt)\le2\cos(\pi/3+t)=\cos t-\sqrt3\sin t<\cos t\). For \(n/6<m<n/3\), the radial coefficient is negative; its absolute value equals \(\cos\delta-\sqrt3\sin\delta\), where \(\delta=\pi/3-mt\ge t/3\) whenever the endpoint is not an integer index. It is strictly below one, and it is below \(\cos t\) using
\[
\cos t-\bigl(\cos(t/3)-\sqrt3\sin(t/3)\bigr)
=\bigl(\sqrt3-2\sin(2t/3)\bigr)\sin(t/3)>0.
\]
For \(m=n/3\), the point is another vertex of \(W\); for \(m>n/3\), its modulus exceeds one, so it is outside \(W\). At \(m=0\) it equals the common vertex. This verifies all boundaries, including odd \(n\), since a radial boundary is always either one or \(\cos t\) at an angle which is an integral multiple of \(t\), whether the coefficient is positive or negative.

**3. Two-component edge facets.** The pair of adjacent vertices in each of two distinct \(P_j\)'s spans a three-dimensional tetrahedron (two nonparallel edges in complementary two-planes). It is a facet exactly when the remaining \(w_j\) belongs to \(W\); it contains no vertex of the remaining component precisely for strict inclusion. By the lemma this means \(1\le m\le\lfloor(n-1)/3\rfloor\). For each of three component pairs and each of \(n\) starting edges, precisely that many directed offsets qualify; no facet is counted twice because its group-incidence pattern is unique. Hence the tetrahedral count above.

**4. Prismatic facets and exclusion of five-vertex facets.** A facet with at least five vertices must touch edges of at least two component polygons, together with a vertex or an edge of the third. The strict-interior part of the lemma excludes this unless \(m=0\) or \(m=n/3\). In either endpoint case the third component also contributes an *edge*, not merely one vertex, because its support direction is a vertex of \(W\). Thus every nonsimplicial facet has precisely two adjacent vertices from each component. Conversely each such simultaneous triple-edge contact gives a three-dimensional triangular prism: for \(m=0\), all three edges project to the same edge in the second complex coordinate, while for \(m=n/3\), they project to the same edge in the first complex coordinate. Their six endpoints span a triangular prism. There are \(n\) choices of shared edge for the first case. In the second case (possible only for \(3\mid n\)) there are another \(n\), and the two families differ since the support is respectively \(a=0\) or \(b=0\). There are no other nonsimplicial facets. Since every facet has at least four vertices, every remaining one is necessarily a tetrahedron.

## Verification
A standalone Python 3 standard-library checker, `verify_facets.py`, tests all supporting edge pairs and triple edge contacts for every integer \(3\le n\le80\), directly evaluating the original four-dimensional support inequalities. Those finite tests corroborate, but do not replace, the all-dimensional proof. See `VERIFICATION.md` for commands and exact scope.

## Relationship to prior work
Choi and Choi introduced and analyzed the four-dimensional triangle-in-polygon similarity-containment polytope and proved complexity/algorithmic results for its maximal-placement silhouette. Their general-position assumptions do not cover all regular polygons, and the inspected primary text does not give the above exact dual-facet classification. Published work on largest inscribed equilateral triangles in regular polygons addresses global scale optimizers, not every facet of the full placement polytope. The proof here instead uses the complete exposed-face structure of three coupled regular polygons in four dimensions.

## Limitations
The formula \(N_{2+2}(n)\) counts only tetrahedra having the indicated two-component incidence pattern; some other tetrahedra have pattern \(2+1+1\). The result does not supply their number, the total number of tetrahedral facets, or a complete face vector. The novelty comparison against unindexed or inaccessible prior geometry remains provisional. No independent audit has been performed.

## References
- Y. Choi and S. Choi, *The Containment Polytope of a Triangle and a Convex Polygon*, arXiv:2611.08556, first posted 2026-11-05, https://arxiv.org/abs/2611.08556 .
- Related published record: *Sharp largest equilateral triangles in every regular polygon*, published-finding corpus (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-largest-equilateral-triangles-in-every-regular-polygon--b61be1edd78b .

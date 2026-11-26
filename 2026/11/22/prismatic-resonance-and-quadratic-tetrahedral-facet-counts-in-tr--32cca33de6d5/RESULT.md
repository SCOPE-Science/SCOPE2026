# Octahedral resonance and two-edge tetrahedral facet counts in triangular containment duals

## Finding

Let \(n\ge 3\), \(\zeta=e^{2\pi i/n}\) and \(\omega=e^{2\pi i/3}\), and set
\[
D_n=\operatorname{conv}\{(\omega^j\zeta^k,\zeta^k):0\le j\le2,\ 0\le k<n\}\subset\mathbb C^2\cong\mathbb R^4.
\]
Every nonsimplicial facet has exactly six vertices. There are \(n(1+\mathbf1_{3\mid n})\) such facets. For \(n=3\) all six are triangular prisms; for every \(n\ge4\) they are octahedra (combinatorial triangular antiprisms), and there are no triangular-prism facets. Every other facet is a tetrahedron. The number of tetrahedral facets with two vertices in each of exactly two distinct component polygons is
\[
3n\left\lfloor\frac{n-1}{3}\right\rfloor.
\]
Up to scaling and a real-linear coordinate identification, \(D_n^\circ\) is the similarity-containment polytope of an equilateral triangle inside a regular \(n\)-gon.

## Assumptions and scope

The component polygons have vertex sets \(P_j=\{(\omega^j\zeta^k,\zeta^k):0\le k<n\}\). A facet is a three-dimensional exposed face; the names of the facet types refer to combinatorial type. The two-edge count does not include tetrahedra with component incidence \(2+1+1\).

## Proof

**Support and polarity.** The three component planes \(z=\omega^j t\) are complementary in pairs, and the origin is in the relative interior of each polygon. The convex hull of any two component polygons therefore contains a neighborhood of zero. Every displayed point is a vertex, since the points are distinct and have the same Euclidean norm. Write a real support functional as \(\operatorname{Re}(az+bt)\), with \(a,b\in\mathbb C\), and put \(w_j=b+a\omega^j\). These are precisely the triples satisfying \(w_0+\omega w_1+\omega^2 w_2=0\). Define \(h=\cos(\pi/n)>0\), and let \(W\) be the regular polygon with vertices \(u_k=e^{-(2k+1)\pi i/n}\). The inequalities \(\operatorname{Re}(w\zeta^k)\le h\) for all \(k\) describe \(W\): consecutive inequalities have intersections at the \(u_k\) (with cyclic indexing). At height \(h\), a component contributes no vertices if \(w_j\in\operatorname{int}W\), one vertex on the relative interior of an edge of \(W\), and two consecutive vertices at a vertex of \(W\). The normalized polar constraints are exactly \(b+a\omega^j\in W\) for all \(j\). By convexity, these say that the equilateral triangle with vertices \(b+a\omega^j\) is contained in \(W\), with \(a=0\) allowed as the zero-scale limit.

**Two edge contacts.** Cyclically relabel the components so that the pair in question is \((0,1)\). Set \(w_0=u_k\) and \(w_1=w_0 e^{2\pi i m/n}\), with \(0\le m<n\). The remaining direction is
\[
\frac{w_2}{w_0}=e^{-\pi i/3}+e^{\pi i/3}e^{2\pi i m/n}
=2\cos\bigl(\pi/3+m\pi/n\bigr)e^{i m\pi/n}.
\]
Write \(t=\pi/n\). If \(0<m<n/3\), then \(\delta=\min(mt,\pi/3-mt)\ge t/3\), since \(m\) and \(n-3m\) are positive integers. The modulus is \(2\cos(\pi/3+\delta)\), at most \(\cos(t/3)-\sqrt3\sin(t/3)\). It is strictly smaller than \(\cos t\), since the difference is \((\sqrt3-2\sin(2t/3))\sin(t/3)>0\) for \(n\ge3\). As \(\cos t\) is the inradius of \(W\), this puts \(w_2\) strictly inside \(W\). For \(m>n/3\), the modulus exceeds one. At \(m=0\), all three directions coincide; at \(m=n/3\) (when integral), the triple is \((w_0,\omega w_0,\omega^2 w_0)\). In both endpoint cases \(w_2\) is a vertex of \(W\).

Four vertices comprising an edge in each of two components are affinely independent: the two edge endpoint vectors in each of the complementary planes are linearly independent, so all four vectors together are linearly independent. Thus they span a tetrahedral facet with no contribution from the third component exactly for \(1\le m\le\lfloor(n-1)/3\rfloor\). Each of the three pairs and each of the \(n\) choices of first edge contributes this many distinct facets. Every facet with five or more vertices has at least two edge contacts. The preceding dichotomy rules out exactly five vertices, and the endpoints give all six-vertex facets. There are \(n\) with a common direction (\(a=0\)) and, if \(3\mid n\), another \(n\) with \(b=0\). These are disjoint families since the supporting functional is nonzero and unique up to positive scale for a facet. All other facets have exactly four vertices and are tetrahedra.

**Combinatorial type of the six-vertex facets.** In the \(a=0\) family, the exposed edge in the second coordinate has endpoints \(x=\zeta^k\), \(y=\zeta x\). The six vertices are \((\omega^j x,x)\) and \((\omega^j y,y)\), for \(0\le j\le 2\). In the affine hull of the facet, identify the free complex first coordinate with a horizontal plane and the edge from \(x\) to \(y\) in the second coordinate with height. There are two parallel equilateral triangular caps, and the upper cap is rotated by \(2\pi/n\). In the \(b=0\) family, the first and second coordinates switch roles: at a fixed first-coordinate edge endpoint \(x\) the other coordinates form \(\{\omega^{-j}x:0\le j\le2\}\), which are available because \(3\mid n\). Thus the two families have the same cap description.

For \(n=3\) the cap rotation is a symmetry of the triangle, and the convex hull is a triangular prism. For \(n\ge4\), the two sets of horizontal outward edge normals are disjoint and alternate around the circle, since they are equally spaced by \(2\pi/3\) and rotated relative to one another by a strictly intermediate angle. Every facet of this three-dimensional hull other than the two caps crosses the two height levels. Its nonzero horizontal normal must support an edge in one cap and a vertex in the other, since there is no common edge-normal ray; two supported vertices alone would not span a two-dimensional face. Conversely each edge-normal ray gives such a triangular face by choosing the vertical normal coefficient to equalize support heights. Each vertex lies on its cap, on two side triangles from its own incident edges, and on exactly one side triangle from the other cap: its open horizontal vertex-normal sector contains exactly one edge normal of that other cap. Hence all eight faces are triangles, and the degree of every vertex is four. The graph on the six vertices is the complement of a perfect matching. The eight triangular faces are exactly the eight triples choosing one vertex from each matched pair, so the combinatorial type is the octahedron.

## Verification

The proof is for every integer \(n\ge3\). The companion `verify_facets.py` checks support on the original polygon vertices for each candidate two-edge contact over \(3\le n\le80\), and checks the cap-based face counts and the vertex degrees of each of the corresponding combinatorial types. The finite numerical cross-check does not replace the proof. As a concrete example, the \(a=0\) facet of \(D_4\) above the edge from \(1\) to \(i\) has its caps rotated by \(\pi/2\) and hence has six triangular side faces, not three quadrilateral side faces.

## Relationship to prior work and limitations

The similarity-containment interpretation belongs to the setting of Y. Choi and S. Choi, *The Containment Polytope of a Triangle and a Convex Polygon*, [arXiv:2611.08556](https://arxiv.org/abs/2611.08556); their silhouette analysis assumes general position, including restrictions on concurrent contacts. The additional assertions here are the facet types and exact counts for the equilateral/regular family. The finding [*Sharp largest equilateral triangles in every regular polygon*](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-sharp-largest-equilateral-triangles-in-every-regular-polygon--b61be1edd78b/RESULT.md) classifies the maximum-scale placements. When \(3\mid n\), its \(n/3\) geometric maximizing triangles are the \(b=0\) family, with three rotation parameters per geometric triangle; that maximizer count does not classify all six-contact placements or their dual facet types. The \(a=0\) family is at zero scale, and the two-edge count allows the third triangle corner to be strictly inside. When \(3\nmid n\), there is also a finite trigonometric orbit formulation: with \(x=\omega^j\zeta^k\), the point set is \((x,x^q)\) for \(x^{3n}=1\) and \(q\equiv0\pmod3\), \(q\equiv1\pmod n\). The count of two-edge tetrahedra isolates a quadratic-size family, not the full face vector or the total number of tetrahedra.

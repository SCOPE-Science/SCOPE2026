# Exact antipodal defect of every convex polygonal prism

## Finding

Let \(Q\subset\mathbb R^2\) be a nondegenerate convex polygon with precisely \(n\ge3\) vertices and no redundant collinear vertices. Let \(p(Q)\) count unordered pairs of parallel edges; any such pair has opposite outward normals. Let \(P\subset\mathbb R^3\) be any nondegenerate affine image of \(Q\times[-1,1]\). Call two distinct points *antipodal* if some pair of parallel supporting hyperplanes of \(P\), on opposite sides, contains them. Let \(A(P)\) be the number of unordered antipodal pairs of distinct vertices, \(B(P)\) the number of unordered antipodal pairs of distinct edge midpoints, and \(\delta(P)=f_0(P)-1-A(P)+B(P)\).

Then
\[
 A(P)=n^2+2n+2p(Q),\qquad B(P)=n^2+3n+7p(Q),\qquad
 \boxed{\delta(P)=3n-1+5p(Q).}
\]
Consequently, at fixed side count every creation of one opposite-parallel pair raises the defect by exactly five. Combined with Phat's general homology theorem [1], the integral second homology of its antipodal square complex is free abelian of rank \(3n-1+5p(Q)\); the homology theorem itself is prior work.

## Assumptions and scope

All polygons are full-dimensional, compact and convex, have \(n\ge3\) *actual* vertices, and have no three consecutive collinear boundary vertices. A prism here means an affine image, by an invertible affine map, of the Cartesian product \(Q\times[-1,1]\); therefore oblique affine prisms are included. A pair of polygonal edges is parallel if its direction lines are parallel, independently of orientation. In a strictly convex polygonal boundary with no redundant vertices, such edges have opposite supporting normals. For a polytope \(K\), two distinct points \(x,y\in K\) are antipodal precisely when \(x-y\in\partial(K-K)\). Vertices and midpoints are counted as *distinct geometric points*, and all pairs are unordered.

## Proof

**1. Difference-body criterion.** Existence of opposite supporting hyperplanes through \(x,y\) is equivalent to a nonzero vector \(u\) realizing \(h_K(u)+h_K(-u)=\langle u,x-y\rangle\). This means \(x-y\) belongs to an exposed boundary face of \(K-K\), hence to its boundary, and conversely every boundary point has such a supporting normal. Both antipodality and all the counts are preserved by invertible affine transformations. It therefore suffices to treat \(P=Q\times[-1,1]\), where
\[
 P-P=(Q-Q)\times[-2,2].
\]
A pair is antipodal if its vertical-coordinate difference has absolute value two, **or** its planar-coordinate difference lies on \(\partial(Q-Q)\).

**2. Planar vertex pairs.** The planar polygon has exactly \(n+p(Q)\) unordered antipodal vertex pairs. Here is a rotating-support proof, including degeneracies. Outward normals of the \(n\) edges give \(n-p(Q)\) distinct directions modulo a half turn, because exactly \(p(Q)\) pairs coincide; a given direction modulo a half turn cannot occur for three edges of a genuine convex polygon. Between consecutive normal events the opposite supporting faces are unique vertices, so each of the \(n-p(Q)\) open arcs yields one different unordered vertex pair. At a normal direction belonging to only one edge, the two pairs using its endpoints are exactly those represented by the neighboring open arcs, and there are no further pairs. At a direction shared by a parallel opposite-edge pair, the opposite supporting faces are two edges: their four cross-endpoint pairs include the two neighboring arc pairs and two additional pairs. Thus the total is \((n-p(Q))+2p(Q)=n+p(Q)\). This is the classical rotating-calipers antipodal-pair count, not a claim of novelty.

**3. Vertex pairs of the prism.** There are \(2n\) vertices, divided into two horizontal layers. Every one of the \(n^2\) cross-layer pairs is antipodal. Within each layer the condition reduces to planar antipodality, so there are \(n+p(Q)\) such pairs per layer. Hence \(A(P)=n^2+2(n+p(Q))\).

**4. Edge-midpoint pairs of the prism.** There are \(2n\) horizontal edges (\(n\) per layer) and \(n\) vertical edges. Partition midpoint pairs into disjoint types:

* Two horizontal midpoints in different layers: all \(n^2\) pairs, because the vertical-coordinate difference is two.
* Two horizontal midpoints in the same layer: a midpoint is exposed by a planar normal only perpendicular to its edge. Consequently antipodality requires opposite parallel supporting edges. Each such pair occurs in both layers, giving \(2p(Q)\).
* Two vertical midpoints: their vertical-coordinate difference is zero and their planar projections are vertices of \(Q\). The planar count in Step 2 yields \(n+p(Q)\).
* One horizontal and one vertical midpoint: for each base edge \(e\), the opposite supporting face of \(Q\) is a single vertex unless it is a parallel edge. In the former case there is exactly one opposite vertex, and in the latter exactly two. Thus there are \(n+2p(Q)\) admissible base edge–vertex incidences, each of which can use either of the two horizontal layers. This gives \(2n+4p(Q)\).

Summing, \(B(P)=n^2+2p(Q)+(n+p(Q))+(2n+4p(Q))=n^2+3n+7p(Q)\). Finally \(f_0(P)=2n\), so
\[
\delta(P)=2n-1-\bigl(n^2+2n+2p(Q)\bigr)
+\bigl(n^2+3n+7p(Q)\bigr)=3n-1+5p(Q).
\]
This proves all three counts and the affine-prism extension.

## Verification

The standalone Python 3 verifier `prism_exact_verifier.py` uses integer-only arithmetic. For each integer-coordinate convex polygon it forms an exact convex hull of all base-vertex differences, tests exact difference-body boundary membership for every unordered vertex pair and every unordered edge-midpoint pair of the prism, and checks the three closed formulas against those direct tests. Its seven fixed examples include a triangle, a rectangle, a trapezoid, a generic quadrilateral, a pentagon, a centrally symmetric hexagon and a centrally symmetric octagon; 180 additional deterministically generated convex integer polygons are checked. The test reports `PRISM_ANTIPODAL_EXACT_OK 187`. The exact finite tests are reproducibility checks, **not** an exhaustive proof for every polygon or arbitrary real coordinates; the proof above supplies the general result.

For illustration, a triangular prism has \((n,p,A,B,\delta)=(3,0,15,18,8)\); a generic quadrilateral prism has \((4,0,24,28,11)\); a trapezoidal prism with exactly one opposite parallel edge pair has \((4,1,26,35,16)\); and a parallelepiped has \((4,2,28,42,21)\). The last special case agrees with the previously known cube defect [1].

## Relationship to prior work

Phat [1] introduced the three-dimensional antipodal defect, proved its integral homological interpretation and an exact general local formula, and calculated, among other examples, the tetrahedral and cubic cases and a polygonal-pyramid formula. The difference-body characterization used above is also part of that framework. The elementary planar count is classical rotating-calipers geometry [2]. This note does **not** claim any of those general ingredients or the cube case as new. Its specific contribution is the full affine-prism family evaluation, separate explicit counts for vertices and edge midpoints, and the fixed five-unit parallel-pair increment. This family-specific evaluation was not identified in the accessible source descriptions or the queried mathematical-result records; an inaccessible portion of [1]'s full text leaves a historical-priority risk.

## Limitations

The theorem is only for affine images of Cartesian prisms, not arbitrary polyhedra combinatorially isomorphic to prisms or arbitrary frusta. It is a count of antipodal vertices and edge midpoints and the associated defect, not a new general integral-homology theorem. The convexity and no-redundant-vertex assumptions are essential to the stated planar count. The result has an analytic proof, but its literature-priority assessment remains provisional because a complete page-by-page comparison with [1] and all earlier sources could not be completed; independent validation has not been performed.

## References

1. Kieu Gia Thinh Phat, *The Antipodal Defect of a Convex Polyhedron*, arXiv:2606.14599, first posted 2026-06-12, https://arxiv.org/abs/2606.14599.
2. F. P. Preparata and M. I. Shamos, *Computational Geometry: An Introduction*, Springer, 1985, section on antipodal pairs and rotating calipers.

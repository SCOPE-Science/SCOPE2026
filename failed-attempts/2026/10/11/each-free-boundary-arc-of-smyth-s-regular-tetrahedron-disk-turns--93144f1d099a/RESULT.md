# Each free-boundary arc of Smyth's regular-tetrahedron disk turns by exactly sixty degrees

## Finding

Let \(\Sigma^*\) be Smyth's embedded free-boundary minimal disk in a regular tetrahedron, in the exact representation of Finch. Its boundary consists of four smooth planar arcs, one in each tetrahedron face, joined at four edge-midpoint corners.

Every smooth boundary arc \(\gamma\) is strictly convex and satisfies
\[
\int_\gamma |\kappa_{\mathrm{pl}}|\,ds=\frac{\pi}{3},
\]
where \(\kappa_{\mathrm{pl}}\) is the ordinary signed curvature of \(\gamma\) in its face plane. Consequently the four smooth pieces together have total absolute curvature
\[
\sum_{\gamma\subset\partial\Sigma^*}\int_\gamma |\kappa_{\mathrm{pl}}|\,ds=\frac{4\pi}{3}.
\]

Equivalently, the unit normal along each face arc turns through exactly sixty degrees. This quantity is scale-invariant, so it is unchanged by the homothety that places the represented surface into any prescribed regular tetrahedron.

## Assumptions and scope

The claim concerns the regular-tetrahedron Smyth disk whose exact Gauss map is established in arXiv:2610.00434v1. It concerns the four smooth open face arcs and their endpoint limits. It does not add the corner turning angles of the piecewise-smooth closed boundary, and it does not claim an analogous exact value for a general tetrahedron or for the conjectural endpoint identifications in the disphenoid deformation discussed in the source.

The curvature here is Euclidean plane-curve curvature inside a tetrahedron face, not the Gaussian curvature of the minimal surface. The source already computes the latter globally; the present result identifies a distinct extrinsic boundary invariant.

## Proof

Fix one smooth boundary arc \(\gamma\), parameterized by Euclidean arclength \(s\), and let \(P\) be the tetrahedron face containing it. Because \(\Sigma^*\) meets \(P\) orthogonally, its unit normal \(N\) is tangent to \(P\) along \(\gamma\). The unit tangent \(T\) of \(\gamma\) also lies in \(P\), and \(N\perp T\). Thus, up to one constant sign on the connected arc, \(N\) is exactly the planar unit normal of \(\gamma\). Therefore
\[
\left|\frac{dN}{ds}\right|=|\kappa_{\mathrm{pl}}|,
\]
and the total absolute curvature of \(\gamma\) equals the spherical arclength of its Gauss image.

Finch identifies the Gauss image of the whole disk with one spherical square in the cuboctahedral arrangement determined by the four tetrahedron face normals. The four square vertices are
\[
\frac{(\pm1,0,-1)}{\sqrt2},\qquad
\frac{(0,\pm1,-1)}{\sqrt2},
\]
and the four free-boundary arcs map to the four sides of this square. For two adjacent vertices, for example
\[
p=\frac{(1,0,-1)}{\sqrt2},\qquad
q=\frac{(0,1,-1)}{\sqrt2},
\]
one has
\[
\langle p,q\rangle=\frac12.
\]
Hence the spherical side length is
\[
d_{\mathbb S^2}(p,q)=\arccos\!\left(\frac12\right)=\frac{\pi}{3}.
\]
The Gauss map has degree one onto the square, and on the fundamental boundary side it is a Schwarz map onto the corresponding great-circle segment. Thus each physical face arc maps once onto one complete square side. Combining this with the preceding curvature identity gives
\[
\int_\gamma |\kappa_{\mathrm{pl}}|\,ds=\frac{\pi}{3}.
\]

It remains only to exclude flat subarcs. Finch's closed formula for the derivative of the Gauss map has no zero on the interior of the relevant boundary side, so \(dN/ds\neq0\) there. Since the Gauss image is one simple great-circle segment traversed once, the signed planar curvature has one sign throughout the open arc. Therefore each boundary arc is strictly convex.

Summing the four congruent arcs yields \(4\pi/3\).

## Verification

The proof uses only three exact ingredients from the represented surface: face-orthogonal free boundary, the degree-one cuboctahedral-square Gauss image, and nonvanishing of the Gauss-map derivative on the open side. The spherical distance computation is independent of the hypergeometric normalization.

The packaged checker verifies the cuboctahedral side computation in two independent coordinate descriptions: directly from the adjacent unit vectors and through the stereographic square vertices \(\sqrt2-1\) and \(i(\sqrt2-1)\). Both give dot product \(1/2\) and side length \(\pi/3\).

This finite calculation is only an arithmetic check. The geometric identification of boundary turning with Gauss-image arclength and the one-to-one boundary correspondence are proved analytically above.

## Relationship to prior work

Smyth's 1984 paper proves existence and uniqueness statements for the three disk-type stationary minimal surfaces in a tetrahedron and analyzes their boundary traces. In the proof, the relevant trace pieces are shown to be convex and their tangential indicatrices have length less than \(\pi\). For the regular tetrahedron, however, no exact turning angle is given there.

Finch's 2026 paper supplies the missing exact geometry: the regular-tetrahedron disk has a degree-one Gauss map onto a specific spherical cuboctahedral square, with explicit vertices, and the free-boundary side maps to the corresponding great circle. The paper records exact total Gaussian curvature, boundary length, area, planarity, orthogonality, and the Gauss square, but it does not state the Euclidean total curvature of an individual planar boundary arc. Combining the exact Gauss square with the free-boundary normal relation gives the new value \(\pi/3\) per arc.

Targeted searches under boundary turning, tangential indicatrix, Gauss-map side length, and planar boundary curvature found no equivalent exact statement for Smyth's regular-tetrahedron disk.

## Limitations

The theorem does not determine the corner contribution to the total curvature of the closed piecewise-smooth spatial boundary. It also does not give a curvature density as a function of arclength, only its exact integral on each smooth face arc.

No claim is made for the two less symmetric Smyth disks in a general disphenoid, for arbitrary tetrahedra, or for global area-minimizing properties. The originality comparison covers the inspected primary sources and targeted searches; an equivalent observation under unrelated terminology could remain unindexed.

## References

1. S. Finch, *An exact hypergeometric Weierstrass representation for Smyth's free-boundary minimal disk in the regular tetrahedron*, arXiv:2610.00434v1, 30 September 2026. Primary MSC 2020: 53A10.
2. B. Smyth, *Stationary minimal surfaces with boundary on a simplex*, Inventiones Mathematicae 76 (1984), 411--420. DOI: 10.1007/BF01388467.

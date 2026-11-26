# Direction-invariant central-section complexity of the two quasiregular polyhedra

## Finding

**Theorem.** Let \(Q_4\) be a regular cuboctahedron centered at the origin, and let \(Q_5\) be a regular icosidodecahedron centered at the origin. For every plane through the origin avoiding all vertices of the relevant solid:

1. The intersection with \(Q_4\) is a centrally symmetric **octagon** with exactly four sides lying in triangular faces and four in square faces.
2. The intersection with \(Q_5\) is a centrally symmetric **dodecagon** with exactly six sides lying in triangular faces and six in pentagonal faces.

This is independent of the orientation of the plane subject to the stated vertex-avoidance condition. Therefore both joint side-type distributions are point masses for uniformly oriented central planes. The same assertions, including the face-type labels inherited from the original solids, hold for any nonsingular affine image of either solid, using planes through the image of its center.

A more general mechanism is given by the following **edge-diamond balance criterion**. Let \(P\) be a convex three-dimensional simplicial polytope containing the origin in its interior. Suppose that, for every edge with endpoints \(u,v\), the two third vertices \(w_+,w_-\) of its incident triangular faces satisfy
\[
(w_++w_-)\times(u+v)=0.
\]
Assume also that the edge-midpoint convex hull \(R(P)\) is a polytope whose vertices are precisely those midpoints and whose edges join midpoint pairs arising from the sides of a triangular face of \(P\), as in ordinary rectification. Then the number of sides of every vertex-avoiding central planar section of \(R(P)\) is constant. If each edge of \(R(P)\) separates one triangular face from one face inherited from a vertex of \(P\), the section's sides alternate between these two types and their counts agree. The octahedron and icosahedron meet these hypotheses.

## Assumptions and scope

A central plane has equation \(H_n=\{x\in\mathbb R^3:n\cdot x=0\}\) with \(n\ne0\). It is **generic** for a polyhedron if \(H_n\) contains no polyhedron vertex. The section is a two-dimensional convex polygon because the origin is interior. A section side *lies in a face* when its relative interior belongs to the relative interior of that face; genericity makes this unambiguous. The theorem is deterministic on the generic domain. The non-generic normal set is a finite union of great circles and has spherical measure zero; no side-count assertion for those exceptional planes is made. The number of section sides is the number of relative-interior edge crossings in the original polyhedron.

For reproducibility, take the regular octahedron with vertices \(\pm e_1,\pm e_2,\pm e_3\). Take the regular icosahedron with twelve vertices obtained as cyclic coordinate permutations of \((0,\pm1,\pm\varphi)\), where \(\varphi=(1+\sqrt5)/2\), with independent signs. In each case construct the rectification by taking all edge midpoints. These produce the cuboctahedron and icosidodecahedron, respectively. Uniform random directions mean normalized rotational area measure on the sphere, modulo identifying opposite normals.

## Proof

**Step 1: vertex-crossing invariance.** Let \(P\) satisfy the criterion and consider a rectified vertex \(x=(u+v)/2\) corresponding to an edge of \(P\). The edge is incident to triangles \((u,v,w_+)\) and \((u,v,w_-)\). The four distinct graph neighbors of \(x\) in its rectification are
\[
A=(u+w_+)/2,\quad B=(v+w_+)/2,\quad C=(u+w_-)/2,\quad D=(v+w_-)/2.
\]
The hypothesis shows that \(A+D=B+C=(u+v+w_++w_-)/2\) is collinear with \(x\). If \(n\cdot x=0\), then \(n\cdot A=-n\cdot D\) and \(n\cdot B=-n\cdot C\). Provided the plane contains no other adjacent vertex, exactly two neighbors are on either side of it. When the normal crosses this vertex's great circle transversely, the sign of \(n\cdot x\) flips; of the four incident edges, two change from crossing to not crossing and two change in the reverse direction. Thus the **total number of crossed edges does not change**. If antipodal vertices cross simultaneously, the same zero-change statement holds separately at both vertices.

The finite set of vertex-orthogonality great circles partitions the sphere into chambers. Any two chambers can be joined by a path crossing circles transversely at points that lie on no other distinct circle. The preceding calculation gives the same crossed-edge count in adjacent chambers. Hence this number is constant over all generic central normals. This argument is global and does not infer an all-direction result from sampling.

**Step 2: balanced diamonds for the regular originals.** Every edge of the regular octahedron or regular icosahedron has a twofold rotational symmetry about the axis joining its midpoint to the origin. This half-turn interchanges \(u,v\) and interchanges the opposite face vertices \(w_+,w_-\). Consequently \(w_++w_-\) is fixed by the half-turn and lies on its axis, parallel to \(u+v\). The criterion follows. Both rectifications have the claimed four graph neighbors at each vertex. The supplied exact-arithmetic checker independently verifies this criterion on every one of the \(12\) octahedral and \(30\) icosahedral edges.

**Step 3: find the constants.** Fix the single generic normal \(n=(1,2,4)\). The original octahedron has \(6\) vertices, \(12\) edges and \(8\) triangular faces. Its rectification has \(12\) vertices and \(24\) edges; direct exact sign tests of the endpoint dot products show precisely \(8\) of these edges cross \(H_n\). The original icosahedron has \(12\) vertices, \(30\) edges and \(20\) triangular faces. Its rectification has \(30\) vertices and \(60\) edges; exact sign tests show precisely \(12\) of these edges cross \(H_n\). The computation uses integer arithmetic for the octahedron and the exact quadratic integer ring \(\mathbb Z[\varphi]\) for the icosahedron. For an element \(a+b\varphi\), sign testing reduces to comparing the integers \((2a+b)^2\) and \(5b^2\), with separate handling of signs. The actual vertex, edge and face construction and all tests appear in `checks/verify.py`.

**Step 4: face colors.** Each rectified edge separates one face coming from an original triangular face and one face coming from an original vertex; these are respectively triangle/square for the cuboctahedron and triangle/pentagon for the icosidodecahedron. A generic section crosses such edges transversely, so consecutive section sides lie in opposite face types. The resulting \(8\)-cycle has \(4\) sides of each type; the \(12\)-cycle has \(6\) sides of each type. Central symmetry of the section follows from central symmetry of both polyhedra. For an invertible affine map, midpoint incidence and plane intersection are preserved, giving the stated affine extension.

## Verification

Execute `python3 checks/verify.py` from the extracted artifact directory using Python's standard library. It constructs both original simplicial solids from exact coordinates, finds their edges by exact squared distance, enumerates incident faces, forms the rectified graph, checks every local edge-diamond balance identity, and verifies the base normal's crossing and face-incidence counts. As additional stress tests, it checks \(720\) generic small-integer normal triples for the cuboctahedron and \(960\) for the icosidodecahedron. Its expected final line is `EXACT CHECKS PASSED`. The finite direction tests are **not** the proof of direction-invariance; Step 1 is.

## Relationship to prior work

The two quasiregular convex polyhedra and their alternating face types are classical. Matteo's 2014 classification treats their flag-orbit geometry and explicitly lists these as the two convex quasiregular types; that classification does not state the present all-generic-central-plane intersection law. Existing geometric expositions identify exceptional centered equatorial hexagons in the cuboctahedron and decagons in the icosidodecahedron; those planes contain polyhedron vertices and are excluded by the stated genericity condition. Their existence is compatible with, and does not establish, the claimed generic octagon/dodecagon law. The local vertex-crossing balance argument and complete two-type central-section incidence constants are the proposed contribution.

## Limitations

The claim covers central, vertex-avoiding planes, not arbitrary offset cuts. The exceptional symmetry-axis sections can have fewer sides and are intentionally excluded; no all-direction constant claim is made. The local criterion assumes ordinary midpoint rectification produces the listed vertices and edges; it is not asserted for arbitrary simplicial polytopes without that condition. Published-literature and searchable-record comparisons do not establish absolute priority; specialist historical accounts of central cuts may contain equivalent descriptions. The symbolic finite tests certify the explicit coordinate identities and base counts, not historical originality or independent review.

## References

- Nicholas Matteo, *Two-orbit convex polytopes and tilings*, arXiv:1403.2125, initial public submission 2014-03-10, https://arxiv.org/abs/1403.2125.
- Paulo Freire, *Polyhedra*, sections on rectification and quasiregular solids, https://www3.mpifr-bonn.mpg.de/staff/pfreire/polyhedra/polyhedra.htm (undated web exposition; used for geometric comparison, not cohort dating).
- *Regular Icosidodecahedron*, Wolfram MathWorld, https://mathworld.wolfram.com/RegularIcosidodecahedron.html (classical face data).
- *Regular-shaped faces derived from the intersection of cube, octahedron and rhomb-dodecahedron*, 2011 geometric exposition, https://www.mi.sanu.ac.rs/vismath/zefirooct2011/__regular_faces_from_truncation_of_cubic_polyhedra_2011_09_11_.htm (cuboctahedral construction; not an all-generic-section result).

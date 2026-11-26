# Independent mathematical audit

## correctness

PASS

The inclusive scale-two flag complex has the same twelve-vertex link as the infinite square grid: all candidate coordinate differences are at most four, and wrapping in factors of size at least seven cannot turn a cyclic coordinate distance into one or two unless the original absolute difference already was one or two. Independently enumerated all link subsets, recovered the nine facets and face vector (1,12,30,24,5) including the empty face, and verified that each of the 35 recorded lower faces has exactly its paired upper face as a proper coface at that step. Replay: python3 /workspace/independent_checks.py 2, reading only the frozen JSON certificate. Coning each pair with the center preserves freeness in the full complex; the last pair removes the edge to the surviving link vertex along with the center. No deleted vertex belongs to another deleted vertex's link, so all subsequent links are intact. Incidence counting gives (mn,6mn,10mn,6mn,mn); the 72 faces per deleted vertex are disjoint across S. The modulo-five kernel is well defined and its defining functional is nonzero on every length-one or length-two displacement, giving the claimed one-fifth and three-fifths ratios. After one deletion the neighboring link loses one axial vertex and has face vector (11,24,16,3), hence Euler characteristic zero and deletion lowers the ambient Euler characteristic by one. The unpunctured torus conclusion is also independently derivable: each axial distance-two edge has common neighbors only in its midpoint diamond. Within each such edge's star, pair all faces containing the edge but not the midpoint with their midpoint extensions, in descending size; first do horizontal, then vertical edges. Remaining diamond faces are in full unit-square tetrahedra. These meet along ordinary grid edges or vertices; two elementary pairs per square remove the tetrahedron and one diagonal, leaving the triangulated torus. An elementary pair requires a free codimension-one face with unique maximal coface, not that the latter have only one possible free face; the certificate uses the correct condition. Distances in the induced complex are inherited, not recomputed.

## originality

PASS

Credit the unpunctured torus type and the all-vertex triangulation collapse to earlier work. The distinct result is a direct collapse to the prescribed induced subcomplex for every separated S, with exact face accounting and a closely matched obstruction. The standard cone-lifting argument does not supply the essential local link collapse. On the examined evidence, none of the nearby statements implies this prescribed-target result; the relevant inaccessible proof details remain an explicit priority risk.

## value

PASS

The result answers whether the inclusion of a prescribed, potentially extensively punctured flag subcomplex is itself a simple homotopy equivalence. It removes 60% of faces in a natural periodic pattern, has an explicit finite local construction, and exposes failure already for two adjacent holes. These are useful exact stability and compression statements, not another unpunctured type computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

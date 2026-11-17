# One-handed scalene-face convex polyhedra are necessarily disphenoids

## Finding
Let \(T\) be a nondegenerate scalene Euclidean triangle with side lengths \(a,b,c\). Let \(P\subset\mathbb R^3\) be a full-dimensional convex polyhedron whose **actual facets** are nondegenerate triangles, all congruent to \(T\). Orient every facet by its outward normal. Suppose the three distinct side lengths, traversed around the oriented boundary of each facet, have the **same cyclic order** up to cyclic shift. Then \(P\) is a tetrahedron with each pair of opposite edges equal (a disphenoid). In particular, \(T\) must be acute.

Conversely, every acute scalene triangle \(T\) admits such a convex polyhedron, unique up to Euclidean isometry: the corresponding disphenoid. Therefore a right or obtuse scalene triangle admits **no** outward-one-handed convex equifacial polyhedron, regardless of its number of facets. This answers the outward-normal, orientation-preserving form of the scalene case singled out in [1].

The hypothesis of common outward-normal handedness is essential. It is **not** ordinary unmarked congruence of planar triangular subsets of \(\mathbb R^3\), for which a three-dimensional proper rotation can reverse a triangle's intrinsic planar orientation. The relevant distinction is the cyclic order as seen from the outward side, exactly as in [1, Remark 3].

## Assumptions and scope
A convex polyhedron is a compact, full-dimensional convex three-polytope. A facet is a maximal two-dimensional face; no artificial coplanar subdivision is counted as a facet. Every vertex is consequently a genuine strictly convex polyhedral vertex, with incident planar face angles summing to strictly less than \(2\pi\). Every triangular facet has the three different edge lengths of \(T\), and every edge belongs to exactly two facets. The boundary has the canonical orientation induced by its outward normal.

Choose the three distinct lengths and label them \(0,1,2\). The one-handed condition is that the cyclic word of labels encountered along the outward-oriented boundary of **every** triangular facet is \((0,1,2)\), up to cyclic permutation, after possibly interchanging labels \(1\) and \(2\) globally. No assumption of a global spatial symmetry is made.

## Proof
**Local cyclic-label lemma.** Fix a vertex \(v\) of \(P\), and let \(u_0,\ldots,u_{d-1}\) be its adjacent vertices in cyclic order, selected so that the outward-oriented incident facets are \((v,u_i,u_{i+1})\), indices modulo \(d\). Write \(c_i\in\{0,1,2\}\) for the length label of \(vu_i\), and \(s_i\) for that of \(u_i u_{i+1}\). By the one-handed hypothesis, the ordered facet-edge labels \((c_i,s_i,c_{i+1})\) run in cyclic order \((0,1,2)\). Thus
\[
 c_{i+1}\equiv c_i+2\pmod 3.
\]
After going once around \(v\), this gives \(3\mid d\). Further, the labels of every three consecutive radial edges are a permutation of \(0,1,2\). Their three intervening face angles are exactly the three angles \(\alpha,\beta,\gamma\) of \(T\), once each. Since \(\alpha+\beta+\gamma=\pi\), the total incident face angle at \(v\) is
\[
 \Theta(v)=\frac{d\pi}{3},\qquad
 \kappa(v)=2\pi-\Theta(v)=\pi\left(2-\frac d3\right).
\]
This is an exact local curvature quantization, not a numerical estimate.

**Convexity forces valence three.** A genuine vertex of a full-dimensional convex polyhedron has \(\Theta(v)<2\pi\). Since \(d\ge3\) and \(d\) is a multiple of three, the preceding formula forces \(d=3\) at every vertex. Thus the polyhedron is simplicial and three-regular. Writing \(V,E,F\) for its numbers of vertices, edges, and facets, double counting gives \(3V=2E=3F\). Euler's formula \(V-E+F=2\) then yields \(V=F=4\), \(E=6\). Hence \(P\) is a tetrahedron.

**It must be a disphenoid.** Each of the four triangular facets contains one edge of each prescribed length. Double counting facet-edge incidences therefore gives exactly two polyhedral edges of each length. Two edges of the same length cannot share a vertex, because together with the third edge of their common triangular facet they would make that facet isosceles, contrary to the scalene hypothesis. The two equal-length edges therefore form an opposite pair. All three opposite pairs have equal lengths, which characterizes a disphenoid.

**Acuteness and converse.** If the prescribed side lengths are \(a,b,c\), set
\[
 x^2=\frac{b^2+c^2-a^2}{8},\quad
 y^2=\frac{c^2+a^2-b^2}{8},\quad
 z^2=\frac{a^2+b^2-c^2}{8}.
\]
The four vertices
\[
 (x,y,z),\quad (x,-y,-z),\quad (-x,y,-z),\quad (-x,-y,z)
\]
form a nondegenerate tetrahedron precisely when all three displayed squares are positive, equivalently when \(T\) is acute. Its opposite edge pairs have lengths \(a,b,c\), so its four faces are congruent to \(T\). The three coordinate-axis half-turns act transitively on these four faces and preserve outward orientation; consequently all four outward-oriented length words agree cyclically. Conversely, any tetrahedron with congruent scalene faces is a disphenoid by the preceding counting argument, and thus must satisfy these strict positivity conditions. The dimensions are determined by the three side lengths, proving uniqueness up to isometry. \(\square\)

## Verification
The proof is self-contained apart from the standard convex-vertex angular-deficit fact, Euler's polyhedron formula, and elementary triangle congruence. The crucial step is the exact relation \(c_{i+1}\equiv c_i+2\pmod3\), followed by the angle sum \(\Theta(v)=d\pi/3\), which holds at every vertex, with no bound on the number of facets. The six-vertex octahedral case is eliminated by the same argument as every other non-tetrahedral convex triangulation.

The standalone `check.py` uses exact integer coordinates and enumerates all oriented three-edge-label assignments of a tetrahedral and an octahedral boundary. It confirms three compatible label assignments for the tetrahedron and none for the octahedron, and directly checks the handedness of an explicit scalene disphenoid. Run with `python3 check.py` from a directory containing the file. These finite checks corroborate the local combinatorics only; the unrestricted theorem is proved above without computational enumeration.

## Relationship to prior work
Georgiou [1] determines the minimum number of congruent triangular facets when reflections are allowed, proves a universal eight-face realization, and explicitly asks about the outward-normal orientation-preserving version for right and obtuse scalene triangles (Section 4). Its Remark 3 precisely distinguishes the two cyclic side-length words on facets. The present theorem rules out all numbers of facets in that remaining case, rather than improving the minimum under reflection-allowed congruence. Its tetrahedral converse agrees with the disphenoid criterion established as [1, Lemma 5] and earlier literature [3].

The full text of Hungerbühler, Hungerbühler and Pirron [2], especially its Euler restrictions and constructions with both mirror-image protogons, addresses general monohedral polyhedra without the one-handed convex scalene hypothesis. Its constructions do not supply the above local cyclic-label curvature identity or the one-handed classification. The published classification [4] treats all reflected-allowed scalene-faced *octahedra*, including their edge-length incidence patterns; it does not impose one-handedness or exclude larger convex polyhedra. These distinctions are implications of the precise hypotheses, not title-based novelty tests.

## Limitations
The assertion applies only to full-dimensional **convex** polyhedra with genuine triangular facets, a **scalene** prescribed triangle, and a single common outward-normal side-length chirality. It makes no claim for isosceles triangles, arbitrary reflection-allowed congruence, nonconvex immersed surfaces, coplanar subdivisions, or a definition of ambient three-dimensional rotation that forgets the outward-normal orientation. Absolute historical priority is not established by searches; unindexed or differently worded prior statements remain possible. No independent mathematical audit has been performed.

## References
[1] G. M. Georgiou, *Congruent Triangular Faces, Reflections Allowed: Universal Realization and the Minimum Face Count in Problem B22*, arXiv:2608.01109v1 (first public 2026-08-02), especially Remark 3, Lemma 5 and Section 4. https://arxiv.org/abs/2608.01109

[2] N. Hungerbühler, N. Hungerbühler and M. Pirron, *New families of monohedral polyhedra*, Journal of Mathematics and the Arts 19 (2025), 1–23, published online 2025-05-20, DOI:10.1080/17513472.2025.2492807. Authorized open-access copy: https://www.research-collection.ethz.ch/entities/publication/bdb775af-ea7f-4ab7-874a-efcf45050267

[3] J. Leech, *Some properties of the isosceles tetrahedron*, Mathematical Gazette 34 (1950), 269–271, as cited in [1].

[4] *All edge-length arrangements of scalene-faced convex octahedra*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-all-edge-length-arrangements-of-scalene-faced-convex-octahedra--72d76a5b3c3a

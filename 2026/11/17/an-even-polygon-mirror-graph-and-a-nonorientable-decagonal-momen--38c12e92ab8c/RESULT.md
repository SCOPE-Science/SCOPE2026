# An even-polygon mirror graph and a nonorientable decagonal moment-angle quotient

## Finding
For every even integer \(n\ge6\), let \(C_n\) be the boundary cycle of an \(n\)-gon and let
\[
X_n=(D^1,S^0)^{C_n}\subset[-1,1]^n,
\qquad Q_n=X_n/D_n,
\]
where the dihedral group permutes coordinate indices, and the quotient is the **ordinary geometric orbit space**. Define the finite graph \(\Gamma_n\) as follows. Its vertices are binary sign words \(u\in\{-1,1\}^n\) that are invariant under at least one dihedral reflection. For each reflection \(s\), its index orbits include exactly two *exceptional* orbits, which are either the two singleton orbits of a vertex-axis reflection, or the two adjacent-coordinate pairs of an edge-axis reflection. Join two \(s\)-invariant words by an edge when they differ precisely on one of these exceptional orbits (both signs flip together for a pair). Retain the edges with their reflection labels, so parallel edges are allowed. The dihedral action permutes vertices and these edges.

**Mirror-graph theorem.** The boundary \(\partial Q_n\) is homeomorphic, as a one-dimensional space, to \(\Gamma_n/D_n\). In particular, the number of boundary circles is the number of graph components \(\#\pi_0(\Gamma_n/D_n)\). This gives an exact all-even-width graph model using only reflection-symmetric sign words, in place of the full two-dimensional quotient cellulation.

**Decagonal homeomorphism classification.** For \(n=10\), this graph has ten orbit-space components and
\[
\boxed{Q_{10}\cong N_{66,10}},
\]
where \(N_{h,b}\) denotes the compact connected nonorientable surface with \(h\) crosscaps and \(b\) boundary circles. Thus this decagonal quotient has exactly **ten** boundary circles, \(\chi(Q_{10})=-74\), and nonorientable genus \(66\). The preceding even widths \(n=6,8\) have two and four boundary circles respectively; ten is the first non-power-of-two count among even widths \(6,8,10\).

## Assumptions and scope
The simplicial cycle \(C_n\) contains the empty face, its \(n\) singletons, and its \(n\) cyclic adjacent pairs, but not the interior of the polygon. A point of \(X_n\) has coordinates strictly between \(-1\) and \(1\) only on a face of \(C_n\). Each cubical cell has zero, one, or two free coordinates. A binary sign word represents a cubical vertex; an exceptional two-coordinate orbit is varied along the diagonal of a square and can vary only if its two indices are adjacent. Reflections of the index cycle act by permuting coordinates and never negate their signs. The general mirror-graph claim is for **even \(n\ge6\)**; the complete homeomorphism classification asserted here is for **\(n=10\)** only. No statement about an arbitrary even width's orientability or closed-form boundary number is asserted.

## Proof
**1. Local surface and mirror structure.** At each sign vertex of \(X_n\), the link is the \(n\)-cycle. Thus \(X_n\) is a connected closed orientable cubical surface. Index rotations preserve the polygonal orientation while reflections reverse it; the orientations can be checked by assigning the square with free adjacent indices \(i,i+1\) the ordered orientation multiplied by the product of signs on all other coordinates. A finite subgroup of local disk isometries acts on a circular link by rotations and/or reflections, so \(Q_n\) is a compact connected surface with boundary, and its boundary is exactly the image of the union of the fixed loci of index reflections.

**2. Exact graph model.** Fix any reflection \(s\) for even \(n\ge6\). Its other index orbits, besides the two exceptional ones, are pairs of nonadjacent indices. In an \(s\)-fixed point of \(X_n\), any nonadjacent index pair must sit at a common endpoint sign, since it cannot be the set of free coordinates. The two exceptional orbits have mutually nonadjacent supports; therefore the two real parameters they supply may range along the **boundary**, and not the interior, of a square. Each assignment of signs to the other index orbits yields one square-boundary circle. Its four sign vertices differ along exactly one exceptional orbit at each of its four arcs. Two distinct reflection fixed circles can meet only at sign vertices: their two different reflections multiply to a nonidentity rotation, and no nonidentity rotation preserves a nonempty face of \(C_n\) for \(n\ge6\). Consequently the full reflection-mirror locus is precisely the graph \(\Gamma_n\), with each edge geometrically realized by the corresponding interval or square diagonal. The action of \(D_n\) identifies those graph arcs exactly as specified. Taking its orbit yields \(\partial Q_n\), proving the mirror-graph theorem.

**3. Exhaustive ten-coordinate boundary enumeration.** Encode \(+1\) by bit one and \(-1\) by bit zero. For each of the ten reflections, enumerate the sign assignments on nonexceptional orbits, form the four corners of its distinguished square, and join them in the graph. Then join every word to its twenty dihedral images. This runs over **all** mirror vertices and edges by Step 2, not a sample. The resulting graph has 424 distinct sign vertices and exactly ten connected components. Their pairs (least numeric bitmask, number of binary vertices), sorted by least bitmask, are
\[
(0,56),(5,40),(9,40),(17,40),(27,40),
(51,40),(85,32),(119,40),(165,56),(347,40).
\]
The component sizes sum to \(424\). The independently implemented face-poset orbit calculation obtains a boundary graph of ten cycles, eight of length eight and two of length sixteen (lengths refer to its barycentric one-skeleton). Both algorithms and their exact output are included.

**4. Euler characteristic and nonorientability.** Construct all cubical cells from the 1024 sign vertices and admissible free-coordinate supports, barycentrically subdivide each square, and take the dihedral orbits of complete flags \(v<e<f\). The action is without inversions on flags because their three ranks differ. The quotient has precisely 486 barycentric vertices, 1584 edges, and 1024 triangles. Each edge belongs to one or two triangles: exactly 96 edges have incidence one, and the other 1488 have incidence two. Hence its Euler characteristic is \(486-1584+1024=-74\).

To rule out orientability, order every triangular flag by increasing cubical-face dimension. Sort orbit triangles lexicographically by their three orbit-vertex identifiers (orbit representatives are lexicographically least coordinate tuples, separately indexed within ranks zero, one and two). In this deterministic enumeration the fifteen triangles indexed
\[
58,57,51,15,14,13,12,3,4,5,22,24,53,55,56
\]
form a closed dual-edge path. Across every successive shared **interior** edge, including the final return, opposite induced boundary orientations require a change of the local triangle-orientation sign. The fifteen changes multiply to \(-1\), so no global orientation exists. The accompanying checker reconstructs all fifteen shared edges and checks the product exactly; this is a finite explicit obstruction, not a heuristic numerical test.

**5. Surface classification.** Every connected compact nonorientable surface with \(b\) boundary components and \(h\) crosscaps has Euler characteristic \(2-h-b\). Here \(b=10\) and \(\chi=-74\), giving \(h=66\). The classification theorem for compact surfaces proves the stated homeomorphism type.

## Verification
Run `python3 verify_mirror_10.py` (Python standard library only). It independently constructs the bitmask graph of all reflection mirrors and the entire barycentric quotient surface, validates edge incidences, orientation obstruction, boundary-cycle lengths and Euler characteristic, and prints `EXACT_DECAGONAL_MIRROR_AND_SURFACE_CHECK_PASS`. The recorded deterministic output is `verify_mirror_10_output.txt`. The separate general-width mirror enumeration `verify_small_boundaries.py` tests the boundary component counts at even widths \(6,8,10,12\), with output `verify_small_boundaries_output.txt`. Neither verifier relies on a previously generated scientific file or on numeric approximations. The full general mirror-graph assertion is proved geometrically; computations are used only for the finite decagonal case and the listed smaller comparisons.

## Relationship to prior work
The real moment-angle polyhedral product is classical (Denham–Suciu; Grujić–Welker). Das proves that the cyclic-only polygon quotient is a closed orientable surface and gives its genus using necklace enumeration; this does not determine the added reflection quotient's boundary or orientability. The published result *Dihedral quotients of polygonal real moment-angle surfaces are graphs up to homotopy* already establishes the full dihedral quotient's homotopy type and Euler characteristic for all polygon sizes and, for **odd** sizes, its boundary count. It explicitly leaves the **even** boundary count and orientability unasserted. Those existing invariants are credited, not claimed as new. The present contribution is the all-even mirror graph, the exact decagonal boundary count and its orientation obstruction, which together determine a previously undetermined homeomorphism type. A published reversal-quotient classification for **paths** concerns a surface with original boundary and only a single reflection, so it does not subsume the closed-cycle full-dihedral case. Previously recorded coordinate sign-change involutions likewise have a different action.

## Limitations
The binary-component algorithm is an exact all-even description, not a simplified divisor-sum formula for every even width. The homeomorphism type \(N_{66,10}\) is asserted only for ten coordinates. In particular the calculation does not establish nonorientability for every \(n\ge6\), nor is an exact boundary count stated beyond the finite widths actually computed. The orientation obstruction depends on a complete, deterministic finite quotient triangulation and can be checked against the included fifteen-step cycle; an independent mathematical audit is not available. Unindexed equivalent accounts of the even quotient remain a residual publication-priority risk.

## References
- G. Denham and A. I. Suciu, *Moment-angle complexes, monomial ideals, and Massey products*, arXiv:math/0512497, first posted 2005-12-21, https://arxiv.org/html/math/0512497v4.
- V. Grujić and V. Welker, *Discrete Morse theory for moment-angle complexes of pairs \(D^n,S^{n-1}\)*, arXiv:1212.2028, first posted 2012-12-10, https://arxiv.org/html/1212.2028v2.
- S. Das, *Genus of the Hypercube Graph and Real Moment-Angle Complexes*, arXiv:1806.10220, first posted 2018-06-26, especially Sections 3–3.1, https://ar5iv.labs.arxiv.org/html/1806.10220.
- *Dihedral quotients of polygonal real moment-angle surfaces are graphs up to homotopy*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-dihedral-quotients-of-polygonal-real-moment-angle-surfaces-are-g--fc9e3338cf87/RESULT.md.
- *Reversal quotients of real moment-angle surfaces of paths*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-reversal-quotients-of-real-moment-angle-surfaces-of-paths--f3ef76f58446/RESULT.md.

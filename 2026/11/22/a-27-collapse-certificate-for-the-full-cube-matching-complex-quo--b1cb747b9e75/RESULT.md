# A 27-collapse certificate for the full cube matching-complex quotient

## Finding
Let \(Q_3\) be the three-dimensional cube graph, \(X=\mathcal M(Q_3)\) its **ordinary matching complex**, and \(G=\operatorname{Aut}(Q_3)\) its full group of 48 graph automorphisms. Thus the vertices of \(X\) are cube graph edges, and its faces are collections of pairwise vertex-disjoint graph edges. The **ordinary geometric quotient**, not the homotopy/Borel quotient and not the simplicial complex formed merely from orbits of graph edges, satisfies
\[
\boxed{|X|/G\searrow\{\mathrm{point}\}.}
\]
More precisely, \(\operatorname{sd}(X)/G\) has exactly nine vertices, 21 one-cells, 19 two-cells and six three-cells. An explicit list of 27 elementary free-face collapses reduces this genuine geometric quotient to one vertex. Therefore its integral reduced homology and all its homotopy groups vanish. This strengthens the previously known *rational acyclicity* of this same quotient to contractibility.

## Assumptions and scope
Identify cube vertices with binary triples \(\mathbb F_2^3\). Two vertices are adjacent precisely when they differ in one coordinate. Fix the twelve graph edges in ascending endpoint order. Each matching is a nonempty subset of these twelve edges with disjoint endpoints. A strict flag is a chain \(M_0\subsetneq\cdots\subsetneq M_k\) of nonempty matchings, not merely a list of matching-orbit classes. The full cube automorphism group consists of all maps \(v\mapsto b+\sigma(v)\) for a translation \(b\in\mathbb F_2^3\) and a coordinate permutation \(\sigma\in S_3\), giving exactly 48 distinct edge permutations.

The simplices of the barycentric subdivision \(\operatorname{sd}(X)\) are strict matching flags. Every automorphism preserves matching cardinalities, hence cannot permute two different vertices of one such flag. Accordingly the geometric orbit space has a finite regular-flag-orbit \(\Delta\)-complex structure: **distinct orbits of flags remain distinct cells**, even when their endpoint matching orbits agree. Codimension-one faces occur with their actual multiplicities. This distinction is essential to the collapse proof.

## Proof
**1. Exact reconstruction of the quotient.** The verifier enumerates all \(2^{12}-1\) nonempty edge subsets, selects exactly 107 matchings, and recursively enumerates their 1,385 strict flags. Their respective numbers by cardinality and simplex dimension are independently checked in code. It constructs the 48 affine cube automorphisms from three-coordinate permutations and binary translations, verifies they induce distinct permutations of the twelve graph edges, and acts on each matching flag. Each flag orbit is represented by the lexicographically smallest flag among its 48 images. This gives precisely 55 quotient cells, with dimension vector
\[
(c_0,c_1,c_2,c_3)=(9,21,19,6).
\]
For every positive-dimensional cell, deleting each flag entry produces a codimension-one face, whose complete flag orbit identifies the attaching face. The verifier builds this **full incidence multilist**, including repeated occurrences of one cell in a boundary; it never replaces multiplicities by a set or equates distinct flag orbits merely because their vertex-orbit labels coincide.

**2. A finite elementary collapse certificate.** In `collapse_certificate.json`, each pair `[free,top]` gives indexes into the canonical quotient-cell enumeration reconstructed by `verify.py`: cells are sorted first by flag length and then lexicographically by their canonical matching-mask tuple. The certificate contains 27 ordered pairs. At every step, before deletion, `verify.py` independently checks all of the following:

- The indicated two cells both survive and have successive dimensions.
- The free cell occurs as a codimension-one face **exactly once in all surviving attaching-face incidence lists**, including multiple occurrences inside one top cell.
- The indicated top cell is maximal: no surviving higher cell has it as a face.
- After deleting the pair, all faces of every other remaining cell still survive.

These are the elementary free-face collapse conditions for this flag-orbit \(\Delta\)-complex. Since the verifier reconstructs the incidences from the original cube and matching definition, the JSON certificate cannot assert a collapse by fiat. It confirms that exactly one zero-cell and no other cells remain after the 27 pairs. Each deletion is a strong deformation retraction, so their composition exhibits \(\operatorname{sd}(X)/G\) as collapsible.

**3. Geometric conclusion.** Barycentric subdivision is \(G\)-equivariantly homeomorphic to the original realization, hence \(|\operatorname{sd}(X)|/G\cong|X|/G\). An elementary collapse preserves homotopy type, and collapsing to a point proves contractibility. Therefore \(\widetilde H_i(|X|/G;\mathbb Z)=0\) for all \(i\), \(\pi_i(|X|/G)=0\) for all positive \(i\), and there is no hidden torsion or fundamental-group obstruction.

## Verification
Execute `python3 verify.py` from the directory containing `collapse_certificate.json`, using a Python 3 interpreter and its standard library only. The verifier rebuilds all graph edges, valid matchings, flags and automorphisms, constructs the complete orbit-incidence data, checks the stated cell counts, then replays and verifies every certified collapse. Its expected output is:

`CUBE_MATCHING_FULL_QUOTIENT_COLLAPSES_OK group=48 matchings=107 flags=1385 cells=55 pairs=27 last_vertex=8`

The last vertex number is an internal deterministic cell index, not a graph-vertex label. No external homology tables or numerical floating-point tolerances enter the proof. Finite exhaustive enumeration is a complete proof for this fixed finite complex; no claim is made about higher-dimensional cubes.

## Relationship to prior work
Braun–Hough's 2016 preprint develops matching-complex topology for **open planar small grids**, providing an archival motivation but no classification of the three-dimensional cube quotient. The established classification \(\mathcal M(Q_3)\simeq\bigvee^4S^2\) concerns the **unquotiented** complex. Two published computations of the full 48-element rational cube-matching homology representation conclude that \(|\mathcal M(Q_3)|/G\) has no positive-degree **rational** homology, but explicitly leave integral torsion and homotopy type unclassified. Rational acyclicity does **not** imply the present contractibility theorem. Published contractibility of the cube graph's **two-point configuration-space** quotient concerns a different topological construction; the full-symmetry quotient of the pentagonal-prism matching complex is instead a homotopy three-sphere, exhibiting a distinct case in the circular-prism family. The present new statement is the 27-step actual geometric collapse, not a recomputation of already known rank or rational character.

## Limitations
The theorem applies only to the ordinary matching complex of the three-dimensional cube under its complete 48-element graph symmetry. It does not assert a classification for proper subgroups, higher-dimensional cubes, or other prism widths. The exact finite certificate is self-review but has not undergone independent mathematical audit. The originality comparison is relative to inspected full published result texts and an accessible archival paper; an equivalent unindexed calculation remains possible. The 2007 graph-complex book was available only in preview and cannot be claimed as fully inspected.

## References
1. B. Braun and W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, arXiv:1606.01204v1 (first publicly posted 2016-06-03), https://arxiv.org/abs/1606.01204.
2. *The cube matching complex is a wedge of four two-spheres*, public mathematical record `79d70fe8b67e`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-cube-matching-complex-is-bigvee-4-s-2--79d70fe8b67e .
3. *The full cube matching-homology symmetry module*, public mathematical record `0d9335a47f2a`, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-full-s-4-times-c-2-symmetry-module-of-cube-matching-homology--0d9335a47f2a .
4. *The axial-vector symmetry module of cube matching homology*, public mathematical record `b431e4a26870`, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-the-axial-vector-symmetry-module-of-the-cube-matching-complex-q--b431e4a26870 .
5. *The cube's two-particle configuration-space full-symmetry quotient*, public mathematical record `a2c7941d36bd`.
6. *The full-symmetry quotient of the pentagonal-prism matching complex*, public mathematical record `5d7c581e07d3`.
7. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928 (2007), DOI: 10.1007/978-3-540-75859-4.

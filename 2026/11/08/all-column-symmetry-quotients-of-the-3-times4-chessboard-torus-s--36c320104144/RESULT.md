# All column-symmetry quotients of the \(3\times4\) chessboard torus: six surface types

## Finding
Let \(X=\Delta_{3,4}\) be the ordinary chessboard complex whose vertices are the twelve squares of a three-row, four-column board, and whose faces are partial non-attacking rook placements. Let \(S_4\) act on \(X\) by permuting the four columns, without permuting the rows.

**Theorem.** For every subgroup \(H\leq S_4\), the geometric orbit space \(|X|/H\) is a compact connected surface, with or without boundary. Up to conjugacy, the eleven possibilities give the following complete classification. The table also lists the numbers of orbit vertices, orbit edges and orbit triangles of the barycentric subdivision, their Euler characteristic, and the number of boundary circles. The subgroup class is specified by order and cycle types, distinguishing the two Klein-four classes.

| Subgroup class | Number of conjugates | Orbit cells \((v,e,f)\) | \(\chi\) | Boundary circles | Homeomorphism type |
|:--|--:|:--|--:|--:|:--|
| Trivial | 1 | \((72,216,144)\) | 0 | 0 | Torus |
| Transposition subgroup \(C_2\) | 6 | \((42,114,72)\) | 0 | 1 | Möbius band |
| Double-transposition subgroup \(C_2\) | 3 | \((36,108,72)\) | 0 | 0 | Torus |
| Three-cycle subgroup \(C_3\) | 4 | \((26,72,48)\) | 2 | 0 | Sphere |
| \(V_4=\langle(12),(34)\rangle\) | 3 | \((24,60,36)\) | 0 | 2 | Annulus |
| \(V_4=\{1,(12)(34),(13)(24),(14)(23)\}\) | 1 | \((18,54,36)\) | 0 | 0 | Torus |
| Four-cycle subgroup \(C_4\) | 3 | \((18,54,36)\) | 0 | 0 | Klein bottle |
| Point stabilizer \(S_3\) | 4 | \((19,42,24)\) | 1 | 1 | Disk |
| Dihedral subgroup \(D_8\) of order eight | 3 | \((12,30,18)\) | 0 | 1 | Möbius band |
| Alternating subgroup \(A_4\) | 1 | \((8,18,12)\) | 2 | 0 | Sphere |
| Full \(S_4\) | 1 | \((7,12,6)\) | 1 | 1 | Disk |

The conjugate subgroups in every table row have homeomorphic quotients. The eleven conjugacy classes contain \(1+6+3+4+3+1+3+4+3+1+1=30\) subgroups. In particular, the full column-symmetry quotient is a disk, the alternating quotient is a sphere, and all six listed surface types actually occur.

## Assumptions and scope
All groups and complexes are finite. The vertex set of \(X\) is \(\{0,1,2\}\times\{0,1,2,3\}\). A subset is a face if both coordinate projections are injective. The action is \(\sigma(r,c)=(r,\sigma(c))\) for \(\sigma\in S_4\). A quotient means the **geometric orbit space** of the realization, not its fixed-point subcomplex, not the quotient of the original face set without subdivision, and not a homotopy orbit/Borel quotient. The phrase “surface” includes the compact surfaces with boundary in the table.

## Proof
**1. The chessboard complex is a torus.** There are \(12\) vertices, \(36\) edges and \(24\) triangles. Every edge belongs to exactly two triangles (choose one of the two remaining columns for the third row), and every vertex link is the six-cycle given by the matching complex of a \(2\times3\) board. Thus the connected complex is a closed triangulated surface with Euler characteristic zero. An integral orientation cycle is obtained by orienting each triangle by increasing row number and assigning to a triangle with column triple \((a,b,c)\) the sign of the four-permutation \((a,b,c,d)\), where \(d\) is the missing column. Around each edge the two triangles receive opposite induced signs, so the chain is a cycle with unit coefficients. Hence the surface is orientable, and therefore a torus. This torus and orientation construction are classical; see Jojić–Panina–Vrećica–Živaljević, Section 2.1, and are *not* claimed to be new. The orientation character of column relabelling is \(\operatorname{sgn}(\sigma)\).

**2. The orbit cell structure is exact.** The barycentric subdivision \(\operatorname{sd}X\) has one vertex for every nonempty face of \(X\), one edge for every strict two-face chain, and one triangle for every strict three-face chain. It has respectively \(72\), \(216\) and \(144\) cells. A column permutation preserves the size of every face, so distinct vertices of any subdivision simplex have different ranks and cannot be identified by a group element. Consequently the orbit simplices form a regular cellular triangulation of the orbit surface, with cells indexed by orbits of face chains. In particular, orbiting the original triangles without barycentric subdivision would not be a justified alternative.

**3. Exhaustion of subgroups and local topology.** Begin with the identity subgroup and repeatedly adjoin each of the \(24\) column permutations, closing under multiplication and inversion. This exhaustive finite process yields exactly \(30\) distinct subgroups. Conjugating them by each permutation yields the eleven classes in the table. For each representative \(H\), enumerate all \(H\)-orbits of one-, two- and three-term chains of nonempty faces. A quotient edge is a boundary edge precisely when it belongs to only one quotient triangle; this incidence count gives the boundary-edge numbers \(0,12,0,0,12,0,0,12,6,0,6\) in the displayed row order. Boundary edges form respectively \(0,1,0,0,2,0,0,1,1,0,1\) connected circles. As an additional check beyond Euler characteristic, the quotient vertex link at **each** orbit vertex is a *single* path (on the boundary) or a *single* circle (in the interior); there are no pinched vertices. The independently executable exhaustive enumeration implementing these elementary constructions is in `verification/verify.py`, with its exact output in `verification/run_output.txt`. No experimental extrapolation is used: there are only \(24\) permutations, \(30\) subgroups and \(144\) original barycentric triangles, and the checker visits all of them.

**4. Orientability and classification.** The orientation cycle in step 1 changes by \(\operatorname{sgn}(\sigma)\) under \(\sigma\in S_4\). A boundaryless quotient is orientable if and only if all elements of \(H\) are even; if an odd element acts without reflecting along a fixed curve, the quotient is instead a closed nonorientable surface. The tabulated Euler characteristics and boundary-component counts, together with the explicit local vertex-link checks, determine the homeomorphism types by the classification of compact connected surfaces. In particular a boundaryless quotient of Euler characteristic zero is a torus when orientable and a Klein bottle otherwise; Euler characteristic two forces the sphere. For a surface with one boundary component, Euler characteristic one gives a disk and Euler characteristic zero a Möbius band; two boundary components and Euler characteristic zero give an annulus. This proves every table entry and the theorem.

## Verification
Run `python verification/verify.py` with Python 3 and only its standard library. The verifier enumerates all faces and strictly increasing face chains, generates every subgroup of \(S_4\), checks the eleven conjugacy classes, constructs each quotient cellular triangulation, computes triangle-edge incidences and boundary circles, verifies connected path/circle links at every quotient vertex, and checks the sign-oriented integral fundamental cycle under all \(24\) column permutations. Its stored stdout ends with `ALL_VERIFY_OK`. The computed whole-domain check is a finite proof of the table when combined with the transparent enumeration algorithm and topological argument; neither a timeout nor a partial sample is used.

## Relationship to prior work
Limonchenko and Yu (first arXiv posting 2026-10-27, Theorem 1.1) classify homotopy types of three-row generalized chessboard complexes and explicitly name the \(3\times4\) torus as an exception. Jojić, Panina, Vrećica and Živaljević (2020, Section 2.1) already present the same torus triangulation, its face vector, the links and its sign orientation. Friedman and Hanlon (1997) develop rational Betti-number and representation methods for chessboard complexes. **None of the inspected results asserts the eleven-class classification of geometric column-subgroup quotient surfaces or the six homeomorphism types appearing above.** The novelty claim concerns only this complete geometric quotient classification, not the classical torus, its orientation, its ordinary Betti numbers, or the general classification of compact surfaces.

## Limitations
Only the fixed \(3\times4\) ordinary chessboard complex and column permutations are considered. The table does not classify the larger combined row-and-column symmetry group, generalized capacity complexes, or homotopy-orbit spaces. Surface classification is an exact mathematical consequence of finite incidence computations, but independent validation has not been performed. An older unindexed equivalent quotient classification could exist.

## References
1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827v1 (first posted 2026-10-27), Theorem 1.1 and Section 4; https://arxiv.org/html/2610.37827v1.
2. D. Jojić, G. Panina, S. T. Vrećica, and R. T. Živaljević, *Generalized chessboard complexes and discrete Morse theory*, arXiv:2003.04018v1 (first posted 2020-03-09), Section 2.1; https://arxiv.org/html/2003.04018v1.
3. J. Friedman and P. Hanlon, *On the Betti Numbers of Chessboard Complexes* (1997), introduction and representation-theoretic treatment; https://www.cs.ubc.ca/~jf/pubs/web_stuff/newchess.pdf.

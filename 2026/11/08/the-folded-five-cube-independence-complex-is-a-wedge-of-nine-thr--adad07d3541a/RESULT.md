# The folded five-cube independence complex is a wedge of nine three-spheres

## Finding
Let \(C\) be the five-regular Clebsch graph, also called the folded five-cube or Greenwood–Gleason graph. For the abstract independence complex \(\operatorname{Ind}(C)\), whose faces are exactly the independent vertex subsets,
\[
\boxed{\operatorname{Ind}(C)\simeq\bigvee^{9}S^3.}
\]
Consequently its only nonzero reduced integral homology is \(\widetilde H_3(\operatorname{Ind}(C);\mathbb Z)\cong\mathbb Z^9\). This is an integral homotopy equivalence, not merely a field-homology computation. The case distinguishes the folded five-cube from the ordinary four-cube, whose independence complex is already known to be a wedge of seven three-spheres.

## Assumptions and scope
The vertex set is \(\mathbb F_2^4\), represented by the integers \(0,\ldots,15\) as four-bit words. Two distinct vertices \(u,v\) are adjacent exactly when their bitwise exclusive-or lies in \(\{1,2,4,8,15\}\). This is the graph obtained from the four-dimensional cube by adding its eight antipodal edges; equivalently, it is the antipodal quotient of the five-dimensional cube. It has sixteen vertices, forty edges, degree five, and strongly regular parameters \((16,5,0,2)\). It is **not** the ten-regular graph sometimes also called the Clebsch graph. The simplicial complex includes the empty simplex, but discrete Morse matching is performed on its nonempty face poset.

## Proof
Every nonempty face corresponds uniquely to a bit mask \(m\in\{1,\ldots,2^{16}-1\}\) whose selected vertices contain no adjacent pair. Exhaustive enumeration by that predicate gives the exact dimension-indexed face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(16,80,160,120,16),
\]
so the nonempty face poset has \(392\) members. A separate recursion that extends independent sets only by currently legal vertices reproduces exactly the same set.

Construct a matching on this complete nonempty face poset by visiting the sixteen pivot vertices in the following order:
\[
(6,13,7,8,14,11,4,0,3,10,5,15,12,1,2,9).
\]
At a pivot \(v\), pair every still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever the latter is also present and still unmatched. Both faces are immediately removed from the unmatched set. There are \(191\) disjoint pairs; pivot-by-pivot counts are
\[
(75,40,31,15,11,6,6,2,2,1,2,0,0,0,0,0).
\]
The only unmatched faces are **one zero-dimensional simplex and nine three-dimensional simplices**.

Orient every covering relation in the nonempty face-poset Hasse diagram downwards, reversing the \(191\) matched relations. There are exactly \(1200\) such covering relations. The bundled verifier constructs each directed relation, confirms disjointness and the stipulated pivot rule, and performs a complete topological sort of all \(392\) vertices of the resulting directed Hasse graph. All vertices are removed, so the orientation is acyclic and the matching is a discrete-Morse matching.

By the acyclic matching theorem of discrete Morse theory, the geometric realization is homotopy equivalent to a CW complex with one zero-cell, nine three-cells and no other cells. Every three-cell attaches to the zero-skeleton via a constant map from \(S^2\), proving the stated wedge of nine three-spheres. This proves the integral homotopy type without inferring it from finite-field homology.

## Verification
Run `python3 verify.py` using Python's standard library; no input data or packages are required. The verifier independently constructs the graph as the antipodal quotient of the five-cube and checks equality with the stated Cayley graph. It checks all forty edges, vertex degrees and common-neighbor counts, recreates the full face set using both brute force and recursion, repeats all matching pairs, and exhaustively certifies acyclicity on all \(1200\) incidences. Independent mod-two boundary elimination gives ranks \((15,65,95,16)\) in degrees one through four, Betti numbers \((1,0,0,9,0)\), and reduced Euler characteristic \(-9\). These last field checks corroborate, but do not substitute for, the integer homotopy proof. The recorded output ends with `ALL_CHECKS_PASS`.

## Relationship to prior work
Barmak's 2010 theorem establishes that the independence complex of any triangle-free graph is homotopy equivalent to a suspension (Theorem 3.4, arXiv:1007.0418). It applies because the folded five-cube is triangle-free, but does not determine the spheres' dimension or number. Its stronger star-cluster description (Theorem 3.5) likewise leaves the case-specific homotopy type to be calculated.

Bousquet-Mélou, Linusson, and Nevo (2007) establish homotopy types for particular open and cylindrical square grids using discrete Morse matchings; those graph families do not contain this antipodally augmented four-cube. The published exact result for the ordinary four-cube gives \(\operatorname{Ind}(Q_4)\simeq\bigvee^7S^3\); adding the eight antipodal edges changes the independence complex, and that result does not imply the nine-sphere conclusion. Published calculations of the **neighborhood complex** and the **matching complex** of the same five-regular Clebsch graph concern different simplicial functors and therefore also do not imply this claim. The matching algorithm is standard; the specific complete acyclic certificate and its exact homotopy implication for this canonical graph are the contribution.

## Limitations
This is a single finite-graph classification and does not establish a formula for the independence complexes of all folded hypercubes, an equivariant wedge decomposition, or the homotopy type of the ten-regular complement. Searching named and equivalent formulations cannot exclude unindexed or unpublished equivalent calculations. An independent mathematical audit has not been performed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02, particularly Theorems 3.4–3.5. https://arxiv.org/abs/1007.0418
2. M. Bousquet-Mélou, S. Linusson, and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890v1, first public 2007-01-30. https://arxiv.org/abs/math/0701890
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. DOI: 10.1006/aima.1997.1650.
4. *The four-cube independence complex is a wedge of seven three-spheres*, published research record dated 2026-10-11, identifier `9947aaad144c`.
5. *The five-regular Clebsch neighborhood complex is a wedge of thirty-one two-spheres*, published research record dated 2026-10-11, identifier `1dc11cc6574a`.
6. *Mod-two homology of the Clebsch matching complex*, published research record dated 2026-10-11, identifier `7e53e4d18ed4`.

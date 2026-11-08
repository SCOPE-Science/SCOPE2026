# The mixed-dimensional out-neighborhood complex of the Paley tournament on nineteen vertices

## Finding
Let \(T\) be the Paley tournament with vertex set \(\mathbb Z/19\mathbb Z\) and arc \(a\to b\) precisely when \(b-a\) is a nonzero quadratic residue modulo \(19\). Define the **irreflexive outward-neighborhood complex** \(K\) by declaring a nonempty set \(\sigma\) to be a simplex if and only if \(\sigma\subseteq N^+(a)\) for some vertex \(a\), where \(N^+(a)=\{b:a\to b\}\).

Then its **integral homotopy type** is
\[
K\simeq S^2\vee\bigvee^{78}S^3.
\]
In particular \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{78}\), and all other reduced integral homology groups vanish. This is a classification of this particular nineteen-vertex complex, not a general theorem for all doubly regular tournaments or Hadamard designs.

## Assumptions and scope
Arithmetic is in \(\mathbb Z/19\mathbb Z\), and
\[
Q=\{1,4,5,6,7,9,11,16,17\}.
\]
The maximal simplices are exactly the nineteen distinct nine-element blocks \(B_a=a+Q\), for \(a\in\mathbb Z/19\mathbb Z\). They form a symmetric \(2\text{-}(19,9,4)\) Paley Hadamard design. The word *out-neighborhood* refers to blocks of vertices reached by a single outgoing arc; loops are **excluded**, and the definition is not a directed flag complex of transitive subtournaments.

All claims use ordinary geometric realization, ordinary homotopy equivalence, and integral coefficients. No equivariance is asserted.

## Proof
**Exact finite complex.** Every \(B_a\) has nine vertices, so the entire simplicial complex is the union of their downward-closed Boolean subset lattices. The supplied standalone checker separately enumerates (i) every nonempty subset of each block and (ii) all \(2^{19}-1\) nonempty vertex subsets using the quantified membership test. Both enumerations agree on all \(8246\) nonempty simplices. The face numbers in dimensions \(0\) through \(8\) are
\[
(19,171,969,2223,2394,1596,684,171,19),
\]
with Euler characteristic \(-76\). Every pair of blocks meets in exactly four vertices, independently checking the stated incidence design.

**Acyclic matching.** Encode a nonempty face by its nineteen-bit vertex mask. For each vertex \(v=0,1,\ldots,18\), in that order, pair all currently unmatched faces \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever the latter is still unmatched; delete each matched pair from consideration. This produces \(4080\) disjoint face-coface pairs and leaves exactly one critical vertex, four critical two-faces, and eighty-one critical three-faces. To certify acyclicity, the checker creates all \(40014\) Hasse cover incidences, directs each matched incidence upwards and every other incidence downwards, and performs complete topological sorting. The sort visits all \(8246\) faces, so there is no directed cycle. Forman's acyclic-matching theorem therefore supplies a CW model \(X\simeq K\) with precisely those critical cells and no cells in dimensions one or above three.

**Integral attaching matrix.** Orient each face by increasing vertex order. For a matched two-face \(\sigma\) with three-dimensional coface \(\tau\), eliminate \(\sigma\) by substituting the exact signed boundary relation \(\partial\tau=0\), with the \(\sigma\)-coefficient equal to \(\pm1\). For a two-face matched with a one-face, project to zero; retain each critical two-face. The resulting recursion is well-founded because the matching is acyclic. Applied to boundaries of all eighty-one critical three-faces, it computes the exact integral Morse differential
\[
\partial^{\mathrm{Morse}}_3:\mathbb Z^{81}\longrightarrow\mathbb Z^4.
\]
The checker verifies on **all columns** that its four rows satisfy the integer relation
\[
R_1-2R_2-R_3+R_4=0.
\]
It also finds determinant \(-1\) for the submatrix using rows \((0,1,2)\) and columns \((0,1,4)\), with zero-based indices in the sorted lists of critical faces. Hence the boundary has rank exactly three and a unimodular rank-three minor. Its nonzero Smith invariants are therefore \((1,1,1)\), and the cokernel is \(\mathbb Z\) without torsion; its kernel is \(\mathbb Z^{78}\).

**From homology to homotopy.** The CW model has one vertex and no one-cells; its two-skeleton is a wedge of four two-spheres. By the degree-two Hurewicz isomorphism, attaching maps of three-cells correspond to their integer vectors in \(\mathbb Z^4\). Unimodular row and column transformations are realized up to homotopy by changes of wedge-sphere basis and three-cell slides. The three unit Smith factors cancel three sphere/three-cell pairs, leaving one two-sphere and seventy-eight trivially attached three-spheres. This proves \(K\simeq S^2\vee\bigvee^{78}S^3\) integrally, not merely at the level of finite-field homology.

## Verification
Run `python3 verify.py` using Python 3.10 or later in the same directory as this document. No third-party packages, external data, or network services are required. The output is recorded in `verification_output.txt`. The checker verifies all faces, block intersections, all face-coface incidences, matching acyclicity, the full integral four-by-eighty-one critical boundary, its null relation and unit minor. An independent full simplicial-chain calculation over \(\mathbb F_2\) gives boundary ranks
\[
(18,153,815,1330,1064,532,152,19)
\]
in dimensions one through eight, and Betti numbers \((1,0,1,78,0,0,0,0,0)\) including unreduced degree zero. These modular ranks are corroboration; the integral homotopy proof uses the acyclic matching and integer matrix witnesses.

## Relationship to prior work
Chowdhury and Mémoli developed Dowker constructions for asymmetric networks (first arXiv posting **2016-08-18**); their general duality, filtrations and cycle-network calculations do not specify this irreflexive Paley-tournament block complex or its integral attaching maps. Dowker's classical relation-complex construction supplies earlier background.

Govc classified **directed flag complexes** of doubly regular tournaments and gives the possible nineteen-vertex flag-complex homotopy types, but his simplices are transitive subtournaments, not subsets of an outward-neighborhood block. The two constructions have different face tests and different homotopy types; the published flag result does not determine this finding. Singhi's classification of six \(2\text{-}(19,9,4)\) designs concerns design isomorphism and residual designs, not the present topological classification. A published research record identifying the Paley-nineteen **directed flag complex** and its affine character also concerns that different complex.

No source examined was found to imply this exact block-complex homotopy type. Published results not indexed or not accessible in full may still overlap; priority is not conclusively certified.

## Limitations
The result is an exact, finite, integral homotopy statement for the specified quadratic-residue tournament only. It does not determine topological types for the other five isomorphism classes of symmetric \(2\text{-}(19,9,4)\) designs, for arbitrary Paley tournaments, or for filtered variants with diagonal loops. It does not determine group-equivariant homotopy or integral symmetry representations. The symbolic-Morse proof is reproducible from the bundled source; no external independent mathematical audit has been performed.

## References
1. S. Chowdhury and F. Mémoli, *A functorial Dowker theorem and persistent homology of asymmetric networks*, first arXiv posting 2016-08-18, arXiv:1608.05432, https://arxiv.org/abs/1608.05432 .
2. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333 (2020), especially Proposition 3.4, https://arxiv.org/abs/2006.05333 .
3. N. M. Singhi, *(19, 9, 4) Hadamard Designs and Their Residual Designs*, J. Combin. Theory Ser. A 16 (1974), 241–252, DOI:10.1016/0097-3165(74)90049-1 .
4. C. H. Dowker, *Homology Groups of Relations*, Ann. Math. 56 (1952), 84–95, DOI:10.2307/1969768 .
5. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145, DOI:10.1006/aima.1997.1650 .

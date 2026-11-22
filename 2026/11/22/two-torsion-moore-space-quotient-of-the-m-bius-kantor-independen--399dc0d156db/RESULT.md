# Two-torsion Moore-space quotient of the Möbius–Kantor independence complex

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph, \(K=\operatorname{Ind}(M)\) its simplicial independence complex, and \(G=\operatorname{Aut}(M)\) its full group of graph automorphisms. The **ordinary geometric orbit space** has the integral homotopy type
\[
|K|/G\simeq M(\mathbb Z/2\mathbb Z,3)\simeq S^3\cup_{\deg 2} e^4.
\]
Consequently, \(\pi_1(|K|/G)=\pi_2(|K|/G)=0\), its sole nonzero reduced integral homology group is \(\widetilde H_3(|K|/G;\mathbb Z)\cong\mathbb Z/2\mathbb Z\), and its reduced rational homology vanishes. The torsion and the integral homotopy classification are the assertions here; rational acyclicity was known.

## Assumptions and scope
The sixteen vertices are \(u_i=i\) and \(v_i=8+i\) for \(i\in\mathbb Z/8\mathbb Z\). The undirected edge set comprises exactly the 24 edges \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\). A nonempty face of \(K\) is an edge-free subset of these sixteen vertices. The group \(G\) consists of *all* adjacency-preserving permutations, including those that exchange the two bipartition classes. Its order is 96, verified by exhaustive adjacency-constrained permutation enumeration. We study the ordinary topological orbit space, **not** the Borel construction, an invariant-face subcomplex, or a homotopy quotient. The Moore-space notation refers to a fourth cell attached to a three-sphere by a map of degree two.

## Proof
**A regular quotient cell structure.** For every independent nonempty vertex set, enumerate its nonempty strict chains of subsets. These are the simplices of the barycentric subdivision \(\operatorname{sd}K\). Each graph automorphism preserves cardinalities of every subset in a chain; hence it cannot permute two different vertices of any chain. Consequently the induced group action is without inversions and the chain-orbit quotient has a regular finite CW structure. Cell incidences are obtained by deleting one member from a chain, with the alternating sign determined by its position. Since different deletions have different surviving cardinality sequences, every codimension-one face appears at most once in a given cellular boundary. Explicit canonicalization under all 96 permutations gives exactly 1,090 nonempty independent faces and, for quotient cells of dimensions \(0,\ldots,7\), the vector
\[
(32,316,1521,4231,7105,7050,3780,840).
\]
The original nonempty faces occur by dimension in counts \((16,96,272,376,240,72,16,2)\).

**Homotopy-preserving reduction.** The attached `quotient.cpp` constructs the group, independent sets, chain-orbit cells, and every boundary incidence, using integer bit masks. It repeatedly chooses a surviving face with exactly one immediate coface, verifies that the coface is maximal, and deletes this free face together with its unique maximal coface. These are valid elementary collapses of a regular CW complex, so they preserve homotopy type. `quotient_certificate.txt` records all 12,114 verified face–coface pairs. The residual complex has 647 cells, with dimensional counts
\[
(c_0,c_1,c_2,c_3,c_4)=(14,83,214,240,96).
\]
`residual_cells.txt` records each surviving chain and its exact signed cellular boundary. Its face incidences are closed under taking boundaries; all higher cells have been removed.

**Exact integral homology.** Using the residual signed boundaries, `homology.py` constructs the integer boundary matrices in degrees one through four, of shapes \(14\times83\), \(83\times214\), \(214\times240\), and \(240\times96\). It first checks every consecutive boundary product is zero. Their integral Smith normal forms have ranks \(13,70,144,96\), respectively. Every nonzero invariant factor is one except the degree-four matrix, whose nonzero factors are exactly 95 ones and a single two. In particular, all free reduced Betti numbers vanish, there is no hidden integral torsion in any other degree, and
\[
\widetilde H_j(|K|/G;\mathbb Z)\cong
\begin{cases}\mathbb Z/2\mathbb Z,&j=3,\\0,&j\ne3.\end{cases}
\]
The invariant factor two is in the cokernel of the degree-four boundary, and the degree-three kernel has the exact rank required to contain that cokernel torsion, making it the stated third-homology class.

**Fundamental group.** `fundamental_group.py` reads exactly this same residual quotient cell structure. The one-skeleton has 14 vertices and 83 edges. A spanning tree consists of 13 edges, leaving 70 fundamental-group generators. Each of its 214 triangular two-cell boundaries is converted to an oriented relator. Free reduction and three successive waves of unit-relator elimination kill all 70 generators, with no relators remaining. This is a finite Tietze reduction of the complete two-skeleton presentation; thus the fundamental group is trivial.

**Homotopy classification.** Since the space is simply connected and its second integral homology vanishes, the Hurewicz theorem gives \(\pi_2=0\). It is thus 2-connected, and the next Hurewicz map is an isomorphism \(\pi_3\cong H_3\cong\mathbb Z/2\mathbb Z\). Choose a map from \(S^3\) representing its generator. Twice this map is nullhomotopic, so it extends over the degree-two attachment to a cellular map \(M(\mathbb Z/2\mathbb Z,3)\to |K|/G\). That map induces isomorphisms on all integral homology groups: in degree three by construction, in all other positive degrees because both groups vanish, and in degree zero because both spaces are connected. Both spaces are simply connected CW complexes, so the homological Whitehead theorem gives the claimed homotopy equivalence.

## Verification
From a directory containing the standalone files, compile and run `g++ -std=c++17 -O3 quotient.cpp -o quotient` followed by `./quotient quotient_certificate.txt`. The program deterministically recreates `quotient_certificate.txt` and `residual_cells.txt`, checks the size of the complete automorphism group, validates the quotient cells and every free-face cancellation, and prints `MK_ORBIT_CELL_COLLAPSE_OK`. With Python 3 and SymPy installed, run `python3 homology.py`, which prints `MK_INTEGRAL_HOMOLOGY_OK` after exact integer Smith computations and boundary-composition tests. Run `python3 fundamental_group.py`, which uses only the Python standard library and prints `MK_FUNDAMENTAL_GROUP_OK` after verifying the 70-generator presentation reduces to the trivial group. The provided text certificate and residual data permit byte-for-byte comparison with regenerated files. All operations are finite exhaustive calculations for the explicitly specified graph; no probabilistic or rational-to-integral inference is used.

## Relationship to prior work
Bıyıkoğlu and Civan [1, Example 3.9] establish the **unquotiented** homotopy type \(\operatorname{Ind}(M)\simeq\bigvee^4S^3\vee S^4\), but do not compute the full graph-symmetry orbit space. Two later full-automorphism studies [2, 3] determine its complete **rational** homology characters and the rational acyclicity of the full geometric quotient, while explicitly leaving integral quotient homology and quotient homotopy undetermined. Neither rational acyclicity nor the covering complex's wedge decomposition implies the two-torsion class exhibited here. The claim concerns the same graph and full symmetry group as [2, 3], but a strictly finer integral invariant: \(H_3\cong\mathbb Z/2\mathbb Z\) and the full Moore-space homotopy type. Search comparisons found no covering statement; that is not a proof of absolute publication priority.

## Limitations
The claim is for this single finite graph and its full 96-element automorphism group, not an arbitrary generalized Petersen graph or subgroup action. The quotient is an ordinary orbit space; it must not be confused with homotopy fixed points or equivariant cohomology. Exact enumerations rely on the included, human-inspectable source and certificate; a separate expert audit has not been performed. The novelty comparison covers the cited accessible full texts and indexed searches; unindexed equivalent results and the uninspected complete graph-topological study of Knill [4] remain residual literature risks. No general statement about torsion in other quotients follows from this computation.

## References
1. T. Bıyıkoğlu and Y. Civan, *Castelnuovo-Mumford regularity of graphs*, arXiv:1503.06018v1, first public 2015-03-20, Example 3.9, https://arxiv.org/abs/1503.06018.
2. *Full automorphism homology representations of the Möbius–Kantor independence complex*, public record dated 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-full-automorphism-homology-representations-of-the-m-bius-kantor--37b5190688cf.
3. *Full automorphism homology of the Möbius–Kantor independence complex*, public record dated 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-full-automorphism-homology-of-the-m-bius-kantor-independence-com--7c9f8e92f3e0.
4. O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799v1, https://arxiv.org/abs/2605.30799 (abstract-level comparison only).

# The Petersen matching complex is a wedge of five two-spheres and five three-spheres

## Finding
Let \(P\) be the Petersen graph, and let \(\mathcal M(P)\) be its *ordinary matching complex*: its vertices are graph edges and its simplices are collections of pairwise endpoint-disjoint graph edges. Then the following is an integral homotopy equivalence:

\[
\mathcal M(P)\simeq\bigvee^{5}S^{2}\vee\bigvee^{5}S^{3}.
\]

In particular, \(\widetilde H_{2}(\mathcal M(P);\mathbb Z)\cong\mathbb Z^5\), \(\widetilde H_{3}(\mathcal M(P);\mathbb Z)\cong\mathbb Z^5\), and all other reduced integral homology groups vanish. The result is about \(\mathcal M(P)\), **not** about the graph \(P=\mathcal M(K_5)\), which is only a one-dimensional simplicial complex.

## Assumptions and scope
The graph \(P\) has vertices \(\{0,1,\ldots,9\}\), with indices \(i\) taken modulo five. Its fifteen edges are the five outer edges \(\{i,i+1\}\), the five spokes \(\{i,i+5\}\), and the five inner edges \(\{i+5,(i+2\bmod 5)+5\}\), for \(0\le i<5\). Every graph edge is represented by its sorted endpoint pair. Sort those fifteen pairs lexicographically and give them indices \(0,\ldots,14\). The simplex corresponding to a nonempty edge set \(A\) is represented by the integer \(\sum_{i\in A}2^i\). The orientation of each simplex is the increasing order of these fifteen graph-edge indices. These conventions completely determine the integer boundary signs.

All claims concern this one finite simple graph, ordinary pairwise-disjoint matchings, and the integral homotopy type of the geometric realization. No claim is made about arbitrary cubic graphs, general graph matching complexes, or perfect-matching subcomplexes.

## Proof
**Exhaustive simplex construction.** Choose graph edges recursively in increasing index order, retaining an edge only if both its endpoints are unused. Every matching has a unique increasing list of edge indices, so this recursion visits every nonempty face exactly once. It gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(15,75,145,90,6),
\]
with exactly \(331\) nonempty simplices. In particular the maximal simplex dimension is four.

**An acyclic matching.** Start with all nonempty faces unmatched. Process the graph-edge indices in this fixed order:

`8, 9, 4, 12, 6, 14, 0, 3, 7, 5, 10, 1, 13, 11, 2`.

At a stage with index \(i\), pair each remaining face \(A\) not containing \(i\) with \(A\cup\{i\}\), whenever both are still unmatched; then remove both faces. The procedure produces \(160\) disjoint face-coface pairs: \(14\) of dimensions \((0,1)\), \(61\) of dimensions \((1,2)\), \(79\) of dimensions \((2,3)\), and \(6\) of dimensions \((3,4)\). The five critical two-faces have integer masks `5248, 8228, 18440, 20482, 20488`, and the five critical three-faces have masks `5154, 8332, 10250, 10274, 18465`. Exactly one critical vertex remains; no other critical faces remain.

For an explicit acyclicity certificate, orient every codimension-one face relation from larger face to smaller face, reversing precisely the \(160\) matched relations. There are exactly \(975\) oriented incidences. The included program computes an exhaustive topological sort visiting all \(331\) faces, with none left on a directed cycle. Therefore the matching is acyclic in Forman's sense. Discrete Morse theory supplies a CW complex with one zero-cell, five two-cells and five three-cells, and with no other cells.

**Integral attaching coefficients.** For a face with ordered graph-edge indices \(i_0<\cdots<i_k\), take the standard simplicial boundary
\[
\partial[i_0,\ldots,i_k]=\sum_{j=0}^k(-1)^j[i_0,\ldots,\widehat{i_j},\ldots,i_k].
\]
For each critical three-face, successively eliminate the coefficient at every matched two-face \(\alpha\), using its paired three-face \(\beta\): replace the current boundary chain \(z\) by
\[
z-\frac{\langle z,\alpha\rangle}{\langle\partial\beta,\alpha\rangle}\,\partial\beta.
\]
Each denominator is \(\pm1\). The acyclic directed matching guarantees termination of this integer gradient-path elimination, and the coefficients remaining on critical two-faces are precisely the integral cellular Morse differential. Using the critical faces in the increasing-mask orders above, exhaustive exact-integer elimination yields the **zero \(5\times5\) matrix**. The code exposes the full recurrence, boundary signs and all critical masks; no numerical rank estimate is substituted for this integer calculation.

**Homotopy type.** The CW two-skeleton has one vertex and five two-cells, with no one-cells; hence it is \(\bigvee^5 S^2\). Every attaching map of a three-cell lands in this two-skeleton. The degree vector of such a map is its Hurewicz image in \(H_2\cong\mathbb Z^5\), and the Hurewicz map \(\pi_2\to H_2\) is an isomorphism for this simply connected two-skeleton. The zero Morse differential therefore forces all five attaching maps to be null-homotopic. Adjoining five three-cells consequently gives \(\bigvee^5S^2\vee\bigvee^5S^3\), as asserted.

## Verification
Both standalone Python programs are included. Run `python3 verify_petersen.py` for exact enumeration, the specified repeated-toggle matching, a complete directed-incidence acyclicity test, and the signed integral Morse boundary. Run `python3 verify_petersen_independent.py` for an independent construction of the same abstract graph as the Kneser graph \(\operatorname{KG}(5,2)\), a separate enumeration, and exact modular boundary ranks over the primes \(2,3,5,7,11\).

The second calculation gives boundary ranks \((14,61,79,6)\) in positive degrees, and reduced Betti numbers \((0,0,5,5,0)\) in degrees zero through four over each field tested. These finite-field calculations are cross-checks only. The integral homotopy conclusion follows from the signed gradient-path computation and the Hurewicz argument, not from finite-field agreement.

## Relationship to prior work
Barmak's archived study of star clusters establishes general methods and a connectivity bound for independence complexes of claw-free graphs; matching complexes fall within that class, but the bound does not give this exact integral homotopy type [1]. Bayer, Jelić Milutinović and Vega prove a wedge-of-spheres result for **outerplanar** graph matching complexes [2]; it does not apply to the nonplanar Petersen graph. Bayer, Goeckner and Jelić Milutinović classify *manifold* matching complexes [3], a different classification question.

A particularly important notation distinction is that Mondal, Mukherjee and Saha identify the **Petersen graph itself** with \(\mathcal M(K_5)\) [4]. Their one-dimensional object has six independent first-homology cycles. The present object \(\mathcal M(P)\) is four-dimensional with the face vector above, so their statement does not imply this finding. Likewise the Petersen *two-matching* complex, a bounded-incidence construction, and the complex of discrete Morse gradient fields of \(P\) are different simplicial complexes. Searches did not locate an equivalent exact homotopy statement, but this cannot certify the absence of unindexed or unpublished work.

## Limitations
This is a computer-assisted but finite, reproducible proof for a single graph. The scripts use exact integers and exhaustive face enumeration, but there is no independent external scientific audit or formal proof-assistant certification. A literature search does not establish unconditional publication priority. No higher-order uniformity, family-wide extension, or equivariant homotopy classification is claimed.

## References
[1] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, public 2010-07-02, https://arxiv.org/html/1007.0418v1, especially Section 5.

[2] M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v2, https://arxiv.org/html/2411.04601v2, Theorem 2 and accompanying proof.

[3] M. Bayer, B. Goeckner and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328v3, https://arxiv.org/html/1906.03328v3, Sections 1–2 and classification statements.

[4] A. Mondal, S. Mukherjee and K. Saha, *Topology of matching complexes of complete graphs via discrete Morse theory*, arXiv:2305.02973v5, https://arxiv.org/html/2305.02973v5, Example 2.1 and Section 2.3.

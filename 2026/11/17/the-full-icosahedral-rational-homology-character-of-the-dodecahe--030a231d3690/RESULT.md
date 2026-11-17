# The full icosahedral rational homology character of the dodecahedral perfect-matching complex

## Finding

Let \(D=\operatorname{GP}(10,2)\) be the regular dodecahedral graph, and let \(P(D)\) be its *perfect-matching complex*: its vertices are the thirty graph edges, and an edge subset is a face precisely when it extends to a perfect matching. Its full graph-automorphism group is \(G\cong A_5\times C_2\), with the central involution acting by antipodal inversion. Let \(V_4\) and \(V_5\) be the rational irreducible representations of \(A_5\) of dimensions four and five, and let \(\varepsilon\) be the nontrivial one-dimensional character of \(C_2\).

**Theorem.** The complete rational reduced homology representation is concentrated in degree three and is

\[
\widetilde H_3(P(D);\mathbb Q)\cong
(\mathbf 1\oplus V_4\oplus 2V_5)\boxtimes\mathbf1
\ \oplus\ V_5\boxtimes\varepsilon.
\]

Central inversion has eigenspace dimensions \(15\) and \(5\). Precisely one rational degree-three class is invariant under the entire \(120\)-element group. Consequently the ordinary orbit space \(|P(D)|/G\) has reduced rational homology \(\mathbb Q\) in degree three and zero in all other degrees.

The character is **equal**, as an \(A_5\times C_2\)-character, to the previously published character of the icosahedral *two-independence/dissociation* complex; this equality is a comparison of rational representations, not an assertion of a map or an integral equivalence. In contrast, the known integral homology of \(P(D)\) has an order-two torsion class in degree two, while the icosahedral dissociation complex is a torsion-free wedge of twenty three-spheres. The known nonequivariant homotopy type of \(P(D)\) is not presented as new here.

## Assumptions and scope

All complexes are finite abstract simplicial complexes, realized geometrically. Write the vertices of \(D\) as \(u_i,v_i\), where \(i\in\mathbb Z/10\mathbb Z\). Its edges are \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\) for all ten subscripts. A perfect matching is a set of ten pairwise vertex-disjoint edges covering all twenty vertices. The notation \(P(D)\) denotes the **extendible** perfect-matching complex, not the ordinary matching complex on all partial matchings. Each automorphism acts on \(P(D)\) by permuting its edge-vertices; rational chain orientations use increasing edge indices.

The theorem concerns the one specified graph, its full graph automorphism group, the complete rational homology representation, and rational homology of the finite-group quotient. It does not assert an integral \(G\)-lattice isomorphism, an equivariant homotopy equivalence, or an integral homology formula for the quotient.

## Proof

**1. Previously determined nonequivariant homology.** The published exact homotopy calculation for the perfect-matching complex of \(D\) gives

\[
P(D)\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^{20}S^3.
\]

In particular, \(\widetilde H_3(P(D);\mathbb Q)\cong\mathbb Q^{20}\), and all other rational reduced homology vanishes. The present theorem **uses this prior result as a stated input**, not as a newly proved homotopy classification. The verifier independently reconstructs the graph, perfect-matchings, faces, group action, and character calculations, but not the earlier integral Morse certificate.

**2. Exhaustive simplicial input and complete group.** Pair the least uncovered graph vertex with each possible uncovered neighbor, recursing until all vertices are covered. This bijectively enumerates all perfect matchings and gives exactly 36. Their downward closure has 30,504 faces, including the empty face; the numbers of faces with respectively \(0,1,\ldots,10\) vertices are

\[
(1,30,375,2180,5790,8352,7440,4320,1620,360,36).
\]

The graph-automorphism permutations `R2`, `R3`, and `Z` are explicitly given in the standalone verifier, using the above \(u_i,v_i\) labeling. Direct composition verifies \(R2^2=R3^3=(R2R3)^5=1\); the first two generate a group of order \(60\), isomorphic to \(A_5\) by the classical \((2,3,5)\)-triangle-group presentation. The antipodal permutation `Z` has order two, commutes with both generators, and lies outside their subgroup. Together these permutations generate 120 distinct graph automorphisms. A dodecahedral graph automorphism is determined by the image of a vertex (twenty choices) and the permutation of its three incident neighbors (at most six choices): the unique planar polyhedral embedding propagates this local choice across pentagonal faces. Thus there are at most \(120\) automorphisms, so the constructed group is full.

**3. Signed simplicial Lefschetz calculation.** For any automorphism \(g\) and any nonempty face \(\sigma\) preserved as a set, write \(\operatorname{sgn}(g|_\sigma)\) for the sign of the induced permutation of its edge-vertices. Set that sign to zero for nonpreserved faces. The reduced chain Lefschetz number is exactly

\[
L(g)=-1+\sum_{\varnothing\ne\sigma\in P(D)}
(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]

By the homology concentration above, \(\operatorname{tr}(g\mid\widetilde H_3)=-L(g)\). Two separate exact enumerations compute \(L(g)\) for every one of the 120 elements: (a) the signed trace on all setwise invariant oriented simplices, and (b) the reduced Euler characteristic of the geometric fixed-point orbit complex. For (b), an orbit of graph edges is a vertex precisely when its entire union lies in a perfect matching, and a set of such orbits is a face precisely when their union lies in one perfect matching. This is the fixed-point orbit-simplex triangulation. The two calculations agree element by element.

For rotation-class sizes \((1,15,20,12,12)\), ordered by element orders \((1,2,3,5,5)\), the rational degree-three trace vector is

\[
(20,4,-1,0,0).
\]

For the same rotational classes multiplied by central inversion, the trace vector is

\[
(10,2,1,0,0).
\]

This includes all 120 elements: there are 60 rotations and 60 inversion-twisted rotations. The two order-five classes have the same trace, zero, and were individually covered by the exhaustive calculation.

**4. Character decomposition and quotient.** Averaging the two trace vectors yields the central-even character \((15,3,0,0,0)\) and the central-odd character \((5,1,-1,0,0)\). The standard \(A_5\) irreducible characters have

\[
\chi_{\mathbf1}=(1,1,1,1,1),\quad
\chi_{V_4}=(4,0,1,-1,-1),\quad
\chi_{V_5}=(5,1,-1,0,0).
\]

The even character equals \(\chi_{\mathbf1}+\chi_{V_4}+2\chi_{V_5}\), and the odd character equals \(\chi_{V_5}\). Equality of rational characters determines the displayed rational representation; it excludes all three-dimensional constituents. Its full-group invariant space is exactly the trivial central-even summand, of dimension one. For a finite simplicial group action, subdivision makes the quotient cellular and rational transfer identifies the rational homology of the quotient with group-invariant rational homology. The remaining rational reduced homology therefore consists of exactly one degree-three class.

**5. Dual-solid comparison.** The published representation calculation for the two-independence complex of the icosahedral graph has precisely the same \(A_5\times C_2\) summands. Direct equality of the character vectors proves the stated coincidence. Since its ground set is 12 icosahedral vertices, whereas \(P(D)\) has 30 dodecahedral edge-vertices, no combinatorial identification, natural equivariant map or integral lattice isomorphism is inferred. The published integral homology groups distinguish the spaces.

## Verification

`verify_dodeca_symmetry.py` is standalone Python 3 code using only the standard library. Execute `python3 verify_dodeca_symmetry.py` and compare its output with `VERIFIER_OUTPUT.txt`. The script reconstructs 36 perfect matchings and 30,504 faces, checks three automorphism generators on the explicit graph, closes the order-120 group, and runs **two independent Lefschetz calculations for all 120 automorphisms**. It then checks complete class frequencies, the even/odd characters, their irreducible decompositions, and the invariant multiplicity. Each calculation is finite and exhaustive, not statistical; the earlier homotopy theorem is cited rather than rerun.

## Relationship to prior work

Fujita's dodecahedral matching-polynomial calculation provides a historical, symmetry-aware enumeration setting; it concerns counts of matchings, not rational homology characters of the complex of extendible edge sets. Bayer, Jelić Milutinović and Vega explicitly defined perfect-matching complexes and analyzed honeycomb families, not the regular dodecahedron. Two independently indexed published exact calculations already determine \(P(D)\)'s nonequivariant Moore-space-plus-spheres homotopy type; the **new claim is solely the full \(A_5\times C_2\) rational homology character and its quotient and comparison consequences**. Published results on the icosahedral dissociation/two-independence complex give the same representation on a *different* face system; neither that character nor its torsion-free homotopy type determines the character of \(P(D)\) without a separate argument. The ordinary dodecahedral matching complex and the icosahedral ordinary matching complex also have different definitions and different homology ranks. These distinctions were checked at the level of implications, not title matching.

## Limitations

The proof relies on the existing nonequivariant integral homology theorem and independently computes the new equivariant character by exact finite enumeration. It establishes equality of two rational representations, **not** a canonical equivariant isomorphism or an integral lattice equivalence. The known order-two torsion in \(P(D)\) is not reclassified as a new result; its automorphism action is necessarily trivial because it is a group of order two. The rational orbit-space statement does not determine integral torsion of the quotient. Fujita's 2012 full article was not obtainable through the checked lawful full-text routes; its accessible abstract and mathematical scope were inspected, but full-document noncoverage is not asserted. Unindexed equivalent homology-character calculations remain a publication-priority risk. No independent scientific audit has been performed.

## References

1. S. Fujita, “The Restricted-Subduced-Cycle-Index (RSCI) Method for Counting Matchings of Graphs and Its Application to Z-Counting Polynomials and the Hosoya Index as Well as to Matching Polynomials,” *Bulletin of the Chemical Society of Japan* **85** (2012), 439–449, first public publication 2012-04-10. DOI: `10.1246/bcsj.20110319`.
2. M. Bayer, M. Jelić Milutinović and J. Vega, “Perfect Matching Complexes of Honeycomb Graphs,” *Electronic Journal of Combinatorics* **30** (2023), P2.45; preprint `arXiv:2209.02803`, first posted 2022-09-06.
3. “Order-two torsion and a Moore-space decomposition for the dodecahedral perfect-matching complex,” published mathematical research record (2026-10-25), `https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-order-two-torsion-and-a-moore-space-decomposition-for-the-dodeca--2c09902bba79`.
4. “A Moore-space summand in the dodecahedral perfect-matching complex,” published mathematical research record (2026-11-01), `https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-moore-space-summand-in-the-dodecahedral-perfect-matching-compl--efd05431d7b5`.
5. “The icosahedral dissociation complex: twenty three-spheres and full symmetry,” published mathematical research record (2026-10-25), `https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-icosahedral-dissociation-complex-twenty-three-spheres-and-fu--73ac86596d16`.
6. “Twenty copies of \(S^3\) in the icosahedral two-independence complex, with full symmetry,” published mathematical research record (2026-11-01), `https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-twenty-copies-of-s-3-in-the-icosahedral-two-independence-complex--68309a4b8f9b`.

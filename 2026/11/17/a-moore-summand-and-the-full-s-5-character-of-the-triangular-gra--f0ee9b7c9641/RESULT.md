# A Moore summand and the full \(S_5\) character of the triangular-graph matching complex

## Finding
Let \(T_5=L(K_5)\) be the triangular graph on the ten two-element subsets of \(\{0,1,2,3,4\}\), with adjacency when two subsets intersect. Let \(X=\mathcal M(T_5)\) be the matching complex of this graph, not the matching complex of the Petersen graph and not the four-cut complex of \(T_5\).

The complete **integral homotopy type** is
\[
X\simeq M(\mathbb Z/3\mathbb Z,2)\vee\bigvee^{152}S^3,
\]
where \(M(\mathbb Z/3\mathbb Z,2)=S^2\cup_3e^3\) is the Moore space attached by a degree-three map. Thus \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z/3\mathbb Z\) and \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{152}\), with no other reduced integral homology. This is a homotopy classification, not merely an equality of homology groups.

The full automorphism group is \(\operatorname{Aut}(T_5)\cong S_5\). On \(\widetilde H_3(X;\mathbb Q)\), its character, in cycle-type order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), equals
\[
(152,0,4,-4,0,-2,-3).
\]
The complete rational decomposition is
\[
5S^{(4,1)}\oplus8S^{(3,2)}\oplus6S^{(3,1,1)}\oplus7S^{(2,2,1)}\oplus5S^{(2,1,1,1)}\oplus S^{(1^5)}.
\]
The trivial representation is absent, so \(\widetilde H^*(|X|/S_5;\mathbb Q)=0\). This conclusion is about rational cohomology only.

## Assumptions and scope
The vertex set of \(T_5\) consists of lexicographically ordered pairs \((a,b)\) with \(0\le a<b\le4\). Its edges are lexicographically ordered pairs of intersecting graph vertices; there are exactly thirty. A face of \(X\) is a set of these edges with pairwise disjoint endpoints in \(T_5\), with oriented simplex order induced by the edge ordering. Every face is enumerated, including the empty face for reduced chains.

There are precisely \((1,30,285,980,1020,144)\) faces of cardinalities zero through five, respectively, totaling 2,460. The geometric realization is finite and connected. All chain computations are over the integers unless a coefficient field is stated.

## Proof
**Acyclic reduction.** Represent a face by a 30-bit integer. Visit edge indices from 29 down to zero. For each as-yet-unpaired face not containing the current edge, in increasing bitmask order, pair it with the face obtained by adding that edge whenever the latter face is also unpaired. This deterministic matching gives 1,146 matched pairs, eight critical two-simplices, 160 critical three-simplices and no other critical simplices in the augmented face poset. Exactly one matched pair contains the empty face. Removing this pair from the matching on the nonempty face poset leaves precisely one critical vertex in addition to those eight and 160 cells.

Orient a face-cover relation upward if matched and downward otherwise. An exhaustive topological sort of the resulting directed Hasse graph visits all 2,460 faces; hence the matching is acyclic. The corresponding ordinary discrete-Morse CW complex has one vertex, no one-cells, eight two-cells and 160 three-cells. In particular its two-skeleton is a wedge of eight two-spheres and its fundamental group is trivial.

**Integral attaching matrix.** For each matched lower face \(l\) and upper face \(h\), let \(\epsilon=[l]\partial h\). Elementary integral chain cancellation replaces the boundary of any other face \(c\) of the same dimension as \(h\) by \(\partial c-([l]\partial c/\epsilon)\partial h\), then deletes \(l,h\). In this fixed cancellation order every pivot is \(+1\) or \(-1\). The residual cellular differential \(B\colon\mathbb Z^{160}\to\mathbb Z^8\) has 625 nonzero entries of absolute value at most four. It is reconstructed exactly by `verify_triangular_matching.py`.

Index the critical two- and three-faces by increasing 30-bit integer. The seven-by-seven minor of \(B\) using zero-indexed rows \((1,2,3,4,5,6,7)\) and columns \((11,20,46,60,62,97,115)\) has determinant \(-1\). The full eight-by-eight minor with columns \((11,13,51,96,97,108,116,117)\) has absolute determinant three. Direct row reduction shows that \(B\) has rank seven over \(\mathbb F_3\), so **every** eight-by-eight minor is divisible by three. The greatest common divisor of its maximal minors is therefore three. Since the seven-minor is a unit, the nonzero integral Smith invariants are exactly seven ones followed by three.

It follows that the cellular reduced homology is \(\widetilde H_2\cong\mathbb Z/3\mathbb Z\) and \(\widetilde H_3\cong\mathbb Z^{160-8}\). More strongly, the eight two-spheres form a simply connected two-skeleton, so the Hurewicz isomorphism \(\pi_2(\bigvee^8S^2)\cong\mathbb Z^8\) identifies the 160 attaching maps with columns of \(B\). Integral row and column basis changes are realized by homotopy equivalences of wedges of two-spheres. Diagonalizing to the Smith form cancels seven degree-one attachments, leaves one degree-three Moore attachment and 152 null attachments. This proves the displayed **homotopy equivalence**, without claiming any equivariance of the splitting.

**The \(S_5\) character.** Any four pairwise intersecting edges of \(K_5\) are a star. The five maximal four-cliques of \(T_5\) therefore recover the five ground symbols, so all graph automorphisms arise from the displayed \(S_5\) action. For each permutation of the five labels, the verifier enumerates its invariant matching faces and their orientation signs. The signed reduced Lefschetz trace equals the alternating sum over all invariant oriented faces, including the empty face with sign \(-1\). Rational homology is concentrated in degree three; its character is the negative of this Lefschetz trace. All 120 permutations are checked, producing the seven character values above. Murnaghan–Nakayama evaluation of the seven irreducible \(S_5\)-characters and exact character inner products give the claimed multiplicities, which sum to dimension 152.

## Verification
Run `python3 verify_triangular_matching.py` with a Python 3 interpreter (standard library only). The program reconstructs all vertices, edges, faces, signed boundaries, the complete directed Hasse graph, the acyclic matching, every unit cancellation, both specified integral minors, and the rank over \(\mathbb F_3\). It independently enumerates the 120 label permutations, computes signed Lefschetz traces, and evaluates the \(S_5\) irreducible multiplicities. The expected output is embedded as `verification_output.txt`. The final marker is `TRIANGULAR_T5_MATCHING_TORSION_CHARACTER_PASS`. No externally generated numerical matrix is assumed.

## Relationship to prior work
Jonsson's 2012 preprint *More Torsion in the Homology of the Matching Complex* studies \(\mathcal M(K_n)\) and its integral torsion. In particular, its table includes \(\widetilde H_2(\mathcal M(K_{10});\mathbb Z)\) with three-torsion. But \(T_5\) has 30 edges, rather than the 45 edges of \(K_{10}\), and matching complexes of subgraphs do not inherit full homology groups or attaching maps from the complete graph. The present Moore summand and representation do not follow from that table.

Bayer, Jelić Milutinović and Vega (2023) prove sphere-wedge results for polygonal **line tilings**, a structurally different graph family; the densely interconnected \(T_5\) is not such a tiling. The indexed four-cut complex of \(T_5\) and the matching complex of the **complementary** Petersen graph are also different simplicial complexes. A source with an equivalent theorem might nevertheless exist outside the inspected literature.

## Limitations
The homotopy decomposition is not asserted to respect \(S_5\). The integral \(S_5\)-action on the order-three homology class and the complete integral homology lattice are not classified. The rationally acyclic full-group quotient need not be contractible, nor is its integral torsion determined. Nothing is asserted for \(T_n\) with \(n\ne5\). An independent mathematical audit has not been performed.

## References
1. Jakob Jonsson, *More Torsion in the Homology of the Matching Complex*, first public arXiv version 2012-03-26, arXiv:1203.5658. https://arxiv.org/abs/1203.5658
2. Margaret Bayer, Marija Jelić Milutinović and Julianne Vega, *General polygonal line tilings and their matching complexes*, first public arXiv version 2022-11-22, arXiv:2211.12559, *Discrete Mathematics* 346 (2023), 113428. https://doi.org/10.1016/j.disc.2023.113428

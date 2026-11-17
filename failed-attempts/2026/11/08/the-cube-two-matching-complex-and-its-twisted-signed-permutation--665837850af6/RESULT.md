# The cube two-matching complex and its twisted signed-permutation homology

## Finding
For the three-dimensional cube graph \(Q_3\), the ordinary two-matching complex has the integral homotopy type
\[
M_2(Q_3)\simeq S^5\vee S^5\vee S^5.
\]
Its full symmetry group \(B_3=(C_2)^3\rtimes S_3\) acts on rational fifth homology as
\[
\widetilde H_5(M_2(Q_3);\mathbb Q)\cong \operatorname{sgn}_{S_3}\otimes U,
\]
where \(U\) is the natural signed coordinate-permutation module of dimension three. This representation is irreducible over \(\mathbb Q\).

## Assumptions and scope
Identify the eight vertices of \(Q_3\) with the binary triples, encoded by integers from zero to seven. Two vertices are adjacent exactly when their bit strings differ in one position. Order the twelve undirected edges lexicographically:
\[
(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7).
\]
The simplicial vertices of \(X=M_2(Q_3)\) are the graph edges. For every subset \(F\) of the twelve graph edges, \(F\in X\) if and only if every graph vertex has at most two incident selected edges. Equivalently, because \(Q_3\) is cubic, \(F\) must avoid containing any of the eight complete three-edge vertex stars. Both definitions are checked exhaustively.

Every cube automorphism is determined by the image of vertex zero (eight choices) and the induced permutation of its three neighbors (six choices), so the group has at most 48 elements. The 48 distinct affine-coordinate maps realize this bound: the full cube automorphism group consists of all maps of binary triples given by a coordinate permutation \(\sigma\in S_3\) and output-bit flips \(b\in\{0,1\}^3\). With the convention that input coordinate \(i\) maps to output coordinate \(\sigma(i)\), its character on fifth homology is
\[
\chi_5(\sigma,b)=\operatorname{sgn}(\sigma)
\sum_{\{i:\sigma(i)=i\}}(-1)^{b_i}.
\]
The signed-permutation action \(U\) has signed diagonal entries \((-1)^{b_i}\) at fixed coordinate positions. The formula includes the identity, all reflections, all rotations and all compositions.

## Proof
**Face enumeration.** Iterate over each of the \(2^{12}=4096\) selected-edge subsets and retain those with selected degree at most two at each graph vertex. A second membership test independently rejects any mask containing a complete three-edge star. The tests agree at every mask. There are exactly 1,699 faces including the empty face, with face vector in dimensions zero through seven
\[
(12,66,212,423,516,352,108,9).
\]

**Acyclic matching.** Give each edge its index in the displayed lexicographic ordering, from zero to eleven. Begin with all nonempty faces unmatched. For index eleven down to zero, match every currently unmatched pair \(F,F\cup\{e_i\}\) where \(e_i\notin F\) and the larger face is also currently unmatched, processing available lower face masks in increasing integer order. The resulting list of 847 pairs and four critical masks appears in `certificate.json`. The critical masks are \(888,1235,1421,2048\), of dimensions five, five, five and zero respectively. The standalone checker independently reconstructs the pairs and confirms every matched covering relation has exactly one added edge and each face appears at most once.

For each covering relation \(A\subset B\) between nonempty faces, direct it upward \(A\to B\) if it is a matched pair and downward \(B\to A\) otherwise. The checker enumerates all 7,980 incidences, runs a complete topological ordering of this directed graph and visits all 1,698 nonempty faces. It therefore verifies that this finite directed graph is acyclic, not merely that no short cycle was found. By the acyclic matching theorem of discrete Morse theory, \(X\) is homotopy equivalent to a CW complex with exactly one zero-cell and three five-cells, and no cells in intermediate dimensions. The only possible cellular attaching maps are constant, as the four-skeleton is a point. Hence the CW complex is a wedge of three five-spheres, proving the integral homotopy claim.

**Symmetry.** A graph automorphism permutes the twelve graph edges and hence all simplices. For each of the 48 cube automorphisms, sum over fixed simplices \(F\ne\varnothing\) the term \((-1)^{|F|-1}\) times the sign of the induced permutation of the ordered edges in \(F\). This is the ordinary Lefschetz number \(L(g)\) computed from exact signed simplicial chain traces. The established homotopy type implies \(L(g)=1-\chi_5(g)\), since \(H_0\) is the trivial line and fifth homology is the only nonzero positive-degree homology. Exhaustive integer comparison for all 48 automorphisms gives
\[
\chi_5(\sigma,b)=\operatorname{sgn}(\sigma)\sum_{i:\sigma(i)=i}(-1)^{b_i}.
\]
This is precisely the rational character of \(\operatorname{sgn}_{S_3}\otimes U\). Semisimplicity of rational representations of finite groups identifies the two rational modules. Irreducibility follows because the three independent coordinate sign flips distinguish the three coordinate weight lines, and the coordinate permutations act transitively on those lines.

## Verification
`verify.py` is a standalone standard-library Python program. In the same directory, run `python verify.py`; it reconstructs the ordered graph, both face-membership tests, the complete matching, its 7,980 oriented Hasse incidences, and its directed acyclicity. It compares the fully reconstructed `certificate.json` byte-for-byte with the included certificate. It also constructs a second matching with the opposite sweep order (846 pairs, one critical vertex, one critical four-cell and four critical five-cells) and verifies its acyclicity. Independently, sparse mod-two boundary elimination gives ranks \((11,55,157,266,250,99,9)\) in chain degrees one through seven, consistent with one degree-five reduced homology group of rank three. Finally, exact integer Lefschetz calculations check all 48 symmetry cases. The included `verification_output.txt` records the expected successful output. A successful replay regenerates these assertions; the recorded output alone is not the proof.

## Relationship to prior work
The definition and discrete-Morse approach are motivated by Julianne Vega's *2-Matching Complexes* (arXiv:1909.10406, first publicly posted September 23, 2019). The full text analyzes clawed graphs, whiskered cycles, wheel graphs and perfect caterpillars, not the unwhiskered cubic cube. Anurag Singh's *Bounded Degree Complexes of Forests* (arXiv:1910.12793) studies forests, whereas the cube has cycles; his *Higher Matching Complexes of Complete Graphs and Complete Bipartite Graphs* (arXiv:2006.13632) studies complete graph families. Although \(Q_3\cong K_{4,4}\setminus M\) for a perfect matching \(M\), it is not itself a complete bipartite graph, and the inclusion into \(K_{4,4}\) does not give a homotopy equivalence of the two-matching complexes.

A publicly indexed record establishes the ordinary one-matching complex of the cube is \(\bigvee^4S^2\), a different degree constraint. Another public indexed result computes the two-matching complex of the Petersen graph as \(\bigvee^4S^7\), a different graph. A result for \(M_2(K_{4,4})\) does not determine the deleted-matching subgraph case. Searches for the cube, the four-crown graph description, bounded-degree complexes and the twisted character did not locate an implication covering the present combined result. These searches cannot prove uniqueness of the result.

## Limitations
The statement is for the three-dimensional cube alone. It does not determine two-matching homotopy for higher-dimensional cubes, or an equivariant homotopy equivalence. The rational symmetry module is determined by its character, but no integral equivariant lattice is classified. The nearest public indexed mathematical records were available as descriptions rather than full manuscripts, so equivalent work not identified in accessible primary literature remains a bibliographic risk.

## References
1. J. Vega, *2-Matching Complexes*, arXiv:1909.10406, initial posting September 23, 2019, https://arxiv.org/abs/1909.10406.
2. A. Singh, *Bounded Degree Complexes of Forests*, arXiv:1910.12793, initial posting October 28, 2019, https://arxiv.org/abs/1910.12793.
3. A. Singh, *Higher Matching Complexes of Complete Graphs and Complete Bipartite Graphs*, arXiv:2006.13632, https://arxiv.org/abs/2006.13632.
4. Publicly indexed result, *The cube matching complex is a wedge of four two-spheres*, public research record dated October 11, 2026 (description inspected; full manuscript not accessed).
5. Publicly indexed result, *The Petersen 2-matching complex is a wedge of four seven-spheres*, public research record dated October 4, 2026 (description inspected; full manuscript not accessed).

# The McGee graph Rips filtration has an oriented five-sphere at scale three

## Finding
For the McGee graph \(M\), its inclusive vertex-shortest-path Vietoris–Rips complexes \(R_r=\operatorname{VR}_{\le r}(M)\) have the complete **integral homotopy** filtration
\[
R_r\simeq\begin{cases}
\bigvee^{23}S^0,&0\le r<1,\\
\bigvee^{13}S^1,&1\le r<3,\\
S^5,&3\le r<4,\\
*,&r\ge4.
\end{cases}
\]
The natural inclusion \(R_1\hookrightarrow R_2\) is a simple-homotopy equivalence. At scale three, \(R_3\) is a **pure eleven-dimensional complex** with the homotopy type of one five-sphere; in particular it is not shellable.

The full automorphism group \(A=\operatorname{Aut}(M)\), of order \(32\), acts nontrivially on \(\widetilde H_5(R_3;\mathbb Z)\cong\mathbb Z\). The action is the orientation character
\[
\chi(g)=\operatorname{sgn}(\pi_g)(-1)^{\sum_{j=1}^6\delta_j(g)},
\]
where \(\pi_g\) permutes the six distance-four four-cycle components and \(\delta_j(g)\in\{0,1\}\) records whether the induced map swaps the two bipartition classes of the source component. Exactly sixteen automorphisms have \(\chi=+1\), and sixteen have \(\chi=-1\). The index-three rotation \(i\mapsto i+3\pmod {24}\) has \(\chi=-1\); hence the group-fixed part of the top homology is zero.

Consequently the reduced field-persistence barcode consists of 23 degree-zero bars on \([0,1)\), 13 degree-one bars on \([1,3)\), and one degree-five bar on \([3,4)\), with no other positive-degree bars. There is also the ordinary unreduced infinite connected-component bar.

## Assumptions and scope
Vertices are the integers \(0,\ldots,23\). Include all cycle edges \(\{i,i+1\pmod {24}\}\), and for each \(i\) the undirected chord \(\{i,i+s_i\pmod {24}\}\), where \((s_0,\ldots,s_{23})\) is \((12,7,-7)\) repeated eight times. Treat repeated edge descriptions once. This is the standard McGee graph LCF representation; \(-12\) and \(12\) represent the same chord mod \(24\). Its 24 vertices have degree three, giving 36 edges, girth seven, and diameter four.

Every simplex of \(R_r\) is a nonempty vertex subset whose pairwise shortest-path distances in \(M\) are all at most the real threshold \(r\). When computing face vectors, the empty face is included once. The theorem concerns ordinary, nonequivariant homotopy types and the specified one-dimensional integral top-homology representation; it does not assert an equivariant homotopy equivalence or a canonical integral sphere basis.

## Proof
**Distances and early scales.** Breadth-first search from all 24 vertices gives 36, 72, 144 and 24 unordered pairs at respective distances one, two, three and four. In particular \(M\) is connected and has diameter four. At scale zero there are 24 points. As the girth is seven, \(R_1=M\), a connected graph of cycle rank \(36-24+1=13\); hence \(R_1\simeq\bigvee^{13}S^1\).

**A relative collapse at scale two.** A face-induction over ordered vertex sets gives the complete face vector \((f_0,f_1,f_2,f_3)=(24,108,96,24)\). All 96 triangles and 24 tetrahedra are removed by exactly 96 explicit elementary face/coface collapses, without ever removing an original vertex or edge of \(M\). For each step the attached verifier reconstructs the current face poset, selects a face contained in exactly one immediate coface, checks the incidence, and removes both. This works in two opposite deterministic orders, and in both cases the remaining simplicial complex is exactly the original graph \(M\) (24 vertices and 36 edges). The graph inclusion \(R_1\hookrightarrow R_2\) is therefore a simple-homotopy equivalence. Since elementary collapses preserve the homotopy type, \(R_2\simeq\bigvee^{13}S^1\), and no circle bar dies at scale two.

**A join description at scale three.** Let \(D_4\) be the graph on the same 24 vertices whose edges are exactly the vertex pairs at \(M\)-distance four. The complete distance table shows that \(D_4\) is the disjoint union of six four-cycles, on vertex sets
\[
\{0,6,12,18\},\ \{1,5,13,17\},\ \{2,10,14,22\},\ \{3,9,15,21\},\ \{4,8,16,20\},\ \{7,11,19,23\}.
\]
For each block, its distance-four edges are exactly the four edges between the two opposite pairs. Two distinct vertices are adjacent in the scale-three graph precisely when they are *not* adjacent in \(D_4\). Therefore, by the flag definition,
\[
R_3=\operatorname{Ind}(D_4)=\operatorname{Ind}(C_4)*\cdots*\operatorname{Ind}(C_4)\quad\text{(six factors)}.
\]
Each \(\operatorname{Ind}(C_4)\) is the disjoint union of two ordinary one-simplices (opposite vertex pairs), so it simplicially collapses to two points, i.e. \(S^0\). Joins preserve homotopy equivalences, and a sixfold join of zero-spheres is \(S^5\). Moreover, each maximal face chooses an opposite pair from every component, so \(R_3\) has \(2^6=64\) facets, all of cardinality 12; it is pure of dimension eleven. Its generating polynomial by face cardinality, including the empty face, is \((1+4t+2t^2)^6\), whose coefficients sum to \(7^6=117649\). At scale four the complex is the full 23-simplex, hence contractible.

**Orientation character.** For each four-cycle, the reduced zero-homology of its two components is a rank-one lattice; interchanging the two components reverses its generator. A permutation of the six join factors changes the top join orientation by the sign of that permutation. The displayed formula for \(\chi\) follows. Exact adjacency-preserving backtracking lists all 32 automorphisms of the original graph and checks 16 with each orientation sign. In particular rotation by three of the LCF indices preserves adjacency and has negative top orientation. Thus the integral top-homology module has no nonzero group-fixed vector.

**Persistence.** The relative collapse proves the scale-one inclusion is an equivalence at scale two. The target at scale three has reduced homology only in degree five, while scale two has it only in degree one; all positive-degree maps across the transition vanish for degree reasons. The target at scale four is contractible. This determines all the asserted barcode intervals over every field, and the integral homology of each stage.

## Verification
Run \(\texttt{python3 mcgee_rips_verify.py}\) using only the Python standard library. The executable reconstructs all 24 vertices and 36 edges, verifies girth seven and diameter four, exhaustively enumerates all scale-two cliques and verifies every relative elementary-collapse incidence in both orders. It checks each distance-four connected component is a four-cycle, the six bipartitions, the 64 maximal scale-three facets, and the join face polynomial. Independent exhaustive graph-automorphism backtracking checks all 32 symmetries and their orientation signs. The JSON execution output is embedded as \(\texttt{mcgee_rips_verification_output.json}\). All calculations concern only the finite, explicitly specified graph; the topological implications are established in the proof above rather than inferred from numerical homology alone.

## Relationship to prior work
Adamaszek and Adams (first publicly posted March 1, 2021) develop graph-metric Vietoris–Rips homotopy calculations for Hamming hypercubes, not for the McGee graph. Parks and Marchette (2016) analyze graph-power persistence and a girth-controlled stability range: those general ideas explain why the radius-two stage might retain the original graph, but do not determine this graph's radius-three join or its integral orientation action.

The previously reported ordinary independence complex \(\operatorname{Ind}(M)\simeq S^5\) uses **edges of the McGee graph as the forbidden pairs**. The present radius-three Rips complex is instead \(\operatorname{Ind}(D_4)\), where \(D_4\) is six disjoint squares, so the results concern different complexes and neither assertion follows just from equality of homotopy dimensions. A published scale-three calculation for the Tutte–Coxeter incidence graph concerns a different graph and yields 256 three-spheres, not the present result. The searched literature and indexed research records disclosed no exact or stronger theorem determining both the McGee Rips radius-three type and its automorphism orientation character.

## Limitations
The conclusions are for one specified finite 24-vertex graph, its unweighted shortest-path metric, and inclusive thresholds. No analogous statement is asserted for all cages, all cubic graphs, or arbitrary higher powers. The ordinary independence-complex result for the McGee graph is distinct and is not claimed here. Exact computations and published-record searches cannot rule out equivalent unindexed work. The symmetry statement specifies the top integral homology character only; no equivariant homotopy classification is claimed. Independent audit has not been performed.

## References
1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040v1 (first posted 2021-03-01), https://arxiv.org/abs/2103.01040.
2. A. D. Parks and D. J. Marchette, *Persistent homology in graph power filtrations*, Royal Society Open Science 3 (2016), 160228, https://doi.org/10.1098/rsos.160228.
3. E. W. Weisstein, *McGee Graph*, MathWorld (the graph's LCF representation, girth and automorphism order), https://mathworld.wolfram.com/McGeeGraph.html.
4. *The McGee graph independence complex is a five-sphere* (publicly indexed research result, 2026), distinct simplicial construction.
5. *The scale-three Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres* (publicly indexed research result, 2026), distinct underlying graph.

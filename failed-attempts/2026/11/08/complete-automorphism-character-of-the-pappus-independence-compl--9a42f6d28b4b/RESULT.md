# Complete automorphism character of the Pappus independence complex

## Finding
Let \(P\) be the eighteen-vertex Pappus graph, with LCF presentation \([5,7,-7,7,-7,-5]^3\), let \(G=\operatorname{Aut}(P)\), and let \(K=\operatorname{Ind}(P)\). The known nonequivariant homotopy type is \(K\simeq\bigvee^{10}S^4\). The result here is the **complete character** \(\chi:G\to\mathbb Z\) of the rational ten-dimensional module \(\widetilde H_4(K;\mathbb Q)\) on all thirteen conjugacy classes of \(G\), whose order is \(216\):

| Class | Class size | Element order | Cycles on eighteen graph vertices | \(\chi\) |
|:--:|--:|--:|:--|--:|
| 00 | 1 | 1 | \(1^{18}\) | 10 |
| 01 | 9 | 2 | \(1^{6}2^{6}\) | -2 |
| 02 | 18 | 2 | \(2^{9}\) | 0 |
| 03 | 18 | 2 | \(1^{4}2^{7}\) | 2 |
| 04 | 2 | 3 | \(3^{6}\) | 1 |
| 05 | 12 | 3 | \(3^{6}\) | -2 |
| 06 | 12 | 3 | \(1^{3}3^{5}\) | 1 |
| 07 | 18 | 4 | \(2^{3}4^{3}\) | 2 |
| 08 | 18 | 6 | \(3^{2}6^{2}\) | 1 |
| 09 | 36 | 6 | \(1^{1}2^{1}3^{1}6^{2}\) | -1 |
| 10 | 36 | 6 | \(6^{3}\) | 0 |
| 11 | 18 | 12 | \(6^{1}12^{1}\) | -1 |
| 12 | 18 | 12 | \(6^{1}12^{1}\) | -1 |

The class labels refer to the explicit representative permutations in `verify_full_aut_output.txt` and `verify_signed_trace.py`; class size, order, cycle type and character jointly disambiguate the classes. In particular, the two order-three classes 04 and 05 have the **same permutation cycle type** \(3^6\) but different homology traces \(1\) and \(-2\).

Moreover,
\[
\dim_{\mathbb Q}\widetilde H_4(K;\mathbb Q)^G
 =\frac1{216}\sum_{g\in G}\chi(g)=0,
\qquad
\langle\chi,\chi\rangle_G
 =\frac1{216}\sum_{g\in G}\chi(g)^2=2.
\]
Consequently the complexification of this rational representation is the direct sum of precisely **two inequivalent nontrivial complex irreducible representations**, each occurring once. No claim is made identifying their individual degrees or their integral representation lattices.

## Assumptions and scope
The Pappus graph is the simple cubic Levi graph of the Pappus configuration; its graph vertices are labeled \(0,\ldots,17\). Start with the Hamiltonian cycle \(i\sim i+1\pmod{18}\), and add edges \(i\sim i+a_i\pmod{18}\) using \((a_0,\ldots,a_{17})=(5,7,-7,7,-7,-5)^3\); duplicate undirected edges are identified. This yields exactly 27 edges and degree three at each vertex. The independence complex consists of all subsets with no graph edge. An automorphism of this graph acts by permuting simplex vertices; all homology representations in the claim are over \(\mathbb Q\). Group elements act on the left by \(g\cdot h(i)=g(h(i))\).

## Proof
**Homology concentration.** Exhaustively enumerate all independent subsets of the 18-element labeled vertex set. The counts of nonempty faces of dimensions zero through eight are
\[
(18,126,438,801,756,348,90,18,2),
\]
with 2,597 nonempty faces. The deterministic matching in `verify_full_aut.py`, using vertex order `(11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12)`, pairs exactly 1,293 cover-related faces, leaving one critical vertex and ten critical four-simplices. On **all** 11,430 nonempty face-poset covers, reverse the matched cover and orient all other covers downward; topological sorting visits all 2,597 vertices, proving acyclicity. Forman's discrete-Morse theorem gives \(K\simeq\bigvee^{10}S^4\), as previously reported in the published work cited below. This step is reproduced here solely to establish the homology-concentration premise independently, not claimed as new.

**Group enumeration.** Search exhaustively for all bijections \(g\) of the eighteen vertices satisfying \(uv\in E(P)\Longleftrightarrow g(u)g(v)\in E(P)\). The search recursively extends partial maps, testing adjacency and nonadjacency to all previously mapped vertices; hence no graph automorphism is skipped. Exactly 216 bijections survive. The code verifies identity, inverses, and all \(216^2\) products. Their conjugation orbits yield exactly thirteen conjugacy classes of sizes shown in the table, summing to 216.

**Character formula.** Fix \(g\in G\). Its cycles on the graph vertex set partition the vertices. A \(g\)-invariant face of \(K\) is a union of entire cycles; a cycle containing a graph edge can never be selected. Make a quotient graph \(Q_g\) whose vertices are those eligible cycles, with two quotient vertices adjacent if some graph edge joins their respective cycles. Then the invariant simplices of \(K\) correspond bijectively to the independent sets of \(Q_g\).

For an invariant simplex consisting of \(k\) vertices and \(c\) cycles of \(g\), the determinant of \(g\) on its oriented simplex is \((-1)^{k-c}\). Its contribution to the non-augmented simplicial Lefschetz sum is \((-1)^{k-1}(-1)^{k-c}=(-1)^{c+1}\). Including the empty face gives the **reduced** Lefschetz number
\[
\widetilde L(g\mid K)=-I(Q_g,-1),\qquad
I(Q,t)=\sum_{A\in\operatorname{Ind}(Q)}t^{|A|}.
\]
Because the only nonzero reduced rational homology is in even degree four, \(\widetilde L(g\mid K)=\chi(g)\). The recurrence \(I(Q,-1)=I(Q-v,-1)-I(Q-N[v],-1)\) computes each of the thirteen class values exactly with integer arithmetic. The output provides a concrete representative permutation for each class.

**Independent chain-level calculation.** The second standalone program constructs every independent simplex by recursive backtracking, computes mod-two simplicial boundary ranks, and, for the thirteen representative permutations, calculates signed chain traces **directly** by sorting the images of setwise-fixed oriented simplices. Subtracting the ordinary zeroth-homology trace \(1\) yields all thirteen character values in exact agreement with the quotient-polynomial method. The mod-two reduced Betti vector is \((0,0,0,0,10,0,0,0,0)\), agreeing with the integral Morse description.

**Representation consequences.** Weighting the character values by the class sizes in the table gives exactly \(\sum_g\chi(g)=0\) and \(\sum_g\chi(g)^2=432=2|G|\). Averaging gives no fixed vectors. By the orthonormality of irreducible complex characters, \(\langle\chi,\chi\rangle=\sum_i m_i^2=2\) implies exactly two distinct constituents, each of multiplicity one. Their nontriviality follows from the fixed-space dimension zero.

## Verification
Execute `python3 verify_full_aut.py` and `python3 verify_signed_trace.py` using Python 3.9 or later; only the standard library is required. Both scripts and exact stdout snapshots are embedded alongside this document. The first independently verifies the entire face-poset matching, exhaustive group enumeration and conjugacy partition, and the quotient-graph character formula for all 216 automorphisms. The second uses an unrelated recursive face generator and signed simplex-orientation traces on each of thirteen class representatives, and calculates mod-two boundary ranks. Executable assertions reject mismatches. The full-group character includes a previously published order-three subgroup trace \(-2\) as one consistency check, not as a novelty claim.

## Relationship to prior work
The established nonequivariant Pappus result \(\operatorname{Ind}(P)\simeq\bigvee^{10}S^4\), and the character \((10,-2,-2)\) on the order-three translation subgroup, appear in the already available work *Order-three symmetry on Pappus independence homology* (public research note, October 2026). That work explicitly restricts its representation claim to the subgroup and does **not** determine the 216-element automorphism-group character. The present table refines it on all conjugacy classes; the two order-three classes with cycle type \(3^6\) and different traces cannot be inferred from the subgroup character, the Betti numbers, or only the graph-vertex cycle structure.

Przytycki and Silvero (2016) study independence-complex homotopy types for circle-graph families; Tsukuda (2017) supplies a general incidence-graph homotopy equivalence; Berghoff (2020/2022) supplies general homology methods. Inspection of the relevant mathematical statements found no full Pappus automorphism-character calculation, nor a result whose hypotheses and conclusion force the thirteen traces. The standard Pappus graph and its LCF labeling are recorded by MathWorld. The full character is finer information than the homotopy type, which does not specify how automorphisms act.

## Limitations
This is a finite, exact character classification for the canonical eighteen-vertex graph, not a theorem about all cubic symmetric graphs or all incidence configurations. The integral \(\mathbb Z[G]\)-module, the precise isomorphism types/degrees of the two complex irreducible constituents, and equivariant homotopy equivalences are not determined. The repeatable finite computations prove the stated finite result when the executable verifiers are checked; they do not constitute an external audit. Publication-priority searches cannot rule out equivalent unindexed results or a relevant inaccessible paper.

## References
1. J. H. Przytycki and M. Silvero, *Homotopy type of circle graphs complexes motivated by extreme Khovanov homology*, arXiv:1608.03002, version 1 first made public 2016-08-09. https://arxiv.org/abs/1608.03002
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics **12** (2017), 28–46, DOI:10.55016/ojs/cdm.v12i1.62277. https://cdm.ucalgary.ca/article/view/62277
3. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, Combinatorial Theory **2** (2022). https://arxiv.org/abs/2008.06267
4. *Order-three symmetry on Pappus independence homology*, publicly indexed research result, October 2026; in particular its subgroup character and previously known sphere-wedge proof.
5. E. W. Weisstein, *Pappus Graph*, MathWorld. https://mathworld.wolfram.com/PappusGraph.html

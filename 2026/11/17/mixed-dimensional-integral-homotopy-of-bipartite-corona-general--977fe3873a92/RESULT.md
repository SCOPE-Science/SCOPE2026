# Mixed-dimensional integral homotopy of bipartite-corona general-position complexes

## Finding
For all integers \(a,b\ge2\), form \(H_{a,b}=K_{a,b}\circ K_1\) by adding one pendant leaf at every vertex of \(K_{a,b}\). Write \(\mathcal{GP}(H_{a,b})\) for the simplicial complex consisting of vertex sets with no three distinct vertices on any graph geodesic. Then
\[
|\mathcal{GP}(H_{a,b})|\simeq
\bigvee^{ab+a+b}S^1\ \vee\ \bigvee^{b-1}S^a\ \vee\ \bigvee^{a-1}S^b.
\]
All homotopy equivalences and homology statements are integral. When \(a=b\), the two higher-dimensional multiplicities add in degree \(a\). For example, \(\mathcal{GP}(H_{2,3})\simeq\bigvee^{11}S^1\vee\bigvee^{2}S^2\vee S^3\); in the balanced case \(\mathcal{GP}(H_{3,3})\simeq\bigvee^{15}S^1\vee\bigvee^{4}S^3\).

## Assumptions and scope
All graphs are finite, simple and undirected, with path metric \(d_H\). A subset \(\sigma\) is in general position if for every three distinct vertices \(u,v,w\in\sigma\) one has \(d_H(u,w)\ne d_H(u,v)+d_H(v,w)\), and similarly for the other two choices of middle vertex. The complex includes the empty face. The graph has shores \(A=\{a_1,\ldots,a_a\}\), \(B=\{b_1,\ldots,b_b\}\), with leaves \(a_i'\) and \(b_j'\). There are no restrictions on \(a,b\) beyond \(a,b\ge2\). The wedge equivalence is not asserted equivariant under graph automorphisms.

For a finite set \(W\), write \(\Delta_W\) for the simplex with vertex set \(W\); for \(b\) individual vertices write \(D_b\) for their discrete simplicial complex. Let \(O_A=*_{i=1}^{a}\{a_i,a_i'\}\), in which every bracket is two isolated vertices, and define \(O_B=*_{j=1}^{b}\{b_j,b_j'\}\). Thus \(|O_A|\cong S^{a-1}\) and \(|O_B|\cong S^{b-1}\).

## Proof
**1. Geodesic face classification.** A leaf cannot be internal to a shortest path. A selected root \(v\) cannot coexist with its own leaf and a third vertex, since \(v\) lies on every path from that leaf to the third vertex. A selected root on the \(A\)-shore cannot coexist with two selected vertices projected to distinct \(B\)-roots: the root is internal on a shortest path between those vertices. By the symmetric argument, a selected \(B\)-root forbids any two selected vertices projected to distinct \(A\)-roots. Consequently a general-position set of size at least three either (i) contains only leaves, (ii) contains roots only from \(A\), chooses at most one endpoint of each \(\{a_i,a_i'\}\), and chooses at most one \(B\)-leaf, or (iii) satisfies the symmetric \(B\)-condition. Conversely, in each of these configurations no selected root lies internally on a shortest path between two other selected vertices, by inspection of all possible root projections in the complete bipartite base. The remaining general-position two-element faces not already in these types are precisely the \(ab\) cross-shore root edges \(\{a_i,b_j\}\) and the \(a+b\) matched root–own-leaf edges \(\{v,v'\}\). No such edge belongs to a simplex of size at least three. This is a specialization of the structural characterization in Wang's Lemma 3 (and Lemma 3 of his bipartite follow-up); all graph-distance restrictions used here have been independently verified.

**2. Decomposition.** Put \(L=A'\sqcup B'\), and let \(D_{A'}\) and \(D_{B'}\) be the discrete leaf complexes. Define
\[
Y=\Delta_L\cup(O_A*D_{B'})\cup(O_B*D_{A'}).
\]
By step 1, \(\mathcal{GP}(H_{a,b})\) is obtained from \(Y\) by attaching exactly \(ab+a+b\) independent edges, each along its two endpoints, and no faces of dimension at least two.

**3. The two sphere bouquets.** In the first join,
\[
\Delta_L\cap(O_A*D_{B'})=\Delta_{A'}*D_{B'},
\]
which is contractible because \(\Delta_{A'}\) is a nonempty simplex. Similarly, \(\Delta_L\cap(O_B*D_{A'})=\Delta_{B'}*D_{A'}\) is contractible. The two joins intersect one another only along leaf faces, all of which are contained in \(\Delta_L\). Collapsing the contractible subcomplex \(\Delta_L\) to a point preserves the homotopy type of \(Y\): it is a connected CW subcomplex of a connected finite CW complex. Consequently
\[
Y\simeq (O_A*D_{B'})\vee(O_B*D_{A'}).
\]
Since joining the sphere \(S^{a-1}\) with a discrete set of \(b\) points yields a wedge of \(b-1\) spheres of dimension \(a\), and similarly on the other side, we have
\[
Y\simeq\bigvee^{b-1}S^a\vee\bigvee^{a-1}S^b.
\]
Both joins are connected because \(a,b\ge2\); hence \(Y\) is connected.

**4. Attached edges.** Every endpoint of each of the \(ab+a+b\) remaining edges belongs to \(Y\). Attaching one interval between any two points of a path-connected CW space adds a free circle summand, by contracting a connecting path in a homotopy-equivalent mapping-cylinder model; applying this successively adds \(ab+a+b\) circle summands and proves the formula. All arguments are integral homotopy arguments, so no torsion or additional homology can remain.

## Verification
The standalone program `verify_corona_gp.py` reconstructs each corona graph from its adjacency list, computes exact graph distances by breadth-first search and lists every forbidden geodesic triple without using the structural classification. It then enumerates **all** simplices independently in two ways: from forbidden triples, and from the claimed shore/leaf decomposition. Exact equality was checked for \((a,b)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\). The checker constructs augmented simplicial boundary matrices over \(\mathbb F_2\) and compares the complete reduced Betti table to the formula. The six cases contain 53, 119, 297, 230, 501 and 929 nonempty simplices respectively, all passing. A finite computation is corroborating evidence, not proof of the infinite statement: that proof is steps 1–4.

Run `python3 verify_corona_gp.py` from the directory containing this document. The accompanying `verification_output.txt` records the observed complete face vectors, exact boundary ranks and PASS marker. No dependencies beyond Python 3's standard library are required.

## Relationship to prior work
Rather's March 6, 2026 manuscript studies the general-position polynomial and coronas, providing the recent context. Wang's May 27, 2026 preprint, particularly Lemmas 2–3, proves the **complete face characterization** of general-position sets for arbitrary complete multipartite coronas, and his May 30 bipartite sequel, Lemmas 3–4, gives a specialized characterization and the face-count polynomial. Those prior combinatorial results are explicitly credited: their characterizations imply the exact face data used in step 1. The mathematical contribution assessed here is the subsequent topological pushout analysis and full **integral homotopy wedge**, rather than a new counting formula or a new face characterization. Searches of relevant indexed results and full texts identified no previous topological classification of this specific family. A differently expressed topological corollary of those papers remains a residual novelty risk.

## Limitations
This covers exactly one new leaf per original vertex and complete bipartite base graphs with both shores of size at least two. It does not classify arbitrary multipartite coronas with three or more shores, different pendant multiplicities, or equivariant homotopy. The prior face characterization already determines the simplicial complex completely, and the present result should be understood as a structural topological refinement, not an independent characterization of general-position sets. The homotopy equivalence is not a canonical map of graph-automorphism spaces. The finite tests used only mod-two homology; integral homotopy is proved theoretically.

## References
1. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930, first submitted 2026-03-06, https://arxiv.org/abs/2603.06930 .
2. X. Wang, *A Complete Multipartite Counterexample to Corona-Unimodality of General Position Polynomials*, 2026-05-27, DOI:10.5281/zenodo.20411641, https://www.researchgate.net/publication/405328607_A_Complete_Multipartite_Counterexample_to_Corona-Unimodality_of_General_Position_Polynomials .
3. X. Wang, *Complete Bipartite Counterexamples and the Rational-Slope Phase Diagram for Corona-Unimodality of General Position Polynomials*, 2026-05-30, DOI:10.5281/zenodo.20453868, https://www.researchgate.net/publication/405463285_Complete_Bipartite_Counterexamples_and_the_Rational-Slope_Phase_Diagram_for_Corona-Unimodality_of_General_Position_Polynomials .

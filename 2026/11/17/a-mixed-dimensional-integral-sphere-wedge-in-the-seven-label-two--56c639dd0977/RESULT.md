# A mixed-dimensional integral sphere wedge in the seven-label two-matching complex

## Finding
Let \(K_7\) be the simple complete graph on vertices \(\{0,1,\ldots,6\}\). Let \(M_2(K_7)\) be the abstract simplicial complex whose vertices are the \(21\) edges of \(K_7\), and whose faces are edge sets having graph-theoretic degree at most two at every graph vertex. Then the following is an **integral, nonequivariant homotopy equivalence**:
\[
\boxed{|M_2(K_7)|\simeq S^4\vee\bigvee^{181} S^5.}
\]
In particular, its reduced integral homology is \(\mathbb Z\) in degree four and \(\mathbb Z^{181}\) in degree five, and vanishes in every other degree. The statement is stronger than a numerical homology calculation: it excludes nontrivial attaching maps and Moore-space summands. The first seven-label case has classes in two consecutive dimensions, unlike the previously calculated six-label sphere wedge.

## Assumptions and scope
The graph is loopless, undirected, and simple. An edge set contributes a face if and only if none of its seven vertices is incident to three selected edges; triangles are **allowed**. This last condition distinguishes \(M_2(K_7)\) from the three-clique-free complex of the triangular graph \(L(K_7)\), which additionally forbids triangles in the selected edge set. The claim concerns precisely seven graph vertices and uniform degree bound two. Chains and cellular incidence coefficients are over \(\mathbb Z\), with each simplex oriented by increasing lexicographic order of its graph edges.

## Proof
**Full finite face set.** Index the \(21\) graph edges lexicographically, and represent each selected-edge set by a \(21\)-bit nonnegative integer. For each graph vertex, precompute its six incident-edge positions. A mask is permitted exactly when its intersection with every incidence mask has popcount at most two. Exhausting all nonzero masks yields the following exact face counts by dimension: \((21,210,1190,3780,6132,3997,465)\), hence \(15{,}795\) nonempty faces. This includes all possible triangles and faces in dimensions up to six.

**Acyclic finite matching.** Starting with this face set, process graph-edge positions in increasing index order. At position \(i\), pair each surviving face \(a\) omitting bit \(i\) with \(a\cup\{i\}\), if both remain, then remove both from subsequent stages. Each pair differs by one simplex vertex. The construction gives exactly \(7{,}675\) disjoint pairs. Its unmatched faces comprise one vertex, \(132\) four-simplices, and \(312\) five-simplices; there are no other critical faces. Reverse the arrows of all matched face/coface covers in the complete ordinary Hasse diagram, retaining every unmatched cover arrow downwards. A complete topological sort of the resulting digraph on \(15{,}795\) faces and \(77{,}007\) cover incidences removes every face. Thus the matching is acyclic and Forman's discrete Morse theorem supplies a homotopy-equivalent CW complex with exactly these critical cells.

**Signed integer attaching data.** Let \(\epsilon(a,b)\in\{\pm1\}\) be the oriented incidence of a facet \(a\) of \(b\). Recursively project a face to the critical chains: for a critical face take its unit generator; for a matched upper face take zero; for a matched lower face \(a\) paired with \(b\), use
\[
P(a)=-\epsilon(a,b)\sum_{a'\prec b,\,a'\ne a}\epsilon(a',b)P(a').
\]
The verified acyclicity ensures termination. Apply this projection to the ordinary boundaries of the \(312\) critical five-cells. The resulting exact integral cellular boundary matrix \(D:\mathbb Z^{312}\to\mathbb Z^{132}\) has Smith normal form containing **exactly \(131\) unit diagonal entries and otherwise zero entries**. The supplied checker constructs the full matrix and calculates these invariants using exact integer arithmetic, not rank estimates over a field.

**Upgrade to homotopy.** The critical CW complex has one zero-cell, no cells in dimensions one through three, \(132\) four-cells, and \(312\) five-cells. Hence its four-skeleton is a wedge of \(132\) four-spheres. By the Hurewicz theorem, \(\pi_4(\bigvee^{132}S^4)\cong\mathbb Z^{132}\), and the five-cell attaching maps are classified by the columns of \(D\). Integral unimodular changes of sphere and attaching-cell generators realize the Smith transformations up to homotopy. The \(131\) unit-degree pairs contract, leaving one four-cell and \(312-131=181\) trivially attached five-cells. The resulting homotopy type is precisely \(S^4\vee\bigvee^{181}S^5\).

## Verification
Run `python3 verify_m2_k7.py` after installing the listed `sympy` dependency. The program checks all candidate subsets of \(21\) edges; all \(7{,}675\) disjoint matching pairs; the full Hasse-graph acyclicity condition; every oriented integer Morse path contribution; and the complete \(132\times312\) Smith matrix. As an independent chain calculation it computes every original simplicial boundary rank over \(\mathbb F_2\) without using the Morse matching; the resulting reduced Betti numbers are \(1\) in degree four and \(181\) in degree five. The final executable line is `M2_K7_INTEGRAL_MIXED_WEDGE_PASS`. The modular calculation is corroboration, while the integer Morse proof establishes the integral result.

## Relationship to prior work
Jonsson's bounded-degree graph-complex theory develops integral homology and connectivity questions for complete graphs, including tables of numerical invariants. Those numerical invariants are not independently claimed as new here. Vega's work on two-matching complexes studies claws, wheel graphs, and caterpillar graphs, not the integral homotopy type of this seven-vertex complete-graph case. Limonchenko and Yu's October 2026 classification concerns generalized chessboard complexes, equivalently bounded-degree **complete bipartite** graphs; its methods and homotopy classifications do not immediately apply to complete nonbipartite graphs. Singh's classification of high-degree complete-graph matching complexes concerns the degree bound \(n-2\), not the bound two here. A separate result for the triangle-free two-matching subcomplex of \(K_7\) has homotopy type \(S^4\vee\bigvee^{146}S^5\); that is a strict subcomplex and does not determine the effect of allowing triangle components. The present exact integral attaching matrix resolves that distinction.

## Limitations
This is one finite graph and one specified degree bound, not a formula for arbitrary graph size or capacities, nor an equivariant splitting. It does not claim novelty for any previously tabulated Betti numbers. The published full text of Jonsson's directly relevant bounded-degree tables was not accessible during this comparison; an implicit or unindexed homotopy classification remains possible. Finite enumeration is exhaustive **only for this seven-vertex complex**. No independent mathematical validation of the proof has been performed.

## References
1. I. Limonchenko and S. Yu, *Homotopy types and torsion in homology of generalized chessboard complexes*, arXiv:2610.37827, first posted 2026-10-27.
2. J. Vega, *2-Matching Complexes*, arXiv:1909.10406, first posted 2019-09-23.
3. J. Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928, Springer, 2008, Chapter 12 and Table 12.2, DOI: 10.1007/978-3-540-75859-4.
4. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, first posted 2020-06-24.
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
6. *First mixed-dimensional homotopy in three-clique-free triangular graphs*, 2026, finite calculation of the triangle-free restricted case.

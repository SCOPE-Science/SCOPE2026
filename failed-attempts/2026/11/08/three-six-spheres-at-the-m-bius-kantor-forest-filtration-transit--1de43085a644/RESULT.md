# Three six-spheres at the Möbius–Kantor forest-filtration transition

## Finding
Let \(G=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph. Its first positive forest-filtration complex has the **integral homotopy type**
\[
\mathcal F_1(G)\simeq \bigvee^{3} S^{6}.
\]
The inclusion of the ordinary independence complex into this stage is null-homotopic, and its homotopy cofiber is
\[
\mathcal F_1(G)/\mathcal F_0(G)\simeq
\bigl(\bigvee^{4}S^{4}\bigr)\vee S^{5}\vee\bigl(\bigvee^{3}S^{6}\bigr).
\]
The known comparison \(\mathcal F_0(G)\simeq (\bigvee^{4}S^{3})\vee S^{4}\) is reconstructed here solely to justify the cofiber; it is not asserted as new.

## Assumptions and scope
The vertex set is \(\{u_i,v_i:i\in\mathbb Z/8\mathbb Z\}\). Edges are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), with indices modulo eight. These are \(16\) vertices and \(24\) distinct undirected edges. In the bit-mask implementation, bit \(i\) denotes \(u_i\) and bit \(8+i\) denotes \(v_i\).

For \(d=0,1\), \(\mathcal F_d(G)\) comprises all vertex subsets inducing an acyclic graph of maximum degree at most \(d\). In particular \(\mathcal F_0\) is the ordinary independence complex, while \(\mathcal F_1=\operatorname{Ind}_2(G)\), because a simple graph with maximum degree at most one is a disjoint union of isolated vertices and edges. This complex is **not** the matching complex of edges of \(G\).

## Proof
**Finite face certificates.** Both an adjacency-mask degree predicate and an independent induced-edge-list degree predicate check every one of the \(2^{16}=65536\) vertex subsets. They agree on all subsets. The first-stage complex has \(6813\) faces including the empty one and the following numbers of nonempty faces in dimensions zero through seven:
\[
(16,120,512,1324,2064,1840,816,120).
\]
Its facets have dimensions six and seven (respectively \(96\) and \(120\) facets). The stage-zero complex has \(1091\) faces including the empty face.

**Acyclic integer Morse reductions.** For each complex, start with every face unmatched. At a prescribed vertex, pair every still-unmatched face missing that vertex with its still-unmatched one-vertex extension, if both faces are present; then remove those pairs from further stages. Visit vertices in ascending order \(0,1,\ldots,15\) for the first matching, and in descending order for a second matching. The attached verifier checks the entire oriented Hasse graph: unmatched covers point downward and matched covers point upward. Its topological sort exhausts all \(6813\) first-stage faces and all \(35120\) Hasse incidences for **each** ordering, proving acyclicity rather than assuming it from face counts.

Both first-stage reductions have \(3401\) matched pairs and critical cells, apart from the base point, of dimensions four, five and six in multiplicities \(1,4,6\). Using increasing vertex order for simplex orientations and increasing critical-face masks within each degree, the ascending-order *integral* Morse differentials are
\[
\partial^{\mathrm M}_5=\begin{pmatrix}-1&0&-1&-1\end{pmatrix},\quad
\partial^{\mathrm M}_6=\begin{pmatrix}
-1&0&0&0&1&-1\\
-1&0&-1&-1&1&0\\
0&1&0&0&0&1\\
1&-1&0&0&-1&0
\end{pmatrix}.
\]
The critical four-cell is mask \(818\), the critical five-cells are masks \((8916,10898,17304,17714)\), and the critical six-cells are \((15048,18344,21924,23714,43684,58008)\). The verifier computes each integer matrix entry directly by signed gradient-path elimination and independently redoes the calculation in descending vertex order. In particular, \(\partial^{\mathrm M}_5\partial^{\mathrm M}_6=0\) holds over the integers.

The incidence coefficient of the unique four-cell in the boundary of the first five-cell is \(-1\). Therefore the unique four-cell and that five-cell form a contractible subcomplex after a CW cell-basis change and may be canceled. The remaining five-cell boundary of the six-cells is the matrix formed by rows two through four of \(\partial^{\mathrm M}_6\); its first three columns form a \(3\times3\) matrix of determinant \(+1\). Three more integral cellular cancellations leave only a point and three six-cells. Since six-cells can only attach trivially to a point, this proves \(\mathcal F_1(G)\simeq\bigvee^3 S^6\) as a homotopy equivalence, not merely a rational or field-homology statement.

**Stage zero and cofiber.** The stage-zero ascending matching has \(542\) pairs and five critical three-cells and two critical four-cells, with the only potentially nonzero boundary
\[
\partial^{\mathrm M}_4=\begin{pmatrix}
0&0\\0&0\\1&1\\-1&-1\\0&0
\end{pmatrix}.
\]
Its primitive rank-one differential allows one three–four cellular cancellation, leaving four three-cells and one four-cell attached to a point. The residual four-cell attaches trivially to a wedge of three-spheres because the integral cellular boundary is zero and \(\pi_3(\bigvee^4 S^3)\cong\mathbb Z^4\). Hence \(\mathcal F_0(G)\simeq\bigvee^4S^3\vee S^4\), agreeing with the known stage-zero literature. A map from this wedge to the five-connected space \(\bigvee^3 S^6\) is null-homotopic. As the simplicial inclusion is a cofibration, its cofiber is homotopy equivalent to \(\mathcal F_1(G)\vee\Sigma\mathcal F_0(G)\), giving the formula above.

## Verification
Run `python3 verify.py` with standard Python 3. The script separately enumerates two membership predicates at both levels, reconstructs two full discrete-Morse matchings and checks acyclicity on their *entire* directed Hasse graphs, computes the displayed signed integral matrices, tests unit minors and boundary composition, and independently computes all original simplicial boundary ranks over \(\mathbb F_2\). Its fixed completion marker is `MOBIUS_KANTOR_FIRST_FOREST_THREE_SIX_SPHERES_VERIFIED`; the exact JSON output is embedded in `verification_output.json`. Thus the computations are finite exact proofs, not Monte Carlo tests or deductions from finite sampling. The verifier is an ordinary standalone checker and is not an independent external audit.

## Relationship to prior work
The first forest filtration is defined by Carnero Bravo [1], who explains its identification with the two-independence complex at this level. Deshpande–Singh [2] develop higher-independence homotopy theory; their concrete classifications apply to complete multipartite, fully whiskered, path, cycle and perfect-ary-tree families, none being the cubic sixteen-vertex graph here. Carnero Bravo's specific calculations concern paths, cycles, double stars, cacti, joins and selected graph products; neither an applicable formula nor this precise graph appears in the inspected results. The pre-existing integral calculation of the *ordinary* Möbius–Kantor independence complex [3] supplies the stage-zero comparison but does not determine the first positive stage or its inclusion/cofiber. Results about the graph's matching complex, total cut complex, metric nerve and graph-theoretic Lefschetz numbers concern different constructions and do not imply the new claim.

## Limitations
This theorem concerns one specified graph and the first positive stage; it is not a uniform theorem for arbitrary generalized Petersen graphs, nor does it determine equivariant homotopy types or higher filtration maps. A possible unindexed equivalent calculation remains a bibliographic risk. Knill's recent same-graph article [4] was identified and its abstract read, but its large author-hosted full text was not accessible during this comparison; its abstract addresses graph groups, geometry and Lefschetz theory rather than induced-degree forest complexes. No independence or outside certification is claimed.

## References
1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, initially made public 2023-07-25; inspected version 3, including the definition, introduction and families/products results.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, initially made public 2020-01-15; inspected version 2, introduction, acyclic-matching results, and theorems on the studied graph families.
3. *Integral homotopy type of the Möbius–Kantor independence complex*, openly available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-m-bius-kantor-independence-complex--b0d62cfde5f3; its RESULT.md was inspected in full for the explicit stage-zero claim.
4. O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799, first publicly submitted 2026-05-29; abstract and author-hosted full-text availability checked.

# The graph-metric Rips filtration of the Desargues graph
## Finding
Let \(D=G(10,3)\) be the Desargues graph with its shortest-path metric, and use the inclusive Vietoris--Rips convention. For every real \(r\ge 0\),
\[
\operatorname{VR}_{\le r}(D)\simeq
\begin{cases}
\text{a discrete 20-point space}, & 0\le r<1,\\
\bigvee^{11}S^1, & 1\le r<2,\\
\bigvee^{19}S^2, & 2\le r<3,\\
S^3, & 3\le r<4,\\
S^9, & 4\le r<5,\\
\ast, & r\ge 5.
\end{cases}
\]
Thus the complete filtration has three consecutive nontrivial sphere dimensions \(1,2,3\), followed by a jump to dimension \(9\) immediately before contractibility.

## Assumptions and scope
Write the vertices as \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). The metric is graph distance. A finite subset is a simplex of \(\operatorname{VR}_{\le r}(D)\) exactly when every pair of its vertices has distance at most \(r\). Since all distances are integral and the diameter is \(5\), the filtration changes only at the integer scales \(1,2,3,4,5\).

## Proof
For \(0\le r<1\), no two distinct vertices can lie in one simplex, so the complex is a discrete set of \(20\) points.

For \(1\le r<2\), the complex is the clique complex of \(D\). The Desargues graph has girth \(6\), hence it is triangle-free, so this clique complex is just the connected graph \(D\). With \(20\) vertices and \(30\) edges, its cycle rank is \(30-20+1=11\). Therefore it is homotopy equivalent to \(\bigvee^{11}S^1\).

At scale \(2\), exhaustive clique enumeration in the distance-two graph gives face vector
\[
(20,90,120,30).
\]
Apply the deterministic staged vertex-toggle matching in the order
\[
u_0,u_1,v_0,v_3,u_2,v_1,v_4,u_3,v_2,v_5,u_4,v_6,u_5,v_7,u_6,v_8,u_7,v_9,u_8,u_9.
\]
At each stage, pair each still-unmatched simplex \(\sigma\) not containing the current vertex with \(\sigma\cup\{x\}\) whenever the latter is also a simplex and is still unmatched. The resulting matching has \(120\) pairs and exactly \(20\) critical cells: one critical \(0\)-cell and nineteen critical \(2\)-cells. A complete topological sort of the Morse-oriented Hasse diagram checks acyclicity. Forman's theorem therefore gives a CW model with one \(0\)-cell and nineteen \(2\)-cells and no other cells, hence
\[
\operatorname{VR}_{\le2}(D)\simeq\bigvee^{19}S^2.
\]

At scale \(3\), exhaustive clique enumeration gives face vector
\[
(20,150,540,1000,960,450,80).
\]
The same staged toggle order gives \(1599\) matched pairs and exactly two critical cells: one critical \(0\)-cell and one critical \(3\)-cell. The complete Morse-oriented Hasse graph is again acyclic. Hence
\[
\operatorname{VR}_{\le3}(D)\simeq S^3.
\]

At scale \(4\), every vertex has a unique vertex at distance \(5\): the antipodal pairs are \(\{u_i,u_{i+5}\}\) and \(\{v_i,v_{i+5}\}\) for \(i\in\mathbb Z/5\mathbb Z\). Thus the only forbidden pairs at scale \(4\) are ten disjoint antipodal pairs. The Rips complex is consequently the join of ten copies of \(S^0\), equivalently the boundary of the \(10\)-dimensional cross-polytope, so
\[
\operatorname{VR}_{\le4}(D)\cong S^9.
\]
Finally the diameter is \(5\), so for \(r\ge5\) every pair of vertices is allowed and the Rips complex is the full \(19\)-simplex, hence contractible.

## Verification
Run `python3 verify_desargues_rips.py`. The verifier reconstructs \(D\) from the defining edge formulas, computes all-pairs shortest-path distances, confirms \(20\) vertices, \(30\) edges, cubic degree sequence, and diameter \(5\), and checks triangle-freeness at scale \(1\). It then enumerates every simplex at scales \(2\) and \(3\), reproduces the stated face vectors, replays every matching pair, constructs every nonempty Hasse cover, and verifies acyclicity by a full topological sort. At scale \(4\) it verifies that the distance-\(5\) relation is exactly a perfect matching of ten antipodal pairs. The terminal line is `DESARGUES_RIPS_VERIFY_OK`.

The scale-\(2\) Hasse diagram has \(660\) nonempty covers; the scale-\(3\) Hasse diagram has \(13980\). The verifier checks every one of them. No sampling or numerical approximation is used.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine complete Vietoris--Rips homotopy types for the five Platonic solids and explicitly motivate extending such computations to other highly structured finite metric spaces. Their paper is primarily classified in MSC \(55N31\). The Desargues graph is not among the Platonic graphs treated there.

Adamaszek identifies \(\operatorname{Cl}(G^r)\) with the graph-metric Vietoris--Rips complex and proves general collapse criteria for powers of graphs. His girth criterion requires girth at least \(3r+1\); for \(r=2\) this means girth at least \(7\), while the Desargues graph has girth \(6\). Thus that theorem does not imply the scale-\(2\) result here. His paper treats cycles and general structural criteria, not the Desargues graph. Targeted exact searches for the Desargues graph together with Vietoris--Rips, Rips complex, clique complex of graph powers, and \(G(10,3)\) found no source stating or implying the complete filtration above.

## Limitations
The theorem concerns the shortest-path metric on one finite graph. It does not classify generalized Petersen graphs as a family, does not address Euclidean realizations, and does not determine the homotopy classes of the inclusion maps between successive nontrivial scales. The originality assessment is limited by indexing and terminology, so an unindexed equivalent computation remains a residual risk.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, “Vietoris--Rips complexes of Platonic solids,” arXiv:2302.14388, first public version 2023-02-28.
2. M. Adamaszek, “Clique complexes and graph powers,” arXiv:1104.0433, first public version 2011-04-03.

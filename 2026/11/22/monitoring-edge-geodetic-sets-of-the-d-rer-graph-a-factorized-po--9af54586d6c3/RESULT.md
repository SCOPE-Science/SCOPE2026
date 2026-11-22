# Monitoring-edge-geodetic sets of the Dürer graph: a factorized polynomial and a Cartesian product of claws

## Finding

Let \(D=GP(6,2)\), the twelve-vertex Dürer graph. Its outer vertices are \(o_i\), its inner vertices are \(u_i\), with indices in \(\mathbb Z/6\mathbb Z\). Edges are \(o_io_{i+1}\), \(o_iu_i\), and \(u_iu_{i+2}\) (with each undirected edge counted once). For \(S\subseteq V(D)\), call \(S\) a *monitoring edge-geodetic set* (MEG-set) if for each edge \(e\) there are \(x,y\in S\) such that deleting \(e\) strictly increases the shortest-path distance between \(x\) and \(y\).

**Theorem.** A set \(S\) is an MEG-set of \(D\) if and only if both of these conditions hold:

1. Each spoke is covered: \(\{o_i,u_i\}\cap S\ne\varnothing\) for every \(i\in\mathbb Z/6\mathbb Z\).
2. Each inner triangle contains at least two selected vertices: \(|S\cap\{u_0,u_2,u_4\}|\ge2\) and \(|S\cap\{u_1,u_3,u_5\}|\ge2\).

The complete cardinality polynomial, whose coefficient of \(z^k\) counts labelled \(k\)-vertex MEG-sets, is

\[
P_D(z)=\sum_{S\text{ MEG-set}}z^{|S|}=z^6(1+z)^4(z+4)^2
=16z^6+72z^7+129z^8+116z^9+54z^{10}+12z^{11}+z^{12}.
\]

Thus there are precisely \(400\) MEG-sets. The minimum size is \(6\), and the \(16\) minimum sets are *all* inclusion-minimal MEG-sets. A minimum set contains exactly one vertex from every spoke, and the indices whose outer vertex is selected contain at most one even and at most one odd index.

If the vertices of the reconfiguration graph are the minimum MEG-sets and a move replaces one selected vertex with one unselected vertex, then both unrestricted token jumping and token sliding along a graph edge yield exactly

\[
\mathcal R(D)\cong K_{1,3}\square K_{1,3}.
\]

Consequently this graph has \(16\) states, \(24\) edges, diameter \(4\), and degree distribution \(9\) states of degree \(2\), \(6\) of degree \(4\), and one of degree \(6\).

## Assumptions and scope

The graph is finite, unweighted, undirected and simple. An edge belongs to *all* shortest paths for a pair if and only if its deletion increases their distance; the latter condition fixes the monitoring convention. Every cardinality refers to the explicitly labelled twelve-vertex graph, not all generalized Petersen graphs or all planar graphs. An exchange is valid only if its endpoint is another minimum MEG-set; a slide additionally requires the exchanged vertices to be adjacent in \(D\).

## Proof

For an edge \(e\) let \(W_e\) denote the unordered vertex pairs \(\{x,y\}\) whose distance increases upon deletion of \(e\). The cyclic rotation \(o_i\mapsto o_{i+1}\), \(u_i\mapsto u_{i+1}\) is an automorphism, so there are three edge types. Direct distance comparison gives the following **complete witness-pair table** for one edge of each type (other tables are its cyclic rotations):

- Outer edge \(e=o_0o_1\): \(W_e=\{\{o_0,o_1\},\{o_0,o_2\},\{o_0,u_1\},\{o_1,o_5\},\{o_1,u_0\},\{u_0,u_1\}\}\).
- Spoke \(e=o_0u_0\): \(W_e=\{\{o_0,u_0\},\{o_0,u_2\},\{o_0,u_4\},\{o_1,u_0\},\{o_5,u_0\},\{u_0,u_1\},\{u_0,u_5\}\}\).
- Inner edge \(e=u_0u_2\): \(W_e=\{\{o_0,u_2\},\{o_2,u_0\},\{u_0,u_2\}\}\).

This finite table can be reconstructed without a shortest-path choice: for each of its three edges, breadth-first search on the displayed adjacency graph and again after deleting the edge determines all \(\binom{12}{2}=66\) pairwise distances. The included checker recomputes the table from adjacency alone. Necessity now follows: every witness pair for a spoke contains one of that spoke's endpoints, while every witness pair for an inner edge contains an endpoint of that inner edge. Hence an MEG-set covers all spokes and meets all three edges of each inner triangle, requiring at least two vertices in each triangle.

Conversely, suppose these two conditions hold. Consider any outer edge \(o_io_{i+1}\). Choose from each of its two spokes a selected endpoint. The four possibilities are \(\{o_i,o_{i+1}\}\), \(\{o_i,u_{i+1}\}\), \(\{u_i,o_{i+1}\}\), and \(\{u_i,u_{i+1}\}\); the rotated outer-edge witness table includes all four. Thus every outer edge is monitored. For an inner edge \(u_iu_{i+2}\), at least one endpoint is selected. If both are selected they monitor it directly; if only \(u_i\) is selected, then \(o_{i+2}\) must be selected by the spoke condition, and \(\{u_i,o_{i+2}\}\) monitors it. The opposite case is symmetric. Finally, consider a spoke \(o_iu_i\). If both endpoints are selected they monitor it. If only \(o_i\) is selected, the triangle condition selects at least one of \(u_{i+2}\), \(u_{i+4}\), and the corresponding pair with \(o_i\) monitors it. If only \(u_i\) is selected, either \(o_{i+1}\) is selected and pairs with \(u_i\), or it is not, in which case the spoke condition selects \(u_{i+1}\), which pairs with \(u_i\). Every pair just cited appears in the rotated witness table. This proves the equivalence.

For counting, independently consider either inner triangle. Each of its three spokes either selects the inner vertex alone (weight \(z\)), the outer vertex alone (weight \(z\)), or both (weight \(z^2\)); at most one of the three inner vertices may be absent. The contribution is therefore

\[
[z(1+z)]^3+3z[z(1+z)]^2=z^3(1+z)^2(z+4).
\]

The two triangles use disjoint vertex sets, so their weights multiply, giving \(P_D(z)\). Every MEG-set contains a minimum one: in each spoke choose the inner vertex if present, otherwise the outer vertex. This produces six vertices while retaining both triangle-coverage constraints. Therefore all inclusion-minimal sets have size six, and exactly one vertex is chosen per spoke. Of the three even spokes one may contribute its outer vertex, or none; independently the same holds for odd spokes. There are \(4\times4=16\) minimum sets.

Index a minimum set by \((a,b)\), where \(a\in\{\bot,0,2,4\}\) identifies its selected outer even index (or \(\bot\) for none) and \(b\in\{\bot,1,3,5\}\) does the same for odd indices. A single-vertex exchange preserving exactly one choice per spoke must switch \(o_i\leftrightarrow u_i\) at a single index. This is legal precisely when one coordinate changes between \(\bot\) and one of its three possible indices; switching between two nonempty indices requires two such exchanges. The exchange graph is exactly the Cartesian product of two three-leaf stars. Each legal switch is along the corresponding spoke edge, so allowing only token slides does not remove any move. This finishes the proof.

## Verification

Run `python3 verify.py` with Python 3 and its standard library only. It constructs \(D\) from its eighteen edges, independently computes each monitoring pair by breadth-first search before and after each edge deletion, compares the asserted three representative witness tables, and tests all \(2^{12}=4096\) vertex subsets against the structural criterion. It then verifies every coefficient of \(P_D(z)\), the exact inclusion-minimal family, and all optimal single-token jumps and slides. Its completed result is `VERIFY_OK` with 16 minima, 24 jump/slide edges, and degree histogram \((2:9,4:6,6:1)\). The analytic proof above establishes the claim; the program provides a separate exhaustive finite replay.

## Relationship to prior work

The MEG-set predicate and its network-failure motivation come from Dev, Dey, Foucaud, Krishna and Ramasubramony Sulochana (arXiv:2210.03774, first posted October 7, 2022). Haslegrave (arXiv:2210.08955, first posted October 17, 2022) proves product bounds and a vertex-cover necessity result for graphs of diameter two. Foucaud and collaborators (arXiv:2403.09122, first posted March 14, 2024) give general extremal, girth and clique-sum results, including a vertex-cover sufficient condition under girth at least five. Those special-case hypotheses do not apply directly to the Dürer graph, which has girth three and diameter four. The present result is a set-level classification, complete enumerator and exact optimal-solution mobility theorem for this particular polyhedral graph; it is not a generic vertex-cover corollary.

## Limitations

Only the Dürer graph \(GP(6,2)\) is covered. The theorem makes no assertion for other generalized Petersen graphs, weighted monitoring, multiple edge failures, or nonminimum reconfiguration. Publication priority remains subject to additional literature inspection, especially a later study of monitoring numbers on planar networks whose complete text was not accessible. The supplied computational check is finite and does not replace external mathematical review.

## References

1. S. R. Dev, S. Dey, F. Foucaud, N. Krishna, and L. R. Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774, https://arxiv.org/abs/2210.03774 (first submitted 2022-10-07).
2. J. Haslegrave, *Monitoring edge-geodetic sets: hardness and graph products*, arXiv:2210.08955, https://arxiv.org/abs/2210.08955 (first submitted 2022-10-17).
3. F. Foucaud, C. Marcille, Z. M. Myint, R. B. Sandeep, S. Sen and S. Taruni, *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, arXiv:2403.09122, https://arxiv.org/abs/2403.09122 (first submitted 2024-03-14).
4. E. W. Weisstein, *Dürer Graph*, MathWorld, https://mathworld.wolfram.com/DuererGraph.html (graph nomenclature and identification with \(GP(6,2)\)).
5. Y. Lei, G. Liu, C. Yang and W. Zhao, *The Monitoring-Edge-Geodetic Number of Some Planar Networks*, DOI:10.1142/S0219265925500124 (abstract consulted; full text unavailable for comparison).

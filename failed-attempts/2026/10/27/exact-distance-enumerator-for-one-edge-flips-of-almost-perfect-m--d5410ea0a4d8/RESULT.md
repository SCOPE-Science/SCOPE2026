# Exact distance enumerator for one-edge flips of almost-perfect matchings in odd complete graphs

## Finding
For every integer \(m\geq1\), let \(\mathcal F_m\) have as vertices the matchings of cardinality \(m\) in the complete graph \(K_{2m+1}\). A *flip* deletes exactly one matching edge and replaces it by another edge while keeping cardinality \(m\) and the matching property. For any two vertices \(M,N\), their symmetric difference is a disjoint union of even alternating cycles and at most one alternating path; denote the number of alternating cycles by \(c(M,N)\). The exact shortest-flip distance is
\[
d_{\mathcal F_m}(M,N)=|M\setminus N|+c(M,N).
\]
In particular, the graph is connected, vertex-transitive and regular of degree \(2m\). The *entire distance distribution* from every fixed matching is the polynomial
\[
\boxed{F_m(z)=\sum_{N}z^{d_{\mathcal F_m}(M,N)}=m!\,[u^m]\,\frac{e^u}{1-2uz}\exp\!\left(\sum_{j\ge2}\frac{2^{j-1}}{j}u^jz^{j+1}\right).}
\]
Equivalently, as a formal power series in \(u\),
\[
F_m(z)=m!\,[u^m]e^{u(1-z^2)}(1-2uz)^{-1-z/2}.
\]
Its degree, the radius and diameter of \(\mathcal F_m\), is exactly \(m+\lfloor m/2\rfloor\). The number of farthest matchings from any vertex is \((2r)!/r!\) when \(m=2r\), and is \(2(2r+1)!/r!+4(2r+1)!/(3(r-1)!)\) when \(m=2r+1\ge3\); for \(m=1\) it is \(2\). These coefficients count all antipodes, not merely a construction of one.

## Assumptions and scope
All vertices of the underlying complete graph are distinguished (labeled); matchings are unordered sets of unordered edges. The parameter \(m\) is an arbitrary positive integer. No requirement of planarity, edge disjointness between successive matchings, or preservation of the identity of the exposed vertex is imposed. Each state has exactly one exposed vertex. The flip must preserve the size and matching property at every intermediate state, and the intermediate state need not have any edges in common with the destination. The distance is ordinary shortest-path distance in this finite flip graph.

## Proof
**1. Exact distance.** Fix matchings \(M,N\). Every component of \(M\mathbin\triangle N\) is an alternating cycle or the one alternating path joining their exposed vertices. Every edge of \(N\setminus M\) must be inserted by some flip, requiring at least \(|M\setminus N|\) steps. Moreover, let \(C\) be an original alternating cycle. Before any edge of the original matching \(M\cap C\) is removed, all vertices of \(C\) remain matched within \(C\), so the exposed vertex lies outside \(C\). The first flip that removes an edge of \(M\cap C\) therefore inserts an edge joining that exposed vertex to a vertex of \(C\). Such an edge cannot belong to \(N\), whose edges incident to \(C\) stay inside \(C\). Thus at least one flip per original alternating cycle adds a non-target edge. Distinct cycles have distinct first removals; such flips cannot count among the at-least-\(|N\setminus M|\) target insertions. Therefore every reconfiguration has length at least \(|M\setminus N|+c(M,N)\).

For the matching upper bound, start with the alternating path, if present. Starting from the exposed vertex of \(M\), sequentially replace each encountered \(M\)-edge by the preceding \(N\)-edge, moving the exposed vertex along the path. Exactly one flip per \(M\)-edge on the path realizes all target path edges and exposes the target's unmatched vertex. Now fix an alternating cycle with \(k\ge2\) matching edges, ordered as \((a_1,b_1),\ldots,(a_k,b_k)\) in \(M\) and \((b_1,a_2),\ldots,(b_{k-1},a_k),(b_k,a_1)\) in \(N\). If \(h\) is currently exposed, first replace \((a_1,b_1)\) by \((h,a_1)\); next replace \((a_2,b_2)\) by \((b_1,a_2)\), and similarly for the remaining pairs; finally replace \((h,a_1)\) by \((b_k,a_1)\). This performs \(k+1\) legal flips, installs all \(k\) target edges on the cycle and again exposes \(h\). All needed edges exist in the complete graph. Process each cycle in this manner. The total is precisely \(|M\setminus N|+c(M,N)\).

**2. Enumerating distances.** Regard the \(m\) pairwise disjoint edges of the fixed matching \(M\) as distinguishable two-vertex *blocks*, together with its single exposed vertex. In \(M\mathbin\triangle N\), any block either remains unchanged, belongs to the unique alternating path, or belongs to an alternating cycle of length \(2j\) for \(j\ge2\). On a selected labeled set of \(k\) blocks, a path starting at the fixed exposed vertex is determined by ordering its \(k\) blocks and choosing which endpoint of each block is encountered first; it admits \(2^k k!\) realizations and contributes distance \(k\). For each chosen labeled set of \(j\ge2\) blocks, one alternating cycle has \(2^{j-1}(j-1)!\) realizations (cyclic ordering and pair orientations, modulo reversal), contributing distance \(j+1\). Unused blocks remain unchanged, contributing one realization and zero distance. The labeled exponential formula consequently gives
\[
\sum_{m\ge0}F_m(z)\frac{u^m}{m!}=\left(\sum_{k\ge0}2^ku^kz^k\right)e^u\exp\!\left(\sum_{j\ge2}\frac{2^{j-1}(j-1)!}{j!}u^jz^{j+1}\right),
\]
which is the stated polynomial identity. The formal logarithmic identity \(\sum_{j\ge2}(2uz)^j/j=-\log(1-2uz)-2uz\) gives the second closed form. This counts every destination once because alternating components are uniquely determined by \(M,N\).

**3. Diameter and farthest states.** If \(p\) fixed matching blocks lie on the alternating path and there are \(c\) alternating cycles occupying \(t\) other blocks, then \(t\ge2c\), so the distance is \(p+t+c\le m+\lfloor m/2\rfloor\). Equality is achievable: for even \(m=2r\), put all blocks into \(r\) cycles of two blocks; for odd \(m=2r+1\), put one block on the path and the others in \(r\) two-block cycles. Every configuration at maximum distance uses all blocks, has \(c=\lfloor m/2\rfloor\), and is of one of the following types. For even \(m\), it consists only of two-block cycles, counted by \(m!/r!\). For odd \(m\ge3\), either there is a one-block path and \(r\) two-block cycles, counted by \(2m!/r!\), or no path, one three-block cycle, and \(r-1\) two-block cycles, counted by \(4m!/(3(r-1)!)\). For \(m=1\) the two one-block-path states are farthest. Vertex-transitivity gives the same eccentricity and distance polynomial for every initial matching.

## Verification
The standalone script `check_bfs.py` constructs every almost-perfect matching of \(K_{2m+1}\) for \(1\le m\le5\), builds adjacency using only legal one-edge replacements, and computes distances by breadth-first search. The independent script `check_cycles.py` directly enumerates symmetric-difference components without constructing any flip graph, and separately evaluates a formal recurrence for the polynomial. Replaying both gives distance layers (in ascending distance) for \(m=1,2,3,4,5\) respectively:
\[
(1,2),\ (1,4,8,2),\ (1,6,24,54,20),\ (1,8,48,204,464,208,12),\ (1,10,80,500,2120,4880,2524,280).
\]
All assertions pass. These computations confirm small instances; the infinite result is established by the combinatorial proof, not finite extrapolation.

## Relationship to prior work
Earlier complete-graph matching flip geometry and geodesics were studied by Jennings (2013 preprint; 2017 publication), using unrestricted two-edge alternating-four-cycle flips among perfect matchings of even-order complete graphs; their metric differs from the one-exposed-vertex restriction here. Sliding-token and matching reconfiguration frameworks also predate this result (Demaine et al., 2014; Bousquet et al., 2018). Aichholzer et al. (2025) analyze the same *flip* rule for odd matchings of general graphs and provide a lower-bound perspective based on alternating cycles and a linear upper bound when the flip graph is connected. The exact complete-graph distance formula is compatible with those bounds and is not claimed as a new model of reconfiguration. Brenner et al. (2026) study the same underlying flip graph for Hamilton paths and cycles, proving Hamilton-connectedness; that is a stronger Hamiltonicity property than mere connectivity but does not by itself determine shortest-path distance multiplicities. The contribution established here is the full distance enumerator, including all distance layers, exact radius/diameter and antipodal counts, for every odd complete graph. Relevant full texts and limitations of comparisons are summarized in `REVIEW.md` and `AUDIT.json`.

## Limitations
The theorem is for complete graphs of odd order under single-edge flips. No analogous distribution is claimed for general graphs, geometric noncrossing matchings, or directed matchings. This is not an independent publication-priority or peer-review certification. The complete 44-page open-access preprint of Brenner et al. (2026) was available and its statement, detailed introduction, combinatorial 1-flip results, and references were inspected. Its Hamilton-connectedness and directed-graph bounds do not state the present all-pairs shortest-distance enumerator. Differently indexed equivalent results remain a publication-priority risk. The simple alternating-cycle lower bound resembles observations already present in the 2025 literature; the novelty assessment concerns the exact distance polynomial and its structural consequences, not that lower bound by itself.

## References
1. R. H. Jennings, *Geodesics in a Graph of Perfect Matchings*, arXiv:1306.3611 (first submitted 2013-06-15); published in Séminaire Lotharingien de Combinatoire 74 (2017), Article B74e, https://www.mat.univie.ac.at/~slc/wpapers/s74jenn.pdf.
2. E. D. Demaine et al., *Linear-Time Algorithm for Sliding Tokens on Trees*, arXiv:1406.6576 (first submitted 2014-06-25), https://arxiv.org/abs/1406.6576.
3. N. Bousquet, T. Hatanaka, T. Ito, M. Mühlenthaler, *Shortest Reconfiguration of Matchings*, arXiv:1812.05419 (2018), https://arxiv.org/abs/1812.05419.
4. S. M. Cioabă, G. Royle, Z. K. Tan, *On the flip graphs on perfect matchings of complete graphs and signed reversal graphs*, Australas. J. Combin. 81 (2021), 480–497, https://ajc.maths.uq.edu.au/pdf/81/ajc_v81_p480.pdf. This studies unrestricted two-edge flips of perfect matchings, not the exposed-vertex single-edge move.
5. O. Aichholzer et al., *Flipping odd matchings in geometric and combinatorial settings*, arXiv:2508.18457 (2025), https://arxiv.org/abs/2508.18457.
6. S. Brenner et al., *Hamilton paths and cycles in flip graphs of (almost-)perfect matchings*, arXiv:2607.04687 (2026), https://arxiv.org/abs/2607.04687.

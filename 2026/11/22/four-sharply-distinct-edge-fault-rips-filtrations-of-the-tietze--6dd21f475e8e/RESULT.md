# Four sharply distinct edge-fault Rips filtrations of the Tietze graph

## Finding
Let \(T\) be the twelve-vertex Tietze cubic graph, obtained by replacing one vertex of the Petersen graph with a triangle, retaining the original three incident edges as distinct triangle attachments. For an edge \(e\) of \(T\), let \(T-e\) carry its **recomputed** unweighted shortest-path metric. Consider the inclusive vertex-metric Vietoris–Rips complexes \(\operatorname{VR}_{\le r}(T-e)\) for every real \(r\ge0\).

The unique triangle provides a natural invariant: let \(\delta(v)\) be the shortest distance of vertex \(v\) to that triangle, and let the edge type of \(e=uv\) be the unordered pair \(\{\delta(u),\delta(v)\}\). All eighteen edges form **exactly four automorphism orbits** by this type. Their entire integral homotopy filtrations are as follows. All four start at twelve isolated points, so \(\operatorname{VR}_{\le0}(T-e)\simeq\bigvee^{11}S^0\).

| Edge type \(\{\delta(u),\delta(v)\}\) | Number of edges | \(1\le r<2\) | \(2\le r<3\) | \(r\ge3\) |
|---|---:|---|---|---|
| \(\{0,0\}\) (triangle edge) | 3 | \(\bigvee^6 S^1\) | \(\bigvee^2 S^2\) | point |
| \(\{0,1\}\) (triangle attachment) | 3 | \(\bigvee^5 S^1\) | \(S^2\) | point |
| \(\{1,2\}\) (outer attachment-side edge) | 6 | \(\bigvee^5 S^1\) | \(\bigvee^4 S^2\) | point |
| \(\{2,2\}\) (edges remote from triangle) | 6 | \(\bigvee^5 S^1\) | \(\bigvee^4 S^2\) | point |

Thus an edge incident with the distinguished triangle destroys two or three of the four scale-two integral sphere classes of the intact graph, depending on its type, while the other twelve edge faults preserve their rank. Exactly the triangle-edge faults preserve the rank-six scale-one cycle group; all other faults reduce it to rank five. There is no torsion in any degree, and every positive-degree integral persistence class lasts exactly one threshold interval. The degree-zero persistent homology has eleven finite intervals \([0,1)\) and one infinite interval, for each connected edge-deleted graph.

## Assumptions and scope
The underlying metric is the shortest-path distance between **vertices** in each edge-deleted graph. It is not the metric on arbitrary points of a geometric realization, and the deleted edge is not merely omitted from the Rips complex while retaining the original metric. For a reproducible graph, let the Petersen graph have outer five-cycle \(0,1,2,3,4,0\), spokes \(i\)--\(i+5\), inner pentagram \(5,7,9,6,8,5\), and replace vertex \(0\) by a triangle. After relabeling original vertices \(1,\ldots,9\) to \(0,\ldots,8\), the new triangle vertices are \(9,10,11\) and have attachments \(\{0,9\},\{3,10\},\{4,11\}\). `FAULT_CERTIFICATE.json` gives the exact eighteen-edge list and four representative deleted edges \(\{9,10\},\{0,9\},\{0,1\},\{1,2\}\). The statement is restricted to **single** edge deletions from this fixed graph.

## Proof
**Orbit exhaustiveness.** The original graph has one triangle. Every automorphism preserves its vertex set, and consequently preserves the unordered endpoint-distance pair \(\{\delta(u),\delta(v)\}\). These pairs partition its eighteen edges into classes of sizes three, three, six and six, respectively. `FAULT_CERTIFICATE.json` also gives twelve explicit vertex permutations; `FAULT_VERIFY.py` checks each permutation preserves every graph edge, and that their images of each representative edge are exactly all edges in its distance class. Hence these four types are precisely the full automorphism orbits, whether or not the twelve listed automorphisms exhaust the entire group.

**Scales zero and one.** All **twelve** vertices are present after each edge deletion. Each fault leaves a connected graph on twelve vertices with seventeen edges. If a nontriangle edge is removed, the unique original triangle persists, and its one free-edge/filled-face collapse leaves a graph of cycle rank \(16-12+1=5\). If an edge of the triangle is removed, no triangle remains and the graph itself has cycle rank \(17-12+1=6\). This gives the exact integral wedge-of-circles results.

**Scale two: four finite, integral, nonabelian certificates.** The enumerated scale-two face vectors, with entries by simplex dimension starting at zero, are:
\[
\begin{array}{c|c}
\{0,0\}&(12,49,88,83,51,19,3)\\
\{0,1\}&(12,46,82,81,51,19,3)\\
\{1,2\}&(12,46,72,49,20,4)\\
\{2,2\}&(12,46,69,37,7).
\end{array}
\]
For the four representative faults in this order, the certificate specifies respectively \(129,134,74,58\) sequential elementary simplicial free-face collapses. The surviving simplicial complexes are two-dimensional, with \((V,E,F)=(9,22,16),(6,12,8),(9,25,21),(9,25,21)\). In each case the certificate supplies an exact spanning tree of \(V-1\) edges and an ordered list of \(E-V+1\) triangular two-cell relators. Each relator contains *precisely one* still-uneliminated non-tree edge; hence the corresponding generator of the fundamental group is killed, **even nonabelianly**, and in the integral cellular boundary matrix the relators provide a full-rank unit-triangular unimodular minor. Thus each residual complex is simply connected, its integral first homology is zero, its second homology is free with rank \(F-E+V-1\), namely \(2,1,4,4\), and there is no higher homology. A simply connected two-dimensional CW complex with free second homology is a wedge of that many two-spheres, by Hurewicz and the homological Whitehead theorem.

**Scale three and later.** The edge-deleted graphs have diameters \(3,5,4,4\), again in the displayed type order. At radius three, the triangle-edge fault has diameter three, so its complex is already a full simplex. For the attachment, attachment-side and remote edge classes, the certificate gives, respectively, \(767,1279,1535\) elementary collapses to a vertex. For the triangle-attachment class, an additional explicit radius-four collapse proves the same; the remaining later radii are full simplices. All these collapses are checked against reconstructed faces. Nontrivial reduced homology occurs in distinct degrees at successive scales and dies before scale three, giving the stated exact persistent intervals over the integers without extension problems.

## Verification
Run `python3 FAULT_VERIFY.py` with the included `FAULT_CERTIFICATE.json` in the same directory; `FAULT_CHECKS.txt` records a successful exact replay. The Python 3 standard-library-only verifier reconstructs the graph from the Petersen-to-triangle substitution, validates the edge-orbit invariants and twelve explicit automorphisms, enumerates all clique faces at each required radius from recomputed graph distances, checks *every* listed elementary free-face collapse, all spanning-tree and ordered nonabelian group-generator eliminations, and all higher-radius contractible collapses. It also recomputes characteristic-two Betti numbers from the original chain groups, strictly as an independent corroborating check. The integral and homotopy conclusions rest on the group presentation and unimodular minor arguments, not on mod-two ranks alone.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* [1] supplies the general graph-power/Rips identification and a high-girth stability theorem; the latter requires girth at least seven at radius two and is not applicable to these low-girth edge-fault cases. Adamaszek et al.'s *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings* [2] gives gluing criteria, but does not supply this four-orbit edge-deletion classification. The general decomposition work of Chachólski et al. [3] likewise does not determine these finite outcomes. Prior results for the **intact** Tietze graph, including its radius-two four-sphere wedge, do not fix the new metrics or the three sharply distinct edge-fault responses. Other tabulations of named cubic-graph Rips complexes concern nonisomorphic graphs, and published Tietze independence, matching, and higher-independence calculations concern different simplicial complexes. None of those statements implies the new four-orbit classification.

## Limitations
This is an exact finite theorem about a specific canonical graph and its eighteen single-edge faults, not a theorem about all cubic graphs or multi-edge faults. The comparison reports homotopy groups and persistence interval multiplicities, not a canonical map between different Rips filtrations (their metrics change). No equivariant homology character or continuous metric-graph homotopy classification is asserted. Exhaustive prior-literature uniqueness has not been proved: unindexed equivalent tables or stronger encompassing results remain possible. No independent external mathematical audit has been performed.

## References
[1] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public 2011-04-03), https://arxiv.org/abs/1104.0433.

[2] M. Adamaszek, H. Adams, E. Gasparovic, M. Gommel, E. Purvine, R. Sazdanovic, B. Wang, Y. Wang and L. Ziegelmeier, *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224 (first public 2017-12-18), https://arxiv.org/abs/1712.06224.

[3] W. Chachólski, A. Jin, M. Scolamiero and F. Tombari, *Homotopical decompositions of simplicial and Vietoris Rips complexes*, Journal of Applied and Computational Topology (2021), https://doi.org/10.1007/s41468-021-00066-2.

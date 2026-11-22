# Sharp fourth-homology onset in scale-three rook-graph Čech nerves

## Finding
For \(q\ge3\), let \(G_q=K_3\square K_q\) be the rectangular rook graph, with vertices \((i,j)\) where \(0\le i<3\) and \(0\le j<q\). Its **intrinsic graph Čech complex** \(X_q=\mathcal N(G_q,3)\) is the nerve of closed metric balls of radius \(3/2\) in the unit-edge geometric realization of the graph, centered at the vertices.

The exact integral homotopy types at the first two nontrivial widths are
\[
X_3\simeq\bigvee^4S^5,\qquad X_4\simeq S^4\vee\bigvee^{16}S^5.
\]
For every integer \(q\ge4\), inclusion of the first four columns \(X_4\hookrightarrow X_q\) admits a simplicial retraction. Consequently, both \(\mathbb Z\subseteq\widetilde H_4(X_q;\mathbb Z)\) and \(\mathbb Z^{16}\subseteq\widetilde H_5(X_q;\mathbb Z)\) are primitive direct summands. In particular, the onset of nonzero integral fourth homology is sharp: it is absent for \(q=3\) but present for all \(q\ge4\).

## Assumptions and scope
The graph has exactly three rows and at least three columns. The metric is the intrinsic shortest-path metric on the **geometric realization**, not the vertex-restricted metric; the ball radius is \(3/2\), with endpoints included. No statement about full homology ranks or higher homotopy types for \(q\ge5\) is made. The first public date of the motivating source is December 12, 2022.

## Proof
**Facet reduction.** In any graph with unit-length edges, a nonempty set of vertex-centered balls of radius \(3/2\) intersects exactly when the centers are contained in \(N[u]\cup N[v]\) for some graph edge \(uv\), provided the graph has no isolated vertices. Indeed any common point is on a vertex or within an edge; replacing a point in an edge by its midpoint does not increase any center's distance past \(3/2\), because all endpoint distances are integers and the center's minimum endpoint distance must be at most one. Conversely the midpoint witnesses every center at graph distance at most one from an endpoint.

In \(G_q\), an edge is either within a row or within a column. Thus every face lies in one of the following maximal candidate simplices: (R) a full row together with two full columns, or (C) a full column together with two full rows. Duplicated and contained candidates are discarded. These give 18 facets for \(q=3\), 30 facets for \(q=4\). The finite construction is independent of any homotopy assumptions.

**Exact finite Morse reductions.** Order the \(3q\) vertices first by row and then by column. Start with all nonempty faces; for each vertex in order, pair each remaining face not containing it with the remaining one-vertex extension, and remove both from further consideration. This provides 236 face pairs for \(q=3\) and 1466 for \(q=4\). The included self-contained verifier reconstructs every face and every pair; it builds the full oriented Hasse graph (reversing matched cover relations) and verifies by topological sorting that the matching is acyclic.

At \(q=3\), only a vertex and four five-dimensional cells remain critical. At \(q=4\), only a vertex, one four-dimensional cell and sixteen five-dimensional cells remain critical. Exact signed cellular Morse boundary reduction, as implemented in the attached code, gives the **zero** boundary from dimension five to four in both cases. Independently, full unreduced simplicial boundary elimination over \(\mathbb F_2\) returns ranks \((4)\) in degree five for \(q=3\), and \((1,16)\) in degrees four and five for \(q=4\). These finite checks are exhaustive over all faces of the claimed two seed complexes.

Forman's elementary discrete-Morse equivalence supplies a CW model having precisely the displayed critical cells. In the four-column case, its four-cell attaches to the unique zero-cell, giving \(S^4\). Any attaching map of a five-cell is a map \(S^4\to S^4\), classified by its integer degree. The zero integral Morse boundary forces every degree to vanish; hence every five-cell attaches trivially, yielding the displayed wedge. In the three-column case, the five-cells attach to a point and similarly give four five-spheres.

**Uniform split persistence.** For \(q\ge4\), identify every column \(j\ge4\) with column zero, leaving columns \(0,1,2,3\) unchanged, and apply this vertex map in all three rows. A simplex of type (R) maps into one full row and at most two full columns; one of type (C) maps into one full column and at most two full rows. Thus the map is simplicial \(\rho_q:X_q\to X_4\), and its composite with the four-column inclusion is the identity on \(X_4\). The induced maps split in every integral homology degree, proving the two direct summands and the sharp fourth-homology threshold. No inference from finite numerical extrapolation is used.

## Verification
Run the embedded `verify_rook.py` using standard Python 3, without third-party packages. It reconstructs all simplices from the two types of edge-midpoint witnesses; verifies 477 and 2950 nonempty faces, respectively; reconstructs all matched pairs; checks complete acyclicity of the gradient digraph; and evaluates the signed integral Morse boundary by exact integer recurrence. The recorded output is in `verification_output.txt`. Supplemental independent direct mod-two ranks were computed from the original simplicial boundary matrices.

## Relationship to prior work
Adams, Shukla and Singh study intrinsic Čech nerves of **binary hypercube graphs**, including their scale-three topology and a persistence nullhomotopy theorem. Those graphs are Cartesian products of \(K_2\), not the three-by-\(q\) rook graphs here. Published work on radius-one Čech nerves of rook graphs concerns scale two, while work on open-neighborhood complexes concerns a different complex. The present result distinguishes the first mixed-dimensional scale-three rook nerve and derives an infinite sharp onset by an explicit retraction, without claiming results already established for those other complexes.

## Limitations
The exact integral ranks for \(q\ge5\) and the complete filtration barcode are not established here. A finite verifier is a proof only of the two explicitly enumerated seeds; the all-width consequence rests on the separate algebraic simplicial retraction proof. Bibliographic searches cannot exclude unindexed equivalent statements. No independent mathematical audit has been performed.

## References
1. H. Adams, S. Shukla, and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first public December 12, 2022. https://arxiv.org/abs/2212.05871
2. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145. DOI:10.1006/aima.1997.1650.

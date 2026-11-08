# Twenty-six eight-spheres in the ordinary three-cut complex of the Frucht graph

## Finding
Let \(F\) be the twelve-vertex cubic Frucht graph specified below, and let \(\Delta_3(F)\) be the simplicial complex whose facets are the complements of disconnected induced three-vertex subgraphs of \(F\). Then
\[
\Delta_3(F)\simeq\bigvee^{26}S^8.
\]
In particular, \(\widetilde H_8(\Delta_3(F);\mathbb Z)\cong\mathbb Z^{26}\), with all other reduced integral homology groups zero. The complex is pure of dimension eight, with exactly 190 facets. This assertion concerns the ordinary cut complex, not the total-cut, independence, Čech, or neighborhood complex.

## Assumptions and scope
Take the vertex set \(V=\{0,1,\ldots,11\}\) and the following complete undirected edge set:
\[
\begin{aligned}
E=\{&(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),\\
&(3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),\\
&(7,11),(8,9),(8,11),(10,11)\}.
\end{aligned}
\]
This is a standard labeling of the Frucht graph. It has twelve vertices, eighteen edges, three triangles, and the single four-cycle on \(\{2,3,8,9\}\); the cycle and a triangle share the edge \((3,9)\). The graph is an extremal natural example: a smallest cubic graph with trivial automorphism group. No assertion for other cubic graphs is made.

For a three-element set \(T\subseteq V\), the induced graph \(F[T]\) is connected exactly when it has at least two of its three possible edges. For the Alexander dual \(D=\Delta_3(F)^\vee\), a set \(S\subseteq V\) is a face precisely when every three-element subset of \(S\) induces a connected graph.

## Proof
**1. Exhaustive structure of the Alexander dual.** For the displayed edge set, the induced connected triples consist of twenty-seven paths of length two and three triangles, for a total of thirty. Every pair is automatically a dual face. Exactly one four-vertex subset has all its triples connected: \(\{2,3,8,9\}\). No five-element subset has this property. The dual therefore has face numbers, grouped by cardinality from zero to four,
\[
(1,12,66,30,1).
\]
All counts are checked independently from the edge list by the included verifier, which enumerates every one of the \(2^{12}\) vertex subsets.

**2. An integral simplicial collapse.** The tetrahedron on \(\{2,3,8,9\}\) has the free triangular face \(\{2,3,8\}\). Remove this simplex pair. In the remaining two-dimensional complex, successively remove twenty-nine triangle–edge pairs. Each edge is free at the instant it is removed; the exact ordered sequence is printed by `verify_frucht_cut.py` and recorded in `verification_output.txt`. The verifier checks at each step that the lower face has exactly one active strict coface, its stated upper face. The remaining complex is a connected graph on all twelve vertices and thirty-seven edges. Hence the whole dual is homotopy equivalent to a wedge of
\[
37-12+1=26
\]
circles. In particular, its only nonzero reduced integral (co)homology occurs in degree one, where it is free of rank twenty-six. The free-face argument certifies integral homotopy, not merely field homology.

**3. Integral Alexander duality and homotopy type.** Combinatorial Alexander duality on the twelve-vertex ground set gives
\[
\widetilde H_i(\Delta_3(F);\mathbb Z)
\cong\widetilde H^{9-i}(D;\mathbb Z).
\]
It follows that the only nonzero reduced integral homology is \(\mathbb Z^{26}\) in degree eight. Because no dual face has five vertices, every subset of \(V\) with at most seven vertices is a face of \(\Delta_3(F)\). Thus \(\Delta_3(F)\) contains the complete six-skeleton of the eleven-simplex and is five-connected. Successive applications of the Hurewicz theorem, using the vanishing of integral homology in degrees six and seven, show that it is in fact seven-connected. Its dimension is eight. The Hurewicz isomorphism supplies twenty-six maps from eight-spheres representing a basis for its top integral homology. Their wedge induces an integral homology equivalence, which is a homotopy equivalence by the simply connected homology version of Whitehead's theorem.

## Verification
Run `python3 verify_frucht_cut.py` with Python 3 and no third-party dependencies. It checks the graph, classifies the dual faces by direct triple connectivity, verifies the full thirty-pair simplicial collapse, and checks that the residual graph is connected with thirty-seven edges. Separately, it generates the ordinary cut complex directly from disconnected triples, confirms the Alexander-dual identity for every vertex subset, and calculates all augmented mod-two boundary ranks of the original complex. The complete deterministic output is in `verification_output.txt`; its final line is a PASS statement. The field computation corroborates, but does not replace, the preceding integral proof.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and studied these cut complexes, including exact homotopy results for several graph families. Their 2023 preprint [1] has primary MSC2020 \(57\mathrm{M}15\). The subsequent paper [2] treats disjoint unions, squared paths, grids, and homology representations. Neither inspected paper states this Frucht-graph classification. Related theorems for graphs with triangles but **no** four-cycles, and for triangle-free graphs with edge-disjoint squares, do not imply this result because \(F\) has both three triangles and a four-cycle. An existing homotopy classification of the independence complex of \(F\) concerns another simplicial complex.

The Frucht graph is a motivated boundary instance: the four-cycle-free formula would give a numerical expression \(\binom{11}{2}-12\binom32+2\cdot3=25\), but its hypothesis fails here. The actual integral sphere multiplicity is twenty-six. This comparison is motivational only; the formula is **not** being applied as a theorem to the Frucht graph.

## Limitations
No general formula for cut complexes of cubic or asymmetric graphs, no shellability classification, and no equivariant homology calculation are asserted. The finite certificate uses an explicitly labeled twelve-vertex graph, so it proves this example rather than an infinite family. Published-work comparisons were performed against accessible primary papers and indexed results; unindexed or otherwise inaccessible equivalent work remains a possible originality risk.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first publicly posted 2023-04-26. https://arxiv.org/abs/2304.13675

[2] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158, first publicly posted 2024-07-11. https://arxiv.org/abs/2407.08158

[3] R. Frucht, *Graphs of Degree Three with a Given Abstract Group*, Canadian Journal of Mathematics 1 (1949), 365–378, DOI:10.4153/CJM-1949-033-6.

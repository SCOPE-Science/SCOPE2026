# Perfect matchings control the homotopy type of every fully whiskered matching complex

## Finding
Let \(G\) be any finite simple graph with \(n\ge1\) vertices. Attach a new pendant leaf to each vertex of \(G\), producing the **fully whiskered graph** \(W(G)\). Denote by \(p(G)\) the number of perfect matchings of \(G\), and write \(\mathcal M(H)\) for the ordinary matching complex of a graph \(H\): the vertices of the simplicial complex are graph edges, and its faces are sets of pairwise disjoint graph edges.

The following uniform homotopy classification holds without connectivity, planarity or bipartiteness assumptions:

\[
\mathcal M(W(G))\simeq
\begin{cases}
\mathrm{pt}, & p(G)=0,\\
\displaystyle\bigvee^{p(G)}S^{k-1}, & p(G)>0\text{ and }n=2k.
\end{cases}
\]

If \(n=2k\), the only possibly nonzero reduced integral homology is \(\widetilde H_{k-1}(\mathcal M(W(G));\mathbb Z)\cong\mathbb Z^{p(G)}\); for odd \(n\), every reduced group vanishes. These conclusions also hold with arbitrary field coefficients. In particular, the fully whiskered matching complex detects perfect matchability of the *original* graph by noncontractibility.

## Assumptions and scope
The vertex set \(V(G)\) is nonempty and finite; all original graph edges are undirected and simple. Fix any total order on \(V(G)\). Each original vertex \(v\) has a distinct new leaf \(v'\), with new edge \(e_v=\{v,v'\}\). The only new edges are these pendant edges. Perfect matching means a matching of original edges covering all original vertices. The matching complex is the **ordinary** complex of *all* graph matchings, not the different complex whose facets are constrained to be perfect matchings.

The convention \(\bigvee^q S^0\) is the disjoint union of \(q+1\) points, with a common distinguished point; thus the formula covers \(n=2\). For \(n=1\) the complex has one vertex and is contractible. No assertion is made for the empty base graph.

## Proof
**1. Partition all faces.** Let \(F\) be any face of \(\mathcal M(W(G))\). The original edges of \(F\) form a matching \(M\subseteq E(G)\). Write \(U(M)\subseteq V(G)\) for the original vertices that are not endpoints of edges of \(M\). All remaining edges of \(F\) are pendant edges \(e_v\), indexed by an arbitrary set \(T\subseteq U(M)\). Conversely, every pair \((M,T)\) of this kind defines a unique face. Hence the augmented face poset (including the empty face) is partitioned into Boolean fibers indexed by original matchings \(M\).

**2. Explicit matching in each fiber.** Whenever \(U(M)\ne\varnothing\), let \(v(M)\) be its least vertex in the fixed order. Pair every face \((M,T)\) with \(v(M)\notin T\) to the unique coface \((M,T\cup\{v(M)\})\). These are covering relations, are disjoint, and pair every face in the fiber. If \(U(M)=\varnothing\), the fiber consists only of \((M,\varnothing)\), which is left critical. Such a matching \(M\) is exactly a perfect matching of \(G\). Thus each perfect matching contributes precisely one critical simplex, having \(k\) edges and simplicial dimension \(k-1\), and there are no other critical faces.

**3. Global acyclicity, not just fiberwise matching.** Direct each cover relation downward (from the larger face to the smaller), except reverse the just-defined paired arrows. Along a reversed arrow, the original-edge matching \(M\) stays constant, since only a pendant edge was added. Along any downward arrow, \(M\) either stays constant (deleting a pendant edge) or strictly loses one original edge. A directed cycle therefore could not delete an original edge, so must lie within a fixed Boolean fiber. Inside this fiber, the reversed arrows only **add** the distinguished edge \(e_{v(M)}\). Every other downward arrow only removes a non-distinguished pendant edge. In a directed cycle, no removal of such an edge is possible because no arrow re-adds it; after excluding these, the distinguished edge can be added at most once and never removed. Hence no directed cycle exists. Equivalently, this is the standard patchwork acyclic-matching argument, but all its hypotheses have been verified directly.

**4. Homotopy conclusion.** The augmented discrete-Morse theorem (Forman's elementary cellular matching theorem in its reduced formulation) gives a based Morse CW model with one critical cell in dimension \(k-1\) for every perfect matching of \(G\), and no other reduced cells. If none exist, the complex is contractible. If they do, all cells have one common dimension. For \(k\ge2\) there are no lower positive-dimensional cells, so every attaching map lands in the basepoint and the CW model is a wedge of \(p(G)\) copies of \(S^{k-1}\). For \(k=1\), a two-vertex simple original graph has at most one perfect matching, and the reduced Morse complex consists of the basepoint plus that isolated critical vertex, yielding \(S^0\). These conclusions are integral homotopy equivalences, so their integral homology is free and concentrated as stated.

## Verification
The companion standalone file `VERIFY.py` constructs each complex directly, enumerates every original-edge matching, builds the leaf-toggling face matching, checks that precisely perfect matchings remain critical, and checks acyclicity through an explicitly constructed oriented augmented Hasse graph. It separately computes simplicial mod-two homology from boundary matrices, so it is not merely replaying the Morse-pair count.

A recorded run checked 1,114 explicitly specified finite graphs, 1,104 exact directed-Hasse acyclicity instances and 1,103 independent mod-two homology instances. The test set includes every labeled simple graph on one through five vertices and selected structured six- to eight-vertex graphs. It also checked cycle-base examples of lengths four through eight. The exact recorded output is in `VERIFY_OUTPUT.txt`; execute `python3 VERIFY.py` to reproduce it. These computations test the construction, but the proof above—not finite enumeration—establishes the result for every finite simple graph.

As two illustrations, \(p(C_6)=2\), hence \(\mathcal M(W(C_6))\simeq S^2\vee S^2\). A six-vertex complete graph has exactly fifteen perfect matchings, hence \(\mathcal M(W(K_6))\simeq\bigvee^{15}S^2\). For a five-cycle, there is no perfect matching and the whiskered matching complex is contractible.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega (first public preprint 2024-11-07) proved that matching complexes of **outerplanar** graphs are contractible or wedges of spheres. The present classification is valid for fully whiskered graphs of arbitrary finite simple base graphs, including nonouterplanar and nonplanar graphs, and specifies precisely the sphere dimensions and multiplicities as the perfect-matching count. The earlier theorem neither states nor forces the global exact formula.

Deshpande and Singh studied **higher independence complexes of fully whiskered graphs**. Those complexes have the original graph vertices as their simplicial vertices and are different from the matching complexes on graph edges studied here. Their exposition also provides a patchwork acyclic-matching principle consistent with the explicit proof above. General polygonal-line-tiling and tree matching-complex classifications likewise involve different or restricted graph families. The standard discrete-Morse construction and patchwork reasoning are credited and not claimed as new.

## Limitations
The classification concerns fully whiskered finite *simple* graphs. It does not determine equivariant homology representations, naturality of a basis under graph automorphisms, weighted filtrations, a persistence barcode, or a canonical equivalence attached to every perfect matching. It does not claim a new general theory of discrete Morse matchings. Equivalent published or unindexed formulations under different names remain a literature-search risk. No independent external audit has been performed.

## References
1. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1 (first public 2024-11-07), https://arxiv.org/abs/2411.04601v1 .
2. A. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first public 2020-01-15), https://arxiv.org/abs/2001.05448 .
3. M. Bayer, M. Jelić Milutinović and J. Vega, *General Polygonal Line Tilings and Their Matching Complexes*, arXiv:2211.12559 (first public 2022-11-22), https://arxiv.org/abs/2211.12559 .
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145 (discrete Morse framework).

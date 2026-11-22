# Universal sharp odd girth of tree three-colouring reconfiguration graphs

## Finding
Let \(T\) be any finite tree with \(n\ge1\) vertices. The vertices of \(\mathcal R(T)\) are proper colourings \(c:V(T)\to\mathbb Z/3\mathbb Z\); an edge changes the colour at precisely one vertex, preserving properness. Equivalently, \(\mathcal R(T)\) is the token-sliding graph on maximum independent sets of \(T\square K_3\), with one token per triangular fibre. The following assertions hold **for every tree shape**:

\[
\operatorname{oddgirth}(\mathcal R(T))=\begin{cases}3n,&n\text{ odd},\\\infty,&n\text{ even};\end{cases}
\qquad
\chi(\mathcal R(T))=\begin{cases}3,&n\text{ odd},\\2,&n\text{ even}.\end{cases}
\]

The graph is connected, and its ordinary girth is \(3\) for \(n=1\), \(6\) for \(n=2\), and \(4\) for \(n\ge3\). Thus for arbitrarily large odd trees, four-cycles coexist with an odd-girth barrier growing linearly and sharply with tree order.

For completeness, if \(d(v)\) denotes vertex degree, the exact vertex and edge counts, and resulting first Betti number of the **graph as a one-dimensional cell complex**, are
\[
|V(\mathcal R(T))|=3\cdot2^{n-1},\qquad
|E(\mathcal R(T))|=3\cdot2^{n-1}\sum_{v\in V(T)}2^{-d(v)},
\]
\[
\beta_1(\mathcal R(T))=1+3\cdot2^{n-1}\left(\sum_v2^{-d(v)}-1\right).
\]
The edge formula is an evaluation at three colours of the *previously published* chromatic-pairs polynomial for trees [2]. It is included to make the global graph-theoretic picture complete, not as an independent novelty claim.

## Assumptions and scope
The tree is finite, simple, connected and acyclic. The three colours are *named*, and each legal reconfiguration step changes one vertex to a different one of the other two colours. Odd girth is the length of the shortest simple odd cycle and is \(\infty\) if none exists. The formula for the Betti number concerns the one-skeleton only, not the homology of the associated independence or Hom complexes after filling higher-dimensional cells.

A maximum independent set of \(T\square K_3\) contains exactly one vertex per triangular fibre, since every fibre induces \(K_3\) and a proper three-colouring of a tree supplies an independent set of order \(n\). A horizontal token move would leave one fibre empty and put two tokens into another triangle, impossible for an independent set; hence legal token slides are exactly recolourings within fibres. This proves the reconfiguration-graph isomorphism.

## Proof
**Integer-height lift.** Fix a proper colouring \(c\) and root the tree. Choose an integer height at the root congruent to its colour modulo three. Extend uniquely over each tree edge, requiring \(h(w)-h(u)\in\{-1,1\}\) and \(h(v)\equiv c(v)\pmod3\) at every vertex. Such a lift exists because adjacent colours differ by one of the two nonzero residues, and those residues uniquely select the sign of the edge increment.

If one legal recolouring changes \(c\) only at vertex \(v\), then, when \(n\ge2\), all neighbours of \(v\) have the third, common colour. Therefore all adjacent height differences have the same sign, and \(h(v)\) is a local maximum or local minimum. Replacing \(h(v)\) by \(h(v)-2\) or \(h(v)+2\), respectively, is a unique valid lift of the recoloured state, leaving all other heights fixed. In the one-vertex case the same change by one of \(\pm2\) realizes either colour change. Thus every walk in \(\mathcal R(T)\) lifts to a sequence of changes by \(\pm2\) in exactly one coordinate.

**Closed-walk lower bound and parity.** Suppose a lifted walk of length \(L\) returns to its starting *colouring*. At both ends, every edge-height difference lies in \(\{-1,1\}\) and is congruent modulo three to the same nonzero colour difference. Consequently each edge-height difference is exactly the same at both ends. Connectedness of \(T\) then implies a constant final-minus-initial height \(3k\) over all vertices. Since coordinate parity is preserved under each \(\pm2\) change, \(3k\) must be even; hence it equals \(6q\) for some integer \(q\). Summing the height increments over all vertices gives \(6nq\), whereas each of the \(L\) moves changes that sum by \(\pm2\). Therefore
\[
L\ge3n|q|,\qquad L\equiv3nq\pmod2.
\]
When \(n\) is even, every closed walk has even length and the graph is bipartite. If a closed walk has odd length, then \(n\) and \(q\) are both odd, so \(L\ge3n\).

**Sharp construction.** Starting with any lifted colouring \(h\), order the vertices by nonincreasing original height (ties are arbitrary). Sweep once through that order, changing each height by \(-2\). Immediately before a vertex \(v\) is changed, its originally higher neighbours have already been lowered by two and its originally lower neighbours remain unchanged. Both kinds now have height \(h(v)-1\). The operation is therefore a legal recolouring, and after one sweep every height is lower by two. Repeat the same sweep twice more. Every step is legal and the final heights are lower by six, so the final colouring is the initial colouring. The resulting closed walk has length exactly \(3n\). For odd \(n\) it is odd; the preceding lower bound shows it must be a simple odd cycle (any repeated vertex would give a shorter odd closed subwalk). This proves the sharp odd-girth assertion.

**Connectedness and chromatic number.** Prove connectedness by induction on \(n\). The one-vertex colouring graph is a triangle. Remove a leaf \(v\) with neighbour \(u\). Lift any recolouring path of the smaller tree: whenever a pending recolouring of \(u\) would conflict with the current colour at \(v\), first recolour \(v\) to the third colour, which differs from both the old and intended new colours of \(u\). After lifting the smaller-tree path, recolour \(v\) to its prescribed final colour. This constructs a path between any two proper colourings of \(T\).

The map \(c\mapsto\sum_{v}c(v)\pmod3\) is a proper three-colouring of \(\mathcal R(T)\), because one move changes the sum by a nonzero residue. It has chromatic number two if \(n\) is even (bipartite and nonempty) and three if \(n\) is odd (odd cycle and a three-colouring).

**Ordinary girth.** At order one the graph is a triangle; at order two, the six proper colourings of an edge form a six-cycle. For any tree with \(n\ge3\), two nonadjacent leaves can be recoloured independently, producing a square. There are no triangles: for an adjacent pair of original-tree vertices there must always be a neighbour constraining any one-vertex recolouring, so a fixed coordinate cannot take all three colours while the rest are held fixed. Any triangle in a Hamming-type one-coordinate-change graph would have to vary only that one coordinate, which is therefore impossible. Hence ordinary girth is four for \(n\ge3\).

**Counts.** Choose a root colour in three ways and each other vertex in two ways, giving \(3\cdot2^{n-1}\) states. For \(n\ge2\), conditioned on the colour of a vertex of degree \(d\), its neighbours independently choose between the other two colours; all neighbours agree with probability \(2^{1-d}\). Exactly one alternative recolour is possible in that event. The sum of directed move counts divided by two yields \(|E|=3\cdot2^{n-1}\sum_v2^{-d(v)}\). The same formula holds directly for the one-vertex triangle. Finally connectedness gives \(\beta_1=|E|-|V|+1\).

## Verification
Run `python3 verify.py` in Python 3, using only the standard library. The checker independently enumerates all labelled trees through order five (146 cases), every proper three-colouring, the complete reconfiguration adjacency, connectivity, edge count, and shortest odd closed walk using parity-expanded breadth-first search. It also replays the legal three-sweep construction for every colouring and checks four larger tree shapes at each of orders six and seven. The exact replay output ends with `VERIFY_OK`.

These finite checks corroborate but do not replace the all-order proof, including its parity and lifting arguments.

## Relationship to prior work
The eligible source [1], first public on 2025-12-03 (primary MSC 05C15), studies the graph \(\mathcal C_3(T)\) for all trees, supplies connectedness and exact extremal diameters via balanced labelings, and supplies useful related integer-lift techniques. It does not state the shape-independent odd-girth value \(3n\), the bipartite parity cutoff, or the sharp square-versus-odd-cycle distinction; diameter information does not determine these cycle invariants. The older full-text work [2] gives the chromatic-pairs polynomial for trees, which already yields our edge-count formula upon specializing to three colours. We do not claim the known edge-count formula as new. The recent work [3] treats the *independence complex* of \(P_m\square C_3\), not the token-sliding graph on its maximum faces. The classical reconfiguration study [4] concerns algorithmic reachability and recolouring paths, not this all-tree odd-girth classification.

## Limitations
This is an unrestricted elementary proof, but historical priority remains conditional on literature indexing; an older equivalent cycle classification could be unindexed. No result is asserted for graphs with cycles, four or more named colours, or higher-dimensional homology of Hom or independence complexes. No independent audit has been performed. The edge-count component is explicitly previously implied, and the novelty claim is restricted to the sharp cycle/parity structure.

## References
[1] S. Asgarli, S. Krehbiel, S. MacLean, G. Zaimi, *Extremal diameters of 3-coloring graphs of trees*, arXiv:2512.03789v1, first public 2025-12-03. https://arxiv.org/abs/2512.03789

[2] S. Asgarli, S. Krehbiel, H. W. Levinson, H. M. Russell, *Counting Subgraphs of Coloring Graphs*, Graphs and Combinatorics 41 (2025), art. 82; first arXiv version 2024-01-23. https://doi.org/10.1007/s00373-025-02938-1

[3] B. Chakraborty, *Cohen–Macaulayness and Buchsbaumness of Cartesian Products of Paths and Cycles*, arXiv:2611.18495v1 (2026-11-13). https://arxiv.org/html/2611.18495v1

[4] L. Cereceda, J. van den Heuvel, M. Johnson, *Finding Paths Between 3-Colorings*, J. Graph Theory 67 (2011), 69–82. https://doi.org/10.1002/jgt.20514

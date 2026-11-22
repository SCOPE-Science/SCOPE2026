# Bipartition-protected edge-landmark mobility on the cuboctahedral graph

## Finding

Let \(Q_3\) be the graph on \(\{0,1\}^3\) joining words at Hamming distance one, and let \(C=L(Q_3)\) be its line graph (the twelve-vertex, twenty-four-edge cuboctahedral graph). A vertex subset \(S\subseteq V(C)\) **edge-resolves** \(C\) when the vectors \((d_C(s,e))_{s\in S}\), with \(d_C(s,uv)=\min\{d_C(s,u),d_C(s,v)\}\), differ for every two distinct edges \(e\) of \(C\). An edge-metric basis is a smallest such subset.

The following complete finite classification holds:

1. \(\operatorname{edim}(C)=5\), with exactly \(168\) distinct edge-metric bases. Under the identification \(V(C)=E(Q_3)\), each basis comprises five cube edges incident collectively with exactly seven of the cube's eight vertices. Exactly \(21\) bases omit each fixed cube vertex.
2. The unrestricted one-vertex-replacement (token-jump) reconfiguration graph on these \(168\) bases has \(948\) edges, is connected, and has radius and diameter both \(5\).
3. When a replacement is permitted only between adjacent vertices of \(C\) (token slide), the reconfiguration graph has \(360\) edges and exactly **two** connected components, each on \(84\) vertices, with radius and diameter both \(6\). The components are exactly the bases for which the unique unincident cube vertex belongs respectively to the even- or odd-weight bipartition class of \(Q_3\). A coordinate bit flip of \(Q_3\) interchanges these isomorphic components.

The \(168\) bases split into four automorphism orbits of sizes \(24,48,48,48\). For comparison, ordinary vertex-metric resolution on the same graph has minimum size \(3\), exactly \(96\) minimum bases, and a **connected** vertex-metric-basis token-slide graph of radius \(7\) and diameter \(8\). Thus edge resolution and vertex resolution lead to qualitatively different optimality-preserving local mobility on the same network.

## Assumptions and scope

Graphs are finite, undirected, simple and unweighted. Distances are shortest-path distances. A basis is represented by an unordered, unlabelled five-element subset of the twelve vertices of \(C\); exchanging one selected vertex \(x\) for one unselected vertex \(y\) is a token jump, and is a token slide only if \(xy\in E(C)\). Every intermediate state must itself be a minimum resolving set. The distinct vertices of \(C\) represent the twelve distinct edges of \(Q_3\); cube-vertex parity means Hamming-weight parity in \(\{0,1\}^3\), not a choice of orientation in Euclidean space. Reconfiguration graph edges are undirected and counted once.

## Proof

**Finite enumeration lemma.** Label the cube vertices by integers \(0,\ldots,7\) using their binary coordinates. Its twelve edges are the ordered list of pairs \((u,v)\) with \(0\le u<v<8\) and \(\operatorname{popcount}(u\oplus v)=1\). Two such pairs define adjacent vertices of \(C\) exactly when they share an endpoint. Thus the entire graph is reconstructed without external graph data.

For each \(s\in V(C)\), breadth-first search in this incidence-defined graph computes \(d_C(s,x)\) for all \(x\in V(C)\), and then \(d_C(s,uv)=\min\{d_C(s,u),d_C(s,v)\}\) for all \(24\) edges \(uv\in E(C)\). A subset resolves edges precisely when the \(24\) resulting distance tuples are pairwise distinct. Enumeration of all \(\binom{12}{4}=495\) four-subsets yields none that resolve; enumeration of all \(\binom{12}{5}=792\) five-subsets yields exactly \(168\). Monotonicity of edge resolution shows that no set of size below four resolves either. The five-subset enumeration further shows that every basis uses cube edges incident to exactly seven cube vertices and that the unique omitted cube vertex occurs in precisely \(21\) bases for each of the eight possible omissions. These are exhaustive mathematical finite sets, not sampled configurations. The standalone `verify_cube_edges.py` reproduces this test directly; `verify_polyhedron.py` independently constructs \(C\) from the twelve spatial points \((\pm1,\pm1,0)\) and their coordinate permutations and uses precomputed edge-pair witness masks instead of equality of distance-tuples.

**Parity obstruction.** Let \(S\) be one of these bases and \(m(S)\) its unique cube vertex unincident to all five selected cube edges. Every basis covers all four cube vertices of one bipartition class and exactly three of the other. An edge of the token-slide reconfiguration graph replaces one selected cube edge \(ab\) by another cube edge \(ac\) with a common endpoint \(a\). Since \(Q_3\) is bipartite, \(b\) and \(c\) have the same parity. The coverage of the opposite cube bipartition class therefore cannot change at that move. Switching the parity of \(m(S)\) would require the covered-vertex counts to change from \((3,4)\) to \((4,3)\), altering both classes; this is impossible. Hence the missing cube vertex's bipartition parity is constant along every slide path. There are \(4\cdot21=84\) bases of each parity.

**Exact component and metric certificate.** Build both graphs on the fully enumerated \(168\) masks. A jump edge is present exactly when the symmetric difference contains two vertices; a slide edge additionally requires their adjacency in \(C\). This yields respectively \(948\) and \(360\) edges. Exhaustive breadth-first search from **every** configuration obtains the all-pairs distance distribution, the component sizes, and all eccentricities. The jump graph is connected with each of its \(168\) eccentricities equal to \(5\). The slide graph has two components of \(84\) vertices, every one of whose eccentricities is \(6\). Combining this connectivity result with the parity obstruction proves that the two components are exactly the two missing-parity classes. A cube coordinate flip is an automorphism of \(C\) which changes the missing parity, establishing component isomorphism.

The jump distances among unordered distinct bases have counts \(948,2688,4704,5160,528\) at distances \(1,2,3,4,5\), summing to \(\binom{168}{2}=14028\). The finite slide distances within components have counts \(360,840,1512,1992,1740,528\) at distances \(1,2,3,4,5,6\), summing to \(2\binom{84}{2}=6972\). Distances between the two slide components are undefined (equivalently infinite under a convention for disconnected graphs). The vertex-metric comparison independently uses all \(\binom{12}{2}\) and \(\binom{12}{3}\) subsets and the same explicit move definitions.

## Verification

Two independent, standalone Python standard-library programs constitute the finite proof certificate and should be executed in the same folder as this document:

```
python3 verify_cube_edges.py
python3 verify_polyhedron.py
```

The first uses incidence of binary cube edges, equality of explicit distance signatures, and breadth-first searches. The second uses Euclidean coordinate differences to construct cuboctahedral adjacency, bitset hitting constraints for every pair of edges, and a separately coded full reconfiguration and distance enumeration. Their outputs were compared field by field and agreed on every independently computed statistic. `check_cube_edges.json` and `check_geometry.json` store actual outputs as convenient regression checks; they are not replacements for running the programs or checking the proof definitions.

The executable certificate enumerates all five-subsets, all four-subsets, all pairs of minimum bases, all pairs of configurations within each component, and, for the first checker, all \(48\) coordinate-flip/permutation cube automorphisms. Thus the scope of exhaustive enumeration is completely specified. It does not establish any formula for higher-dimensional cubes or line graphs of arbitrary graphs.

## Relationship to prior work

Edge-metric dimension and distance-to-edge resolution were introduced by Kelenc, Tratnik and Yero (2016; published 2018). Yi (2021) studies edge and fractional edge dimension in general graph families, including structural bounds, but the checked text has no cuboctahedral or cube-line-graph basis-reconfiguration classification. Avis and Hoang (2022) analyze token-sliding reconfiguration graphs of independent sets, a different feasibility predicate. The cuboctahedral graph's identification with \(L(Q_3)\), degree four, and automorphism group order \(48\) appear in MathWorld, without the present resolving-set classification. Indexed studies of edge-metric bases on the Heawood and Chvátal graphs concern non-isomorphic, distinct graph instances, and their numerical coincidences do not imply this parity-separated result.

The contribution is **not** the existence of the cuboctahedral graph, the definition of edge metric dimension, or a generic theorem asserting that some token-slide graphs are disconnected. It is the complete optimum-locating and move-graph metric classification on this graph, including a concrete bipartition-class invariant and an opposite connectivity behavior for ordinary vertex-metric bases.

## Limitations

The conclusion is an exact, computationally certified finite theorem for \(C=L(Q_3)\). The two independent implementations reduce shared programming errors but are not an independent human mathematical audit. No claim is made about line graphs of \(Q_d\) for \(d>3\), about dynamic or weighted networks, or about all polyhedral graphs. Existing unindexed literature or a historical equivalent result could affect priority. The all-pairs distance certificates prove the stated finite diameters, not a general infinite-family theorem.

## References

- Kelenc, A., Tratnik, N., Yero, I. G. *Uniquely identifying the edges of a graph: the edge metric dimension.* arXiv:1602.00291 (2016); Discrete Applied Mathematics (2018). https://arxiv.org/abs/1602.00291
- Yi, E. *On the edge dimension and fractional edge dimension of graphs.* arXiv:2103.07375, first posted 2021-03-12. https://arxiv.org/abs/2103.07375
- Avis, D., Hoang, D. A. *On Reconfiguration Graphs of Independent Sets under Token Sliding.* arXiv:2203.16861, first posted 2022-03-31. https://arxiv.org/abs/2203.16861
- Weisstein, E. W. *Cuboctahedral Graph.* MathWorld—A Wolfram Resource. https://mathworld.wolfram.com/CuboctahedralGraph.html

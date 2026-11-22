# Hexagonal mobility and frozen optimal power-domination triples on the Coxeter graph

## Finding

Let \(G\) be the 28-vertex Coxeter graph, defined explicitly below. Its minimum power-domination number is \(3\) and it has exactly \(336\) minimum power-dominating sets. Write \(R_{\mathrm{J}}\) for the graph of these three-vertex sets with an edge when one chosen vertex is replaced by an arbitrary unchosen vertex, and \(R_{\mathrm{S}}\) for the subgraph that permits a replacement only when the deleted and added vertices are adjacent in \(G\).

The sharp local mobility classification is
\[
R_{\mathrm{S}}\cong168K_1\sqcup28C_6.
\]
Each six-state component is supported on six original vertices spanning exactly three independent edges. Its states are six of the eight selections of one endpoint per edge, the two omitted selections being complementary. Among valid triples, the \(168\) isolated states have pairwise graph-distance signature \((3,3,3)\) and the \(168\) mobile states have signature \((3,3,4)\). These signatures distinguish mobility **only after** power domination is imposed; half of all triples with each signature are not power dominating.

In contrast, \(R_{\mathrm{J}}\) is connected, has \(336\) vertices and \(1764\) edges, radius \(5\), and diameter \(6\). Its degrees are \(9\) (on the \(168\) mobile states) and \(12\) (on the \(168\) frozen-under-sliding states). Its eccentricity distribution is \(112\) vertices of eccentricity \(5\) and \(224\) of eccentricity \(6\). The numbers of unordered pairs at distances \(1,2,3,4,5,6\) are respectively
\[
(1764,7392,19740,22428,4844,112).
\]

## Assumptions and scope

Use point labels \(0,1,\ldots,6\), with arithmetic modulo seven. Form the seven triples \(L_i=\{i,i+1,i+3\}\). Each unordered pair of distinct points lies in exactly one of these triples, so they form the Fano plane. The vertices of \(G\) are the \(28\) three-point subsets **not** equal to any \(L_i\). Two vertices of \(G\) are adjacent exactly when their point triples are disjoint. This is the standard Fano-plane construction of the Coxeter graph, with \(28\) vertices, \(42\) edges and degree three.

For a sensor set \(S\), first observe its closed neighborhood \(N[S]\). Subsequently, whenever an observed vertex has exactly one unobserved neighbor, observe that neighbor. Repeat to closure. The set \(S\) power dominates if and only if the closure is all \(28\) vertices. Both reconfiguration rules preserve the number of sensors and require every intermediate set to power dominate. Unrestricted replacement is token jumping; adjacent replacement is token sliding.

All labels and counts refer to distinct labelled subsets of this particular finite graph; no infinite-family extension is claimed.

## Proof

The result has a finite exhaustive proof with two separate, executable implementations, `verify_cyclic.py` and `verify_xor.py`. Both derive the graph from a definition, rather than taking precomputed state or adjacency tables as input.

**1. Complete generation.** Generate all \(\binom73-7=28\) nonline triples, join disjoint triples, and check there are exactly \(42\) edges and each vertex has three neighbors. For each sensor subset of cardinality at most three, compute its observation closure by the above forcing rule. The programs inspect exactly \(1+\binom{28}{1}+\binom{28}{2}+\binom{28}{3}=3683\) choices, including the empty set. Neither the empty set nor any singleton or pair works; exactly \(336\) triples work. Thus \(3\) is the global minimum, not merely the minimum within a sample.

**2. Exact movement graphs.** On the complete list of \(336\) successful triples, two states are joined by a jump precisely when their intersection has size two. They are joined by a slide precisely when the replaced vertices are adjacent in \(G\). The resulting undirected jump graph has \(1764\) edges and degree multiplicities \(168\) of degree \(9\) and \(168\) of degree \(12\). The slide graph has \(168\) edges, with \(168\) vertices of degree zero and \(168\) vertices of degree two. Exhaustive connected-component traversal finds \(168\) singleton components and exactly \(28\) six-vertex components. A connected simple graph in which each of six vertices has degree two is \(C_6\), proving the displayed decomposition.

**3. Three-edge support of each mobile hexagon.** For each six-state component, compute the union of its selected original-graph vertices. The union has exactly six elements, whose induced original-graph edges form a three-edge matching. Every one of its six states chooses exactly one endpoint of each edge. Of the \(2^3=8\) endpoint choices, the two missing triples are complements within that six-vertex support. This is explicitly checked for all \(28\) components, including distinctness of their three-edge supports. This explains the hexagonal geometry: the cube of three independent endpoint switches is deprived of two opposite corners, leaving a six-cycle.

**4. Metric and geometric checks.** Breadth-first search from every one of the \(336\) jump states visits all other states and returns the stated degree, eccentricity, radius and diameter data. Counting only unordered vertex pairs yields the six distance coefficients whose sum equals \(\binom{336}{2}=56280\). Independently, breadth-first search in the original Coxeter graph computes the three pairwise distances within every successful triple and gives exactly \(168\) signatures \((3,3,3)\) for frozen states and \(168\) signatures \((3,3,4)\) for mobile states. The degree distribution and component counts are checked directly, not inferred from sample paths.

These finite computations are an exhaustive proof for the explicitly defined 28-vertex graph; no probabilistic sampling, extrapolation or unstated classification is used. The programs contain assertions for every numerical and structural statement above and require only Python's standard library.

## Verification

Run `python3 verify_cyclic.py` and `python3 verify_xor.py` in the same directory as this document. Each prints one `VERIFY_OK` line containing identical JSON summaries. The first realization uses seven cyclic Fano lines, bit-mask propagation with parallel forcing rounds and bit-mask state graphs. The second uses the independent XOR construction of the Fano plane on the seven nonzero three-bit vectors, set-based sequential forcing and tuple-state breadth-first search. Both directly generate the full candidate state space and validate three-edge matching supports for all mobile components.

The identical numerical output includes `optimal_sets=336`, `jump_edges=1764`, `slide_edges=168`, `slide_components={"1":168,"6":28}`, and jump distance-pair counts \((1764,7392,19740,22428,4844,112)\). Independent implementations mitigate, but do not eliminate, the risk of conceptual errors in the common mathematical definitions.

## Relationship to prior work

Bjorkman et al. introduced power-domination token-jump and token-addition/removal reconfiguration, including universal graph-theoretic results and specific families such as complete and complete bipartite graphs [1]. Their work supplies the reconfiguration framework, not this Coxeter-graph classification. Anderson and Kuenzel studied power domination in cubic graphs and Cartesian products [2]. Their cubic-graph bounds do not provide the exact Coxeter-graph minimum-set census or the two movement graphs. The Coxeter Fano-plane model and standard parent-graph properties are classical background [3]. In particular, no new construction of the Coxeter graph is claimed.

A 2023 study of sensor failure [4] concerns a different probabilistic reliability predicate, not optimal sensor relocation. Nearby results on Coxeter perfect matchings and Heawood path-cover reconfiguration concern distinct solution predicates; their statements do not imply the present 336-state power-domination classification. Searches for equivalent wording, full implications and exact tables found no covering result among the inspected sources. This is evidence of originality under the search scope, not a claim that every possible historical source has been excluded.

## Limitations

This is a finite computer-assisted classification, not a theorem about arbitrary cubic graphs. The structural matching-support statement and numerical shortest-path claims rely on complete, auditable enumeration rather than a symbolic closed-form classification of all Fano-plane triples. The argument does not establish uniqueness in the world literature, and an unindexed earlier source could cover part or all of the finding. The code verifies exactly the stated 28-vertex model and does not certify other graph conventions or sensor-failure models.

## References

[1] B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob and C. Reinhart, *Power domination reconfiguration*, first public arXiv draft 2022-01-05, https://arxiv.org/abs/2201.01798 ; open-access article https://doi.org/10.1007/s44007-025-00187-5.

[2] S. E. Anderson and K. Kuenzel, *Power domination in cubic graphs and Cartesian products*, first arXiv submission 2022-09-08, https://arxiv.org/abs/2209.03931.

[3] *Coxeter graph*, Fano-plane construction and basic graph data, https://en.wikipedia.org/wiki/Coxeter_graph ; see also https://mathworld.wolfram.com/CoxeterGraph.html.

[4] B. Bjorkman, Z. Brennan, M. Flagg and J. Koch, *Power domination with random sensor failure*, first submitted 2023-12-19, https://arxiv.org/abs/2312.12259.

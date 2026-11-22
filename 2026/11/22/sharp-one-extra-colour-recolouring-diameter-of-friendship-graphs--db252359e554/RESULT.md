# Sharp one-extra-colour recolouring diameter of friendship graphs

## Finding

Let \(F_t=K_1\vee(tK_2)\) be the friendship graph made of \(t\) triangles sharing one common hub. All base-graph vertices are distinct and named. A proper \(q\)-colouring uses named colours from \(\{0,\ldots,q-1\}\), not necessarily every colour; in its recolouring graph \(\mathcal R_q(F_t)\), two colourings are adjacent precisely if they differ at one base-graph vertex while remaining proper.

**Theorem.** For every integer \(t\ge1\), the three-colour recolouring graph is edgeless on \(3\cdot2^t\) states. The four-colour recolouring graph is connected, has \(4\cdot6^t\) states and \(4t6^t+6\cdot2^t\) edges, and its exact diameter is
\[
\operatorname{diam}\mathcal R_4(F_t)=3t+1.
\]
The number of states supporting a recolouring of the common hub is exactly \(12\cdot2^t\); each such state permits exactly one hub recolouring. A shortest-length witness for the diameter and a constructive \(3t+1\)-move upper bound for arbitrary pairs are given below. No assertion about the exact distance of arbitrary pairs or the radius for all \(t\) is required.

## Assumptions and scope

We use the ordinary, undirected *single-vertex* recolouring graph, with fixed vertex identities and a fixed named palette. The central vertex is \(z\), and the vertices in petal \(i\) are adjacent \(x_i,y_i\). Its three edges are \(zx_i,zy_i,x_iy_i\), for \(1\le i\le t\), with no other edges. The chromatic number of \(F_t\) is three. All formulas apply at \(t=1\) as well as for arbitrarily many petals. States are not quotiented by petal permutations, leaf swaps, or global renaming of colours. Distances count individual vertex recolourings, not simultaneous colour changes or Kempe moves.

## Proof

**Three colours.** Once the hub colour is fixed, each of the \(t\) ordered pairs on a petal must use the other two colours in one of two orders. Hence \(3\cdot2^t\) states exist. Every vertex belongs to a triangle displaying all three colours: recolouring any vertex with the fixed three-colour palette would repeat a neighbour's colour. Thus every state is isolated.

**Four-colour geometry and counting.** Fix the hub colour \(h\). Each petal then carries one of the six ordered pairs of distinct colours in the three-element set of colours other than \(h\). Within a fixed hub-colour layer, changing one endpoint of a petal changes its ordered pair along one edge of a six-cycle: every ordered pair has exactly two legal single-endpoint changes, and the resulting connected two-regular graph has six vertices. Different petals are independent. Therefore the fixed-hub layer is the Cartesian product of \(t\) copies of \(C_6\), with \(6^t\) vertices, degree \(2t\), and \(t6^t\) undirected edges. Over the four hub colours, this contributes \(4\cdot6^t\) vertices and \(4t6^t\) edges.

For distinct hub colours \(h,h'\), a centre change from \(h\) to \(h'\) is legal exactly when \(h'\) is absent from *all* petals. Their two endpoint colours must then be the two colours \(a,b\) outside \(\{h,h'\}\), in either order. There are exactly \(2^t\) such states and exactly \(2^t\) centre-change edges for this unordered hub-colour pair. There are six unordered pairs \(h,h'\), hence \(6\cdot2^t\) additional edges. Each state has either zero or one legal hub change because even a single petal uses two of the three colours distinct from \(h\); consequently exactly \(12\cdot2^t\) states support a hub change.

**Local gateway lemma.** For any distinct hub colours \(h,h'\), let \(a,b\) be the other two palette colours and let \(g_0=(a,b)\), \(g_1=(b,a)\) be the two petal pairs compatible with both hub colours. These two pairs are antipodal at graph distance three on the six-cycle for hub \(h\), and also on the six-cycle for hub \(h'\). If \(s\) is any legal petal pair at hub \(h\) and \(v\) is any legal petal pair at hub \(h'\), write \(d_h\) and \(d_{h'}\) for the two six-cycle distances. Antipodality implies
\[
\bigl(d_h(s,g_0)+d_{h'}(g_0,v)\bigr)
+\bigl(d_h(s,g_1)+d_{h'}(g_1,v)\bigr)=6.
\]
Therefore at least one gateway choice has total leaf-recolouring cost at most three.

**Connectivity and sharp upper bound.** If two target colourings share their hub colour, independently traverse shortest paths in their \(t\) six-cycles. This uses at most \(3t\) moves. Otherwise, apply the local gateway lemma independently to each petal. First take every petal from its source pair to its chosen gateway pair while keeping the source hub colour; change the hub once; then take every petal from its gateway pair to its target pair with the target hub colour. The total number of leaf moves is at most \(3t\), and the hub changes once, giving a valid path of length at most \(3t+1\). In particular the graph is connected.

**Matching lower bound.** Name the four colours \(h,a,b,c\). Let \(\alpha\) give the hub colour \(h\) and assign the ordered pair \((a,b)\) to every petal. Let \(\beta\) give the hub colour \(c\) and assign \((b,a)\) to every petal. Each petal must exchange its two endpoint colours. This requires at least three recolourings on that petal: both endpoints must change, but if each were changed only once then the first change would assign the other endpoint's currently occupied colour, contradicting properness. Hub changes cannot alter this obstruction, so at least \(3t\) leaf moves are necessary. The hub has different initial and final colours and needs at least one additional move. Thus every \(\alpha\)-to-\(\beta\) path has length at least \(3t+1\). Equality is attainable: for each petal, perform \((a,b)\to(c,b)\to(c,a)\to(b,a)\) while the hub stays \(h\), then recolour the now-eligible hub from \(h\) to \(c\). Consequently the exact diameter is \(3t+1\).

## Verification

The included standalone Python 3 file `verify.py` enumerates named proper four-colourings directly, generates moves by independently checking every possible one-vertex recolouring against the base graph, and verifies counts, edge reversibility and connectivity. To limit redundant breadth-first searches, eccentricity is computed once for each canonical class under global palette permutations and petal permutations; these are graph automorphisms, so one representative per class is exhaustive for eccentricity. This check covers \(1\le t\le5\), up to \(31{,}104\) vertices, and confirms that all tested eccentricities equal \(3t+1\). In addition it exhaustively verifies the six-cycle gateway lemma for each ordered pair of distinct hub colours. Run `python3 verify.py` in the directory containing the supplied file. `verification_output.txt` records a successful execution. These finite checks are supplementary and do not substitute for the all-\(t\) proof above.

## Relationship to prior work

The 2020 paper of Biedl, Lubiw and Merkel constructs OAT graphs using operations that include attaching a clique at a vertex, and establishes connectivity and a general polynomial diameter bound at one extra colour. Friendship graphs are in this general graph class. The 2022 paper of Belavadi, Cameron and Merkel reports broad recolouring-connectivity and upper-diameter results, including a \(4n\) bound for \(P_4\)-free graphs, which includes \(F_t\). The 2024 modular-decomposition work focuses on connectivity of further hereditary classes. These general results imply that some recolouring sequence exists but not this exact \(3t+1\) worst-case minimum. The new proof identifies the six-cycle product layers, exact hub-change gateway count and antipodal-leaf obstruction that make the bound sharp. Searches for the same assertion under friendship, Dutch windmill, clique bouquet and \(K_1\vee(tK_2)\) terminology found no covering exact result among the checked sources; non-indexed historical literature has not been exhaustively excluded.

## Limitations

This is a specialized exact theorem for four *named* colours on a specific all-size graph family. It does not assert an optimal diameter for arbitrary chordal, cograph or OAT graphs; it does not establish an explicit distance formula between each pair of colourings, nor does it classify the radius for all sizes. It does not concern edge colourings, simultaneous recolourings or colour-permutation-quotiented states. Source coverage cannot establish absolute historical novelty; independent mathematical assessment remains unperformed.

## References

1. T. Biedl, A. Lubiw, O. Merkel, *Building a larger class of graphs for efficient reconfiguration of vertex colouring*, arXiv:2003.01818 (first publicly posted 2020-03-03). https://arxiv.org/abs/2003.01818
2. M. Belavadi, K. Cameron, O. Merkel, *Reconfiguration of vertex colouring and forbidden induced subgraphs*, arXiv:2206.09268 (first publicly posted 2022-06-18). https://arxiv.org/abs/2206.09268
3. M. Belavadi, K. Cameron, N. L. D. Sintiari, *Recoloring via modular decomposition*, arXiv:2405.06446 (first publicly posted 2024-05-10). https://arxiv.org/abs/2405.06446
4. M. Bonamy, M. Johnson, I. Lignos, V. Patel, D. Paulusma, *Reconfiguration graphs for vertex colourings of chordal and chordal bipartite graphs*, Journal of Combinatorial Optimization 27 (2014), 132–143. https://doi.org/10.1007/s10878-012-9490-y

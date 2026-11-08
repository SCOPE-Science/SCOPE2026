# Strong-majority two-edge-colourings of quartic graphs and Hamming-layer codes

## Finding

**Theorem.** Let \(G\) be any finite connected simple \(4\)-regular graph. A *named two-colour strong-majority edge colouring* is a map \(c:E(G)\to\{\mathrm{red},\mathrm{blue}\}\) such that, for each edge, exactly three of its six adjacent edges are red and three are blue. Let \(\mathcal H(G)\) consist of all nonempty vertex sets \(C\subseteq V(G)\) with the following property: their distance layers
\[
L_i(C)=\{v\in V(G):\operatorname{dist}_G(v,C)=i\},\qquad 0\le i\le4,
\]
partition \(V(G)\), and each vertex in \(L_i(C)\) has exactly \(i\) neighbours in \(L_{i-1}(C)\) and \(4-i\) neighbours in \(L_{i+1}(C)\), with empty out-of-range layers. Then the set of named two-colour strong-majority edge colourings is in canonical bijection with \(\mathcal H(G)\). In particular,
\[
N_2(G)=|\mathcal H(G)|,\qquad N_2(G)>0\ \Longrightarrow\ 16\mid |V(G)|,
\]
and every \(G\) with \(N_2(G)>0\) is bipartite. For each \(C\in\mathcal H(G)\),
\[
(|L_0|,|L_1|,|L_2|,|L_3|,|L_4|)
=\frac{|V(G)|}{16}(1,4,6,4,1).
\]

The sets \(C\) are precisely completely regular radius-four codes with intersection array \((4,3,2,1;1,2,3,4)\), where the first four entries count neighbours one layer farther from \(C\), and the final four count neighbours one layer nearer.

The divisibility bound is sharp. On the four-cube \(Q_4\), exactly \(16\) such named colourings exist. On the \(16\)-vertex quartic graph formed from \(Q_4\) by exchanging edges \(\{1,9\},\{2,10\}\) for \(\{1,10\},\{2,9\}\), exactly \(8\) exist. The two graphs are nonisomorphic: they have respectively \(24\) and \(22\) distinct four-cycles. Thus the two-colouring count is not fixed by the graph order, even at the smallest possible order.

## Assumptions and scope

Graphs are finite, simple, undirected and connected; degree is exactly four at every vertex. Vertices of \(Q_4\) are numbered \(0,\ldots,15\) by their four binary coordinates; the endpoints of every exchanged edge above are distinct. Two colours are **named**, so interchanging them is a different colouring. Colour classes are not required to be proper. The neighbours of an edge consist of other edges sharing at least one endpoint; there are six for a quartic graph. Every vertex in each of the five nonempty layers has the indicated counts, including the boundary cases \(i=0,4\).

## Proof

Fix a named two-colour strong-majority edge colouring \(c\). For each vertex \(v\), let \(r(v)\in\{0,1,2,3,4\}\) be its number of incident red edges. Given a red edge \(uv\), among the six adjacent edges precisely three are red, hence
\[
r(u)+r(v)-2=3,\qquad r(u)+r(v)=5.
\]
Given a blue edge \(uv\), exactly three adjacent edges are red, so
\[
r(u)+r(v)=3.
\]
Consequently a vertex with red-degree \(k\) has red neighbours of red-degree \(5-k\) and blue neighbours of red-degree \(3-k\), whenever these neighbours exist. The only possible type transitions are
\[
0\stackrel{\mathrm{blue}}{-}3\stackrel{\mathrm{red}}{-}2
\stackrel{\mathrm{blue}}{-}1\stackrel{\mathrm{red}}{-}4.
\]
Each type has respectively \(4,1,2,3,0\) red edges, so its numbers of neighbours in the preceding and following displayed type classes are exactly \((0,4),(1,3),(2,2),(3,1),(4,0)\). The graph is connected and contains an edge; all red-degree types necessarily occur: any occupied class forces neighbouring classes, and the resulting five-class transition path is connected and has no proper nonempty transition-closed subcollection.

Set \(C=\{v:r(v)=0\}\). In the displayed order, each vertex in a later class has a neighbour in the preceding class, and every graph edge joins consecutive classes. Therefore a vertex in the \(i\)-th class has a path of length \(i\) to \(C\), and no shorter path, since its class index changes by exactly one at each step. The five classes are precisely \(L_0(C),\ldots,L_4(C)\). They have the required intersection array. Uniqueness of \(C\) follows directly from its definition in terms of the colouring.

Conversely, suppose \(C\in\mathcal H(G)\). Each edge joins consecutive distance layers because the asserted within-layer neighbour counts total four; the classes are all nonempty, by connectedness and the required layer transitions. Colour edges joining \(L_0\) to \(L_1\) and \(L_2\) to \(L_3\) blue; colour edges joining \(L_1\) to \(L_2\) and \(L_3\) to \(L_4\) red. The red degrees on the consecutive layers are
\[
0,\ 3,\ 2,\ 1,\ 4.
\]
Thus every red edge has endpoint red-degree sum \(5\) and every blue edge has endpoint red-degree sum \(3\). For either edge, exactly three adjacent edges are red and three blue, proving strong majority. The vertices with red-degree zero are exactly \(C\), so the two constructions invert each other.

Double-counting edges between successive layers gives
\[
4|L_0|=|L_1|,\quad3|L_1|=2|L_2|,\quad
2|L_2|=3|L_3|,\quad |L_3|=4|L_4|.
\]
Hence \((|L_i|)=(a,4a,6a,4a,a)\) for a positive integer \(a\), and \(|V(G)|=16a\). Every edge joins layers of opposite index parity, so \(G\) is bipartite.

For the two \(16\)-vertex examples, the layer cardinalities force \(C\) to be a singleton. A vertex \(v\) is an admissible singleton if and only if its distance layers have the intersection array above. In \(Q_4\), every vertex is such a singleton by Hamming-distance counting, giving \(16\). In the specified switched graph, explicit enumeration of the \(16\) possible singleton centers using graph distances gives exactly \(8\), reproduced in the accompanying standalone verifier. The verifier also computes four-cycle counts from common-neighbour intersections, giving \(24\) and \(22\), so the graphs are not isomorphic. The general bijection and divisibility conclusion do not depend on finite computation.

## Verification

The standalone standard-library program `verify.py` checks the local strong-majority condition by enumerating adjacent edges, rather than relying solely on the layer criterion. It exhausts all \(2^{10}\) and \(2^{16}\) named edge colourings of \(K_5\) and \(K_{4,4}\), respectively, finding none. It enumerates all possible singleton code centers in the two \(16\)-vertex graphs, checking their distances, intersection arrays, constructed colourings and four-cycle counts. It additionally constructs a connected twisted double cover of \(Q_4\), enumerates all \(\binom{32}{2}=496\) potential two-vertex codes, and finds exactly \(40\) admissible ones, verifying each constructed colouring against the original edge condition. Run with `python3 verify.py` from the directory containing this file and the script. The unrestricted classification is established by the preceding proof, not by finite checks.

## Relationship to prior work

Kalinowski, Kamyczura, Pilśniak and Woźniak introduced strong-majority edge colourings and bounded their number of colours, including upper bounds for even-degree graphs. Antoniuk, Prorok and Salia later improved general upper bounds. Pękała and Przybyło observed the broad necessary condition that connected graphs admitting two strong-majority edge colours must have all degrees even or all odd, but their results do not give the precise quartic code criterion. Freyberg and Marr defined neighbourhood-balanced vertex colouring; applying their definition to the line graph makes it equivalent to the present two-colour edge condition, but their circulant classification concerns quartic **coloured graphs**, not line graphs of arbitrary quartic graphs. The contribution here is the exact five-layer completely regular code bijection, its sharp divisibility restriction, and its counting interpretation for *all* finite connected quartic graphs. Searches found no stronger covering classification; this historical assessment is provisional.

## Limitations

This result applies to finite connected simple \(4\)-regular graphs and exactly two named colours. It does not determine higher strong-majority indices or count the layer codes in all quartic graphs. Its characterization may require enumerating vertex subsets in the general case. All numerical examples are finite computational checks; independent mathematical review has not been performed. Historical priority remains provisional.

## References

- R. Kalinowski, M. Kamyczura, M. Pilśniak and M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828v1 (22 May 2026), https://arxiv.org/abs/2605.23828.
- S. Antoniuk, M. Prorok and N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212v1 (30 June 2026), https://arxiv.org/abs/2607.00212.
- P. Pękała and J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122v1 (4 August 2026), https://arxiv.org/abs/2608.04122.
- B. Freyberg and A. Marr, *Neighborhood Balanced Colorings of Graphs*, Graphs and Combinatorics **40**, 41 (2024), https://doi.org/10.1007/s00373-024-02766-9.

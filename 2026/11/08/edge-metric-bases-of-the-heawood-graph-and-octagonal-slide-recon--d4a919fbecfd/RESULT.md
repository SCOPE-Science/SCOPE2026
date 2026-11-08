# Edge-metric bases of the Heawood graph and octagonal slide reconfiguration

## Finding

Let \(H\) be the point–line incidence graph of the Fano plane. An **edge-metric resolving set** is a vertex set whose distance vectors distinguish all 21 edges, with distance from a vertex to an edge defined as the minimum of its distances to the edge's endpoints. Then \(\operatorname{edim}(H)=5\), and exactly 168 five-vertex sets attain this minimum.

The bases have a complete geometric classification. In one class, choose a noncollinear triple of Fano points and two of the three Fano lines meeting that triple in exactly one point each; the other class is the point–line dual, choosing a nonconcurrent triple of lines and two of the three points incident with exactly one chosen line. These classes each contain 84 bases.

Join two bases when one selected vertex can be exchanged for one unselected vertex. The token-jump graph has 168 vertices, 420 edges, degree five at every vertex, and radius and diameter five. If an exchange is allowed only along an edge of \(H\) (token sliding), the resulting graph is the disjoint union \(21C_8\). In fact, the vertex union of the eight bases in any slide component is the vertex set of an eight-cycle of \(H\), and this gives a bijection between the 21 slide components and the 21 eight-cycles of \(H\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Points are \(p_i\), lines are \(\ell_j\), where \(i,j\in\{0,1,\ldots,6\}\). Incidence is \(p_i\in\ell_j\) exactly when \(i-j\pmod 7\in\{0,1,3\}\). Hence \(V(H)\) consists of seven point vertices and seven line vertices, and \(E(H)\) is the set of 21 incident point–line pairs. The graph distance \(d_H\) is unweighted shortest-path distance. For \(e=uv\), put \(d_H(s,e)=\min\{d_H(s,u),d_H(s,v)\}\). A set \(S\subseteq V(H)\) resolves edges if the vectors \(\bigl(d_H(s,e)\bigr)_{s\in S}\) are different for all distinct edges \(e\); the chosen order of \(S\) is immaterial.

The reconfiguration graphs use *minimum* edge-metric resolving sets only. Token jumping replaces one element by any other graph vertex; token sliding requires the removed and inserted vertices to be adjacent in \(H\). There is no assumption about ordered landmarks or about a larger finite projective plane.

## Proof

**1. Distances.** For any incidence edge \(e=(p_i,\ell_j)\) and a point landmark \(p_a\), the edge distance is zero if \(a=i\), one if \(a\ne i\) and \(p_a\in\ell_j\), and two otherwise. Indeed, different points are at graph distance two, while a point is at distance one or three from a line according to incidence. Dually, for a line landmark \(\ell_b\), the edge distance is zero if \(b=j\), one if \(b\ne j\) and \(p_i\in\ell_b\), and two otherwise. These two formulas specify the entire \(14\)-by-\(21\) distance table, without approximate arithmetic.

**2. Exhaustive finite classification.** The following is a complete small certificate, not a sampling argument. Enumerate every unordered pair of distinct edges of \(H\) (210 pairs). For each possible landmark \(s\), form the 210-bit integer whose bit for \(\{e,f\}\) is one exactly when \(d_H(s,e)=d_H(s,f)\). A vertex set \(S\) resolves precisely when the bitwise intersection of its landmark integers is zero. Apply this exact test to every subset of cardinality at most five. The complete counts are: no resolving subsets of sizes zero through four, and precisely 168 resolving five-subsets. There are only \(\sum_{k=0}^{5}\binom{14}{k}=3473\) subsets to check. This is implemented verbatim, using breadth-first graph distances, in `heawood_edge_bases_verify.py`.

Independently, `heawood_edge_bases_verify_alt.py` uses the closed incidence distance formulas from Step 1 and constructs the geometric candidates directly. There are 28 noncollinear point triples (35 triples minus seven lines). Each has precisely three one-secant lines, allowing three selections of two lines. Hence this class has \(28\cdot3=84\) members. The dual line construction likewise has 84 members. The second program checks all 2002 five-subsets against its independently computed edge-distance vectors and proves that their resolving members are *exactly* the disjoint union of these two candidate classes. Therefore the preceding exhaustive lower bound and the geometric characterization agree, giving \(\operatorname{edim}(H)=5\) and 168 bases.

**3. Replacement graphs.** For each of the 168 certified bases \(S\), enumerate each \(u\in S\) and each \(v\in V(H)\setminus S\), and check membership of \((S\setminus\{u\})\cup\{v\}\) in the complete list of bases. This produces each token-jump edge. Restricting these exchanges to \(uv\in E(H)\) gives every token-slide edge. Each of the two standalone implementations independently makes this enumeration. They agree on 420 jump edges and 168 slide edges. Every jump vertex has degree five. Breadth-first search from each of the 168 jump states reaches every state and has eccentricity five, establishing connectedness and diameter (and radius) five. For a simple lower-bound witness, \(\{p_0,p_1,p_2,\ell_2,\ell_4\}\) and \(\{p_3,p_4,p_5,\ell_0,\ell_1\}\) are disjoint bases: at least five single-vertex exchanges are required to transform one into the other.

Every slide state has degree two, and complete component search finds exactly 21 components of size eight. A connected finite simple two-regular graph on eight vertices is \(C_8\), so the slide graph is \(21C_8\). The second verifier additionally enumerates all simple eight-cycles in \(H\), modulo cyclic rotation and reversal, and obtains exactly 21. Taking the union of all graph vertices used by the eight bases in each slide component gives 21 distinct eight-element sets, exactly equal to the vertex sets of those 21 original eight-cycles. Thus the claimed cycle correspondence is an explicit equality of two fully enumerated finite families.

The certificate is self-contained: its graph is constructed only from the displayed modular incidence rule, its distance and resolution tests follow the displayed definitions, and every finite universe over which it quantifies is exhaustively generated. Neither a failed search nor a timed-out calculation is counted as a proof.

## Verification

With Python 3 standard library, run `python3 heawood_edge_bases_verify.py` and `python3 heawood_edge_bases_verify_alt.py`. Both scripts were run from the embedded package contents. The first constructs the graph and computes vertex-to-edge distance by shortest-path BFS and bitwise unresolved edge-pair masks. The second uses the incidence formulas without BFS, builds the geometric candidates, independently computes all legal replacements and diameters, and checks the eight-cycle correspondence. Their precise terminal outputs are provided in the companion `.out` files. All assertions passed. The certificate is a complete finite enumeration of one specified fourteen-vertex graph; no assertion of an all-order theorem for other projective planes is made.

## Relationship to prior work

Kelenc, Tratnik, and Yero introduced the vertex-to-edge metric and studied edge-metric generators for general graphs and several graph families. Their preprint of January 31, 2016 is the foundational source for the definition; its examined sections establish general principles and formulas for paths, cycles, trees, complete bipartite graphs, grids, wheels, and hypercubes, but do not state the present Heawood classification or reconfiguration graphs. Bartoli, Kiss, Marcugini, and Pambianco study **vertex**-resolving sets of projective-space incidence graphs; distinguishing graph vertices is not the same as distinguishing its edges, and their bounds do not determine the 168 bases or the two exchange graphs here. Related existing calculations of edge metric bases for crown and half graphs concern different graph families and do not imply this Fano-plane result.

## Limitations

The theorem is finite, specific to the order-two projective plane, and does not compute edge-metric bases for arbitrary projective planes. The geometric description is a complete classification **for this graph only**. Exhaustive computational steps have two independent Python implementations and exact transparent domains, but they have not received independent scholarly audit. Literature comparisons did not find a stronger prior claim, yet unindexed historical calculations and alternative terminology remain possible priority risks. The result should not be represented as independently validated or as proof that no earlier equivalent theorem exists.

## References

1. A. Kelenc, N. Tratnik, and I. G. Yero, “Uniquely identifying the edges of a graph: the edge metric dimension,” arXiv:1602.00291v1 (January 31, 2016), https://arxiv.org/abs/1602.00291.
2. D. Bartoli, G. Kiss, S. Marcugini, and F. Pambianco, “On resolving sets in the point-line incidence graph of PG(n,q),” *Ars Mathematica Contemporanea* 19 (2020), 231–247, https://doi.org/10.26493/1855-3974.2125.7b0.
3. Heawood graph, Wolfram MathWorld, https://mathworld.wolfram.com/HeawoodGraph.html (graph identity and geometric background, not an edge-metric-base census).

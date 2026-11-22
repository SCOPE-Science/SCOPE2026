# The 171 minimum three-edge bondage sets of the Pappus graph

## Finding
Let \(G\) be the 18-vertex Pappus graph, realized as the Levi graph of the nine-point configuration defined below. Its ordinary domination number is \(\gamma(G)=5\), with exactly 18 minimum dominating sets. Its ordinary bondage number is
\[
b(G)=3.
\]
Exactly 171 of the \(\binom{27}{3}=2925\) three-edge subsets increase the domination number, and each increases it to six. Under the full automorphism group, these 171 minimum bondage sets form four orbits of sizes
\[
9,\quad18,\quad36,\quad108.
\]
The 18-set orbit consists of all complete three-edge vertex stars. Every other minimum bondage set is a matching of three pairwise disjoint edges: there are 153 such non-isolating failure sets, split into orbits of sizes 9, 36 and 108. Representatives of those three orbits have induced six-endpoint subgraphs \(3K_2\), \(C_6\) and \(P_6\), respectively. Endpoint-shape alone does not characterize the path and induced-matching orbits; the representatives and full automorphism-orbit test below give the exact classification.

## Assumptions and scope
All graphs are finite, undirected and simple. Write \(\mathbb F_3=\{0,1,2\}\), with arithmetic modulo three. Define the nine points \(P_{x,y}\) for \(x,y\in\mathbb F_3\) and the nine lines \(L_{d,c}\) for \(d,c\in\mathbb F_3\), where incidence is \(x=c\) for \(d=0\), \(y=c\) for \(d=1\), and \(x+y=c\) for \(d=2\). Vertices are points and lines; incidence gives the 27 graph edges. This graph is isomorphic to the standard Pappus graph, checked against the independently constructed LCF model and the standard graph database generator.

A vertex subset \(S\) dominates \(G\) when every vertex lies in \(S\) or has a neighbor in \(S\). Its minimum size is \(\gamma(G)\). For \(F\subseteq E(G)\), \(G-F\) keeps every vertex but deletes the edges of \(F\). Define the ordinary bondage number \(b(G)=\min\{|F|:\gamma(G-F)>\gamma(G)\}\). A minimum bondage set has size \(b(G)\). No restriction excluding isolated vertices is imposed on edge-deleted graphs.

For numerical orbit representatives, index points by \(i=3x+y\in\{0,\dots,8\}\), and index lines by \(9+j\), where \(j=3d+c\in\{0,\dots,8\}\). The following sets are lists of unordered vertex-pair edges:

| Orbit size | Representative three-edge deletion | Six-endpoint induced type |
|---:|---|---|
| 9 | \((0,9),(4,10),(8,11)\) | \(3K_2\) |
| 18 | \((0,9),(0,12),(0,15)\) | vertex star, four endpoint vertices |
| 36 | \((0,9),(1,13),(7,15)\) | \(C_6\) |
| 108 | \((0,9),(1,13),(4,10)\) | \(P_6\) |

## Proof
**Minimum domination.** The graph is cubic on 18 vertices, so any four closed neighborhoods cover at most 16 vertices. Hence \(\gamma(G)\ge5\). If a five-vertex dominating set contains \(p\) points and \(\ell\) lines, then \(p+\ell=5\), and domination of the two shores requires \(p+3\ell\ge9\) and \(\ell+3p\ge9\). Thus \((p,\ell)=(3,2)\) or \((2,3)\).

In the first case the two chosen lines must be disjoint: intersecting lines cover five points, leaving four uncovered point vertices but only three selected point vertices. The chosen lines are therefore parallel; their complement in the point shore is the three points of the third line of that class, which must all be selected. Every resulting set dominates, since the three point vertices collectively meet every line outside that parallel class. This yields exactly nine minimum sets, indexed by the omitted line of the three allowed parallel classes.

In the second case the two selected points must lie on no common allowed line: otherwise together they meet at most five lines and, even with three selected line vertices, fail to cover all nine line vertices. Conversely there are exactly nine unordered point pairs on no allowed line (out of 36 point pairs, 27 lie on one of the nine three-point lines). For any such pair, its six incident lines are distinct, so the three other lines must all be selected. Those three lines meet at the third point on the missing-direction line through the chosen pair and cover exactly the other seven points. Thus all nine resulting five-sets dominate. We have proved \(\gamma(G)=5\) with exactly 18 specified minimizers.

**Deletion criterion.** For any set \(F\) of edges and any one of the 18 minimum dominating sets \(S\), \(S\) fails to dominate in \(G-F\) if and only if some vertex \(v\notin S\) has *all* its edges to \(S\) contained in \(F\). In particular, because deleting edges cannot lower domination number, \(F\) is a bondage set exactly when this criterion holds for each of the 18 sets. This is a finite logical equivalence, not a statistical test.

**Exhaustive finite step.** The standard-library portion of `verify_structural.py` constructs the graph from the displayed incidence equations; enumerates exactly the 18 five-vertex dominators; checks the criterion for every one of the 2925 three-edge subsets; and directly verifies survival of a minimum dominating set under all \(\binom{27}{2}=351\) two-edge subsets. It obtains 171 destructive triples, including precisely 18 edge stars and 153 pairwise vertex-disjoint triples. Since no edge pair is destructive, the bondage number is at least three; since all vertex stars of size three are destructive, it is at most three.

Independently, `verify_direct.cpp` constructs the same graph via the conventional 18-cycle LCF jumps \([5,7,-7,7,-7,-5]^3\), enumerates all \(\binom{18}{5}=8568\) five-vertex candidates, and rechecks domination directly in every edge-deleted graph for subsets of one, two, or three edges, without using the failure-criterion formula. Its counts agree: 18 minimum sets, zero destructive one- or two-edge sets, 171 destructive triples, 18 stars and 153 three-edge matchings. As each two-edge proper subset of a destructive triple still admits a five-vertex dominator, deleting the final edge can increase the minimum by at most one: take a surviving dominator after the first two deletions and add the endpoint of the final deleted edge. Thus every destructive triple has resulting domination number exactly six.

**Orbit classification.** The `verify_structural.py` graph-isomorphism audit checks agreement with the independently implemented standard Pappus graph, enumerates all 216 automorphisms, applies every automorphism to each remaining destructive triple, and verifies the disjoint orbit sizes \(9,18,36,108\) with the four representatives above. The orbits exhaust all 171 destructive triples, so this is a complete classification rather than a symmetry sample.

## Verification
Run from the directory containing the two source files:

```sh
c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
./verify_direct
python verify_structural.py
```

The Python orbit audit requires `networkx` (tested with version 3.6.1); its domination and bondage enumeration uses the standard library only. The C++17 program has no external dependencies. Both were executed on the exact packaged sources and returned the expected counts. The core finite ranges are 8568 vertex five-subsets, 351 edge pairs and 2925 edge triples, not a bounded partial search. The orbit test traverses the full 216-member automorphism group rather than assuming a transitivity result. The two graph constructions were checked for isomorphism, so their agreement does not depend on matching vertex labels.

## Relationship to prior work
The ordinary bondage parameter and general edge-deletion methodology are classical, as reviewed by Xu (2013). The value \(\gamma(G)=5\) is also already exhibited for the Pappus graph in the Sage graph documentation, and is not asserted as a new parameter. Kutnar and Marušič classify cubic symmetric graphs of girth six, a graph-structural result not implying the present edge-failure census. Prior published computations on the truncated-octahedral graph concern a different, 24-vertex graph and its five-edge bondage sets, while prior Pappus semitotal-domination studies impose a different domination requirement and do not address ordinary-edge sabotage.

The proposed new contribution is the *complete* minimum bondage-set classification of the Pappus graph, including all 153 non-isolating three-edge matching obstructions and the four orbit sizes. The primary-text comparisons and remaining priority risks are itemized in `AUDIT.json` and `REVIEW.md`.

## Limitations
This is an exact finite theorem for the single 18-vertex Pappus graph, not an all-order assertion about affine-plane Levi graphs or arbitrary cubic symmetric graphs. The sharp counts and orbit decomposition rely on transparent, independently replayed exhaustive finite programs; a purely conceptual count of the 153 non-star configurations is not supplied. The structural 18-minimizer lemma is proved without enumeration. The literature comparison is best-knowledge, not a proof that no unindexed historical classification exists. No independent scholarly audit has been performed.

## References
1. Jun-Ming Xu, *On Bondage Numbers of Graphs: A Survey with Some Comments*, International Journal of Combinatorics, first published 2013-05-13, https://doi.org/10.1155/2013/595210.
2. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html.
3. Sage Graph Theory Reference Manual, example `PappusGraph` with ordinary domination number 5, https://docs.huihoo.com/sagemath/8/html/en/reference/graphs/sage/graphs/generic_graph.html.
4. K. Kutnar and D. Marušič, *A complete classification of cubic symmetric graphs of girth 6*, J. Combin. Theory Ser. B 99 (2009), 162--184, https://doi.org/10.1016/j.jctb.2008.06.001.

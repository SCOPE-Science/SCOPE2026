# Exact spanning-tree shattering complex of the Petersen graph

## Finding

Let \(P=KG(5,2)\) be the Petersen graph, whose ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\) and whose edges join disjoint pairs. Let \(\mathcal T(P)\) be the family of all spanning-tree edge sets. Queries ask whether a named edge belongs to an unknown tree. A support \(S\subseteq E(P)\) is shattered if every \(0/1\) assignment on its edges is realized by some tree. Write \(\Phi_P(z)=\sum_s f_s z^s\), where \(f_s\) counts shattered supports containing exactly \(s\) edges.

**Theorem.** The complete shattering polynomial is
\[
\boxed{\Phi_P(z)=1+15z+105z^2+445z^3+1230z^4+2160z^5+1930z^6.}
\]
In particular the VC dimension is six, and the shattering simplicial complex is **pure of dimension five**, with exactly \(1930\) facets. Under the natural full automorphism group \(\operatorname{Aut}(P)\cong S_5\), these facets form exactly **nineteen orbits**: one of size \(30\), one of size \(40\), three of size \(60\) and fourteen of size \(120\). The complex is **not a matroid independence complex**, despite purity.

Of the \(2000\) six-edge complements of spanning trees, precisely \(70\) fail shattering: **ten six-cycles** and **sixty sets consisting of a five-cycle plus one edge**. The remaining \(1930\) are exactly the facets. The finite numbers concern labeled edge subsets of the fixed Petersen graph, not graph-isomorphism classes.

## Assumptions and scope

The graph is undirected, finite, simple, and fixed as \(KG(5,2)\). A graph on the full vertex set is deemed connected even if some selected edges omit vertices, and a selected edge set is called a forest when it contains no cycle, including isolated vertices. A shattered support is an **edge-query support**, not a vertex-query support. A tree has nine edges; there are fifteen possible query coordinates. The empty support is shattered.

For exact reproducibility, order the graph vertices by lexicographic order on two-subsets, and order the fifteen edges lexicographically by the pairs of vertex indices. The resulting edge list (zero-based) is

```
0:(0,7), 1:(0,8), 2:(0,9), 3:(1,5), 4:(1,6),
5:(1,9), 6:(2,4), 7:(2,6), 8:(2,8), 9:(3,4),
10:(3,5), 11:(3,7), 12:(4,9), 13:(5,8), 14:(6,7).
```

A support bitmask \(b\) means precisely that edge \(j\) is selected when its \(j\)-th bit is one. The automorphisms come from permuting the five symbols of the two-subset labels.

## Proof

**1. Universal support criterion (background, not a new lemma).** For any finite connected graph \(G\), an edge set \(S\) is shattered by its spanning-tree incidence concepts if and only if (i) \(S\) is acyclic, and (ii) \(G-S\) is connected. The all-positive trace forces (i); the all-negative trace forces (ii). Conversely, given any desired positive subset \(A\subseteq S\), the forest \(A\) can be extended to a spanning tree of the connected graph \(G-(S\setminus A)\), because that graph contains \(G-S\). This tree meets \(S\) exactly in \(A\), establishing every possible trace. Equivalently the shattering complex is the intersection of graphic and cographic independence complexes. This is the known basis-concept criterion specialized to graphic matroids.

**2. Exhaustive finite certificate for the face polynomial and purity.** Construct the ten labeled two-subsets and their fifteen disjointness edges exactly as in the assumptions. For every integer \(b\) from \(0\) to \(2^{15}-1\), use union-find on the selected edges to decide if they form a forest, and independently on the omitted edges to decide connectivity. Count accepted masks by popcount. The seven nonzero coefficients are exactly \((1,15,105,445,1230,2160,1930)\); no mask with seven or more selected edges satisfies the criterion. To determine facets, test for each accepted mask every single-edge extension. Precisely the \(1930\) accepted six-edge masks have no admissible extension. All accepted masks of size at most five have at least one admissible extension. This is exhaustive over exactly \(32768\) masks, with no sampling or unbounded search. The complete standard-library implementation is `verify/check_direct.py`.

An **independent second certificate**, `verify/check_traces.cpp`, does not rely on the forest/complement predicate to count shattered masks. It enumerates every possible nine-edge set among the fifteen, tests which are trees, finds exactly \(2000\) of them, and for each of the \(32768\) supports computes the number of distinct actual Boolean traces among all \(2000\) trees. It accepts a support exactly when this number equals \(2^{|S|}\). It reproduces all polynomial coefficients and the facet/purity assertion. These two finite algorithms establish the displayed exact finite results by complete coverage of their specified finite domains; they are not experiments purporting to prove an unrestricted infinite statement.

**3. Explaining the seventy excluded coforest bases.** A six-edge set \(S\) has connected complement if and only if its nine omitted edges form a spanning tree: connected on ten vertices with nine edges is automatically a tree. The Petersen graph has \(2000\) spanning trees, a standard consequence of the Matrix-Tree Theorem and Laplacian spectrum \(0,2^5,5^4\): \(2^5 5^4/10=2000\). Hence there are \(2000\) six-edge supports passing the complement-connectivity test. A six-edge selected set fails the forest test only if it contains a cycle, and Petersen's girth five means that cycle has length five or six.

There are twelve five-cycles and ten six-cycles, as can be counted by a direct finite simple-cycle traversal or by the natural \(S_5\) action. For any five-cycle \(C\), its five outside vertices also induce a five-cycle, with the remaining five edges forming a perfect matching between the cycles. Consequently \(P-E(C)\) is a unicyclic graph: the opposite five-cycle with five pendant edges. Exactly the five edges of the opposite cycle may be deleted while retaining a spanning tree. Thus every \(C\) contributes precisely five six-edge sets of type five-cycle plus an extra edge, for a total of \(12\cdot5=60\). Each of the ten six-cycles has connected complement (verified on one symmetry representative and all ten by the finite certificate), contributing ten further exclusions. No six-edge set can contain two distinct cycles here: two simple cycles of length at least five in a graph with at most six edges would force a forbidden short cycle or require more than six edges. The exclusion types are disjoint, giving \(2000-60-10=1930\) shattered six-edge supports, independently explaining the top coefficient.

**4. Exact facet orbits.** The group of all \(120\) permutations of the five vertex labels acts on all fifteen edge indices and hence on six-element supports. For each unassigned facet choose the least integer mask and apply all \(120\) permutations, obtaining its complete orbit. The extracted masks form a partition of the \(1930\) facets into exactly nineteen orbits. Their representative-mask/size pairs are

```
4501:30, 235:40,
222:60, 245:60, 669:60,
219:120, 238:120, 246:120, 667:120, 683:120,
685:120, 686:120, 691:120, 693:120, 694:120,
746:120, 754:120, 4330:120, 4491:120.
```

The list is in orbit-size order, not in increasing representative-mask order. Summing yields \(30+40+3\cdot60+14\cdot120=1930\). Both the automorphism action and the orbit partition are explicitly generated by the direct checker, not inferred from divisibility alone.

**5. A basis-exchange obstruction.** In the same edge encoding, \(A=238\) and \(B=8283\) are shattered six-element supports. Edge index \(7\) is in \(A\setminus B\), and \(B\setminus A\) consists of edge indices \(0,4,13\). The three candidate replacements are masks \(111,126,8302\). Their failures can be checked directly: masks \(111\) and \(126\) each have a **disconnected edge complement** (two components), while mask \(8302\) has a **selected cycle**. Therefore no basis exchange is possible for this \(A,B,7\), contradicting the matroid basis-exchange axiom. This demonstrates that purity does not entail matroidality in this natural shattering example.

## Verification

Run `python3 verify/check_direct.py` and, independently, compile/run `verify/check_traces.cpp` with `c++ -std=c++17 -O2 -o /tmp/petersen_check verify/check_traces.cpp && /tmp/petersen_check`. The Python program prints `PETERSEN_DIRECT_PASS faces=5886 facets=1930 facet_orbits=19 bad_cotrees=70`; the C++ program prints `PETERSEN_TRACES_PASS trees=2000 faces=5886 facets=1930`. Both were run successfully from the packaged source files. The Python computation verifies all integer support masks, facet extensions, 120 natural graph automorphisms, orbit sizes and the explicit failed exchange; the C++ algorithm independently uses the actual trace definition. Both are deterministic and use no external datasets or third-party libraries.

## Relationship to prior work

Benediktsson, Macpherson and Adler (first public 2020-07-31) develop model-theoretic and graph-theoretic VC dimension for Johnson and Hamming graph **neighborhoods**. Their paper motivates studying complete shattering information on highly symmetric finite graphs but does not discuss the Petersen spanning-tree incidence concept class. Kobayashi, Kurita and Wasa (first public 2023-07-18) study **enumeration of maximal common independent sets in two matroids** and algorithms for the general setting; their full arXiv exposition gives neither the Petersen complete face vector nor the orbit/exclusion census. The general identification of basis-concept shattering with common graphic/cographic independence and the 2000 spanning-tree count are expressly prior knowledge.

For specific neighboring claims, the Petersen **pivot-exchange** census concerns distances and symmetry in the tree-reconfiguration graph, rather than traces of edge queries. The complete shattering polynomial for \(K_{3,n}\) concerns another graphic-matroid family; neither its parameter formula nor its matroidality obstruction determines the Petersen coefficients. The existing Petersen **induced-forest** homology results concern subsets of graph vertices, not graph-edge sets whose complements are connected. These distinctions concern actual compared mathematical statements, not just titles. An unindexed earlier table for common graphic/cographic independent sets remains a genuine originality risk.

## Limitations

This is a complete finite result for the single canonical Petersen graph, not an asymptotic formula for all Kneser graphs, a new algorithm for matroid intersection, or a general theorem on all cubic graphs. Its value is the whole face vector, exact sixty-plus-ten obstruction split, purity without matroidality, and full symmetry-orbit census; the universal forest/complement-connectedness lemma is not new. Enumeration is exhaustive for the specified graph, but the source-code certificates have not received independent external validation. The literature search does not certify historical priority against all unpublished computations or indexing omissions.

## References

1. B. G. Benediktsson, D. Macpherson and I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, first posted 2020-07-31, arXiv:2007.16042; https://arxiv.org/abs/2007.16042 .
2. Y. Kobayashi, K. Kurita and K. Wasa, *Polynomial-Delay Enumeration of Large Maximal Common Independent Sets in Two Matroids and Beyond*, first posted 2023-07-18, arXiv:2307.08948; earlier conference version MFCS 2023 DOI 10.4230/LIPIcs.MFCS.2023.58; https://arxiv.org/abs/2307.08948 .
3. *Exact pivot-exchange geometry of the Petersen spanning-tree graph*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-pivot-exchange-geometry-of-the-petersen-spanning-tree-grap--a0f4ecd55781 .
4. *Matroid basis concepts have equal static and adaptive shattering dimensions*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-matroid-basis-concepts-have-equal-static-and-adaptive-shattering--dd07b0e752eb .
5. *Exact shattering polynomial and a matroid boundary for spanning trees of \(K_{3,n}\)*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-shattering-polynomial-and-a-matroid-boundary-for-spanning--0c288e04bf53 .

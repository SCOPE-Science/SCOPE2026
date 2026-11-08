# Unique first color-refinement collision among connected bicyclic graphs

## Finding
Let \(\mathcal B_n\) be the set of isomorphism classes of finite simple connected graphs on \(n\) vertices and \(n+1\) edges (cycle rank two). Two graphs are \(C^2\)-equivalent if they satisfy the same first-order sentences using at most two variables and counting quantifiers, with no bound on quantifier rank. **Theorem.** For \(n\le5\), any two \(C^2\)-equivalent members of \(\mathcal B_n\) are isomorphic. There are exactly \(19\) isomorphism classes in \(\mathcal B_6\), distributed among \(18\) \(C^2\)-equivalence classes. Its unique nonsingleton class has exactly two members: two triangles joined by a bridge, and two four-cycles sharing an edge. For each \(n\ge6\), there is a nonisomorphic \(C^2\)-equivalent pair of graphs in \(\mathcal B_n\).

## Assumptions and scope
All graphs are finite, simple, undirected and connected, with no vertex or edge labels; equivalence is within the connected cycle-rank-two class, not identification among all finite graphs. Cycle rank is \(|E|-|V|+1\). The finite minimality/uniqueness statement concerns \(n\le6\), while the existence construction covers every \(n\ge6\).

## Proof
Define the six core vertices \(0,1,2,3,4,5\). Both graphs contain \(02,03,14,15\). In \(G_t\) also include \(23,45\); in \(H_t\) include \(24,35\). Add a path between \(0\) and \(1\) with \(t\) new internal vertices, where \(t\ge0\). Then both connected graphs have \(6+t\) vertices and \(7+t\) edges, and thus cycle rank two. Graph \(G_t\) has exactly two triangles, \(023\) and \(145\), whereas \(H_t\) has none; they cannot be isomorphic.

To show equivalence, run simultaneous color refinement from the uniform coloring. In each graph the four satellite vertices \(2,3,4,5\) always have the same color: each has one neighbor among satellites and one neighbor among the two path endpoints, and reversal of the linking path swaps the endpoints. At any round the two endpoints share a color, the satellites share a color, and each corresponding internal path position has the same color in \(G_t\) and \(H_t\). The neighbor-color multiset for every such vertex is the same in both graphs; induction establishes this for every round. Hence all global color histograms agree at every round, including stabilization. By the Immerman–Lander correspondence, the graphs are \(C^2\)-equivalent.

For minimality and uniqueness, enumerate all simple graphs on \(n=4,5,6\) vertices having precisely \(n+1\) edges: choose exactly \(n+1\) edges from the \(\binom n2\) possible unordered pairs, retaining only connected graphs. For each \(n\), perform \(n\) rounds of simultaneous color refinement, using canonical per-round vertex signatures consisting of the previous color and the sorted multiset of neighbor colors; share one signature dictionary across all graphs at that order. Such a partition must stabilize within \(n\) rounds. Group graphs by final multiset of globally consistent colors. Within each group use exhaustive adjacency-preserving backtracking to remove isomorphic duplicates; candidates are assigned by degree-compatible bijections and every mapped pair's adjacency is checked. The complete counts of nonisomorphic connected bicyclic types and refinement classes are respectively \((1,1)\) at \(n=4\), \((5,5)\) at \(n=5\), and \((19,18)\) at \(n=6\). There is exactly one nonsingleton class at order six and its members have triangle counts \(2\) and \(0\). The displayed \(G_0,H_0\) lie in that class, so the classification is exact. This is an exhaustive finite computation, not a sampling inference.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. The enumerator tests every labelled simple graph with \(n+1\) edges for \(4\le n\le6\), and removes isomorphic copies via exact backtracking; no external graph catalogue is used. The output must include `CENSUS_OK` and `FAMILY_OK t=0..20`. The finite family test corroborates, but does not prove, the all-order symbolic argument above.

## Relationship to prior work
Color refinement, fractional isomorphism and \(C^2\)-equivalence are related as in Arvind–Köbler–Rattan–Verbitsky (2015), recalling Immerman–Lander. The six-vertex pair itself is **not new**: Bodnar et al. (NeurIPS 2021, arXiv:2106.12575), Figure 8, exhibit exactly this pair, and Zhu (arXiv:2610.22909), Section 4.2, uses it again. Neither of those inspected presentations supplies the complete nineteen-type enumeration or proves the uniqueness of the first nonsingleton equivalence class. The narrowly claimed contribution is this exact first-order classification and the complete order-existence spectrum, not discovery of the pair.

## Limitations
This theorem does not classify larger bicyclic \(C^2\)-classes, determine all graph orders' numbers of distinct classes, or imply identification among arbitrary graphs. Novelty is conditional on the bounded literature and internal-record searches; a specialized published enumeration could preempt the uniqueness assertion. No independent verification has been performed.

## References
- Arvind, Köbler, Rattan, and Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first submitted 2015-02-04).
- Bodnar et al., *Weisfeiler and Lehman Go Cellular: CW Networks*, NeurIPS 2021, arXiv:2106.12575, Appendix Figure 8.
- Zhu, *Sharp Bounds for Common Spanning Forests under Color Refinement*, arXiv:2610.22909 (2026), Section 4.2.
- Verbitsky and Zhukovskii, *Canonical Labeling of Sparse Random Graphs*, STACS 2025, on unicyclic identification.

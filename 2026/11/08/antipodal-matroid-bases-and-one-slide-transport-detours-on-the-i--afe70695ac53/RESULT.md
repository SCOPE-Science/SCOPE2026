# Antipodal matroid bases and one-slide transport detours on the icosahedron

## Finding

Let \(I\) be the ordinary icosahedral graph. A *metric basis* of \(I\) is a minimum-size vertex set whose vectors of graph distances distinguish all twelve vertices. Two metric bases are *slide adjacent* if one is obtained from the other by moving one selected vertex to an unselected neighbor in \(I\), with the resulting three-set still a metric basis. Let \(R\) denote this token-slide reconfiguration graph.

**The exact classification** is as follows.

1. The metric dimension of \(I\) is \(3\) (known previously). Its **complete basis family** consists exactly of the triples taking one vertex from each of three distinct antipodal vertex pairs. There are \(\binom{6}{3}2^3=160\) such bases. These triples form the bases of the rank-\(3\) truncation of the partition matroid with six blocks of size two.
2. The induced token-slide graph \(R\) has \(160\) vertices, is connected and \(9\)-regular, and has \(720\) edges. Its radius is \(4\) and its diameter is \(6\). Exactly \(20\) configurations have eccentricity \(4\), \(120\) have eccentricity \(5\), and \(20\) have eccentricity \(6\). These correspond respectively to the three pairwise landmark-distance patterns \((2,2,2)\), mixed \((1,1,2)\) or \((1,2,2)\), and \((1,1,1)\).
3. For any two distinct metric bases \(S,T\), define their unconstrained three-token transport cost
   \[
   W(S,T)=\min_{\sigma:S\overset{\sim}\longrightarrow T}\sum_{s\in S}d_I(s,\sigma(s)).
   \]
   The **exact slide distance satisfies**
   \[
   \boxed{d_R(S,T)\in\{W(S,T),\,W(S,T)+1\}.}
   \]
   Among all \(\binom{160}{2}=12720\) unordered distinct pairs, precisely \(12110\) attain \(W\), while exactly \(610\) incur the additional slide. Thus preserving the metric-basis property creates a sharp and limited geodesic obstruction. The numbers of unordered pairs at distances \(1,2,3,4,5,6\) are, respectively, \(720,2730,4960,3490,810,10\).
4. The unrestricted *token-jump* graph on the same \(160\) bases—where a selected vertex can be replaced by any unselected vertex, provided the result remains a metric basis—is \(21\)-regular with \(1680\) edges, and has diameter and radius \(3\). Its distance is the classical partition-matroid basis-exchange metric \(\,d_J(S,T)=3-|S\cap T|\,\). The jump metric is supporting context; the adjacency-restricted graph and its detours are the central finding.

The result is an *exact finite classification*, not an infinite-family extrapolation.

## Assumptions and scope

The host graph is undirected, simple, unweighted and finite, with ordinary shortest-path distance. Tokens are indistinguishable and cannot occupy the same vertex. Every intermediate state in a legal reconfiguration remains a minimum resolving set.

For an entirely reproducible labeled presentation of the icosahedron, take \(V(I)=\{0,\ldots,11\}\) and neighbors:

- `0`: 1, 5, 7, 8, 11
- `1`: 0, 2, 5, 6, 8
- `2`: 1, 3, 6, 8, 9
- `3`: 2, 4, 6, 9, 10
- `4`: 3, 5, 6, 10, 11
- `5`: 0, 1, 4, 6, 11
- `6`: 1, 2, 3, 4, 5
- `7`: 0, 8, 9, 10, 11
- `8`: 0, 1, 2, 7, 9
- `9`: 2, 3, 7, 8, 10
- `10`: 3, 4, 7, 9, 11
- `11`: 0, 4, 5, 7, 10

These lists determine the \(30\) edges without requiring a graph-library package. The six antipodal pairs (at graph distance \(3\)) are \(\{0,3\},\{1,10\},\{2,11\},\{4,8\},\{5,9\},\{6,7\}\). All figures above refer to this graph or an isomorphic copy, and are invariant under relabeling.

## Proof

**Step 1: exact finite neighborhood and distance certificates.**
Breadth-first searches from each of the twelve vertices of the stated adjacency list generate the full \(12\times12\) integer distance matrix \(d_I\). Exhausting all \(\binom{12}{2}=66\) unordered vertex pairs gives the following elementary distance facts:

- Exactly \(30\) pairs have distance \(1\), \(30\) have distance \(2\), and \(6\) have distance \(3\). Every vertex has a unique antipode at distance \(3\), and \(d_I(x,\bar a)=3-d_I(x,a)\) for all \(x,a\).
- For every pair \(u\ne v\) at distance \(1\) or \(2\), the set \(E(u,v)=\{x:d_I(x,u)=d_I(x,v)\}\) consists of exactly four vertices, comprising two complete antipodal pairs. For a pair at distance \(3\), \(E(u,v)=\varnothing\).
- Any pair of selected landmarks has fewer than twelve distinct two-coordinate distance signatures: there are exactly \(8\) signatures if their mutual distance is \(1\) or \(2\), and \(4\) if it is \(3\).

Each statement is a complete check of explicitly bounded integer arrays, reproduced by `check_python.py`; the independent `check_cpp.cpp` reconstructs the distance matrix and the complete three-landmark resolving condition. No probabilistic sampling is involved.

**Step 2: all metric bases.**
The last bullet shows no set of at most two landmarks can resolve \(I\). If a three-set contains an antipodal pair \(a,\bar a\), then the corresponding two distance coordinates are redundant, since \(d_I(x,\bar a)=3-d_I(x,a)\). The remaining third coordinate cannot rescue a two-landmark non-resolving signature, so this three-set does not resolve \(I\).

Conversely, take three landmarks from three different antipodal pairs. If two vertices \(u,v\) had identical distances to all three landmarks, those landmarks would all lie in \(E(u,v)\). This contradicts the second bullet: \(E(u,v)\) is the union of at most two antipodal pairs. Thus every such triple is resolving, hence is minimum, and the precise family and its count follow. The matroid description follows directly from the independence constraint of at most one element per antipodal block and the rank-\(3\) truncation.

**Step 3: legal moves and regularity.**
To replace a chosen landmark \(a\), keep the other two chosen vertices \(b,c\). Among the five neighbors of \(a\), exactly one belongs to the antipodal pair of \(b\), and exactly one to that of \(c\), because the two vertices of any antipodal pair have complementary distances summing to \(3\) from \(a\). These two neighbors would violate the distinct-block condition; the remaining three are legal. Consequently, each of three tokens has three legal slides, for degree \(9\) and \(\frac{160\cdot9}{2}=720\) edges.

For unrestricted jumps, a token has nine unoccupied destinations, two of which are the antipodes of the *other* selected landmarks and hence forbidden; the other seven are legal. This gives degree \(3\cdot7=21\) and \(\frac{160\cdot21}{2}=1680\) edges. The matroid basis-exchange property gives jump distance \(3-|S\cap T|\).

**Step 4: exhaustive finite graph metric.**
The codes `check_python.py` and `check_cpp.cpp` independently enumerate all \(\binom{12}{3}=220\) three-sets, test the resolving condition, generate the complete \(160\)-state slide and jump graphs, and run breadth-first shortest-path search from every state. The resulting *exact integer arrays*, checked by assertions rather than inferred from printed logs, yield the claimed connectivity, radii, diameters, eccentricity classes, and pair-distance histogram.

For each of the \(12720\) distinct unordered pairs of bases, both codes compute \(W(S,T)\) by checking all six bijections between the two three-sets and compare it with the independently computed slide distance. The pairwise exhaustive comparison yields the partition into \(12110\) equal-cost cases and \(610\) cases needing one more slide, and verifies that no pair requires a larger excess. As a separate check, `check_python.py` constructs the unrestricted \(3\)-token graph on *all* \(220\) three-sets and verifies that its shortest-path distances between bases agree exactly with \(W\). Each permitted slide in \(R\) is also such an unconstrained slide, so \(W\) is a mathematically valid lower bound; this establishes the claimed meaning of the one-step excess.

The computations are exhaustive finite proofs: they terminate after fixed loops over \(12\) original vertices, \(220\) possible triples, \(160\) valid states, \(12720\) pairs and the six bijections per pair. They do not use floating-point decisions, heuristics, randomized testing, or incomplete search. The source programs are embedded in this package.

## Verification

From the directory containing the extracted package files, execute:

```sh
python3 -S check_python.py
g++ -std=c++17 -O2 -Wall -Wextra check_cpp.cpp -o check_cpp
./check_cpp
```

Both programs use only the literal \(30\)-edge icosahedral graph above and integer graph algorithms. They independently generate bases and transformations; the Python and C++ code follow different state-construction strategies (move enumeration versus pairwise comparison of all bases). The first additionally verifies two-landmark obstruction and compares distances in the unconstrained \(220\)-state token graph. Their successful complete outputs are supplied in `check_python.out` and `check_cpp.out`. The full finite enumerations are rerunnable and need no external downloaded data.

## Relationship to prior work

The metric dimension \(3\) of the icosahedral graph was already reported in Bailey's 2013 computational catalog; it is not a new conclusion. Bailey's other 2013 work explicitly examines the relation of resolving sets in antipodal Taylor graphs to their folded/descendant graphs. The antipodal-coordinate relation above builds on that mathematical context, rather than claiming antipodal reduction as an invention. Boutin's 2008 study describes the exchange property for resolving sets and its connection with matroids, but not the specific partition-matroid basis family or its *adjacency-restricted* slide metric for the icosahedron. Fabila-Monroy and coauthors' 2009 *Token Graphs* studies all \(k\)-subsets with moves along graph edges: \(R\) is a proper induced \(160\)-state subgraph of their \(220\)-state three-token graph, and distances in induced subgraphs are not determined by the unrestricted graph's diameter or connectivity theorems.

A university faculty webpage also lists a 2026 master's thesis titled *Reconfigurations of Metric Bases*; its full text was not located in bounded searches, so its coverage remains an explicit historical-priority risk. An indexed university project description discusses the token-slide and token-jump problem for other graph families but does not mention the icosahedron.

These distinctions were checked by reading the relevant original arXiv full texts, including Bailey's icosahedral metric-dimension table, the Taylor-graph theorem and its proof, Boutin's resolving-set exchange setup, and the token-graph definition and results. Searching equivalent forms in terms of basis exchanges, metric generators, antipodal selection and token transportation found no covering result. The claim is subject to normal historical-priority uncertainty.

## Limitations

This theorem concerns only the labeled icosahedral graph (or an isomorphic graph), and only minimum resolving sets. It does not assert analogous formulas for larger graph families, all resolving sets, weighted moves, multiple simultaneous moves, or arbitrary other graph bases. All pairwise distance and detour counts are established by self-contained exact exhaustive computation with two separately implemented checkers, not by a closed-form symbolic formula valid for other graphs. There is no independent external scholarly audit of this package.

## References

1. D. L. Boutin, *Determining sets, resolving sets, and the exchange property*, first public arXiv submission 2008-08-10. https://arxiv.org/abs/0808.1427
2. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, D. R. Wood, *Token Graphs*, first public arXiv submission 2009-10-25. https://arxiv.org/abs/0910.4774
3. R. F. Bailey, *On the metric dimension of imprimitive distance-regular graphs*, first public arXiv submission 2013-12-17. https://arxiv.org/abs/1312.4971
4. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, first public arXiv submission 2013-12-17. https://arxiv.org/abs/1312.4973
5. Cal Poly Pomona, faculty student-research listing (2026 thesis title) and university metric-basis-reconfiguration project description. https://www.cpp.edu/faculty/brianaf/student-research.shtml and https://www.cpp.edu/camp-reu/research_projects.shtml

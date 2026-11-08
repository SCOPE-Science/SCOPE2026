# Sharp order-eleven four-round threshold in two-variable counting logic on cographs

## Finding
Let \(G\) be a finite simple undirected **cograph**, equivalently a graph with no induced four-vertex path. Starting from the uniform vertex coloring, let \(\Pi_0(G)\) be the one-block partition and obtain \(\Pi_{i+1}(G)\) by splitting each block according to the vector of numbers of neighbors in every block of \(\Pi_i(G)\). Define \(t(G)\) as the number of **strict** splitting rounds before the partition stabilizes. A final unsuccessful stabilization test is not counted.

**Theorem.** Every cograph on at most ten vertices satisfies \(t(G)\le 3\). Exactly two nonisomorphic cographs on eleven vertices satisfy \(t(G)=4\), and they are complements of each other. One is disconnected,
\[
W=\bigl((P_3\sqcup K_1)\vee(2K_1)\bigr)\sqcup\bigl((K_2\sqcup K_1)\vee K_2\bigr),
\]
and the other, \(\overline W\), is connected. Both have the color-class-count trace \(1,3,5,6,7\), after which no further split occurs. In particular, \(\overline W\) is the unique smallest **connected** cograph requiring four strict rounds.

Here \(\sqcup\) denotes disjoint union, \(\vee\) denotes complete join, \(P_3\) is the three-vertex path, and \(K_r\) is the complete graph on \(r\) vertices. For example, \(2K_1\) denotes two isolated vertices. Both exceptional graphs contain an induced four-cycle and thus lie outside the smaller trivially-perfect graph class.

Equivalently, in the one-free-variable fragment of two-variable first-order logic **with arbitrary counting quantifiers**, no cograph of order at most ten has two vertices that first acquire distinct unary counting-logic types at quantifier rank four. At order eleven, exactly the two stated graph isomorphism classes do. This equivalence uses the standard correspondence between rank-\(i\) unary \(\mathrm C^2\)-types and round-\(i\) color refinement in an individual graph.

## Assumptions and scope
The graph language has one undirected irreflexive adjacency relation, equality, and no distinguished vertices or labels. Every graph is finite; connectedness is imposed only for the separate connected assertion. Counting quantifiers may use arbitrary fixed natural-number thresholds. Quantifier rank counts nested quantifiers, not the magnitude of a counting threshold. The theorem concerns a finite minimum-order cutoff, not the maximum number of rounds on all larger cographs.

## Proof
**1. Canonical exhaustive reduction.** Every cograph has a unique reduced cotree up to permutations of sibling subtrees. Each leaf represents a vertex, each internal node is labeled \(U\) (disjoint union) or \(J\) (complete join), each internal node has at least two children, and consecutive internal nodes along any root-to-leaf path carry opposite labels. Conversely, every such reduced cotree encodes a cograph. These are the standard cotree properties [1,3].

The verification code enumerates all reduced cotrees of each leaf count \(1\le n\le 11\) by the complete set of integer partitions of \(n\) into at least two parts. For each part size and multiplicity it chooses all multisets of reduced child cotrees of the opposite internal label (or a leaf of size one), then takes every Cartesian product of those choices. Sorting the child multiset yields one canonical representative per isomorphism class. Induction on leaf count proves both completeness and absence of duplicates. Hence an exhaustive evaluation on these cotrees proves a universal assertion for all cographs up to the stated order.

For each cotree, adjacency is reconstructed exactly: edges between distinct children occur precisely at a \(J\)-node, while no such edges occur at a \(U\)-node. One refinement method recomputes per-vertex signatures consisting of old color and all neighbor counts by old color; another independently performs equitable block splitting. Both are exact integer computations and agree on every enumerated graph. The following complete census is produced by the supplied verifier:

| Vertices | Nonisomorphic cographs | Maximum strict rounds | Number attaining maximum |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 0 | 1 |
| 2 | 2 | 0 | 2 |
| 3 | 4 | 1 | 2 |
| 4 | 10 | 1 | 6 |
| 5 | 24 | 2 | 2 |
| 6 | 66 | 2 | 10 |
| 7 | 180 | 2 | 44 |
| 8 | 522 | 3 | 2 |
| 9 | 1,532 | 3 | 10 |
| 10 | 4,624 | 3 | 46 |
| 11 | 14,136 | 4 | 2 |

Thus none of the \(4,624\) order-ten classes, nor any smaller class, requires four rounds, while exactly two of the \(14,136\) order-eleven classes do. Their canonical cotrees and graph data are embedded in `census.json`. The independently published enumeration of connected cographs [6] gives \(7,068\) at order eleven, consistent with half of the total computed count.

**2. Direct verification of the witness.** Write \(W=A\sqcup B\), with \(A=(P_3\sqcup K_1)\vee(2K_1)\) and \(B=(K_2\sqcup K_1)\vee K_2\). In \(A\), let \(p_1,p_2\) be the path ends, \(c\) its center, \(z\) the isolated vertex before the join, and \(u,v\) the independent joined pair. In \(B\), let \(a,b\) be the original adjacent pair, \(w\) the isolated vertex before the join, and \(r,s\) the adjacent joined pair.

After the first round, the degree classes are \(\{z,w\}\) of degree two, \(\{p_1,p_2,a,b\}\) of degree three, and \(\{c,u,v,r,s\}\) of degree four. At the second round, the degree-three class splits into \(\{p_1,p_2\}\) and \(\{a,b\}\), because the former sees three degree-four neighbors while the latter sees two degree-four neighbors and one degree-three neighbor. The degree-four class splits into \(\{c\}\) and \(\{u,v,r,s\}\), because only \(c\) sees no degree-two vertex. Therefore there are five classes. At the third round, \(\{u,v\}\) and \(\{r,s\}\) split, because they see distinct newly separated degree-three classes, giving six classes. At the fourth round, \(z\) and \(w\) split because the former sees \(u,v\) and the latter sees \(r,s\), giving seven classes. Each displayed final class consists of twins or a singleton and therefore cannot split further. Thus the trace is exactly \(1,3,5,6,7\), followed by stability.

**3. Complementation and connectedness.** Suppose vertices in the same current color class are compared in a refinement. For any old color class \(C\), their counts of complement-neighbors in \(C\) equal \(|C|\) minus their original neighbor counts in \(C\), with the same correction for excluding the vertex itself. Hence the refinement partition in a graph and its complement coincide at every round, inductively from the uniform partition. Thus \(t(\overline W)=4\), with the same class trace. Because \(W\) is disconnected and has at least two components, its complement is connected. The exhaustive census identifies precisely those two cotrees, related by interchanging \(U\) and \(J\), and thereby proves uniqueness in both the unrestricted and connected cases.

**4. Counting-logic interpretation.** Over a fixed finite graph, two vertices have equal rank-zero unary \(\mathrm C^2\)-types. Inductively, their rank-\(i+1\) types agree exactly when their rank-\(i\) types agree and they have the same numbers of neighbors in every rank-\(i\) type: counting formulas can test every such integer, and other counted choices (nonneighbors and equality) are determined from the fixed type-class sizes. This is exactly the color refinement recursion. The rank-four formulation therefore follows from the same census and witness trace.

## Verification
Run `python3 verify.py` with Python 3.10 or later and no external packages. The program enumerates all \(21,101\) isomorphism classes of cographs with orders from one to eleven, recomputes every partition two ways, checks the stated witness cotrees are complements, verifies the four-cycle condition, checks known total class counts, and writes `census.json`. Its final line is `VERIFY_OK 21101`. Reproduction should compare the emitted `census.json` byte-for-byte with the embedded file. This finite exhaustive verification is the proof method for the minimum-order and uniqueness assertions; it is not an extrapolation to unbounded order.

## Relationship to prior work
Corneil, Perl, and Stewart [1] establish the unique cotree representation used for exhaustive completeness. Arvind, Köbler, Rattan, and Verbitsky [2] study the expressive power and amenability of color refinement, not this class-specific iteration cutoff. Jones, Protti, and Del-Vecchio [3] give an independent complete cotree-generation method, but do not give these rank-four refinement thresholds. Kiefer and McKay [4] establish extremal iteration lengths among all graphs; Kiefer and de Mel [5] characterize long-refinement graphs with nearly maximal general-graph iteration numbers. Neither result implies the first **four-round** cutoff for the \(P_4\)-free class. A published cograph graph collection [6] lists graph classes, not the iterated logical-type profile established here.

## Limitations
No closed formula for the maximal refinement depth at arbitrary cograph order is claimed, nor is any theorem about counting-free logic, higher-dimensional Weisfeiler–Leman refinement, or graphs outside the cograph class. The finite bound and uniqueness rely on exhaustive exact enumeration whose completeness follows from canonical cotrees and whose outputs are independently recomputed by a second partition algorithm. Historical-priority comparison is bounded to the specified literature, databases, and accessible research records; an unpublished or unindexed earlier calculation could coincide with the result.

## References
1. D. G. Corneil, Y. Perl, and L. K. Stewart, *A linear recognition algorithm for cographs*, SIAM J. Comput. 14 (1985), 926–934, doi:10.1137/0214065.
2. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public posting 2015-02-04).
3. Á. A. Jones, F. Protti, and R. R. Del-Vecchio, *Cograph generation with linear delay*, arXiv:1612.05827 (2016-12-17).
4. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182 (2020-05-20).
5. S. Kiefer and T. D. de Mel, *A Classification of Long-Refinement Graphs for Colour Refinement*, arXiv:2510.20802 (2025-10-23).
6. House of Graphs, *Cographs* metadata collection, https://houseofgraphs.org/meta-directory/cographs (accessed 2026-11-04).

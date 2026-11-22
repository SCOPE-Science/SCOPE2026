# Six points are the sharp failure threshold for joint finite-space separation graphs

## Finding
For finite \(T_0\) Alexandrov spaces, the simultaneous isomorphism type of the **inseparability graph** and the **closure-meeting graph** determines the weak homotopy type at every cardinality at most five, but not at six. The same sharp statement holds if the Urysohn and functional graphs are included. Crucially, simultaneous isomorphism means a **single bijection** that preserves every named graph, not separate isomorphisms.

At six points, let \(A_2\) denote a two-point antichain, \([2]\) a two-point chain, and \(\oplus\) ordinal sum. The two posets
\[
P_0=A_2\oplus A_2\oplus A_2,\qquad P_1=A_2\oplus[2]\oplus A_2
\]
have identical graph pairs on the same underlying labeled set, although
\[
|\mathcal K(P_0)|\cong S^2,\qquad |\mathcal K(P_1)|\simeq \{\mathrm{point}\}.
\]
Here \(\mathcal K(P)\) is the order complex. In particular the two finite spaces are not weakly homotopy equivalent.

## Assumptions and scope
Use the downset Alexandrov topology of a finite poset \(P\). For distinct \(x,y\), inseparability means their smallest open neighborhoods (principal downsets) intersect, equivalently they have a common lower bound. Closure-meeting means their singleton closures (principal upsets) intersect, equivalently they have a common upper bound. Each graph is simple and loopless. A pair of graphs is isomorphic only when the same bijection on all vertices preserves both edge sets. The weak homotopy type of a finite poset agrees with the ordinary homotopy type of its geometric order complex, by the finite-space order-complex equivalence.

For finite Alexandrov spaces the Urysohn graph is the graph square of the inseparability graph, and the functional graph is the disjoint union of cliques on the connected components of the inseparability graph. Thus the two other graphs add no information beyond inseparability in the present category.

## Proof
**Six-point upper bound.** Label both posets with bottom elements \(0,1\), middle elements \(2,3\), and top elements \(4,5\). Every element of a lower level is below every element of a higher level. In \(P_0\), the middle pair is incomparable; in \(P_1\), add the relation \(2<3\). The inseparability graph of either poset is \(K_6\) minus edge \(\{0,1\}\), because that is the only pair having no common lower bound. The closure-meeting graph is \(K_6\) minus edge \(\{4,5\}\). The Urysohn and functional graphs are both \(K_6\). These identifications hold on the same six labels.

The order complex of an ordinal sum is the simplicial join of its factors' order complexes. Consequently \(\mathcal K(P_0)=S^0*S^0*S^0\), the octahedral two-sphere. For \(P_1\), the middle factor is the edge \(\Delta^1\), so \(\mathcal K(P_1)=S^0*\Delta^1*S^0\) is contractible. Their reduced integral second homology groups are therefore \(\mathbb Z\) and zero, respectively.

**Sharpness below six.** Every finite poset on \(n\) points has a linear extension. Relabel its points in extension order; its strict order relation is a subset of the upper-triangular pairs \((i,j)\), \(i<j\), and is transitively closed. Conversely every such transitively closed upper-triangular subset defines a poset. Hence enumerating all \(2^{\binom n2}\) candidate masks, discarding exactly the nontransitive masks, covers **every isomorphism type** (possibly multiple times). The standalone exact program `checks/four_graph_threshold.py` implements precisely this enumeration without external libraries.

For each retained poset, the program derives common-lower-bound and common-upper-bound graphs from its reflexive order masks, and derives the Urysohn and functional graphs from inseparability. It canonicalizes the entire four-graph tuple over **all** \(n!\) simultaneous vertex permutations. It constructs every simplex of the order complex by exhaustive pairwise comparability of a chain. For each connected component it repeatedly chooses an actual free codimension-one face of a maximal simplex and deletes that face and its unique coface until no simplex of dimension at least two survives. The code checks freeness against the **complete current face set** at every move. Thus it produces a genuine simplicial collapse to a graph, not merely a homology computation.

The exact finite counts for \(n=1,2,3,4,5\) are respectively \(1,2,7,40,357\) transitively closed orders and \(1,2,5,15,52\) simultaneous four-graph signature classes. Every order complex in those classes collapses componentwise to a graph. For each component the remaining graph gives the exact nonnegative first Betti rank \(|E|-|V|+1\). The program checks that the **sorted multiset of componentwise ranks is identical within each signature class**, with zero mismatches in all five cardinalities. A disjoint union of connected graphs is homotopy equivalent to the disjoint union of corresponding wedges of circles. The multiset therefore determines its homotopy type. By the finite-space/order-complex equivalence, the weak homotopy types agree. The six-point witness above shows that the bound five is optimal.

## Verification
Running `python3 checks/four_graph_threshold.py` yields the exact counts of upper-triangular transitively closed orders \((1,2,7,40,357)\), signature classes \((1,2,5,15,52)\), and total valid free-face pairs \((0,0,1,20,400)\), with `all_class_types_consistent=YES` at every size and `CERTIFICATE PASS` at the end. The two explicitly defined six-element orders are verified directly, including equality of the four graph adjacency arrays and respective total numbers of nonempty order-complex faces \(26\) and \(35\). The infinite-sounding statement “all spaces on at most five points” is an exhaustive **finite theorem**, not an extrapolation from a sample.

## Relationship to prior work
Cameron and Kumar, *Graphs on Topological Spaces*, introduced the hierarchy of five graphs and proved the finite-Alexandrov relationships used above. Their joint/topological graph framework, a four-point example where inseparability **alone** fails to retain weak homotopy, and the specialization graph's positive recovery theorem are acknowledged. Their general ordinal-sum graph identities imply the elementary six-point witness once specialized; the asserted additional result here is the **sharp impossibility of any smaller joint-graph collision**, supported by a complete five-point census. The work of Matsushima and Tsukuda constrains small finite-space homotopy types, but does not give this joint-graph threshold. Literature involving clique graphs of minimal/maximal elements uses different graph functors and does not establish this specific threshold from its accessible abstract.

## Limitations
The implication is **about weak homotopy equivalence**, not homeomorphism, ordinary homotopy of finite spaces, or equality of posets. The graphs must be compared under a common vertex bijection. The specialization graph is intentionally omitted because its recovery theorem makes an analogous counterexample impossible. Classification beyond the sharp failure threshold is not asserted. Exhaustiveness is guaranteed by the finite enumeration argument and checked program, not by unverified database completeness. An equivalent unpublished or unindexed earlier priority result remains possible. No independent mathematical audit is claimed.

## References
- P. J. Cameron and V. Kumar P. B., *Graphs on Topological Spaces*, arXiv:2610.14783v1 (first public 2026-10-10), https://arxiv.org/abs/2610.14783.
- K. Matsushima and S. Tsukuda, *On the weak homotopy types of small finite spaces*, arXiv:2404.12564v1 (first public 2024-04-19), https://arxiv.org/abs/2404.12564.
- *Posets, clique graphs and their homotopy type*, *European Journal of Combinatorics* (2008), https://doi.org/10.1016/j.ejc.2006.04.012 (abstract-level comparison only).

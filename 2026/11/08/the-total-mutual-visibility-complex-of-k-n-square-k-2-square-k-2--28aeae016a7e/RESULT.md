# The total mutual-visibility complex of \(K_n\square K_2\square K_2\)

## Finding

Let \(n\ge2\) and let \(G_n=K_n\square K_2\square K_2\). A total mutual-visibility set \(X\) is a vertex subset for which every pair of graph vertices admits a shortest path with no internal vertex in \(X\). Let \(\Delta_n\) be the simplicial complex whose faces are all such \(X\), including the empty set. The following statements form one complete structural theorem.

**Classification.** Write the vertices as \((i,s)\), with \(i\in[n]\) and \(s\in\{00,01,10,11\}\). Define the parity of \(s\) as the sum of its two bits modulo \(2\). Every face belongs to one of the following families, and every displayed family is feasible:

1. At most one vertex from each column \(i\), with all selected bit-pairs having the same parity. The empty set is allowed, and its parity is unspecified.
2. Exactly two vertices in a single column, with adjacent bit-pairs (Hamming distance one).

For \(n\ge2\), the facets are precisely the \(2^{n+1}\) first-type faces that select one vertex from *every* column, and the \(4n\) second-type two-element faces. Their sizes are \(n\) and \(2\) (coincident when \(n=2\)). Consequently the lower total mutual-visibility number is \(2\) while the maximum is \(n\); for \(n\ge4\), no facet has any size strictly between these two extremes.

The exact all-face cardinality polynomial is
\[
F_n(z)=\sum_{X\in\Delta_n}z^{|X|}=2(1+2z)^n-1+4nz^2.
\]
The corresponding facet polynomial is \(4nz^2+2^{n+1}z^n\), with coinciding-degree contributions added when \(n=2\).

**Homotopy type.** The entire complex, not merely its homology ranks, satisfies
\[
\Delta_n\simeq S^{n-1}\vee S^{n-1}\vee\bigvee^{4n-1}S^1\qquad(n\ge2).
\]
In particular, for \(n\ge3\) its only positive-dimensional reduced integral homology groups are \(\widetilde H_1(\Delta_n;\mathbb Z)\cong\mathbb Z^{4n-1}\) and \(\widetilde H_{n-1}(\Delta_n;\mathbb Z)\cong\mathbb Z^2\). For \(n=2\), these dimensions coincide and \(\Delta_2\simeq\bigvee^9S^1\). All integral homology is torsion-free.

**Fixed-size token jumping.** For \(1\le k\le n\), form a graph on the \(k\)-vertex total mutual-visibility sets, joining two sets when one selected vertex can be replaced by one unselected vertex. This graph is connected for \(k=1,2\), and has exactly two connected components for every \(3\le k\le n\). For \(k>n\), it has no vertices.

## Assumptions and scope

All graphs are finite, undirected, and simple. The complete graph \(K_n\) has vertices \([n]\). The two binary factors are independent coordinates, and their product is the four-cycle \(Q_2=K_2\square K_2\). Graph distances are shortest-path lengths in the Cartesian product. The complex contains the empty face, but the empty face contributes no point to its usual geometric realization. A facet means an inclusion-maximal face. A token-jumping edge changes exactly one element while preserving the selected cardinality.

## Proof

**1. Reduction to forbidden distance two.** We reproduce the pertinent Hamming-graph lemma so that the classification does not depend on an unproved external step. In a Cartesian product of complete graphs, a subset \(X\) is total mutual-visible if and only if it has no two points at graph distance exactly \(2\). Necessity: a distance-two pair of points in \(X\) is the pair of internal alternatives on a convex Cartesian four-cycle between the other two opposite corners; therefore those other corners have no unblocked shortest path. Sufficiency: take any two vertices \(u,v\) at distance \(d\ge2\). Within their coordinate interval, the \(d\) immediate predecessors of \(v\) are pairwise at distance exactly \(2\); hence at most one belongs to \(X\). Choose a predecessor \(w\notin X\). Inductively, a shortest \(u,w\)-path has no internal vertex in \(X\); adjoining \(wv\) gives a shortest unblocked \(u,v\)-path. The distance-one case is immediate. This is also Theorem 6 of Bujtás--Klavžar--Tian (2023).

**2. Column classification.** For \((i,s),(j,t)\in V(G_n)\),
\[
d((i,s),(j,t))=\mathbf1_{\{i\ne j\}}+d_{Q_2}(s,t).
\]
Two selected vertices in a common column cannot be antipodal in \(Q_2\), while two selected vertices from different columns cannot have adjacent binary labels. Every subset of the four-cycle without antipodal pairs has at most two labels; if it has two, those labels are adjacent. If column \(i\) contains adjacent labels \(s,t\), every other binary label is adjacent to at least one of them, since the union of their open neighborhoods in \(Q_2\) is all four vertices. Thus all other columns must be empty. Otherwise every column contains at most one selected label, and any two labels in different occupied columns must be nonadjacent. The bipartition of \(Q_2\) into two parity classes gives exactly the first family. These constraints are precisely the forbidden-distance-two conditions, proving necessity and sufficiency.

**3. Facets and enumeration.** Within either parity class there are two possible binary labels for each occupied column and exactly one occupancy choice per column. The face polynomial of one parity family is \((1+2z)^n\). The two parity families share only the empty face. The second family supplies four additional two-element faces in each of the \(n\) columns, yielding \(F_n(z)\). A first-type face with an empty column extends by a same-parity label. A first-type face covering every column cannot extend because any new vertex lies in an occupied column: it is either antipodal to its selected label or adjacent to a selected label in another column, which exists for \(n\ge2\). A second-type face cannot extend to any third vertex by Step 2. This proves the exact facets and the stated lower/upper sizes.

**4. Homotopy type.** Let \(A_0,A_1\) be the subcomplexes of first-type faces of parity \(0\) and \(1\), respectively. In either, each column contributes two isolated vertices and at most one may be chosen. Thus \(A_p\) is the \(n\)-fold simplicial join of a zero-sphere with itself, and \(|A_p|\cong S^{n-1}\). The two geometric realizations are disjoint. The only faces outside them are the \(4n\) second-type edges; each joins one vertex of \(A_0\) to one of \(A_1\), with no higher-dimensional mixed face. Because \(n\ge2\), both spheres are path-connected. Attaching one of these edges joins the two components, while attaching each of the remaining \(4n-1\) edges contributes a free circle in a CW homotopy decomposition. More formally, adjoining finitely many one-cells between two path-connected CW subcomplexes is homotopy equivalent to their wedge with one fewer circle than the number of connecting cells, obtained by collapsing a connecting path in a maximal tree. The claimed wedge homotopy follows integrally.

**5. Token-jumping connectivity.** All singleton faces are mutually adjacent by a single replacement. At size \(2\), first-type faces with a fixed parity are connected because one can change a binary label within a chosen column or exchange an occupied column with an unoccupied one. Each second-type edge \(\{(i,s),(i,t)\}\), where \(s,t\) are adjacent, has token-jumping neighbors of either parity: retain \((i,s)\) and replace \((i,t)\) by any same-parity label in a second column, or retain \((i,t)\) and replace \((i,s)\) analogously. Since \(n\ge2\), this joins the parity subgraphs and proves connectivity at size \(2\). For \(k\ge3\), all faces are first-type, and any single replacement preserves the parity (two parity families have disjoint vertex sets and \(k-1\ge2\) unchanged vertices). Within one parity class, replacements change labels in occupied columns and exchange occupied columns, yielding connectivity. Hence precisely two components for \(3\le k\le n\).

## Verification

The supplied standard-library Python verifier constructs the actual Hamming graph, derives every forbidden pair by common-neighbor tests on pairs of vertices at distance two, recursively enumerates all legal faces for \(2\le n\le6\), and compares them with the explicit polynomial, facet spectrum, and fixed-cardinality token-jumping components. It also checks every subset at \(n=2,3,4\) against the classification, and separately checks the original all-pairs shortest-path definition for every subset at \(n=2,3\). Binary simplicial boundary ranks independently establish the stated homology ranks through \(n=4\). This is finite corroboration; the unrestricted statements follow from Steps 1--5.

## Relationship to prior work

Bujtás, Klavžar and Tian (arXiv:2307.05168, first public 2023-07-11) prove the general distance-two characterization for Hamming graph total mutual-visibility sets and determine the maximum total mutual-visibility number for all three-factor Hamming graphs. In this family their maximum equals \(n\), a known fact **not claimed as new**. The contribution here is the exact family and facet decomposition, complete enumerator, integral homotopy type, and fixed-cardinality reconfiguration components for the two-binary-factor slice. The predecessor's membership criterion is an essential general antecedent; its exact theorem does not itself state the evaluations and topology in this note.

Brešar and Yero (arXiv:2307.02951, first public 2023-07-06) introduce the lower total mutual-visibility number and study its behavior in products, without the complete present facet classification. Tian and Klavžar (arXiv:2212.07193) prove earlier product bounds, including the maximum for a product of two complete graphs. Bujtás, Klavžar and Tian (arXiv:2412.03066) establish additional general total-visibility characterizations and visibility polynomials, but do not explicitly compute this homotopy or this enumeration in the inspected text.

## Limitations

Only the three-factor family with two binary factors is covered; no formula is asserted for general \(K_a\square K_b\square K_c\). The result is an exact mathematical deduction from the known Hamming distance-two criterion rather than a new general criterion. No independent mathematical audit or publication-priority certification has been performed. An unindexed equivalent combinatorial/topological treatment cannot be ruled out by the available literature and database comparisons.

## References

1. C. Bujtás, S. Klavžar, J. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168 (first posted 2023-07-11), especially Theorems 1, 6 and 9. https://arxiv.org/abs/2307.05168
2. B. Brešar, I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951 (first posted 2023-07-06). https://arxiv.org/abs/2307.02951
3. J. Tian, S. Klavžar, *Graphs with total mutual-visibility number zero and total mutual-visibility in Cartesian products*, arXiv:2212.07193 (first posted 2022-12-14). https://arxiv.org/abs/2212.07193
4. C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066 (first posted 2024-12-04). https://arxiv.org/abs/2412.03066

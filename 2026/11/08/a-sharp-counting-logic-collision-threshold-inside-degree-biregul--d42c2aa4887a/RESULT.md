# A sharp counting-logic collision threshold inside degree-biregular block graphs

## Finding
Let \(\mathcal B\) consist of all finite connected simple **block graphs** (all biconnected blocks are cliques) with the following degree incidence rule: every vertex has degree two or three; every degree-three vertex has three degree-two neighbors; and every degree-two vertex has exactly one degree-three neighbor and one degree-two neighbor. Graphs in \(\mathcal B\) have no externally prescribed vertex colors.

For each integer \(i\ge0\), define \(a_0=1\), and for \(i\ge1\) let \(a_i\) be the number of nonisomorphic unrooted trees on \(i\) vertices of maximum degree at most three. Then the following classification holds:

1. The possible orders of graphs in \(\mathcal B\) are exactly \(8i+8\), for \(i\ge0\).
2. There are exactly \(a_i\) isomorphism types at order \(8i+8\). **All** these types satisfy exactly the same unrestricted two-variable first-order sentences with counting quantifiers, \(\mathrm C^2\), in the pure undirected-adjacency/equality language.
3. The first order containing nonisomorphic, \(\mathrm C^2\)-equivalent members of \(\mathcal B\) is **40**, when \(i=4\), and precisely two types occur there. For each \(i\ge4\), there are at least two distinct types in a single \(\mathrm C^2\)-equivalence class.

The numbers of types for \(i=0,\ldots,8\) are \(1,1,1,1,2,2,4,6,11\). The theorem concerns **equivalence within the stated class**; it does not assert that these graphs are identified by counting logic among arbitrary graphs, and does not claim that 40 is the first collision among all block graphs.

## Assumptions and scope
A finite simple block graph is one whose maximal biconnected subgraphs are complete. A degree-biregular incidence rule means precisely the three degree conditions stated above, not just a prescribed degree sequence. All structures are undirected, loopless, uncolored finite graphs. The logic allows all finite numerical counting thresholds and arbitrary quantifier nesting, but uses at most two variable names.

We use the standard correspondence between stable one-dimensional color refinement and \(\mathrm C^2\) graph equivalence. Joint refinement uses a common palette across both graphs; two graphs are indistinguishable precisely when they have identical stable color histograms.

## Proof
**1. Structural reduction.** Let \(G\in\mathcal B\). Write \(C\) for its degree-three vertices and \(S\) for its degree-two vertices. Every vertex of \(S\) is adjacent to exactly one vertex of \(C\), and its other neighbor lies in \(S\). Thus the edges induced by \(S\) form a perfect matching, and each \(c\in C\) has exactly three matched half-edges attached to it.

For every matched edge \(ss'\), let \(c,c'\in C\) be the unique centers adjacent to \(s,s'\). If \(c=c'\), this matching edge closes a triangle \(css'c\). Since \(c\) has only three stubs, it can close at most one such triangle. Otherwise the matching edge creates a three-edge path \(c-s-s'-c'\) between distinct centers. Form a multigraph \(T\) with vertex set \(C\) and one edge for each such path. Connectivity of \(G\) implies connectivity of \(T\) (and \(C\ne\varnothing\)). If \(T\) had a parallel pair or any cycle, those subdivided paths would form a cycle of length at least six in \(G\). Such a cycle would lie in a biconnected component that is not a clique, contrary to the block-graph hypothesis. Hence \(T\) is a simple tree.

At each center, either two stubs are paired with one another (one triangle, one edge of \(T\)), or all three stubs lead to distinct edges of \(T\). Therefore every vertex of \(T\) has degree one or three; triangles occur exactly at its leaves. No tree with a single vertex can meet the three-stub matching rule, so \(T\) has at least two vertices.

Conversely, given **any** tree \(T\) whose degrees are in \(\{1,3\}\), replace each vertex by a center joined to three new degree-two stubs. For each tree edge, pair one previously unused stub at each endpoint, and at each leaf pair the two remaining stubs with each other. This creates a connected simple graph \(G(T)\) whose only nontrivial blocks are triangles at the leaves and whose remaining blocks are bridges. Thus \(G(T)\in\mathcal B\). The pairing choices are immaterial up to isomorphism. The original \(T\) is recovered canonically from \(G(T)\) by selecting the degree-three centers and recording the three-edge paths between distinct centers. Hence \(G(T)\cong G(T')\) if and only if \(T\cong T'\).

**2. Enumeration.** Let \(i\) be the number of degree-three vertices of \(T\), and \(l\) its number of leaves. The handshake lemma gives \(l+3i=2(l+i-1)\), hence \(l=i+2\) and \(|V(T)|=2i+2\). Each vertex of \(T\) contributes one center and three stubs, so \(|V(G(T))|=4(2i+2)=8i+8\).

For \(i=0\), the only tree is a single edge. For \(i\ge1\), deleting the leaves of \(T\) gives a tree on \(i\) vertices of maximum degree at most three. Conversely, attach \(3-\deg_U(u)\) leaves to every vertex \(u\) of such an internal tree \(U\) (for \(i=1\), attach three). This construction and leaf deletion are inverse on isomorphism types. Thus there are exactly \(a_i\) possibilities.

**3. Counting-logic equivalence.** Every degree-three center has exactly three neighbors in \(S\) and none in \(C\). Every degree-two stub has exactly one neighbor in \(C\) and one in \(S\). Accordingly \((C,S)\) is an equitable partition with quotient neighbor counts \(\bigl(\begin{smallmatrix}0&3\\1&1\end{smallmatrix}\bigr)\), independent of \(T\). Starting from the uniform coloring, the first refinement distinguishes the two degrees, and that two-color partition is already stable. For any two graphs associated with the same \(i\), the cell sizes are identically \((2i+2,6i+6)\). Joint refinement therefore has identical color histograms at every depth. By the standard one-dimensional color-refinement/\(\mathrm C^2\) equivalence, the graphs satisfy the same \(\mathrm C^2\) sentences.

**4. Sharpness and infinitude.** Trees on \(i\le3\) vertices are unique up to isomorphism. At \(i=4\), the path on four vertices and the three-leaf star are distinct, both with maximum degree three; these are the only two unrooted four-vertex trees. Their expansions give distinct, indistinguishable 40-vertex members. For every \(i\ge4\), the path on \(i\) vertices and the tree obtained by adding one leaf to a non-end vertex of a path on \(i-1\) vertices are nonisomorphic and have maximum degree three. Their expansions yield the asserted infinite sequence of collisions.

## Verification
The package includes a standalone, standard-library Python program `verify.py`, a successful captured output `verification_output.txt`, and both explicit forty-vertex edge lists `witness_edges.txt`. Run `python verify.py` from a directory containing the program. The program enumerates unrooted trees through eight internal vertices by exhaustive leaf attachment and exact recursive tree canonization, filters maximum degree three, constructs their expanded block graphs, verifies their block structure with an independent Tarjan decomposition, recovers the internal trees, and checks simultaneous color refinement for every pair at each size. It additionally checks one explicit pair at every internal size from four to twenty-nine. The program ends in `VERIFY_OK`. All enumerated checks are finite; the unrestricted theorem rests on the proof above.

## Relationship to prior work
Arvind, Köbler, Rattan and Verbitsky explain color refinement, its equivalence with two-variable counting logic, and the distinction between amenable and non-amenable graphs. Kiefer, Schweitzer and Selman characterize graphs identified absolutely by \(\mathrm C^2\) and develop general matching/inversion constructions. Neither general theorem alone states a classification **within this degree-biregular block-graph class** or the first relative collision at forty vertices. Gavrilyuk, Nedela and Ponomarenko prove that two-dimensional Weisfeiler–Leman identifies distance-hereditary graphs, including block graphs; that is a stronger algorithm than the one-dimensional refinement considered here, so it is consistent with this result. Classical block-graph characterizations specify the structural domain.

The eight-vertex single-edge-skeleton example, two triangles joined by a three-edge path, is not new as an isolated nonrefinable graph. The new claimed contribution is the complete internal-tree parametrization and counting-logic spectrum of the specified class, including the sharp **relative** collision threshold and infinite distinct pairs.

## Limitations
No claim is made about minimum collision order among unrestricted block graphs or chordal graphs, nor about higher-dimensional Weisfeiler–Leman. The classification requires the exact degree-incidence rule; dropping this rule admits many additional graphs. Historical priority is provisional: an equivalent tree-gadget description under different terminology may exist. An independent mathematical audit has not been performed.

## References
- V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public version 2015-02-04), especially introduction and color-refinement definitions.
- S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (first public version 2015-03-30), especially Section 4 and matching constructions.
- A. L. Gavrilyuk, R. Nedela and I. Ponomarenko, *The Weisfeiler-Leman Dimension of Distance-Hereditary Graphs*, arXiv:2005.11766 (first public version 2020-05-24), Theorem 1.
- A. Behtoei, M. Jannesari and B. Taeri, *A characterization of block graphs*, Discrete Applied Mathematics 158 (2010), 219–221, DOI:10.1016/j.dam.2009.09.024.

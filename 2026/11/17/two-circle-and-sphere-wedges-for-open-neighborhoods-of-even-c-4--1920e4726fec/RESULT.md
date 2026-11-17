# Two circle-and-sphere wedges for open neighborhoods of even \(C_4\square C_n\) tori

## Finding
For every **even integer** \(n\ge 6\), let \(G_n=C_4\square C_n\) be the simple Cartesian graph on \((r,c)\in\mathbb Z/4\times\mathbb Z/n\), in which two vertices are adjacent when they differ by one in exactly one cyclic coordinate. Let \(\mathcal N(G_n)\) denote the *open Lovász neighborhood complex*: its nonempty faces are finite sets of vertices having a common neighbor in \(G_n\). Then the exact integral homotopy type is
\[
\boxed{\mathcal N(G_n)\simeq\left(S^1\vee\bigvee^{n}S^2\right)\ \sqcup\ \left(S^1\vee\bigvee^{n}S^2\right).}
\]
In particular, \(\widetilde H_0(\mathcal N(G_n);\mathbb Z)\cong\mathbb Z\), \(H_1(\mathcal N(G_n);\mathbb Z)\cong\mathbb Z^2\), and \(H_2(\mathcal N(G_n);\mathbb Z)\cong\mathbb Z^{2n}\), with no higher homology or integral torsion. The homotopy assertion is stronger than this homology calculation.

## Assumptions and scope
The parameter \(n\) is even and at least six. Both cycle graphs are simple; thus \(G_n\) has \(4n\) vertices and is four-regular. The maximal faces of \(\mathcal N(G_n)\) are the \(4n\) four-vertex neighborhoods
\[
T_{r,c}=\{(r-1,c),(r+1,c),(r,c-1),(r,c+1)\},
\]
where cyclic coordinates are understood. Its full face-vector, in dimensions zero through three, is \((4n,14n,16n,4n)\), as follows either from the local neighborhood incidences or from the reduction below. Here homotopy equivalence is of geometric realizations. The result concerns open, not closed, neighborhoods; neither a graph-metric Rips complex nor a graph matching complex is involved.

## Proof
**1. Two components and a row-zero cycle.** Fix the row \(A=\{(0,c):c\in\mathbb Z/n\}\). Faces supported on \(A\) are precisely vertices and pairs \(\{(0,c-1),(0,c+1)\}\), since each vertex-neighborhood contains at most two row-zero vertices. Hence this induced one-complex is the disjoint union of two simple cycles of length \(n/2\): their column labels have opposite parity. For even \(n\), the graph \(G_n\) is connected and bipartite by parity of \(r+c\). The open-neighborhood complex has exactly the same two components as the two parity classes: simplicial edges arise from length-two walks, and all same-parity vertices are connected by even walks in the connected graph.

**2. A complete first-stage acyclic matching.** Write each face as \(F\cup B\), with \(F\) the set of its vertices outside \(A\) and \(B\subseteq A\). Consider the order-preserving map sending a face to \(F\). For any nonempty \(F\), its allowed row-zero extensions \(B\) form the full power set of a set \(E(F)\subseteq A\) with at most two elements. This can be checked directly from the displayed four-vertex neighborhoods: a row-zero vertex can coexist with \(F\) only in a neighborhood centered in rows zero, one, or three; two such row-zero vertices, when possible, are the two row-zero vertices of the same \(T_{0,c}\), so their joint extension is also allowed. When \(E(F)\ne\varnothing\), toggle its least vertex in every face of the fiber. This perfectly matches that fiber, and these matchings are acyclic by the standard fiber/patchwork criterion. When \(E(F)=\varnothing\), keep \(F\) critical at this stage.

In the empty fiber \(F=\varnothing\), match each non-root vertex of the two row-zero cycles to the edge joining it to its predecessor along the corresponding cycle, leaving one vertex and one edge on each cycle. This is acyclic and compatible with the fiber matching. Exactly the following additional critical faces remain: for each \(c\in\mathbb Z/n\), the edge
\[
e_c=\{(2,c-1),(2,c+1)\},\]
the four triangular facets of \(T_{2,c}\), and the tetrahedron \(T_{2,c}\). Indeed, every other face outside \(A\) has a row-zero extension; the four listed triangles and tetrahedron do not. Thus the intermediate critical counts are two vertices, \(n+2\) edges, \(4n\) triangles, and \(n\) tetrahedra.

**3. A further acyclic Morse cancellation.** For each \(c\), append the two face-coface pairs
\[
\begin{split}
e_c&\longleftrightarrow e_c\cup\{(1,c)\},\\
e_c\cup\{(3,c)\}&\longleftrightarrow T_{2,c}.
\end{split}
\]
They are disjoint from the earlier pairs. To verify combined acyclicity, use the dimensional gradient-path criterion. A first-stage matched upward move toggles a row-zero vertex, and any subsequent downward move never increases the set of non-row-zero vertices. At dimension one, after taking a new pair from \(e_c\) to its triangle, any alternative downward edge has only one row-two vertex together with a row-one vertex, and subsequent first-stage moves cannot return to an \(e_d\), which has two row-two vertices. At dimension two, after the new pairing of the triangle with \(T_{2,c}\), its other triangular facets are either the dimension-one paired triangle or two unpaired triangles; no further dimension-two matched upward move is available. For all other dimensions only the already acyclic first-stage matching acts. This rules out every closed gradient path.

The remaining critical cells are exactly two zero-cells, two one-cells, and \(2n\) two-cells, with nothing in higher dimensions. The two one-cells represent the two row-zero cycles; parity separates the remaining critical two-cells equally, giving \(n\) two-cells in each component. Discrete Morse theory therefore supplies a two-dimensional CW model in which each connected component has one zero-cell, one loop, and \(n\) two-cells.

**4. Every attaching degree is zero, integrally.** For an oriented simplicial edge \((r,c)\to(r',c')\), define \(\omega\) to be the unique integer \(d\in\{-2,-1,0,1,2\}\) congruent to \(c'-c\pmod n\). Uniqueness holds for all edges in this complex when even \(n\ge6\), because each edge lies within the three consecutive columns of a neighborhood. Every triangle lies in such a three-column window and thus has \(\omega\)-sum zero around its boundary. So \(\omega\) is an integral cocycle. On either row-zero cycle, orient successive edges with column step \(+2\); there are \(n/2\) edges, and \(\omega\) evaluates to \(n\ne0\). Consequently the generator of \(H^1\) represented by the circle of each Morse CW component survives nontrivially in the entire complex.

An attaching map of a two-cell to a circle is classified by an integer degree. If any of the \(n\) attaching degrees in either component were nonzero, then \(H^1\) of that component would vanish, contradicting the nonzero evaluation of \(\omega\). Hence all degrees are zero. Each two-cell is attached by a nullhomotopic loop, proving the asserted disjoint union of two copies of \(S^1\vee\bigvee^nS^2\). This argument works over the integers, without extrapolating a finite mod-prime rank calculation.

## Verification
The standalone standard-library script `verify_even_tori.py` constructs every face from the original graph neighborhoods, independently rebuilds both stages of the matching, verifies each pair is a codimension-one incidence, checks exact critical-cell counts, and topologically sorts the entire oriented Hasse graph to test acyclicity. It also tests the integer cocycle on every triangle and its nonzero winding on both row-zero cycles. It runs these checks for every even \(n\) from six through twenty and computes reduced mod-two homology independently for \(n=6,8,10,12\). Its deterministic output is `EXPECTED.txt`. These finite tests corroborate, but are not used as substitutes for, the all-parameter proof above.

## Relationship to prior work
Shukla [1, Theorem 6(B) and Theorem 13] classifies analogous *four-regular circulant* neighborhood complexes, including the odd-length \(C_4\square C_n\) cases (there the Cartesian product is circulant because \(\gcd(4,n)=1\)). Those odd cases are **not** claimed here. The even-length product is not circulant: for \(n\ge6\) its Cartesian-factor automorphism group has no cyclic regular subgroup of order \(4n\), so that circulant theorem does not imply this result. More importantly, the published square-lattice quotient theorem [2] explicitly assumes every nonzero lattice period has Manhattan length at least five; the period \((4,0)\) in our graph violates this hypothesis. Its torus conclusion therefore cannot be applied to \(C_4\square C_n\). The 2026 neighborhood-complex classification of Namiq [3] concerns two-linear Stanley–Reisner resolutions and graphs with no induced cycles longer than four; our graphs contain induced \(n\)-cycles with even \(n\ge6\), so its stated classification does not determine these homotopy types. These comparisons identify a genuine short-period boundary regime without asserting uniqueness from database absence.

## Limitations
The result applies to even lengths \(n\ge6\) only. It does not reclassify the previously covered odd-length circulant cases, the exceptional \(n=4\) grid, arbitrary twisted periods, or general four-regular graphs. Exact digital calculations corroborate the first eight even cases; only the explicit Morse and winding arguments establish the infinite statement. The literature comparisons leave the usual residual risk of unpublished or unindexed equivalents. Independent mathematical auditing has not been performed.

## References
[1] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, *Electronic Journal of Combinatorics* 26 (2019), P2.4, first preprint arXiv:1802.04526 (2018-02-13), https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i2p4/pdf/ .

[2] *Toroidal grid neighborhood complexes collapse to one or two tori*, public mathematical research note (2026-10-11), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-toroidal-grid-neighborhood-complexes-collapse-to-one-or-two-tori--737edf71bc86/RESULT.md .

[3] M. R. Namiq, *A Complete Classification of 2-Linear Neighborhood Complexes*, arXiv:2606.03573 (first posted 2026-06-02), https://arxiv.org/abs/2606.03573 .

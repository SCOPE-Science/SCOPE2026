# Dyck and Shrikhande line graphs as optimal power-domination relocation networks

## Finding
Let \(G\) be the Shrikhande graph on \(\mathbb Z_4^2\), with two distinct vertices adjacent when their difference belongs to
\[
D=\{\pm(1,0),\pm(0,1),\pm(1,1)\}.
\]
Its power-domination number is \(\gamma_P(G)=2\). The **complete family** of its minimum power-dominating sets consists of the \(48\) unordered pairs \(\{u,v\}\) for which \(v-u\) belongs to
\[
C=\{\pm(1,2),\pm(2,1),\pm(1,3)\}.
\]
Here all coordinates are reduced modulo four, so there are no duplicate directions in the displayed set. The graph of optimal single-sensor exchanges, with any replacement permitted, is isomorphic to the line graph of the Shrikhande graph; the graph of optimal single-sensor **slides along an original edge** is isomorphic to the line graph of the \(32\)-vertex cubic Dyck graph:
\[
R_{\mathrm{jump}}(G)\cong L(G),\qquad R_{\mathrm{slide}}(G)\cong L(\mathrm{Dyck}).
\]
Consequently, both are connected. The first has \(48\) vertices, \(240\) edges, degree \(10\), radius and diameter \(3\); the second has \(48\) vertices, \(96\) edges, degree \(4\), radius and diameter \(5\). The unrestricted and local unordered-distance histograms are respectively
\[
(240,696,192),\qquad(96,192,336,384,120),
\]
with the entries indexed by positive distances in increasing order. Both graphs have \(48\) vertices, so either histogram totals \(\binom{48}{2}=1128\). For contrast, the cospectral, nonisomorphic \(4\times4\) rook graph with the same strongly regular parameters \((16,6,2,2)\) requires \(3\) power-domination sensors, rather than \(2\).

## Assumptions and scope
All graphs are finite, simple, undirected and labelled unless explicitly considered up to isomorphism. A nonempty sensor set \(S\) power dominates a graph when one initially marks \(N[S]\), and repeatedly marks every unique unmarked neighbor of a marked vertex, until all vertices are marked. An *optimal placement* is a power-dominating set of minimum cardinality. Two optimal placements are adjacent in \(R_{\mathrm{jump}}\) when their symmetric difference has size two, and in \(R_{\mathrm{slide}}\) when the removed and inserted vertices are additionally adjacent in \(G\). A line graph \(L(H)\) has one vertex for every edge of \(H\), adjacent exactly when those edges meet. The assertion concerns this fixed \(16\)-vertex Shrikhande graph and its \(16\)-vertex rook companion, not arbitrary strongly regular graphs.

## Proof
**1. Exhaustive orbit reduction using actual automorphisms.** Translations of \(\mathbb Z_4^2\) are automorphisms of \(G\). The invertible linear maps \(F(x,y)=(y,x)\) and \(T(x,y)=(x,x-y)\) also preserve \(D\); their action partitions the \(15\) possible nonzero displacements into exactly three orbits: \(D\) (six members), \(Q=\{(2,0),(0,2),(2,2)\}\) (three members), and \(C\) (six members). This is a direct finite verification under the two displayed maps; neither map depends on the chosen sensor pair. By translation, the same representatives classify every unordered pair.

A singleton at \((0,0)\) initially marks \(7\) vertices and cannot force any additional one. For an arbitrary pair, the following table reports the number marked immediately after its closed-neighborhood step and after all possible propagations. The table is checked directly against the six-neighbor formula \(N(u)=u+D\):

| Pair representative \(\{(0,0),v\}\) | Orbit | Initially marked | Finally marked |
|---|---|---:|---:|
| \(v=(1,0)\) | \(D\) | 10 | 10 |
| \(v=(0,2)\) | \(Q\) | 12 | 12 |
| \(v=(1,2)\) | \(C\) | 12 | 16 |

For the successful representative the four unmarked vertices after initial observation are \((2,0),(2,1),(3,1),(3,2)\). They are all forced immediately: respectively by \((1,3),(1,1),(0,1),(0,3)\), each of which has that unique unmarked neighbor. For the other two representatives every marked vertex has either no unmarked neighbors or at least two; thus no propagation can start. This proves the complete classification and, since there are six successful differences per vertex, the count \(16\cdot6/2=48\).

**2. Unrestricted relocation.** Define \(G_C\) on \(\mathbb Z_4^2\) with connection set \(C\). Its edges are precisely the \(48\) optimal placements. An unrestricted one-token exchange of a two-element placement changes one endpoint and retains the other, precisely the line-graph adjacency of \(G_C\). The invertible linear map \(U(x,y)=(x+y,2x+3y)\) sends \(C\) onto \(D\), so \(G_C\cong G\) and therefore \(R_{\mathrm{jump}}(G)\cong L(G)\).

**3. Local relocation and the cubic intermediary.** At the vertex \((0,0)\), the six permissible partners in \(C\), with adjacency inherited from the **original** Shrikhande graph, form exactly two disjoint triangles:
\[
\{(1,2),(1,3),(2,3)\}\quad\text{and}\quad\{(2,1),(3,1),(3,2)\}.
\]
Translation gives the same two-triangle partition at every original vertex \(u\). Construct a graph \(H\) with two vertices \((u,0),(u,1)\) for each \(u\in\mathbb Z_4^2\), representing these local triangles, ordered lexicographically. For each optimal pair \(\{u,v\}\), add one edge between the unique local triangle at \(u\) containing \(v\) and the unique local triangle at \(v\) containing \(u\). This yields \(32\) vertices and \(48\) distinct edges and each triangle-vertex has degree \(3\). Two optimal pairs are joined by a legal slide exactly when their two associated edges of \(H\) share a triangle-vertex: they retain the corresponding sensor \(u\), and the two alternative partners are adjacent in \(G\), as the local partition proves. Hence \(R_{\mathrm{slide}}(G)\cong L(H)\).

The attached file `dyck_isomorphism.json` gives an explicit bijection from the lexicographically numbered \(32\) vertices of \(H\) to the standard cubic Dyck graph labelled by the LCF chord sequence `[-13,5,-5,13]` repeated eight times, together with the Hamiltonian cycle. The standalone checkers validate the vertex bijection and all \(48\) edges, not just a matching size or spectrum. Thus \(H\cong\mathrm{Dyck}\), proving the claimed line-graph identification. The known Dyck construction from the \(32\) triangles of the Shrikhande graph supplies a second geometric interpretation of the same cubic graph, but is not used to assume the result.

**4. Exact relocation distances.** Both line graphs have \(48\) vertices. Exhaustive breadth-first search from **every one** of the \(48\) vertices gives the histograms above and verifies connectivity, radius and diameter. Both programs in the package reconstruct those graphs from separate representations, and the Dyck adjacency is independently verified from the LCF construction. Because all \(\binom{48}{2}\) pairs are included, this is an exhaustive finite certificate, not a sample extrapolated to an infinite family.

**5. The cospectral contrast.** On the \(4\times4\) rook graph, two selected cells meet at most two rows and at most two columns. Following initial monitoring, the remaining cells in the uncovered rows and columns form a rectangular unmarked block with both side lengths at least \(2\); no monitored vertex has exactly one unmarked neighbor. Thus no pair succeeds. Three cells in three distinct rows and three distinct columns leave only the opposite fourth-row/fourth-column cell unmarked, which is forced, so the optimum is \(3\). Both graphs have sixteen vertices, degree six, and exactly two common neighbors for every pair of distinct vertices. Consequently they have identical strongly regular parameters and spectrum even though their power-domination budgets differ.

## Verification
The package provides `verify_power_domination.py`, `verify_structural.py` and `dyck_isomorphism.json`; the first two require only the Python standard library. From their common directory run `python verify_power_domination.py` and `python verify_structural.py`. The first enumerates every singleton and every pair of the Shrikhande graph, every singleton/pair and all \(\binom{16}{3}\) triples of the rook graph, and all \(\binom{48}{2}\) pairs of distinct optimal Shrikhande configurations under both reconfiguration rules. The second uses coordinate-set arithmetic, checks all displacement-orbit representatives, constructs the local-triangle graph, verifies the line-graph correspondence, rechecks the local distance census and validates the Dyck certificate. Both computations have been replayed from the accompanying files. The algebraic orbit reduction and the explicit isomorphism certificate independently cover the critical nonstandard steps.

## Relationship to prior work
The framework, definition and motivation for power-domination reconfiguration come from Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798v1, first publicly available 5 January 2022. Its original work primarily treats token addition/removal and token jumping, rather than this example's exact local token sliding geometry. The standard Dyck graph is independently described by A. E. Brouwer and by MathWorld, including the cubic symmetric \(32\)-vertex construction from triangles of the Shrikhande graph and its LCF presentation. Those established facts alone do not classify which Shrikhande two-sensor placements power dominate, nor do they imply that the optimal local relocation graph is a Dyck line graph. The previously established power-domination enumeration for square rook graphs encompasses the rook comparison, which is used only as a contrast and not claimed anew. Indexed graph monitoring and reconfiguration records checked for equivalent formulations have not exposed this joint classification; unindexed or differently named literature may exist.

## Limitations
No general claim is made for larger strongly regular graphs, graph products, arbitrary power systems, or sensor movement allowing temporary nonoptimal placements. The shortest-path census and Dyck graph isomorphism are exact for the specified finite labelled graphs. An independent mathematical audit has not been performed. The available indexed record search does not prove priority over inaccessible historical work.

## References
1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798v1 (5 January 2022), https://arxiv.org/html/2201.01798v1 .
2. A. E. Brouwer, *Dyck graph*, https://aeb.win.tue.nl/graphs/Dyck.html .
3. E. W. Weisstein, *Dyck Graph*, MathWorld, https://mathworld.wolfram.com/DyckGraph.html .
4. Mathematical Reviews and zbMATH, *MSC2020: 68R10, graph theory in computer science*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=68R10 .

# The Shrikhande minimum independent-dominating exchange graph is the Dyck graph

## Finding

Let \(G\) be the Shrikhande graph. Its minimum independent dominating sets have size \(3\), and there are precisely \(32\) such sets. Under token sliding, where one selected vertex may be moved across an edge while the resulting three-set remains independent and dominating, their reconfiguration graph \(\mathcal I(G)\) is isomorphic to the **Dyck graph**, equivalently the triangular-face dual of the standard toroidal Shrikhande triangulation. This isomorphism is given explicitly below by a linear automorphism of the toroidal coordinate group.

In particular, \(\mathcal I(G)\) is connected, cubic, bipartite, and has \(32\) vertices, \(48\) edges, radius \(5\), and diameter \(5\). Every vertex has exactly \(1,3,6,9,9,4\) vertices at distances \(0,1,2,3,4,5\), respectively. Thus any two optimum configurations are connected by at most five optimality-preserving slides, and some pairs require five. For this graph, any exchange between minimum independent dominating sets that changes one vertex is a slide.

The previously documented facts that \(i(G)=3\) and that the triangular-face dual is the Dyck graph are not independently claimed as new. The principal assertion is the identification of the optimal-set reconfiguration graph with that dual, with its explicit correspondence and exact transformation distances.

## Assumptions and scope

Work in the additive group \(A=(\mathbb Z/4\mathbb Z)^2\). Define \(G=\operatorname{Cay}(A,C)\), with \(C=\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}\). Arithmetic on coordinates is modulo \(4\). A vertex set \(S\subseteq A\) is independent if no two of its elements are adjacent; it dominates if \(\bigcup_{v\in S}N[v]=A\), with \(N[v]\) denoting closed neighborhood. The independent domination number \(i(G)\) is the smallest size of an independent dominating set. The reconfiguration graph \(\mathcal I(G)\) has one vertex for each such minimum set and joins two sets when their symmetric difference consists of adjacent vertices of \(G\).

For a subset \(U\subseteq A\), let \(U+t=\{u+t:u\in U\}\). Define
\[
T_0=\{(0,0),(1,2),(2,1)\},\qquad T_1=\{(0,0),(1,3),(2,1)\}.
\]
Define two types of triangular faces
\[
F_0=\{(0,0),(1,0),(1,1)\},\qquad F_1=\{(0,0),(0,1),(1,1)\}.
\]
Their translates are the triangles in the standard toroidal embedding of \(G\). The triangular-face dual has one vertex per triangle and an edge when two triangles share an entire primal edge.

## Proof

**1. Minimum sets and classification.** Each closed neighborhood has size \(7\), and any two nonadjacent vertices have exactly two common neighbors, since \(G\) has strongly regular parameters \((16,6,2,2)\). Hence the union of two closed neighborhoods of nonadjacent vertices has size \(7+7-2=12<16\): no independent two-set dominates, and a singleton cannot dominate.

Both displayed triples \(T_0,T_1\) are independent and dominate \(G\), by direct examination of the six Cayley differences, so \(i(G)=3\). To classify all such triples, fix the origin by translation. Its nine nonneighbors yield exactly eighteen unordered pairs \(\{u,v\}\) for which \(\{(0,0),u,v\}\) is independent. Exactly the following six of those eighteen triples dominate:
\[
\begin{aligned}
&\{(0,0),(1,2),(2,1)\},\quad \{(0,0),(1,2),(3,1)\},\\
&\{(0,0),(1,3),(2,1)\},\quad \{(0,0),(1,3),(3,2)\},\\
&\{(0,0),(2,3),(3,1)\},\quad \{(0,0),(2,3),(3,2)\}.
\end{aligned}
\]
These six are exactly the triples through the origin among the translations of \(T_0\) and \(T_1\). Since every minimum triple has three vertices, translation transitivity gives \(16\cdot6/3=32\) minimum triples, exactly
\[
\{T_0+t:t\in A\}\ \dot\cup\ \{T_1+t:t\in A\}.
\]
Each orbit has sixteen distinct members. The limited eighteen-pair check is completely specified and is independently reproduced by the code; no incomplete search of larger configurations is used to claim classification.

**2. Exchange structure.** Two minimum triples can differ in one vertex only when they come from different displayed orbits. A direct coordinate-intersection calculation shows
\[
|T_0\cap(T_1+d)|=2\iff d\in D=\{(0,0),(1,2),(3,1)\}.
\]
No two distinct translates of either \(T_j\) overlap in two points. In every cross-orbit exchange the unique departing vertex and arriving vertex differ by an element of \(C\), so all one-vertex exchanges are valid slides. Thus \(\mathcal I(G)\) has two parts of sixteen vertices, each of degree three, and hence \(48\) edges.

**3. Identification with the triangular-face dual.** The \(32\) distinct triangles of \(G\) are the sixteen translates of each \(F_j\). Every one of the \(48\) edges of \(G\) lies in exactly two such triangles, so their dual is cubic on \(32\) vertices. Face adjacency has the analogous difference criterion
\[
|F_0\cap(F_1+d)|=2\iff d\in D'=\{(0,0),(0,3),(1,0)\}.
\]
The linear map \(L:A\to A\),
\[
L(a,b)=(2a+3b,a+b)\pmod4,
\]
has determinant \(-1\) modulo \(4\) and so is invertible, and sends \(D\) bijectively onto \(D'\). Therefore
\[
\Phi(T_j+t)=F_j+L(t),\qquad j\in\{0,1\},\ t\in A,
\]
is a bijection preserving and reflecting every adjacency. Hence \(\mathcal I(G)\) is the triangular-face dual of \(G\), which is the classical Dyck graph under the standard identification of that toroidal triangulation.

**4. Exact distances.** Breadth-first search from each of the thirty-two minimum sets in the fully specified graph of Step 2 gives the uniform distance profile \((1,3,6,9,9,4)\). The certificate contains all thirty-two vertex masks and all forty-eight edges, while the independent structural verifier reconstructs the dual graph from its two translation orbits. Consequently every vertex has eccentricity \(5\), so both the radius and diameter are \(5\), and the graph is connected. The complete enumerator and its independent structural cross-check are included below.

## Verification

Run `python3 verify_enumeration.py --certificate certificate.json` and `python3 verify_structural.py` from the directory containing the embedded files. The first program exhaustively considers all independent vertex subsets of cardinality at most three, constructs every eligible exchange, and computes all-source shortest-path distributions; it regenerates `certificate.json`. The second program independently proves the two translation-orbit description via the eighteen origin-containing independent triples, checks the thirty-two face triangles and all forty-eight primal edge incidences, and verifies the explicit linear isomorphism. Outputs are preserved in `enumeration.out` and `structural.out`. The certificate uses sorted binary masks for minimum triples and for graph edges.

These checks are exact and finite. They verify the stated graph-specific classification; they do not establish a general theorem for other strongly regular graphs or independent-domination reconfiguration problems.

## Relationship to prior work

Bonsma (arXiv:1402.1587, 2014) studies independent-set reconfiguration under standard models, with algorithms and structural results for cographs and related classes, rather than this non-cograph's minimum dominating independent sets. Brewster, Mynhardt and Teshima (arXiv:2303.06299, 2023) introduce and study the \(i\)-graph of a source graph, including general realizability questions; the present graph-specific identification is not among their reported results. The equivalence of unrestricted single exchanges and token slides for minimum independent dominating sets is consistent with the general theory and is not presented as a new general theorem. The Shrikhande graph's triangular-face dual is already identified as the Dyck graph in a published graph profile. The existing independent-domination value \(i(G)=3\) is also available in graph databases. Neither existing identification individually supplies the explicit relationship between minimum independent-dominating configurations and triangular faces.

## Limitations

The claim concerns only this sixteen-vertex graph, its minimum independent dominating triples, and one-vertex sliding exchanges. Numerical enumeration alone would not establish arbitrary-order statements; none are claimed. Priority may be affected by unindexed descriptions or database supplements giving the same 32-state \(i\)-graph. Literature and online database coverage are not exhaustive. No independent external scientific audit has been conducted.

## References

1. P. J. Cameron, *The Shrikhande graph*, dated 2010-08-26. https://cameroncounts.wordpress.com/2010/08/26/the-shrikhande-graph/
2. P. Bonsma, *Independent Set Reconfiguration in Cographs*, arXiv:1402.1587, first posted 2014-02-07. https://arxiv.org/abs/1402.1587
3. R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *Reconfiguration of Minimum Independent Dominating Sets in Graphs*, arXiv:2303.06299, first posted 2023-03-11. https://arxiv.org/abs/2303.06299
4. A. E. Brouwer, *Shrikhande* graph profile and its triangle dual. https://jaanos.github.io/tables/graphs/Shrikhande.html
5. House of Graphs, Shrikhande graph record (independent domination entry). https://houseofgraphs.org/graphs/1308

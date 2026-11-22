# All-cardinality general-position exchange components of complete multipartite graphs

## Finding
For each finite complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), the full fixed-size general-position reconfiguration phase diagram has a closed form. A *general-position set* contains no three vertices on a common shortest path. An exchange of batch size at most \(k\) changes at most \(k\) occupied vertices, keeping the number \(s\) of occupied vertices and the general-position property.

For \(r\ge2\), \(n_i\ge1\), and \(3\le s\le\max\{r,\max_i n_i\}\), set
\[
p_s=|\{i:n_i\ge s\}|,\qquad b_s=\mathbf1_{\{r\ge s\}}.
\]
The exact number \(c_{s,k}\) of exchange components is
\[
c_{s,k}=\begin{cases}
p_s+b_s,&1\le k\le s-2,\\
1,&k=s-1,\ b_s=1,\\
p_s,&k=s-1,\ b_s=0,\\
1,&k\ge s.
\end{cases}
\]
For \(s\in\{1,2\}\), the graph is connected for every \(k\ge1\). At batch size one and \(s\ge3\), the \(p_s\) pure-part components are Johnson graphs \(J(n_i,s)\); when \(b_s=1\) there is one further component of all rainbow partial transversals. Within either component, distance is exactly \(s-|X\cap Y|\). If \(r\ge s\), the graph at batch size \(s-1\) is connected with diameter at most two.

For instance, in \(K_{4,4,4}\) the 76 general-position triples have four one-exchange components: three copies of \(K_4\) and the 64-state product \(K_4\square K_4\square K_4\). Permitting two replacements makes all 76 states connected with diameter two. Conversely, \(K_{5,5}\) has two disjoint five-state components of four-sets for every batch size at most three; only a four-replacement move joins them.

## Assumptions and scope
All graphs are finite, simple, and labelled. There are at least two nonempty parts, so \(G\) is connected, and each shortest path is taken in \(G\). Fix a size \(s\) with \(1\le s\le\max\{r,\max_i n_i\}\), ensuring a nonempty state space. Batch exchanges are **unrestricted jumps**, not movements only along graph edges. Two distinct states \(X,Y\) are adjacent precisely when \(|X\setminus Y|=|Y\setminus X|\le k\). Every intermediate state, but not an ordering of the simultaneous replacements, must be feasible. The result is valid for all integers \(k\ge1\), including \(k\ge s\).

## Proof
**Classification of feasible sets.** Every pair of vertices in different parts is adjacent; every pair in the same part is at distance two, with each vertex from a different part lying on a length-two geodesic between them. Therefore a triple is forbidden exactly when it contains two vertices from one part and one from another. Consequently, every general-position set of size at least three is either **pure** (all vertices from a single part) or **rainbow** (at most one vertex from every part). This structural classification is known and is used here as input, not asserted as new.

**One-replacement components.** For a fixed part \(V_i\), the pure \(s\)-sets induce the Johnson graph \(J(n_i,s)\), nonempty precisely when \(n_i\ge s\). Its edges replace one chosen element, and the standard greedy replacement path gives distance \(s-|X\cap Y|\). If \(r\ge s\), the rainbow \(s\)-sets also form a connected one-replacement graph: given rainbow \(X,Y\), choose a vertex \(y\in Y\setminus X\). If the part of \(y\) is represented in \(X\), replace its current vertex (which is outside \(Y\)); otherwise replace any vertex of \(X\setminus Y\) from a part unrepresented in \(Y\). The second choice always exists, since both supports have size \(s\). In either case, the intersection with \(Y\) grows by one, proving exact distance \(s-|X\cap Y|\). For \(s\ge3\), any pure set and any rainbow set intersect in at most one vertex, and pure sets from distinct parts are disjoint. Hence no exchange of size at most \(s-2\) connects different types or different pure parts. This proves \(c_{s,k}=p_s+b_s\) for \(k\le s-2\), including the precise component structures at \(k=1\).

**Sharp batch thresholds.** If \(r\ge s\), every pure \(s\)-set \(X\subseteq V_i\) has a rainbow \(s\)-set meeting it in exactly one vertex: choose one vertex of \(X\) and one vertex from each of \(s-1\) other parts. Such states are adjacent at batch size \(s-1\). Since all rainbow states are already in one component, every pure component joins that component. If \(r<s\), rainbow states do not exist and the only types are pure; distinct parts have disjoint states, so no batch smaller than \(s\) joins them. At batch size \(s\), any two feasible states are adjacent, proving all remaining cases. For \(s=1,2\), every set of cardinality \(s\) is general position, so the exchange graph at \(k=1\) is the connected Johnson graph on all graph vertices.

**Diameter collapse.** When \(s\ge3\) and \(r\ge s\), two feasible states that intersect are adjacent in \(\mathcal R_{s,s-1}\). For disjoint pure sets in the same part, choose another pure \(s\)-set containing one vertex from each (possible since their union contains at least \(2s\) vertices). For disjoint pure sets in different parts, choose a rainbow set containing one vertex from each. For disjoint pure and rainbow sets, choose one vertex from each in different parts, then complete to a rainbow \(s\)-set. For two disjoint rainbow sets, their \(s\ge3\) chosen vertices include a pair from distinct parts; again complete to a rainbow set. Since \(r\ge s\), the required distinct parts are available. In each case the intermediate set meets both endpoints, producing a path of length two.

## Verification
The accompanying standalone Python 3 program `VERIFY.py` tests general-position feasibility from graph shortest-path distances independently of the two-family characterization. For all evaluated positive part-size profiles with two to four parts, each part of size at most four, and total order at most eleven, it enumerates every feasible size and all exchange budgets up to that size. It then computes all connected components directly by graph search and compares them with the theorem. The program reports `VERIFIED_PROFILES 1036`, `COMPONENT_COMPARISONS 2534`, and `VERIFY_OK`. This is a finite cross-check; the proof above establishes the unrestricted statement.

## Relationship to prior work
Cody and Detore (arXiv:2601.04351; first public January 7, 2026) develop higher-order geodesic independence, which motivates a dynamical study of feasible configurations. Rather (arXiv:2603.06930, especially Section 3) explicitly classifies general-position sets of complete multipartite graphs and counts them, so the foundational classification and state enumeration are **known**. Klavžar and collaborators (arXiv:2505.00535) examine the distinct mobile general-position problem using adjacent-vertex robot moves and graph coverage; their paper does not provide the unrestricted batch-exchange component diagram. The present claim concerns the entire all-cardinality, all-batch component geometry, sharp thresholds, and diameter collapse rather than any known static enumeration or adjacent-move mobility number.

## Limitations
The graph family is restricted to complete multipartite graphs; no universal result is asserted for arbitrary graphs or for adjacent-edge token sliding. The four-cluster decomposition and its consequences are elementary once the known general-position-set classification is available; the claimed contribution is its complete reconfiguration refinement. Historical priority remains provisional, particularly for results indexed under partition-matroid exchange or abstract independence-system reconfiguration. No independent external mathematical audit has been performed.

## References
- B. Cody and R. Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351 (first posted 2026-01-07), https://arxiv.org/html/2601.04351.
- B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (first posted 2026-03-06), https://arxiv.org/abs/2603.06930.
- S. Klavžar et al., *Moving through Cartesian products, coronas and joins in general position*, arXiv:2505.00535 (first posted 2025-05-01), https://arxiv.org/abs/2505.00535.
- S. Klavžar et al., *Traversing a graph in general position*, arXiv:2209.12631 (first posted 2022-09-26), https://arxiv.org/abs/2209.12631.

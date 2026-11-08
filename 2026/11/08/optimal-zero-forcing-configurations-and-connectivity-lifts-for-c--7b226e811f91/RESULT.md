# Optimal zero-forcing configurations and connectivity lifts for clique coronas

## Finding
For a finite connected simple graph \(G\) of order \(n\ge2\) and integer \(r\ge2\), let \(H=G\odot K_r\) be its *clique corona*: to each original vertex \(v\) attach a fresh clique \(C_v\) of size \(r\), joining every vertex of \(C_v\) to \(v\) and to no other original vertex. Let \(z=Z(G)\), let \(b(G)\) denote the number of minimum classical zero-forcing sets of \(G\), and define \(q=r^{n-z}(r+1)^z\).

**Classification.** Every minimum zero-forcing set of \(H\) arises uniquely from a minimum zero-forcing set \(B\) of \(G\) by the following independent choices for each \(v\):

* For \(v\in B\), choose **any \(r\) of the \(r+1\)** vertices of \(C_v\cup\{v\}\).
* For \(v\notin B\), choose **any \(r-1\) of the \(r\)** vertices of \(C_v\), excluding \(v\).

Consequently,
\[
Z(H)=n(r-1)+z,\qquad b(H)=b(G)r^{n-z}(r+1)^z.
\]

Write \(\mathcal R(X)\) for the token-jump reconfiguration graph of minimum zero-forcing sets of \(X\), joining two sets whose symmetric difference contains exactly two vertices. The classification defines a natural projection \(\pi:\mathcal R(H)\to\mathcal R(G)\). Its fiber over each \(B\) is the Cartesian product
\[
\mathcal R(H)[\pi^{-1}(B)]\cong
\left(\mathop{\square}_{v\in B} K_{r+1}\right)\square
\left(\mathop{\square}_{v\notin B} K_r\right).
\]
For each edge \(BB'\) of \(\mathcal R(G)\), there are exactly
\[
c=4r^{n-z+1}(r+1)^{z-1}
\]
reconfiguration edges with one end over \(B\) and the other over \(B'\); no edges join fibers over nonadjacent distinct base sets. In particular, the connected components of \(\mathcal R(H)\) correspond bijectively to those of \(\mathcal R(G)\), each component having exactly \(q\) times as many vertices. Moreover,
\[
|E(\mathcal R(H))|=
\frac{b(G)q}{2}\bigl(zr+(n-z)(r-1)\bigr)
+4r^{n-z+1}(r+1)^{z-1}|E(\mathcal R(G))|.
\]

These are exact results for all specified \(G\) and \(r\), not asymptotic statements.

## Assumptions and scope
All graphs are finite, undirected, simple. The graph \(G\) is connected and has \(n\ge2\) vertices; the attached cliques have \(r\ge2\) vertices. A classical zero-forcing process begins with selected (black) vertices; a black vertex with exactly one white neighbor may force that neighbor black. A zero-forcing set is an initially black set that can eventually make every vertex black. The minimum size is \(Z(X)\); a *minimum zero-forcing set* is a feasible set of that size, not merely inclusion-minimal. Token jumping replaces exactly one chosen vertex with one unchosen vertex; moves must preserve minimum feasibility. Each \(C_v\) is indexed by its original root \(v\).

## Proof
**Compulsory clique bound.** No zero-forcing set can leave two vertices of any \(C_v\) initially white. Otherwise these two remain white forever: they are adjacent twins, and every possible black neighbor of either sees both white vertices. Thus every zero-forcing set \(S\) contains at least \(r-1\) vertices of every \(C_v\).

**Projection lemma.** For any such \(S\) define
\[
B(S)=\{v\in V(G):v\in S\ \text{or}\ C_v\subseteq S\}.
\]
A root \(v\notin B(S)\) is initially white and has exactly one initially white attached-clique vertex, which cannot be forced before \(v\) becomes black: each black attached vertex then sees both white vertices, while the missing clique vertex sees no black-root route into its clique. Hence a root outside \(B(S)\) can become black only through a force from another root along an edge of \(G\). A root in \(B(S)\) is either initially black or can be forced from its fully black attached clique immediately. Deleting the attached-clique forcing steps from any complete forcing chronology therefore produces a legitimate zero-forcing chronology on \(G\) beginning at \(B(S)\). Thus \(B(S)\) is zero forcing in \(G\).

Count every selected clique vertex and each selected root. If \(v\notin B(S)\), the local contribution is at least \(r-1\). If \(v\in B(S)\), it is at least \(r\), since either the root is selected in addition to at least \(r-1\) clique vertices, or the full clique is selected. It follows that
\[
|S|\ge n(r-1)+|B(S)|\ge n(r-1)+z.
\]

**Construction and equality.** Take any zero-forcing basis \(B\) of \(G\) and apply the stated local choices. Each root of \(B\) is black initially or can be forced by its own full clique. Each such root with one white attached vertex can have that vertex forced by a black clique neighbor. Next follow any zero-forcing chronology for \(B\) in \(G\): before a black root makes an external force, its remaining attached vertex can be forced black. Whenever a new root becomes black, its missing attached vertex can then be forced black. Thus the constructed state forces all of \(H\), and its size equals the lower bound. Conversely, equality in the two lower-bound inequalities forces \(B(S)\) to be a minimum basis and forces exactly the listed local occupancies. The choices recover \(S\) uniquely. Hence the classification and multiplicity formula hold.

**Fiber structure.** For a fixed \(B\), the local active choices at \(v\in B\) are all \(r\)-subsets of an \((r+1)\)-set, pairwise related by one replacement: a \(K_{r+1}\). At \(v\notin B\) the local choices are all \((r-1)\)-subsets of the \(r\)-clique, forming \(K_r\). A move within one fiber changes only one local choice, so the induced fiber is the asserted Cartesian product and is connected.

**Between fibers.** A single replacement affecting different local blocks can change their selected occupancies only by \(-1\) and \(+1\). Thus the projected base sets either agree (for a move within a block) or differ by exchanging exactly one root. For an edge \(B'=B-\{v\}+\{w\}\), fix choices at the remaining \(n-2\) roots: there are \((r+1)^{z-1}r^{n-z-1}\) possibilities. At \(v\), each inactive local choice \(C_v-\{j\}\) is contained in exactly two active local choices: \(C_v\) and \((C_v-\{j\})\cup\{v\}\); hence there are \(2r\) valid ordered local descents. There are independently \(2r\) ordered ascents at \(w\). This gives exactly \(4r^{n-z+1}(r+1)^{z-1}\) crossing edges. It also ensures that each base edge has crossing edges in its lift. Connected fibers together with these crossings prove the component correspondence and component-size multiplier \(q\). Summing the edges of the regular Cartesian-product fibers (each fiber has degree \(zr+(n-z)(r-1)\)) and all crossing edges proves the edge formula.

## Verification
The symbolic proof is valid for arbitrary finite connected \(G\) and integer \(r\ge2\). For an independent finite check run `python3 verify_a.py` and `python3 verify_b.py` in the same directory as this document. They depend only on the Python standard library.

`verify_a.py` constructs corona graphs with bitset adjacency, exhaustively tests every candidate starting set until the true zero-forcing minimum, computes the complete one-token exchange graph, and compares exact minimum counts, edges, and component-size multisets against the theorem for several base graphs (including paths, cycles, stars, and a triangle), with attachment sizes two and three.

`verify_b.py` independently constructs adjacency using tagged vertices and immutable sets. For every labelled connected graph with two, three, or four vertices when \(r=2\), and every labelled connected graph with three vertices when \(r=3\), it exhaustively determines *all* true minimum zero-forcing sets and checks equality with the classification-generated sets. It checks 47 connected graph instances. The packaged output files record observed totals and passes. These finite checks support, but do not replace, the general proof.

## Relationship to prior work
Javaid, Irshad, Batool and Raza established the zero-forcing number of corona products (arXiv:1607.04071, first posted 14 July 2016); their known formula \(Z(G\odot K_r)=Z(G)+n(r-1)\) is **not new here**. The new claim is a complete characterization and exact number of all *minimum sets*, with a natural projection and quantitative connected-component transfer for their token-jump reconfiguration graph. In the inspected corona section of that paper the authors construct forcing sets and obtain the numerical invariant, without a minimum-set multiplicity formula or the reconfiguration lift.

Geneson, Haas and Hogben established the general framework of zero-forcing reconfiguration graphs (arXiv:2009.00220, first posted 1 September 2020), including the reconfiguration graph of a disjoint union and connectedness for forests. Their examined treatment does not give the present connected clique-corona lifting theorem. Neither their disjoint-union product rule nor the known numerical corona result implies the stated fiber/crossing-edge structure without the additional local classification. The possibility of an unindexed equivalent historical formulation remains an originality limitation.

## Limitations
The theorem concerns classical zero forcing and token jumping, not positive-semidefinite or skew forcing, not token sliding, and not arbitrary attached graphs in place of complete cliques. It does not claim a new formula for the zero-forcing *number*. No assertion of uniqueness across all mathematical literature or of independent scholarly validation is made; priority assessment is limited to the cited primary texts and searches. Computations check only small graphs; the infinite-family conclusion rests on the proof above.

## References
1. I. Javaid, I. Irshad, M. Batool, Z. Raza, *On the zero forcing number of corona and lexicographic product of graphs*, arXiv:1607.04071 (first posted 2016-07-14), https://arxiv.org/abs/1607.04071.
2. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (first posted 2020-09-01); Discrete Applied Mathematics 2023, https://arxiv.org/abs/2009.00220, https://doi.org/10.1016/j.dam.2023.01.027.

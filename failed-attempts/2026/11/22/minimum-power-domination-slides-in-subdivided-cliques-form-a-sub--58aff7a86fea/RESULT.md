# Minimum power-domination slides in subdivided cliques form a subdivided Johnson graph

## Finding

For every integer \(n\ge 3\), let \(G_n\) be the graph obtained by subdividing each edge of the complete graph \(K_n\) exactly once. Its original vertices are \(v_i\), for \(i\in[n]\); the subdivision vertex of \(v_iv_j\) is \(w_{ij}=w_{ji}\). Power domination starts by observing the selected vertices and all their neighbors, and thereafter allows an observed vertex with exactly one unobserved neighbor to observe that neighbor.

The minimum power-domination number is
\[
\gamma_P(G_n)=n-2.
\]
All minimum power-dominating sets are exactly of these two types:

- **Type A:** \(\{v_i:i\in[n]\setminus\{a,b\}\}\), for an unordered pair \(\{a,b\}\subset[n]\).
- **Type B:** \(\{v_i:i\in[n]\setminus T\}\cup\{w_{ab}\}\), for a three-element set \(T\subset[n]\) and a two-element set \(\{a,b\}\subset T\).

Consequently, the number of distinct minimum sets is
\[
\binom n2+3\binom n3=\binom n2(n-1).
\]
Let \(R_n\) be the graph of these optimal sets under **token sliding**: two sets are adjacent when one selected vertex can be replaced by an unselected *adjacent vertex of \(G_n\)*, with the new set also minimum power dominating. Write \(J(n,2)\) for the Johnson graph whose vertices are two-element subsets of \([n]\), adjacent when they share exactly one element; write \(\operatorname{Sub}(H)\) for the graph obtained by subdividing every edge of \(H\) once. Then
\[
R_n\cong\operatorname{Sub}(J(n,2)).
\]
The slide graph is connected and bipartite with
\[
|V(R_n)|=\binom n2(n-1),\qquad |E(R_n)|=2\binom n2(n-2),
\]
and exact radius and diameter
\[
\operatorname{rad}(R_n)=\min\{n,5\},\qquad
\operatorname{diam}(R_n)=\min\{n,6\}.
\]
For \(n\ge6\), the \(\binom n2\) type-A states have eccentricity five and the \(\binom n2(n-2)\) type-B states have eccentricity six. All vertices have eccentricity \(n\) when \(3\le n\le5\).

## Assumptions and scope

The graphs are finite, simple, and labeled. Each edge of \(K_n\) is replaced by a path of length two; no original edges survive. Initial closed-neighborhood observation is followed by ordinary (one-unobserved-neighbor) forcing, with no bound on the number of forcing rounds. Tokens are indistinguishable, and only slides along edges of the *original subdivided graph* are allowed. The claims concern all integers \(n\ge3\) and optimum-cardinality states only. For \(n=3\), the graph is a six-cycle and the classification still holds.

## Proof

**1. The forest obstruction and criterion.** Consider an arbitrary selected set \(S=O\cup W\), where \(O\subseteq\{v_1,\ldots,v_n\}\) consists of original vertices and \(W\) consists of subdivision vertices. Let \(R\subseteq[n]\) index original vertices not in \(O\). Form a simple graph \(H\) on \(R\) whose edges are exactly those pairs \(\{a,b\}\subseteq R\) for which \(w_{ab}\notin W\).

If \(H\) contains a cycle, each subdivision vertex corresponding to an edge on that cycle is unobserved initially, and remains so: its only neighbors are original vertices; each original vertex on that cycle always has at least two still-unobserved subdivision neighbors belonging to that cycle, so neither can force one. Hence such a set \(S\) cannot power dominate. This obstruction also applies when \(O=\varnothing\), taking \(R=[n]\).

When \(O\ne\varnothing\), the converse holds. For every \(b\in R\), pick \(a\) with \(v_a\in O\). The subdivision vertex \(w_{ab}\) is initially observed and, because \(v_a\) is observed, it can force \(v_b\) if not yet observed. Thus all original vertices are observed after at most one forcing wave. The remaining unobserved vertices are precisely the subdivision vertices representing edges of \(H\). If \(H\) is a forest, an original vertex corresponding to a leaf of a nontrivial component can force its unique remaining unobserved incident subdivision vertex. Removing that edge preserves acyclicity. Repeating peels every edge. Consequently, for \(O\ne\varnothing\), \(S\) power dominates **if and only if \(H\) is a forest**.

**2. Minimum size and complete classification.** Put \(k=|O|\), \(r=n-k\), and \(\ell=|W|\). If \(k\ge1\) and \(r\ge2\), foresthood requires deleting at least
\[
\binom r2-(r-1)=\frac{(r-1)(r-2)}2
\]
edges from \(K_r\). Each such deletion requires a selected subdivision vertex internal to \(R\), so
\[
|S|\ge n-r+\frac{(r-1)(r-2)}2
=n-2+\frac{(r-2)(r-3)}2.
\]
When \(r=0,1\), already \(|O|\ge n-1\). In the remaining cases, the inequality is at least \(n-2\), with equality only for \(r=2\) or \(r=3\). For \(r=2\), equality means \(k=n-2\), \(\ell=0\), giving type A. For \(r=3\), equality means \(k=n-3\), \(\ell=1\), and the chosen subdivision vertex must correspond to an edge internal to the three excluded original vertices, giving type B. The forest criterion proves every listed set succeeds.

If \(k=0\), each initially unselected edge-subdivision vertex of a cycle in \(K_n\) has the same permanent-obstruction property. Thus \(K_n\) with the selected edges deleted must be acyclic; this needs at least \(\binom n2-(n-1)=\binom{n-1}2\) selected subdivision vertices. For \(n\ge4\), this strictly exceeds \(n-2\). For \(n=3\), selecting any one of the three subdivision vertices succeeds by propagation around the six-cycle, and these are precisely the type-B sets. This proves the lower bound, attainment, and exhaustive classification for all \(n\ge3\).

**3. Exact token-slide graph.** Since \(G_n\) is bipartite with original vertices on one side and subdivision vertices on the other, every slide changes the number of selected original vertices by exactly one. Consequently every optimal slide goes between type A and type B, never within a type. Let the A state indexed by an unselected pair \(U\in\binom{[n]}2\) be \(A_U\). For a B state with missing triple \(T=\{a,b,c\}\) and selected subdivision vertex \(w_{ab}\), sliding \(w_{ab}\) onto its endpoint \(v_a\) or \(v_b\) produces exactly the two A states \(A_{\{b,c\}}\) and \(A_{\{a,c\}}\); there are no other slides from that B state. Those two index pairs intersect in the single element \(c\), so form an edge of \(J(n,2)\).

Conversely, every edge of \(J(n,2)\) is a unique pair \(\{a,c\}\), \(\{b,c\}\) with distinct \(a,b,c\); its unique intermediate B state has missing triple \(\{a,b,c\}\) and selected subdivision vertex \(w_{ab}\). Hence the B states are in bijection with the *edges* of \(J(n,2)\), and their only slide neighbors are the corresponding A endpoints. This is precisely the one-subdivision of \(J(n,2)\). Since \(J(n,2)\) is connected, so is \(R_n\). The order, edge count, bipartition sizes, and degrees follow because \(J(n,2)\) has \(\binom n2\) vertices, degree \(2(n-2)\), and \(\binom n2(n-2)\) edges.

**4. Distances, radius, and diameter.** Denote an original Johnson vertex in its subdivision by \(O_x\) and the midpoint of a Johnson edge \(e=uv\) by \(M_e\). For distinct edges \(e,f\),
\[
\begin{aligned}
d(O_x,O_y)&=2d_J(x,y),\\
d(O_x,M_{uv})&=1+2\min\{d_J(x,u),d_J(x,v)\},\\
d(M_e,M_f)&=2+2\min_{u\in e,\,v\in f}d_J(u,v).
\end{aligned}
\]
These formulas are exact, since a path between midpoints must pass through their endpoints, and every Johnson edge has been subdivided. Johnson distances are zero for equal pairs, one for intersecting unequal pairs, and two for disjoint pairs (the last case requires \(n\ge4\)). Thus all distances in \(R_n\) are at most six.

For \(n=3\), \(J(3,2)\cong K_3\), so its subdivision is a six-cycle of radius and diameter three. For \(n=4\), two disjoint Johnson vertices give distance four; every triple of ground labels meets every other triple, bounding all midpoint-to-midpoint distances by four. For each midpoint one can choose a different edge with no common Johnson endpoint, yielding distance four. Hence every state has eccentricity four. For \(n=5\), every original pair has a disjoint three-element ground-label set, so it is five steps from the midpoint supported on that triple; conversely all supported triples intersect, so midpoint-to-midpoint distances are at most four. Every midpoint is five steps from an original pair disjoint from its supporting triple. All states therefore have eccentricity five.

For \(n\ge6\), every original pair is five steps from a midpoint supported on a disjoint ground-label triple, and all original-to-anything distances are at most five. Every midpoint is six steps from one supported on a disjoint triple, and all midpoint distances are at most six. Thus originals have eccentricity five and midpoints six, proving the stated exact radius, diameter, and eccentricity distribution.

## Verification

Two standalone Python 3 scripts provide checks independent of the symbolic argument. `check_small.py` directly enumerates all vertex subsets up to minimum size using integer-bit-mask propagation, tests the complete optimizer classification for \(3\le n\le7\), constructs every legal slide from original graph edges, and computes all-pairs shortest distances. `check_independent.py` independently constructs the graph using standard-library adjacency sets, propagates monitored *sets*, exhaustively identifies minimum sets for \(3\le n\le6\), reconstructs the Johnson-edge bijection through an independently built token-slide graph for \(3\le n\le10\), and checks that bijection again at \(n=12,16\). Both programs terminate with assertions and print the verified finite cases. They corroborate, but do not replace, the all-order proof above.

## Relationship to prior work

Bong, Carlson, Curtis, Haas and Hogben, *Isomorphisms and properties of TAR reconfiguration graphs for zero forcing and other X-set parameters*, arXiv:2205.09668v1 (first posted 19 May 2022), develops the general reconfiguration framework and discusses power domination but studies token addition/removal and does not give minimum power-dominating configurations or token sliding on the fully subdivided clique. Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798v1 (first posted 5 January 2022; open-access expanded 2026 publication), initiates power-domination reconfiguration and explicitly identifies token sliding as a further direction, without stating the family-specific isomorphism proved here.

Related published analyses of subdivided cliques concern different vertex-set predicates, including paired domination and total-domination sequences; their conclusions are not statements about power domination and do not imply the particular optimal slide graph. Direct equivalence, stronger-coverage, and graph-family searches have not located an earlier result proving the Johnson-subdivision identity. This is a best-knowledge priority assessment, not a proof of absolute novelty.

## Limitations

The claimed formula is for simultaneous single subdivision of **every** edge of a complete graph; it does not assert the same result for arbitrary subdivisions or arbitrary base graphs. It concerns only minimum-cardinality power-dominating sets, not the full power-domination polynomial or token-addition/removal graph. The exact minimum-slide metric follows from the isomorphism; no analogous exact unrestricted token-jump metric is claimed. Published results not indexed by the searched services or inaccessible historical sources may affect priority. Independent mathematical validation has not been performed.

## References

1. N. H. Bong, J. Carlson, B. Curtis, R. Haas, and L. Hogben, *Isomorphisms and properties of TAR reconfiguration graphs for zero forcing and other X-set parameters*, arXiv:2205.09668v1, 2022-05-19. https://arxiv.org/abs/2205.09668 . Full text: https://ar5iv.labs.arxiv.org/html/2205.09668 .
2. B. Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798v1, 2022-01-05. https://arxiv.org/abs/2201.01798 . Open access full text: https://link.springer.com/article/10.1007/s44007-025-00187-5 .
3. B. A. Curtis, M. Flagg, and L. Hogben, *TAR reconfiguration for vertex set parameters*, arXiv:2406.05509, 2024-06-08. https://arxiv.org/abs/2406.05509 .

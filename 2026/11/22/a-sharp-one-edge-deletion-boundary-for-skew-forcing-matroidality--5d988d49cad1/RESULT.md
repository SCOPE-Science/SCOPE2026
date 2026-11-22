# A sharp one-edge-deletion boundary for skew-forcing matroidality of bicliques

## Finding
Let \(a,b\ge1\) be integers and let \(G_{a,b}\) be the graph obtained from the simple complete bipartite graph \(K_{a,b}\) by removing one edge. For its skew zero-forcing closure \(\operatorname{scl}_{G_{a,b}}\), the following are equivalent:

1. \(\operatorname{scl}_{G_{a,b}}\) satisfies the matroid exchange axiom on every initial vertex set.
2. \(\min\{a,b\}=1\), or \((a,b)=(2,2)\).

When \(\min\{a,b\}=1\) and \(\max\{a,b\}=m\ge2\), the associated matroid is the direct sum \(U_{m-2,m-1}\oplus U_{0,1}\oplus U_{1,1}\): respectively the nonisolated leaves, the star center, and the vertex isolated by deleting the edge. For \((a,b)=(2,2)\), the graph is \(P_4\) and the associated matroid is \(U_{0,4}\). For \((a,b)=(1,1)\), the graph has two isolated vertices and the matroid is \(U_{2,2}\).

For every \(\max\{a,b\}\ge3\) with \(\min\{a,b\}\ge2\), an explicit exchange obstruction is given below. Thus every such nonexceptional biclique loses skew-forcing matroidality upon deletion of **any single edge**, although the undeleted biclique is matroidal.

## Assumptions and scope
All graphs are finite, simple, and unweighted. A vertex may force its unique unfilled neighbor irrespective of whether the forcing vertex is itself filled. The closure \(\operatorname{scl}_G(S)\) is the terminal filled set from initial set \(S\). The matroid exchange axiom is
\[
 x\in\operatorname{scl}_G(S\cup\{y\})\setminus\operatorname{scl}_G(S)
 \quad\Longrightarrow\quad
 y\in\operatorname{scl}_G(S\cup\{x\}).
\]
The bipartite parts are labelled; the conclusion does not depend on which edge is removed.

## Proof
Relabel the shores so that \(A\) has size \(a\ge3\) and \(B\) has size \(b\ge2\), whenever the graph is in the asserted nonmatroidal regime. Write \(u\in A\) and \(v\in B\) for the missing edge's endpoints. Choose distinct \(w_1,w_2\in A\setminus\{u\}\). Put
\[
 S=A\setminus\{u,w_1,w_2\},\qquad x=u,\quad y=w_1.
\]

First, \(u\notin\operatorname{scl}(S)\). If \(b\ge3\), no forcing occurs: each member of \(B\) has at least two unfilled neighbors in \(A\), and each member of \(A\) has at least two unfilled neighbors in \(B\). If \(b=2\), the only initially possible move fills \(B\setminus\{v\}\), since \(u\) is its unique neighbor and is itself initially unfilled; then the other vertex \(v\) is filled by \(w_1\) or \(w_2\). The three vertices \(u,w_1,w_2\) are still unfilled, and both vertices of \(B\) have at least two unfilled neighbors, so the process stops without filling \(u\).

Second, \(u\in\operatorname{scl}(S\cup\{w_1\})\). Indeed, \(v\) sees only one unfilled neighbor, namely \(w_2\), so it forces \(w_2\). Every vertex in \(B\setminus\{v\}\) now sees only one unfilled neighbor in \(A\), namely \(u\), and forces \(u\). This argument applies for every \(b\ge2\).

Third, \(w_1\notin\operatorname{scl}(S\cup\{u\})\). Initially the only unfilled vertices in \(A\) are \(w_1,w_2\). For \(b\ge3\), no vertex has a unique unfilled neighbor: every vertex in \(B\) sees both \(w_1,w_2\), every vertex in \(A\setminus\{u\}\) sees all \(b\) unfilled vertices of \(B\), and \(u\) sees \(b-1\ge2\) unfilled vertices of \(B\). For \(b=2\), \(u\) first forces the sole vertex of \(B\setminus\{v\}\), and then any member of \(A\setminus\{u\}\) forces \(v\). Both \(B\) vertices are filled, while \(w_1,w_2\) remain unfilled, each adjacent to both vertices of \(B\). No further force is possible. Thus the displayed sets violate exchange.

It remains to inspect the asserted matroidal exceptions. If \(a=1\) and \(b=m\ge2\), the graph is a star with \(m-1\) leaves plus one isolated vertex. The center is always forced, regardless of the initial set; the isolated vertex is never forced unless initially filled; and a leaf not initially filled is forced precisely when all other nonisolated leaves are initially filled. This is exactly the closure of \(U_{m-2,m-1}\oplus U_{0,1}\oplus U_{1,1}\). The symmetric case \(b=1\) is identical. If \(a=b=2\), the graph is a four-vertex path. Both pendant vertices force the two internal vertices from the empty set; the internal vertices then force the pendant vertices. Hence the empty set closes to the whole graph, giving \(U_{0,4}\). If \(a=b=1\), the two vertices are isolated and closure is identity, giving \(U_{2,2}\). These cases exhaust all positive integers \(a,b\).

## Verification
A standard-library Python program \(\texttt{verify.py}\) independently constructs every relevant adjacency relation and computes skew closures by parallel rounds. It exhaustively tests the exchange axiom on every initial subset for all \(a,b\ge1\) with \(a+b\le10\), checks explicit obstructions for all \(3\le a\le40\) and \(2\le b\le40\), and verifies the claimed exceptional direct-sum closure on all initial subsets for stars up to \(m=13\). To replay, run \(\texttt{python3 verify.py}\). The all-order theorem follows from the case analysis above; computation is supplementary.

## Relationship to prior work
Hall, Pfeil and Taylor (2026, arXiv:2611.15741) formulate skew-forcing matroidality and show that this property need not survive arbitrary edge deletion (Theorem 3.4), without classifying single-edge-deleted bicliques. Cooper and Fickes (2023, arXiv:2303.17419, Proposition 3.16) establish a positive matroidal result for undeleted complete bipartite graphs. The current classification resolves exactly which members of this natural dense family retain matroidality after one edge is removed. It is stronger than the general existence of a counterexample and different from a numerical skew-zero-forcing-number determination. Previously known results for all complete multipartite graphs are not claimed as new.

## Limitations
The classification concerns deletion of exactly one edge from a complete bipartite graph, not arbitrary deleted matchings, multigraphs, or arbitrary perturbations of multipartite graphs. Historical priority is provisional because the literature may contain an equivalent unindexed classification.

## References
- D. Hall, S. Pfeil and J. Taylor, *Skew Zero Forcing Matroids*, arXiv:2611.15741 (first public 2026-11-11), especially the exchange axiom and Theorem 3.4. https://arxiv.org/abs/2611.15741
- J. Cooper and G. Fickes, *Zero loci of nullvectors and skew zero forcing in graphs and hypergraphs*, arXiv:2303.17419 (2023), especially Proposition 3.16. https://arxiv.org/abs/2303.17419
- L. M. DeAlba, *Some results on minimum skew zero forcing sets, and skew zero forcing number*, arXiv:1404.1618 (2014), especially complete multipartite skew-forcing-number computations. https://arxiv.org/abs/1404.1618

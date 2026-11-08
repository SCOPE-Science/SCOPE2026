# Diamond-free token sliding and clique-complex homotopy of rook matching reconfiguration graphs

## Finding

For a finite simple graph \(G\) and integer \(k\ge1\), let \(\mathsf{TS}_k(G)\) have the independent \(k\)-subsets of \(V(G)\) as vertices; two states are adjacent when one vertex is replaced by an adjacent vertex of \(G\), preserving independence. Let \(q_t(H)\) count complete \(t\)-vertex subgraphs of \(H\), and let \(N_G[I]\) denote the closed neighborhood of \(I\). For every \(t\ge2\),

\[
q_t(\mathsf{TS}_k(G))=\sum_{I\in\operatorname{Ind}_{k-1}(G)}q_t\bigl(G[V(G)\setminus N_G[I]]\bigr).
\]

If \(G\) is **diamond-free** (has no induced \(K_4\) minus one edge), then \(\mathsf{TS}_k(G)\) is diamond-free as well, and the clique complex of \(\mathsf{TS}_k(G)\) simplicially collapses onto a graph. Thus its integral homology is torsion-free and supported only in degrees zero and one.

Specialize to the rook graph \(R_{m,n}=K_m\square K_n=L(K_{m,n})\), where \(m,n\ge k\ge1\). Write

\[
V_k=\binom{m}{k}\binom{n}{k}k!,\quad
B_k=\binom{m}{k-1}\binom{n}{k-1}(k-1)!,\quad
A=m-k+1,\quad B=n-k+1.
\]

The complete clique polynomial, counting the empty clique, is

\[
\boxed{Q_{m,n,k}(z)=1+V_kz+B_k\left[A((1+z)^B-1-Bz)+B((1+z)^A-1-Az)\right].}
\]

The reconfiguration graph has \(V_k\) vertices, is \(k(m+n-2k)\)-regular, has exactly \(k!\) isolated vertices if \(m=n=k\), and is connected otherwise. Whenever \((m,n)\ne(k,k)\), its clique complex has integral homotopy type

\[
\boxed{\bigvee^{\beta_{m,n,k}}S^1,\qquad
\beta_{m,n,k}=1-V_k+B_k\big[A(B-1)+B(A-1)\big].}
\]

Here a wedge of zero circles means a point. If \(m=n=k\), the clique complex is a discrete set of \(k!\) points. In particular, no positive-degree integral homology occurs except free first homology. The graph is bipartite exactly when \(m-k\le1\) and \(n-k\le1\). Its girth, with \(\infty\) for an acyclic graph, is

\[
\boxed{
\operatorname{girth}=\begin{cases}
3,&\max(m-k,n-k)\ge2,\\
4,&m=n=k+1,\\
6,&\{m-k,n-k\}=\{0,1\}\text{ and }k\ge2,\\
\infty,&\text{otherwise}.
\end{cases}}
\]

On the double-one-spare boundary \(m=n=k+1\), the exact number of distinct unoriented four-cycles is \(V_k k^2/4\). On either one-spare boundary \(\{m,n\}=\{k,k+1\}\), the reconfiguration graph is isomorphic to the classical star-transposition Cayley graph on \(\mathfrak S_{k+1}\), hence has diameter \(\lfloor3k/2\rfloor\). The latter star-graph diameter is pre-existing literature, not a priority claim.

## Assumptions and scope

All graphs are finite, simple, undirected, with labeled vertex sets. A clique is a complete vertex subset; \(q_0=1\). A diamond is an induced four-vertex graph with five edges. For a graph \(H\), its clique complex \(\mathrm{Cl}(H)\) consists of all cliques of \(H\), including the empty face. Reconfiguration states are unlabeled independent sets, not distinguishable tokens. Reconfiguration changes one selected vertex along an edge, keeping set cardinality \(k\). The rook graph represents the cells of an \(m\)-by-\(n\) board, adjacent if in a common row or column. Independent \(k\)-sets are precisely placements of \(k\) mutually nonattacking rooks, or \(k\)-edge matchings of \(K_{m,n}\). Binomial coefficients vanish when the lower index exceeds the upper. Homotopy claims concern the flag/clique complex of the reconfiguration graph, **not** the original rook graph's independence/matching complex.

## Proof

**1. Common-core lemma and all-graph clique identity.** Fix adjacent independent states \(X=I\cup\{u\}\) and \(Y=I\cup\{v\}\) in \(\mathsf{TS}_k(G)\), with \(|I|=k-1\) and \(uv\in E(G)\). A third state \(Z\), adjacent to both, either contains \(I\), or has the Johnson-graph top-triangle form \((I\setminus\{a\})\cup\{u,v\}\). The latter is not independent because \(uv\in E(G)\). Hence every common neighbor of \(X,Y\) is \(I\cup\{w\}\), with \(w\) adjacent to both \(u,v\) in \(G\) and nonadjacent to \(I\). The same core is forced for every vertex of any clique containing \(X,Y\). It is unique because \(X\cap Y=I\). The extra vertices of the clique form a clique in \(G[V\setminus N_G[I]]\), and conversely every such clique gives exactly one clique of states with core \(I\). Summing over independent cores proves the identity for \(t\ge2\). For \(k=1\), the core is the empty set and the identity holds directly.

**2. Diamond transfer.** Suppose \(G\) is diamond-free but \(\mathsf{TS}_k(G)\) has an induced diamond. Let \(X,Y\) be its two degree-three vertices and \(Z,W\) its degree-two vertices. By the lemma, the four states have one common core \(I\) and variable vertices \(u,v,w,x\). Adjacency of \(X,Y,Z\) and \(X,Y,W\) implies \(uv,uw,vw,ux,vx\in E(G)\), while nonadjacency of \(Z,W\) implies \(wx\notin E(G)\). Thus \(G\) contains an induced diamond on \(u,v,w,x\), contradiction. This applies to every \(k\ge1\).

**3. Collapse to dimension one.** In any diamond-free graph \(H\), distinct maximal cliques meet in at most one vertex: if they shared an edge, maximality would give nonadjacent vertices outside the intersection producing an induced diamond. Thus distinct maximal simplices of \(\mathrm{Cl}(H)\) share no edges. For each maximal clique choose an anchor vertex \(a\). In decreasing order of size, pair each face \(\sigma\) not containing \(a\) and having at least two vertices with \(\sigma\cup\{a\}\). These are elementary free-face collapses internal to that maximal simplex, since no face of size at least two is shared with another maximal simplex. They leave just the star edges joining \(a\) to every other vertex of the clique, and its vertices. Performing these collapses separately for all maximal cliques gives a one-dimensional simplicial complex, proving the asserted homotopy type, integral freeness, and higher-homology vanishing.

**4. Rook clique enumeration and homotopy rank.** There are \(V_k\) nonattacking placements. A core of \(k-1\) rooks can be chosen in \(B_k\) ways, leaving \(A\) unused rows and \(B\) unused columns. Its allowed replacement cells induce a rook graph on an \(A\)-by-\(B\) board. For \(t\ge2\), every \(t\)-clique in that board lies in a unique row or column and their number is

\[
A\binom Bt+B\binom At.
\]

Apply step 1 and the binomial theorem to obtain \(Q_{m,n,k}\). Every state can move one of its \(k\) rooks to any of the \(m-k\) vacant rows keeping its column, or to any of the \(n-k\) vacant columns keeping its row, proving regularity. If both sides are saturated there are no moves, giving \(k!\) isolated states. Otherwise the graph is connected: when both sides have vacancies, first exchange occupied rows to the target row set, then use a vacant column to rearrange the injection of occupied rows into columns; when only one side has vacancies, the corresponding row/column exchanges alone generate all injections. Specifically, a vacant column can successively replace the target column of an occupied row, breaking any cycle of incorrect assignments and finally filling the vacancy. The row-only argument is symmetric. Since the rook graph is diamond-free (two distinct maximal row/column cliques share at most one cell), step 3 applies. In the connected case, the clique complex has the homotopy type of a wedge of circles, and evaluating \(Q\) at \(-1\) gives its first Betti number because \(Q(-1)=1-\chi\). Direct substitution yields \(\beta_{m,n,k}=Q_{m,n,k}(-1)=1-V_k+B_k[A(B-1)+B(A-1)]\). The saturated case has \(k!\) isolated points instead.

**5. Bipartiteness and girth.** If either excess \(m-k\) or \(n-k\) is at least two, a core with three possible replacement cells in a common column or row gives a triangle. When both excesses are zero there are only isolates. If exactly one excess equals one and the other zero, list the \(k\) occupied columns (or rows) followed by the one vacant label. This is a permutation of \(k+1\) labels. A legal move exchanges the vacant entry with one occupied entry: exactly a star transposition. This is a bipartite graph (permutation parity), with no four-cycles since two distinct products of two star transpositions cannot be equal, and it contains a six-cycle from any two distinct generators when \(k\ge2\). For \(k=1\) it is an edge. If both excesses are one, augment the matching with its unique missing-row/missing-column pair to a permutation of \(k+1\) labels. Every row slide or column slide composes this permutation with a transposition, so parity gives a bipartition. Choosing any rook and moving it successively between the two available rows and two available columns yields a four-cycle. These cases exhaust all parameters.

**6. Four-cycle census at double one-spare.** At \(m=n=k+1\), each state has exactly \(k\) possible row slides and \(k\) possible column slides. A row slide and column slide (whether on the same rook or different rooks) commute in the sense that the other order leads to one common opposite state, giving a four-cycle. Two different row-slide neighbors cannot have a second common neighbor: the subgraph of row-only moves at fixed columns is a star-transposition Cayley graph with no four-cycle, and a column move changes the free column. The analogous assertion holds for two column-slide neighbors. Thus each state lies on exactly \(k^2\) four-cycles, with each cycle counted at four states, giving \(V_k k^2/4\).

**7. One-spare diameter.** The identification with the star-transposition graph yields its known diameter \(\lfloor3k/2\rfloor\). For completeness, in a permutation of \(k+1\) symbols let \(\ell_0\) be the cycle length containing the distinguished vacant position, and let the other nontrivial cycle lengths be \(\ell_1,\ldots,\ell_r\ge2\). The exact star-transposition word length is \((\ell_0-1)+\sum_i(\ell_i+1)\). An explicit factorization gives the upper bound; multiplying by a star transposition changes this expression by exactly one in absolute value, proving the lower bound. Maximizing the expression gives \(k+\lfloor k/2\rfloor\): use as many disjoint two-cycles away from the vacant position as possible, with one three-cycle if necessary (and treat \(k=1\) directly). This is the classical diameter formula, included to identify the precise boundary graph rather than asserted as a new fact.

## Verification

The accompanying standalone standard-library Python program constructs nonattacking rook placements and legal token slides directly, independently counts **all** cliques via intersection of adjacency sets, checks coefficient-by-coefficient against the polynomial, checks degrees and connectivity, and checks the one-sided boundary diameters and double-one-spare four-cycle census. It also checks the core-clique identity and preservation of diamond-freeness on all labeled graphs of order at most five. Finite tests corroborate, but do not substitute for, the unrestricted combinatorial and collapse arguments above.

Run with `python3 verify.py` from a folder containing the supplied file. No third-party packages or external data are needed.

## Relationship to prior work

Avis and Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding* (first arXiv submission March 31, 2022), establish the general TS framework and prove a common-core observation for triangles (Lemma 2) and other realizability/girth statements. The common-core mechanism used here is closely related to that earlier lemma; no novelty is asserted for that mechanism alone. Their inspected full text does not provide the all-graph clique-count identity, diamond-free transfer, clique-complex collapse, or two-parameter rook clique and homotopy formulas. The rook specialization is distinct from results about the ordinary matching/chessboard complex, which is the independent-set complex of the **input** rook graph. The star-transposition Cayley graph and its diameter have long been known; see Khomyakova and Konstantinova (first publicly published November 19, 2019), and Gregor, Merino, and Mütze (arXiv first posted August 17, 2021). These classical components are acknowledged and excluded from any independent priority claim.

## Limitations

The findings concern token **sliding**, not token jumping or token addition/removal; the clique complex is that of the **reconfiguration** graph and not the original matching complex. The general all-graph identity does not determine connected components or homology for arbitrary input graphs. The full rook specialization assumes complete bipartite root graphs with no forbidden cells. The source comparison is not a proof of publication priority; a differently named reconfiguration graph or an unindexed general graph-topology theorem could cover portions of the result. No independent mathematical audit has been performed.

## References

- D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861, first posted 2022-03-31, https://arxiv.org/abs/2203.16861.
- E. Khomyakova and E. V. Konstantinova, *Catalogue of the Star graph eigenvalue multiplicities*, Arabian Journal of Mathematics, first published online 2019-11-19, https://doi.org/10.1007/s40065-019-00271-z.
- P. Gregor, A. Merino, and T. Mütze, *Star transposition Gray codes for multiset permutations*, arXiv:2108.07465, first posted 2021-08-17, https://arxiv.org/abs/2108.07465.

# Matching-skeleton NOR dynamics on triangular graphs and a doubled rare-defect law

## Finding

For each integer \(n\ge3\), identify the vertices of the triangular graph \(T_n=L(K_n)\) with the labelled unordered pairs \(E_n=\binom{[n]}2\). A configuration is an arbitrary edge set \(S\subseteq E_n\). Simultaneous **open-neighborhood NOR** is
\[
F(S)=\{e\in E_n:\text{no distinct }s\in S\text{ shares an endpoint with }e\}.
\]
In particular, the currently active edge does not block itself. Write \(E(A)=\binom A2\). For an edge matching \(M\), let \(R=[n]\setminus V(M)\), \(m=|M|\), and \(r=|R|\).

**Complete attractor classification.** Fixed configurations are precisely matchings with \(r=0\) or \(r=1\). Every primitive two-cycle, uniquely up to swapping its phases, is one of the following:

* \(M\leftrightarrow M\cup E(R)\), for any matching with \(r\ge3\);
* \(M\cup E(A)\leftrightarrow M\cup E(B)\), for any matching and unordered partition \(A\sqcup B=R\), with \(|A|,|B|\ge3\).

There are no other attractors, and every configuration enters one after **at most one update**, sharply. Put \(a_0=1\) and let \(a_j\) count all simple labelled graphs on a prescribed set of \(j\) vertices, every connected component having order at least three. Its exact formal exponential generating function is
\[
\sum_{j\ge0}a_j\frac{z^j}{j!}
=\exp(-z-z^2/2)\sum_{j\ge0}2^{\binom j2}\frac{z^j}{j!}.
\]
Thus \(a_1=a_2=0\), \(a_3=4\), \(a_4=38\), \(a_5=728\), and \(a_6=26864\).

**Every individual attraction basin.** The two-cycle of the first kind has basin size
\[
\boxed{B(M;R)=1+(m+1)a_r+r a_{r-1}}.
\]
The two-cycle of the second kind has basin size
\[
\boxed{B(M;A,B)=a_{|A|}+a_{|B|}}.
\]
A fixed perfect matching has basin \(m+1\); a fixed near-perfect matching has basin \(1\). Basins include their recurrent states.

Consequently, writing \(h=\lfloor n/2\rfloor\), the number of fixed configurations is
\[
\boxed{E_n=\frac{n!}{2^h h!}},
\]
and the number of primitive temporal two-cycle *orbits* (without spatial quotient) is
\[
\boxed{C_n=\sum_{m=0}^{\lfloor(n-3)/2\rfloor}
\frac{n!}{2^m m!(n-2m)!}
\left(1+\frac12\sum_{k=3}^{n-2m-3}\binom{n-2m}{k}\right)}.
\]
The interior sum is zero if its upper limit is below three.

The distinguished empty/full two-cycle has basin
\[
\boxed{B_n=1+a_n+n a_{n-1}}.
\]
It is uniquely largest for every \(n\ge3\), and attracts more than half of all \(2^{\binom n2}\) initial configurations. With independent fair initial bits its attraction probability satisfies the **doubled rare-defect asymptotic**
\[
\boxed{\frac{B_n}{2^{\binom n2}}
=1-2\binom n2 2^{-(2n-3)}\left(1+O(n2^{-n})\right)}
\qquad(n\to\infty).
\]
The factor two comes from two equally likely leading obstructions: a pair of isolated vertices and an isolated edge component of the auxiliary graph on \([n]\).

## Assumptions and scope

The input is a labelled simple graph \(S\) on the fixed labelled vertex set \([n]\), with isolated vertices permitted. Graph-theoretic vertices of the dynamical network correspond to edges of this complete auxiliary graph. NOR is synchronous and has **open**, not closed, neighborhoods, so the self-coordinate is excluded. Orbits are distinct as labelled temporal orbits; no graph automorphism quotient is imposed. There is no finite-size probabilistic assumption in any counting formula. The probability statement assumes independent Bernoulli\((1/2)\) choices for all \(\binom n2\) initial binary coordinates. The generating-function identity is interpreted formally; no analytic convergence of the series is required.

## Proof

**1. The exact edge-set update.** Regard \(S\) as a simple graph on \([n]\). Let \(I(S)\) consist of its isolated-edge components (connected components of order exactly two); these edges form a matching. Let \(U(S)\) be its isolated vertices. An edge \(e\) has no *other* active edge sharing an endpoint precisely if it is an isolated-edge component of \(S\), or both its endpoints are isolated vertices of \(S\). Therefore
\[
\boxed{F(S)=I(S)\mathbin{\dot\cup} E(U(S))}.
\]
The vertices outside \(V(I(S))\cup U(S)\) are covered by components of order at least three, hence their number is either zero or at least three. This is the only realizability constraint needed for images; conversely any prescribed matching, isolated-vertex set, and remaining graph with all components of order at least three give an input with exactly that image.

**2. Dynamical classification.** The standard general identity \(F^3=F\) holds on any simple undirected graph for open NOR: inclusion \(S\subseteq F^2(S)\) follows because a neighbor of an active vertex is inactive after one update; antitonicity gives \(F^3(S)\subseteq F(S)\), and applying the first inclusion to \(F(S)\) gives its reverse. Thus every image is recurrent and its least period divides two. This well-known universal fact is *not* an originality claim.

Apply the update identity to an arbitrary input whose isolated-edge matching is \(I\), isolated vertices are \(U\), and remaining component-support set is \(W\), with \(|W|=0\) or \(|W|\ge3\). If \(|U|\le1\), the image is \(I\), which is fixed if \(|W|=0\), otherwise paired with \(I\cup E(U\cup W)\). If \(|U|=2\), the image is the matching \(I\cup E(U)\), fixed if \(W\) is empty and otherwise paired with its union with \(E(W)\). If \(|U|\ge3\), the image is \(I\cup E(U)\), paired with \(I\cup E(W)\); here \(W\) is empty or has at least three vertices. These are exactly the stated orbit shapes. Conversely, substituting every displayed shape into the update formula verifies its fixed or swapping behavior. Both shapes have uniquely recoverable isolated-edge matching and either no clique or a unique nontrivial clique component, so there is no duplication except swapping \(A\) and \(B\). The fixed states are maximal independent sets of \(L(K_n)\), equivalently maximal matchings of \(K_n\), which are perfect or near-perfect. The state consisting of two adjacent auxiliary edges is nonperiodic for all \(n\ge3\), proving sharp one-update entry.

**3. Fibre counts and exact basins.** The exponential formula for labelled graphs says all simple graphs have EGF \(G(z)=\sum_{j\ge0}2^{\binom j2}z^j/j!\); components of size one and two each contribute \(z\) and \(z^2/2\). Removing those components gives the displayed EGF for \(a_j\). By Step 2 a basin is the union of the inverse images of its one or two recurrent states.

For a matching \(M\) with \(r\ge3\), the equation \(F(S)=M\cup E(R)\) has exactly the one solution \(S=M\). To obtain \(F(S)=M\), either (i) \(I(S)=M\) and there are zero or one isolated auxiliary vertices in \(R\), giving \(a_r+r a_{r-1}\) possibilities; or (ii) one designated edge \(e\in M\) is absent, its endpoints form the two isolated vertices of \(S\), \(I(S)=M\setminus\{e\}\), and the residual set \(R\) supports only components of order at least three, giving \(m a_r\). The cases are disjoint and exhaustive, proving \(1+(m+1)a_r+r a_{r-1}\).

For a second-kind cycle with \(A,B\) both of size at least three, \(F(S)=M\cup E(A)\) forces \(I(S)=M\), \(U(S)=A\), and the remaining vertices \(B\) to carry a graph counted by \(a_{|B|}\). Interchanging \(A\) and \(B\) contributes \(a_{|A|}\). For a perfect matching, the preimages are the matching itself and the matchings obtained by deleting one of its edges, giving \(m+1\); for a near-perfect matching, only the matching itself maps to it, giving one. This completes every basin fibre calculation.

**4. Orbit counts.** There are \(n!/(2^m m!(n-2m)!)\) matchings with exactly \(m\) edges. Fixed matchings have \(m=\lfloor n/2\rfloor\). A matching with \(r\ge3\) contributes one first-kind cycle and exactly \(\frac12\sum_{k=3}^{r-3}\binom rk\) unordered complementary partitions with both parts at least three. The formulas for \(E_n\) and \(C_n\) follow. Taking \(M=\varnothing\) gives the distinguished basin formula.

**5. Concentration and sharp coefficient.** For a uniformly random initial auxiliary graph \(G(n,1/2)\), the distinguished basin contains the empty graph and precisely those nonempty graphs with no isolated-edge component and at most one isolated vertex. For an unordered pair \(\{i,j\}\), let \(A_{ij}\) be the event that both vertices are isolated, and \(D_{ij}\) the event that their edge forms an isolated component. Each has probability \(2^{-(2n-3)}\): the first requires the absence of \(2n-3\) edges; the second requires one present edge and the absence of \(2n-4\) incident edges. Apart from the empty graph, failure to reach the distinguished cycle is exactly the union of these \(2\binom n2\) events. Distinct pairs of such events with overlapping supports are either incompatible or require at least three prescribed vertices to be isolated, an event of probability at most \(2^{-(3n-6)}\); disjoint supports contribute probability at most \(2^{-(4n-10)}\). Hence the first two Bonferroni bounds give
\[
1-\frac{B_n}{2^{\binom n2}}
=2\binom n2 2^{-(2n-3)}
+O\!\left(n^3 2^{-(3n-6)}+n^4 2^{-(4n-10)}\right).
\]
The empty graph correction \(2^{-\binom n2}\) is smaller than the displayed error for large \(n\). Dividing by the leading term yields the relative \(O(n2^{-n})\) form. The union bound already gives \(B_n/2^{\binom n2}\ge1-2\binom n2 2^{-(2n-3)}>1/2\) for \(n\ge4\), and this lower bound increases with \(n\). At \(n=3\), the exact basin is \(5\) out of \(8\). In every case one basin holds strictly over half the states, so it is uniquely largest.

## Verification

The standalone program `verify_symbolic.py` constructs the theoretical basin dictionary from the matching and clique formulas and independently implements the NOR local rule. It compares every individual basin on \(T_n\), \(3\le n\le6\), including the sharp entrance identity, fixed points, period-two cycles, and distinguished basin. The separately written C++17 program `verify_independent.cpp` enumerates all \(2^{\binom n2}\) configurations through \(n=7\), using precomputed open-neighbor masks and a separately coded matching recursion. It verifies \(F^3(S)=F(S)\) for each configuration and compares its exact observed orbit dictionary with the structural formulas, not merely aggregate totals. Its largest check covers \(2{,}097{,}152\) initial states at \(n=7\). The attached `symbolic_output.txt` and `independent_output.txt` contain actual successful outputs. These finite tests corroborate the symbolic all-length proof; they are not themselves an infinite proof.

## Relationship to prior work

The correspondence between fixed points of the negative-conjunctive (MIS) network and maximal independent sets is established background, as is the universal period-at-most-two fact and the one-update identity for symmetric open NOR. Aledo, Martínez and Valverde (2015) survey general parallel graph dynamical systems and motivate orbit and basin questions. Aracena, Richard and Salinas (2014, and 2015 preprint on conjunctive networks) analyze fixed-state bounds and independent-set relationships, not this complete basin classification. Aledo and collaborators (2020) provide general fixed and periodic point counting methods; those can cover generic periodicity or fixed-point consequences and are not claimed here as new. Gadouleau and Kutner (2024 preprint/2025 journal) formulate the same open-neighbor NOR operation as the MIS network but concentrate on sequential update and fixing-word complexity.

The closest recorded triangular-graph classification uses **closed-neighborhood** NOR, explicitly including each coordinate as an input; it has no fixed states and an exceptional-basin deficit with *one*, rather than two, leading rare-event families. The open-neighborhood rook-graph classification concerns \(L(K_{a,b})\), not \(L(K_n)\); the complete open-neighborhood Kneser-graph classification concerns disjointness adjacency, not intersection adjacency. Their general image methods are relevant but do not imply the displayed matching-skeleton basin spectrum. The present contribution is the simultaneous open-neighborhood triangular-graph matching/clique classification **with exact individual basins**, and the doubled coefficient in its sharp asymptotic; general periods and matching-fixed-point facts are credited rather than repeated as novel.

## Limitations

The result applies to labelled complete-graph line graphs with synchronous open NOR, not to arbitrary line graphs, closed NOR or asynchronous schedules. The generating function is formal. Individual basin sizes are exact, but independent mathematical audit and absolute historical-priority certification are not claimed. The relevant accessible full-text and archived comparisons did not reveal an equivalent exact basin theorem, although unindexed or inaccessible older work could still exist. The case \(n<3\) is outside scope.

## References

1. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), 594294. First publicly posted 24 March 2015, https://doi.org/10.1155/2015/594294.
2. J. Aracena, A. Richard and L. Salinas, *Maximum number of fixed points in AND–OR–NOT networks*, Journal of Computer and System Sciences 80 (2014), 1175–1190, https://doi.org/10.1016/j.jcss.2014.04.025.
3. J. Aracena, A. Richard and L. Salinas, *Fixed points in conjunctive networks and maximal independent sets in graph contractions*, first arXiv 22 July 2015, https://arxiv.org/abs/1507.06141.
4. J. A. Aledo, A. Barzanouni, G. Malekbala, L. Sharifan and J. C. Valverde, *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), article 9708347, https://doi.org/10.1155/2020/9708347.
5. M. Gadouleau and D. C. Kutner, *Generalising the maximum independent set algorithm via Boolean networks*, arXiv:2403.17658 (2024), https://arxiv.org/abs/2403.17658; Information and Computation 303 (2025), 105266.
6. *Basin concentration for closed-neighborhood NOR on triangular graphs* (2026), publicly accessible result: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-basin-concentration-for-closed-neighborhood-nor-on-triangular-gr--4c118cb00c41.
7. *NOR dynamics on rook graphs: rectangles, matchings, and a square-board gap* (2026), publicly accessible result: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-nor-dynamics-on-rook-graphs-rectangles-matchings-and-a-square-bo--c79fc7919f54.
8. *Complete NOR attractors and basin concentration on two-set Kneser graphs* (2026), publicly accessible result: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-nor-attractors-and-basin-concentration-on-two-set-knese--e75c8d277ab3.

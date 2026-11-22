# Local clique factorization of semi-cutting sets at terminal diameter two

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph, and let \(T\subseteq V\) have at least two vertices. Assume every two distinct terminals have graph distance at most two. Set \(U=V\setminus T\), \(e_T=|E(G[T])|\), and \(e_U=|E(G[U])|\). For each \(v\in U\), put \(L_v=N_G(v)\cap T\) and \(d_v=|L_v|\). Define the clique-counting polynomial, including the empty clique,

\[
K_v(w)=\sum_{C\subseteq L_v:\,G[C]\text{ complete}}w^{|C|}.
\]

The full semi-cutting edge-set polynomial is

\[
\boxed{\mathcal S_{G,T}(z)=z^{e_T}(1+z)^{e_U}\prod_{v\in U}\left(\sum_{C\subseteq L_v:\,G[C]\text{ complete}}z^{d_v-|C|}\right).}
\]

Here \(\mathcal S_{G,T}(z)=\sum_{F\subseteq E:\,d_{G\setminus F}(s,t)>d_G(s,t)\,\forall s\ne t\in T} z^{|F|}\), with disconnected terminal pairs after deletion assigned distance \(\infty\). The formula holds even if nonterminal vertices lie in other components of \(G\).

In particular, writing \(\omega_v\) for the maximum clique order of \(G[L_v]\), with \(\omega_v=0\) when \(L_v=\varnothing\), the smallest semi-cutting size is

\[
\delta(G,T)=e_T+\sum_{v\in U}(d_v-\omega_v).
\]

The number of minimum sets equals the product of the numbers of maximum cliques in the graphs \(G[L_v]\). An edge set is inclusion-minimal semi-cutting if and only if it contains all terminal-terminal edges, no nonterminal-nonterminal edges, and for every \(v\in U\), its *surviving* terminal neighbors form an inclusion-maximal clique in \(G[L_v]\). Thus inclusion-minimal sets need not have the same cardinality.

The factorization is universal for clique polynomials: for any finite graph \(H\) with at least two vertices, add a vertex adjacent to every vertex of \(H\), and take \(T=V(H)\). Then

\[
\mathcal S_{G,T}(z)=z^{|E(H)|}\sum_{C\subseteq V(H):\,H[C]\text{ complete}}z^{|V(H)|-|C|}.
\]

For \(H=K_3\sqcup K_3\), this is \(z^9(z^3+6z^2+6z+2)\); the cubic discriminant is \(-108\), so the semi-cutting polynomial need not be real-rooted even on a graph of diameter two.

**Complete multipartite specialization and rigidity.** For \(G=K_{n_1,\ldots,n_r}\) with \(r\ge2\) and positive integer part sizes, let \(p_i\) be the number of terminals in part \(i\), \(q_i=n_i-p_i\), \(Q=\sum_iq_i\), \(a_i=Q-q_i\), \(c=\sum_{i<j}p_ip_j\), and \(h=\sum_{i<j}q_iq_j\). The polynomial is

\[
\boxed{\mathcal S_{G,T}(z)=z^{c+\sum_{i:p_i>0}(p_i-1)a_i}(1+z)^h\prod_{i:p_i>0}(z+p_i)^{a_i}.}
\]

All its roots are nonpositive real numbers, and its positive coefficient span is strictly log-concave whenever it has at least three terms. All inclusion-minimal semi-cutting sets are minimum, their number is \(\prod_{i:p_i>0}p_i^{a_i}\), and the one-edge-swap graph of these minimum sets is the Cartesian product of \(a_i\) copies of \(K_{p_i}\) for each \(i\) with \(p_i>0\). For \(|T|\ge3\), equality in the universal lower bound \(\delta(G,T)\ge |T|-1\) holds for a complete multipartite graph if and only if that graph is a star.

## Assumptions and scope

Graphs are labelled, finite, simple, and unweighted; no connectedness assumption on all of \(G\) is required. The hypotheses demand that every pair of distinct terminals have original distance exactly one or two. An induced subgraph on the empty set is a clique of order zero. A one-vertex graph has clique polynomial \(1+w\); an empty graph on zero vertices has clique polynomial \(1\). For the complete multipartite corollary, the graph is connected because it has at least two nonempty parts. A single-edge swap means removing one deleted edge and inserting one previously undeleted edge, without leaving the set of minimum semi-cutting configurations.

## Proof

**Local characterization.** If two terminals are adjacent, the unique length-one path between them must be destroyed; hence every edge of \(G[T]\) is deleted. If terminals \(s,t\) are nonadjacent, their original distance is two. Every length-two shortest path has one intermediate vertex. If that vertex lies in \(T\), the path is already hit, because both its edges join terminals and were forced deleted. If its intermediate vertex is \(v\in U\), the path survives precisely when both \(s,t\) belong to the set of terminal neighbors still joined to \(v\) after deletion. Therefore no shortest path survives exactly when, for every \(v\in U\), those surviving terminal neighbors contain no nonadjacent pair: equivalently they form a clique in \(G[L_v]\). This proves both necessity and sufficiency, including cases in which the remaining graph disconnects terminals.

**Enumeration and extrema.** Edges partition into terminal-terminal, nonterminal-nonterminal, and disjoint stars of edges from individual \(v\in U\) to terminals. The first group is compulsory; the second is unrestricted, as it cannot occur on a terminal path of length at most two. In each star the surviving terminal neighbors form an arbitrary clique \(C\subseteq L_v\), contributing exactly \(d_v-|C|\) deletions. Multiplying these independent contributions proves the displayed polynomial. Maximizing each \(|C|\) proves the minimum formula and its count. Inclusion minimality forbids unnecessary nonterminal-nonterminal deletions and requires each surviving clique to be inclusion-maximal (otherwise one may restore a deleted incident edge without violating any constraint). Conversely, if each is maximal, every deleted star edge is necessary, and every terminal-terminal edge is necessary; therefore the set is inclusion-minimal.

**Universality and negative-root counterexample.** For the graph obtained from \(H\) by adding a universal vertex \(v\), all terminals belong to \(H\); there is exactly one nonterminal, with \(L_v=T\). Substitution yields the reciprocal clique polynomial formula. When \(H\) is two disjoint triangles, its clique polynomial is \(1+6w+6w^2+2w^3\). The corresponding semi-cutting polynomial equals \(z^9(z^3+6z^2+6z+2)\). Substituting \((a,b,c,d)=(1,6,6,2)\) into the ordinary cubic discriminant \(b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd\) gives \(-108\). Hence the cubic has exactly one real root and two nonreal conjugate roots.

**Complete multipartite factorization.** Each nonterminal \(v\) in part \(j\) sees all terminals outside part \(j\). The induced terminal-neighborhood graph is complete multipartite, so each surviving clique contains at most one vertex from any other terminal part \(i\). Choices for different terminal parts are independent, producing for each such pair \((v,i)\) the factor \(z^{p_i}+p_i z^{p_i-1}=z^{p_i-1}(z+p_i)\) when \(p_i\ge1\). There are \(a_i\) nonterminal vertices outside part \(i\). Exactly \(c\) terminal-terminal edges must be deleted, and the \(h\) nonterminal-nonterminal edges are arbitrary. Multiplication yields the formula. In a minimum set one edge to each nonempty terminal part is retained from every outside nonterminal vertex; these choices give \(\prod_i p_i^{a_i}\) minimum sets. Changing one retained choice exchanges exactly one deleted edge and realizes the stated Cartesian product.

All factors in the multipartite polynomial are nonnegative powers of \(z\), \(z+1\), or \(z+p_i\), so its zeros are nonpositive real numbers. For a degree-\(d\) polynomial with positive coefficients and all real nonpositive roots, Newton's inequalities give \(b_k^2\ge b_{k-1}b_{k+1}\binom d k^2/(\binom d{k-1}\binom d{k+1})\); the binomial ratio exceeds one for each interior index. Removing the initial power of \(z\) proves strict log-concavity throughout its positive coefficient span.

**Sharp equality case.** Let \(t=\sum_i p_i\ge3\). The minimum size is \(c+\sum_{i:p_i>0}(p_i-1)a_i\). If terminals occupy at least three parts, already \(c\ge t\): start from one terminal in each of three parts, when \(c=t=3\), and note that each additional terminal increases \(c\) by at least two; extra nonempty terminal parts do not weaken the inequality. If terminals occupy exactly two parts with counts \(p,q\), then \(c=pq\ge p+q-1=t-1\), with equality only if one count is one. For \(t\ge3\), say \(p=1\) and \(q=t-1\), the additional cost vanishes only if all nonterminal vertices lie in the part with \(q\) terminals; because the singleton terminal part must then have one vertex and no third part may exist, the graph is a star. If terminals occupy one part, the minimum equals \((t-1)\) times the number of vertices outside it, and equality holds only when the entire complement is one vertex, again a star. Conversely, in a star every terminal set with \(t\ge3\) admits exactly \(t-1\) requisite deletions, by the same formula.

## Verification

Run `python3 verify_semicut.py` from a directory containing the extracted script; it uses only the Python standard library. It independently enumerates every graph on at most five labelled vertices and every terminal choice satisfying the distance hypothesis; for each eligible pair it enumerates all edge-deletion subsets and recomputes terminal distances by breadth-first search. The exact factorization agrees in all \(17{,}804\) eligible cases across \(1{,}098\) tested labelled graphs (including disconnected graphs). The verifier checks the seven-vertex nonreal-root example, the exact discriminant, and a nine-vertex multipartite coefficient expansion. The separate `verify_multipartite.py` exhaustively checks a further \(1{,}905\) complete-multipartite graph-terminal configurations of order at most six using independent full distance computations. No finite enumeration is used to infer the unrestricted theorem; its proof is combinatorial.

## Relationship to prior work

Bosek, Serra and Vena introduce the semi-cutting formulation and prove the universal cardinality lower bound, using a characterization by shortest-path edge transversals (arXiv:2611.20287v1, especially Lemma 2.6 and Theorem 4.1). The new result gives an exact factorization, structural description of every inclusion-minimal solution, and clique-polynomial universality for *all terminal-diameter-two instances*. It also completely resolves the exact count, root behavior, optimum exchange structure and equality cases inside the complete multipartite subclass. The earlier edge-geodesic-transversal problem of Prabha, Sandhiya and Manuel (arXiv:2610.36821) hits maximal geodesics of the whole graph, rather than every terminal-pair geodesic; it is a distinct parameter. No claim of full historical priority or independent certification is made.

## Limitations

This result does not extend the factorization to graphs with a terminal pair at distance three or greater; in that regime shortest paths can contain two nonterminals, coupling decisions at different nonterminal vertices. Computing arbitrary local clique factors remains potentially expensive; the theorem does not claim a polynomial-time algorithm for unrestricted input graphs. The negative-root example is not claimed to be smallest. Earlier equivalent formulations outside the inspected sources cannot be fully excluded without independent literature review.

## References

1. B. Bosek, O. Serra and L. Vena, *Structural properties of semi-cutting sets*, arXiv:2611.20287v1, first public 2026-11-15, https://arxiv.org/abs/2611.20287.
2. R. Prabha, B. Sandhiya and P. Manuel, *The Edge Geodesic Transversal Problem*, arXiv:2610.36821v1, first public 2026-10-27, https://arxiv.org/abs/2610.36821.

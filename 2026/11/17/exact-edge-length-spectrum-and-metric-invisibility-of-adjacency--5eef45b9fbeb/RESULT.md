# Exact edge-length spectrum and metric invisibility of adjacency in derangement matching polytopes

## Finding
Let \(n\ge3\) and let \(\mathcal D_n\) be the convex hull, in the usual Frobenius-Euclidean space of real \(n\)-by-\(n\) matrices, of permutation matrices with zero diagonal. Equivalently, this is the perfect-matching polytope of the crown graph obtained by deleting a prescribed perfect matching from \(K_{n,n}\). For \(2\le k\le n\), define
\[
 c_{k,t}=\frac{2k}{2k-t}\binom{2k-t}{t}\quad(0\le t\le k),\qquad
 a_{n,k}=\sum_{j=0}^{n}(-1)^j(n-j)!
 \sum_{t=\max(0,j-n+k)}^{\min(k,j)}
 \binom{n-k}{j-t}c_{k,t}.
\]
Then the number \(E_{n,k}\) of *unoriented polytope edges* of Euclidean length \(\sqrt{2k}\) is exactly
\[
 \boxed{E_{n,k}=\frac12\binom nk(k-1)!\,a_{n,k}.}
\]
There are no other edge lengths. Writing \(E_n=\sum_{k=2}^nE_{n,k}\), one has
\[
 \boxed{E_n\sim\frac{(n!)^2}{2en}.}
\]
For an edge selected uniformly from all \(E_n\) edges, write \(K_n\) for half its squared Frobenius length and \(J_n=n-K_n\). For two independently uniformly selected, distinct vertices, write \(F_n\) for the number of matrix entries occupied by both corresponding perfect matchings (equivalently, the number of agreeing permutation positions). Then
\[
 \boxed{J_n\Longrightarrow\operatorname{Poisson}(1),\qquad F_n\Longrightarrow\operatorname{Poisson}(1),}
\]
and, more strongly, the probability laws of \(J_n\) and \(F_n\) have total-variation distance tending to zero. Thus the entire *discrete Euclidean distance spectra* of a random adjacent pair and of a random distinct vertex pair become asymptotically indistinguishable when distances are indexed by their exact squared deficits \(2n-\|P-Q\|_F^2\). Nevertheless, the probability that two distinct uniformly sampled vertices are adjacent is
\[
 \boxed{\frac{E_n}{\binom{!n}{2}}\sim\frac en,}
\]
where \(!n\) denotes the number of derangements of \(n\) labels. Here the sample in the last display is an unordered pair of distinct vertices, not a pair of independent unconditioned draws.

## Assumptions and scope
The ambient metric is the unscaled Frobenius metric \(\|A-B\|_F^2=\sum_{i,j}(A_{ij}-B_{ij})^2\). Every vertex is indexed by a derangement \(\pi\in S_n\), with matrix \(P_\pi\). The theorem holds for every integer \(n\ge3\), including the one-dimensional case \(n=3\). Its finite formula counts unoriented one-skeleton edges, not arbitrary vertex pairs. All convergence statements use \(n\to\infty\); no rate for the total-variation convergence is asserted.

## Proof
**1. Adjacency and Euclidean length.** The polytope \(\mathcal D_n\) is the face of the Birkhoff polytope defined by its diagonal coordinate equalities \(X_{ii}=0\). A pair \(P_\pi,P_\sigma\) is therefore adjacent in \(\mathcal D_n\) exactly when it is adjacent in the Birkhoff polytope, or, equivalently, when \(\pi^{-1}\sigma\) is one nontrivial cycle with all other points fixed. The latter characterization also follows from the single-alternating-cycle criterion for bipartite perfect-matching polytopes. If the cycle moves \(k\) points, exactly \(k\) ones are deleted and \(k\) ones inserted between the matrices, so \(\|P_\pi-P_\sigma\|_F^2=2k\).

**2. Exact count by a forbidden board.** Choose the support \(S\) of the relative cycle in \(\binom nk\) ways and a cyclic permutation \(\tau\) of \(S\) in \((k-1)!\) ways. The first endpoint is a permutation \(\pi\), and both \(\pi\) and \(\pi\circ\tau\) must avoid the main diagonal. On the \(n-k\) rows outside \(S\), this gives one forbidden diagonal entry per row. On the \(k\) rows inside \(S\), it gives two forbidden entries per row, one from each derangement condition. The incidence bipartite graph of these latter forbidden cells is a cycle of length \(2k\), disjoint from the outside forbidden matching. Thus the forbidden board has rook polynomial
\[
 (1+z)^{n-k}\sum_{t=0}^{k}c_{k,t}z^t.
\]
The standard count of \(t\) pairwise nonincident edges in a cycle of length \(2k\) is \(c_{k,t}=\frac{2k}{2k-t}\binom{2k-t}{t}\): arrange \(t\) selected edges on the labelled circle with a positive gap between consecutive selected edges, then divide by the choice of the designated selected edge. Inclusion–exclusion on forbidden cells yields precisely \(a_{n,k}\) allowed choices of \(\pi\). Each unoriented edge is constructed twice, once from either endpoint. This proves the formula.

**3. Fixed-deficit asymptotics.** Fix \(j\ge0\) and put \(k=n-j\). The forbidden bipartite board in step 2 has \(2n-j\) cells, with maximum row and column degree two. For a uniformly random permutation, let \(H_n\) count occupied forbidden cells. For each fixed positive integer \(r\), the number of ordered \(r\)-tuples of mutually nonattacking forbidden cells is \((2n)^r(1+O_r(1/n))\). The probability that a given such tuple is occupied is \(1/(n)_r\), so
\[
 \mathbb E(H_n)_r\longrightarrow 2^r.
\]
Factorial-moment convergence (or alternating Bonferroni bounds at fixed orders followed by the order limit) gives \(\Pr(H_n=0)\to e^{-2}\). Therefore \(a_{n,n-j}/n!\to e^{-2}\), and
\[
 \frac{2nE_{n,n-j}}{(n!)^2}
 =\frac{n}{(n-j)j!}\frac{a_{n,n-j}}{n!}
 \longrightarrow\frac{e^{-2}}{j!}.
\]
Since \(0\le a_{n,k}\le n!\), the same left-hand expression is bounded above by \(n/((n-j)j!)\) for \(0\le j\le n-2\). This is at most \(2/j!\) when \(j\le n/2\); the sum for \(j>n/2\) is at most \(n\sum_{j>n/2}1/(2j!)=o(1)\). Summation therefore yields \(2nE_n/(n!)^2\to e^{-2}\sum_{j\ge0}1/j!=e^{-1}\), and \(\Pr(J_n=j)\to e^{-1}/j!\) for each fixed \(j\).

**4. Independent-pair distances.** Choose independent uniform derangements \(\pi,\sigma\). For any \(r\) prescribed distinct row indices, and conditional on \(\pi\), the constraint that \(\sigma\) agrees with \(\pi\) on those rows leaves \((n-r)!\) bijections before forbidding fixed points. The remaining forbidden diagonal board is a partial matching with between \(n-2r\) and \(n-r\) cells. Its avoidance proportion tends to \(e^{-1}\), uniformly in the chosen rows and \(\pi\), by fixed-order inclusion–exclusion. Since \(!n/n!\to e^{-1}\), the conditional probability of agreement on all \(r\) rows is \((n-r)!/n!\,(1+o(1))\). Hence the agreeing-position count \(F'_n\) for independent draws satisfies \(\mathbb E(F'_n)_r\to1\) for every fixed \(r\), and so \(F'_n\Rightarrow\operatorname{Poisson}(1)\). Conditioning the vertices to be distinct changes this law by a total-variation amount at most \(1/!n\); therefore \(F_n\Rightarrow\operatorname{Poisson}(1)\).

**5. Total variation and adjacency rarity.** On the countable state space of nonnegative integers, pointwise convergence of two probability mass functions to the same Poisson mass function implies total-variation convergence to each other (truncate at fixed large index, then control the tails). Two vertices sharing exactly \(f\) ones have squared Frobenius distance \(2(n-f)\); this proves the distance-spectrum statement. Finally \(!n\sim n!/e\) and the edge asymptotic from step 3 give \(E_n/\binom{!n}{2}\sim e/n\).

## Verification
The standalone file `verification/check_edge_spectrum.py` uses exact integer arithmetic. It directly enumerates all derangements and every unordered pair for \(3\le n\le7\), independently determines adjacency from the nontrivial cycles of the relative permutation, compares each length class to the forbidden-rook formula, and independently enumerates matchings of the forbidden \(2k\)-cycle for \(2\le k\le6\). It reports `DERANGEMENT_EDGE_SPECTRUM_PASS n=3..7; cycle_rooks k=2..6`. The exact edge totals for \(n=3,4,5,6,7\) are respectively \(1,30,706,20770,835311\). The infinite-limit claims rest on the analytical argument above, not on finite tests.

## Relationship to prior work
The classical single-cycle adjacency characterization of the Birkhoff and bipartite perfect-matching polytopes is assumed, not claimed as new; Behrend's Corollary 26 (2013) and Ito et al. (2019) provide explicit accounts. Torres (2023) studies descriptions and normality of bipartite matching polytopes. The present claim concerns the **complete exact Euclidean edge-length multiplicity sequence of the zero-diagonal face**, its rook-polynomial formula, and the coincidence of its limiting edge-distance and unconditioned vertex-pair distance spectra. General adjacency criteria alone do not determine the count of cycles compatible with two forbidden diagonals, and are not the displayed metric asymptotic. Related earlier research determines distances *to* the derangement face from permutation vertices of the full Birkhoff polytope; this is a different object and statistic from edge lengths *within* the face.

## Limitations
This statement does not characterize individual vertex degrees by cycle type, compute any metric intrinsic volume, or assert a quantitative total-variation rate. The single-cycle criterion and cycle-rook coefficients are established classical ingredients. Exact enumeration only checks small cases; the asymptotic claims rely on the proved combinatorial bounds. Historical priority remains provisional: an unindexed count of adjacent perfect matchings by alternating-cycle length or a previously tabulated crown-graph matching-polytope edge distribution could overlap the exact formula.

## References
- T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi, Y. Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, first arXiv version July 3, 2019, https://arxiv.org/abs/1907.01700 (especially Section 1.1 on the matching-polytope graph).
- R. E. Behrend, *Fractional Perfect b-Matching Polytopes I: General Theory*, first arXiv version January 30, 2013, https://arxiv.org/abs/1301.7356 (especially Corollary 26 on bipartite edge adjacency).
- J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, first arXiv version June 20, 2023, https://arxiv.org/abs/2306.11910 (Sections 2–4 on matching-polytope representations and normality).

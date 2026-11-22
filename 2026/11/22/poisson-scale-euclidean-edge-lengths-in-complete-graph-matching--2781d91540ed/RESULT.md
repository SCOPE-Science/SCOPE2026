# Poisson-scale Euclidean edge lengths in complete-graph matching polytopes

## Finding

For an integer \(n\ge 2\), let \(P_n\subset\mathbb R^{\binom n2}\) be the convex hull of the edge-indicator vectors of all matchings of the complete graph \(K_n\), in the standard orthonormal edge-coordinate metric. Let \(M\) be any matching with \(k\) edges, \(0\le k\le\lfloor n/2\rfloor\), and write \(s=n-2k\) for its number of uncovered vertices. Define the local squared-distance enumerator
\[
H_{n,k}(z)=\sum_{N:\,[\mathbf1_M,\mathbf1_N]\text{ is an edge of }P_n}z^{\|\mathbf1_M-\mathbf1_N\|_2^2}.
\]
Then this polynomial depends only on \(n,k\) and has the exact expansion
\[
\boxed{\begin{aligned}
H_{n,k}(z)={}&\sum_{j=1}^{k}\binom kj2^{j-1}j!\,z^{2j-1}
+s\sum_{j=1}^{k}\binom kj2^jj!\,z^{2j}\\
&+\binom s2\sum_{j=0}^{k}\binom kj2^jj!\,z^{2j+1}
+\sum_{j=2}^{k}\binom kj2^{j-1}(j-1)!\,z^{2j}.
\end{aligned}}
\]
All sums with empty ranges are zero. The four summands count, respectively, alternating paths with two matched endpoints, paths with exactly one uncovered endpoint, paths with two uncovered endpoints, and alternating cycles.

There is a precise high-rank limit. Fix any nonnegative integer \(s\), let \(n=2k+s\), and choose \(N_k\) uniformly among the neighbors of the vertex \(\mathbf1_{M_k}\) for any \(k\)-edge matching \(M_k\). With \(D_k=\|\mathbf1_{M_k}-\mathbf1_{N_k}\|_2^2\),
\[
\boxed{2k-D_k\ \xrightarrow{\mathrm d}\ 2R+B_s,}
\]
where \(R\sim\operatorname{Poisson}(1/2)\), independently of the variable \(B_s\) taking the values \(1,0,-1\) with respective probabilities
\[
\frac1{s^2+s+1},\qquad \frac{2s}{s^2+s+1},\qquad\frac{s(s-1)}{s^2+s+1}.
\]
In particular, the local Euclidean edge length divided by \(\sqrt{2k}\) converges in probability to one. The vertex degree satisfies the sharp equivalent
\[
\deg_{P_n}(M_k)\sim (s^2+s+1)e^{1/2}\,2^{k-1}k!.
\]
For \(s=0\) the limiting squared-length deficit is the positive odd-valued variable \(2R+1\). Thus nearly all the incident edges of a nearly perfect matching perform long alternating exchanges, despite the existence of short-exchange Hamilton listings.

## Assumptions and scope

The graph is the simple, labelled complete graph with \(n\ge2\) vertices. A matching is an arbitrary set of pairwise vertex-disjoint edges, including the empty matching. The polytope uses one orthonormal Euclidean coordinate per graph edge; hence squared distances of incidence vectors equal sizes of symmetric differences. “Neighbor” means adjacent vertex in the actual polytope one-skeleton, not an arbitrarily chosen local-edit graph. The finite polynomial holds for all permitted \(n,k\); the probabilistic limit assumes \(s\) fixed and \(k\to\infty\). The independent random choice in the limit is uniform over all distinct polytope neighbors of \(M_k\), not over alternating paths with their orientations or over all matchings of \(K_n\).

## Proof

**1. Geometric adjacency.** The established matching-polytope adjacency theorem says that two distinct matching vertices are joined by a polytope edge exactly when their symmetric difference is a single alternating path or alternating even cycle (Chvátal; also the exposition of Abreu–Costa–Nascimento–Patuzzi). Every such connected symmetric difference determines a unique neighbor by toggling its edges. Since the coordinates are binary, its number of edges equals its squared Euclidean length.

**2. Classification and exact count.** Fix a matching \(M\) with \(k\) disjoint matched pairs and \(s\) uncovered vertices. A valid alternating path whose end edges belong to \(M\), using \(j\ge1\) matched pairs, is obtained by choosing the \(j\) pairs, ordering them, and orienting each pair, modulo reversing the entire path. There are \(\binom kj2^{j-1}j!\) choices. Its squared edge length is \(2j-1\). When a path has one uncovered and one matched endpoint, choose the uncovered endpoint, order and orient the \(j\ge1\) pairs starting at that endpoint: there are \(s\binom kj2^jj!\) choices, each of squared length \(2j\). When both endpoints are uncovered, choose the unordered pair of uncovered endpoints, order and orient the \(j\ge0\) matched pairs, and account for the reversal of the whole path: there are \(\binom s2\binom kj2^jj!\) paths of squared length \(2j+1\). Finally, an alternating cycle uses \(j\ge2\) selected matched pairs. Their cyclic order and orientation, modulo whole-cycle reversal, give \(\binom kj2^{j-1}(j-1)!\) cycles of squared length \(2j\). In the smallest cases (single matched pair, single uncovered–uncovered edge), these quotient factors still yield the unique un-oriented path correctly. Every alternating path or cycle admissible for a matching belongs to exactly one of these four families: an endpoint incident to a nonmatching edge must be uncovered unless the endpoint is internal to the selected alternating path. Summing the four disjoint families proves the displayed polynomial without double-counting.

**3. Factorial concentration.** Set \(A_{k,j}=\binom kj2^{j-1}j!\) for \(1\le j\le k\), and \(a_k=2^{k-1}k!\). For each integer \(r\) with \(0\le r\le k-1\),
\[
\frac{A_{k,k-r}}{a_k}=\frac1{2^rr!}.
\]
For every \(j\ge1\), the three path-family weights with \(j\) matched pairs are respectively \(A_{k,j}\), \(2sA_{k,j}\), and \(s(s-1)A_{k,j}\). The \(j=0\) uncovered–uncovered contribution is the constant \(\binom s2\). The cycle weight is \(A_{k,j}/j\) for \(j\ge2\). The sum of cycle weights is \(o(a_k)\): for \(j>k/2\), the factor \(1/j\) is at most \(2/k\), while the total relative weight for \(j\le k/2\) is bounded by a vanishing tail of \(\sum_{r\ge0}1/(2^rr!)\). This establishes
\[
\frac{\deg_{P_{2k+s}}(M_k)}{a_k}\longrightarrow (s^2+s+1)e^{1/2}.
\]
It also proves that the probability of choosing a cycle tends to zero.

**4. Joint limit and metric normalization.** Conditioned on any one of the three nonempty path families, the distribution of the defect \(r=k-j\) is proportional to \(1/(2^rr!)\) on its admissible range, apart from the negligible \(j=0\) contribution. Hence \(r\) converges to \(\operatorname{Poisson}(1/2)\). The relative total weights of the three path types converge to \(1:2s:s(s-1)\), and the common defect distribution makes the limiting path type and \(R\) independent. Their squared lengths are \(2(k-r)-1\), \(2(k-r)\), and \(2(k-r)+1\), respectively, proving the stated convergence. It follows that \(D_k/(2k)\to1\) in probability, and therefore also \(\sqrt{D_k}/\sqrt{2k}\to1\). No finite enumeration is used to infer convergence.

## Verification

The included standalone script `verify_matching_metric.py` requires Python 3.9 or later and no nonstandard packages. Run `python3 verify_matching_metric.py` from the directory containing this file. It enumerates all matchings of \(K_n\) for every \(2\le n\le10\), tests adjacency by connectedness of symmetric differences (rather than using the closed count), and compares the full squared-length histogram in all 34 possible matching-size strata against the formula. It additionally checks the exact factorial ratios and numerical high-rank degree equivalent for 15 parameter pairs with \(0\le s\le4\). The observed output was `KCOMPLETE_MATCHING_EDGE_METRIC_PASS (34 exhaustive strata, 15 asymptotic diagnostics)`. The numerical diagnostics do not certify the infinite limit; Steps 3–4 prove it.

## Relationship to prior work

Chvátal's matching-polytope adjacency theorem characterizes edges via connected symmetric differences. Abreu, Costa, Nascimento and Patuzzi (first arXiv version, January 22, 2017) count general admissible alternating paths and cycles to obtain vertex degrees, and establish degree monotonicity for arbitrary graphs. Merino and Mütze (first arXiv version, April 17, 2023) show that all matchings can be listed along polytope edges using alternating paths of length at most three, which provides a geometric contrast to the present uniform-neighbor law. Ito and collaborators (July 3, 2019) study shortest reconfiguration sequences of perfect matchings, a distinct statistic. The present result evaluates **every local Euclidean edge-length multiplicity** for complete graphs and the resulting Poisson-scale high-rank law, not just a scalar degree or the existence of a short-edge traversal. The general adjacency structure is explicitly prior art; no claim of a new adjacency criterion is made.

## Limitations

The result does not address non-complete graphs or arbitrary weighted edge metrics. Its Poisson law is for fixed uncovered count \(s\), not for a randomly sampled matching with a varying uncovered count. It concerns Euclidean distances between endpoints of incident polytope edges, not graph-theoretic shortest-path distances on the one-skeleton. Earlier general alternating-path counting results substantially reduce the required combinatorial groundwork; the historical novelty assessment is limited to the evaluated metric distribution and the asymptotic law. Unindexed equivalent literature cannot be ruled out. Independent mathematical validation is not claimed.

## References

1. V. Chvátal, “On certain polytopes associated with graphs,” *Journal of Combinatorial Theory, Series B* 18 (1975), 138–154. DOI: https://doi.org/10.1016/0095-8956(75)90041-6 .
2. N. Abreu, L. Costa, C. H. do Nascimento and L. Patuzzi, “On the vertex degrees of the skeleton of the matching polytope of a graph,” arXiv:1701.06210 (first public January 22, 2017), https://arxiv.org/abs/1701.06210 .
3. A. Merino and T. Mütze, “Traversing combinatorial 0/1-polytopes via optimization,” arXiv:2304.08567 (first public April 17, 2023), https://arxiv.org/abs/2304.08567 ; *SIAM Journal on Computing* 53 (2024), 1257–1292. DOI: https://doi.org/10.1137/23M1612019 .
4. T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi and Y. Okamoto, “Shortest Reconfiguration of Perfect Matchings via Alternating Cycles,” arXiv:1907.01700 (first public July 3, 2019), https://arxiv.org/abs/1907.01700 .

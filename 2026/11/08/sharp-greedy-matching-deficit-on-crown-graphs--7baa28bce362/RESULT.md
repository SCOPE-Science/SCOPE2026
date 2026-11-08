# Sharp greedy-matching deficit on crown graphs

## Finding

For each integer \(n\ge3\), let \(G_n\) be the crown graph with bipartition \(L=\{\ell_1,\ldots,\ell_n\}\), \(R=\{r_1,\ldots,r_n\}\) and edges \(\ell_i r_j\) precisely when \(i\ne j\). Begin with the empty matching and repeatedly select **uniformly among the currently feasible edges** (edges whose endpoints remain unmatched) until none exists. Denote the resulting matching by \(M_n\) and put \(p_n=\Pr(|M_n|=n-1)\).

**Theorem.** Every run ends with either \(n\) or \(n-1\) selected edges, and for all \(n\ge3\),
\[
0<p_n<\frac{2}{n+1},\qquad
0\le \frac{2}{n+1}-p_n\le
\frac{20}{n(n-1)}\left(H_n-\frac32\right)+\frac{20}{3n(n-1)},
\]
where \(H_n=\sum_{j=1}^n j^{-1}\). Consequently,
\[
\boxed{p_n=\frac2n+O\!\left(\frac{\log n}{n^2}\right),\qquad np_n\longrightarrow2.}
\]
In contrast, let \(\widetilde M_n\) be uniform over **all inclusion-maximal matchings** of the same graph. Writing \(D_k\) for the number of derangements of \(k\) symbols,
\[
\Pr(|\widetilde M_n|=n-1)=\frac{nD_{n-1}}{D_n+nD_{n-1}}\longrightarrow\frac12.
\]
Thus the two natural measures on maximal matchings have sharply different limiting chances of missing a perfect matching: asymptotically \(2/n\) versus \(1/2\).

The finite probabilities are also determined exactly by the rational recurrence below; for instance \(p_3=1/3\), \(p_4=p_5=4/21\), and \(p_6=172/1029\).

## Assumptions and scope

The graph is finite, simple, and has **all** off-diagonal bipartite edges, with all edges treated symmetrically. The greedy procedure samples a *currently eligible edge* uniformly at each successful step, equivalently accepting edges in an independent uniform random global edge order. It is not the distinct procedure that selects a random unmatched vertex and then one of its neighbors. No random input-graph distribution is assumed. The comparison measure is uniform over maximal matchings, not all matchings or only maximum matchings.

## Proof

**1. Possible output sizes.** If a matching leaves \(s\ge2\) unmatched vertices in each part, there must be an admissible edge between the two unmatched sets, because among the \(s^2\) possible cross edges only at most \(s\) are deleted diagonal edges. Hence no matching with fewer than \(n-1\) edges is maximal. With exactly one unmatched vertex in each part, maximality requires their two indices to coincide. Each greedy output is maximal, proving the claimed support.

**2. Exact finite-state chain.** At a stage with \(m\) unmatched left and \(m\) unmatched right vertices, let \(T_m=t\) count labels present on both sides. There are \(m^2-t\) feasible edges. Selecting one deletes two common labels in \(t(t-1)\) cases, one common label in \(2t(m-t)\) cases, and no common label in \((m-t)^2\) cases. Thus the next value has respective probabilities
\[
\frac{t(t-1)}{m^2-t},\qquad
\frac{2t(m-t)}{m^2-t},\qquad
\frac{(m-t)^2}{m^2-t}.
\]
The chain starts at \(T_n=n\) and moves to smaller \(m\). When \(m=2\), its only way to fail is to have \(T_2=1\) and then choose the unique edge joining the two *noncommon* labels, an event of conditional probability \(1/3\). Hence
\[
p_n=\frac13\Pr(T_2=1).
\]
For exact evaluation define \(Q_{1,0}=0\), \(Q_{1,1}=1\), and, for \(m\ge2\),
\[
Q_{m,t}=\frac{t(t-1)Q_{m-1,t-2}+2t(m-t)Q_{m-1,t-1}+(m-t)^2Q_{m-1,t}}{m^2-t},
\]
where a term with zero coefficient is omitted. Then \(p_n=Q_{n,n}\). These identities are exact for every integer \(n\ge2\).

**3. First-moment nearly-martingale.** Put \(U_m=\mathbb E T_m\) and \(Z_m=U_m/[m(m+1)]\). Given \(T_m=t\),
\[
\mathbb E(T_{m-1}\mid T_m=t)=t-\frac{2t(m-1)}{m^2-t}.
\]
An exact rearrangement gives, for \(m\ge3\),
\[
Z_m-Z_{m-1}=\frac{2}{m(m^2-1)}\,
\mathbb E\!\left[\frac{T_m(T_m-1)}{m^2-T_m}\right]\ge0.
\]
Initially \(Z_n=1/(n+1)\), and the first decrement is strictly positive for \(n\ge3\).

**4. Control of collisions of two common labels.** Write \(V_m=\mathbb E[T_m(T_m-1)]\). Conditional on \(T_m=t\ge2\), a specified *ordered pair* of shared labels survives the next chosen edge with probability
\[
\frac{(m-2)^2-(t-2)}{m^2-t}
=1-\frac{4m-6}{m^2-t}
\le\frac{(m-2)^2}{m^2-2}.
\]
It follows that, for every \(2\le m\le n\),
\[
V_m\le n(n-1)\prod_{j=m+1}^n\frac{(j-2)^2}{j^2-2}
\le\frac{5m^2(m-1)^2}{n(n-1)}.
\]
For the final inequality, extract \(\prod_{j=m+1}^n ((j-2)/j)^2=[m(m-1)/(n(n-1))]^2\). The remaining product is bounded above by \(\prod_{j=3}^\infty(1-2/j^2)^{-1}<5\), since
\[
\sum_{j=3}^\infty-\log(1-2/j^2)
\le3\sum_{j=3}^\infty j^{-2}<\frac65<\log5.
\]
The middle sum is below \(2/5\) by convexity and comparison with the integral over \([5/2,\infty)\).

**5. Sharp deficit asymptotic.** Since \(T_m\le m\), the decrement in step 3 is at most
\[
\frac{2V_m}{m^3(m-1)^2}\le\frac{10}{mn(n-1)}.
\]
Summing gives
\[
0\le\frac1{n+1}-Z_2\le\frac{10}{n(n-1)}\left(H_n-\frac32\right).
\]
At \(m=2\), write \(b=\Pr(T_2=2)\). Then \(U_2=\Pr(T_2=1)+2b\) and \(b=V_2/2\le10/[n(n-1)]\). Consequently
\[
p_n=\frac13(U_2-2b)=2Z_2-\frac23b.
\]
The stated explicit upper error bound follows. Also \(p_n>0\) for \(n\ge3\): an \((n-1)\)-edge matching leaving a diagonal nonedge unmatched can be selected as the first \(n-1\) greedy edges with positive probability. Strictness of the upper bound follows from the strictly positive initial decrement in step 3. Finally \(H_n=O(\log n)\) and \(2/(n+1)=2/n+O(n^{-2})\).

**6. Uniform maximal-matching comparison.** Perfect matchings of \(G_n\) are derangements and number \(D_n\). A maximal matching of size \(n-1\) must leave precisely \(\ell_i,r_i\) uncovered for some \(i\); the remaining edges form a derangement of the other \(n-1\) labels, giving exactly \(nD_{n-1}\) such matchings. The exact uniform probability follows. The classical inclusion–exclusion count \(D_k=k!\sum_{j=0}^k(-1)^j/j!\) implies \(D_k/k!\to e^{-1}\), so its probability tends to one half.

## Verification

The accompanying `checker.py` implements both the \((m,t)\)-recurrence and a separate labeled row-mask/column-mask recursion. Their exact rational probabilities agree through eight labels per side; additional exact checks verify the finite formulas, near-martingale inequalities, factorial-moment bounds and derangement probabilities. The included checker runs without external packages. Run `python checker.py` from the directory containing the extracted file. Finite execution checks do not replace the algebraic proof of the infinite asymptotic.

## Relationship to prior work

Mészáros (arXiv:2006.07234, first public June 12, 2020; primary MSC2020 60C05) proves a BK inequality for uniform random matchings of bipartite graphs, a measure distinct from uniform-on-maximal matchings and random-edge greedy sampling. This motivates comparing sampling laws, but does not imply the greedy deficit asymptotic. Arnosti studies RANDOM-EDGE and alternative greedy algorithms on random-input bipartite graphs; the fixed crown-graph analysis here is not a corollary of those average-input comparisons. Dyer and Frieze introduced broad fixed-graph randomized greedy matching guarantees, but the accessible abstract and secondary discussion do not establish the sharp crown asymptotic. None of these works is claimed to introduce the crown graph or the greedy algorithm. The full text of the 1991 paper was not available for a decisive historical-priority comparison.

## Limitations

No claim is made for other nearly complete bipartite graphs, independently weighted edges, random-vertex greedy matching, or the distribution of the complete matching itself. The integer recurrence is exact but not a closed elementary expression. Historical originality remains subject to independent literature review, particularly the inaccessible fixed-graph 1991 paper. Independent mathematical validation has not been performed.

## References

- A. Mészáros, *A BK inequality for random matchings*, arXiv:2006.07234 (first public June 12, 2020); *Combinatorics, Probability and Computing* **32** (2023), 151–157. https://arxiv.org/abs/2006.07234 ; https://doi.org/10.1017/S0963548322000189 .
- N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, 2021 pre-publication version, *Stochastic Systems* **12** (2022), 133–150. https://nickarnosti.com/ResearchPapers/Arnosti_GreedyMatching.pdf ; https://doi.org/10.1287/stsy.2021.0082 .
- M. Dyer and A. Frieze, *Randomized greedy matching*, *Random Structures & Algorithms* **2** (1991), 29–45. https://doi.org/10.1002/rsa.3240020104 .
- E. W. Weisstein, *Crown Graph*, MathWorld, for terminology and the deleted-diagonal bipartite definition. https://mathworld.wolfram.com/CrownGraph.html .

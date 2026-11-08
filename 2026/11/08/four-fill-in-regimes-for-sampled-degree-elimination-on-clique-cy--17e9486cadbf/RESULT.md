# Four fill-in regimes for sampled-degree elimination on clique–cycle joins

## Finding

Consider exact symbolic Cholesky elimination on the graph \(G_{h,m}=K_h\vee C_m\), the join of a clique of \(h\ge1\) vertices (called hubs) and a simple cycle of \(m\ge3\) vertices (called rim vertices). At every elimination, uniformly sample \(q\ge1\) **distinct** remaining vertices (or all remaining vertices if fewer than \(q\) survive), choose a vertex of smallest **current filled-graph degree** within this sample, break ties arbitrarily or uniformly, complete its surviving neighborhood to a clique, and delete it. Let \(F_{h,m,q}\) count the **total number of new, distinct edges**, not the number of arithmetic operations or nonzeros already present. Put

\[
 p_k=\begin{cases}\dfrac{\binom hq}{\binom{h+k}q},&1\le q\le h,\\0,&q>h,\end{cases}
 \qquad \delta_k=\frac{(k-2)(k-3)}2\quad(k\ge4),
 \qquad s_{m,k}=\prod_{j=k+1}^{m}(1-p_j).
\]

An empty product is one. Then the **complete finite-size law** is

\[
 \Pr(F_{h,m,q}=m-3+\delta_k)=s_{m,k}p_k\quad(4\le k\le m),\qquad
 \Pr(F_{h,m,q}=m-3)=\prod_{j=4}^{m}(1-p_j).
\]

All \(\delta_k\) for \(k\ge4\) are distinct and positive. In particular, \(m-3\) is the minimum possible fill, and if \(q\ge h+1\), the fill equals this minimum with probability one for every \(m\ge3\).

For fixed \(h\), let \(m\to\infty\), and define excess fill \(X_{h,m,q}=F_{h,m,q}-(m-3)\). The **number of sampled degree candidates produces four asymptotically distinct mean-excess regimes**:

\[
\begin{aligned}
\mathbb E X_{h,m,1}&=\frac{h}{2(h+2)}m^2+O_h(m),\\
\mathbb E X_{h,m,2}&=\frac{h(h-1)}2m+O_h(\log m) &&(h\ge2),\\
\mathbb E X_{h,m,3}&=\frac{h(h-1)(h-2)}2\log m+O_h(1) &&(h\ge3),\\
\mathbb E X_{h,m,q}&\longrightarrow C_{h,q}\in(0,\infty) &&(4\le q\le h),\\
X_{h,m,q}&=0\text{ almost surely} &&(q>h).
\end{aligned}
\]

The constants in the first three regimes are sharp. The exact finite-\(m\) expectation for one candidate is

\[
\mathbb E X_{h,m,1}=\frac{hm(m-1)}{2(h+2)}-\frac{2hm}{h+1}+3-\frac{h+3}{\binom{m+h}{h}}.
\]

For \(q=1\), the normalized **total fill** has the nondegenerate limit

\[
 \frac{F_{h,m,1}}{m^2}\Longrightarrow Y_h,\qquad
 \Pr(Y_h\le y)=(2y)^{h/2}\quad(0\le y\le\tfrac12).
\]

For each fixed \(2\le q\le h\), the excess instead converges in distribution to a finite-valued, unbounded random variable \(X_{h,q}\). With
\[
 s_{\infty,k}=\prod_{j=k+1}^{\infty}(1-p_j),
\]
its law and sharp heavy tail are
\[
\begin{aligned}
\Pr(X_{h,q}=\delta_k)&=p_k s_{\infty,k}\quad(k\ge4),\\
\Pr(X_{h,q}=0)&=\prod_{j=4}^{\infty}(1-p_j)>0,\\
\Pr(X_{h,q}>t)&\sim\frac{(h)_q}{(q-1)2^{(q-1)/2}}\,t^{-(q-1)/2}\quad(t\to\infty),
\end{aligned}
\]
where \((h)_q=h(h-1)\cdots(h-q+1)\). Thus \(\mathbb E X_{h,q}^{r}<\infty\) **exactly when** \(0<r<(q-1)/2\). In particular, the limiting excess for two and three candidates has infinite mean even though every finite input has finite expected fill.

## Assumptions and scope

The rim is an ordinary simple cycle, including \(C_3=K_3\). The hubs form a clique and are joined to all rim vertices; \(h\) and \(q\) are fixed in the asymptotic statements. Sampling is uniform **without replacement**, refreshed at every pivot, and uses degrees of the *current* fill graph, not the original graph. Equal-degree tie breaking cannot affect the fill distribution because the graph is symmetric in the relevant states. This is **exact** symbolic elimination: every pivot adds all currently missing edges between surviving neighbors. It is not the randomized approximate edge-clique sparsification inside the RCHOL preconditioner.

For an explicit symmetric positive-definite matrix realizing the symbolic count without numerical cancellation, take \(A=I+L(G_{h,m})\), where \(L\) is the unit-weight combinatorial graph Laplacian. Its Schur complements are symmetric positive definite with negative entries on every present off-diagonal edge; an elimination creates strictly negative entries on every newly filled edge. The theorem does **not** quantify factorization runtime, flop count, stability under floating-point cancellation, or preconditioner quality.

## Proof

**1. The only dangerous pivot.** While no hub has been eliminated and at least four rim vertices remain, deleting a rim vertex joins its two rim neighbors, which were nonadjacent, by one new edge. The surviving rim is still a cycle, the surviving hubs still form a clique joined to all rim vertices, and exactly one new edge was added. If there are \(k\ge4\) remaining rim vertices, each hub has degree \(h+k-1\) whereas each rim vertex has degree \(h+2\). The latter is strictly smaller. Therefore a hub is chosen precisely if *all* \(q\) sampled candidates are hubs, with conditional probability \(p_k\) above. If \(q>h\), this event is impossible.

If the first hub is eliminated with \(k\ge4\) rim vertices left, it completes the rim cycle to a clique, inserting exactly \(\binom k2-k=k(k-3)/2\) edges. Every surviving vertex is then part of a clique, so no later pivot adds fill. Before this event, the \(m-k\) rim deletions each added one edge. Consequently the total fill is
\[
(m-k)+\frac{k(k-3)}2=m-3+\frac{(k-2)(k-3)}2.
\]
If no hub is eliminated while at least four rim vertices survive, then \(m-3\) rim eliminations leave a complete graph \(K_{h+3}\), hence exactly \(m-3\) total edges are added. These cases prove the stated event partition, distribution, and minimality.

**2. The exact stopping probabilities.** Starting at \(k=m\), the event that all previous choices were rim vertices has probability \(s_{m,k}\); conditioned on this, the first hub pivot occurs at \(k\) with probability \(p_k\). Multiplying proves the finite law. This argument also covers \(m=3\) by empty products.

**3. One-candidate mean and limit law.** When \(q=1\), pivots constitute a uniform random permutation until the first hub. If \(K\in\{0,\ldots,m\}\) is the number of remaining rim vertices at the first hub, then
\[
\Pr(K=k)=\frac{\binom{h+k-1}{h-1}}{\binom{h+m}{h}},\qquad
\mathbb EK=\frac{hm}{h+1},\qquad
\mathbb E[K(K-1)]=\frac{hm(m-1)}{h+2}.
\]
This is a beta-binomial law. The polynomial \((K-2)(K-3)/2\) agrees with the excess fill except for \(K=0,1\), at which it overcounts by three and one, respectively. Subtracting these two exact masses yields the stated exact mean. Moreover \(K/m\Rightarrow Z\) with \(\Pr(Z\le z)=z^h\) on \([0,1]\). Since \(F_{h,m,1}/m^2-(K/m)^2/2\to0\) uniformly over \(0\le K\le m\), the continuous mapping theorem proves the claimed law for \(Y_h\).

**4. Two or more candidates.** Fix \(2\le q\le h\). As \(k\to\infty\),
\[
 p_k=(h)_q k^{-q}(1+O_h(k^{-1})),\qquad
 \prod_{j=k+1}^{m}(1-p_j)=1+O_h(k^{1-q})
\]
uniformly in \(m\ge k\). Consequently the contribution of the stopping event at \(k\) to the mean excess is
\[
 p_k s_{m,k}\delta_k=\frac{(h)_q}{2}k^{2-q}\bigl(1+O_h(k^{-1}+k^{1-q})\bigr).
\]
Summing this estimate gives respectively linear growth for \(q=2\), logarithmic growth for \(q=3\), and a convergent positive limit for \(q\ge4\), with the stated remainder estimates. For fixed \(k\), the probability of first hub selection at \(k\) converges to \(p_k s_{\infty,k}\); since \(\sum_{k\ge4}p_k<\infty\), the no-hub probability converges to a positive product. These probabilities total one by telescoping survival differences, proving convergence in distribution of the excess. Finally \(p_k s_{\infty,k}\sim (h)_q k^{-q}\), and \(\delta_k\sim k^2/2\); summing this regularly varying discrete tail gives the asserted sharp tail constant and moment cutoff.

## Verification

The standalone standard-library checker `verify.py` independently computes the graph-level pivot transition distribution by enumerating sampled subsets, degree-minimizing choices and exact clique-completion, **without using the stopping-hazard formula**. It compares those exact rational probabilities to the theorem for all \(1\le h\le4\), \(3\le m\le6\), \(h+m\le8\), and every tested \(1\le q\le\min(h+m,5)\). It also enumerates complete vertex permutations in five instances, independently checks the closed one-candidate expectation across \(333\) parameter pairs, and performs finite-scale sanity tests of the asymptotic constants. Running `python verify.py` yields `ALL_PASS 491`; see `verify_output.txt`. These finite tests corroborate the formulas but do not replace the proof for all sizes or the limiting assertions.

For \(h=4,m=20\), the minimum possible fill is \(17\) edges. The exact-law expected total fills (rounded) for \(q=1,2,3,4,5\) are respectively \(114.66600791\), \(46.07021124\), \(21.52865154\), \(17.38124178\), and \(17\). The integer-graph verification is exact; these displayed expectation values are decimals of exact rational sums.

## Relationship to prior work

Fahrbach et al., *Graph Sketching Against Adaptive Adversaries Applied to the Minimum Degree Algorithm* (2018, arXiv:1804.04239), and Cummings, Fahrbach and Fatehpuria, *A Fast Minimum Degree Algorithm and Matching Lower Bound* (2019, arXiv:1907.12119), analyze efficient computation of (approximate) minimum-degree orderings and the fill-graph machinery. Their candidate sampling and data-structure guarantees do not state a fixed-\(q\) uniform candidate-selection law on clique–cycle joins. Chen, Liang and Biros, *RCHOL* (2020, arXiv:2011.07769), sample **clique edges** to create approximate factors; their reported ordering comparisons and reordering heuristics do not yield exact candidate-degree fill probabilities. Rothberg and Eisenstat, *Node Selection Strategies for Bottom-Up Sparse Matrix Ordering* (1998, DOI:10.1137/S0895479896302692), concern different node-order heuristics. The general framework of eliminating a vertex and completing its neighborhood to a clique is established prior knowledge. The contribution assessed here is the **joint finite law, sharp four-regime asymptotics, and limiting heavy-tail moment thresholds for this precisely specified sampled-degree rule**.

## Limitations

The analysis applies to clique–cycle joins with fixed hub count and sampling budget; it does not claim that this particular inexpensive randomized heuristic is competitive with production AMD or nested dissection on general sparse matrices. Underlying graph symmetries drive the exact formulas, so extensions to irregular graphs are open. There is an unresolved publication-precedence risk from specialist elimination-order probability literature that may use different terminology. The independence of an outside mathematical audit has not been established; the analytic proof and independent exact checker are provided for examination.

## References

1. M. Fahrbach, G. L. Miller, R. Peng, S. Sawlani, J. Wang, S. C. Xu, *Graph Sketching Against Adaptive Adversaries Applied to the Minimum Degree Algorithm*, arXiv:1804.04239, first posted 2018-04-11. https://arxiv.org/abs/1804.04239
2. R. Cummings, M. Fahrbach, A. Fatehpuria, *A Fast Minimum Degree Algorithm and Matching Lower Bound*, arXiv:1907.12119, first posted 2019-07-28. https://arxiv.org/abs/1907.12119
3. C. Chen, T. Liang, G. Biros, *RCHOL: Randomized Cholesky Factorization for Solving SDD Linear Systems*, arXiv:2011.07769, first posted 2020-11-16. https://arxiv.org/abs/2011.07769
4. E. Rothberg, S. C. Eisenstat, *Node Selection Strategies for Bottom-Up Sparse Matrix Ordering*, SIAM J. Matrix Anal. Appl. https://doi.org/10.1137/S0895479896302692

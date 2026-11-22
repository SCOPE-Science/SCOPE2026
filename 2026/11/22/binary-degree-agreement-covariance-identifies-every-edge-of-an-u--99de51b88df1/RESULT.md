# Binary degree-agreement covariance identifies every edge of an unknown percolation host

## Finding

**Theorem (binary replica-degree tomography).** Let \(H=(V,E)\) be any finite labelled simple undirected graph, with \(|V|=n\ge2\). For each edge \(e\in E\), fix an arbitrary probability \(0<p_e<1\). Independently generate two bond-percolated graphs \(G^{(1)},G^{(2)}\) on \(V\): in each copy, retain each host edge \(e\) with probability \(p_e\), independently across edges and copies. At vertex \(u\), observe only the bit
\[
 X_u={\bf1}\bigl\{\deg_{G^{(1)}}(u)=\deg_{G^{(2)}}(u)\bigr\}.
\]
Then for distinct \(u,v\),
\[
 \boxed{\quad \operatorname{Cov}(X_u,X_v)>0\ \Longleftrightarrow\ uv\in E;\qquad
 \operatorname{Cov}(X_u,X_v)=0\ \Longleftrightarrow\ uv\notin E.\quad}
\]
Thus the **support of the off-diagonal covariance matrix of one-bit degree-agreement observations exactly reconstructs every edge of the unknown labelled host**, including isolated vertices, with no knowledge of the individual probabilities.

More precisely, for a host edge \(uv\), put \(a_e=p_e(1-p_e)\). For each endpoint \(w\in\{u,v\}\), let \(S_w^{(uv)}\) be the sum of independent signed edge differences on all edges incident to \(w\), excluding \(uv\), where each edge difference has probabilities \(a_e,1-2a_e,a_e\) at \(-1,0,1\). Define
\[
 \Delta_w^{(uv)}=\Pr(S_w^{(uv)}=0)-\Pr(S_w^{(uv)}=1).
\]
Then \(\Delta_w^{(uv)}>0\) and
\[
 \boxed{\operatorname{Cov}(X_u,X_v)
 =2a_{uv}(1-2a_{uv})\,\Delta_u^{(uv)}\Delta_v^{(uv)}.}
\]

**Uniform finite-sample recovery.** Suppose all present-edge probabilities belong to \([\varepsilon,1-\varepsilon]\), where \(0<\varepsilon\le1/2\), and independent experiments each provide a fresh pair of percolated graphs but reveal only the binary vector \(X\). Define
\[
 b_n=\frac{\binom{2n-4}{n-2}}{4^{n-2}(n-1)},\qquad c_n=\varepsilon(1-\varepsilon)b_n^2.
\]
Every actual host edge has covariance at least \(c_n\), while nonedges have covariance zero. For \(0<\delta<1\), from \(m\) independent binary-vector observations, form the empirical covariance (with divisor \(m\)) and declare \(uv\) an edge iff its covariance entry exceeds \(c_n/2\). Then
\[
 \boxed{m\ge 32c_n^{-2}\log\!\frac{2n^2}{\delta}}
\]
is a sufficient sample count for exact simultaneous reconstruction with probability at least \(1-\delta\). In particular, for fixed \(\varepsilon\), this is \(O_\varepsilon(n^6\log(n/\delta))\). No optimality claim is made.

## Assumptions and scope

The labels of all vertices are aligned between the two graphs in each experiment and across repeated experiments. Host edges are independently retained in each copy, with the *same* nondegenerate probability for the same host edge in both copies; edge probabilities may otherwise vary arbitrarily and are not required to be known. Every experiment resamples both graphs afresh. No edges are observed: a sample is an \(n\)-bit vector recording whether the two degree magnitudes agree at each vertex. The theorem concerns labelled undirected simple hosts, not directed graphs, dependent-edge sampling or independently relabelled vertices. The finite-sample result assumes a known lower bound \(\varepsilon\) on every present-edge probability and its complement.

## Proof

**1. Signed differences.** Let \(B_e^{(r)}\in\{0,1\}\) be the retention indicator of edge \(e\) in replica \(r\in\{1,2\}\). Write \(Z_e=B_e^{(1)}-B_e^{(2)}\). By independence,
\[
 \Pr(Z_e=1)=\Pr(Z_e=-1)=a_e=p_e(1-p_e),\qquad
 \Pr(Z_e=0)=1-2a_e.
\]
The variables \(Z_e\) are independent over distinct host edges. Since \(\deg_{G^{(1)}}(u)-\deg_{G^{(2)}}(u)=\sum_{e\ni u} Z_e\), the observable \(X_u\) is exactly the zero-indicator of this signed sum.

**2. Exact pair covariance.** If \(uv\notin E\), the two signed sums involve disjoint edge sets, so \(X_u\) and \(X_v\) are independent. Suppose \(uv\in E\). Set \(Z=Z_{uv}\), \(U=S_u^{(uv)}\), \(W=S_v^{(uv)}\). The three variables \(Z,U,W\) are independent: even when \(u,v\) have common neighbors, they use *distinct* independent edges. Each is symmetric under a sign change. Conditional on \(Z\), the indicators \({\bf1}\{U+Z=0\}\) and \({\bf1}\{W+Z=0\}\) are independent, and their conditional means are \(h_u(0)\), \(h_v(0)\) when \(Z=0\), and \(h_u(1)\), \(h_v(1)\) when \(|Z|=1\), where \(h_w(k)=\Pr(S_w^{(uv)}=k)\). The law of total covariance therefore yields
\[
 \operatorname{Cov}(X_u,X_v)=\operatorname{Var}({\bf1}\{|Z|=1\})
 [h_u(0)-h_u(1)][h_v(0)-h_v(1)],
\]
which is the displayed formula because \(\Pr(|Z|=1)=2a_{uv}\).

**3. Strict central-mass gaps.** Consider any independent sum \(S\) of \(k\ge0\) signed edge differences with respective parameters \(a_1,\ldots,a_k\in(0,1/4]\). Its characteristic function is
\[
 \varphi_S(t)=\prod_{j=1}^k\left(1-2a_j(1-\cos t)\right).
\]
Each factor is nonnegative for all real \(t\), and strictly positive near zero. Fourier inversion for the integer-valued variable gives
\[
 \Pr(S=0)-\Pr(S=1)=\frac1{2\pi}\int_{-\pi}^{\pi}(1-\cos t)\varphi_S(t)\,dt>0.
\]
The empty sum gives gap one, as required. Since \(2a_j\le1/2\), every factor is at least \((1+\cos t)/2=\cos^2(t/2)\). Consequently the gap is bounded below by the gap in the symmetric binomial difference of size \(k\), namely
\[
 \Pr(S=0)-\Pr(S=1)\ge \frac{\binom{2k}{k}}{4^k(k+1)}.
\]
This last identity follows from Vandermonde's identity for the difference of two independent \(\operatorname{Bin}(k,1/2)\) variables and the ratio \(\binom{2k}{k-1}/\binom{2k}{k}=k/(k+1)\). The bound decreases strictly with \(k\), because successive ratios equal \((2k+1)/(2k+4)\). For every endpoint, \(k\le n-2\), so its gap is at least \(b_n\). Since \(0<a_{uv}\le1/4\), the coefficient \(2a_{uv}(1-2a_{uv})\) is at least \(a_{uv}\), which under the stated uniform probability bound is at least \(\varepsilon(1-\varepsilon)\). This proves both strictness and the finite-population lower bound.

**4. Concentration and reconstruction.** From independent observations \(X^{(1)},\ldots,X^{(m)}\), let \(\bar X_u\) be the empirical mean and \(\overline{X_uX_v}\) the empirical pair mean. Define \(\widehat C_{uv}=\overline{X_uX_v}-\bar X_u\bar X_v\). Hoeffding's inequality and a union bound over at most \(n^2\) first and pair means show that, with probability at least \(1-2n^2e^{-2mt^2}\), all empirical means differ from their expectations by at most \(t\). On this event, because all means lie in \([0,1]\), each covariance entry differs from its population value by at most \(3t\). Take \(t=c_n/8\). The prescribed sample count makes the failure probability at most \(\delta\), and the covariance error is at most \(3c_n/8<c_n/2\). Therefore each nonedge is below the threshold and each edge is above it. Stirling's formula gives \(b_n=\Theta(n^{-3/2})\), so \(c_n^{-2}=O_\varepsilon(n^6)\). This completes the proof.

## Verification

The standalone standard-library script `verify.py` independently enumerates every signed-edge difference configuration for all \(78\) host/probability models (all labelled host graphs of orders two through four, plus four selected five-vertex hosts with heterogeneous edge probabilities). It compares exact rational covariances with the conditional formula, checks that their support equals the host edge set across \(450\) pair identities, and checks \(54\) exact binomial lower bounds at independent rational parameter choices. Run `python3 verify.py` in the same directory. The confirmed output is `VERIFY_OK 78 exact host laws, 450 pair covariance identities, 54 gap bounds`. Enumeration is finite evidence; the theorem for arbitrary hosts and the sample bound follow from the general proof above, not from enumeration.

## Relationship to prior work

Bollobás, Janson and Riordan (2005) develop independent-edge inhomogeneous random graphs and study percolation-scale components and degree frequencies; their general matrix of edge probabilities includes the finite model used here. Lyzinski, Fishkind and Priebe (2013) address vertex alignment of correlated Erdős–Rényi graphs using adjacency information; the independent-replica case is a boundary of their model, but they do not recover an unknown host from covariances of equality-of-degree bits. McGregor and Sengupta (2022) reconstruct graphs from vertex-deletion subgraphs or adjacency principal submatrices, not binary replica-degree agreement. Two related graph-covariance inversion results for *vertex-threshold* random subgraphs infer the host from the full real-valued degree-vector covariance under a different, dependent-edge mechanism; those theorems do not give positivity of the covariance of the nonlinear equality bits under independent bond percolation. The classical covariance of raw sampled degrees also identifies the host in independent bond percolation, but observing **only binary equality between two sampled degrees** is a strictly coarser channel; the exact positive-support identity and quantitative recovery for that channel are the present claim.

## Limitations

The result does not recover individual probabilities, hidden vertex permutations, edge-correlated graph models, or a host with deterministic present edges: when \(p_e\) equals zero or one, a host edge may become invisible to equality-bit covariance. The sample-complexity bound is sufficient and likely conservative, not minimax. The observable requires independent paired graph samples and stable vertex labels. Stronger graph-inference results with different observables do not constitute a proof here. Historical novelty remains subject to unindexed literature and independent review.

## References

1. B. Bollobás, S. Janson and O. Riordan, *The phase transition in inhomogeneous random graphs*, arXiv:math/0504589v1, first posted 2005-04-29, Sections 1, 2 and 13, https://arxiv.org/abs/math/0504589.
2. V. Lyzinski, D. E. Fishkind and C. E. Priebe, *Seeded graph matching for correlated Erdős–Rényi graphs*, arXiv:1304.7844v1, first posted 2013-04-30, Sections 1–2, https://arxiv.org/html/1304.7844v4.
3. A. McGregor and R. Sengupta, *Graph Reconstruction from Random Subgraphs*, ICALP 2022, DOI:10.4230/LIPIcs.ICALP.2022.96, Sections 1–2, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2022.96.
4. *Host-graph reconstruction from degree covariance in vertex-threshold subgraphs*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-host-graph-reconstruction-from-degree-covariance-in-vertex-thres--4f959cf417db.
5. *Covariance tomography for vertex-threshold random subgraphs*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-covariance-tomography-for-vertex-threshold-random-subgraphs--b4fe0bc105ae.

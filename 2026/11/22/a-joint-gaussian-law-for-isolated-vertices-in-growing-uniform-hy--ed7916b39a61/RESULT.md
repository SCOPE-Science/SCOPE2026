# A joint Gaussian law for isolated vertices in growing uniform hypergraphs

## Finding
Fix an integer \(k\ge3\), a vertex-birth probability \(p\in(0,1)\), and an initially finite collection of at least \(k\) vertices and distinct \(k\)-uniform hyperedges. Independently at each integer time, add an isolated vertex with probability \(p\), or, with probability \(q=1-p\), add a uniformly sampled previously absent \(k\)-element hyperedge. If no unused hyperedge exists, the latter choice leaves the structure unchanged. Let \(N_t\) and \(I_t\) denote the number of vertices and isolated vertices after \(t\) steps. Put

\[
 r=\frac{p}{p+kq},\qquad \alpha=pr.
\]

Then \(N_t/t\to p\) and \(I_t/t\to\alpha\) almost surely, and

\[
 \frac1{\sqrt t}\begin{pmatrix}N_t-pt\\ I_t-\alpha t\end{pmatrix}
 \ \Longrightarrow\ \mathcal N_2(0,\Sigma),
\]

where the full covariance matrix is explicitly

\[
 \Sigma_{NN}=pq,\quad
 \Sigma_{NI}=rpq+pr(1-r),\quad
 \Sigma_{II}=r^2pq+2pr^2(1-r)
 +\frac{pr(1-r)[2+(k-2)r]}{2-r}.
\]

The convergence holds also at the level of normalized covariance and variance, including \(t^{-1}\operatorname{Var}(I_t)\to\Sigma_{II}\) and \(t^{-1}\operatorname{Cov}(N_t,I_t)\to\Sigma_{NI}\). The matrix is strictly positive definite. For example, with \(k=3\) and \(p=1/2\),

\[
\Sigma=\begin{pmatrix}1/4&5/32\\5/32&41/224\end{pmatrix}.
\]

This exact isolation-fluctuation law holds throughout the whole percolating and nonpercolating parameter ranges, notwithstanding the model's giant-component transition.

## Assumptions and scope
The vertices are labelled by birth order. All hyperedges have exactly \(k\) different endpoints and cannot be repeated. Conditional on an edge step, each still-unused \(k\)-set is equally likely. The finite initial hypergraph is arbitrary; when the set of eligible edges is empty, an edge step is interpreted as a null step. This convention affects only a finite initial stage almost surely, since new vertices are born indefinitely. The parameters \(k,p\) are fixed as \(t\to\infty\). Isolation means incidence to no hyperedge, not membership in a non-giant component. The distinction matters in the percolating regime.

## Proof
Write \(E_t\) for the number of used hyperedges and \(C_t=\binom{N_t}{k}\). The number of used hyperedges is at most the number of edge attempts, so \(E_t\le t+E_0\). The vertex creation indicators are independent Bernoulli\((p)\), hence \(N_t=N_0+\sum_{j=1}^{t}B_j\) and \(N_t/t\to p\) almost surely. In particular, \(E_t/C_t=O(t^{1-k})\) almost surely for all sufficiently large \(t\).

When \(C_t>E_t\), let \(Y_t\) be the number of isolated vertices of the newly added hyperedge. Every used hyperedge contains no isolated vertex; hence its exact conditional distribution, given the current hypergraph and that an edge step occurs, is

\[
 \Pr(Y_t=y\mid\mathcal F_t,\text{edge})
 =\frac{\binom{I_t}{y}\binom{N_t-I_t}{k-y}-\mathbf1_{\{y=0\}}E_t}{C_t-E_t},
 \quad 0\le y\le k,
\]

with invalid binomial coefficients interpreted as zero. Therefore, with \(H_t=C_t/(C_t-E_t)\),

\[
 \mathbb E[Y_t\mid\mathcal F_t,\text{edge}]=k\frac{I_t}{N_t}H_t.
\]

Set \(D_t=I_t-rN_t\), and \(a=kq/p\). The identity \(p(1-r)=qkr\) produces an exact damping equation:

\[
 \mathbb E[D_{t+1}-D_t\mid\mathcal F_t]
 =-\frac{qk}{N_t}D_t+\varepsilon_t,
 \qquad
 \varepsilon_t=-qk\frac{I_t}{N_t}\frac{E_t}{C_t-E_t}.
\]

The equation is used only after the almost-surely finite time when \(C_t>E_t\). On the event \(N_t\ge pt/2\), we have \(|\varepsilon_t|\le C t^{1-k}\), with a deterministic \(C=C(k,p,N_0,E_0)\) for large \(t\). The complementary event has exponentially small probability by a binomial Chernoff bound. The bounded increments and dissipative conditional drift imply \(D_t/t\to0\) almost surely by the Robbins–Siegmund argument for \(D_t/t\), and \(\mathbb E D_t^2=O(t)\), \(\mathbb E D_t^4=O(t^2)\) by expanding the second and fourth conditional moments. More explicitly, the leading terms in those expansions are \(-2qkD_t^2/N_t\) and \(-4qkD_t^4/N_t\), while the bounded-increment remainders are \(O(1)\) and \(O(1+D_t^2)\), respectively. The extra terms from \(\varepsilon_t\) are controlled using \(|D_t|\le N_t\) and the exponentially unlikely small-\(N_t\) event. These estimates establish the stated moment orders by induction. Thus \(I_t/N_t\to r\) almost surely.

Write \(\zeta_{t+1}=B_{t+1}-p\) and

\[
 \eta_{t+1}=D_{t+1}-D_t-\mathbb E[D_{t+1}-D_t\mid\mathcal F_t].
\]

These are uniformly bounded martingale differences. Since the hypergeometric sampling law tends to \(\operatorname{Bin}(k,r)\), the predictable covariance matrix of \((\zeta_{t+1},\eta_{t+1})\) converges almost surely to

\[
 Q=\begin{pmatrix}
 pq&p(1-r)\\
 p(1-r)&p(1-r)[2+(k-2)r]
 \end{pmatrix}.
\]

For example, \(Q_{12}=\mathbb E[B(\Delta I-r\Delta N)]=p(1-r)\) in the limit because the limiting mean of \(\Delta D\) is zero. For the bottom-right entry use the binomial second moment and \(qkr=p(1-r)\).

The centered recursion becomes, for sufficiently large \(t\),

\[
 D_{t+1}=(1-a/t)D_t+\eta_{t+1}+R_t,
 \qquad R_t=qkD_t\left(\frac1{pt}-\frac1{N_t}\right)+\varepsilon_t.
\]

The fourth-moment bounds, binomial concentration, and Cauchy–Schwarz give \(\|R_t\|_2=O(t^{-1})\). In the resulting stable linear recursion, the cumulative effect of these remainders is \(O(\log t)\) in \(L^2\), hence \(o(\sqrt t)\). The homogeneous initial term is also \(o(\sqrt t)\). For times \(j\) proportional to \(t\), the deterministic propagation weights converge uniformly to \((j/t)^a\); the finitely many early indices contribute negligibly. A bounded-increment martingale triangular-array central limit theorem now yields the joint normal limit of \((N_t-pt,D_t)/\sqrt t\), with covariance

\[
 \widetilde\Sigma=\begin{pmatrix}
 pq&Q_{12}/(a+1)\\
 Q_{12}/(a+1)&Q_{22}/(2a+1)
 \end{pmatrix}
 =\begin{pmatrix}
 pq&pr(1-r)\\
 pr(1-r)&\frac{pr(1-r)[2+(k-2)r]}{2-r}
 \end{pmatrix}.
\]

Indeed the entries are integrals of the predictable covariance against the weights \(1,s^a,s^{2a}\) on \([0,1]\). Since \(I_t=rN_t+D_t\), a deterministic linear transformation gives the claimed \(\Sigma\). The martingale isometry and the \(o_{L^2}(\sqrt t)\) bound also establish convergence of normalized covariance matrices. The limiting \(Q\) is positive definite because the birth indicator and conditional random hyperedge isolate count are not almost-surely affinely dependent when \(0<p<1\), \(k\ge3\), and \(0<r<1\). Positivity persists under positive-weight integration and the invertible change of coordinates; hence \(\Sigma\) is positive definite.

## Verification
The standalone file `checker.py` runs exact rational dynamic programming for the lumped state \((N_t,I_t,E_t)\), checks conservation and finite-time covariance identities, tests strict positivity of the proposed limiting covariance for rational parameter grids, verifies the Lyapunov relations, and checks the example \(\Sigma_{II}=41/224\). It passed 1,412 exact-arithmetic assertions in the recorded execution. The optional `simulation.py` uses a seeded exact no-repeat sampling mechanism for 16,000 repetitions over 1,200 steps and compares empirical covariance with the proposed formula for three parameter pairs. Its relative deviations were below 1.6% in that execution. These finite tests check implementation and coefficients; they are not proofs of the infinite-time assertion.

Run with `python checker.py`; if NumPy is available, run `python simulation.py` as an additional stochastic sanity check.

## Relationship to prior work
Krapivsky, *Randomly growing uniform hypergraphs*, arXiv:2611.14824v1 (2026), defines the same growth mechanism, gives the asymptotic singleton frequency, and explicitly notes that fluctuation variances of isolated vertices are not known in that analysis (Section II). Its Section V treats general uniformity \(k\), but does not state the joint central limit theorem or the explicit variance coefficient established here. Standard martingale central limit and stochastic approximation methods provide general techniques; the model-specific two-coordinate isolation projection and closed variance coefficient constitute the proposed additional result. Betken's 2019 isolated-vertex CLT concerns a different preferential-attachment graph where every new vertex independently connects to earlier vertices; it does not imply these formulas. The fixed-edge random-hypergraph isolation and overlap-covariance results address an ensemble with a fixed vertex population, not the randomly growing vertex population in this theorem. A prior calculation of duplicate-edge attempts in the same growing model does not determine isolation fluctuations.

## Limitations
The claim concerns only fixed \(k\ge3\), fixed \(0<p<1\), and a finite initial configuration. It does not give quantitative normal-approximation rates, large-deviation estimates, distributions of non-singleton clusters, or limits when \(k\) or \(p\) changes with time. The exhaustion convention resolves otherwise undefined early edge attempts and does not influence the limit. Historical priority has not been conclusively determined; stochastic approximation literature could contain a more general result that subsumes some statements. Independent external mathematical assessment has not occurred.

## References
1. P. L. Krapivsky, *Randomly growing uniform hypergraphs*, arXiv:2611.14824v1, first submitted 2026-11-10, https://arxiv.org/html/2611.14824v1.
2. C. Betken, *A central limit theorem for the number of isolated vertices in a preferential attachment random graph*, arXiv:1910.02668, 2019, https://arxiv.org/abs/1910.02668.
3. M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, Journal of Applied Probability, 2018, https://doi.org/10.1017/jpr.2018.9.
4. H. Robbins and D. Siegmund, *A convergence theorem for nonnegative almost supermartingales and some applications*, 1971.

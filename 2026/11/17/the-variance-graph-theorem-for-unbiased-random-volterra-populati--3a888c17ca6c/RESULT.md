# The variance-graph theorem for unbiased random Volterra population maps

## Finding

Let \(G\) be any finite simple graph representing the pairs of species whose competitive interaction fluctuates independently. In the unbiased, bounded, independent-edge Volterra dynamics defined below, **every population trajectory converges almost surely**. Its limiting support is an independent set of \(G\), and the set of **all stationary probability laws** is exactly the set of probabilities supported on the union of the corresponding simplex faces. In particular,

\[
\boxed{\text{Fixation at a single species for every initial state}\quad\Longleftrightarrow\quad G=K_m.}
\]

When \(G\) is complete, the winning species \(I\) satisfies the exact fixation law \(\Pr_x(I=i)=x_i\); every losing species has an explicit negative pathwise extinction exponent determined by its one-edge noise distribution. The graph criterion is sharp: if one edge is missing, a nonvertex population supported on the two nonadjacent species is fixed under every realization.

## Assumptions and scope

Fix \(m\ge2\) and \(\rho\in(0,1)\). For every unordered pair \(\{i,j\}\), \(1\le i<j\le m\), choose a real random variable \(\xi_{ij}\) satisfying \(\mathbb E\xi_{ij}=0\) and \(|\xi_{ij}|\le\rho\) almost surely. The variables belonging to different pairs are independent; at each generation their entire collection is resampled independently with the same law. Zero-variance pairs may equivalently be omitted. Define \(\xi_{ji}=-\xi_{ij}\), \(\xi_{ii}=0\), and the graph

\[
G=\bigl(\{1,\ldots,m\},\{\{i,j\}:\ v_{ij}=\mathbb E\xi_{ij}^{2}>0\}\bigr).
\]

Starting with any deterministic \(x\) in the probability simplex \(\Delta_{m-1}\), define

\[
X_{n+1,i}=X_{n,i}\left(1+\sum_{j=1}^{m}\xi_{ij}^{(n+1)}X_{n,j}\right),\qquad X_0=x.
\]

This is a Volterra quadratic stochastic operator at every realization: for \(i\ne j\), its two nonzero parental offspring coefficients are \((1+\xi_{ij})/2\) and \((1-\xi_{ij})/2\). The bound \(\rho<1\) ensures every initially positive coordinate remains positive at every finite time.

Write \(\mathcal F(G)=\bigcup_{S\text{ independent in }G}\{z\in\Delta_{m-1}:\operatorname{supp}(z)\subseteq S\}\). This is a finite closed union of simplex faces, not necessarily convex.

## Proof

**1. Exact martingale and variance identities.** Skew-symmetry gives \(\sum_iX_{n+1,i}=\sum_iX_{n,i}=1\), while \(|\sum_j\xi_{ij}^{(n+1)}X_{n,j}|\le\rho\); hence all iterates stay in the simplex. Conditional centering gives

\[
\mathbb E[X_{n+1,i}\mid\mathcal F_n]=X_{n,i}.
\]

Thus every coordinate is a bounded martingale and converges almost surely and in \(L^1\), yielding a limit \(X_\infty\in\Delta_{m-1}\). For \(H(z)=\sum_i z_i^2\), independence of different edge noises implies the exact *conditional* identity

\[
\boxed{\mathbb E[H(X_{n+1})-H(X_n)\mid\mathcal F_n]
=2\sum_{\{i,j\}\in E(G)}v_{ij}X_{n,i}^2X_{n,j}^2.}\tag{1}
\]

No unspecified remainder appears: the centered cross-covariances vanish, and every unordered edge contributes once from each endpoint.

**2. Classification of all almost-sure limits.** Since \(H\le1\), summing expectations of (1) gives

\[
\sum_{n=0}^{\infty}\sum_{\{i,j\}\in E(G)}v_{ij}\,\mathbb E[X_{n,i}^{2}X_{n,j}^{2}]\le\tfrac12.
\]

For any edge \(\{i,j\}\), the nonnegative summands have a finite sum, so \(\mathbb E[X_{n,i}^2X_{n,j}^2]\to0\). The bounded almost-sure convergence of the coordinates and dominated convergence imply \(X_{\infty,i}X_{\infty,j}=0\) almost surely. This holds simultaneously on every edge; therefore \(X_\infty\in\mathcal F(G)\) almost surely.

Conversely, if \(z\in\mathcal F(G)\), every active pair has at least one zero coordinate. Because a zero-variance centered variable is identically zero, the update fixes every positive coordinate of \(z\), and zero coordinates remain zero. Thus **every point of \(\mathcal F(G)\) is fixed under every random operator**. The limit classification is exact as a set of attainable limiting states: choosing \(X_0=z\in\mathcal F(G)\) attains any such \(z\).

**3. Classification of stationary distributions.** If \(\mu\) is any stationary Borel probability for the random-update Markov kernel, integrate (1) against \(\mu\). Stationarity makes the left side zero, and every term on the right is nonnegative. Since every \(v_{ij}\) on an edge is strictly positive, \(\mu\bigl(\{z:z_i z_j>0\}\bigr)=0\) for each edge. Finitely many edges give \(\mu(\mathcal F(G))=1\). Conversely every probability supported on \(\mathcal F(G)\) is stationary because that set is fixed pointwise. This proves the entire invariant-probability classification, not only existence of some stationary measures.

**4. Sharp complete-graph threshold.** If \(G=K_m\), all independent sets have size at most one, so \(X_\infty=e_I\) almost surely. Bounded martingale conservation then gives

\[
\mathbb P_x(I=i)=\mathbb E[X_{\infty,i}]=x_i.
\]

If \(G\) is not complete, choose a nonedge \(\{i,j\}\). Every nontrivial mixture \(t e_i+(1-t)e_j\) with \(0<t<1\) belongs to \(\mathcal F(G)\) and never changes. Hence the assertion of vertex fixation *for every initial state* fails. In particular, knowing only that the interaction graph is connected is insufficient.

**5. Exact selection law for complete multipartite variance graphs.** Suppose \(G\) is complete multipartite with nonempty parts \(V_1,\ldots,V_r\), with every cross-part pair an edge and no within-part edges. Every independent set is contained in exactly one part. Consequently the limiting population is supported on one random part \(V_J\). Each part total \(Y_{n,a}=\sum_{i\in V_a}X_{n,i}\) is a bounded martingale. Since \(Y_{\infty,a}\) is one if \(J=a\) and zero otherwise, \(\mathbb P_x(J=a)=\sum_{i\in V_a}x_i\). In the three-species path \(1\! -\!2\! -\!3\), this gives exact selection probability \(\mathbb P_x(X_\infty=e_2)=x_2\), with complementary probability \(1-x_2\) of landing somewhere on the stationary edge joining species 1 and 3. The distribution *within* that edge is not asserted to be deterministic.

**6. Pathwise extinction exponents when \(G=K_m\).** Suppose now \(x_i>0\) for all \(i\). Fix distinct indices \(i,j\). On the event \(I=i\), all coordinates remain positive at finite times and

\[
\log X_{n,j}-\log x_j=\sum_{k=1}^{n}\log\left(1+\sum_{\ell}\xi_{j\ell}^{(k)}X_{k-1,\ell}\right).
\]

Because both logarithm arguments lie in \([1-\rho,1+\rho]\), the difference between its \(k\)-th summand and \(\log(1+\xi_{ji}^{(k)})\) is at most \(2\rho(1-X_{k-1,i})/(1-\rho)\). Cesàro averaging makes the total difference divided by \(n\) tend to zero on \(I=i\). The ordinary strong law for the i.i.d. single-edge sequence therefore gives simultaneously for all losers

\[
\boxed{\lim_{n\to\infty}\frac1n\log X_{n,j}
=\gamma_{ji}:=\mathbb E\log(1+\xi_{ji})<0\qquad(j\ne I).}\tag{2}
\]

Strict negativity follows from strict Jensen since \(\mathbb E\xi_{ji}=0\) and \(v_{ij}>0\). For independent fair signs of magnitudes \(a_{ij}\in(0,1)\), (2) reduces to \(\gamma_{ji}=\frac12\log(1-a_{ij}^2)\). No independence between the winner event and the individual signs is assumed; the strong-law event has probability one before conditioning.

## Verification

`check_variance_graph.py` uses exact rational arithmetic on dimensions \(m=2,3,4\), with several empty, sparse, and complete variance graphs and multiple boundary and interior initial states. It exhaustively sums \(416\) finite independent-sign realizations to verify simplex preservation, coordinate conditional expectations, the exact quadratic-variation identity (1), and pointwise invariance of independent-set faces. A separate exact calculation verifies that the same cyclic three-species interaction has a fixed positive interior point under *perfectly correlated* global sign reversal, but positive conditional quadratic variation under independent edge reversal. Invoke `python check_variance_graph.py`. These finite checks are not substitutes for the martingale convergence theorem or the strong law used in the proof.

## Relationship to prior work

Adilova, Jamilov and Reinfelds (2023) motivate discrete population propagation via quadratic stochastic operators and classify trajectories in specific deterministic models. Their paper assigns primary classification 37N25; it does not state a random independent-edge variance-graph theorem.

Jamilov, Scheutzow and Wilke-Berenguer (2014, Theorem 3.1) prove vertex convergence for certain random Volterra operators. Their crucial assumption requires the law to give positive probability to an operator with \((Vx)_k=x_k^2\) for each species \(k\), equivalently requiring corresponding interaction entries equal to \(-1\). Here all interaction coefficients are bounded in modulus by \(\rho<1\), so that hypothesis is not satisfied. Their theorem does not imply the stationary independent-face classification or the exact fixation and extinction laws here.

Under a different noise convention, reversing a *single common cyclic skew matrix* by one global fair sign leaves its positive kernel composition fixed. Independent edge noises of positive variance, even when they have the same zero mean and the same pairwise coefficient magnitudes, eliminate that nonvertex stationary state. Thus the source of correlation in the random environment matters, not only the mean operator and individual edge intensities.

## Limitations

The classification requires edge-centered noise, temporal resampling, finite species number, a uniform \(\rho<1\), and uncorrelated (here independent) edge fluctuations. It does not classify biased random interaction means, correlated edge noises, infinite species, or convergence *rates* when the variance graph is incomplete. For a general incomplete graph, the law on surviving independent-set faces need not be a simple discrete mixture, although its coordinate means remain the starting masses. The theorem concerns random operator evolution of population fractions, not finite-population demographic sampling. An equivalent but unindexed theorem may exist; publication priority is not independently established.

## References

1. F. Adilova, U. Jamilov and A. Reinfelds, *On Discrete-Time Models of Network Worm Propagation Generated by Quadratic Operators*, Mathematical Modelling and Analysis 28 (2023), 194–217. https://doi.org/10.3846/mma.2023.15999 . First verified public date: 2023-03-21.
2. U. U. Jamilov, M. Scheutzow and M. Wilke-Berenguer, *On the Random Dynamics of Volterra Quadratic Operators*, arXiv:1401.7840 (2014), https://arxiv.org/abs/1401.7840 .

# Exact star-graph tuning of random-forest trace control variates and a factor-two gap

## Finding
For the unit-weight star with one hub and \(k\geq1\) leaves, the rooted-forest regularization parameter \(q>0\), and the trace estimator \(T_\alpha\) specified below, the unique variance-minimizing scalar control coefficient is
\[
\alpha_*(k,q)=\frac{q(k+2q+1)}{2kq+k+2q^2+4q+3}.
\]
The result gives exact finite-parameter variances, not only an optimizer. For the commonly used mean-degree setting
\[
\alpha_{\mathrm{av}}(k,q)=\frac{q}{q+2k/(k+1)},
\]
consider the integer sequence \(q=Q\), \(k=Q^2\), \(Q\to\infty\). The *variance ratios to the raw number-of-roots estimate* satisfy
\[
\frac{\operatorname{Var}(T_{\alpha_*})}{\operatorname{Var}(R)}\longrightarrow\frac12,
\qquad
\frac{\operatorname{Var}(T_{\alpha_{\mathrm{av}}})}{\operatorname{Var}(R)}\longrightarrow1.
\]
Thus, on this explicit highly inhomogeneous family, the mean-degree setting becomes asymptotically ineffective while optimal tuning still halves the variance. The equivalent ratio of the heuristic variance to the optimal variance tends to \(2\). For \(k=1\), the optimum has exactly zero variance; for all \(k\ge2\) the optimal variance is strictly positive.

## Assumptions and scope
Let \(G\) be the unweighted simple star \(K_{1,k}\), \(k\in\mathbb N\), with hub vertex \(0\) and leaves \(1,\ldots,k\). Let \(L\) be its combinatorial graph Laplacian, \(I\) the identity, and \(K=q(L+qI)^{-1}\) for a real \(q>0\). A rooted spanning forest \(\Phi\) assigns probability proportional to \(q^{R(\phi)}\) to each oriented forest, where each component is oriented toward its root and \(R(\phi)\) counts its roots. Every edge has weight one. Its normalizing constant is
\[
Z=q(q+1)^{k-1}(q+k+1).
\]
Write \(r_\phi(i)\) for the root of vertex \(i\) and define the random matrix \(S(\phi)_{ij}=\mathbf1\{r_\phi(i)=j\}\). Then \(\mathbb ES=K\), \(R=\operatorname{tr} S\), and the trace-level control variable and estimator are
\[
C=\operatorname{tr}(K^{-1}S)- (k+1),\qquad
T_\alpha=R-\alpha C
=\operatorname{tr}\bigl(S-\alpha(K^{-1}S-I)\bigr),\quad\alpha\in\mathbb R.
\]
Both \(R\) and \(T_\alpha\) are unbiased for \(\operatorname{tr}K\). The optimizer is over all fixed real scalar coefficients for this **particular trace control variable**, not over arbitrary trace estimators, graph algorithms, or data-dependent coefficients. Distinct independent forests reduce the variance by their sample count; all ratios below are per sample.

## Proof
**Complete forest decomposition.** Exactly two disjoint cases exhaust the oriented rooted forests. In case A the hub is a root. Each of its \(k\) leaves independently either is a root (weight \(q\)) or points to the hub (weight one). Case A has total weight \(q(q+1)^k\) and probability \((q+1)/(q+k+1)\). Writing \(J\sim\operatorname{Bin}(k,q/(q+1))\) conditional on A, one has \(R=1+J\). In case B the hub points toward one of the \(k\) leaves, which is therefore a root; each of the other \(k-1\) leaves independently is rooted or points to the hub. This case has weight \(kq(q+1)^{k-1}\) and probability \(k/(q+k+1)\). With \(H\sim\operatorname{Bin}(k-1,q/(q+1))\) conditional on B, one has \(R=1+H\).

**Control statistic.** Since \(K^{-1}=I+L/q\), the identity
\[
\operatorname{tr}(LS)=\sum_{i\in\rho(\phi)}\#\{j:\{i,j\}\in E(G),\ r_\phi(j)\ne i\}
\]
expresses the Laplacian contribution as the number of incidences from root vertices to neighboring vertices outside the root's tree. In case A there are exactly \(2J\) such incidences: once from each of the \(J\) rooted leaves and once from the rooted hub. In case B there are exactly \(H\) such incidences, from the other rooted leaves. Consequently
\[
(R,C)=
\begin{cases}
(1+J,\ -k+(1+2/q)J),&\text{case A},\\
(1+H,\ -k+(1+1/q)H),&\text{case B}.
\end{cases}
\]
The two cases are exhaustive also at \(k=1\), with \(H=0\). By binomial first and second moments, and the stated mixing probabilities,
\[
\begin{aligned}
\mathbb EC&=0,\\
V_R:=\operatorname{Var}(R)
&=\frac{q(k-1)}{(q+1)^2}+\frac{q(k+1)}{(q+k+1)^2},\\
B:=\operatorname{Cov}(R,C)
&=\frac{k(k+2q+1)}{(q+1)(q+k+1)},\\
V_C:=\operatorname{Var}(C)
&=\frac{k(2kq+k+2q^2+4q+3)}{q(q+1)(q+k+1)}.
\end{aligned}
\]
The variance of \(R-\alpha C\) is exactly \(V_R-2\alpha B+\alpha^2 V_C\). Since \(V_C>0\), it is strictly convex in \(\alpha\), with the claimed unique minimizer \(\alpha_*=B/V_C\) and minimum \(V_R-B^2/V_C\). Direct factorization gives
\[
V_R-\frac{B^2}{V_C}
=\frac{kq(k-1)[k^2q+kq^2+kq+k-q^2+1]}{(q+1)^2(k+q+1)^2(2kq+k+2q^2+4q+3)}.
\]
For \(k=1\) this is zero. For integers \(k\ge2\), every factor in the bracket is positive because \(kq^2-q^2=(k-1)q^2\); hence the minimum is strictly positive.

**Asymptotic separation.** For \(q=Q\), \(k=Q^2\), \(Q\in\mathbb N\to\infty\), direct degree counting gives \(d_{\mathrm{av}}=2k/(k+1)\), so \(\alpha_{\mathrm{av}}\to1\), while the exact expression yields \(\alpha_*\to1/2\). Dividing the displayed moments by \(Q\) gives
\[
V_R/Q\to1,\qquad B/Q\to1,\qquad V_C/Q\to2.
\]
Inserting these limits into \(V_R-2\alpha B+\alpha^2V_C\) gives the two variance ratios \(1/2\) and \(1\). Because the optimal ratio has a strictly positive limit, their quotient tends to \(2\). No limit exchange or stochastic approximation is needed: these are limits of explicit rational functions along one integer sequence.

## Verification
The standalone \(\texttt{verify.py}\) enumerates every oriented rooted forest on stars with \(1\le k\le8\) and six positive rational parameter choices, computes the exact rational partition function and joint moments of \((R,C)\), and compares them with all displayed finite-parameter formulas. It also checks optimality against mean-degree tuning and several larger integer parameter choices. The recorded run reports \(429\) successful exact-rational assertions. Computation is confirmatory; the proof above covers all integers \(k\ge1\) and reals \(q>0\). Reproduce with \(\texttt{python3 verify.py}\); only Python standard-library modules are used.

## Relationship to prior work
Barthelmé and collaborators (2019, arXiv:1905.02086) introduced the random-forest root-count inverse-trace estimator and its general spectral variance formula; this work does **not** claim either as new. Pilavcı and collaborators (2021, arXiv:2110.07894) established general gradient-step/control-variate variance reduction and the abstract covariance-over-variance optimal coefficient, in a related graph-regularization setting. Pilavcı and collaborators (2022, arXiv:2206.07421) applied control variates to random-forest inverse-trace estimation and proposed a practical mean-degree coefficient. The contribution here is instead the **exact all-parameter star-graph covariance and coefficient**, with a rigorous explicit limiting family on which the published mean-degree rule loses its variance benefit despite a remaining factor-two improvement being achievable. General abstract variance identities alone do not specify this star-graph comparison without evaluating the joint rooted-forest distribution.

## Limitations
The star is a deliberately heterogeneous graph family, not an assertion about all sparse, irregular or random graphs. The optimal coefficient depends on the known graph size and regularization parameter; the risk analysis assumes exact forest draws, exact arithmetic and a fixed coefficient. It does not include the cost of sampling or computing the control statistic, and it does not claim runtime dominance over other estimators. It does not concern the separate partition-averaged estimator or optimal nonlinear control variates. No independent validation has been performed. Specialist precedence outside inspected sources remains possible.

## References
- S. Barthelmé, N. Tremblay, A. Gaudillière, L. Avena, P.-O. Amblard. *Estimating the inverse trace using random forests on graphs*. arXiv:1905.02086, first posted 2019-05-06. https://arxiv.org/abs/1905.02086
- Y. Pilavcı, P.-O. Amblard, S. Barthelmé, N. Tremblay. *Variance reduction in stochastic methods for large-scale regularised least-squares problems*. arXiv:2110.07894, first posted 2021-10-15. https://arxiv.org/abs/2110.07894
- Y. Y. Pilavcı, P.-O. Amblard, S. Barthelmé, N. Tremblay. *Variance Reduction for Inverse Trace Estimation via Random Spanning Forests*. arXiv:2206.07421, first posted 2022-06-15. https://arxiv.org/abs/2206.07421
